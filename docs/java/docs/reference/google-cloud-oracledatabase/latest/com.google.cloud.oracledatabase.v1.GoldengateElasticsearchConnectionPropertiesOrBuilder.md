---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionPropertiesOrBuilder
title: Interface GoldengateElasticsearchConnectionPropertiesOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:45.110817+00:00
---

# Interface GoldengateElasticsearchConnectionPropertiesOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionPropertiesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GoldengateElasticsearchConnectionPropertiesOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GoldengateElasticsearchConnectionPropertiesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthenticationType()
    
    
    public abstract GoldengateElasticsearchConnectionProperties.ElasticsearchAuthenticationType getAuthenticationType()

Optional. Authentication type for Elasticsearch.

` .google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ElasticsearchAuthenticationType authentication_type = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateElasticsearchConnectionProperties.ElasticsearchAuthenticationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ElasticsearchAuthenticationType)` | The authenticationType.  
  
### getAuthenticationTypeValue()
    
    
    public abstract int getAuthenticationTypeValue()

Optional. Authentication type for Elasticsearch.

` .google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ElasticsearchAuthenticationType authentication_type = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for authenticationType.  
  
### getConnectionPasswordOptionsCase()
    
    
    public abstract GoldengateElasticsearchConnectionProperties.ConnectionPasswordOptionsCase getConnectionPasswordOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[GoldengateElasticsearchConnectionProperties.ConnectionPasswordOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ConnectionPasswordOptionsCase)` |   
  
### getFingerprint()
    
    
    public abstract String getFingerprint()

Optional. Fingerprint required by TLS security protocol. Eg.: '6152b2dfbff200f973c5074a5b91d06ab3b472c07c09a1ea57bb7fd406cdce9c'

`string fingerprint = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fingerprint.  
  
### getFingerprintBytes()
    
    
    public abstract ByteString getFingerprintBytes()

Optional. Fingerprint required by TLS security protocol. Eg.: '6152b2dfbff200f973c5074a5b91d06ab3b472c07c09a1ea57bb7fd406cdce9c'

`string fingerprint = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fingerprint.  
  
### getPassword()
    
    
    public abstract String getPassword()

Optional. Input only. The password Oracle Goldengate uses for Elastic Search connection in plain text.

` string password = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The password.  
  
### getPasswordBytes()
    
    
    public abstract ByteString getPasswordBytes()

Optional. Input only. The password Oracle Goldengate uses for Elastic Search connection in plain text.

` string password = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for password.  
  
### getPasswordSecretVersion()
    
    
    public abstract String getPasswordSecretVersion()

Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Elastic Search connection. Format: projects/{project}/secrets/{secret}/versions/{version}.

` string password_secret_version = 9 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The passwordSecretVersion.  
  
### getPasswordSecretVersionBytes()
    
    
    public abstract ByteString getPasswordSecretVersionBytes()

Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Elastic Search connection. Format: projects/{project}/secrets/{secret}/versions/{version}.

` string password_secret_version = 9 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for passwordSecretVersion.  
  
### getSecurityProtocol()
    
    
    public abstract GoldengateElasticsearchConnectionProperties.ElasticsearchSecurityProtocol getSecurityProtocol()

Optional. Security protocol for Elasticsearch.

` .google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ElasticsearchSecurityProtocol security_protocol = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GoldengateElasticsearchConnectionProperties.ElasticsearchSecurityProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ElasticsearchSecurityProtocol)` | The securityProtocol.  
  
### getSecurityProtocolValue()
    
    
    public abstract int getSecurityProtocolValue()

Optional. Security protocol for Elasticsearch.

` .google.cloud.oracledatabase.v1.GoldengateElasticsearchConnectionProperties.ElasticsearchSecurityProtocol security_protocol = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for securityProtocol.  
  
### getServers()
    
    
    public abstract String getServers()

Optional. Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Example: "server1.example.com:4000,server2.example.com:4000"

`string servers = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servers.  
  
### getServersBytes()
    
    
    public abstract ByteString getServersBytes()

Optional. Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Example: "server1.example.com:4000,server2.example.com:4000"

`string servers = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servers.  
  
### getTechnologyType()
    
    
    public abstract String getTechnologyType()

Optional. The technology type of ElasticsearchConnection.

`string technology_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The technologyType.  
  
### getTechnologyTypeBytes()
    
    
    public abstract ByteString getTechnologyTypeBytes()

Optional. The technology type of ElasticsearchConnection.

`string technology_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for technologyType.  
  
### getUsername()
    
    
    public abstract String getUsername()

Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.

`string username = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes()
    
    
    public abstract ByteString getUsernameBytes()

Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.

`string username = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### hasPassword()
    
    
    public abstract boolean hasPassword()

Optional. Input only. The password Oracle Goldengate uses for Elastic Search connection in plain text.

` string password = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the password field is set.  
  
### hasPasswordSecretVersion()
    
    
    public abstract boolean hasPasswordSecretVersion()

Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Elastic Search connection. Format: projects/{project}/secrets/{secret}/versions/{version}.

` string password_secret_version = 9 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the passwordSecretVersion field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
