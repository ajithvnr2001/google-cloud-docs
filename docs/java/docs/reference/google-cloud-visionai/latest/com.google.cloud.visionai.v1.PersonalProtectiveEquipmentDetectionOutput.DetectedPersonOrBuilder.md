---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.DetectedPersonOrBuilder
title: Interface PersonalProtectiveEquipmentDetectionOutput.DetectedPersonOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:35.190802+00:00
---

# Interface PersonalProtectiveEquipmentDetectionOutput.DetectedPersonOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.DetectedPersonOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PersonalProtectiveEquipmentDetectionOutput.DetectedPersonOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface PersonalProtectiveEquipmentDetectionOutput.DetectedPersonOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBodyCoverageScore()
    
    
    public abstract float getBodyCoverageScore()

Coverage score for body.

`optional float body_coverage_score = 8;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bodyCoverageScore.  
  
### getDetectedPersonIdentifiedBox()
    
    
    public abstract PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox getDetectedPersonIdentifiedBox()

The info of detected person identified box.

` .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox detected_person_identified_box = 2; `

**Returns**  
---  
**Type** | **Description**  
`[PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox)` | The detectedPersonIdentifiedBox.  
  
### getDetectedPersonIdentifiedBoxOrBuilder()
    
    
    public abstract PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBoxOrBuilder getDetectedPersonIdentifiedBoxOrBuilder()

The info of detected person identified box.

` .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox detected_person_identified_box = 2; `

**Returns**  
---  
**Type** | **Description**  
`[PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBoxOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBoxOrBuilder)` |   
  
### getDetectedPpeIdentifiedBoxes(int index)
    
    
    public abstract PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox getDetectedPpeIdentifiedBoxes(int index)

The info of detected person associated ppe identified boxes.

` repeated .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox detected_ppe_identified_boxes = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox)` |   
  
### getDetectedPpeIdentifiedBoxesCount()
    
    
    public abstract int getDetectedPpeIdentifiedBoxesCount()

The info of detected person associated ppe identified boxes.

` repeated .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox detected_ppe_identified_boxes = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDetectedPpeIdentifiedBoxesList()
    
    
    public abstract List<PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox> getDetectedPpeIdentifiedBoxesList()

The info of detected person associated ppe identified boxes.

` repeated .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox detected_ppe_identified_boxes = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PPEIdentifiedBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox)>` |   
  
### getDetectedPpeIdentifiedBoxesOrBuilder(int index)
    
    
    public abstract PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBoxOrBuilder getDetectedPpeIdentifiedBoxesOrBuilder(int index)

The info of detected person associated ppe identified boxes.

` repeated .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox detected_ppe_identified_boxes = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBoxOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBoxOrBuilder)` |   
  
### getDetectedPpeIdentifiedBoxesOrBuilderList()
    
    
    public abstract List<? extends PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBoxOrBuilder> getDetectedPpeIdentifiedBoxesOrBuilderList()

The info of detected person associated ppe identified boxes.

` repeated .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox detected_ppe_identified_boxes = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBoxOrBuilder>` |   
  
### getEyesCoverageScore()
    
    
    public abstract float getEyesCoverageScore()

Coverage score for eyes.

`optional float eyes_coverage_score = 5;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The eyesCoverageScore.  
  
### getFaceCoverageScore()
    
    
    public abstract float getFaceCoverageScore()

Coverage score for each body part. Coverage score for face.

`optional float face_coverage_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The faceCoverageScore.  
  
### getFeetCoverageScore()
    
    
    public abstract float getFeetCoverageScore()

Coverage score for feet.

`optional float feet_coverage_score = 9;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The feetCoverageScore.  
  
### getHandsCoverageScore()
    
    
    public abstract float getHandsCoverageScore()

Coverage score for hands.

`optional float hands_coverage_score = 7;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The handsCoverageScore.  
  
### getHeadCoverageScore()
    
    
    public abstract float getHeadCoverageScore()

Coverage score for head.

`optional float head_coverage_score = 6;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The headCoverageScore.  
  
### getPersonId()
    
    
    public abstract long getPersonId()

The id of detected person.

`int64 person_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The personId.  
  
### hasBodyCoverageScore()
    
    
    public abstract boolean hasBodyCoverageScore()

Coverage score for body.

`optional float body_coverage_score = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bodyCoverageScore field is set.  
  
### hasDetectedPersonIdentifiedBox()
    
    
    public abstract boolean hasDetectedPersonIdentifiedBox()

The info of detected person identified box.

` .google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox detected_person_identified_box = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the detectedPersonIdentifiedBox field is set.  
  
### hasEyesCoverageScore()
    
    
    public abstract boolean hasEyesCoverageScore()

Coverage score for eyes.

`optional float eyes_coverage_score = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eyesCoverageScore field is set.  
  
### hasFaceCoverageScore()
    
    
    public abstract boolean hasFaceCoverageScore()

Coverage score for each body part. Coverage score for face.

`optional float face_coverage_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the faceCoverageScore field is set.  
  
### hasFeetCoverageScore()
    
    
    public abstract boolean hasFeetCoverageScore()

Coverage score for feet.

`optional float feet_coverage_score = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the feetCoverageScore field is set.  
  
### hasHandsCoverageScore()
    
    
    public abstract boolean hasHandsCoverageScore()

Coverage score for hands.

`optional float hands_coverage_score = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the handsCoverageScore field is set.  
  
### hasHeadCoverageScore()
    
    
    public abstract boolean hasHeadCoverageScore()

Coverage score for head.

`optional float head_coverage_score = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the headCoverageScore field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
