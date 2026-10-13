---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1
title: Package google.identity.accesscontextmanager.v1 \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:11.695602+00:00
---

# Package google.identity.accesscontextmanager.v1  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.identity.accesscontextmanager.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` (message)
  * `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessPolicy)` (message)
  * `[BasicLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.BasicLevel)` (message)
  * `[BasicLevel.ConditionCombiningFunction](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.BasicLevel.ConditionCombiningFunction)` (enum)
  * `[Condition](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.Condition)` (message)
  * `[CustomLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.CustomLevel)` (message)
  * `[DevicePolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.DevicePolicy)` (message)
  * `[OsConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.OsConstraint)` (message)
  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` (message)
  * `[ServicePerimeter.PerimeterType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter.PerimeterType)` (enum)
  * `[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig)` (message)
  * `[ServicePerimeterConfig.ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` (message)
  * `[ServicePerimeterConfig.EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)` (message)
  * `[ServicePerimeterConfig.EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` (message)
  * `[ServicePerimeterConfig.EgressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressSource)` (message)
  * `[ServicePerimeterConfig.EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressTo)` (message)
  * `[ServicePerimeterConfig.IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType)` (enum)
  * `[ServicePerimeterConfig.IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` (message)
  * `[ServicePerimeterConfig.IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` (message)
  * `[ServicePerimeterConfig.IngressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)` (message)
  * `[ServicePerimeterConfig.IngressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressTo)` (message)
  * `[ServicePerimeterConfig.MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.MethodSelector)` (message)
  * `[ServicePerimeterConfig.SourceRestriction](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.SourceRestriction)` (enum)
  * `[ServicePerimeterConfig.VpcAccessibleServices](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices)` (message)
  * `[VpcNetworkSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.VpcNetworkSource)` (message)
  * `[VpcSubNetwork](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.VpcSubNetwork)` (message)



## AccessLevel

An `AccessLevel` is a label that can be applied to requests to Google Cloud services, along with a list of requirements necessary for the label to be applied.

Fields  
---  
`name` |  `string` Identifier. Resource name for the `AccessLevel`. Format: `accessPolicies/{access_policy}/accessLevels/{access_level}`.The `access_level` component must begin with a letter, followed by alphanumeric characters or `_`. Its maximum length is 50 characters.After you create an `AccessLevel`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `AccessLevel` and its use. Does not affect behavior.  
Union field `level`. Required. Describes the necessary conditions for the level to apply. `level` can be only one of the following:  
`basic` |  `[BasicLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.BasicLevel)` A `BasicLevel` composed of `Conditions`.  
`custom` |  `[CustomLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.CustomLevel)` A `CustomLevel` written in the Common Expression Language.  
  
## AccessPolicy

`AccessPolicy` is a container for `AccessLevels` (which define the necessary attributes to use Google Cloud services) and `ServicePerimeters` (which define regions of services able to freely pass data within a perimeter). An access policy is globally visible within an organization, and the restrictions it specifies apply to all projects within an organization.

Fields  
---  
`name` |  `string` Output only. Identifier. Resource name of the `AccessPolicy`. Format: `accessPolicies/{access_policy}`  
`parent` |  `string` Required. The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organization_id}`  
`title` |  `string` Required. Human readable title. Does not affect behavior.  
`scopes[]` |  `string` The scopes of the `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessPolicy)`. Scopes define which resources a policy can restrict and where its resources can be referenced. For example, policy A with `scopes=["folders/123"]` has the following behavior:

  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` can only restrict projects within `folders/123`.
  * `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` within policy A can only reference access levels defined within policy A.
  * Only one policy can include a given scope; thus, attempting to create a second policy which includes `folders/123` will result in an error.

If no scopes are provided, then any resource within the organization can be restricted. Scopes cannot be modified after a policy is created. Policies can only have a single scope. Format: list of `folders/{folder_number}` or `projects/{project_number}`  
`etag` |  `string` Output only. An opaque identifier for the current version of the `AccessPolicy`. This will always be a strongly validated etag, meaning that two Access Policies will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format.  
  
## BasicLevel

`BasicLevel` is an `AccessLevel` using a set of recommended features.

Fields  
---  
`conditions[]` |  `[Condition](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.Condition)` Required. A list of requirements for the `AccessLevel` to be granted.  
`combining_function` |  `[ConditionCombiningFunction](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.BasicLevel.ConditionCombiningFunction)` How the `conditions` list should be combined to determine if a request is granted this `AccessLevel`. If AND is used, each `Condition` in `conditions` must be satisfied for the `AccessLevel` to be applied. If OR is used, at least one `Condition` in `conditions` must be satisfied for the `AccessLevel` to be applied. Default behavior is AND.  
  
## ConditionCombiningFunction

Options for how the `conditions` list should be combined to determine if this `AccessLevel` is applied. Default is AND.

Enums  
---  
`AND` | All `Conditions` must be true for the `BasicLevel` to be true.  
`OR` | If at least one `Condition` is true, then the `BasicLevel` is true.  
  
## Condition

A condition necessary for an `AccessLevel` to be granted. The Condition is an AND over its fields. So a Condition is true if: 1) the request IP is from one of the listed subnetworks AND 2) the originating device complies with the listed device policy AND 3) all listed access levels are granted AND 4) the request was sent at a time allowed by the DateTimeRestriction.

Fields  
---  
`ip_subnetworks[]` |  `string` CIDR block IP subnetwork specification. May be IPv4 or IPv6. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly, for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32" is not. The originating IP of a request must be in one of the listed subnets in order for this Condition to be true. If empty, all IP addresses are allowed.  
`device_policy` |  `[DevicePolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.DevicePolicy)` Device specific restrictions, all restrictions must hold for the Condition to be true. If not specified, all devices are allowed.  
`required_access_levels[]` |  `string` A list of other access levels defined in the same `Policy`, referenced by resource name. Referencing an `AccessLevel` which does not exist is an error. All access levels listed must be granted for the Condition to be true. Example: "`accessPolicies/MY_POLICY/accessLevels/LEVEL_NAME"`  
`negate` |  `bool` Whether to negate the Condition. If true, the Condition becomes a NAND over its non-empty fields. Any non-empty field criteria evaluating to false will result in the Condition to be satisfied. Defaults to false.  
`members[]` |  `string` The request must be made by one of the provided user or service accounts. Groups are not supported. Syntax: `user:{emailid}` `serviceAccount:{emailid}` If not specified, a request may come from any user.  
`regions[]` |  `string` The request must originate from one of the provided countries/regions. Must be valid ISO 3166-1 alpha-2 codes.  
`vpc_network_sources[]` |  `[VpcNetworkSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.VpcNetworkSource)` The request must originate from one of the provided VPC networks in Google Cloud. Cannot specify this field together with `ip_subnetworks`.  
  
## CustomLevel

`CustomLevel` is an `AccessLevel` using the Cloud Common Expression Language to represent the necessary conditions for the level to apply to a request. See CEL spec at: <https://github.com/google/cel-spec>

Fields  
---  
`expr` |  `[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.type#google.type.Expr)` Required. A Cloud CEL expression evaluating to a boolean.  
  
## DevicePolicy

`DevicePolicy` specifies device specific restrictions necessary to acquire a given access level. A `DevicePolicy` specifies requirements for requests from devices to be granted access levels, it does not do any enforcement on the device. `DevicePolicy` acts as an AND over all specified fields, and each repeated field is an OR over its elements. Any unset fields are ignored. For example, if the proto is { os_type : DESKTOP_WINDOWS, os_type : DESKTOP_LINUX, encryption_status: ENCRYPTED}, then the DevicePolicy will be true for requests originating from encrypted Linux desktops and encrypted Windows desktops.

Fields  
---  
`require_screenlock` |  `bool` Whether or not screenlock is required for the DevicePolicy to be true. Defaults to `false`.  
`allowed_encryption_statuses[]` |  `[DeviceEncryptionStatus](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.DeviceEncryptionStatus)` Allowed encryptions statuses, an empty list allows all statuses.  
`os_constraints[]` |  `[OsConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.OsConstraint)` Allowed OS versions, an empty list allows all types and all versions.  
`allowed_device_management_levels[]` |  `[DeviceManagementLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.DeviceManagementLevel)` Allowed device management levels, an empty list allows all management levels.  
`require_admin_approval` |  `bool` Whether the device needs to be approved by the customer admin.  
`require_corp_owned` |  `bool` Whether the device needs to be corp owned.  
  
## OsConstraint

A restriction on the OS type and version of devices making requests.

Fields  
---  
`os_type` |  `[OsType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.OsType)` Required. The allowed OS type.  
`minimum_version` |  `string` The minimum allowed OS version. If not set, any version of this OS satisfies the constraint. Format: `"major.minor.patch"`. Examples: `"10.5.301"`, `"9.2.1"`.  
`require_verified_chrome_os` |  `bool` Only allows requests from devices with a verified Chrome OS. Verifications includes requirements that the device is enterprise-managed, conformant to domain policies, and the caller has permission to call the API targeted by the request.  
  
## ServicePerimeter

`ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project or VPC network can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

Fields  
---  
`name` |  `string` Identifier. Resource name for the `ServicePerimeter`. Format: `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`.The `service_perimeter` component must begin with a letter, followed by alphanumeric characters or `_`.After you create a `ServicePerimeter`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `ServicePerimeter` and its use. Does not affect behavior.  
`perimeter_type` |  `[PerimeterType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter.PerimeterType)` Perimeter type indicator. A single project or VPC network is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty.  
`status` |  `[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig)` Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries.  
`spec` |  `[ServicePerimeterConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig)` Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set.  
`use_explicit_dry_run_spec` |  `bool` Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values.  
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

Fields  
---  
`resources[]` |  `string` A list of Google Cloud resources that are inside of the service perimeter. Currently only projects and VPCs are allowed. Project format: `projects/{project_number}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`.  
`access_levels[]` |  `string` A list of `AccessLevel` resource names that allow resources within the `ServicePerimeter` to be accessed from the internet. `AccessLevels` listed must be in the same policy as this `ServicePerimeter`. Referencing a nonexistent `AccessLevel` is a syntax error. If no `AccessLevel` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `"accessPolicies/MY_POLICY/accessLevels/MY_LEVEL"`. For Service Perimeter Bridge, must be empty.  
`restricted_services[]` |  `string` Google Cloud services that are subject to the Service Perimeter restrictions. For example, if `storage.googleapis.com` is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions.  
`vpc_accessible_services` |  `[VpcAccessibleServices](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices)` Configuration for APIs allowed within Perimeter.  
`ingress_policies[]` |  `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` List of `[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` to apply to the perimeter. A perimeter may have multiple `[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)`, each of which is evaluated separately. Access is granted if any `[Ingress Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` grants it. Must be empty for a perimeter bridge.  
`egress_policies[]` |  `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` List of `[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` to apply to the perimeter. A perimeter may have multiple `[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)`, each of which is evaluated separately. Access is granted if any `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` grants it. Must be empty for a perimeter bridge.  
  
## ApiOperation

Identification for an API Operation.

Fields  
---  
`service_name` |  `string` The name of the API whose methods or permissions the `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` or `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` want to allow. A single `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` with `service_name` field set to `*` will allow all methods AND permissions for all services.  
`method_selectors[]` |  `[MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.MethodSelector)` API methods or permissions to allow. Method or permission must belong to the service specified by `service_name` field. A single `[MethodSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.MethodSelector)` entry with `*` specified for the `method` field will allow all methods AND permissions for the service specified in `service_name`.  
  
## EgressFrom

Defines the conditions under which an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`, then that `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` must have an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` which allows access in order for this request to succeed.

Fields  
---  
`identities[]` |  `string` A list of identities that are allowed access through [EgressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identity_type` |  `[IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType)` Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
`sources[]` |  `[EgressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressSource)` Sources that this [EgressPolicy] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressPolicy] authorizes access from. If this field is not empty, then `source_restriction` must be set to `SOURCE_RESTRICTION_ENABLED`.  
`source_restriction` |  `[SourceRestriction](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.SourceRestriction)` Whether to enforce traffic restrictions based on `sources` field. If the `sources` fields is non-empty, then this field must be set to `SOURCE_RESTRICTION_ENABLED`.  
  
## EgressPolicy

Policy for egress from perimeter.

`[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` match requests based on `egress_from` and `egress_to` stanzas. For an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` to match, both `egress_from` and `egress_to` stanzas must be matched. If an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` matches a request, the request is allowed to span the `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` boundary. For example, an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` can be used to allow VMs on networks within the `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` to access a defined set of projects outside the perimeter in certain contexts (e.g. to read data from a Cloud Storage bucket or query against a BigQuery dataset).

`[EgressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` are concerned with the _resources_ that a request relates as well as the API services and API actions being used. They do not related to the direction of data movement. More detailed documentation for this concept can be found in the descriptions of `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)` and `[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressTo)`.

Fields  
---  
`egress_from` |  `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)` Defines conditions on the source of a request causing this `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` to apply.  
`egress_to` |  `[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressTo)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` and destination resources that cause this `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the egress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
## EgressSource

The source that [EgressPolicy] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressPolicy] authorizes access from inside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] to somewhere outside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] boundaries.

Fields  
---  
Union field `source`. Allowed egress source. `source` can be only one of the following:  
`access_level` |  `string` An [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] resource name that allows protected resources inside the [ServicePerimeters] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] to access outside the [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter] boundaries. [AccessLevels] [google.identity.accesscontextmanager.v1alpha.AccessLevel] listed must be in the same policy as this [ServicePerimeter] [google.identity.accesscontextmanager.v1alpha.ServicePerimeter]. Referencing a nonexistent [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] will cause an error. If an [AccessLevel] [google.identity.accesscontextmanager.v1alpha.AccessLevel] name is not specified, only resources within the perimeter can be accessed through Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `access_level`, then all [EgressSources] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressSource] will be allowed.  
`resource` |  `string` A Google Cloud resource from the service perimeter that you want to allow to access data outside the perimeter. This field supports only projects. The project format is `projects/{project_number}`. You can't use `*` in this field to allow all Google Cloud resources.  
  
