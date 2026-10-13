---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName
title: Oracle Database@Google Cloud v1 API - Class DbNodeName (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:21.095963+00:00
---

# Oracle Database@Google Cloud v1 API - Class DbNodeName (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class DbNodeName (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class DbNodeName : IResourceName, IEquatable<DbNodeName>

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class DbNodeName.

Resource name for the `DbNode` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DbNodeName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### DbNodeName(string, string, string, string)
    
    
    public DbNodeName(string projectId, string locationId, string cloudVmClusterId, string dbNodeId)

Constructs a new instance of a [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) class from the component parts of pattern `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudVmClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudVmCluster` ID. Must not be `null` or empty.  
`dbNodeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DbNode` ID. Must not be `null` or empty.  
  
## Properties 

### CloudVmClusterId
    
    
    public string CloudVmClusterId { get; }

The `CloudVmCluster` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DbNodeId
    
    
    public string DbNodeId { get; }

The `DbNode` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExadbVmClusterId
    
    
    public string ExadbVmClusterId { get; }

The `ExadbVmCluster` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IsKnownPattern
    
    
    public bool IsKnownPattern { get; }

Whether this instance contains a resource name with a known pattern.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LocationId
    
    
    public string LocationId { get; }

The `Location` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public DbNodeName.ResourceNameType Type { get; }

The [DbNodeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string cloudVmClusterId, string dbNodeId)

Formats the IDs into the string representation of this [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with pattern `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudVmClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudVmCluster` ID. Must not be `null` or empty.  
`dbNodeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DbNode` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with pattern `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`.  
  
### FormatProjectLocationCloudVmClusterDbNode(string, string, string, string)
    
    
    public static string FormatProjectLocationCloudVmClusterDbNode(string projectId, string locationId, string cloudVmClusterId, string dbNodeId)

Formats the IDs into the string representation of this [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with pattern `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudVmClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudVmCluster` ID. Must not be `null` or empty.  
`dbNodeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DbNode` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with pattern `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`.  
  
### FormatProjectLocationExadbVmClusterDbNode(string, string, string, string)
    
    
    public static string FormatProjectLocationExadbVmClusterDbNode(string projectId, string locationId, string exadbVmClusterId, string dbNodeId)

Formats the IDs into the string representation of this [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with pattern `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`exadbVmClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ExadbVmCluster` ID. Must not be `null` or empty.  
`dbNodeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DbNode` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with pattern `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`.  
  
### FromProjectLocationCloudVmClusterDbNode(string, string, string, string)
    
    
    public static DbNodeName FromProjectLocationCloudVmClusterDbNode(string projectId, string locationId, string cloudVmClusterId, string dbNodeId)

Creates a [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with the pattern `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudVmClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudVmCluster` ID. Must not be `null` or empty.  
`dbNodeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DbNode` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)` | A new instance of [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) constructed from the provided ids.  
  
### FromProjectLocationExadbVmClusterDbNode(string, string, string, string)
    
    
    public static DbNodeName FromProjectLocationExadbVmClusterDbNode(string projectId, string locationId, string exadbVmClusterId, string dbNodeId)

Creates a [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) with the pattern `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`exadbVmClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ExadbVmCluster` ID. Must not be `null` or empty.  
`dbNodeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DbNode` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)` | A new instance of [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static DbNodeName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)` | A new instance of [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) containing the provided `unparsedResourceName`.  
  
### GetHashCode()
    
    
    public override int GetHashCode()

Returns a hash code for this resource name.

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### Parse(string)
    
    
    public static DbNodeName Parse(string dbNodeName)

Parses the given resource name string into a new [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) instance.

**Parameter**  
---  
**Name** | **Description**  
`dbNodeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)` | The parsed [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`
  * `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`



### Parse(string, bool)
    
    
    public static DbNodeName Parse(string dbNodeName, bool allowUnparsed)

Parses the given resource name string into a new [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`dbNodeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName#Google_Cloud_OracleDatabase_V1_DbNodeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)` | The parsed [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`
  * `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`



Or may be in any format if `allowUnparsed` is `true`.

### ToString()
    
    
    public override string ToString()

The string representation of the resource name.

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of the resource name.  
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### TryParse(string, out DbNodeName)
    
    
    public static bool TryParse(string dbNodeName, out DbNodeName result)

Tries to parse the given resource name string into a new [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) instance.

**Parameters**  
---  
**Name** | **Description**  
`dbNodeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)`  
When this method returns, the parsed [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`
  * `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`



### TryParse(string, bool, out DbNodeName)
    
    
    public static bool TryParse(string dbNodeName, bool allowUnparsed, out DbNodeName result)

Tries to parse the given resource name string into a new [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`dbNodeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName#Google_Cloud_OracleDatabase_V1_DbNodeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)`  
When this method returns, the parsed [DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}`
  * `projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}/dbNodes/{db_node}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(DbNodeName, DbNodeName)
    
    
    public static bool operator ==(DbNodeName a, DbNodeName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)`  
The first resource name to compare, or null.  
`b` | `[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(DbNodeName, DbNodeName)
    
    
    public static bool operator !=(DbNodeName a, DbNodeName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)`  
The first resource name to compare, or null.  
`b` | `[DbNodeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbNodeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
