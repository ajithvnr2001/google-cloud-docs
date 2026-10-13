---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets/
title: MCP Tools Reference: cloudasset.googleapis.com \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:12.481924+00:00
---

# MCP Tools Reference: cloudasset.googleapis.com  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  MCP Tools Reference: cloudasset.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_assets`

List assets from Cloud Asset Inventory

The following code sample shows how to use `curl` to call the `list_assets` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudasset.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_assets",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

ListAssets request.

### ListAssetsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "readTime": string,
      "assetTypes": [
        string
      ],
      "contentType": enum ([ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Input.Schema.ContentType)),
      "pageSize": integer,
      "pageToken": string,
      "relationshipTypes": [
        string
      ]
    }  
  
Fields  
---  
`parent` |  `string` Required. Name of the project the assets belong to. Format: "projects/[project-id]" (such as "projects/my-project-id") or "projects/[project-number]" (such as "projects/12345"). Folders and organizations aren't supported.  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assetTypes[]` |  `string` A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".Regular expression is also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Input.Schema.ContentType)`)` Asset content type. If not specified, no content but the asset name will be returned.  
`pageSize` |  `integer` The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000.  
`pageToken` |  `string` The `next_page_token` returned from the previous `ListAssetsResponse`, or unspecified for the first `ListAssetsRequest`. It is a continuation of a prior `ListAssets` call, and the API should return the next page of assets.  
`relationshipTypes[]` |  `string` A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. * If specified: it snapshots specified relationships. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_types] or if any of the [asset_types] doesn't belong to the source types of the [relationship_types]. * Otherwise: it snapshots the supported relationships for all [asset_types] or returns an error if any of the [asset_types] has no relationship support. An unspecified asset types field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
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
  
### ContentType

Asset content type.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | Unspecified content type.  
`RESOURCE` | Resource metadata.  
`IAM_POLICY` | The actual IAM policy set on a resource.  
`ORG_POLICY` | The organization policy set on an asset.  
`ACCESS_POLICY` | The Access Context Manager policy set on an asset.  
`OS_INVENTORY` | The runtime OS Inventory information.  
`RELATIONSHIP` | The related resources.  
  
## Output Schema

ListAssets response.

### ListAssetsResponse

JSON representation  
---  
      
    
    {
      "readTime": string,
      "assets": [
        {
          object ([Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Asset))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the snapshot was taken.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assets[]` |  `object (`[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Asset)`)` Assets.  
`nextPageToken` |  `string` Token to retrieve the next page of results. It expires 72 hours after the page token for the first page is generated. Set to empty if there are no remaining results.  
  
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
  
### Asset

JSON representation  
---  
      
    
    {
      "updateTime": string,
      "name": string,
      "assetType": string,
      "resource": {
        object ([Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Resource))
      },
      "iamPolicy": {
        object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Policy))
      },
      "orgPolicy": [
        {
          object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Policy_1))
        }
      ],
      "osInventory": {
        object ([Inventory](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Inventory))
      },
      "relatedAssets": {
        object ([RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelatedAssets))
      },
      "relatedAsset": {
        object ([RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelatedAsset))
      },
      "ancestors": [
        string
      ],
      "assetExceptions": [
        {
          object ([AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AssetException))
        }
      ],
    
      // Union field access_context_policy can be only one of the following:
      "accessPolicy": {
        object ([AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessPolicy))
      },
      "accessLevel": {
        object ([AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel))
      },
      "servicePerimeter": {
        object ([ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter))
      }
      // End of list of possible types for union field access_context_policy.
    }  
  
Fields  
---  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`name` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`assetType` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Resource)`)` A representation of the resource.  
`iamPolicy` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Policy)`)` A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.  
`orgPolicy[]` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Policy_1)`)` A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.  
`osInventory` |  `object (`[Inventory](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Inventory)`)` A representation of runtime OS Inventory information. See [this topic](https://cloud.google.com/compute/docs/instances/os-inventory-management) for more information.  
`relatedAssets  
**(deprecated)**` |  `object (`[RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelatedAssets)`)` This item is deprecated!DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.  
`relatedAsset` |  `object (`[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelatedAsset)`)` One related asset of the current asset.  
`ancestors[]` |  `string` The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
`assetExceptions[]` |  `object (`[AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AssetException)`)` The exceptions of a resource.  
Union field `access_context_policy`. A representation of an [access policy](https://cloud.google.com/access-context-manager/docs/overview#access-policies). `access_context_policy` can be only one of the following:  
`accessPolicy` |  `object (`[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessPolicy)`)` Also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).  
`accessLevel` |  `object (`[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel)`)` Also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).  
`servicePerimeter` |  `object (`[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)`)` Also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).  
  
### Resource

JSON representation  
---  
      
    
    {
      "version": string,
      "discoveryDocumentUri": string,
      "discoveryName": string,
      "resourceUrl": string,
      "parent": string,
      "data": {
        object
      },
      "location": string
    }  
  
Fields  
---  
`version` |  `string` The API version. Example: `v1`  
`discoveryDocumentUri` |  `string` The URL of the discovery document containing the resource's JSON schema. Example: `https://www.googleapis.com/discovery/v1/apis/compute/v1/rest`This value is unspecified for resources that do not have an API based on a discovery document, such as Cloud Bigtable.  
`discoveryName` |  `string` The JSON schema name listed in the discovery document. Example: `Project`This value is unspecified for resources that do not have an API based on a discovery document, such as Cloud Bigtable.  
`resourceUrl` |  `string` The REST URL for accessing the resource. An HTTP `GET` request using this URL returns the resource itself. Example: `https://cloudresourcemanager.googleapis.com/v1/projects/my-project-123`This value is unspecified for resources without a REST API.  
`parent` |  `string` The full name of the immediate parent of this resource. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.For Google Cloud assets, this value is the parent resource defined in the [IAM policy hierarchy](https://cloud.google.com/iam/docs/overview#policy_hierarchy). Example: `//cloudresourcemanager.googleapis.com/projects/my_project_123`  
`data` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The content of the resource, in which some sensitive fields are removed and may not be present.  
`location` |  `string` The location of the resource in Google Cloud, such as its zone and region. For more information, see <https://cloud.google.com/about/locations/>.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### Policy

JSON representation  
---  
      
    
    {
      "version": integer,
      "bindings": [
        {
          object ([Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Binding))
        }
      ],
      "auditConfigs": [
        {
          object ([AuditConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AuditConfig))
        }
      ],
      "etag": string
    }  
  
Fields  
---  
`version` |  `integer` Specifies the format of the policy.Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:

  * Getting a policy that includes a conditional role binding
  * Adding a conditional role binding to a policy
  * Changing a conditional role binding in a policy
  * Removing any role binding, with or without a condition, from a policy that includes conditions

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).  
`bindings[]` |  `object (`[Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Binding)`)` Associates a list of `members`, or principals, with a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one principal.The `bindings` in a `Policy` can refer to up to 1,500 principals; up to 250 of these principals can be Google groups. Each occurrence of a principal counts towards these limits. For example, if the `bindings` grant 50 different roles to `user:alice@example.com`, and not to any other principal, then you can add another 1,450 principals to the `bindings` in the `Policy`.  
`auditConfigs[]` |  `object (`[AuditConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AuditConfig)`)` Specifies cloud audit logging configuration for this policy.  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.A base64-encoded string.  
  
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
  
