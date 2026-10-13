---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupOrBuilder
title: Interface NodeGroupOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:03.877553+00:00
---

# Interface NodeGroupOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NodeGroupOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface NodeGroupOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutoscalingPolicy()
    
    
    public abstract NodeGroupAutoscalingPolicy getAutoscalingPolicy()

Specifies how autoscaling should behave.

` optional .google.cloud.compute.v1.NodeGroupAutoscalingPolicy autoscaling_policy = 221950041; `

**Returns**  
---  
**Type** | **Description**  
`[NodeGroupAutoscalingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupAutoscalingPolicy)` | The autoscalingPolicy.  
  
### getAutoscalingPolicyOrBuilder()
    
    
    public abstract NodeGroupAutoscalingPolicyOrBuilder getAutoscalingPolicyOrBuilder()

Specifies how autoscaling should behave.

` optional .google.cloud.compute.v1.NodeGroupAutoscalingPolicy autoscaling_policy = 221950041; `

**Returns**  
---  
**Type** | **Description**  
`[NodeGroupAutoscalingPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupAutoscalingPolicyOrBuilder)` |   
  
### getCreationTimestamp()
    
    
    public abstract String getCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public abstract ByteString getCreationTimestampBytes()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getDescription()
    
    
    public abstract String getDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getFingerprint()
    
    
    public abstract String getFingerprint()

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fingerprint.  
  
### getFingerprintBytes()
    
    
    public abstract ByteString getFingerprintBytes()

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fingerprint.  
  
### getId()
    
    
    public abstract long getId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output Only] The type of the resource. Alwayscompute#nodeGroup for node group.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output Only] The type of the resource. Alwayscompute#nodeGroup for node group.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getLocationHint()
    
    
    public abstract String getLocationHint()

An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate.

`optional string location_hint = 350519505;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The locationHint.  
  
### getLocationHintBytes()
    
    
    public abstract ByteString getLocationHintBytes()

An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate.

`optional string location_hint = 350519505;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for locationHint.  
  
### getMaintenanceInterval()
    
    
    public abstract String getMaintenanceInterval()

Specifies the frequency of planned maintenance events. The accepted values are: `AS_NEEDED` and `RECURRENT`. Check the MaintenanceInterval enum for the list of possible values.

`optional string maintenance_interval = 403368049;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The maintenanceInterval.  
  
### getMaintenanceIntervalBytes()
    
    
    public abstract ByteString getMaintenanceIntervalBytes()

Specifies the frequency of planned maintenance events. The accepted values are: `AS_NEEDED` and `RECURRENT`. Check the MaintenanceInterval enum for the list of possible values.

`optional string maintenance_interval = 403368049;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for maintenanceInterval.  
  
### getMaintenancePolicy()
    
    
    public abstract String getMaintenancePolicy()

Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT,RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies. Check the MaintenancePolicy enum for the list of possible values.

`optional string maintenance_policy = 528327646;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The maintenancePolicy.  
  
### getMaintenancePolicyBytes()
    
    
    public abstract ByteString getMaintenancePolicyBytes()

Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT,RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies. Check the MaintenancePolicy enum for the list of possible values.

`optional string maintenance_policy = 528327646;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for maintenancePolicy.  
  
### getMaintenanceWindow()
    
    
    public abstract NodeGroupMaintenanceWindow getMaintenanceWindow()

` optional .google.cloud.compute.v1.NodeGroupMaintenanceWindow maintenance_window = 186374812; `

**Returns**  
---  
**Type** | **Description**  
`[NodeGroupMaintenanceWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupMaintenanceWindow)` | The maintenanceWindow.  
  
### getMaintenanceWindowOrBuilder()
    
    
    public abstract NodeGroupMaintenanceWindowOrBuilder getMaintenanceWindowOrBuilder()

` optional .google.cloud.compute.v1.NodeGroupMaintenanceWindow maintenance_window = 186374812; `

