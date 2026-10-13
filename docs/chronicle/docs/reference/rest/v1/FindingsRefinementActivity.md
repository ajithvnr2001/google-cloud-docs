---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementActivity/
title: FindingsRefinementActivity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:29.230500+00:00
---

# FindingsRefinementActivity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementActivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  FindingsRefinementActivity Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DetectionExclusionActivity
    * JSON representation
  * DetectionExclusionDetectorActivity
    * JSON representation



The activity for a specific findings refinement.

JSON representation  
---  
      
    
    {
      "findingsRefinement": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "detectionExclusionActivity": {
        object ([DetectionExclusionActivity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementActivity#DetectionExclusionActivity))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`findingsRefinement` |  `string` Required. Full resource name for the findings refinement this activity corresponds to. Format: projects/{project}/locations/{region}/instances/{instance}/findingsRefinements/{findingsRefinement}  
The activity for the findings refinement. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`detectionExclusionActivity` |  `object (`[DetectionExclusionActivity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementActivity#DetectionExclusionActivity)`)` The activity for the detection exclusion.  
End of mutually exclusive fields.  
  
## DetectionExclusionActivity

The activity for a findings refinement that is a detection exclusion. The activity is broken down per detector.

JSON representation  
---  
      
    
    {
      "detectionExclusionDetectorActivities": [
        {
          object ([DetectionExclusionDetectorActivity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementActivity#DetectionExclusionDetectorActivity))
        }
      ]
    }  
  
Fields  
---  
`detectionExclusionDetectorActivities[]` |  `object (`[DetectionExclusionDetectorActivity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementActivity#DetectionExclusionDetectorActivity)`)` The activity for the detection exclusion broken down by detector.  
  
## DetectionExclusionDetectorActivity

The activity for a findings refinement that is a detection exclusion broken down for one specific detector.

JSON representation  
---  
      
    
    {
      "excludedDetectionCount": string,
      "totalDetectionCount": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "curatedRule": string,
      "curatedRuleSet": string,
      "rule": string,
      "deletedCuratedRuleSet": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`excludedDetectionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of detections for the detector that were excluded by the detection exclusion.  
`totalDetectionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of detections found by the detector. This includes both excluded detections and non-excluded detections.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`curatedRule` |  `string` Full resource name for the curated rule this activity corresponds to. Format: projects/{project}/locations/{location}/instances/{instance}/curatedRules/{rule}  
`curatedRuleSet` |  `string` Full resource name for the curated rule set this activity corresponds to. This field will only be set if the customer has access to the curated rule set the exclusion is applied to. Format: projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{curatedRuleSetCategory}/curatedRuleSets/{curatedRuleSet}  
`rule` |  `string` Full resource name for the rule this activity corresponds to. Format: projects/{project}/locations/{location}/instances/{instance}/rules/{rule}  
`deletedCuratedRuleSet` |  `string` Full resource name for the deleted curated rule set this activity corresponds to. This field will only be set if the customer does not have access to the curated rule set the exclusion is applied to. Format: projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{curatedRuleSetCategory}/curatedRuleSets/{curatedRuleSet}  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