### AuditConfig

JSON representation  
---  
      
    
    {
      "service": string,
      "auditLogConfigs": [
        {
          object ([AuditLogConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AuditLogConfig))
        }
      ]
    }  
  
Fields  
---  
`service` |  `string` Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.  
`auditLogConfigs[]` |  `object (`[AuditLogConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AuditLogConfig)`)` The configuration for logging of each type of permission.  
  
### AuditLogConfig

JSON representation  
---  
      
    
    {
      "logType": enum ([LogType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.LogType)),
      "exemptedMembers": [
        string
      ]
    }  
  
Fields  
---  
`logType` |  `enum (`[LogType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.LogType)`)` The log type that this config enables.  
`exemptedMembers[]` |  `string` Specifies the identities that do not cause logging for this type of permission. Follows the same format of `Binding.members`.  
  
### Policy

JSON representation  
---  
      
    
    {
      "version": integer,
      "constraint": string,
      "etag": string,
      "updateTime": string,
    
      // Union field policy_type can be only one of the following:
      "listPolicy": {
        object ([ListPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ListPolicy))
      },
      "booleanPolicy": {
        object ([BooleanPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.BooleanPolicy))
      },
      "restoreDefault": {
        object (RestoreDefault)
      }
      // End of list of possible types for union field policy_type.
    }  
  
