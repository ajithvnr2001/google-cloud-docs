---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateMysqlConnectionPropertiesOrBuilder
title: Interface GoldengateMysqlConnectionPropertiesOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:28.215025+00:00
---

# Interface GoldengateMysqlConnectionPropertiesOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateMysqlConnectionPropertiesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GoldengateMysqlConnectionPropertiesOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GoldengateMysqlConnectionPropertiesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalAttributes(int index)
    
    
    public abstract NameValuePair getAdditionalAttributes(int index)

Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.

` repeated .google.cloud.oracledatabase.v1.NameValuePair additional_attributes = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NameValuePair](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.NameValuePair)` |   
  
### getAdditionalAttributesCount()
    
    
    public abstract int getAdditionalAttributesCount()

Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.

` repeated .google.cloud.oracledatabase.v1.NameValuePair additional_attributes = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdditionalAttributesList()
    
    
    public abstract List<NameValuePair> getAdditionalAttributesList()

Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.

` repeated .google.cloud.oracledatabase.v1.NameValuePair additional_attributes = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NameValuePair](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.NameValuePair)>` |   
  
### getAdditionalAttributesOrBuilder(int index)
    
    
    public abstract NameValuePairOrBuilder getAdditionalAttributesOrBuilder(int index)

Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.

` repeated .google.cloud.oracledatabase.v1.NameValuePair additional_attributes = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NameValuePairOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.NameValuePairOrBuilder)` |   
  
### getAdditionalAttributesOrBuilderList()
    
    
    public abstract List<? extends NameValuePairOrBuilder> getAdditionalAttributesOrBuilderList()

Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.

` repeated .google.cloud.oracledatabase.v1.NameValuePair additional_attributes = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.oracledatabase.v1.NameValuePairOrBuilder>` |   
  
### getConnectionPasswordOptionsCase()
    
    
    public abstract GoldengateMysqlConnectionProperties.ConnectionPasswordOptionsCase getConnectionPasswordOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[GoldengateMysqlConnectionProperties.ConnectionPasswordOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.ConnectionPasswordOptionsCase)` |   
  
### getDatabase()
    
    
    public abstract String getDatabase()

Optional. The name of the database.

`string database = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The database.  
  
### getDatabaseBytes()
    
    
    public abstract ByteString getDatabaseBytes()

Optional. The name of the database.

`string database = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for database.  
  
### getDbSystemId()
    
    
    public abstract String getDbSystemId()

Optional. The OCID of the database system being referenced.

`string db_system_id = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dbSystemId.  
  
### getDbSystemIdBytes()
    
    
    public abstract ByteString getDbSystemIdBytes()

Optional. The OCID of the database system being referenced.

`string db_system_id = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dbSystemId.  
  
### getHost()
    
    
    public abstract String getHost()

Optional. The name or address of a host.

`string host = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The host.  
  
### getHostBytes()
    
    
    public abstract ByteString getHostBytes()

Optional. The name or address of a host.

`string host = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for host.  
  
### getPassword()
    
    
    public abstract String getPassword()

Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.

` string password = 15 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The password.  
  
### getPasswordBytes()
    
    
    public abstract ByteString getPasswordBytes()

Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.

` string password = 15 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for password.  
  
### getPasswordSecretVersion()
    
    
    public abstract String getPasswordSecretVersion()

Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.

` string password_secret_version = 16 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The passwordSecretVersion.  
  
### getPasswordSecretVersionBytes()
    
    
    public abstract ByteString getPasswordSecretVersionBytes()

Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.

` string password_secret_version = 16 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for passwordSecretVersion.  
  
### getPort()
    
    
    public abstract int getPort()

Optional. The port of an endpoint usually specified for a connection.

`int32 port = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The port.  
  
### getSecurityProtocol()
    
    
    public abstract GoldengateMysqlConnectionProperties.MysqlSecurityProtocol getSecurityProtocol()

Optional. Security Type for MySQL.

` .google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.MysqlSecurityProtocol security_protocol = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateMysqlConnectionProperties.MysqlSecurityProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.MysqlSecurityProtocol)` | The securityProtocol.  
  
### getSecurityProtocolValue()
    
    
    public abstract int getSecurityProtocolValue()

Optional. Security Type for MySQL.

` .google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.MysqlSecurityProtocol security_protocol = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for securityProtocol.  
  
### getSslCaFile()
    
    
    public abstract String getSslCaFile()

Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1 and 2-way SSL).

`string ssl_ca_file = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sslCaFile.  
  
### getSslCaFileBytes()
    
    
    public abstract ByteString getSslCaFileBytes()

Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1 and 2-way SSL).

`string ssl_ca_file = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sslCaFile.  
  
### getSslCertFile()
    
    
    public abstract String getSslCertFile()

Optional. Client Certificate - The base64 encoded content of a .pem or .crt file containing the client public key (for 2-way SSL).

`string ssl_cert_file = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sslCertFile.  
  
### getSslCertFileBytes()
    
    
    public abstract ByteString getSslCertFileBytes()

Optional. Client Certificate - The base64 encoded content of a .pem or .crt file containing the client public key (for 2-way SSL).

`string ssl_cert_file = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sslCertFile.  
  
### getSslCrlFile()
    
    
    public abstract String getSslCrlFile()

Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA).

`string ssl_crl_file = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sslCrlFile.  
  
### getSslCrlFileBytes()
    
    
    public abstract ByteString getSslCrlFileBytes()

Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA).

`string ssl_crl_file = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sslCrlFile.  
  
### getSslKeyFile()
    
    
    public abstract String getSslKeyFile()

Optional. Client Key - The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL).

`string ssl_key_file = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sslKeyFile.  
  
### getSslKeyFileBytes()
    
    
    public abstract ByteString getSslKeyFileBytes()

Optional. Client Key - The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL).

`string ssl_key_file = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sslKeyFile.  
  
### getSslMode()
    
    
    public abstract GoldengateMysqlConnectionProperties.SSLMode getSslMode()

Optional. SSL modes for MySQL.

` .google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.SSLMode ssl_mode = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateMysqlConnectionProperties.SSLMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.SSLMode)` | The sslMode.  
  
### getSslModeValue()
    
    
    public abstract int getSslModeValue()

Optional. SSL modes for MySQL.

` .google.cloud.oracledatabase.v1.GoldengateMysqlConnectionProperties.SSLMode ssl_mode = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sslMode.  
  
### getTechnologyType()
    
    
    public abstract String getTechnologyType()

Optional. The technology type of MysqlConnection.

`string technology_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The technologyType.  
  
### getTechnologyTypeBytes()
    
    
    public abstract ByteString getTechnologyTypeBytes()

Optional. The technology type of MysqlConnection.

`string technology_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for technologyType.  
  
### getUsername()
    
    
    public abstract String getUsername()

Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.

`string username = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes()
    
    
    public abstract ByteString getUsernameBytes()

Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.

`string username = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### hasPassword()
    
    
    public abstract boolean hasPassword()

Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.

` string password = 15 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the password field is set.  
  
### hasPasswordSecretVersion()
    
    
    public abstract boolean hasPasswordSecretVersion()

Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.

` string password_secret_version = 16 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the passwordSecretVersion field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
