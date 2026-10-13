---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfigOrBuilder
title: Interface WorkstationConfigOrBuilder (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:33.603627+00:00
---

# Interface WorkstationConfigOrBuilder (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WorkstationConfigOrBuilder (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.0  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface WorkstationConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAnnotations(String key)
    
    
    public abstract boolean containsAnnotations(String key)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowedPorts(int index)
    
    
    public abstract WorkstationConfig.PortRange getAllowedPorts(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)` |   
  
### getAllowedPortsCount()
    
    
    public abstract int getAllowedPortsCount()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowedPortsList()
    
    
    public abstract List<WorkstationConfig.PortRange> getAllowedPortsList()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)>` |   
  
### getAllowedPortsOrBuilder(int index)
    
    
    public abstract WorkstationConfig.PortRangeOrBuilder getAllowedPortsOrBuilder(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRangeOrBuilder)` |   
  
### getAllowedPortsOrBuilderList()
    
    
    public abstract List<? extends WorkstationConfig.PortRangeOrBuilder> getAllowedPortsOrBuilderList()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.PortRangeOrBuilder>` |   
  
### getAnnotations() (deprecated)
    
    
    public abstract Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfigOrBuilder#com_google_cloud_workstations_v1_WorkstationConfigOrBuilder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public abstract int getAnnotationsCount()

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public abstract Map<String,String> getAnnotationsMap()

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public abstract String getAnnotationsOrDefault(String key, String defaultValue)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public abstract String getAnnotationsOrThrow(String key)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getConditions(int index)
    
    
    public abstract Status getConditions(int index)

Output only. Status conditions describing the workstation configuration's current state.

`repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` |   
  
### getConditionsCount()
    
    
    public abstract int getConditionsCount()

Output only. Status conditions describing the workstation configuration's current state.

`repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConditionsList()
    
    
    public abstract List<Status> getConditionsList()

Output only. Status conditions describing the workstation configuration's current state.

`repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.rpc.Status>` |   
  
### getConditionsOrBuilder(int index)
    
    
    public abstract StatusOrBuilder getConditionsOrBuilder(int index)

Output only. Status conditions describing the workstation configuration's current state.

`repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getConditionsOrBuilderList()
    
    
    public abstract List<? extends StatusOrBuilder> getConditionsOrBuilderList()

Output only. Status conditions describing the workstation configuration's current state.

`repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.rpc.StatusOrBuilder>` |   
  
### getContainer()
    
    
    public abstract WorkstationConfig.Container getContainer()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Container)` | The container.  
  
### getContainerOrBuilder()
    
    
    public abstract WorkstationConfig.ContainerOrBuilder getContainerOrBuilder()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ContainerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ContainerOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when this workstation configuration was created.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when this workstation configuration was created.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDegraded()
    
    
    public abstract boolean getDegraded()

Output only. Whether this workstation configuration is in degraded mode, in which case it may require user action to restore full functionality. The conditions field contains detailed information about the status of the configuration.

`bool degraded = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The degraded.  
  
### getDeleteTime()
    
    
    public abstract Timestamp getDeleteTime()

Output only. Time when this workstation configuration was soft-deleted.

`.google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteTime.  
  
### getDeleteTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getDeleteTimeOrBuilder()

Output only. Time when this workstation configuration was soft-deleted.

`.google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisableTcpConnections()
    
    
    public abstract boolean getDisableTcpConnections()

Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections through a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain TCP connections, such as SSH. When enabled, all communication must occur over HTTPS or WSS.

`bool disable_tcp_connections = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableTcpConnections.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnableAuditAgent()
    
    
    public abstract boolean getEnableAuditAgent()

Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service_account must also be specified that has `roles/logging.logWriter` and `roles/monitoring.metricWriter` on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging) and [Container output logging](https://cloud.google.com/workstations/docs/container-output-logging#overview). Operating system audit logs are available in the [Cloud Logging](https://cloud.google.com/logging/docs) console by querying:

resource.type="gce_instance" log_name:"/logs/linux-auditd"

`bool enable_audit_agent = 20 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableAuditAgent.  
  
### getEncryptionKey()
    
    
    public abstract WorkstationConfig.CustomerEncryptionKey getEncryptionKey()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey)` | The encryptionKey.  
  
### getEncryptionKeyOrBuilder()
    
    
    public abstract WorkstationConfig.CustomerEncryptionKeyOrBuilder getEncryptionKeyOrBuilder()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.CustomerEncryptionKeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKeyOrBuilder)` |   
  
### getEphemeralDirectories(int index)
    
    
    public abstract WorkstationConfig.EphemeralDirectory getEphemeralDirectories(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)` |   
  
### getEphemeralDirectoriesCount()
    
    
    public abstract int getEphemeralDirectoriesCount()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEphemeralDirectoriesList()
    
    
    public abstract List<WorkstationConfig.EphemeralDirectory> getEphemeralDirectoriesList()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)>` |   
  
### getEphemeralDirectoriesOrBuilder(int index)
    
    
    public abstract WorkstationConfig.EphemeralDirectoryOrBuilder getEphemeralDirectoriesOrBuilder(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectoryOrBuilder)` |   
  
### getEphemeralDirectoriesOrBuilderList()
    
    
    public abstract List<? extends WorkstationConfig.EphemeralDirectoryOrBuilder> getEphemeralDirectoriesOrBuilderList()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectoryOrBuilder>` |   
  