Fields  
---  
`version` |  `integer` Version of the `Policy`. Default version is 0;  
`constraint` |  `string` The name of the `Constraint` the `Policy` is configuring, for example, `constraints/serviceuser.services`.A [list of available constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) is available.Immutable after creation.  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` An opaque tag indicating the current version of the `Policy`, used for concurrency control.When the `Policy` is returned from either a `GetPolicy` or a `ListOrgPolicy` request, this `etag` indicates the version of the current `Policy` to use when executing a read-modify-write loop.When the `Policy` is returned from a `GetEffectivePolicy` request, the `etag` will be unset.When the `Policy` is used in a `SetOrgPolicy` method, use the `etag` value that was returned from a `GetOrgPolicy` request as part of a read-modify-write loop for concurrency control. Not setting the `etag`in a `SetOrgPolicy` request will result in an unconditional write of the `Policy`.A base64-encoded string.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time stamp the `Policy` was previously updated. This is set by the server, not specified by the caller, and represents the last time a call to `SetOrgPolicy` was made for that `Policy`. Any value set by the client will be ignored.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `policy_type`. The field to populate is based on the `constraint_type` value in the `Constraint`. `list_constraint` => `list_policy` `boolean_constraint` => `boolean_policy`A `restore_default` message may be used with any `Constraint` type.Providing a *_policy that is incompatible with the `constraint_type` will result in an `invalid_argument` error.Attempting to set a `Policy` with a `policy_type` not set will result in an `invalid_argument` error. `policy_type` can be only one of the following:  
`listPolicy` |  `object (`[ListPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ListPolicy)`)` List of values either allowed or disallowed.  
`booleanPolicy` |  `object (`[BooleanPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.BooleanPolicy)`)` For boolean `Constraints`, whether to enforce the `Constraint` or not.  
`restoreDefault` |  `object (`RestoreDefault`)` Restores the default behavior of the constraint; independent of `Constraint` type.  
  
### ListPolicy

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ],
      "allValues": enum ([AllValues](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AllValues)),
      "suggestedValue": string,
      "inheritFromParent": boolean
    }  
  
Fields  
---  
`allowedValues[]` |  `string` List of values allowed at this resource. Can only be set if `all_values` is set to `ALL_VALUES_UNSPECIFIED`.  
`deniedValues[]` |  `string` List of values denied at this resource. Can only be set if `all_values` is set to `ALL_VALUES_UNSPECIFIED`.  
`allValues` |  `enum (`[AllValues](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AllValues)`)` The policy all_values state.  
`suggestedValue` |  `string` Optional. The Google Cloud Console will try to default to a configuration that matches the value specified in this `Policy`. If `suggested_value` is not set, it will inherit the value specified higher in the hierarchy, unless `inherit_from_parent` is `false`.  
`inheritFromParent` |  `boolean` Determines the inheritance behavior for this `Policy`.By default, a `ListPolicy` set at a resource supersedes any `Policy` set anywhere up the resource hierarchy. However, if `inherit_from_parent` is set to `true`, then the values from the effective `Policy` of the parent resource are inherited, meaning the values set in this `Policy` are added to the values inherited up the hierarchy.Setting `Policy` hierarchies that inherit both allowed values and denied values isn't recommended in most circumstances to keep the configuration simple and understandable. However, it is possible to set a `Policy` with `allowed_values` set that inherits a `Policy` with `denied_values` set. In this case, the values that are allowed must be in `allowed_values` and not present in `denied_values`.For example, suppose you have a `Constraint` `constraints/serviceuser.services`, which has a `constraint_type` of `list_constraint`, and with `constraint_default` set to `ALLOW`. Suppose that at the Organization level, a `Policy` is applied that restricts the allowed API activations to {`E1`, `E2`}. Then, if a `Policy` is applied to a project below the Organization that has `inherit_from_parent` set to `false` and field all_values set to DENY, then an attempt to activate any API will be denied.The following examples demonstrate different possible layerings for `projects/bar` parented by `organizations/foo`:Example 1 (no inherited values): `organizations/foo` has a `Policy` with values: {allowed_values: "E1" allowed_values:"E2"} `projects/bar` has `inherit_from_parent` `false` and values: {allowed_values: "E3" allowed_values: "E4"} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are `E3`, and `E4`.Example 2 (inherited values): `organizations/foo` has a `Policy` with values: {allowed_values: "E1" allowed_values:"E2"} `projects/bar` has a `Policy` with values: {value: "E3" value: "E4" inherit_from_parent: true} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are `E1`, `E2`, `E3`, and `E4`.Example 3 (inheriting both allowed and denied values): `organizations/foo` has a `Policy` with values: {allowed_values: "E1" allowed_values: "E2"} `projects/bar` has a `Policy` with: {denied_values: "E1"} The accepted values at `organizations/foo` are `E1`, `E2`. The value accepted at `projects/bar` is `E2`.Example 4 (RestoreDefault): `organizations/foo` has a `Policy` with values: {allowed_values: "E1" allowed_values:"E2"} `projects/bar` has a `Policy` with values: {RestoreDefault: {}} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are either all or none depending on the value of `constraint_default` (if `ALLOW`, all; if `DENY`, none).Example 5 (no policy inherits parent policy): `organizations/foo` has no `Policy` set. `projects/bar` has no `Policy` set. The accepted values at both levels are either all or none depending on the value of `constraint_default` (if `ALLOW`, all; if `DENY`, none).Example 6 (ListConstraint allowing all): `organizations/foo` has a `Policy` with values: {allowed_values: "E1" allowed_values: "E2"} `projects/bar` has a `Policy` with: {all: ALLOW} The accepted values at `organizations/foo` are `E1`, E2`. Any value is accepted at`projects/bar`.Example 7 (ListConstraint allowing none): `organizations/foo` has a `Policy` with values: {allowed_values: "E1" allowed_values: "E2"} `projects/bar` has a `Policy` with: {all: DENY} The accepted values at `organizations/foo` are `E1`, E2`. No value is accepted at`projects/bar`.Example 10 (allowed and denied subtrees of Resource Manager hierarchy): Given the following resource hierarchy O1->{F1, F2}; F1->{P1}; F2->{P2, P3}, `organizations/foo` has a `Policy` with values: {allowed_values: "under:organizations/O1"} `projects/bar` has a `Policy` with: {allowed_values: "under:projects/P3"} {denied_values: "under:folders/F2"} The accepted values at `organizations/foo` are `organizations/O1`, `folders/F1`, `folders/F2`, `projects/P1`, `projects/P2`, `projects/P3`. The accepted values at `projects/bar` are `organizations/O1`, `folders/F1`, `projects/P1`.  
  
### BooleanPolicy

JSON representation  
---  
      
    
    {
      "enforced": boolean
    }  
  
Fields  
---  
`enforced` |  `boolean` If `true`, then the `Policy` is enforced. If `false`, then any configuration is acceptable.Suppose you have a `Constraint` `constraints/compute.disableSerialPortAccess` with `constraint_default` set to `ALLOW`. A `Policy` for that `Constraint` exhibits the following behavior: - If the `Policy` at this resource has enforced set to `false`, serial port connection attempts will be allowed. - If the `Policy` at this resource has enforced set to `true`, serial port connection attempts will be refused. - If the `Policy` at this resource is `RestoreDefault`, serial port connection attempts will be allowed. - If no `Policy` is set at this resource or anywhere higher in the resource hierarchy, serial port connection attempts will be allowed. - If no `Policy` is set at this resource, but one exists higher in the resource hierarchy, the behavior is as if the`Policy` were set at this resource.The following examples demonstrate the different possible layerings:Example 1 (nearest `Constraint` wins): `organizations/foo` has a `Policy` with: {enforced: false} `projects/bar` has no `Policy` set. The constraint at `projects/bar` and `organizations/foo` will not be enforced.Example 2 (enforcement gets replaced): `organizations/foo` has a `Policy` with: {enforced: false} `projects/bar` has a `Policy` with: {enforced: true} The constraint at `organizations/foo` is not enforced. The constraint at `projects/bar` is enforced.Example 3 (RestoreDefault): `organizations/foo` has a `Policy` with: {enforced: true} `projects/bar` has a `Policy` with: {RestoreDefault: {}} The constraint at `organizations/foo` is enforced. The constraint at `projects/bar` is not enforced, because `constraint_default` for the `Constraint` is `ALLOW`.  
  
### AccessPolicy

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "title": string,
      "scopes": [
        string
      ],
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Resource name of the `AccessPolicy`. Format: `accessPolicies/{access_policy}`  
`parent` |  `string` Required. The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organization_id}`  
`title` |  `string` Required. Human readable title. Does not affect behavior.  
`scopes[]` |  `string` The scopes of the `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessPolicy)`. Scopes define which resources a policy can restrict and where its resources can be referenced. For example, policy A with `scopes=["folders/123"]` has the following behavior:

  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)` can only restrict projects within `folders/123`.
  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)` within policy A can only reference access levels defined within policy A.
  * Only one policy can include a given scope; thus, attempting to create a second policy which includes `folders/123` will result in an error.

If no scopes are provided, then any resource within the organization can be restricted. Scopes cannot be modified after a policy is created. Policies can only have a single scope. Format: list of `folders/{folder_number}` or `projects/{project_number}`  
`etag` |  `string` Output only. An opaque identifier for the current version of the `AccessPolicy`. This will always be a strongly validated etag, meaning that two Access Policies will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format.  
  
### AccessLevel

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
    
      // Union field level can be only one of the following:
      "basic": {
        object ([BasicLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.BasicLevel))
      },
      "custom": {
        object ([CustomLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.CustomLevel))
      }
      // End of list of possible types for union field level.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for the `AccessLevel`. Format: `accessPolicies/{access_policy}/accessLevels/{access_level}`.The `access_level` component must begin with a letter, followed by alphanumeric characters or `_`. Its maximum length is 50 characters.After you create an `AccessLevel`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `AccessLevel` and its use. Does not affect behavior.  
Union field `level`. Required. Describes the necessary conditions for the level to apply. `level` can be only one of the following:  
`basic` |  `object (`[BasicLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.BasicLevel)`)` A `BasicLevel` composed of `Conditions`.  
`custom` |  `object (`[CustomLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.CustomLevel)`)` A `CustomLevel` written in the Common Expression Language.  
  
### BasicLevel

JSON representation  
---  
      
    
    {
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Condition))
        }
      ],
      "combiningFunction": enum ([ConditionCombiningFunction](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ConditionCombiningFunction))
    }  
  
Fields  
---  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Condition)`)` Required. A list of requirements for the `AccessLevel` to be granted.  
`combiningFunction` |  `enum (`[ConditionCombiningFunction](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ConditionCombiningFunction)`)` How the `conditions` list should be combined to determine if a request is granted this `AccessLevel`. If AND is used, each `Condition` in `conditions` must be satisfied for the `AccessLevel` to be applied. If OR is used, at least one `Condition` in `conditions` must be satisfied for the `AccessLevel` to be applied. Default behavior is AND.  
  
