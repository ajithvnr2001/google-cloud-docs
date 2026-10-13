---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy/
title: MCP Tools Reference: cloudasset.googleapis.com \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:12.871514+00:00
---

# MCP Tools Reference: cloudasset.googleapis.com  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  MCP Tools Reference: cloudasset.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `analyze_iam_policy`

Analyzes Google Cloud IAM allow policies to determine who can do what on which resources. It can perform policy analysis such as finding resources accessible to a principal, finding principals with access to a resource, or checking access paths.

This tool requires the `analysis_query` parameter, which specifies the root container where policies are analyzed (`scope`) and offers optional selectors for resource names, principal identifiers, and applicable roles and permissions.

  * Folder and Organization scopes are _not_ supported. `scope` must be a project scope (`projects/PROJECT_ID`).
  * When analyzing policies in a specific project (for example, 'in `PROJECT_ID`'), set `scope` to `projects/PROJECT_ID` and do _not_ set `resource_selector`.
  * Only set `resource_selector.full_resource_name` (for example, `//storage.googleapis.com/BUCKET_NAME`) if the user specifically asks for access to a particular resource within that scope.
  * If a project scope is not specified in the request, confirm the scope before calling this tool.
  * If `execution_timeout` is not specified in the request, set `execution_timeout` to `60s` as a string with suffix 's'.



You can also provide `options` to `expand_groups`, `expand_roles`, `expand_resources` (default `false`), and `analyze_service_account_impersonation` (default `false`). For supported policy types, see <https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview#supported-policy-types>. For BYOID support, see <https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#policy-intelligence>.

The following code sample shows how to use `curl` to call the `analyze_iam_policy` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudasset.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "analyze_iam_policy",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

A request message for `AssetService.AnalyzeIamPolicy`.

### AnalyzeIamPolicyRequest

JSON representation  
---  
      
    
    {
      "analysisQuery": {
        object ([IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IamPolicyAnalysisQuery))
      },
      "savedAnalysisQuery": string,
      "executionTimeout": string
    }  
  
Fields  
---  
`analysisQuery` |  `object (`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IamPolicyAnalysisQuery)`)` Required. The request query.  
`savedAnalysisQuery` |  `string` Optional. The name of a saved query, which must be in the format of `projects/project_number/savedQueries/saved_query_id`.  If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page.Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.  
`executionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json).If this field is set with a value less than the RPC deadline, and the execution of your query hasn't finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query's execution will continue until the RPC deadline. If it's not finished until then, you will get a DEADLINE_EXCEEDED error.Default is empty.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### IamPolicyAnalysisQuery

JSON representation  
---  
      
    
    {
      "scope": string,
      "resourceSelector": {
        object ([ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ResourceSelector))
      },
      "identitySelector": {
        object ([IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IdentitySelector))
      },
      "accessSelector": {
        object ([AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.AccessSelector))
      },
      "options": {
        object ([Options](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.Options))
      },
      "conditionContext": {
        object ([ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ConditionContext))
      }
    }  
  
Fields  
---  
`scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be a project ID (such as "projects/my-project-id") or a project number (such as "projects/12345").To know how to get a folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).  
`resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ResourceSelector)`)` Optional. Specifies a resource for analysis.  
`identitySelector` |  `object (`[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IdentitySelector)`)` Optional. Specifies an identity for analysis.  
`accessSelector` |  `object (`[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.AccessSelector)`)` Optional. Specifies roles or permissions for analysis. This is optional.  
`options` |  `object (`[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.Options)`)` Optional. The query options.  
`conditionContext` |  `object (`[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ConditionContext)`)` Optional. The hypothetical context for IAM conditions evaluation.  
  
### ResourceSelector

JSON representation  
---  
      
    
    {
      "fullResourceName": string
    }  
  
Fields  
---  
`fullResourceName` |  `string` Required. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).  
  
### IdentitySelector

JSON representation  
---  
      
    
    {
      "identity": string
    }  
  
Fields  
---  
`identity` |  `string` Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding).The examples of supported forms are: "user:[mike@example.com"](mailto:mike@example.com"), "group:[admins@example.com"](mailto:admins@example.com"), "domain:google.com", "serviceAccount:[my-project-id@appspot.gserviceaccount.com"](mailto:my-project-id@appspot.gserviceaccount.com").Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.  
  
### AccessSelector

JSON representation  
---  
      
    
    {
      "roles": [
        string
      ],
      "permissions": [
        string
      ]
    }  
  
Fields  
---  
`roles[]` |  `string` Optional. The roles to appear in result.  
`permissions[]` |  `string` Optional. The permissions to appear in result.  
  
### Options

JSON representation  
---  
      
    
    {
      "expandGroups": boolean,
      "expandRoles": boolean,
      "expandResources": boolean,
      "outputResourceEdges": boolean,
      "outputGroupEdges": boolean,
      "analyzeServiceAccountImpersonation": boolean
    }  
  
Fields  
---  
`expandGroups` |  `boolean` Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding.If `IamPolicyAnalysisQuery.identity_selector` is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set.If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][].Default is false.  
`expandRoles` |  `boolean` Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions.If `IamPolicyAnalysisQuery.access_selector` is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set.Default is false.  
`expandResources` |  `boolean` Optional. If true and `IamPolicyAnalysisQuery.resource_selector` is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy.For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P.If true and `IamPolicyAnalysisQuery.resource_selector` is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option.For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource.If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][].Default is false.  
`outputResourceEdges` |  `boolean` Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.  
`outputGroupEdges` |  `boolean` Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.  
`analyzeServiceAccountImpersonation` |  `boolean` Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use `AssetService.AnalyzeIamPolicyLongrunning` RPC instead.For example, if the request analyzes for which resources user A has permission P, and there's an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there's another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `AnalyzeIamPolicyResponse.service_account_impersonation_analysis`.Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there's an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there's another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `AnalyzeIamPolicyResponse.service_account_impersonation_analysis`.Only the following permissions are considered in this analysis:

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.implicitDelegation`

