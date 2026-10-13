---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseEvidence/
title: CaseEvidence \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:21.824523+00:00
---

# CaseEvidence  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseEvidence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  CaseEvidence Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvidenceType



Represents a piece of evidence associated with a Chronicle case. Evidence can be of various types, such as alerts, detections, or events.

JSON representation  
---  
      
    
    {
      "evidenceType": enum ([EvidenceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseEvidence#EvidenceType)),
      "evidenceId": string,
      "attachTime": string,
      "attacher": string,
      "sourceEvidenceId": string,
      "sourceEvidenceType": enum ([EvidenceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseEvidence#EvidenceType)),
      "sourceEvidenceKey": string,
      "soarEvidenceId": string
    }  
  
Fields  
---  
`evidenceType` |  `enum (`[EvidenceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseEvidence#EvidenceType)`)` Output only. The type of evidence.  
`evidenceId` |  `string` Output only. The unique identifier of the evidence.  
`attachTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the evidence was attached to the Case.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attacher` |  `string` Output only. The user who attached the evidence to the Case.  
`sourceEvidenceId` |  `string` Output only. The ID of the evidence that this evidence was extracted from.  
`sourceEvidenceType` |  `enum (`[EvidenceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseEvidence#EvidenceType)`)` Output only. The type of evidence that this evidence was extracted from.  
`sourceEvidenceKey` |  `string` Output only. The key of the evidence that this evidence was extracted from.  
`soarEvidenceId` |  `string` Output only. The ID of the evidence in SOAR.  
  
## EvidenceType

Describes the type of evidence a case evidence is. Note: This enum is not frozen and new values are likely to be added in the future.

Enums  
---  
`EVIDENCE_TYPE_UNSPECIFIED` | The evidence type is unspecified.  
`EVIDENCE_TYPE_ALERT` | The evidence type is alert.  
`EVIDENCE_TYPE_EVENT` | The evidence type is event.  
`EVIDENCE_TYPE_DETECTION` | The evidence type is detection.  
`EVIDENCE_TYPE_ENTITY` | The evidence type is entity.  
`EVIDENCE_TYPE_RULE_MATCH_ENTITY` | The evidence type is rule match entity.  
`EVIDENCE_TYPE_RULE_OUTCOME_ENTITY` | The evidence type is rule outcome entity.  
`EVIDENCE_TYPE_UDM_PRINCIPAL_ENTITY` | The evidence type is UDM entity principal.  
`EVIDENCE_TYPE_UDM_TARGET_ENTITY` | The evidence type is UDM entity target.  
`EVIDENCE_TYPE_UDM_ABOUT_ENTITY` | The evidence type is UDM entity about.  
`EVIDENCE_TYPE_THREAT_HUNT` | The evidence type is threat hunt.  
`EVIDENCE_TYPE_TINA_INVESTIGATION` | The evidence type is investigation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