### Condition

JSON representation  
---  
      
    
    {
      "ipSubnetworks": [
        string
      ],
      "devicePolicy": {
        object ([DevicePolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.DevicePolicy))
      },
      "requiredAccessLevels": [
        string
      ],
      "negate": boolean,
      "members": [
        string
      ],
      "regions": [
        string
      ],
      "vpcNetworkSources": [
        {
          object ([VpcNetworkSource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VpcNetworkSource))
        }
      ]
    }  
  
Fields  
---  
`ipSubnetworks[]` |  `string` CIDR block IP subnetwork specification. May be IPv4 or IPv6. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly, for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32" is not. The originating IP of a request must be in one of the listed subnets in order for this Condition to be true. If empty, all IP addresses are allowed.  
`devicePolicy` |  `object (`[DevicePolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.DevicePolicy)`)` Device specific restrictions, all restrictions must hold for the Condition to be true. If not specified, all devices are allowed.  
`requiredAccessLevels[]` |  `string` A list of other access levels defined in the same `Policy`, referenced by resource name. Referencing an `AccessLevel` which does not exist is an error. All access levels listed must be granted for the Condition to be true. Example: "`accessPolicies/MY_POLICY/accessLevels/LEVEL_NAME"`  
`negate` |  `boolean` Whether to negate the Condition. If true, the Condition becomes a NAND over its non-empty fields. Any non-empty field criteria evaluating to false will result in the Condition to be satisfied. Defaults to false.  
`members[]` |  `string` The request must be made by one of the provided user or service accounts. Groups are not supported. Syntax: `user:{emailid}` `serviceAccount:{emailid}` If not specified, a request may come from any user.  
`regions[]` |  `string` The request must originate from one of the provided countries/regions. Must be valid ISO 3166-1 alpha-2 codes.  
`vpcNetworkSources[]` |  `object (`[VpcNetworkSource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VpcNetworkSource)`)` The request must originate from one of the provided VPC networks in Google Cloud. Cannot specify this field together with `ip_subnetworks`.  
  
### DevicePolicy

JSON representation  
---  
      
    
    {
      "requireScreenlock": boolean,
      "allowedEncryptionStatuses": [
        enum ([DeviceEncryptionStatus](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.DeviceEncryptionStatus))
      ],
      "osConstraints": [
        {
          object ([OsConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OsConstraint))
        }
      ],
      "allowedDeviceManagementLevels": [
        enum ([DeviceManagementLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.DeviceManagementLevel))
      ],
      "requireAdminApproval": boolean,
      "requireCorpOwned": boolean
    }  
  
Fields  
---  
`requireScreenlock` |  `boolean` Whether or not screenlock is required for the DevicePolicy to be true. Defaults to `false`.  
`allowedEncryptionStatuses[]` |  `enum (`[DeviceEncryptionStatus](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.DeviceEncryptionStatus)`)` Allowed encryptions statuses, an empty list allows all statuses.  
`osConstraints[]` |  `object (`[OsConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OsConstraint)`)` Allowed OS versions, an empty list allows all types and all versions.  
`allowedDeviceManagementLevels[]` |  `enum (`[DeviceManagementLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.DeviceManagementLevel)`)` Allowed device management levels, an empty list allows all management levels.  
`requireAdminApproval` |  `boolean` Whether the device needs to be approved by the customer admin.  
`requireCorpOwned` |  `boolean` Whether the device needs to be corp owned.  
  
### OsConstraint

JSON representation  
---  
      
    
    {
      "osType": enum ([OsType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OsType)),
      "minimumVersion": string,
      "requireVerifiedChromeOs": boolean
    }  
  
Fields  
---  
`osType` |  `enum (`[OsType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OsType)`)` Required. The allowed OS type.  
`minimumVersion` |  `string` The minimum allowed OS version. If not set, any version of this OS satisfies the constraint. Format: `"major.minor.patch"`. Examples: `"10.5.301"`, `"9.2.1"`.  
`requireVerifiedChromeOs` |  `boolean` Only allows requests from devices with a verified Chrome OS. Verifications includes requirements that the device is enterprise-managed, conformant to domain policies, and the caller has permission to call the API targeted by the request.  
  
### VpcNetworkSource

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "vpcSubnetwork": {
        object ([VpcSubNetwork](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VpcSubNetwork))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`.`kind` can be only one of the following:  
`vpcSubnetwork` |  `object (`[VpcSubNetwork](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VpcSubNetwork)`)` Sub-segment ranges of a VPC network.  
  
### VpcSubNetwork

JSON representation  
---  
      
    
    {
      "network": string,
      "vpcIpSubnetworks": [
        string
      ]
    }  
  
Fields  
---  
`network` |  `string` Required. Network name. If the network is not part of the organization, the `compute.network.get` permission must be granted to the caller. Format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NETWORK_NAME}` Example: `//compute.googleapis.com/projects/my-project/global/networks/network-1`  
`vpcIpSubnetworks[]` |  `string` CIDR block IP subnetwork specification. The IP address must be an IPv4 address and can be a public or private IP address. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. If empty, all IP addresses are allowed.  
  
### CustomLevel

JSON representation  
---  
      
    
    {
      "expr": {
        object ([Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Expr))
      }
    }  
  
Fields  
---  
`expr` |  `object (`[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Expr)`)` Required. A Cloud CEL expression evaluating to a boolean.  
  
### ServicePerimeter

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
      "perimeterType": enum ([PerimeterType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PerimeterType)),
      "status": {
        object ([ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeterConfig))
      },
      "spec": {
        object ([ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeterConfig))
      },
      "useExplicitDryRunSpec": boolean,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for the `ServicePerimeter`. Format: `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`.The `service_perimeter` component must begin with a letter, followed by alphanumeric characters or `_`.After you create a `ServicePerimeter`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `ServicePerimeter` and its use. Does not affect behavior.  
`perimeterType` |  `enum (`[PerimeterType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PerimeterType)`)` Perimeter type indicator. A single project or VPC network is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty.  
`status` |  `object (`[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeterConfig)`)` Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries.  
`spec` |  `object (`[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeterConfig)`)` Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set.  
`useExplicitDryRunSpec` |  `boolean` Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values.  
`etag` |  `string` Optional. An opaque identifier for the current version of the `ServicePerimeter`. This identifier does not follow any specific format. If an etag is not provided, the operation will be performed as if a valid etag is provided.  
  
