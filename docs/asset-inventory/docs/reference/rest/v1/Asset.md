---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset/
title: Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:06.754257+00:00
---

# Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Asset Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Resource
    * JSON representation
  * Policy
    * JSON representation
  * ListPolicy
    * JSON representation
  * AllValues
  * BooleanPolicy
    * JSON representation
  * RestoreDefault
  * AccessPolicy
    * JSON representation
  * AccessLevel
    * JSON representation
  * BasicLevel
    * JSON representation
  * Condition
    * JSON representation
  * DevicePolicy
    * JSON representation
  * DeviceEncryptionStatus
  * OsConstraint
    * JSON representation
  * OsType
  * DeviceManagementLevel
  * VpcNetworkSource
    * JSON representation
  * VpcSubNetwork
    * JSON representation
  * ConditionCombiningFunction
  * CustomLevel
    * JSON representation
  * ServicePerimeter
    * JSON representation
  * PerimeterType
  * ServicePerimeterConfig
    * JSON representation
  * VpcAccessibleServices
    * JSON representation
  * IngressPolicy
    * JSON representation
  * IngressFrom
    * JSON representation
  * IngressSource
    * JSON representation
  * IdentityType
  * IngressTo
    * JSON representation
  * ApiOperation
    * JSON representation
  * MethodSelector
    * JSON representation
  * EgressPolicy
    * JSON representation
  * EgressFrom
    * JSON representation
  * EgressSource
    * JSON representation
  * SourceRestriction
  * EgressTo
    * JSON representation
  * Inventory
    * JSON representation
  * OsInfo
    * JSON representation
  * Item
    * JSON representation
  * OriginType
  * Type
  * SoftwarePackage
    * JSON representation
  * VersionedPackage
    * JSON representation
  * ZypperPatch
    * JSON representation
  * WindowsUpdatePackage
    * JSON representation
  * WindowsUpdateCategory
    * JSON representation
  * WindowsQuickFixEngineeringPackage
    * JSON representation
  * WindowsApplication
    * JSON representation
  * Date
    * JSON representation
  * RelatedAssets
    * JSON representation
  * RelationshipAttributes
    * JSON representation
  * RelatedAsset
    * JSON representation



An asset in Google Cloud. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy), or a relationship (e.g. an INSTANCE_TO_INSTANCEGROUP relationship). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

JSON representation  
---  
      
    
    {
      "updateTime": string,
      "name": string,
      "assetType": string,
      "resource": {
        object ([Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Resource))
      },
      "iamPolicy": {
        object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy))
      },
      "orgPolicy": [
        {
          object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Policy))
        }
      ],
      "osInventory": {
        object ([Inventory](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Inventory))
      },
      "relatedAssets": {
        object ([RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelatedAssets))
      },
      "relatedAsset": {
        object ([RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelatedAsset))
      },
      "ancestors": [
        string
      ],
      "assetExceptions": [
        {
          object ([AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException))
        }
      ],
    
      // Union field access_context_policy can be only one of the following:
      "accessPolicy": {
        object ([AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessPolicy))
      },
      "accessLevel": {
        object ([AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel))
      },
      "servicePerimeter": {
        object ([ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter))
      }
      // End of list of possible types for union field access_context_policy.
    }  
  
Fields  
---  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last update timestamp of an asset. updateTime is updated when create/update/delete operation is performed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`name` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`assetType` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Resource)`)` A representation of the resource.  
`iamPolicy` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy)`)` A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.  
`orgPolicy[]` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Policy)`)` A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.  
`osInventory` |  `object (`[Inventory](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Inventory)`)` A representation of runtime OS Inventory information. See [this topic](https://cloud.google.com/compute/docs/instances/os-inventory-management) for more information.  
`relatedAssets  
**(deprecated)**` |  `object (`[RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelatedAssets)`)` This item is deprecated!DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.  
`relatedAsset` |  `object (`[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelatedAsset)`)` One related asset of the current asset.  
`ancestors[]` |  `string` The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
`assetExceptions[]` |  `object (`[AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException)`)` The exceptions of a resource.  
Union field `access_context_policy`. A representation of an [access policy](https://cloud.google.com/access-context-manager/docs/overview#access-policies). `access_context_policy` can be only one of the following:  
`accessPolicy` |  `object (`[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessPolicy)`)` Also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).  
`accessLevel` |  `object (`[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)`)` Also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).  
`servicePerimeter` |  `object (`[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`)` Also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).  
  
## Resource

A representation of a Google Cloud resource.

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
  
## Policy

Defines a Cloud Organization `Policy` which is used to specify `Constraints` for configurations of Cloud Platform resources.

