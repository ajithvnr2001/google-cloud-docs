---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.OnPremisesConfigurationOrBuilder
title: Interface OnPremisesConfigurationOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:04.264082+00:00
---

# Interface OnPremisesConfigurationOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.OnPremisesConfigurationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OnPremisesConfigurationOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface OnPremisesConfigurationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCaCertificate()
    
    
    public abstract String getCaCertificate()

PEM representation of the trusted CA's x509 certificate.

`string ca_certificate = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The caCertificate.  
  
### getCaCertificateBytes()
    
    
    public abstract ByteString getCaCertificateBytes()

PEM representation of the trusted CA's x509 certificate.

`string ca_certificate = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for caCertificate.  
  
### getClientCertificate()
    
    
    public abstract String getClientCertificate()

PEM representation of the replica's x509 certificate.

`string client_certificate = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientCertificate.  
  
### getClientCertificateBytes()
    
    
    public abstract ByteString getClientCertificateBytes()

PEM representation of the replica's x509 certificate.

`string client_certificate = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientCertificate.  
  
### getClientKey()
    
    
    public abstract String getClientKey()

PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate.

`string client_key = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientKey.  
  
### getClientKeyBytes()
    
    
    public abstract ByteString getClientKeyBytes()

PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate.

`string client_key = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientKey.  
  
### getDmsManaged()
    
    
    public abstract boolean getDmsManaged()

Output only. Indicates whether the resource is managed by Database Migration Service.

`bool dms_managed = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dmsManaged.  
  
### getDumpFilePath()
    
    
    public abstract String getDumpFilePath()

The dump file to create the Cloud SQL replica.

`string dump_file_path = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dumpFilePath.  
  
### getDumpFilePathBytes()
    
    
    public abstract ByteString getDumpFilePathBytes()

The dump file to create the Cloud SQL replica.

`string dump_file_path = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dumpFilePath.  
  
### getHostPort()
    
    
    public abstract String getHostPort()

The host and port of the on-premises instance in host:port format

`string host_port = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostPort.  
  
### getHostPortBytes()
    
    
    public abstract ByteString getHostPortBytes()

The host and port of the on-premises instance in host:port format

`string host_port = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostPort.  
  
### getKind()
    
    
    public abstract String getKind()

This is always `sql#onPremisesConfiguration`.

`string kind = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

This is always `sql#onPremisesConfiguration`.

`string kind = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getPassword()
    
    
    public abstract String getPassword()

The password for connecting to on-premises instance.

`string password = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The password.  
  
### getPasswordBytes()
    
    
    public abstract ByteString getPasswordBytes()

The password for connecting to on-premises instance.

`string password = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for password.  
  
### getSelectedObjects(int index)
    
    
    public abstract SelectedObjects getSelectedObjects(int index)

Optional. A list of objects that the user selects for replication from an external source instance.

` repeated .google.cloud.sql.v1beta4.SelectedObjects selected_objects = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SelectedObjects](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SelectedObjects)` |   
  
### getSelectedObjectsCount()
    
    
    public abstract int getSelectedObjectsCount()

Optional. A list of objects that the user selects for replication from an external source instance.

` repeated .google.cloud.sql.v1beta4.SelectedObjects selected_objects = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSelectedObjectsList()
    
    
    public abstract List<SelectedObjects> getSelectedObjectsList()

Optional. A list of objects that the user selects for replication from an external source instance.

` repeated .google.cloud.sql.v1beta4.SelectedObjects selected_objects = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SelectedObjects](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SelectedObjects)>` |   
  
### getSelectedObjectsOrBuilder(int index)
    
    
    public abstract SelectedObjectsOrBuilder getSelectedObjectsOrBuilder(int index)

Optional. A list of objects that the user selects for replication from an external source instance.

` repeated .google.cloud.sql.v1beta4.SelectedObjects selected_objects = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SelectedObjectsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SelectedObjectsOrBuilder)` |   
  
### getSelectedObjectsOrBuilderList()
    
    
    public abstract List<? extends SelectedObjectsOrBuilder> getSelectedObjectsOrBuilderList()

Optional. A list of objects that the user selects for replication from an external source instance.

` repeated .google.cloud.sql.v1beta4.SelectedObjects selected_objects = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.sql.v1beta4.SelectedObjectsOrBuilder>` |   
  
### getSourceInstance()
    
    
    public abstract InstanceReference getSourceInstance()

The reference to Cloud SQL instance if the source is Cloud SQL.

`.google.cloud.sql.v1beta4.InstanceReference source_instance = 15;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.InstanceReference)` | The sourceInstance.  
  
### getSourceInstanceOrBuilder()
    
    
    public abstract InstanceReferenceOrBuilder getSourceInstanceOrBuilder()

The reference to Cloud SQL instance if the source is Cloud SQL.

`.google.cloud.sql.v1beta4.InstanceReference source_instance = 15;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceReferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.InstanceReferenceOrBuilder)` |   
  
### getSslOption()
    
    
    public abstract OnPremisesConfiguration.SslOption getSslOption()

Optional. SslOption for replica connection to the on-premises source.

` .google.cloud.sql.v1beta4.OnPremisesConfiguration.SslOption ssl_option = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OnPremisesConfiguration.SslOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.OnPremisesConfiguration.SslOption)` | The sslOption.  
  
### getSslOptionValue()
    
    
    public abstract int getSslOptionValue()

Optional. SslOption for replica connection to the on-premises source.

` .google.cloud.sql.v1beta4.OnPremisesConfiguration.SslOption ssl_option = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sslOption.  
  
### getUsername()
    
    
    public abstract String getUsername()

The username for connecting to on-premises instance.

`string username = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes()
    
    
    public abstract ByteString getUsernameBytes()

The username for connecting to on-premises instance.

`string username = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### hasSourceInstance()
    
    
    public abstract boolean hasSourceInstance()

The reference to Cloud SQL instance if the source is Cloud SQL.

`.google.cloud.sql.v1beta4.InstanceReference source_instance = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceInstance field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
