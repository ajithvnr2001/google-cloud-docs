---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockersOrBuilder
title: Interface InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockersOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:06.085533+00:00
---

# Interface InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockersOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockersOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockersOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockersOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttachments(int index)
    
    
    public abstract String getAttachments(int index)

Output only. [Output Only] URLs of any particular Attachments to explain this blocker in more detail.

`repeated string attachments = 334744496;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The attachments at the given index.  
  
### getAttachmentsBytes(int index)
    
    
    public abstract ByteString getAttachmentsBytes(int index)

Output only. [Output Only] URLs of any particular Attachments to explain this blocker in more detail.

`repeated string attachments = 334744496;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the attachments at the given index.  
  
### getAttachmentsCount()
    
    
    public abstract int getAttachmentsCount()

Output only. [Output Only] URLs of any particular Attachments to explain this blocker in more detail.

`repeated string attachments = 334744496;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of attachments.  
  
### getAttachmentsList()
    
    
    public abstract List<String> getAttachmentsList()

Output only. [Output Only] URLs of any particular Attachments to explain this blocker in more detail.

`repeated string attachments = 334744496;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the attachments.  
  
### getBlockerType()
    
    
    public abstract String getBlockerType()

Check the BlockerType enum for the list of possible values.

`optional string blocker_type = 381194847;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The blockerType.  
  
### getBlockerTypeBytes()
    
    
    public abstract ByteString getBlockerTypeBytes()

Check the BlockerType enum for the list of possible values.

`optional string blocker_type = 381194847;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for blockerType.  
  
### getDocumentationLink()
    
    
    public abstract String getDocumentationLink()

Output only. [Output Only] The url of Google Cloud public documentation explaining this requirement. This is set for every type of requirement.

`optional string documentation_link = 93465183;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The documentationLink.  
  
### getDocumentationLinkBytes()
    
    
    public abstract ByteString getDocumentationLinkBytes()

Output only. [Output Only] The url of Google Cloud public documentation explaining this requirement. This is set for every type of requirement.

`optional string documentation_link = 93465183;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for documentationLink.  
  
### getExplanation()
    
    
    public abstract String getExplanation()

Output only. [Output Only] A human-readable explanation of this requirement and why it's not met. This is set for every type of requirement.

`optional string explanation = 504745497;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The explanation.  
  
### getExplanationBytes()
    
    
    public abstract ByteString getExplanationBytes()

Output only. [Output Only] A human-readable explanation of this requirement and why it's not met. This is set for every type of requirement.

`optional string explanation = 504745497;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for explanation.  
  
### getMetros(int index)
    
    
    public abstract String getMetros(int index)

Output only. [Output Only] Metros used to explain this blocker in more detail. These are three-letter lowercase strings like "iad". This will be set for some blockers (like NO_ATTACHMENTS_IN_METRO_AND_ZONE) but does not apply to others.

`repeated string metros = 533067386;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metros at the given index.  
  
### getMetrosBytes(int index)
    
    
    public abstract ByteString getMetrosBytes(int index)

Output only. [Output Only] Metros used to explain this blocker in more detail. These are three-letter lowercase strings like "iad". This will be set for some blockers (like NO_ATTACHMENTS_IN_METRO_AND_ZONE) but does not apply to others.

`repeated string metros = 533067386;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the metros at the given index.  
  
### getMetrosCount()
    
    
    public abstract int getMetrosCount()

Output only. [Output Only] Metros used to explain this blocker in more detail. These are three-letter lowercase strings like "iad". This will be set for some blockers (like NO_ATTACHMENTS_IN_METRO_AND_ZONE) but does not apply to others.

`repeated string metros = 533067386;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of metros.  
  
### getMetrosList()
    
    
    public abstract List<String> getMetrosList()

Output only. [Output Only] Metros used to explain this blocker in more detail. These are three-letter lowercase strings like "iad". This will be set for some blockers (like NO_ATTACHMENTS_IN_METRO_AND_ZONE) but does not apply to others.

`repeated string metros = 533067386;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the metros.  
  
### getRegions(int index)
    
    
    public abstract String getRegions(int index)

Output only. [Output Only] Regions used to explain this blocker in more detail. These are region names formatted like "us-central1". This will be set for some blockers (like INCOMPATIBLE_REGIONS) but does not apply to others.

`repeated string regions = 12367871;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The regions at the given index.  
  
### getRegionsBytes(int index)
    
    
    public abstract ByteString getRegionsBytes(int index)

Output only. [Output Only] Regions used to explain this blocker in more detail. These are region names formatted like "us-central1". This will be set for some blockers (like INCOMPATIBLE_REGIONS) but does not apply to others.

`repeated string regions = 12367871;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the regions at the given index.  
  
### getRegionsCount()
    
    
    public abstract int getRegionsCount()

Output only. [Output Only] Regions used to explain this blocker in more detail. These are region names formatted like "us-central1". This will be set for some blockers (like INCOMPATIBLE_REGIONS) but does not apply to others.

`repeated string regions = 12367871;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of regions.  
  
### getRegionsList()
    
    
    public abstract List<String> getRegionsList()

Output only. [Output Only] Regions used to explain this blocker in more detail. These are region names formatted like "us-central1". This will be set for some blockers (like INCOMPATIBLE_REGIONS) but does not apply to others.

`repeated string regions = 12367871;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the regions.  
  
### getZones(int index)
    
    
    public abstract String getZones(int index)

Output only. [Output Only] Zones used to explain this blocker in more detail. Format is "zone1" and/or "zone2". This will be set for some blockers (like MISSING_ZONE) but does not apply to others.

`repeated string zones = 116085319;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zones at the given index.  
  
### getZonesBytes(int index)
    
    
    public abstract ByteString getZonesBytes(int index)

Output only. [Output Only] Zones used to explain this blocker in more detail. Format is "zone1" and/or "zone2". This will be set for some blockers (like MISSING_ZONE) but does not apply to others.

`repeated string zones = 116085319;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the zones at the given index.  
  
### getZonesCount()
    
    
    public abstract int getZonesCount()

Output only. [Output Only] Zones used to explain this blocker in more detail. Format is "zone1" and/or "zone2". This will be set for some blockers (like MISSING_ZONE) but does not apply to others.

`repeated string zones = 116085319;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of zones.  
  
### getZonesList()
    
    
    public abstract List<String> getZonesList()

Output only. [Output Only] Zones used to explain this blocker in more detail. Format is "zone1" and/or "zone2". This will be set for some blockers (like MISSING_ZONE) but does not apply to others.

`repeated string zones = 116085319;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the zones.  
  
### hasBlockerType()
    
    
    public abstract boolean hasBlockerType()

Check the BlockerType enum for the list of possible values.

`optional string blocker_type = 381194847;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the blockerType field is set.  
  
### hasDocumentationLink()
    
    
    public abstract boolean hasDocumentationLink()

Output only. [Output Only] The url of Google Cloud public documentation explaining this requirement. This is set for every type of requirement.

`optional string documentation_link = 93465183;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the documentationLink field is set.  
  
### hasExplanation()
    
    
    public abstract boolean hasExplanation()

Output only. [Output Only] A human-readable explanation of this requirement and why it's not met. This is set for every type of requirement.

`optional string explanation = 504745497;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the explanation field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