JSON representation  
---  
      
    
    {
      "version": integer,
      "constraint": string,
      "etag": string,
      "updateTime": string,
    
      // Union field policy_type can be only one of the following:
      "listPolicy": {
        object ([ListPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ListPolicy))
      },
      "booleanPolicy": {
        object ([BooleanPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#BooleanPolicy))
      },
      "restoreDefault": {
        object ([RestoreDefault](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RestoreDefault))
      }
      // End of list of possible types for union field policy_type.
    }  
  
Fields  
---  
`version` |  `integer` Version of the `Policy`. Default version is 0;  
`constraint` |  `string` The name of the `Constraint` the `Policy` is configuring, for example, `constraints/serviceuser.services`.A [list of available constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) is available.Immutable after creation.  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` An opaque tag indicating the current version of the `Policy`, used for concurrency control.When the `Policy` is returned from either a `GetPolicy` or a `ListOrgPolicy` request, this `etag` indicates the version of the current `Policy` to use when executing a read-modify-write loop.When the `Policy` is returned from a `policies.getEffectivePolicy` request, the `etag` will be unset.When the `Policy` is used in a `SetOrgPolicy` method, use the `etag` value that was returned from a `GetOrgPolicy` request as part of a read-modify-write loop for concurrency control. Not setting the `etag`in a `SetOrgPolicy` request will result in an unconditional write of the `Policy`.A base64-encoded string.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time stamp the `Policy` was previously updated. This is set by the server, not specified by the caller, and represents the last time a call to `SetOrgPolicy` was made for that `Policy`. Any value set by the client will be ignored.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `policy_type`. The field to populate is based on the `constraint_type` value in the `Constraint`. `list_constraint` => `list_policy` `boolean_constraint` => `boolean_policy`A `restore_default` message may be used with any `Constraint` type.Providing a *_policy that is incompatible with the `constraint_type` will result in an `invalid_argument` error.Attempting to set a `Policy` with a `policy_type` not set will result in an `invalid_argument` error. `policy_type` can be only one of the following:  
`listPolicy` |  `object (`[ListPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ListPolicy)`)` List of values either allowed or disallowed.  
`booleanPolicy` |  `object (`[BooleanPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#BooleanPolicy)`)` For boolean `Constraints`, whether to enforce the `Constraint` or not.  
`restoreDefault` |  `object (`[RestoreDefault](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RestoreDefault)`)` Restores the default behavior of the constraint; independent of `Constraint` type.  
  
## ListPolicy

Used in `policyType` to specify how `listPolicy` behaves at this resource.

`ListPolicy` can define specific values and subtrees of Cloud Resource Manager resource hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or denied by setting the `allowedValues` and `deniedValues` fields. This is achieved by using the `under:` and optional `is:` prefixes. The `under:` prefix is used to denote resource subtree values. The `is:` prefix is used to denote specific values, and is required only if the value contains a ":". Values prefixed with "is:" are treated the same as values with no prefix. Ancestry subtrees must be in one of the following formats:

  * "projects/", e.g. "projects/tokyo-rain-123"
  * "folders/", e.g. "folders/1234"
  * "organizations/", e.g. "organizations/1234"



The `supportsUnder` field of the associated `Constraint` defines whether ancestry prefixes can be used. You can set `allowedValues` and `deniedValues` in the same `Policy` if `allValues` is `ALL_VALUES_UNSPECIFIED`. `ALLOW` or `DENY` are used to allow or deny all values. If `allValues` is set to either `ALLOW` or `DENY`, `allowedValues` and `deniedValues` must be unset.

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ],
      "allValues": enum ([AllValues](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AllValues)),
      "suggestedValue": string,
      "inheritFromParent": boolean
    }  
  
Fields  
---  
`allowedValues[]` |  `string` List of values allowed at this resource. Can only be set if `allValues` is set to `ALL_VALUES_UNSPECIFIED`.  
`deniedValues[]` |  `string` List of values denied at this resource. Can only be set if `allValues` is set to `ALL_VALUES_UNSPECIFIED`.  
`allValues` |  `enum (`[AllValues](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AllValues)`)` The policy allValues state.  
`suggestedValue` |  `string` Optional. The Google Cloud Console will try to default to a configuration that matches the value specified in this `Policy`. If `suggestedValue` is not set, it will inherit the value specified higher in the hierarchy, unless `inheritFromParent` is `false`.  
`inheritFromParent` |  `boolean` Determines the inheritance behavior for this `Policy`.By default, a `ListPolicy` set at a resource supersedes any `Policy` set anywhere up the resource hierarchy. However, if `inheritFromParent` is set to `true`, then the values from the effective `Policy` of the parent resource are inherited, meaning the values set in this `Policy` are added to the values inherited up the hierarchy.Setting `Policy` hierarchies that inherit both allowed values and denied values isn't recommended in most circumstances to keep the configuration simple and understandable. However, it is possible to set a `Policy` with `allowedValues` set that inherits a `Policy` with `deniedValues` set. In this case, the values that are allowed must be in `allowedValues` and not present in `deniedValues`.For example, suppose you have a `Constraint` `constraints/serviceuser.services`, which has a `constraint_type` of `listConstraint`, and with `constraintDefault` set to `ALLOW`. Suppose that at the Organization level, a `Policy` is applied that restricts the allowed API activations to {`E1`, `E2`}. Then, if a `Policy` is applied to a project below the Organization that has `inheritFromParent` set to `false` and field allValues set to DENY, then an attempt to activate any API will be denied.The following examples demonstrate different possible layerings for `projects/bar` parented by `organizations/foo`:Example 1 (no inherited values): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues:"E2"} `projects/bar` has `inheritFromParent` `false` and values: {allowedValues: "E3" allowedValues: "E4"} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are `E3`, and `E4`.Example 2 (inherited values): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues:"E2"} `projects/bar` has a `Policy` with values: {value: "E3" value: "E4" inheritFromParent: true} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are `E1`, `E2`, `E3`, and `E4`.Example 3 (inheriting both allowed and denied values): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues: "E2"} `projects/bar` has a `Policy` with: {deniedValues: "E1"} The accepted values at `organizations/foo` are `E1`, `E2`. The value accepted at `projects/bar` is `E2`.Example 4 (RestoreDefault): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues:"E2"} `projects/bar` has a `Policy` with values: {RestoreDefault: {}} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are either all or none depending on the value of `constraintDefault` (if `ALLOW`, all; if `DENY`, none).Example 5 (no policy inherits parent policy): `organizations/foo` has no `Policy` set. `projects/bar` has no `Policy` set. The accepted values at both levels are either all or none depending on the value of `constraintDefault` (if `ALLOW`, all; if `DENY`, none).Example 6 (ListConstraint allowing all): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues: "E2"} `projects/bar` has a `Policy` with: {all: ALLOW} The accepted values at `organizations/foo` are `E1`, E2`. Any value is accepted at`projects/bar`.Example 7 (ListConstraint allowing none): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues: "E2"} `projects/bar` has a `Policy` with: {all: DENY} The accepted values at `organizations/foo` are `E1`, E2`. No value is accepted at`projects/bar`.Example 10 (allowed and denied subtrees of Resource Manager hierarchy): Given the following resource hierarchy O1->{F1, F2}; F1->{P1}; F2->{P2, P3}, `organizations/foo` has a `Policy` with values: {allowedValues: "under:organizations/O1"} `projects/bar` has a `Policy` with: {allowedValues: "under:projects/P3"} {deniedValues: "under:folders/F2"} The accepted values at `organizations/foo` are `organizations/O1`, `folders/F1`, `folders/F2`, `projects/P1`, `projects/P2`, `projects/P3`. The accepted values at `projects/bar` are `organizations/O1`, `folders/F1`, `projects/P1`.  
  
## AllValues

This enum can be used to set `Policies` that apply to all possible configuration values rather than specific values in `allowedValues` or `deniedValues`.

Setting this to `ALLOW` will mean this `Policy` allows all values. Similarly, setting it to `DENY` will mean no values are allowed. If set to either `ALLOW` or `DENY,`allowedValues`and`deniedValues` must be unset. Setting this to`ALL_VALUES_UNSPECIFIED`allows for setting`allowedValues`and`deniedValues`.

Enums  
---  
`ALL_VALUES_UNSPECIFIED` | Indicates that allowedValues or deniedValues must be set.  
`ALLOW` | A policy with this set allows all values.  
`DENY` | A policy with this set denies all values.  
  
## BooleanPolicy

Used in `policyType` to specify how `booleanPolicy` will behave at this resource.

JSON representation  
---  
      
    
    {
      "enforced": boolean
    }  
  
Fields  
---  
`enforced` |  `boolean` If `true`, then the `Policy` is enforced. If `false`, then any configuration is acceptable.Suppose you have a `Constraint` `constraints/compute.disableSerialPortAccess` with `constraintDefault` set to `ALLOW`. A `Policy` for that `Constraint` exhibits the following behavior: - If the `Policy` at this resource has enforced set to `false`, serial port connection attempts will be allowed. - If the `Policy` at this resource has enforced set to `true`, serial port connection attempts will be refused. - If the `Policy` at this resource is `RestoreDefault`, serial port connection attempts will be allowed. - If no `Policy` is set at this resource or anywhere higher in the resource hierarchy, serial port connection attempts will be allowed. - If no `Policy` is set at this resource, but one exists higher in the resource hierarchy, the behavior is as if the`Policy` were set at this resource.The following examples demonstrate the different possible layerings:Example 1 (nearest `Constraint` wins): `organizations/foo` has a `Policy` with: {enforced: false} `projects/bar` has no `Policy` set. The constraint at `projects/bar` and `organizations/foo` will not be enforced.Example 2 (enforcement gets replaced): `organizations/foo` has a `Policy` with: {enforced: false} `projects/bar` has a `Policy` with: {enforced: true} The constraint at `organizations/foo` is not enforced. The constraint at `projects/bar` is enforced.Example 3 (RestoreDefault): `organizations/foo` has a `Policy` with: {enforced: true} `projects/bar` has a `Policy` with: {RestoreDefault: {}} The constraint at `organizations/foo` is enforced. The constraint at `projects/bar` is not enforced, because `constraintDefault` for the `Constraint` is `ALLOW`.  
  
## RestoreDefault

This type has no fields.

Ignores policies set above this resource and restores the `constraintDefault` enforcement behavior of the specific `Constraint` at this resource.

Suppose that `constraintDefault` is set to `ALLOW` for the `Constraint` `constraints/serviceuser.services`. Suppose that organization foo.com sets a `Policy` at their Organization resource node that restricts the allowed service activations to deny all service activations. They could then set a `Policy` with the `policyType` `restoreDefault` on several experimental projects, restoring the `constraintDefault` enforcement of the `Constraint` for only those projects, allowing those projects to have all services activated.

## AccessPolicy

`AccessPolicy` is a container for `AccessLevels` (which define the necessary attributes to use Google Cloud services) and `ServicePerimeters` (which define regions of services able to freely pass data within a perimeter). An access policy is globally visible within an organization, and the restrictions it specifies apply to all projects within an organization.

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
`name` |  `string` Output only. Identifier. Resource name of the `AccessPolicy`. Format: `accessPolicies/{accessPolicy}`  
`parent` |  `string` Required. The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organizationId}`  
`title` |  `string` Required. Human readable title. Does not affect behavior.  
`scopes[]` |  `string` The scopes of the `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessPolicy)`. Scopes define which resources a policy can restrict and where its resources can be referenced. For example, policy A with `scopes=["folders/123"]` has the following behavior:

  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` can only restrict projects within `folders/123`.
  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` within policy A can only reference access levels defined within policy A.
  * Only one policy can include a given scope; thus, attempting to create a second policy which includes `folders/123` will result in an error.

If no scopes are provided, then any resource within the organization can be restricted. Scopes cannot be modified after a policy is created. Policies can only have a single scope. Format: list of `folders/{folder_number}` or `projects/{projectNumber}`  
`etag` |  `string` Output only. An opaque identifier for the current version of the `AccessPolicy`. This will always be a strongly validated etag, meaning that two Access Policies will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format.  
  
## AccessLevel

An `AccessLevel` is a label that can be applied to requests to Google Cloud services, along with a list of requirements necessary for the label to be applied.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
    
      // Union field level can be only one of the following:
      "basic": {
        object ([BasicLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#BasicLevel))
      },
      "custom": {
        object ([CustomLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#CustomLevel))
      }
      // End of list of possible types for union field level.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for the `AccessLevel`. Format: `accessPolicies/{accessPolicy}/accessLevels/{accessLevel}`.The `accessLevel` component must begin with a letter, followed by alphanumeric characters or `_`. Its maximum length is 50 characters.After you create an `AccessLevel`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `AccessLevel` and its use. Does not affect behavior.  
Union field `level`. Required. Describes the necessary conditions for the level to apply. `level` can be only one of the following:  
`basic` |  `object (`[BasicLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#BasicLevel)`)` A `BasicLevel` composed of `Conditions`.  
`custom` |  `object (`[CustomLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#CustomLevel)`)` A `CustomLevel` written in the Common Expression Language.  
  
## BasicLevel

`BasicLevel` is an `AccessLevel` using a set of recommended features.

JSON representation  
---  
      
    
    {
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Condition))
        }
      ],
      "combiningFunction": enum ([ConditionCombiningFunction](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ConditionCombiningFunction))
    }  
  
Fields  
---  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Condition)`)` Required. A list of requirements for the `AccessLevel` to be granted.  
`combiningFunction` |  `enum (`[ConditionCombiningFunction](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ConditionCombiningFunction)`)` How the `conditions` list should be combined to determine if a request is granted this `AccessLevel`. If AND is used, each `Condition` in `conditions` must be satisfied for the `AccessLevel` to be applied. If OR is used, at least one `Condition` in `conditions` must be satisfied for the `AccessLevel` to be applied. Default behavior is AND.  
  
## Condition

A condition necessary for an `AccessLevel` to be granted. The Condition is an AND over its fields. So a Condition is true if: 1) the request IP is from one of the listed subnetworks AND 2) the originating device complies with the listed device policy AND 3) all listed access levels are granted AND 4) the request was sent at a time allowed by the DateTimeRestriction.

JSON representation  
---  
      
    
    {
      "ipSubnetworks": [
        string
      ],
      "devicePolicy": {
        object ([DevicePolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#DevicePolicy))
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
          object ([VpcNetworkSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VpcNetworkSource))
        }
      ]
    }  
  
Fields  
---  
`ipSubnetworks[]` |  `string` CIDR block IP subnetwork specification. May be IPv4 or IPv6. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly, for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32" is not. The originating IP of a request must be in one of the listed subnets in order for this Condition to be true. If empty, all IP addresses are allowed.  
`devicePolicy` |  `object (`[DevicePolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#DevicePolicy)`)` Device specific restrictions, all restrictions must hold for the Condition to be true. If not specified, all devices are allowed.  
`requiredAccessLevels[]` |  `string` A list of other access levels defined in the same `Policy`, referenced by resource name. Referencing an `AccessLevel` which does not exist is an error. All access levels listed must be granted for the Condition to be true. Example: "`accessPolicies/MY_POLICY/accessLevels/LEVEL_NAME"`  
`negate` |  `boolean` Whether to negate the Condition. If true, the Condition becomes a NAND over its non-empty fields. Any non-empty field criteria evaluating to false will result in the Condition to be satisfied. Defaults to false.  
`members[]` |  `string` The request must be made by one of the provided user or service accounts. Groups are not supported. Syntax: `user:{emailid}` `serviceAccount:{emailid}` If not specified, a request may come from any user.  
`regions[]` |  `string` The request must originate from one of the provided countries/regions. Must be valid ISO 3166-1 alpha-2 codes.  
`vpcNetworkSources[]` |  `object (`[VpcNetworkSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VpcNetworkSource)`)` The request must originate from one of the provided VPC networks in Google Cloud. Cannot specify this field together with `ipSubnetworks`.  
  