### ServicePerimeterConfig

JSON representation  
---  
      
    
    {
      "resources": [
        string
      ],
      "accessLevels": [
        string
      ],
      "restrictedServices": [
        string
      ],
      "vpcAccessibleServices": {
        object ([VpcAccessibleServices](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VpcAccessibleServices))
      },
      "ingressPolicies": [
        {
          object ([IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy))
        }
      ],
      "egressPolicies": [
        {
          object ([EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy))
        }
      ]
    }  
  
Fields  
---  
`resources[]` |  `string` A list of Google Cloud resources that are inside of the service perimeter. Currently only projects and VPCs are allowed. Project format: `projects/{project_number}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`.  
`accessLevels[]` |  `string` A list of `AccessLevel` resource names that allow resources within the `ServicePerimeter` to be accessed from the internet. `AccessLevels` listed must be in the same policy as this `ServicePerimeter`. Referencing a nonexistent `AccessLevel` is a syntax error. If no `AccessLevel` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `"accessPolicies/MY_POLICY/accessLevels/MY_LEVEL"`. For Service Perimeter Bridge, must be empty.  
`restrictedServices[]` |  `string` Google Cloud services that are subject to the Service Perimeter restrictions. For example, if `storage.googleapis.com` is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions.  
`vpcAccessibleServices` |  `object (`[VpcAccessibleServices](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VpcAccessibleServices)`)` Configuration for APIs allowed within Perimeter.  
`ingressPolicies[]` |  `object (`[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)`)` List of `[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)` to apply to the perimeter. A perimeter may have multiple `[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)`, each of which is evaluated separately. Access is granted if any `[Ingress Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)` grants it. Must be empty for a perimeter bridge.  
`egressPolicies[]` |  `object (`[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)`)` List of `[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)` to apply to the perimeter. A perimeter may have multiple `[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)`, each of which is evaluated separately. Access is granted if any `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)` grants it. Must be empty for a perimeter bridge.  
  
### VpcAccessibleServices

JSON representation  
---  
      
    
    {
      "enableRestriction": boolean,
      "allowedServices": [
        string
      ],
      "allowedServicePatterns": [
        {
          object ([ServicePattern](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePattern))
        }
      ],
      "servicePatternsEnforcementScopes": [
        enum ([ServicePatternsEnforcementScope](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePatternsEnforcementScope))
      ]
    }  
  
Fields  
---  
`enableRestriction` |  `boolean` Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowed_services'.  
`allowedServices[]` |  `string` The list of APIs usable within the Service Perimeter. Must be empty unless 'enable_restriction' is True. You can specify a list of individual services, as well as include the 'RESTRICTED-SERVICES' value, which automatically includes all of the services protected by the perimeter.  
`allowedServicePatterns[]` |  `object (`[ServicePattern](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePattern)`)` Specifies which Google services are allowed to be accessed from VPC networks in the service perimeter.  
`servicePatternsEnforcementScopes[]` |  `enum (`[ServicePatternsEnforcementScope](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePatternsEnforcementScope)`)` Defines the enforcement scopes of service patterns.  
  
### ServicePattern

JSON representation  
---  
      
    
    {
      "modifiers": [
        {
          object ([Modifier](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Modifier))
        }
      ],
    
      // Union field kind can be only one of the following:
      "service": string,
      "pattern": string
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`modifiers[]` |  `object (`[Modifier](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Modifier)`)` Modifiers to apply to the requests that match the URL pattern.  
Union field `kind`. The service or pattern to allow. `kind` can be only one of the following:  
`service` |  `string` Supported service to allow.  
`pattern` |  `string` URL pattern to allow.Only patterns of ".googleapis.com/*", "www.googleapis.com//*" and "*.appspot.com/* forms are supported, where  should be an alphanumeric name.  
  
### Modifier

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "addRequestHeader": {
        object ([AddRequestHeader](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AddRequestHeader))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. Modifier to apply to the API requests. `kind` can be only one of the following:  
`addRequestHeader` |  `object (`[AddRequestHeader](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AddRequestHeader)`)` Adds an additional HTTP request header.  
  
### AddRequestHeader

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` HTTP header key.  
`value` |  `string` HTTP header value.  
  
### IngressPolicy

JSON representation  
---  
      
    
    {
      "ingressFrom": {
        object ([IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressFrom))
      },
      "ingressTo": {
        object ([IngressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressTo))
      },
      "title": string
    }  
  
Fields  
---  
`ingressFrom` |  `object (`[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressFrom)`)` Defines the conditions on the source of a request causing this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)` to apply.  
`ingressTo` |  `object (`[IngressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressTo)`)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)` and request destination that cause this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the ingress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
### IngressFrom

JSON representation  
---  
      
    
    {
      "sources": [
        {
          object ([IngressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressSource))
        }
      ],
      "identities": [
        string
      ],
      "identityType": enum ([IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IdentityType))
    }  
  
Fields  
---  
`sources[]` |  `object (`[IngressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressSource)`)` Sources that this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)` authorizes access from.  
`identities[]` |  `string` A list of identities that are allowed access through [IngressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identityType` |  `enum (`[IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IdentityType)`)` Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
  
### IngressSource

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "accessLevel": string,
      "resource": string,
      "pscEndpoint": {
        object ([PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Allowed ingress source. It can be one of `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel)` or Google Cloud resource or a `[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint)`. `source` can be only one of the following:  
`accessLevel` |  `string` An `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel)` resource name that allow resources within the `[ServicePerimeters](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)` to be accessed from the internet. `[AccessLevels](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel)` listed must be in the same policy as this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)`. Referencing a nonexistent `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel)` will cause an error. If no `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.AccessLevel)` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `access_level`, then all `[IngressSources](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressSource)` will be allowed.  
`resource` |  `string` A Google Cloud resource that is allowed to ingress the perimeter. Requests from these resources will be allowed to access perimeter data. Currently only projects and VPCs are allowed. Project format: `projects/{project_number}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`. The project may be in any Google Cloud organization, not just the organization that the perimeter is defined in. `*` is not allowed, the case of allowing all Google Cloud resources only is not supported.  
`pscEndpoint` |  `object (`[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint)`)` A `[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint)` that is allowed to access the perimeter. The Private Service Connect endpoint may be in any organization, not just the organization that the perimeter is defined in.  
  
### PrivateServiceConnectEndpoint

JSON representation  
---  
      
    
    {
      "forwardingRule": string
    }  
  
Fields  
---  
`forwardingRule` |  `string` The full resource name of the global forwarding rule that identifies a Private Service Connect endpoint. Forwarding rule format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/forwardingRules/{FORWARDING_RULE_ID}`.  
  
### IngressTo

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation))
        }
      ],
      "resources": [
        string
      ],
      "roles": [
        string
      ]
    }  
  
