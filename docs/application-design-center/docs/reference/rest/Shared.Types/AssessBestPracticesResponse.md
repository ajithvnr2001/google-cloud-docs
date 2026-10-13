---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessBestPracticesResponse/
title: AssessBestPracticesResponse \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:39.649939+00:00
---

# AssessBestPracticesResponse  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessBestPracticesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  AssessBestPracticesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AssessmentResult
    * JSON representation
  * AssessmentFinding
    * JSON representation



A comprehensive assessment report that evaluates an Application Template against industry-standard security and operational benchmarks.

JSON representation  
---  
      
    
    {
      "applicationTemplate": string,
      "assessmentResults": [
        {
          object ([AssessmentResult](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessBestPracticesResponse#AssessmentResult))
        }
      ],
      "summary": string
    }  
  
Fields  
---  
`applicationTemplate` |  `string` Output only. The full canonical Google Cloud resource path of the application template being assessed.  
`assessmentResults[]` |  `object (`[AssessmentResult](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessBestPracticesResponse#AssessmentResult)`)` A collection of evaluation sets, grouped by the specific security or best-practice framework used.  
`summary` |  `string` Output only. A brief summary of the assessment results.  
  
## AssessmentResult

The result of the assess best practices for a framework.

JSON representation  
---  
      
    
    {
      "framework": string,
      "findings": [
        {
          object ([AssessmentFinding](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessBestPracticesResponse#AssessmentFinding))
        }
      ]
    }  
  
Fields  
---  
`framework` |  `string` Output only. The formal name of the regulatory or architectural standard (e.g., NIST, CIS, or Internal Policy).  
`findings[]` |  `object (`[AssessmentFinding](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessBestPracticesResponse#AssessmentFinding)`)` Individual instances where the template deviates from the 'Gold Standard' best practices.  
  
## AssessmentFinding

The details of the assessment finding.

JSON representation  
---  
      
    
    {
      "description": string,
      "severity": string
    }  
  
Fields  
---  
`description` |  `string` Output only. A clear, human-readable explanation of the finding and why it matters for template quality.  
`severity` |  `string` Output only. The risk level of the finding.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
