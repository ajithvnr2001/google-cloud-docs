---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy/
title: Method: analyzeIamPolicy \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.053302+00:00
---

# Method: analyzeIamPolicy  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: analyzeIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IamPolicyAnalysis
    * JSON representation
  * IamPolicyAnalysisResult
    * JSON representation
  * AccessControlList
    * JSON representation
  * Resource
    * JSON representation
  * IamPolicyAnalysisState
    * JSON representation
  * Code
  * Access
    * JSON representation
  * Edge
    * JSON representation
  * IdentityList
    * JSON representation
  * Identity
    * JSON representation
  * Try it!



Analyzes IAM policies to answer which identities have what accesses on which resources.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{analysisQuery.scope=*/*}:analyzeIamPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`analysisQuery.scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.analyzeIamPolicy`
  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`

  
  
### Query parameters

Parameters  
---  
`analysisQuery.resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ResourceSelector)`)` Optional. Specifies a resource for analysis.  
`analysisQuery.identitySelector` |  `object (`[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IdentitySelector)`)` Optional. Specifies an identity for analysis.  
`analysisQuery.accessSelector` |  `object (`[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#AccessSelector)`)` Optional. Specifies roles or permissions for analysis. This is optional.  
`analysisQuery.options` |  `object (`[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#Options)`)` Optional. The query options.  
`analysisQuery.conditionContext` |  `object (`[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ConditionContext)`)` Optional. The hypothetical context for IAM conditions evaluation.  
`savedAnalysisQuery` |  `string` Optional. The name of a saved query, which must be in the format of:

  * projects/projectNumber/savedQueries/savedQueryId
  * folders/folder_number/savedQueries/savedQueryId
  * organizations/organization_number/savedQueries/savedQueryId

If both `analysisQuery` and `savedAnalysisQuery` are provided, they will be merged together with the `savedAnalysisQuery` as base and the `analysisQuery` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page.Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.  
`executionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json).If this field is set with a value less than the RPC deadline, and the execution of your query hasn't finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query's execution will continue until the RPC deadline. If it's not finished until then, you will get a DEADLINE_EXCEEDED error.Default is empty.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Request body

The request body must be empty.

### Response body

A response message for `[AssetService.AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#google.cloud.asset.v1.AssetService.AnalyzeIamPolicy)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mainAnalysis": {
        object ([IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysis))
      },
      "serviceAccountImpersonationAnalysis": [
        {
          object ([IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysis))
        }
      ],
      "fullyExplored": boolean
    }  
  
Fields  
---  
`mainAnalysis` |  `object (`[IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysis)`)` The main analysis that matches the original request.  
`serviceAccountImpersonationAnalysis[]` |  `object (`[IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysis)`)` The service account impersonation analysis if `[IamPolicyAnalysisQuery.Options.analyze_service_account_impersonation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#Options.FIELDS.analyze_service_account_impersonation)` is enabled.  
`fullyExplored` |  `boolean` Represents whether all entries in the `[mainAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#body.AnalyzeIamPolicyResponse.FIELDS.main_analysis)` and `[serviceAccountImpersonationAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#body.AnalyzeIamPolicyResponse.FIELDS.service_account_impersonation_analysis)` have been fully explored to answer the query in the request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## IamPolicyAnalysis

An analysis message to group the query and results.

JSON representation  
---  
      
    
    {
      "analysisQuery": {
        object ([IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery))
      },
      "analysisResults": [
        {
          object ([IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult))
        }
      ],
      "fullyExplored": boolean,
      "nonCriticalErrors": [
        {
          object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState))
        }
      ]
    }  
  
Fields  
---  
`analysisQuery` |  `object (`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery)`)` The analysis query.  
`analysisResults[]` |  `object (`[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult)`)` A list of `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult)` that matches the analysis query, or empty if no result is found.  
`fullyExplored` |  `boolean` Represents whether all entries in the `[analysisResults](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysis.FIELDS.analysis_results)` have been fully explored to answer the query.  
`nonCriticalErrors[]` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState)`)` A list of non-critical errors happened during the query handling.  
  
## IamPolicyAnalysisResult

IAM Policy analysis result, consisting of one IAM policy binding and derived access control lists.

JSON representation  
---  
      
    
    {
      "attachedResourceFullName": string,
      "iamBinding": {
        object ([Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding))
      },
      "accessControlLists": [
        {
          object ([AccessControlList](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#AccessControlList))
        }
      ],
      "identityList": {
        object ([IdentityList](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IdentityList))
      },
      "fullyExplored": boolean
    }  
  
Fields  
---  
`attachedResourceFullName` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource to which the `[iamBinding](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult.FIELDS.iam_binding)` policy attaches.  
`iamBinding` |  `object (`[Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding)`)` The IAM policy binding under analysis.  
`accessControlLists[]` |  `object (`[AccessControlList](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#AccessControlList)`)` The access control lists derived from the `[iamBinding](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult.FIELDS.iam_binding)` that match or potentially match resource and access selectors specified in the request.  
`identityList` |  `object (`[IdentityList](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IdentityList)`)` The identity list derived from members of the `[iamBinding](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult.FIELDS.iam_binding)` that match or potentially match identity selector specified in the request.  
`fullyExplored` |  `boolean` Represents whether all analyses on the `[iamBinding](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult.FIELDS.iam_binding)` have successfully finished.  
  
## AccessControlList

An access control list, derived from the above IAM policy binding, which contains a set of resources and accesses. May include one item from each set to compose an access control entry.

NOTICE that there could be multiple access control lists for one IAM policy binding. The access control lists are created based on resource and access combinations.

For example, assume we have the following cases in one IAM policy binding: - Permission P1 and P2 apply to resource R1 and R2; - Permission P3 applies to resource R2 and R3;

This will result in the following access control lists: - AccessControlList 1: [R1, R2], [P1, P2] - AccessControlList 2: [R2, R3], [P3]

JSON representation  
---  
      
    
    {
      "resources": [
        {
          object ([Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Resource))
        }
      ],
      "accesses": [
        {
          object ([Access](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Access))
        }
      ],
      "resourceEdges": [
        {
          object ([Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge))
        }
      ],
      "conditionEvaluation": {
        object ([ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation))
      }
    }  
  
Fields  
---  
`resources[]` |  `object (`[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Resource)`)` The resources that match one of the following conditions: - The resourceSelector, if it is specified in request; - Otherwise, resources reachable from the policy attached resource.  
`accesses[]` |  `object (`[Access](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Access)`)` The accesses that match one of the following conditions: - The accessSelector, if it is specified in request; - Otherwise, access specifiers reachable from the policy binding's role.  
`resourceEdges[]` |  `object (`[Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge)`)` Resource edges of the graph starting from the policy attached resource to any descendant resources. The `[Edge.source_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge.FIELDS.source_node)` contains the full resource name of a parent resource and `[Edge.target_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge.FIELDS.target_node)` contains the full resource name of a child resource. This field is present only if the outputResourceEdges option is enabled in request.  
`conditionEvaluation` |  `object (`[ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation)`)` Condition evaluation for this AccessControlList, if there is a condition defined in the above IAM policy binding.  
  
## Resource

A Google Cloud resource under analysis.

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
      "analysisState": {
        object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState))
      }
    }  
  
Fields  
---  
`fullResourceName` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format)  
`analysisState` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState)`)` The analysis state of this resource.  
  
## IamPolicyAnalysisState

Represents the detailed state of an entity under analysis, such as a resource, an identity or an access.

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Code)),
      "cause": string
    }  
  
Fields  
---  
`code` |  `enum (`[Code](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Code)`)` The Google standard error code that best describes the state. For example: - OK means the analysis on this entity has been successfully finished; - PERMISSION_DENIED means an access denied error is encountered; - DEADLINE_EXCEEDED means the analysis on this entity hasn't been started in time;  
`cause` |  `string` The human-readable description of the cause of failure.  
  
## Code

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
  
## Access

An IAM role or permission under analysis.

JSON representation  
---  
      
    
    {
      "analysisState": {
        object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState))
      },
    
      // Union field oneof_access can be only one of the following:
      "role": string,
      "permission": string
      // End of list of possible types for union field oneof_access.
    }  
  
Fields  
---  
`analysisState` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState)`)` The analysis state of this access.  
Union field `oneof_access`.`oneof_access` can be only one of the following:  
`role` |  `string` The role.  
`permission` |  `string` The permission.  
  
## Edge

A directional edge.

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
  
## IdentityList

The identities and group edges.

JSON representation  
---  
      
    
    {
      "identities": [
        {
          object ([Identity](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Identity))
        }
      ],
      "groupEdges": [
        {
          object ([Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge))
        }
      ]
    }  
  
Fields  
---  
`identities[]` |  `object (`[Identity](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Identity)`)` Only the identities that match one of the following conditions will be presented: - The identitySelector, if it is specified in request; - Otherwise, identities reachable from the policy binding's members.  
`groupEdges[]` |  `object (`[Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge)`)` Group identity edges of the graph starting from the binding's group members to any node of the `[identities](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IdentityList.FIELDS.identities)`. The `[Edge.source_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge.FIELDS.source_node)` contains a group, such as `group:parent@google.com`. The `[Edge.target_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#Edge.FIELDS.target_node)` contains a member of the group, such as `group:child@google.com` or `user:foo@google.com`. This field is present only if the outputGroupEdges option is enabled in request.  
  
## Identity

An identity under analysis.

JSON representation  
---  
      
    
    {
      "name": string,
      "analysisState": {
        object ([IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState))
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

  
`analysisState` |  `object (`[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisState)`)` The analysis state of this identity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