## EgressTo

Defines the conditions under which an `[EgressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy)` matches a request. Conditions are based on information about the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` intended to be performed on the `resources` specified. Note that if the destination of the request is also protected by a `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`, then that `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` must have an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` which allows access in order for this request to succeed. The request must match `operations` AND `resources` fields in order to be allowed egress out of the perimeter.

Fields  
---  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, that are allowed to be accessed by sources defined in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)`. A request matches if it contains a resource in this list. If `*` is specified for `resources`, then this `[EgressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressTo)` rule will authorize access to all resources outside the perimeter.  
`operations[]` |  `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` A list of `[ApiOperations](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` allowed to be performed by the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)`. A request matches if it uses an operation/service in this list.  
`external_resources[]` |  `string` A list of external resources that are allowed to be accessed. Only AWS and Azure resources are supported. For Amazon S3, the supported formats are s3://BUCKET_NAME, s3a://BUCKET_NAME, and s3n://BUCKET_NAME. For Azure Storage, the supported format is <azure://myaccount.blob.core.windows.net/CONTAINER_NAME>. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)`. are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`.  
  
## IdentityType

Specifies the types of identities that are allowed access in either `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` or `[EgressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom)` rules.

Enums  
---  
`IDENTITY_TYPE_UNSPECIFIED` | No blanket identity group specified.  
`ANY_IDENTITY` | Authorize access from all identities outside the perimeter.  
`ANY_USER_ACCOUNT` | Authorize access from all human users outside the perimeter.  
`ANY_SERVICE_ACCOUNT` | Authorize access from all service accounts outside the perimeter.  
  
## IngressFrom

Defines the conditions under which an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` matches a request. Conditions are based on information about the source of the request. The request must satisfy what is defined in `sources` AND identity related fields in order to match.

Fields  
---  
`sources[]` |  `[IngressSource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)` Sources that this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` authorizes access from.  
`identities[]` |  `string` A list of identities that are allowed access through [IngressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identity_type` |  `[IdentityType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType)` Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
  
## IngressPolicy

Policy for ingress into `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`.

`[IngressPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` match requests based on `ingress_from` and `ingress_to` stanzas. For an ingress policy to match, both the `ingress_from` and `ingress_to` stanzas must be matched. If an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` matches a request, the request is allowed through the perimeter boundary from outside the perimeter.

For example, access from the internet can be allowed either based on an `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` or, for traffic hosted on Google Cloud, the project of the source network. For access from private networks, using the project of the hosting network is required.

Individual ingress policies can be limited by restricting which services and/or actions they match using the `ingress_to` field.

Fields  
---  
`ingress_from` |  `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` Defines the conditions on the source of a request causing this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` to apply.  
`ingress_to` |  `[IngressTo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressTo)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` and request destination that cause this `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the ingress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
## IngressSource

The source that `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` authorizes access from.

Fields  
---  
Union field `source`. Allowed ingress source. It can be one of `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` or Google Cloud resource. `source` can be only one of the following:  
`access_level` |  `string` An `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` resource name that allow resources within the `[ServicePerimeters](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` to be accessed from the internet. `[AccessLevels](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` listed must be in the same policy as this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`. Referencing a nonexistent `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` will cause an error. If no `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `access_level`, then all `[IngressSources](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)` will be allowed.  
`resource` |  `string` A Google Cloud resource that is allowed to ingress the perimeter. Requests from these resources will be allowed to access perimeter data. Currently only projects and VPCs are allowed. Project format: `projects/{project_number}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`. The project may be in any Google Cloud organization, not just the organization that the perimeter is defined in. `*` is not allowed, the case of allowing all Google Cloud resources only is not supported.  
  
## IngressTo

Defines the conditions under which an `[IngressPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy)` matches a request. Conditions are based on information about the `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` intended to be performed on the target resource of the request. The request must satisfy what is defined in `operations` AND `resources` in order to match.

Fields  
---  
`operations[]` |  `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` A list of `[ApiOperations](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)` allowed to be performed by the sources specified in corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`.  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, protected by this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` that are allowed to be accessed by sources defined in the corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)`. If a single `*` is specified, then access to all resources inside the perimeter are allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[IngressFrom](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)`.  
  
## MethodSelector

An allowed method or permission of a service specified in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)`.

Fields  
---  
Union field `kind`. The API method name or Cloud IAM permission name to allow. `kind` can be only one of the following:  
`method` |  `string` A valid method name for the corresponding `service_name` in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)`. If `*` is used as the value for the `method`, then ALL methods and permissions are allowed.  
`permission` |  `string` A valid Cloud IAM permission for the corresponding `service_name` in `[ApiOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation)`.  
  
## SourceRestriction

Whether to enable the enforcement of traffic based on on the `sources` field. Only applies to [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].

Enums  
---  
`SOURCE_RESTRICTION_UNSPECIFIED` | Enforcement preference unspecified, will not enforce traffic restrictions based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
`SOURCE_RESTRICTION_ENABLED` | Enforcement preference enabled, traffic restrictions will be enforced based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
`SOURCE_RESTRICTION_DISABLED` | Enforcement preference disabled, will not enforce traffic restrictions based on `sources` in [EgressFrom] [google.identity.accesscontextmanager.v1alpha.ServicePerimeterConfig.EgressFrom].  
  
## VpcAccessibleServices

Specifies how APIs are allowed to communicate within the Service Perimeter.

Fields  
---  
`enable_restriction` |  `bool` Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowed_services'.  
`allowed_services[]` |  `string` The list of APIs usable within the Service Perimeter. Must be empty unless 'enable_restriction' is True. You can specify a list of individual services, as well as include the 'RESTRICTED-SERVICES' value, which automatically includes all of the services protected by the perimeter.  
  
## VpcNetworkSource

The originating network source in Google Cloud.

Fields  
---  
Union field `kind`. The type of the originating network source of the request. `kind` can be only one of the following:  
`vpc_subnetwork` |  `[VpcSubNetwork](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.VpcSubNetwork)` Sub-segment ranges of a VPC network.  
  
## VpcSubNetwork

Sub-segment ranges inside of a VPC Network.

Fields  
---  
`network` |  `string` Required. Network name. If the network is not part of the organization, the `compute.network.get` permission must be granted to the caller. Format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NETWORK_NAME}` Example: `//compute.googleapis.com/projects/my-project/global/networks/network-1`  
`vpc_ip_subnetworks[]` |  `string` CIDR block IP subnetwork specification. The IP address must be an IPv4 address and can be a public or private IP address. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. If empty, all IP addresses are allowed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
