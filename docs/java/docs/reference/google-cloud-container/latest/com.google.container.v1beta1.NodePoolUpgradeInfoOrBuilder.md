---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfoOrBuilder
title: Interface NodePoolUpgradeInfoOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:40.285142+00:00
---

# Interface NodePoolUpgradeInfoOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NodePoolUpgradeInfoOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface NodePoolUpgradeInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutoUpgradeStatus(int index)
    
    
    public abstract NodePoolUpgradeInfo.AutoUpgradeStatus getAutoUpgradeStatus(int index)

The auto upgrade status.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus auto_upgrade_status = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeInfo.AutoUpgradeStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus)` | The autoUpgradeStatus at the given index.  
  
### getAutoUpgradeStatusCount()
    
    
    public abstract int getAutoUpgradeStatusCount()

The auto upgrade status.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus auto_upgrade_status = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of autoUpgradeStatus.  
  
### getAutoUpgradeStatusList()
    
    
    public abstract List<NodePoolUpgradeInfo.AutoUpgradeStatus> getAutoUpgradeStatusList()

The auto upgrade status.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus auto_upgrade_status = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AutoUpgradeStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus)>` | A list containing the autoUpgradeStatus.  
  
### getAutoUpgradeStatusValue(int index)
    
    
    public abstract int getAutoUpgradeStatusValue(int index)

The auto upgrade status.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus auto_upgrade_status = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of autoUpgradeStatus at the given index.  
  
### getAutoUpgradeStatusValueList()
    
    
    public abstract List<Integer> getAutoUpgradeStatusValueList()

The auto upgrade status.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradeStatus auto_upgrade_status = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for autoUpgradeStatus.  
  
### getEndOfExtendedSupportTimestamp()
    
    
    public abstract String getEndOfExtendedSupportTimestamp()

The node pool's current minor version's end of extended support timestamp.

`optional string end_of_extended_support_timestamp = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endOfExtendedSupportTimestamp.  
  
### getEndOfExtendedSupportTimestampBytes()
    
    
    public abstract ByteString getEndOfExtendedSupportTimestampBytes()

The node pool's current minor version's end of extended support timestamp.

`optional string end_of_extended_support_timestamp = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endOfExtendedSupportTimestamp.  
  
### getEndOfStandardSupportTimestamp()
    
    
    public abstract String getEndOfStandardSupportTimestamp()

The node pool's current minor version's end of standard support timestamp.

`optional string end_of_standard_support_timestamp = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endOfStandardSupportTimestamp.  
  
### getEndOfStandardSupportTimestampBytes()
    
    
    public abstract ByteString getEndOfStandardSupportTimestampBytes()

The node pool's current minor version's end of standard support timestamp.

`optional string end_of_standard_support_timestamp = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endOfStandardSupportTimestamp.  
  
### getMinorTargetVersion()
    
    
    public abstract String getMinorTargetVersion()

minor_target_version indicates the target version for minor upgrade.

`optional string minor_target_version = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minorTargetVersion.  
  
### getMinorTargetVersionBytes()
    
    
    public abstract ByteString getMinorTargetVersionBytes()

minor_target_version indicates the target version for minor upgrade.

`optional string minor_target_version = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minorTargetVersion.  
  
### getPatchTargetVersion()
    
    
    public abstract String getPatchTargetVersion()

patch_target_version indicates the target version for patch upgrade.

`optional string patch_target_version = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The patchTargetVersion.  
  
### getPatchTargetVersionBytes()
    
    
    public abstract ByteString getPatchTargetVersionBytes()

patch_target_version indicates the target version for patch upgrade.

`optional string patch_target_version = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for patchTargetVersion.  
  
### getPausedReason(int index)
    
    
    public abstract NodePoolUpgradeInfo.AutoUpgradePausedReason getPausedReason(int index)

The auto upgrade paused reason.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason paused_reason = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeInfo.AutoUpgradePausedReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason)` | The pausedReason at the given index.  
  
### getPausedReasonCount()
    
    
    public abstract int getPausedReasonCount()

The auto upgrade paused reason.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason paused_reason = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of pausedReason.  
  
### getPausedReasonList()
    
    
    public abstract List<NodePoolUpgradeInfo.AutoUpgradePausedReason> getPausedReasonList()

The auto upgrade paused reason.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason paused_reason = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AutoUpgradePausedReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason)>` | A list containing the pausedReason.  
  
### getPausedReasonValue(int index)
    
    
    public abstract int getPausedReasonValue(int index)

The auto upgrade paused reason.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason paused_reason = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of pausedReason at the given index.  
  
### getPausedReasonValueList()
    
    
    public abstract List<Integer> getPausedReasonValueList()

The auto upgrade paused reason.

` repeated .google.container.v1beta1.NodePoolUpgradeInfo.AutoUpgradePausedReason paused_reason = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for pausedReason.  
  
### getUpgradeDetails(int index)
    
    
    public abstract UpgradeDetails getUpgradeDetails(int index)

The list of past auto upgrades.

`repeated .google.container.v1beta1.UpgradeDetails upgrade_details = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UpgradeDetails)` |   
  
### getUpgradeDetailsCount()
    
    
    public abstract int getUpgradeDetailsCount()

The list of past auto upgrades.

`repeated .google.container.v1beta1.UpgradeDetails upgrade_details = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUpgradeDetailsList()
    
    
    public abstract List<UpgradeDetails> getUpgradeDetailsList()

The list of past auto upgrades.

`repeated .google.container.v1beta1.UpgradeDetails upgrade_details = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpgradeDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UpgradeDetails)>` |   
  
### getUpgradeDetailsOrBuilder(int index)
    
    
    public abstract UpgradeDetailsOrBuilder getUpgradeDetailsOrBuilder(int index)

The list of past auto upgrades.

`repeated .google.container.v1beta1.UpgradeDetails upgrade_details = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UpgradeDetailsOrBuilder)` |   
  
### getUpgradeDetailsOrBuilderList()
    
    
    public abstract List<? extends UpgradeDetailsOrBuilder> getUpgradeDetailsOrBuilderList()

The list of past auto upgrades.

`repeated .google.container.v1beta1.UpgradeDetails upgrade_details = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1beta1.UpgradeDetailsOrBuilder>` |   
  
### hasEndOfExtendedSupportTimestamp()
    
    
    public abstract boolean hasEndOfExtendedSupportTimestamp()

The node pool's current minor version's end of extended support timestamp.

`optional string end_of_extended_support_timestamp = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endOfExtendedSupportTimestamp field is set.  
  
### hasEndOfStandardSupportTimestamp()
    
    
    public abstract boolean hasEndOfStandardSupportTimestamp()

The node pool's current minor version's end of standard support timestamp.

`optional string end_of_standard_support_timestamp = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endOfStandardSupportTimestamp field is set.  
  
### hasMinorTargetVersion()
    
    
    public abstract boolean hasMinorTargetVersion()

minor_target_version indicates the target version for minor upgrade.

`optional string minor_target_version = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minorTargetVersion field is set.  
  
### hasPatchTargetVersion()
    
    
    public abstract boolean hasPatchTargetVersion()

patch_target_version indicates the target version for patch upgrade.

`optional string patch_target_version = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the patchTargetVersion field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
