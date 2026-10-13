---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/
title: REST Resource: savedQueries \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:05.005305+00:00
---

# REST Resource: savedQueries  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  REST Resource: savedQueries Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SavedQuery
    * JSON representation
  * QueryContent
    * JSON representation
  * IamPolicyAnalysisQuery
    * JSON representation
  * ResourceSelector
    * JSON representation
  * IdentitySelector
    * JSON representation
  * AccessSelector
    * JSON representation
  * Options
    * JSON representation
  * ConditionContext
    * JSON representation
  * Methods



## Resource: SavedQuery

A saved query which can be shared with others or used later.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "creator": string,
      "lastUpdateTime": string,
      "lastUpdater": string,
      "labels": {
        string: string,
        ...
      },
      "content": {
        object ([QueryContent](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#QueryContent))
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name of the saved query. The format must be:

  * projects/projectNumber/savedQueries/savedQueryId
  * folders/folder_number/savedQueries/savedQueryId
  * organizations/organization_number/savedQueries/savedQueryId

  
`description` |  `string` The description of this saved query. This value should be fewer than 255 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of this saved query.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creator` |  `string` Output only. The account's email address who has created this saved query.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of this saved query.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdater` |  `string` Output only. The account's email address who has updated this saved query most recently.  
`labels` |  `map (key: string, value: string)` Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`content` |  `object (`[QueryContent](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#QueryContent)`)` The query content.  
  
## QueryContent

The query content.

JSON representation  
---  
      
    
    {
    
      // Union field query_content can be only one of the following:
      "iamPolicyAnalysisQuery": {
        object ([IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery))
      }
      // End of list of possible types for union field query_content.
    }  
  
Fields  
---  
Union field `query_content`.`query_content` can be only one of the following:  
`iamPolicyAnalysisQuery` |  `object (`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery)`)` An IAM Policy Analysis query, which could be used in the `[AssetService.AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#google.cloud.asset.v1.AssetService.AnalyzeIamPolicy)` RPC or the `[AssetService.AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)` RPC.  
  
## IamPolicyAnalysisQuery

IAM policy analysis query message.

JSON representation  
---  
      
    
    {
      "scope": string,
      "resourceSelector": {
        object ([ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ResourceSelector))
      },
      "identitySelector": {
        object ([IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IdentitySelector))
      },
      "accessSelector": {
        object ([AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#AccessSelector))
      },
      "options": {
        object ([Options](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#Options))
      },
      "conditionContext": {
        object ([ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ConditionContext))
      }
    }  
  
Fields  
---  
`scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).  
`resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ResourceSelector)`)` Optional. Specifies a resource for analysis.  
`identitySelector` |  `object (`[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IdentitySelector)`)` Optional. Specifies an identity for analysis.  
`accessSelector` |  `object (`[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#AccessSelector)`)` Optional. Specifies roles or permissions for analysis. This is optional.  
`options` |  `object (`[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#Options)`)` Optional. The query options.  
`conditionContext` |  `object (`[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ConditionContext)`)` Optional. The hypothetical context for IAM conditions evaluation.  
  
## ResourceSelector

Specifies the resource to analyze for access policies, which may be set directly on the resource, or on ancestors such as organizations, folders or projects.

JSON representation  
---  
      
    
    {
      "fullResourceName": string
    }  
  
Fields  
---  
`fullResourceName` |  `string` Required. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).  
  
## IdentitySelector

Specifies an identity for which to determine resource access, based on roles assigned either directly to them or to the groups they belong to, directly or indirectly.

JSON representation  
---  
      
    
    {
      "identity": string
    }  
  
Fields  
---  
`identity` |  `string` Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding).The examples of supported forms are: "user:[mike@example.com"](mailto:mike@example.com"), "group:[admins@example.com"](mailto:admins@example.com"), "domain:google.com", "serviceAccount:[my-project-id@appspot.gserviceaccount.com"](mailto:my-project-id@appspot.gserviceaccount.com").Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.  
  
## AccessSelector

Specifies roles and/or permissions to analyze, to determine both the identities possessing them and the resources they control. If multiple values are specified, results will include roles or permissions matching any of them. The total number of roles and permissions should be equal or less than 10.

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
  
## Options

Contains query options.

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
`expandGroups` |  `boolean` Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding.If `[IamPolicyAnalysisQuery.identity_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery.FIELDS.identity_selector)` is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set.If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][].Default is false.  
`expandRoles` |  `boolean` Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions.If `[IamPolicyAnalysisQuery.access_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery.FIELDS.access_selector)` is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set.Default is false.  
`expandResources` |  `boolean` Optional. If true and `[IamPolicyAnalysisQuery.resource_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery.FIELDS.resource_selector)` is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy.For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P.If true and `[IamPolicyAnalysisQuery.resource_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IamPolicyAnalysisQuery.FIELDS.resource_selector)` is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option.For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource.If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][].Default is false.  
`outputResourceEdges` |  `boolean` Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.  
`outputGroupEdges` |  `boolean` Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.  
`analyzeServiceAccountImpersonation` |  `boolean` Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use `[AssetService.AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)` RPC instead.For example, if the request analyzes for which resources user A has permission P, and there's an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there's another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `[AnalyzeIamPolicyResponse.service_account_impersonation_analysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#body.AnalyzeIamPolicyResponse.FIELDS.service_account_impersonation_analysis)`.Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there's an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there's another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `[AnalyzeIamPolicyResponse.service_account_impersonation_analysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#body.AnalyzeIamPolicyResponse.FIELDS.service_account_impersonation_analysis)`.Only the following permissions are considered in this analysis:

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.implicitDelegation`

Default is false.  
  
## ConditionContext

The IAM conditions context.

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
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/create)`

|  Creates a saved query in a parent project/folder/organization.  
  
### `[delete](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/delete)`

|  Deletes a saved query.  
  
### `[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/get)`

|  Gets details about a saved query.  
  
### `[list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/list)`

|  Lists all saved queries in a parent project/folder/organization.  
  
### `[patch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/patch)`

|  Updates a saved query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
