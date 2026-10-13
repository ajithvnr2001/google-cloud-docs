---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmClusterOrBuilder
title: Interface ExadbVmClusterOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:16.437960+00:00
---

# Interface ExadbVmClusterOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmClusterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExadbVmClusterOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ExadbVmClusterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. The labels or tags associated with the ExadbVmCluster.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBackupOdbSubnet()
    
    
    public abstract String getBackupOdbSubnet()

Required. Immutable. The name of the backup OdbSubnet associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}

` string backup_odb_subnet = 8 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backupOdbSubnet.  
  
### getBackupOdbSubnetBytes()
    
    
    public abstract ByteString getBackupOdbSubnetBytes()

Required. Immutable. The name of the backup OdbSubnet associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}

` string backup_odb_subnet = 8 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backupOdbSubnet.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The date and time that the ExadbVmCluster was created.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The date and time that the ExadbVmCluster was created.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. Immutable. The display name for the ExadbVmCluster. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters.

` string display_name = 9 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. Immutable. The display name for the ExadbVmCluster. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters.

` string display_name = 9 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEntitlementId()
    
    
    public abstract String getEntitlementId()

Output only. The ID of the subscription entitlement associated with the ExadbVmCluster.

`string entitlement_id = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The entitlementId.  
  
### getEntitlementIdBytes()
    
    
    public abstract ByteString getEntitlementIdBytes()

Output only. The ID of the subscription entitlement associated with the ExadbVmCluster.

`string entitlement_id = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for entitlementId.  
  
### getGcpOracleZone()
    
    
    public abstract String getGcpOracleZone()

Output only. Immutable. The GCP Oracle zone where Oracle ExadbVmCluster is hosted. Example: us-east4-b-r2. During creation, the system will pick the zone assigned to the ExascaleDbStorageVault.

` string gcp_oracle_zone = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcpOracleZone.  
  
### getGcpOracleZoneBytes()
    
    
    public abstract ByteString getGcpOracleZoneBytes()

Output only. Immutable. The GCP Oracle zone where Oracle ExadbVmCluster is hosted. Example: us-east4-b-r2. During creation, the system will pick the zone assigned to the ExascaleDbStorageVault.

` string gcp_oracle_zone = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcpOracleZone.  
  
### getIdentityConnector()
    
    
    public abstract IdentityConnector getIdentityConnector()

Output only. The identity connector details which will allow OCI to securely access the resources in the customer project.

` .google.cloud.oracledatabase.v1.IdentityConnector identity_connector = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.IdentityConnector)` | The identityConnector.  
  
### getIdentityConnectorOrBuilder()
    
    
    public abstract IdentityConnectorOrBuilder getIdentityConnectorOrBuilder()

Output only. The identity connector details which will allow OCI to securely access the resources in the customer project.

` .google.cloud.oracledatabase.v1.IdentityConnector identity_connector = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityConnectorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.IdentityConnectorOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmClusterOrBuilder#com_google_cloud_oracledatabase_v1_ExadbVmClusterOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. The labels or tags associated with the ExadbVmCluster.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. The labels or tags associated with the ExadbVmCluster.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. The labels or tags associated with the ExadbVmCluster.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. The labels or tags associated with the ExadbVmCluster.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the ExadbVmCluster resource in the following format: projects/{project}/locations/{region}/exadbVmClusters/{exadb_vm_cluster}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the ExadbVmCluster resource in the following format: projects/{project}/locations/{region}/exadbVmClusters/{exadb_vm_cluster}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOdbNetwork()
    
    
    public abstract String getOdbNetwork()

Optional. Immutable. The name of the OdbNetwork associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.

` string odb_network = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The odbNetwork.  
  
### getOdbNetworkBytes()
    
    
    public abstract ByteString getOdbNetworkBytes()

Optional. Immutable. The name of the OdbNetwork associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.

` string odb_network = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for odbNetwork.  
  
### getOdbSubnet()
    
    
    public abstract String getOdbSubnet()

Required. Immutable. The name of the OdbSubnet associated with the ExadbVmCluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}

` string odb_subnet = 7 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The odbSubnet.  
  
### getOdbSubnetBytes()
    
    
    public abstract ByteString getOdbSubnetBytes()

Required. Immutable. The name of the OdbSubnet associated with the ExadbVmCluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}

` string odb_subnet = 7 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for odbSubnet.  
  
### getProperties()
    
    
    public abstract ExadbVmClusterProperties getProperties()

Required. The properties of the ExadbVmCluster.

` .google.cloud.oracledatabase.v1.ExadbVmClusterProperties properties = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ExadbVmClusterProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmClusterProperties)` | The properties.  
  
### getPropertiesOrBuilder()
    
    
    public abstract ExadbVmClusterPropertiesOrBuilder getPropertiesOrBuilder()

Required. The properties of the ExadbVmCluster.

` .google.cloud.oracledatabase.v1.ExadbVmClusterProperties properties = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ExadbVmClusterPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmClusterPropertiesOrBuilder)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The date and time that the ExadbVmCluster was created.

`.google.protobuf.Timestamp create_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasIdentityConnector()
    
    
    public abstract boolean hasIdentityConnector()

Output only. The identity connector details which will allow OCI to securely access the resources in the customer project.

` .google.cloud.oracledatabase.v1.IdentityConnector identity_connector = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the identityConnector field is set.  
  
### hasProperties()
    
    
    public abstract boolean hasProperties()

Required. The properties of the ExadbVmCluster.

` .google.cloud.oracledatabase.v1.ExadbVmClusterProperties properties = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the properties field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
