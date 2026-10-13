---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetOrBuilder
title: Interface AssetOrBuilder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:22.259134+00:00
---

# Interface AssetOrBuilder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AssetOrBuilder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.2-SNAPSHOT  3.6.0  3.4.1  3.3.1  3.2.17 
    
    
    public interface AssetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessContextPolicyCase()
    
    
    public abstract Asset.AccessContextPolicyCase getAccessContextPolicyCase()

**Returns**  
---  
**Type** | **Description**  
`[Asset.AccessContextPolicyCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Asset.AccessContextPolicyCase)` |   
  
### getAccessLevel()
    
    
    public abstract AccessLevel getAccessLevel()

Also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).

`.google.identity.accesscontextmanager.v1.AccessLevel access_level = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.identity.accesscontextmanager.v1.AccessLevel` | The accessLevel.  
  
### getAccessLevelOrBuilder()
    
    
    public abstract AccessLevelOrBuilder getAccessLevelOrBuilder()

Also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).

`.google.identity.accesscontextmanager.v1.AccessLevel access_level = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.identity.accesscontextmanager.v1.AccessLevelOrBuilder` |   
  
### getAccessPolicy()
    
    
    public abstract AccessPolicy getAccessPolicy()

Also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).

`.google.identity.accesscontextmanager.v1.AccessPolicy access_policy = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.identity.accesscontextmanager.v1.AccessPolicy` | The accessPolicy.  
  
### getAccessPolicyOrBuilder()
    
    
    public abstract AccessPolicyOrBuilder getAccessPolicyOrBuilder()

Also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).

`.google.identity.accesscontextmanager.v1.AccessPolicy access_policy = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.identity.accesscontextmanager.v1.AccessPolicyOrBuilder` |   
  
### getAncestors(int index)
    
    
    public abstract String getAncestors(int index)

The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.

Example: `["projects/123456789", "folders/5432", "organizations/1234"]`

`repeated string ancestors = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ancestors at the given index.  
  
### getAncestorsBytes(int index)
    
    
    public abstract ByteString getAncestorsBytes(int index)

The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.

Example: `["projects/123456789", "folders/5432", "organizations/1234"]`

`repeated string ancestors = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the ancestors at the given index.  
  
### getAncestorsCount()
    
    
    public abstract int getAncestorsCount()

The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.

Example: `["projects/123456789", "folders/5432", "organizations/1234"]`

`repeated string ancestors = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of ancestors.  
  
### getAncestorsList()
    
    
    public abstract List<String> getAncestorsList()

The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.

Example: `["projects/123456789", "folders/5432", "organizations/1234"]`

`repeated string ancestors = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the ancestors.  
  
### getAssetType()
    
    
    public abstract String getAssetType()

The type of the asset. Example: `compute.googleapis.com/Disk`

See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

`string asset_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The assetType.  
  
### getAssetTypeBytes()
    
    
    public abstract ByteString getAssetTypeBytes()

The type of the asset. Example: `compute.googleapis.com/Disk`

See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

`string asset_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for assetType.  
  
### getIamPolicy()
    
    
    public abstract Policy getIamPolicy()

A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.

`.google.iam.v1.Policy iam_policy = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` | The iamPolicy.  
  
### getIamPolicyOrBuilder()
    
    
    public abstract PolicyOrBuilder getIamPolicyOrBuilder()

A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.

`.google.iam.v1.Policy iam_policy = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.PolicyOrBuilder` |   
  
### getName()
    
    
    public abstract String getName()

The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`

See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`

See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOrgPolicy(int index)
    
    
    public abstract Policy getOrgPolicy(int index)

A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.

`repeated .google.cloud.orgpolicy.v1.Policy org_policy = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.orgpolicy.v1.Policy` |   
  
### getOrgPolicyCount()
    
    
    public abstract int getOrgPolicyCount()

A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.

`repeated .google.cloud.orgpolicy.v1.Policy org_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOrgPolicyList()
    
    
    public abstract List<Policy> getOrgPolicyList()

A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.

`repeated .google.cloud.orgpolicy.v1.Policy org_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.cloud.orgpolicy.v1.Policy>` |   
  
### getOrgPolicyOrBuilder(int index)
    
    
    public abstract PolicyOrBuilder getOrgPolicyOrBuilder(int index)

A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.

`repeated .google.cloud.orgpolicy.v1.Policy org_policy = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.orgpolicy.v1.PolicyOrBuilder` |   
  
### getOrgPolicyOrBuilderList()
    
    
    public abstract List<? extends PolicyOrBuilder> getOrgPolicyOrBuilderList()

A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.

`repeated .google.cloud.orgpolicy.v1.Policy org_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.orgpolicy.v1.PolicyOrBuilder>` |   
  
### getOsInventory()
    
    
    public abstract Inventory getOsInventory()

A representation of runtime OS Inventory information. See [this topic](https://cloud.google.com/compute/docs/instances/os-inventory-management) for more information.

`.google.cloud.osconfig.v1.Inventory os_inventory = 12;`

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.osconfig.v1.Inventory` | The osInventory.  
  