## DevicePolicy

`DevicePolicy` specifies device specific restrictions necessary to acquire a given access level. A `DevicePolicy` specifies requirements for requests from devices to be granted access levels, it does not do any enforcement on the device. `DevicePolicy` acts as an AND over all specified fields, and each repeated field is an OR over its elements. Any unset fields are ignored. For example, if the proto is { osType : DESKTOP_WINDOWS, osType : DESKTOP_LINUX, encryption_status: ENCRYPTED}, then the DevicePolicy will be true for requests originating from encrypted Linux desktops and encrypted Windows desktops.

JSON representation  
---  
      
    
    {
      "requireScreenlock": boolean,
      "allowedEncryptionStatuses": [
        enum ([DeviceEncryptionStatus](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#DeviceEncryptionStatus))
      ],
      "osConstraints": [
        {
          object ([OsConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OsConstraint))
        }
      ],
      "allowedDeviceManagementLevels": [
        enum ([DeviceManagementLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#DeviceManagementLevel))
      ],
      "requireAdminApproval": boolean,
      "requireCorpOwned": boolean
    }  
  
Fields  
---  
`requireScreenlock` |  `boolean` Whether or not screenlock is required for the DevicePolicy to be true. Defaults to `false`.  
`allowedEncryptionStatuses[]` |  `enum (`[DeviceEncryptionStatus](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#DeviceEncryptionStatus)`)` Allowed encryptions statuses, an empty list allows all statuses.  
`osConstraints[]` |  `object (`[OsConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OsConstraint)`)` Allowed OS versions, an empty list allows all types and all versions.  
`allowedDeviceManagementLevels[]` |  `enum (`[DeviceManagementLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#DeviceManagementLevel)`)` Allowed device management levels, an empty list allows all management levels.  
`requireAdminApproval` |  `boolean` Whether the device needs to be approved by the customer admin.  
`requireCorpOwned` |  `boolean` Whether the device needs to be corp owned.  
  
## DeviceEncryptionStatus

The encryption state of the device.

Enums  
---  
`ENCRYPTION_UNSPECIFIED` | The encryption status of the device is not specified or not known.  
`ENCRYPTION_UNSUPPORTED` | The device does not support encryption.  
`UNENCRYPTED` | The device supports encryption, but is currently unencrypted.  
`ENCRYPTED` | The device is encrypted.  
  
## OsConstraint

A restriction on the OS type and version of devices making requests.

JSON representation  
---  
      
    
    {
      "osType": enum ([OsType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OsType)),
      "minimumVersion": string,
      "requireVerifiedChromeOs": boolean
    }  
  
Fields  
---  
`osType` |  `enum (`[OsType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OsType)`)` Required. The allowed OS type.  
`minimumVersion` |  `string` The minimum allowed OS version. If not set, any version of this OS satisfies the constraint. Format: `"major.minor.patch"`. Examples: `"10.5.301"`, `"9.2.1"`.  
`requireVerifiedChromeOs` |  `boolean` Only allows requests from devices with a verified Chrome OS. Verifications includes requirements that the device is enterprise-managed, conformant to domain policies, and the caller has permission to call the API targeted by the request.  
  
## OsType

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
  
## DeviceManagementLevel

The degree to which the device is managed by the Cloud organization.

Enums  
---  
`MANAGEMENT_UNSPECIFIED` | The device's management level is not specified or not known.  
`NONE` | The device is not managed.  
`BASIC` | Basic management is enabled, which is generally limited to monitoring and wiping the corporate account.  
`COMPLETE` | Complete device management. This includes more thorough monitoring and the ability to directly manage the device (such as remote wiping). This can be enabled through the Android Enterprise Platform.  
  
## VpcNetworkSource

The originating network source in Google Cloud.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "vpcSubnetwork": {
        object ([VpcSubNetwork](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VpcSubNetwork))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The type of the originating network source of the request. `kind` can be only one of the following:  
`vpcSubnetwork` |  `object (`[VpcSubNetwork](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VpcSubNetwork)`)` Sub-segment ranges of a VPC network.  
  
## VpcSubNetwork

Sub-segment ranges inside of a VPC Network.

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
  
## ConditionCombiningFunction

Options for how the `conditions` list should be combined to determine if this `AccessLevel` is applied. Default is AND.

Enums  
---  
`AND` | All `Conditions` must be true for the `BasicLevel` to be true.  
`OR` | If at least one `Condition` is true, then the `BasicLevel` is true.  
  
## CustomLevel

`CustomLevel` is an `AccessLevel` using the Cloud Common Expression Language to represent the necessary conditions for the level to apply to a request. See CEL spec at: <https://github.com/google/cel-spec>

JSON representation  
---  
      
    
    {
      "expr": {
        object ([Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding#Expr))
      }
    }  
  
Fields  
---  
`expr` |  `object (`[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding#Expr)`)` Required. A Cloud CEL expression evaluating to a boolean.  
  
## ServicePerimeter

`ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project or VPC network can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
      "perimeterType": enum ([PerimeterType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#PerimeterType)),
      "status": {
        object ([ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeterConfig))
      },
      "spec": {
        object ([ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeterConfig))
      },
      "useExplicitDryRunSpec": boolean,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for the `ServicePerimeter`. Format: `accessPolicies/{accessPolicy}/servicePerimeters/{servicePerimeter}`.The `servicePerimeter` component must begin with a letter, followed by alphanumeric characters or `_`.After you create a `ServicePerimeter`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `ServicePerimeter` and its use. Does not affect behavior.  
`perimeterType` |  `enum (`[PerimeterType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#PerimeterType)`)` Perimeter type indicator. A single project or VPC network is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty.  
`status` |  `object (`[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeterConfig)`)` Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries.  
`spec` |  `object (`[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeterConfig)`)` Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "useExplicitDryRunSpec" flag is set.  
`useExplicitDryRunSpec` |  `boolean` Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.  
`etag` |  `string` Optional. An opaque identifier for the current version of the `ServicePerimeter`. This identifier does not follow any specific format. If an etag is not provided, the operation will be performed as if a valid etag is provided.  
  
## PerimeterType

Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter.

In addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by the regular perimeter that resource is in.

Perimeter Bridges are typically useful when building more complex toplogies with many independent perimeters that need to share some data with a common perimeter, but should not be able to share data among themselves.

Enums  
---  
`PERIMETER_TYPE_REGULAR` | Regular Perimeter. When no value is specified, the perimeter uses this type.  
`PERIMETER_TYPE_BRIDGE` | Perimeter Bridge.  
  
## ServicePerimeterConfig

`ServicePerimeterConfig` specifies a set of Google Cloud resources that describe specific Service Perimeter configuration.

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
        object ([VpcAccessibleServices](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VpcAccessibleServices))
      },
      "ingressPolicies": [
        {
          object ([IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy))
        }
      ],
      "egressPolicies": [
        {
          object ([EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy))
        }
      ]
    }  
  
Fields  
---  
`resources[]` |  `string` A list of Google Cloud resources that are inside of the service perimeter. Currently only projects and VPCs are allowed. Project format: `projects/{projectNumber}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`.  
`accessLevels[]` |  `string` A list of `AccessLevel` resource names that allow resources within the `ServicePerimeter` to be accessed from the internet. `AccessLevels` listed must be in the same policy as this `ServicePerimeter`. Referencing a nonexistent `AccessLevel` is a syntax error. If no `AccessLevel` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `"accessPolicies/MY_POLICY/accessLevels/MY_LEVEL"`. For Service Perimeter Bridge, must be empty.  
`restrictedServices[]` |  `string` Google Cloud services that are subject to the Service Perimeter restrictions. For example, if `storage.googleapis.com` is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions.  
`vpcAccessibleServices` |  `object (`[VpcAccessibleServices](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VpcAccessibleServices)`)` Configuration for APIs allowed within Perimeter.  
`ingressPolicies[]` |  `object (`[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)`)` List of `[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` to apply to the perimeter. A perimeter may have multiple `[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)`, each of which is evaluated separately. Access is granted if any `[Ingress Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` grants it. Must be empty for a perimeter bridge.  
`egressPolicies[]` |  `object (`[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)`)` List of `[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` to apply to the perimeter. A perimeter may have multiple `[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)`, each of which is evaluated separately. Access is granted if any `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` grants it. Must be empty for a perimeter bridge.  
  
## VpcAccessibleServices

Specifies how APIs are allowed to communicate within the Service Perimeter.

JSON representation  
---  
      
    
    {
      "enableRestriction": boolean,
      "allowedServices": [
        string
      ]
    }  
  
Fields  
---  
`enableRestriction` |  `boolean` Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'.  
`allowedServices[]` |  `string` The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True. You can specify a list of individual services, as well as include the 'RESTRICTED-SERVICES' value, which automatically includes all of the services protected by the perimeter.  
  
## IngressPolicy

Policy for ingress into `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`.

`[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` match requests based on `ingressFrom` and `ingressTo` stanzas. For an ingress policy to match, both the `ingressFrom` and `ingressTo` stanzas must be matched. If an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` matches a request, the request is allowed through the perimeter boundary from outside the perimeter.

For example, access from the internet can be allowed either based on an `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)` or, for traffic hosted on Google Cloud, the project of the source network. For access from private networks, using the project of the hosting network is required.

Individual ingress policies can be limited by restricting which services and/or actions they match using the `ingressTo` field.

JSON representation  
---  
      
    
    {
      "ingressFrom": {
        object ([IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressFrom))
      },
      "ingressTo": {
        object ([IngressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressTo))
      },
      "title": string
    }  
  
Fields  
---  
`ingressFrom` |  `object (`[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressFrom)`)` Defines the conditions on the source of a request causing this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` to apply.  
`ingressTo` |  `object (`[IngressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressTo)`)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` and request destination that cause this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the ingress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
## IngressFrom

Defines the conditions under which an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` matches a request. Conditions are based on information about the source of the request. The request must satisfy what is defined in `sources` AND identity related fields in order to match.

JSON representation  
---  
      
    
    {
      "sources": [
        {
          object ([IngressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressSource))
        }
      ],
      "identities": [
        string
      ],
      "identityType": enum ([IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IdentityType))
    }  
  
Fields  
---  
`sources[]` |  `object (`[IngressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressSource)`)` Sources that this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` authorizes access from.  
`identities[]` |  `string` A list of identities that are allowed access through [IngressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identityType` |  `enum (`[IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IdentityType)`)` Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
  
## IngressSource

The source that `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` authorizes access from.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "accessLevel": string,
      "resource": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Allowed ingress source. It can be one of `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)` or Google Cloud resource. `source` can be only one of the following:  
`accessLevel` |  `string` An `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)` resource name that allow resources within the `[ServicePerimeters](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` to be accessed from the internet. `[AccessLevels](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)` listed must be in the same policy as this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`. Referencing a nonexistent `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)` will cause an error. If no `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#AccessLevel)` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `accessLevel`, then all `[IngressSources](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressSource)` will be allowed.  
`resource` |  `string` A Google Cloud resource that is allowed to ingress the perimeter. Requests from these resources will be allowed to access perimeter data. Currently only projects and VPCs are allowed. Project format: `projects/{projectNumber}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`. The project may be in any Google Cloud organization, not just the organization that the perimeter is defined in. `*` is not allowed, the case of allowing all Google Cloud resources only is not supported.  
  
## IdentityType

Specifies the types of identities that are allowed access in either `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressFrom)` or `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom)` rules.

Enums  
---  
`IDENTITY_TYPE_UNSPECIFIED` | No blanket identity group specified.  
`ANY_IDENTITY` | Authorize access from all identities outside the perimeter.  
`ANY_USER_ACCOUNT` | Authorize access from all human users outside the perimeter.  
`ANY_SERVICE_ACCOUNT` | Authorize access from all service accounts outside the perimeter.  
  
## IngressTo

Defines the conditions under which an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` matches a request. Conditions are based on information about the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` intended to be performed on the target resource of the request. The request must satisfy what is defined in `operations` AND `resources` in order to match.

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation))
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
`operations[]` |  `object (`[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)`)` A list of `[ApiOperations](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` allowed to be performed by the sources specified in corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressFrom)` in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`.  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, protected by this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` that are allowed to be accessed by sources defined in the corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressFrom)`. If a single `*` is specified, then access to all resources inside the perimeter are allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressFrom)` are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`.  
  
## ApiOperation

Identification for an API Operation.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "methodSelectors": [
        {
          object ([MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#MethodSelector))
        }
      ]
    }  
  
Fields  
---  
`serviceName` |  `string` The name of the API whose methods or permissions the `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` or `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` want to allow. A single `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` with `serviceName` field set to `*` will allow all methods AND permissions for all services.  
`methodSelectors[]` |  `object (`[MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#MethodSelector)`)` API methods or permissions to allow. Method or permission must belong to the service specified by `serviceName` field. A single `[MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#MethodSelector)` entry with `*` specified for the `method` field will allow all methods AND permissions for the service specified in `serviceName`.  
  
## MethodSelector

An allowed method or permission of a service specified in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)`.

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
`method` |  `string` A valid method name for the corresponding `serviceName` in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)`. If `*` is used as the value for the `method`, then ALL methods and permissions are allowed.  
`permission` |  `string` A valid Cloud IAM permission for the corresponding `serviceName` in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)`.  
  
## EgressPolicy

Policy for egress from perimeter.

`[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` match requests based on `egressFrom` and `egressTo` stanzas. For an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` to match, both `egressFrom` and `egressTo` stanzas must be matched. If an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` matches a request, the request is allowed to span the `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` boundary. For example, an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` can be used to allow VMs on networks within the `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` to access a defined set of projects outside the perimeter in certain contexts (e.g. to read data from a Cloud Storage bucket or query against a BigQuery dataset).

`[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` are concerned with the _resources_ that a request relates as well as the API services and API actions being used. They do not related to the direction of data movement. More detailed documentation for this concept can be found in the descriptions of `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom)` and `[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressTo)`.

JSON representation  
---  
      
    
    {
      "egressFrom": {
        object ([EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom))
      },
      "egressTo": {
        object ([EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressTo))
      },
      "title": string
    }  
  
Fields  
---  
`egressFrom` |  `object (`[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom)`)` Defines conditions on the source of a request causing this `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` to apply.  
`egressTo` |  `object (`[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressTo)`)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` and destination resources that cause this `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the egress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
## EgressFrom

Defines the conditions under which an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`, then that `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` must have an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` which allows access in order for this request to succeed.

JSON representation  
---  
      
    
    {
      "identities": [
        string
      ],
      "identityType": enum ([IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IdentityType)),
      "sources": [
        {
          object ([EgressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressSource))
        }
      ],
      "sourceRestriction": enum ([SourceRestriction](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#SourceRestriction))
    }  
  
Fields  
---  
`identities[]` |  `string` A list of identities that are allowed access through [EgressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identityType` |  `enum (`[IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IdentityType)`)` Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
`sources[]` |  `object (`[EgressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressSource)`)` Sources that this [EgressPolicy] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressPolicy] authorizes access from. If this field is not empty, then `sourceRestriction` must be set to `SOURCE_RESTRICTION_ENABLED`.  
`sourceRestriction` |  `enum (`[SourceRestriction](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#SourceRestriction)`)` Whether to enforce traffic restrictions based on `sources` field. If the `sources` fields is non-empty, then this field must be set to `SOURCE_RESTRICTION_ENABLED`.  
  
## EgressSource

The source that [EgressPolicy] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressPolicy] authorizes access from inside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] to somewhere outside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] boundaries.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "accessLevel": string,
      "resource": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Allowed egress source. `source` can be only one of the following:  
`accessLevel` |  `string` An [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] resource name that allows protected resources inside the [ServicePerimeters] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] to access outside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] boundaries. [AccessLevels] [google.identity.accesscontextmanager.v1alpha.AccessLevel] listed must be in the same policy as this [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter]. Referencing a nonexistent [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] will cause an error. If an [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] name is not specified, only resources within the perimeter can be accessed through Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `accessLevel`, then all [EgressSources] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressSource] will be allowed.  
`resource` |  `string` A Google Cloud resource from the service perimeter that you want to allow to access data outside the perimeter. This field supports only projects. The project format is `projects/{projectNumber}`. You can't use `*` in this field to allow all Google Cloud resources.  
  
## SourceRestriction

Whether to enable the enforcement of traffic based on on the `sources` field. Only applies to [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].

Enums  
---  
`SOURCE_RESTRICTION_UNSPECIFIED` | Enforcement preference unspecified, will not enforce traffic restrictions based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
`SOURCE_RESTRICTION_ENABLED` | Enforcement preference enabled, traffic restrictions will be enforced based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
`SOURCE_RESTRICTION_DISABLED` | Enforcement preference disabled, will not enforce traffic restrictions based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
  
## EgressTo

Defines the conditions under which an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressPolicy)` matches a request. Conditions are based on information about the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` intended to be performed on the `resources` specified. Note that if the destination of the request is also protected by a `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`, then that `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)` must have an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#IngressPolicy)` which allows access in order for this request to succeed. The request must match `operations` AND `resources` fields in order to be allowed egress out of the perimeter.

JSON representation  
---  
      
    
    {
      "resources": [
        string
      ],
      "operations": [
        {
          object ([ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation))
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
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, that are allowed to be accessed by sources defined in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom)`. A request matches if it contains a resource in this list. If `*` is specified for `resources`, then this `[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressTo)` rule will authorize access to all resources outside the perimeter.  
`operations[]` |  `object (`[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)`)` A list of `[ApiOperations](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ApiOperation)` allowed to be performed by the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom)`. A request matches if it uses an operation/service in this list.  
`externalResources[]` |  `string` A list of external resources that are allowed to be accessed. Only AWS and Azure resources are supported. For Amazon S3, the supported formats are s3://BUCKET_NAME, s3a://BUCKET_NAME, and s3n://BUCKET_NAME. For Azure Storage, the supported format is <azure://myaccount.blob.core.windows.net/CONTAINER_NAME>. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#EgressFrom)`. are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ServicePerimeter)`.  
  
## Inventory

This API resource represents the available inventory data for a Compute Engine virtual machine (VM) instance at a given point in time.

You can use this API resource to determine the inventory data of your VM.

For more information, see [Information provided by OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).

JSON representation  
---  
      
    
    {
      "name": string,
      "osInfo": {
        object ([OsInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OsInfo))
      },
      "items": {
        string: {
          object ([Item](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Item))
        },
        ...
      },
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The `Inventory` API resource name.Format: `projects/{projectNumber}/locations/{location}/instances/{instance_id}/inventory`  
`osInfo` |  `object (`[OsInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OsInfo)`)` Base level operating system information for the VM.  
`items` |  `map (key: string, value: object (`[Item](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Item)`))` Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last reported inventory for the VM.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## OsInfo

Operating system information for the VM.

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
  
## Item

A single piece of inventory on a VM.

JSON representation  
---  
      
    
    {
      "id": string,
      "originType": enum ([OriginType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OriginType)),
      "createTime": string,
      "updateTime": string,
      "type": enum ([Type](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Type)),
    
      // Union field details can be only one of the following:
      "installedPackage": {
        object ([SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#SoftwarePackage))
      },
      "availablePackage": {
        object ([SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#SoftwarePackage))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`id` |  `string` Identifier for this item, unique across items for this VM.  
`originType` |  `enum (`[OriginType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#OriginType)`)` The origin of this inventory item.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When this inventory item was first detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When this inventory item was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Type)`)` The specific type of inventory, correlating to its specific details.  
Union field `details`. Specific details of this inventory item based on its type. `details` can be only one of the following:  
`installedPackage` |  `object (`[SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#SoftwarePackage)`)` Software package present on the VM instance.  
`availablePackage` |  `object (`[SoftwarePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#SoftwarePackage)`)` Software package available to be installed on the VM instance.  
  
## OriginType

The origin of a specific inventory item.

Enums  
---  
`ORIGIN_TYPE_UNSPECIFIED` | Invalid. An origin type must be specified.  
`INVENTORY_REPORT` | This inventory item was discovered as the result of the agent reporting inventory via the reporting API.  
  
## Type

The different types of inventory that are tracked on a VM.

Enums  
---  
`TYPE_UNSPECIFIED` | Invalid. A type must be specified.  
`INSTALLED_PACKAGE` | This represents a package that is installed on the VM.  
`AVAILABLE_PACKAGE` | This represents an update that is available for a package.  
  
## SoftwarePackage

Software package information of the operating system.

JSON representation  
---  
      
    
    {
    
      // Union field details can be only one of the following:
      "yumPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage))
      },
      "aptPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage))
      },
      "zypperPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage))
      },
      "googetPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage))
      },
      "zypperPatch": {
        object ([ZypperPatch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ZypperPatch))
      },
      "wuaPackage": {
        object ([WindowsUpdatePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsUpdatePackage))
      },
      "qfePackage": {
        object ([WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsQuickFixEngineeringPackage))
      },
      "cosPackage": {
        object ([VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage))
      },
      "windowsApplication": {
        object ([WindowsApplication](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsApplication))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
Union field `details`. Information about the different types of software packages. `details` can be only one of the following:  
`yumPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage)`)` Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.  
`aptPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage)`)` Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.  
`zypperPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage)`)` Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`googetPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage)`)` Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.  
`zypperPatch` |  `object (`[ZypperPatch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#ZypperPatch)`)` Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.  
`wuaPackage` |  `object (`[WindowsUpdatePackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsUpdatePackage)`)` Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.  
`qfePackage` |  `object (`[WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsQuickFixEngineeringPackage)`)` Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.  
`cosPackage` |  `object (`[VersionedPackage](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#VersionedPackage)`)` Details of a COS package.  
`windowsApplication` |  `object (`[WindowsApplication](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsApplication)`)` Details of Windows Application.  
  
## VersionedPackage

Information related to the a standard versioned package. This includes package info for APT, Yum, Zypper, and Googet package managers.

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
  
## ZypperPatch

Details related to a Zypper Patch.

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
  
## WindowsUpdatePackage

Details related to a Windows Update package. Field data and names are taken from Windows Update API IUpdate Interface: <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> Descriptive fields like title, and description are localized based on the locale of the VM being updated.

JSON representation  
---  
      
    
    {
      "title": string,
      "description": string,
      "categories": [
        {
          object ([WindowsUpdateCategory](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsUpdateCategory))
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
`categories[]` |  `object (`[WindowsUpdateCategory](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#WindowsUpdateCategory)`)` The categories that are associated with this update package.  
`kbArticleIds[]` |  `string` A collection of Microsoft Knowledge Base article IDs that are associated with the update package.  
`supportUrl` |  `string` A hyperlink to the language-specific support information for the update.  
`moreInfoUrls[]` |  `string` A collection of URLs that provide more information about the update package.  
`updateId` |  `string` Gets the identifier of an update package. Stays the same across revisions.  
`revisionNumber` |  `integer` The revision number of this update package.  
`lastDeploymentChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last published date of the update, in (UTC) date and time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## WindowsUpdateCategory

Categories specified by the Windows Update.

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
  
## WindowsQuickFixEngineeringPackage

Information related to a Quick Fix Engineering package. Fields are taken from Windows QuickFixEngineering Interface and match the source names: <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering>

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
  
## WindowsApplication

Contains information about a Windows application that is retrieved from the Windows Registry. For more information about these fields, see: <https://docs.microsoft.com/en-us/windows/win32/msi/uninstall-registry-key>

JSON representation  
---  
      
    
    {
      "displayName": string,
      "displayVersion": string,
      "publisher": string,
      "installDate": {
        object ([Date](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Date))
      },
      "helpLink": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the application or product.  
`displayVersion` |  `string` The version of the product or application in string format.  
`publisher` |  `string` The name of the manufacturer for the product or application.  
`installDate` |  `object (`[Date](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#Date)`)` The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product.  
`helpLink` |  `string` The internet address for technical support.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `google.type.TimeOfDay`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

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
  
## RelatedAssets

This item is deprecated!

DEPRECATED. This message only presents for the purpose of backward-compatibility. The server will never populate this message in responses. The detailed related assets with the `relationshipType`.

JSON representation  
---  
      
    
    {
      "relationshipAttributes": {
        object ([RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelationshipAttributes))
      },
      "assets": [
        {
          object ([RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelatedAsset))
        }
      ]
    }  
  
Fields  
---  
`relationshipAttributes` |  `object (`[RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelationshipAttributes)`)` The detailed relationship attributes.  
`assets[]` |  `object (`[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset#RelatedAsset)`)` The peer resources of the relationship.  
  
## RelationshipAttributes

This item is deprecated!

DEPRECATED. This message only presents for the purpose of backward-compatibility. The server will never populate this message in responses. The relationship attributes which include `type`, `sourceResourceType`, `targetResourceType` and `action`.

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
  
## RelatedAsset

An asset identifier in Google Cloud which contains its name, type and ancestors. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
