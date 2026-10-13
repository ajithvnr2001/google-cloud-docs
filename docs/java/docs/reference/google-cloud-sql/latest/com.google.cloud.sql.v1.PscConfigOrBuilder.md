---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PscConfigOrBuilder
title: Interface PscConfigOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:10.773353+00:00
---

# Interface PscConfigOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PscConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PscConfigOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface PscConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowedConsumerProjects(int index)
    
    
    public abstract String getAllowedConsumerProjects(int index)

Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects.

Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric).

`repeated string allowed_consumer_projects = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowedConsumerProjects at the given index.  
  
### getAllowedConsumerProjectsBytes(int index)
    
    
    public abstract ByteString getAllowedConsumerProjectsBytes(int index)

Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects.

Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric).

`repeated string allowed_consumer_projects = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the allowedConsumerProjects at the given index.  
  
### getAllowedConsumerProjectsCount()
    
    
    public abstract int getAllowedConsumerProjectsCount()

Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects.

Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric).

`repeated string allowed_consumer_projects = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedConsumerProjects.  
  
### getAllowedConsumerProjectsList()
    
    
    public abstract List<String> getAllowedConsumerProjectsList()

Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects.

Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric).

`repeated string allowed_consumer_projects = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the allowedConsumerProjects.  
  
### getNetworkAttachmentUri()
    
    
    public abstract String getNetworkAttachmentUri()

Optional. The network attachment of the consumer network that the Private Service Connect enabled Cloud SQL instance is authorized to connect via PSC interface. format: projects/PROJECT/regions/REGION/networkAttachments/ID

`string network_attachment_uri = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The networkAttachmentUri.  
  
### getNetworkAttachmentUriBytes()
    
    
    public abstract ByteString getNetworkAttachmentUriBytes()

Optional. The network attachment of the consumer network that the Private Service Connect enabled Cloud SQL instance is authorized to connect via PSC interface. format: projects/PROJECT/regions/REGION/networkAttachments/ID

`string network_attachment_uri = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for networkAttachmentUri.  
  
### getPscAutoConnectionPolicyEnabled()
    
    
    public abstract boolean getPscAutoConnectionPolicyEnabled()

Optional. Whether to set up the PSC service connection policy automatically.

` optional bool psc_auto_connection_policy_enabled = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pscAutoConnectionPolicyEnabled.  
  
### getPscAutoConnections(int index)
    
    
    public abstract PscAutoConnectionConfig getPscAutoConnections(int index)

Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.

` repeated .google.cloud.sql.v1.PscAutoConnectionConfig psc_auto_connections = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscAutoConnectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PscAutoConnectionConfig)` |   
  
### getPscAutoConnectionsCount()
    
    
    public abstract int getPscAutoConnectionsCount()

Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.

` repeated .google.cloud.sql.v1.PscAutoConnectionConfig psc_auto_connections = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPscAutoConnectionsList()
    
    
    public abstract List<PscAutoConnectionConfig> getPscAutoConnectionsList()

Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.

` repeated .google.cloud.sql.v1.PscAutoConnectionConfig psc_auto_connections = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PscAutoConnectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PscAutoConnectionConfig)>` |   
  
### getPscAutoConnectionsOrBuilder(int index)
    
    
    public abstract PscAutoConnectionConfigOrBuilder getPscAutoConnectionsOrBuilder(int index)

Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.

` repeated .google.cloud.sql.v1.PscAutoConnectionConfig psc_auto_connections = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscAutoConnectionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.PscAutoConnectionConfigOrBuilder)` |   
  
### getPscAutoConnectionsOrBuilderList()
    
    
    public abstract List<? extends PscAutoConnectionConfigOrBuilder> getPscAutoConnectionsOrBuilderList()

Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.

` repeated .google.cloud.sql.v1.PscAutoConnectionConfig psc_auto_connections = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.sql.v1.PscAutoConnectionConfigOrBuilder>` |   
  
### getPscAutoDnsEnabled()
    
    
    public abstract boolean getPscAutoDnsEnabled()

Optional. Indicates whether Private Service Connect DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal DNS record across all networks configured with Private Service Connect auto-connections. This will default to true for new instances when Private Service Connect is enabled.

`optional bool psc_auto_dns_enabled = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pscAutoDnsEnabled.  
  
### getPscEnabled()
    
    
    public abstract boolean getPscEnabled()

Whether PSC connectivity is enabled for this instance.

`optional bool psc_enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pscEnabled.  
  
### getPscWriteEndpointDnsEnabled()
    
    
    public abstract boolean getPscWriteEndpointDnsEnabled()

Optional. Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal global DNS record across all networks configured with Private Service Connect auto-connections that points to the cluster primary instance. This feature is only supported for Enterprise Plus edition. This will default to true for new Enterprise Plus instances when `psc_auto_dns_enabled` is enabled.

` optional bool psc_write_endpoint_dns_enabled = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pscWriteEndpointDnsEnabled.  
  
### hasPscAutoConnectionPolicyEnabled()
    
    
    public abstract boolean hasPscAutoConnectionPolicyEnabled()

Optional. Whether to set up the PSC service connection policy automatically.

` optional bool psc_auto_connection_policy_enabled = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscAutoConnectionPolicyEnabled field is set.  
  
### hasPscAutoDnsEnabled()
    
    
    public abstract boolean hasPscAutoDnsEnabled()

Optional. Indicates whether Private Service Connect DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal DNS record across all networks configured with Private Service Connect auto-connections. This will default to true for new instances when Private Service Connect is enabled.

`optional bool psc_auto_dns_enabled = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscAutoDnsEnabled field is set.  
  
### hasPscEnabled()
    
    
    public abstract boolean hasPscEnabled()

Whether PSC connectivity is enabled for this instance.

`optional bool psc_enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscEnabled field is set.  
  
### hasPscWriteEndpointDnsEnabled()
    
    
    public abstract boolean hasPscWriteEndpointDnsEnabled()

Optional. Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal global DNS record across all networks configured with Private Service Connect auto-connections that points to the cluster primary instance. This feature is only supported for Enterprise Plus edition. This will default to true for new Enterprise Plus instances when `psc_auto_dns_enabled` is enabled.

` optional bool psc_write_endpoint_dns_enabled = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscWriteEndpointDnsEnabled field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