### getOsInventoryOrBuilder()
    
    
    public abstract InventoryOrBuilder getOsInventoryOrBuilder()

A representation of runtime OS Inventory information. See [this topic](https://cloud.google.com/compute/docs/instances/os-inventory-management) for more information.

`.google.cloud.osconfig.v1.Inventory os_inventory = 12;`

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.osconfig.v1.InventoryOrBuilder` |   
  
### getRelatedAsset()
    
    
    public abstract RelatedAsset getRelatedAsset()

One related asset of the current asset.

`.google.cloud.asset.v1.RelatedAsset related_asset = 15;`

**Returns**  
---  
**Type** | **Description**  
`[RelatedAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.RelatedAsset)` | The relatedAsset.  
  
### getRelatedAssetOrBuilder()
    
    
    public abstract RelatedAssetOrBuilder getRelatedAssetOrBuilder()

One related asset of the current asset.

`.google.cloud.asset.v1.RelatedAsset related_asset = 15;`

**Returns**  
---  
**Type** | **Description**  
`[RelatedAssetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.RelatedAssetOrBuilder)` |   
  
### getRelatedAssets() (deprecated)
    
    
    public abstract RelatedAssets getRelatedAssets()

**Deprecated.** _google.cloud.asset.v1.Asset.related_assets is deprecated. See google/cloud/asset/v1/assets.proto;l=177_

DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.

`.google.cloud.asset.v1.RelatedAssets related_assets = 13 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[RelatedAssets](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.RelatedAssets)` | The relatedAssets.  
  
### getRelatedAssetsOrBuilder() (deprecated)
    
    
    public abstract RelatedAssetsOrBuilder getRelatedAssetsOrBuilder()

DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.

`.google.cloud.asset.v1.RelatedAssets related_assets = 13 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[RelatedAssetsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.RelatedAssetsOrBuilder)` |   
  
### getResource()
    
    
    public abstract Resource getResource()

A representation of the resource.

`.google.cloud.asset.v1.Resource resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Resource](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Resource)` | The resource.  
  
### getResourceOrBuilder()
    
    
    public abstract ResourceOrBuilder getResourceOrBuilder()

A representation of the resource.

`.google.cloud.asset.v1.Resource resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ResourceOrBuilder)` |   
  
### getServicePerimeter()
    
    
    public abstract ServicePerimeter getServicePerimeter()

Also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).

`.google.identity.accesscontextmanager.v1.ServicePerimeter service_perimeter = 9;`

**Returns**  
---  
**Type** | **Description**  
`com.google.identity.accesscontextmanager.v1.ServicePerimeter` | The servicePerimeter.  
  
### getServicePerimeterOrBuilder()
    
    
    public abstract ServicePerimeterOrBuilder getServicePerimeterOrBuilder()

Also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).

`.google.identity.accesscontextmanager.v1.ServicePerimeter service_perimeter = 9;`

**Returns**  
---  
**Type** | **Description**  
`com.google.identity.accesscontextmanager.v1.ServicePerimeterOrBuilder` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.

`.google.protobuf.Timestamp update_time = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.

`.google.protobuf.Timestamp update_time = 11;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAccessLevel()
    
    
    public abstract boolean hasAccessLevel()

Also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).

`.google.identity.accesscontextmanager.v1.AccessLevel access_level = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accessLevel field is set.  
  
### hasAccessPolicy()
    
    
    public abstract boolean hasAccessPolicy()

Also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).

`.google.identity.accesscontextmanager.v1.AccessPolicy access_policy = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accessPolicy field is set.  
  
### hasIamPolicy()
    
    
    public abstract boolean hasIamPolicy()

A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.

`.google.iam.v1.Policy iam_policy = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the iamPolicy field is set.  
  
### hasOsInventory()
    
    
    public abstract boolean hasOsInventory()

A representation of runtime OS Inventory information. See [this topic](https://cloud.google.com/compute/docs/instances/os-inventory-management) for more information.

`.google.cloud.osconfig.v1.Inventory os_inventory = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the osInventory field is set.  
  
### hasRelatedAsset()
    
    
    public abstract boolean hasRelatedAsset()

One related asset of the current asset.

`.google.cloud.asset.v1.RelatedAsset related_asset = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the relatedAsset field is set.  
  
### hasRelatedAssets() (deprecated)
    
    
    public abstract boolean hasRelatedAssets()

**Deprecated.** _google.cloud.asset.v1.Asset.related_assets is deprecated. See google/cloud/asset/v1/assets.proto;l=177_

DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.

`.google.cloud.asset.v1.RelatedAssets related_assets = 13 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the relatedAssets field is set.  
  
### hasResource()
    
    
    public abstract boolean hasResource()

A representation of the resource.

`.google.cloud.asset.v1.Resource resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resource field is set.  
  
### hasServicePerimeter()
    
    
    public abstract boolean hasServicePerimeter()

Also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).

`.google.identity.accesscontextmanager.v1.ServicePerimeter service_perimeter = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the servicePerimeter field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.

`.google.protobuf.Timestamp update_time = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