Fields  
---  
`operations[]` |  `object (`[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)`)` A list of `[ApiOperations](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)` allowed to be performed by the sources specified in corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressFrom)` in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)`.  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, protected by this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)` that are allowed to be accessed by sources defined in the corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressFrom)`. If a single `*` is specified, then access to all resources inside the perimeter are allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressFrom)` are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)`.  
  
### ApiOperation

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "methodSelectors": [
        {
          object ([MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.MethodSelector))
        }
      ]
    }  
  
Fields  
---  
`serviceName` |  `string` The name of the API whose methods or permissions the `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressPolicy)` or `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)` want to allow. A single `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)` with `service_name` field set to `*` will allow all methods AND permissions for all services.  
`methodSelectors[]` |  `object (`[MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.MethodSelector)`)` API methods or permissions to allow. Method or permission must belong to the service specified by `service_name` field. A single `[MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.MethodSelector)` entry with `*` specified for the `method` field will allow all methods AND permissions for the service specified in `service_name`.  
  
### MethodSelector

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "method": string,
      "permission": string
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The API method name or Cloud IAM permission name to allow. `kind` can be only one of the following:  
`method` |  `string` A valid method name for the corresponding `service_name` in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)`. If `*` is used as the value for the `method`, then ALL methods and permissions are allowed.  
`permission` |  `string` A valid Cloud IAM permission for the corresponding `service_name` in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)`.  
  
### EgressPolicy

JSON representation  
---  
      
    
    {
      "egressFrom": {
        object ([EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressFrom))
      },
      "egressTo": {
        object ([EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressTo))
      },
      "title": string
    }  
  
Fields  
---  
`egressFrom` |  `object (`[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressFrom)`)` Defines conditions on the source of a request causing this `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)` to apply.  
`egressTo` |  `object (`[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressTo)`)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)` and destination resources that cause this `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the egress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
### EgressFrom

JSON representation  
---  
      
    
    {
      "identities": [
        string
      ],
      "identityType": enum ([IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IdentityType)),
      "sources": [
        {
          object ([EgressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressSource))
        }
      ],
      "sourceRestriction": enum ([SourceRestriction](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.SourceRestriction))
    }  
  
Fields  
---  
`identities[]` |  `string` A list of identities that are allowed access through [EgressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identityType` |  `enum (`[IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IdentityType)`)` Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
`sources[]` |  `object (`[EgressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressSource)`)` Sources that this [EgressPolicy] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressPolicy] authorizes access from. If this field is not empty, then `source_restriction` must be set to `SOURCE_RESTRICTION_ENABLED`.  
`sourceRestriction` |  `enum (`[SourceRestriction](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.SourceRestriction)`)` Whether to enforce traffic restrictions based on `sources` field. If the `sources` fields is non-empty, then this field must be set to `SOURCE_RESTRICTION_ENABLED`.  
  
### EgressSource

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "accessLevel": string,
      "resource": string,
      "pscEndpoint": {
        object ([PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Allowed egress source. `source` can be only one of the following:  
`accessLevel` |  `string` An [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] resource name that allows protected resources inside the [ServicePerimeters] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] to access outside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] boundaries. [AccessLevels] [google.identity.accesscontextmanager.v1alpha.AccessLevel] listed must be in the same policy as this [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter]. Referencing a nonexistent [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] will cause an error. If an [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] name is not specified, only resources within the perimeter can be accessed through Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `access_level`, then all [EgressSources] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressSource] will be allowed.  
`resource` |  `string` A Google Cloud resource from the service perimeter that you want to allow to access data outside the perimeter. This field supports only projects. The project format is `projects/{project_number}`. You can't use `*` in this field to allow all Google Cloud resources.  
`pscEndpoint` |  `object (`[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint)`)` A `[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.PrivateServiceConnectEndpoint)` that is allowed to access data outside the perimeter. The Private Service Connect endpoint may be in any organization, not just the organization that the perimeter is defined in.  
  
### EgressTo

JSON representation  
---  
      
    
    {
      "resources": [
        string
      ],
      "operations": [
        {
          object ([ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation))
        }
      ],
      "externalResources": [
        string
      ],
      "roles": [
        string
      ]
    }  
  
Fields  
---  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, that are allowed to be accessed by sources defined in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressFrom)`. A request matches if it contains a resource in this list. If `*` is specified for `resources`, then this `[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressTo)` rule will authorize access to all resources outside the perimeter.  
`operations[]` |  `object (`[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)`)` A list of `[ApiOperations](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ApiOperation)` allowed to be performed by the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressFrom)`. A request matches if it uses an operation/service in this list.  
`externalResources[]` |  `string` A list of external resources that are allowed to be accessed. Only AWS and Azure resources are supported. For Amazon S3, the supported formats are s3://BUCKET_NAME, s3a://BUCKET_NAME, and s3n://BUCKET_NAME. For Azure Storage, the supported format is <azure://myaccount.blob.core.windows.net/CONTAINER_NAME>. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressFrom)`. are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ServicePerimeter)`.  
  
### Inventory