### getEtag()
    
    
    public abstract String getEtag()

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGrantWorkstationAdminRoleOnCreate()
    
    
    public abstract boolean getGrantWorkstationAdminRoleOnCreate()

Optional. Grant creator of a workstation `roles/workstations.policyAdmin` role along with `roles/workstations.user` role on the workstation created by them. This allows workstation users to share access to either their entire workstation, or individual ports. Defaults to false.

` bool grant_workstation_admin_role_on_create = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The grantWorkstationAdminRoleOnCreate.  
  
### getHost()
    
    
    public abstract WorkstationConfig.Host getHost()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Host)` | The host.  
  
### getHostOrBuilder()
    
    
    public abstract WorkstationConfig.HostOrBuilder getHostOrBuilder()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.HostOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.HostOrBuilder)` |   
  
### getIdleTimeout()
    
    
    public abstract Duration getIdleTimeout()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The idleTimeout.  
  
### getIdleTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getIdleTimeoutOrBuilder()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfigOrBuilder#com_google_cloud_workstations_v1_WorkstationConfigOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMaxUsableWorkstations()
    
    
    public abstract int getMaxUsableWorkstations()

Optional. Maximum number of workstations under this configuration a user can have `workstations.workstation.use` permission on.

Only enforced on CreateWorkstation API calls on the user issuing the API request. Can be overridden by:

  * granting a user workstations.workstationConfigs.exemptMaxUsableWorkstationLimit permission, or
  * having a user with that permission create a workstation and granting another user `workstations.workstation.use` permission on that workstation.

If not specified, defaults to `0`, which indicates unlimited.




`int32 max_usable_workstations = 28 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxUsableWorkstations.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPersistentDirectories(int index)
    
    
    public abstract WorkstationConfig.PersistentDirectory getPersistentDirectories(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)` |   
  
### getPersistentDirectoriesCount()
    
    
    public abstract int getPersistentDirectoriesCount()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPersistentDirectoriesList()
    
    
    public abstract List<WorkstationConfig.PersistentDirectory> getPersistentDirectoriesList()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)>` |   
  
### getPersistentDirectoriesOrBuilder(int index)
    
    
    public abstract WorkstationConfig.PersistentDirectoryOrBuilder getPersistentDirectoriesOrBuilder(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectoryOrBuilder)` |   
  
### getPersistentDirectoriesOrBuilderList()
    
    
    public abstract List<? extends WorkstationConfig.PersistentDirectoryOrBuilder> getPersistentDirectoriesOrBuilderList()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectoryOrBuilder>` |   
  
### getReadinessChecks(int index)
    
    
    public abstract WorkstationConfig.ReadinessCheck getReadinessChecks(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)` |   
  
### getReadinessChecksCount()
    
    
    public abstract int getReadinessChecksCount()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getReadinessChecksList()
    
    
    public abstract List<WorkstationConfig.ReadinessCheck> getReadinessChecksList()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)>` |   
  
### getReadinessChecksOrBuilder(int index)
    
    
    public abstract WorkstationConfig.ReadinessCheckOrBuilder getReadinessChecksOrBuilder(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheckOrBuilder)` |   
  
### getReadinessChecksOrBuilderList()
    
    
    public abstract List<? extends WorkstationConfig.ReadinessCheckOrBuilder> getReadinessChecksOrBuilderList()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheckOrBuilder>` |   
  
### getReconciling()
    
    
    public abstract boolean getReconciling()

Output only. Indicates whether this workstation configuration is currently being updated to match its intended state.

`bool reconciling = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getReplicaZones(int index)
    
    
    public abstract String getReplicaZones(int index)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The replicaZones at the given index.  
  
### getReplicaZonesBytes(int index)
    
    
    public abstract ByteString getReplicaZonesBytes(int index)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the replicaZones at the given index.  
  
### getReplicaZonesCount()
    
    
    public abstract int getReplicaZonesCount()

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of replicaZones.  
  
### getReplicaZonesList()
    
    
    public abstract List<String> getReplicaZonesList()

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the replicaZones.  
  
### getRunningTimeout()
    
    
    public abstract Duration getRunningTimeout()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

`.google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The runningTimeout.  
  
### getRunningTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getRunningTimeoutOrBuilder()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

`.google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getUid()
    
    
    public abstract String getUid()

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Time when this workstation configuration was most recently updated.

`.google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Time when this workstation configuration was most recently updated.

`.google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasContainer()
    
    
    public abstract boolean hasContainer()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the container field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when this workstation configuration was created.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDeleteTime()
    
    
    public abstract boolean hasDeleteTime()

Output only. Time when this workstation configuration was soft-deleted.

`.google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteTime field is set.  
  
### hasEncryptionKey()
    
    
    public abstract boolean hasEncryptionKey()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionKey field is set.  
  
### hasHost()
    
    
    public abstract boolean hasHost()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the host field is set.  
  
### hasIdleTimeout()
    
    
    public abstract boolean hasIdleTimeout()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the idleTimeout field is set.  
  
### hasRunningTimeout()
    
    
    public abstract boolean hasRunningTimeout()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

`.google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the runningTimeout field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Time when this workstation configuration was most recently updated.

`.google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
