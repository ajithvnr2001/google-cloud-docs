---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.InvestigationOrBuilder
title: Interface InvestigationOrBuilder (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:20.735166+00:00
---

# Interface InvestigationOrBuilder (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.InvestigationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InvestigationOrBuilder (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public interface InvestigationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getComments(int index)
    
    
    public abstract String getComments(int index)

Comment added by the Analyst.

`repeated string comments = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The comments at the given index.  
  
### getCommentsBytes(int index)
    
    
    public abstract ByteString getCommentsBytes(int index)

Comment added by the Analyst.

`repeated string comments = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the comments at the given index.  
  
### getCommentsCount()
    
    
    public abstract int getCommentsCount()

Comment added by the Analyst.

`repeated string comments = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of comments.  
  
### getCommentsList()
    
    
    public abstract List<String> getCommentsList()

Comment added by the Analyst.

`repeated string comments = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the comments.  
  
### getId()
    
    
    public abstract String getId()

Identifier for the investigation

`optional string id = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Identifier for the investigation

`optional string id = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getPriority()
    
    
    public abstract Priority getPriority()

Priority of the Alert or Finding set by analyst.

`optional .google.backstory.Priority priority = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Priority](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Priority)` | The priority.  
  
### getPriorityValue()
    
    
    public abstract int getPriorityValue()

Priority of the Alert or Finding set by analyst.

`optional .google.backstory.Priority priority = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for priority.  
  
### getReason()
    
    
    public abstract Reason getReason()

Reason for closing the Case or Alert.

`optional .google.backstory.Reason reason = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Reason](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Reason)` | The reason.  
  
### getReasonValue()
    
    
    public abstract int getReasonValue()

Reason for closing the Case or Alert.

`optional .google.backstory.Reason reason = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for reason.  
  
### getReputation()
    
    
    public abstract Reputation getReputation()

Describes whether a finding was useful or not-useful.

`optional .google.backstory.Reputation reputation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Reputation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Reputation)` | The reputation.  
  
### getReputationValue()
    
    
    public abstract int getReputationValue()

Describes whether a finding was useful or not-useful.

`optional .google.backstory.Reputation reputation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for reputation.  
  
### getRiskScore()
    
    
    public abstract int getRiskScore()

Risk score for a finding set by an analyst.

`optional uint32 risk_score = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The riskScore.  
  
### getRootCause()
    
    
    public abstract String getRootCause()

Root cause of the Alert or Finding set by analyst.

`optional string root_cause = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The rootCause.  
  
### getRootCauseBytes()
    
    
    public abstract ByteString getRootCauseBytes()

Root cause of the Alert or Finding set by analyst.

`optional string root_cause = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for rootCause.  
  
### getSeverityScore()
    
    
    public abstract int getSeverityScore()

Severity score for a finding set by an analyst.

`optional uint32 severity_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The severityScore.  
  
### getStatus()
    
    
    public abstract Status getStatus()

Describes the workflow status of a finding.

`optional .google.backstory.Status status = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Status)` | The status.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Describes the workflow status of a finding.

`optional .google.backstory.Status status = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getVerdict()
    
    
    public abstract Verdict getVerdict()

Describes reason a finding investigation was resolved.

`optional .google.backstory.Verdict verdict = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Verdict](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Verdict)` | The verdict.  
  
### getVerdictValue()
    
    
    public abstract int getVerdictValue()

Describes reason a finding investigation was resolved.

`optional .google.backstory.Verdict verdict = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for verdict.  
  
### hasId()
    
    
    public abstract boolean hasId()

Identifier for the investigation

`optional string id = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasPriority()
    
    
    public abstract boolean hasPriority()

Priority of the Alert or Finding set by analyst.

`optional .google.backstory.Priority priority = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the priority field is set.  
  
### hasReason()
    
    
    public abstract boolean hasReason()

Reason for closing the Case or Alert.

`optional .google.backstory.Reason reason = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reason field is set.  
  
### hasReputation()
    
    
    public abstract boolean hasReputation()

Describes whether a finding was useful or not-useful.

`optional .google.backstory.Reputation reputation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reputation field is set.  
  
### hasRiskScore()
    
    
    public abstract boolean hasRiskScore()

Risk score for a finding set by an analyst.

`optional uint32 risk_score = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the riskScore field is set.  
  
### hasRootCause()
    
    
    public abstract boolean hasRootCause()

Root cause of the Alert or Finding set by analyst.

`optional string root_cause = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rootCause field is set.  
  
### hasSeverityScore()
    
    
    public abstract boolean hasSeverityScore()

Severity score for a finding set by an analyst.

`optional uint32 severity_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the severityScore field is set.  
  
### hasStatus()
    
    
    public abstract boolean hasStatus()

Describes the workflow status of a finding.

`optional .google.backstory.Status status = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the status field is set.  
  
### hasVerdict()
    
    
    public abstract boolean hasVerdict()

Describes reason a finding investigation was resolved.

`optional .google.backstory.Verdict verdict = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the verdict field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