Default is false.  
  
### ConditionContext

JSON representation  
---  
      
    
    {
    
      // Union field TimeContext can be only one of the following:
      "accessTime": string
      // End of list of possible types for union field TimeContext.
    }  
  
Fields  
---  
Union field `TimeContext`. The IAM conditions time context. `TimeContext` can be only one of the following:  
`accessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
## Output Schema

A response message for `AssetService.AnalyzeIamPolicy`.

### AnalyzeIamPolicyResponse

JSON representation  
---  
      
    
    {
      "mainAnalysis": {
        object ([IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysis))
      },
      "serviceAccountImpersonationAnalysis": [
        {
          object ([IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysis))
        }
      ],
      "fullyExplored": boolean
    }  
  
Fields  
---  
`mainAnalysis` |  `object (`[IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysis)`)` The main analysis that matches the original request.  
`serviceAccountImpersonationAnalysis[]` |  `object (`[IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysis)`)` The service account impersonation analysis if `IamPolicyAnalysisQuery.Options.analyze_service_account_impersonation` is enabled.  
`fullyExplored` |  `boolean` Represents whether all entries in the `main_analysis` and `service_account_impersonation_analysis` have been fully explored to answer the query in the request.  
  
### IamPolicyAnalysis

JSON representation  
---  
      
    
    {
      "analysisQuery": {
        object ([IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IamPolicyAnalysisQuery))
      },
      "analysisResults": [
        {
          object ([IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisResult))
        }
      ],
      "fullyExplored": boolean,
      "nonCriticalErrors": [
        {
          object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState))
        }
      ]
    }  
  
Fields  
---  
`analysisQuery` |  `object (`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IamPolicyAnalysisQuery)`)` The analysis query.  
`analysisResults[]` |  `object (`[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisResult)`)` A list of `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisResult)` that matches the analysis query, or empty if no result is found.  
`fullyExplored` |  `boolean` Represents whether all entries in the `analysis_results` have been fully explored to answer the query.  
`nonCriticalErrors[]` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState)`)` A list of non-critical errors happened during the query handling.  
  
### IamPolicyAnalysisQuery

JSON representation  
---  
      
    
    {
      "scope": string,
      "resourceSelector": {
        object ([ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ResourceSelector))
      },
      "identitySelector": {
        object ([IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IdentitySelector))
      },
      "accessSelector": {
        object ([AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.AccessSelector))
      },
      "options": {
        object ([Options](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.Options))
      },
      "conditionContext": {
        object ([ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ConditionContext))
      }
    }  
  
Fields  
---  
`scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be a project ID (such as "projects/my-project-id") or a project number (such as "projects/12345").To know how to get a project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).  
`resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ResourceSelector)`)` Optional. Specifies a resource for analysis.  
`identitySelector` |  `object (`[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IdentitySelector)`)` Optional. Specifies an identity for analysis.  
`accessSelector` |  `object (`[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.AccessSelector)`)` Optional. Specifies roles or permissions for analysis. This is optional.  
`options` |  `object (`[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.Options)`)` Optional. The query options.  
`conditionContext` |  `object (`[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ConditionContext)`)` Optional. The hypothetical context for IAM conditions evaluation.  
  
### ResourceSelector

JSON representation  
---  
      
    
    {
      "fullResourceName": string
    }  
  
Fields  
---  
`fullResourceName` |  `string` Required. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).  
  
### IdentitySelector

JSON representation  
---  
      
    
    {
      "identity": string
    }  
  
Fields  
---  
`identity` |  `string` Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding).The examples of supported forms are: "user:[mike@example.com"](mailto:mike@example.com"), "group:[admins@example.com"](mailto:admins@example.com"), "domain:google.com", "serviceAccount:[my-project-id@appspot.gserviceaccount.com"](mailto:my-project-id@appspot.gserviceaccount.com").Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.  
  
### AccessSelector

JSON representation  
---  
      
    
    {
      "roles": [
        string
      ],
      "permissions": [
        string
      ]
    }  
  
Fields  
---  
`roles[]` |  `string` Optional. The roles to appear in result.  
`permissions[]` |  `string` Optional. The permissions to appear in result.  
  
### Options

JSON representation  
---  
      
    
    {
      "expandGroups": boolean,
      "expandRoles": boolean,
      "expandResources": boolean,
      "outputResourceEdges": boolean,
      "outputGroupEdges": boolean,
      "analyzeServiceAccountImpersonation": boolean
    }  
  
Fields  
---  
`expandGroups` |  `boolean` Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding.If `IamPolicyAnalysisQuery.identity_selector` is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set.If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][].Default is false.  
`expandRoles` |  `boolean` Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions.If `IamPolicyAnalysisQuery.access_selector` is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set.Default is false.  
`expandResources` |  `boolean` Optional. If true and `IamPolicyAnalysisQuery.resource_selector` is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy.For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P.If true and `IamPolicyAnalysisQuery.resource_selector` is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option.For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource.If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][].Default is false.  
`outputResourceEdges` |  `boolean` Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.  
`outputGroupEdges` |  `boolean` Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.  
`analyzeServiceAccountImpersonation` |  `boolean` Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use `AssetService.AnalyzeIamPolicyLongrunning` RPC instead.For example, if the request analyzes for which resources user A has permission P, and there's an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there's another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `AnalyzeIamPolicyResponse.service_account_impersonation_analysis`.Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there's an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there's another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `AnalyzeIamPolicyResponse.service_account_impersonation_analysis`.Only the following permissions are considered in this analysis:

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.implicitDelegation`

