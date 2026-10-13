---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework/
title: AssessedFramework \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:39.317907+00:00
---

# AssessedFramework  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  AssessedFramework Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AssessmentFinding
    * JSON representation
  * RemediationStep
    * JSON representation
  * FindingADCMetadata
    * JSON representation
  * AssetDetails
    * JSON representation
  * SCCMetadata
    * JSON representation



Framework assessed and their findings.

JSON representation  
---  
      
    
    {
      "framework": {
        object ([Framework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Framework))
      },
      "findings": [
        {
          object ([AssessmentFinding](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#AssessmentFinding))
        }
      ],
      "scoreCard": {
        object ([ScoreCard](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ScoreCard))
      },
      "skipped": boolean,
      "skippedReason": string
    }  
  
Fields  
---  
`framework` |  `object (`[Framework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Framework)`)` Required. The framework that was assessed.  
`findings[]` |  `object (`[AssessmentFinding](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#AssessmentFinding)`)` Required. A list of every Finding found during the assessment.  
`scoreCard` |  `object (`[ScoreCard](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ScoreCard)`)` Optional. Score card associated with the report.  
`skipped` |  `boolean` Optional. Whether the framework was skipped during assessment.  
`skippedReason` |  `string` Optional. Reason for skipping the framework during assessment.  
  
## AssessmentFinding

Details of an Assessment Finding.

JSON representation  
---  
      
    
    {
      "id": string,
      "assessedFrameworkId": string,
      "adcMetadata": {
        object ([FindingADCMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#FindingADCMetadata))
      },
      "findingType": enum (Type),
      "severity": enum ([Severity](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Severity)),
      "assessedAsset": {
        object ([AssetDetails](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#AssetDetails))
      },
      "assessedFramework": {
        object ([Framework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Framework))
      },
      "description": string,
      "findingsUri": string,
      "sccMetadata": {
        object ([SCCMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#SCCMetadata))
      },
    
      // Union field next_step can be only one of the following:
      "remediationStep": {
        object ([RemediationStep](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#RemediationStep))
      }
      // End of list of possible types for union field next_step.
    
      // Union field additional_details can be only one of the following:
      "additionalNotes": string
      // End of list of possible types for union field additional_details.
    }  
  
Fields  
---  
`id` |  `string` Output only. The Finding ID.  
`assessedFrameworkId` |  `string` Optional. The framework that was assessed.  
`adcMetadata` |  `object (`[FindingADCMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#FindingADCMetadata)`)` Output only. Metadata related to the Application Design Center with the finding.  
`findingType` |  `enum (`Type`)` Required. The type of the finding. Findings can be informational, warning, or error.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Severity)`)` Optional. The severity of the finding.  
`assessedAsset` |  `object (`[AssetDetails](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#AssetDetails)`)` Required. Details of the Cloud Asset Inventory asset that was assessed.  
`assessedFramework` |  `object (`[Framework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Framework)`)` Optional. Details of the framework that was assessed.  
`description` |  `string` Optional. Description of the finding.  
`findingsUri` |  `string` Optional. Link to the findings, if persisted by the domain.  
`sccMetadata` |  `object (`[SCCMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#SCCMetadata)`)` Output only. SCC related metadata for the finding.  
Union field `next_step`. Next steps related to the findings. `next_step` can be only one of the following:  
`remediationStep` |  `object (`[RemediationStep](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework#RemediationStep)`)` Optional. A description of the steps that users can take to fix the finding.  
Union field `additional_details`. Additional details about the finding. `additional_details` can be only one of the following:  
`additionalNotes` |  `string` Optional. A description of the additional details about finding.  
  
## RemediationStep

Remediation steps that can be taken to rectify the finding.

JSON representation  
---  
      
    
    {
      "remediationSteps": [
        string
      ],
      "remediationDocumentationUrl": string,
      "note": string
    }  
  
Fields  
---  
`remediationSteps[]` |  `string` Required. A description of the steps that users can take to remediate the findings.  
`remediationDocumentationUrl` |  `string` Optional. Remediation documentation URL.  
`note` |  `string` Optional. Any other note related to the remediation.  
  
## FindingADCMetadata

Metadata related to the Application Design Center with the finding.

JSON representation  
---  
      
    
    {
      "componentName": string
    }  
  
Fields  
---  
`componentName` |  `string` Output only. Component the finding belongs to.  
  
## AssetDetails

Details of a Cloud Asset Inventory asset that caused the finding.

JSON representation  
---  
      
    
    {
      "assetId": string,
      "assetType": string
    }  
  
Fields  
---  
`assetId` |  `string` Required. Information about the Cloud Asset Inventory asset that the framework is assessed against. The full resource name of the asset in CAIS format.For details about the format of the full resource name for each asset type, see [Resource name format](https://cloud.google.com/asset-inventory/docs/resource-name-format).  
`assetType` |  `string` Optional. The type of Cloud Asset Inventory asset. For a list of asset types, see [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types).  
  
## SCCMetadata

SCC metadata for the assessment finding.

JSON representation  
---  
      
    
    {
      "findingClass": string,
      "findingType": string
    }  
  
Fields  
---  
`findingClass` |  `string` Optional. The SCC finding class. Also known as category.  
`findingType` |  `string` Optional. The SCC finding type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