JSON representation  
---  
      
    
    {
      "name": string,
      "osInfo": {
        object ([OsInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OsInfo))
      },
      "items": {
        string: {
          object ([Item](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Item))
        },
        ...
      },
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The `Inventory` API resource name.Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/inventory`  
`osInfo` |  `object (`[OsInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OsInfo)`)` Base level operating system information for the VM.  
`items` |  `map (key: string, value: object (`[Item](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Item)`))` Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last reported inventory for the VM.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### OsInfo

JSON representation  
---  
      
    
    {
      "hostname": string,
      "longName": string,
      "shortName": string,
      "version": string,
      "architecture": string,
      "kernelVersion": string,
      "kernelRelease": string,
      "osconfigAgentVersion": string
    }  
  
Fields  
---  
`hostname` |  `string` The VM hostname.  
`longName` |  `string` The operating system long name. For example 'Debian GNU/Linux 9' or 'Microsoft Window Server 2019 Datacenter'.  
`shortName` |  `string` The operating system short name. For example, 'windows' or 'debian'.  
`version` |  `string` The version of the operating system.  
`architecture` |  `string` The system architecture of the operating system.  
`kernelVersion` |  `string` The kernel version of the operating system.  
`kernelRelease` |  `string` The kernel release of the operating system.  
`osconfigAgentVersion` |  `string` The current version of the OS Config agent running on the VM.  
  
### ItemsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Item](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Item))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Item](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Item)`)`  
  
### Item

JSON representation  
---  
      
    
    {
      "id": string,
      "originType": enum ([OriginType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OriginType)),
      "createTime": string,
      "updateTime": string,
      "type": enum ([Type](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Type)),
    
      // Union field details can be only one of the following:
      "installedPackage": {
        object ([SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.SoftwarePackage))
      },
      "availablePackage": {
        object ([SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.SoftwarePackage))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`id` |  `string` Identifier for this item, unique across items for this VM.  
`originType` |  `enum (`[OriginType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.OriginType)`)` The origin of this inventory item.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When this inventory item was first detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When this inventory item was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Type)`)` The specific type of inventory, correlating to its specific details.  
Union field `details`. Specific details of this inventory item based on its type. `details` can be only one of the following:  
`installedPackage` |  `object (`[SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.SoftwarePackage)`)` Software package present on the VM instance.  
`availablePackage` |  `object (`[SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.SoftwarePackage)`)` Software package available to be installed on the VM instance.  
  
### SoftwarePackage

JSON representation  
---  
      
    
    {
    
      // Union field details can be only one of the following:
      "yumPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage))
      },
      "aptPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage))
      },
      "zypperPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage))
      },
      "googetPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage))
      },
      "zypperPatch": {
        object ([ZypperPatch](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ZypperPatch))
      },
      "wuaPackage": {
        object ([WindowsUpdatePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsUpdatePackage))
      },
      "qfePackage": {
        object ([WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsQuickFixEngineeringPackage))
      },
      "cosPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage))
      },
      "windowsApplication": {
        object ([WindowsApplication](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsApplication))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
Union field `details`. Information about the different types of software packages. `details` can be only one of the following:  
`yumPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage)`)` Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.  
`aptPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage)`)` Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.  
`zypperPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage)`)` Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`googetPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage)`)` Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.  
`zypperPatch` |  `object (`[ZypperPatch](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ZypperPatch)`)` Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`wuaPackage` |  `object (`[WindowsUpdatePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsUpdatePackage)`)` Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.  
`qfePackage` |  `object (`[WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsQuickFixEngineeringPackage)`)` Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.  
`cosPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.VersionedPackage)`)` Details of a COS package.  
`windowsApplication` |  `object (`[WindowsApplication](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsApplication)`)` Details of Windows Application.  
  
### VersionedPackage

JSON representation  
---  
      
    
    {
      "packageName": string,
      "architecture": string,
      "version": string
    }  
  
Fields  
---  
`packageName` |  `string` The name of the package.  
`architecture` |  `string` The system architecture this package is intended for.  
`version` |  `string` The version of the package.  
  
### ZypperPatch

JSON representation  
---  
      
    
    {
      "patchName": string,
      "category": string,
      "severity": string,
      "summary": string
    }  
  
Fields  
---  
`patchName` |  `string` The name of the patch.  
`category` |  `string` The category of the patch.  
`severity` |  `string` The severity specified for this patch  
`summary` |  `string` Any summary information provided about this patch.  
  
### WindowsUpdatePackage

JSON representation  
---  
      
    
    {
      "title": string,
      "description": string,
      "categories": [
        {
          object ([WindowsUpdateCategory](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsUpdateCategory))
        }
      ],
      "kbArticleIds": [
        string
      ],
      "supportUrl": string,
      "moreInfoUrls": [
        string
      ],
      "updateId": string,
      "revisionNumber": integer,
      "lastDeploymentChangeTime": string
    }  
  
Fields  
---  
`title` |  `string` The localized title of the update package.  
`description` |  `string` The localized description of the update package.  
`categories[]` |  `object (`[WindowsUpdateCategory](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.WindowsUpdateCategory)`)` The categories that are associated with this update package.  
`kbArticleIds[]` |  `string` A collection of Microsoft Knowledge Base article IDs that are associated with the update package.  
`supportUrl` |  `string` A hyperlink to the language-specific support information for the update.  
`moreInfoUrls[]` |  `string` A collection of URLs that provide more information about the update package.  
`updateId` |  `string` Gets the identifier of an update package. Stays the same across revisions.  
`revisionNumber` |  `integer` The revision number of this update package.  
`lastDeploymentChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last published date of the update, in (UTC) date and time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### WindowsUpdateCategory

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string
    }  
  
Fields  
---  
`id` |  `string` The identifier of the windows update category.  
`name` |  `string` The name of the windows update category.  
  
### WindowsQuickFixEngineeringPackage

JSON representation  
---  
      
    
    {
      "caption": string,
      "description": string,
      "hotFixId": string,
      "installTime": string
    }  
  
Fields  
---  
`caption` |  `string` A short textual description of the QFE update.  
`description` |  `string` A textual description of the QFE update.  
`hotFixId` |  `string` Unique identifier associated with a particular QFE update.  
`installTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date that the QFE update was installed. Mapped from installed_on field.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### WindowsApplication