Default is false.  
  
### ConditionContext

JSON representation  
---  
      
    
    {
    
      // Union field TimeContext can be only one of the following:
      "accessTime": string
      // End of list of possible types for union field TimeContext.
    }  
  
Fields  
---  
Union field `TimeContext`. The IAM conditions time context. `TimeContext` can be only one of the following:  
`accessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### IamPolicyAnalysisResult

JSON representation  
---  
      
    
    {
      "attachedResourceFullName": string,
      "iamBinding": {
        object ([Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Binding))
      },
      "accessControlLists": [
        {
          object ([AccessControlList](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.AccessControlList))
        }
      ],
      "identityList": {
        object ([IdentityList](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IdentityList))
      },
      "fullyExplored": boolean
    }  
  
Fields  
---  
`attachedResourceFullName` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource to which the `iam_binding` policy attaches.  
`iamBinding` |  `object (`[Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Binding)`)` The IAM policy binding under analysis.  
`accessControlLists[]` |  `object (`[AccessControlList](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.AccessControlList)`)` The access control lists derived from the `iam_binding` that match or potentially match resource and access selectors specified in the request.  
`identityList` |  `object (`[IdentityList](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IdentityList)`)` The identity list derived from members of the `iam_binding` that match or potentially match identity selector specified in the request.  
`fullyExplored` |  `boolean` Represents whether all analyses on the `iam_binding` have successfully finished.  
  
### Binding

JSON representation  
---  
      
    
    {
      "role": string,
      "members": [
        string
      ],
      "condition": {
        object ([Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Expr))
      }
    }  
  
Fields  
---  
`role` |  `string` Role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`.For an overview of the IAM roles and permissions, see the [IAM documentation](https://cloud.google.com/iam/docs/roles-overview). For a list of the available pre-defined roles, see [here](https://cloud.google.com/iam/docs/understanding-roles).  
`members[]` |  `string` Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values:

  * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.
  * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account. Does not include identities that come from external identity providers (IdPs) through identity federation.
  * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .


  * `serviceAccount:{emailid}`: An email address that represents a Google service account. For example, `my-other-app@appspot.gserviceaccount.com`.
  * `serviceAccount:{projectid}.svc.id.goog[{namespace}/{kubernetes-sa}]`: An identifier for a [Kubernetes service account](https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts). For example, `my-project.svc.id.goog[my-namespace/my-kubernetes-sa]`.
  * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.


  * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.


  * `principal://iam.googleapis.com/locations/global/workforcePools/{pool_id}/subject/{subject_attribute_value}`: A single identity in a workforce identity pool.
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/group/{group_id}`: All workforce identities in a group.
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/attribute.{attribute_name}/{attribute_value}`: All workforce identities with a specific attribute value.
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/*`: All identities in a workforce identity pool.
  * `principal://iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/subject/{subject_attribute_value}`: A single identity in a workload identity pool.
  * `principalSet://iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/group/{group_id}`: A workload identity pool group.
  * `principalSet://iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/attribute.{attribute_name}/{attribute_value}`: All identities in a workload identity pool with a certain attribute.
  * `principalSet://iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/*`: All identities in a workload identity pool.
  * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.
  * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.
  * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.
  * `deleted:principal://iam.googleapis.com/locations/global/workforcePools/{pool_id}/subject/{subject_attribute_value}`: Deleted single identity in a workforce identity pool. For example, `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-pool-id/subject/my-subject-attribute-value`.

  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Expr)`)` The condition that is associated with this binding.If the condition evaluates to `true`, then this binding applies to the current request.If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the principals in this binding.To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).  
  
### Expr

JSON representation  
---  
      
    
    {
      "expression": string,
      "title": string,
      "description": string,
      "location": string
    }  
  
Fields  
---  
`expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
  
### AccessControlList

JSON representation  
---  
      
    
    {
      "resources": [
        {
          object ([Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Resource))
        }
      ],
      "accesses": [
        {
          object ([Access](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Access))
        }
      ],
      "resourceEdges": [
        {
          object ([Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Edge))
        }
      ],
      "conditionEvaluation": {
        object ([ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.ConditionEvaluation))
      }
    }  
  
Fields  
---  
`resources[]` |  `object (`[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Resource)`)` The resources that match one of the following conditions: - The resource_selector, if it is specified in request; - Otherwise, resources reachable from the policy attached resource.  
`accesses[]` |  `object (`[Access](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Access)`)` The accesses that match one of the following conditions: - The access_selector, if it is specified in request; - Otherwise, access specifiers reachable from the policy binding's role.  
`resourceEdges[]` |  `object (`[Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Edge)`)` Resource edges of the graph starting from the policy attached resource to any descendant resources. The `Edge.source_node` contains the full resource name of a parent resource and `Edge.target_node` contains the full resource name of a child resource. This field is present only if the output_resource_edges option is enabled in request.  
`conditionEvaluation` |  `object (`[ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.ConditionEvaluation)`)` Condition evaluation for this AccessControlList, if there is a condition defined in the above IAM policy binding.  
  
### Resource

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
      "analysisState": {
        object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState))
      }
    }  
  
Fields  
---  
`fullResourceName` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format)  
`analysisState` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState)`)` The analysis state of this resource.  
  
### IamPolicyAnalysisState

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Code)),
      "cause": string
    }  
  
Fields  
---  
`code` |  `enum (`[Code](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Code)`)` The Google standard error code that best describes the state. For example: - OK means the analysis on this entity has been successfully finished; - PERMISSION_DENIED means an access denied error is encountered; - DEADLINE_EXCEEDED means the analysis on this entity hasn't been started in time;  
`cause` |  `string` The human-readable description of the cause of failure.  
  
### Access

JSON representation  
---  
      
    
    {
      "analysisState": {
        object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState))
      },
    
      // Union field oneof_access can be only one of the following:
      "role": string,
      "permission": string
      // End of list of possible types for union field oneof_access.
    }  
  
Fields  
---  
`analysisState` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState)`)` The analysis state of this access.  
Union field `oneof_access`.`oneof_access` can be only one of the following:  
`role` |  `string` The role.  
`permission` |  `string` The permission.  
  
### Edge

JSON representation  
---  
      
    
    {
      "sourceNode": string,
      "targetNode": string
    }  
  
Fields  
---  
`sourceNode` |  `string` The source node of the edge. For example, it could be a full resource name for a resource node or an email of an identity.  
`targetNode` |  `string` The target node of the edge. For example, it could be a full resource name for a resource node or an email of an identity.  
  
### ConditionEvaluation

JSON representation  
---  
      
    
    {
      "evaluationValue": enum ([EvaluationValue](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.EvaluationValue))
    }  
  
Fields  
---  
`evaluationValue` |  `enum (`[EvaluationValue](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.EvaluationValue)`)` The evaluation result.  
  
### IdentityList

JSON representation  
---  
      
    
    {
      "identities": [
        {
          object ([Identity](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Identity))
        }
      ],
      "groupEdges": [
        {
          object ([Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Edge))
        }
      ]
    }  
  
Fields  
---  
`identities[]` |  `object (`[Identity](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Identity)`)` Only the identities that match one of the following conditions will be presented: - The identity_selector, if it is specified in request; - Otherwise, identities reachable from the policy binding's members.  
`groupEdges[]` |  `object (`[Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Edge)`)` Group identity edges of the graph starting from the binding's group members to any node of the `identities`. The `Edge.source_node` contains a group, such as `group:parent@google.com`. The `Edge.target_node` contains a member of the group, such as `group:child@google.com` or `user:foo@google.com`. This field is present only if the output_group_edges option is enabled in request.  
  
### Identity

JSON representation  
---  
      
    
    {
      "name": string,
      "analysisState": {
        object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState))
      }
    }  
  
Fields  
---  
`name` |  `string` The identity of members, formatted as appear in an [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). For example, they might be formatted like the following:

  * user:[foo@google.com](mailto:foo@google.com)
  * group:[group1@google.com](mailto:group1@google.com)
  * serviceAccount:[s1@prj1.iam.gserviceaccount.com](mailto:s1@prj1.iam.gserviceaccount.com)
  * projectOwner:some_project_id
  * domain:google.com
  * allUsers

  
`analysisState` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisState)`)` The analysis state of this identity.  
  
### Code

The canonical error codes for gRPC APIs.

Sometimes multiple error codes may apply. Services should return the most specific error code that applies. For example, prefer `OUT_OF_RANGE` over `FAILED_PRECONDITION` if both codes apply. Similarly prefer `NOT_FOUND` or `ALREADY_EXISTS` over `FAILED_PRECONDITION`.

Enums  
---  
`OK` | Not an error; returned on success.HTTP Mapping: 200 OK  
`CANCELLED` | The operation was cancelled, typically by the caller.HTTP Mapping: 499 Client Closed Request  
`UNKNOWN` | Unknown error. For example, this error may be returned when a `Status` value received from another address space belongs to an error space that is not known in this address space. Also errors raised by APIs that do not return enough error information may be converted to this error.HTTP Mapping: 500 Internal Server Error  
`INVALID_ARGUMENT` | The client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (e.g., a malformed file name).HTTP Mapping: 400 Bad Request  
`DEADLINE_EXCEEDED` | The deadline expired before the operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.HTTP Mapping: 504 Gateway Timeout  
`NOT_FOUND` | Some requested entity (e.g., file or directory) was not found.Note to server developers: if a request is denied for an entire class of users, such as gradual feature rollout or undocumented allowlist, `NOT_FOUND` may be used. If a request is denied for some users within a class of users, such as user-based access control, `PERMISSION_DENIED` must be used.HTTP Mapping: 404 Not Found  
`ALREADY_EXISTS` | The entity that a client attempted to create (e.g., file or directory) already exists.HTTP Mapping: 409 Conflict  
`PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. `PERMISSION_DENIED` must not be used for rejections caused by exhausting some resource (use `RESOURCE_EXHAUSTED` instead for those errors). `PERMISSION_DENIED` must not be used if the caller can not be identified (use `UNAUTHENTICATED` instead for those errors). This error code does not imply the request is valid or the requested entity exists or satisfies other pre-conditions.HTTP Mapping: 403 Forbidden  
`UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation.HTTP Mapping: 401 Unauthorized  
`RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.HTTP Mapping: 429 Too Many Requests  
`FAILED_PRECONDITION` | The operation was rejected because the system is not in a state required for the operation's execution. For example, the directory to be deleted is non-empty, an rmdir operation is applied to a non-directory, etc.Service implementors can use the following guidelines to decide between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`: (a) Use `UNAVAILABLE` if the client can retry just the failing call. (b) Use `ABORTED` if the client should retry at a higher level. For example, when a client-specified test-and-set fails, indicating the client should restart a read-modify-write sequence. (c) Use `FAILED_PRECONDITION` if the client should not retry until the system state has been explicitly fixed. For example, if an "rmdir" fails because the directory is non-empty, `FAILED_PRECONDITION` should be returned since the client should not retry unless the files are deleted from the directory.HTTP Mapping: 400 Bad Request  
`ABORTED` | The operation was aborted, typically due to a concurrency issue such as a sequencer check failure or transaction abort.See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.HTTP Mapping: 409 Conflict  
`OUT_OF_RANGE` | The operation was attempted past the valid range. E.g., seeking or reading past end-of-file.Unlike `INVALID_ARGUMENT`, this error indicates a problem that may be fixed if the system state changes. For example, a 32-bit file system will generate `INVALID_ARGUMENT` if asked to read at an offset that is not in the range [0,2^32-1], but it will generate `OUT_OF_RANGE` if asked to read from an offset past the current file size.There is a fair bit of overlap between `FAILED_PRECONDITION` and `OUT_OF_RANGE`. We recommend using `OUT_OF_RANGE` (the more specific error) when it applies so that callers who are iterating through a space can easily look for an `OUT_OF_RANGE` error to detect when they are done.HTTP Mapping: 400 Bad Request  
`UNIMPLEMENTED` | The operation is not implemented or is not supported/enabled in this service.HTTP Mapping: 501 Not Implemented  
`INTERNAL` | Internal errors. This means that some invariants expected by the underlying system have been broken. This error code is reserved for serious errors.HTTP Mapping: 500 Internal Server Error  
`UNAVAILABLE` | The service is currently unavailable. This is most likely a transient condition, which can be corrected by retrying with a backoff. Note that it is not always safe to retry non-idempotent operations.See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.HTTP Mapping: 503 Service Unavailable  
`DATA_LOSS` | Unrecoverable data loss or corruption.HTTP Mapping: 500 Internal Server Error  
  
### EvaluationValue

Value of this expression.

Enums  
---  
`EVALUATION_VALUE_UNSPECIFIED` | Reserved for future use.  
`TRUE` | The evaluation result is `true`.  
`FALSE` | The evaluation result is `false`.  
`CONDITIONAL` | The evaluation result is `conditional` when the condition expression contains variables that are either missing input values or have not been supported by Policy Analyzer yet.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
