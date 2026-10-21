---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions
title: REST Resource: projects.locations.qaScorecards.revisions \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:09:53.614915+00:00
---

# REST Resource: projects.locations.qaScorecards.revisions  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.qaScorecards.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: QaScorecardRevision
    * JSON representation
  * State
  * Methods



## Resource: QaScorecardRevision

A revision of a QaScorecard.

Modifying published scorecard fields would invalidate existing scorecard results — the questions may have changed, or the score weighting will make existing scores impossible to understand. So changes must create a new revision, rather than modifying the existing resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "snapshot": {
        object ([QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards#QaScorecard))
      },
      "createTime": string,
      "alternateIds": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the scorecard revision. Format: projects/{project}/locations/{location}/qaScorecards/{qaScorecard}/revisions/{revision}  
`snapshot` |  `object (`[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards#QaScorecard)`)` The snapshot of the scorecard at the time of this revision's creation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`alternateIds[]` |  `string` Output only. Alternative IDs for this revision of the scorecard, e.g., `latest`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions#State)`)` Output only. State of the scorecard revision, indicating whether it's ready to be used in analysis.  
  
## State

Enum representing the set of states a scorecard revision may be in.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`EDITABLE` | The scorecard revision can be edited.  
`TRAINING` | Scorecard model training is in progress.  
`TRAINING_FAILED` | Scorecard revision model training failed.  
`READY` | The revision can be used in analysis.  
`DELETING` | Scorecard is being deleted.  
`TRAINING_CANCELLED` | Scorecard model training was explicitly cancelled by the user.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/create)`

|  Creates a QaScorecardRevision.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/delete)`

|  Deletes a QaScorecardRevision.  
  
### `[deploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/deploy)`

|  Deploy a QaScorecardRevision.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/get)`

|  Gets a QaScorecardRevision.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/list)`

|  Lists all revisions under the parent QaScorecard.  
  
### `[tuneQaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/tuneQaScorecardRevision)`

|  Fine tune one or more QaModels.  
  
### `[undeploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/undeploy)`

|  Undeploy a QaScorecardRevision.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