JSON representation  
---  
      
    
    {
      "displayName": string,
      "displayVersion": string,
      "publisher": string,
      "installDate": {
        object ([Date](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Date))
      },
      "helpLink": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the application or product.  
`displayVersion` |  `string` The version of the product or application in string format.  
`publisher` |  `string` The name of the manufacturer for the product or application.  
`installDate` |  `object (`[Date](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.Date)`)` The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product.  
`helpLink` |  `string` The internet address for technical support.  
  
### Date

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
### RelatedAssets

JSON representation  
---  
      
    
    {
      "relationshipAttributes": {
        object ([RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelationshipAttributes))
      },
      "assets": [
        {
          object ([RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelatedAsset))
        }
      ]
    }  
  
Fields  
---  
`relationshipAttributes` |  `object (`[RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelationshipAttributes)`)` The detailed relationship attributes.  
`assets[]` |  `object (`[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.RelatedAsset)`)` The peer resources of the relationship.  
  
### RelationshipAttributes

JSON representation  
---  
      
    
    {
      "type": string,
      "sourceResourceType": string,
      "targetResourceType": string,
      "action": string
    }  
  
Fields  
---  
`type` |  `string` The unique identifier of the relationship type. Example: `INSTANCE_TO_INSTANCEGROUP`  
`sourceResourceType` |  `string` The source asset type. Example: `compute.googleapis.com/Instance`  
`targetResourceType` |  `string` The target asset type. Example: `compute.googleapis.com/Disk`  
`action` |  `string` The detail of the relationship, e.g. `contains`, `attaches`  
  
### RelatedAsset

JSON representation  
---  
      
    
    {
      "asset": string,
      "assetType": string,
      "ancestors": [
        string
      ],
      "relationshipType": string
    }  
  
Fields  
---  
`asset` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`assetType` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`ancestors[]` |  `string` The ancestors of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
`relationshipType` |  `string` The unique identifier of the relationship type. Example: `INSTANCE_TO_INSTANCEGROUP`  
  
### AssetException

JSON representation  
---  
      
    
    {
      "exceptionType": enum ([ExceptionType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ExceptionType)),
      "details": string
    }  
  
Fields  
---  
`exceptionType` |  `enum (`[ExceptionType](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.ExceptionType)`)` The type of exception.  
`details` |  `string` The details of the exception.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### LogType

The list of valid permission types for which logging can be configured. Admin writes are always logged, and are not configurable.

Enums  
---  
`LOG_TYPE_UNSPECIFIED` | Default case. Should never be this.  
`ADMIN_READ` | Admin reads. Example: CloudIAM getIamPolicy  
`DATA_WRITE` | Data writes. Example: CloudSQL Users create  
`DATA_READ` | Data reads. Example: CloudSQL Users list  
  
### AllValues

This enum can be used to set `Policies` that apply to all possible configuration values rather than specific values in `allowed_values` or `denied_values`.

Setting this to `ALLOW` will mean this `Policy` allows all values. Similarly, setting it to `DENY` will mean no values are allowed. If set to either `ALLOW` or `DENY,`allowed_values`and`denied_values` must be unset. Setting this to`ALL_VALUES_UNSPECIFIED`allows for setting`allowed_values`and`denied_values`.

Enums  
---  
`ALL_VALUES_UNSPECIFIED` | Indicates that allowed_values or denied_values must be set.  
`ALLOW` | A policy with this set allows all values.  
`DENY` | A policy with this set denies all values.  
  
### DeviceEncryptionStatus

The encryption state of the device.

Enums  
---  
`ENCRYPTION_UNSPECIFIED` | The encryption status of the device is not specified or not known.  
`ENCRYPTION_UNSUPPORTED` | The device does not support encryption.  
`UNENCRYPTED` | The device supports encryption, but is currently unencrypted.  
`ENCRYPTED` | The device is encrypted.  
  
### OsType

The operating system type of the device.

Enums  
---  
`OS_UNSPECIFIED` | The operating system of the device is not specified or not known.  
`DESKTOP_MAC` | A desktop Mac operating system.  
`DESKTOP_WINDOWS` | A desktop Windows operating system.  
`DESKTOP_LINUX` | A desktop Linux operating system.  
`DESKTOP_CHROME_OS` | A desktop ChromeOS operating system.  
`ANDROID` | An Android operating system.  
`IOS` | An iOS operating system.  
  
### DeviceManagementLevel

The degree to which the device is managed by the Cloud organization.

Enums  
---  
`MANAGEMENT_UNSPECIFIED` | The device's management level is not specified or not known.  
`NONE` | The device is not managed.  
`BASIC` | Basic management is enabled, which is generally limited to monitoring and wiping the corporate account.  
`COMPLETE` | Complete device management. This includes more thorough monitoring and the ability to directly manage the device (such as remote wiping). This can be enabled through the Android Enterprise Platform.  
  
### ConditionCombiningFunction

Options for how the `conditions` list should be combined to determine if this `AccessLevel` is applied. Default is AND.

Enums  
---  
`AND` | All `Conditions` must be true for the `BasicLevel` to be true.  
`OR` | If at least one `Condition` is true, then the `BasicLevel` is true.  
  
### PerimeterType

Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter.

In addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by the regular perimeter that resource is in.

Perimeter Bridges are typically useful when building more complex toplogies with many independent perimeters that need to share some data with a common perimeter, but should not be able to share data among themselves.

Enums  
---  
`PERIMETER_TYPE_REGULAR` | Regular Perimeter. When no value is specified, the perimeter uses this type.  
`PERIMETER_TYPE_BRIDGE` | Perimeter Bridge.  
  
### ServicePatternsEnforcementScope

Defines the enforcement scope of service patterns.

Enums  
---  
`SERVICE_PATTERNS_ENFORCEMENT_SCOPE_UNSPECIFIED` | Default value. This cannot be used.  
`GOOGLE_APIS_VIA_PRIVATE_PATH` | Enables VPC Accessible Services enforcement for all APIs (including unsupported APIs) for Private Google Access configured with Private VIP and Private Service Connect Endpoint for Global Google APIs that uses 'all-apis' bundle.  
  
### IdentityType

Specifies the types of identities that are allowed access in either `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.IngressFrom)` or `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets#Output.Schema.EgressFrom)` rules.

Enums  
---  
`IDENTITY_TYPE_UNSPECIFIED` | No blanket identity group specified.  
`ANY_IDENTITY` | Authorize access from all identities outside the perimeter.  
`ANY_USER_ACCOUNT` | Authorize access from all human users outside the perimeter.  
`ANY_SERVICE_ACCOUNT` | Authorize access from all service accounts outside the perimeter.  
  
### SourceRestriction

Whether to enable the enforcement of traffic based on on the `sources` field. Only applies to [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].

Enums  
---  
`SOURCE_RESTRICTION_UNSPECIFIED` | Enforcement preference unspecified, will not enforce traffic restrictions based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
`SOURCE_RESTRICTION_ENABLED` | Enforcement preference enabled, traffic restrictions will be enforced based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
`SOURCE_RESTRICTION_DISABLED` | Enforcement preference disabled, will not enforce traffic restrictions based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
  
### OriginType

The origin of a specific inventory item.

Enums  
---  
`ORIGIN_TYPE_UNSPECIFIED` | Invalid. An origin type must be specified.  
`INVENTORY_REPORT` | This inventory item was discovered as the result of the agent reporting inventory via the reporting API.  
  
### Type

The different types of inventory that are tracked on a VM.

Enums  
---  
`TYPE_UNSPECIFIED` | Invalid. A type must be specified.  
`INSTALLED_PACKAGE` | This represents a package that is installed on the VM.  
`AVAILABLE_PACKAGE` | This represents an update that is available for a package.  
  
### ExceptionType

The type of exception.

Enums  
---  
`EXCEPTION_TYPE_UNSPECIFIED` | exception_type is not applicable for the current asset.  
`TRUNCATION` | The asset content is truncated.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