**Returns**  
---  
**Type** | **Description**  
`[NodeGroupMaintenanceWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupMaintenanceWindowOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNodeTemplate()
    
    
    public abstract String getNodeTemplate()

URL of the node template to create the node group from.

`optional string node_template = 323154455;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodeTemplate.  
  
### getNodeTemplateBytes()
    
    
    public abstract ByteString getNodeTemplateBytes()

URL of the node template to create the node group from.

`optional string node_template = 323154455;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodeTemplate.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getShareSettings()
    
    
    public abstract ShareSettings getShareSettings()

Share-settings for the node group

`optional .google.cloud.compute.v1.ShareSettings share_settings = 266668163;`

**Returns**  
---  
**Type** | **Description**  
`[ShareSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettings)` | The shareSettings.  
  
### getShareSettingsOrBuilder()
    
    
    public abstract ShareSettingsOrBuilder getShareSettingsOrBuilder()

Share-settings for the node group

`optional .google.cloud.compute.v1.ShareSettings share_settings = 266668163;`

**Returns**  
---  
**Type** | **Description**  
`[ShareSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettingsOrBuilder)` |   
  
### getSize()
    
    
    public abstract int getSize()

Output only. [Output Only] The total number of nodes in the node group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The size.  
  
### getStatus()
    
    
    public abstract String getStatus()

Check the Status enum for the list of possible values.

`optional string status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The status.  
  
### getStatusBytes()
    
    
    public abstract ByteString getStatusBytes()

Check the Status enum for the list of possible values.

`optional string status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for status.  
  
### getZone()
    
    
    public abstract String getZone()

Output only. [Output Only] The name of the zone where the node group resides, such as us-central1-a.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public abstract ByteString getZoneBytes()

Output only. [Output Only] The name of the zone where the node group resides, such as us-central1-a.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasAutoscalingPolicy()
    
    
    public abstract boolean hasAutoscalingPolicy()

Specifies how autoscaling should behave.

` optional .google.cloud.compute.v1.NodeGroupAutoscalingPolicy autoscaling_policy = 221950041; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoscalingPolicy field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasFingerprint()
    
    
    public abstract boolean hasFingerprint()

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fingerprint field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output Only] The type of the resource. Alwayscompute#nodeGroup for node group.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasLocationHint()
    
    
    public abstract boolean hasLocationHint()

An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate.

`optional string location_hint = 350519505;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the locationHint field is set.  
  
### hasMaintenanceInterval()
    
    
    public abstract boolean hasMaintenanceInterval()

Specifies the frequency of planned maintenance events. The accepted values are: `AS_NEEDED` and `RECURRENT`. Check the MaintenanceInterval enum for the list of possible values.

`optional string maintenance_interval = 403368049;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceInterval field is set.  
  
### hasMaintenancePolicy()
    
    
    public abstract boolean hasMaintenancePolicy()

Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT,RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies. Check the MaintenancePolicy enum for the list of possible values.

`optional string maintenance_policy = 528327646;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenancePolicy field is set.  
  
### hasMaintenanceWindow()
    
    
    public abstract boolean hasMaintenanceWindow()

` optional .google.cloud.compute.v1.NodeGroupMaintenanceWindow maintenance_window = 186374812; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceWindow field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasNodeTemplate()
    
    
    public abstract boolean hasNodeTemplate()

URL of the node template to create the node group from.

`optional string node_template = 323154455;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeTemplate field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasShareSettings()
    
    
    public abstract boolean hasShareSettings()

Share-settings for the node group

`optional .google.cloud.compute.v1.ShareSettings share_settings = 266668163;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shareSettings field is set.  
  
### hasSize()
    
    
    public abstract boolean hasSize()

Output only. [Output Only] The total number of nodes in the node group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the size field is set.  
  
### hasStatus()
    
    
    public abstract boolean hasStatus()

Check the Status enum for the list of possible values.

`optional string status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the status field is set.  
  
### hasZone()
    
    
    public abstract boolean hasZone()

Output only. [Output Only] The name of the zone where the node group resides, such as us-central1-a.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zone field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
