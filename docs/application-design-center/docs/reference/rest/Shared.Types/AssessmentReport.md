---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport/
title: AssessmentReport \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:39.515463+00:00
---

# AssessmentReport  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  AssessmentReport Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DomainAssessmentReport
    * JSON representation
  * DomainRedirectInfo
    * JSON representation
  * SkippedDomain
    * JSON representation



Aggregated assessment report from all domains.

JSON representation  
---  
      
    
    {
      "domainAssessmentReports": [
        {
          object ([DomainAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport#DomainAssessmentReport))
        }
      ],
      "skippedDomains": [
        {
          object ([SkippedDomain](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport#SkippedDomain))
        }
      ],
      "createTime": string,
    
      // Union field adc_resource_uri can be only one of the following:
      "adcApplicationUri": string,
      "adcApplicationTemplateUri": string,
      "adcCatalogTemplateUri": string,
      "adcSpaceUri": string
      // End of list of possible types for union field adc_resource_uri.
    }  
  
Fields  
---  
`domainAssessmentReports[]` |  `object (`[DomainAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport#DomainAssessmentReport)`)` Output only. Generated best practice reports.  
`skippedDomains[]` |  `object (`[SkippedDomain](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport#SkippedDomain)`)` Output only. Skipped domains.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the report was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `adc_resource_uri`. Resource associated with the report. `adc_resource_uri` can be only one of the following:  
`adcApplicationUri` |  `string` Output only. Application URI.  
`adcApplicationTemplateUri` |  `string` Output only. Application Template URI.  
`adcCatalogTemplateUri` |  `string` Output only. Catalog Template URI.  
`adcSpaceUri` |  `string` Output only. Space URI.  
  
## DomainAssessmentReport

The assessment report for each domain.

JSON representation  
---  
      
    
    {
      "reportName": string,
      "domainId": string,
      "createTime": string,
      "updateTime": string,
      "status": enum ([Status](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Status)),
      "adcMetadata": {
        object ([AdcMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AdcMetadata))
      },
      "assessedFrameworks": [
        {
          object ([AssessedFramework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework))
        }
      ],
      "additionalInfo": string,
      "skippedAssetTypes": [
        string
      ],
      "domainRedirectInfo": {
        object ([DomainRedirectInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport#DomainRedirectInfo))
      },
      "reportScore": {
        object ([ScoreCard](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ScoreCard))
      }
    }  
  
Fields  
---  
`reportName` |  `string` Optional. The report name as per Application Design Center.  
`domainId` |  `string` Output only. The ID of the domain.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the report was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the report was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Status)`)` Optional. Status of assessment report.  
`adcMetadata` |  `object (`[AdcMetadata](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AdcMetadata)`)` Output only. Specific information and metadata.  
`assessedFrameworks[]` |  `object (`[AssessedFramework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessedFramework)`)` Required. List of frameworks assessed and their findings.  
`additionalInfo` |  `string` Optional. Additional information about the report.  
`skippedAssetTypes[]` |  `string` Optional. List of asset types skipped during assessment.  
`domainRedirectInfo` |  `object (`[DomainRedirectInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport#DomainRedirectInfo)`)` Optional. Information on how to redirect to domain.  
`reportScore` |  `object (`[ScoreCard](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ScoreCard)`)` Output only. Score card associated with the report.  
  
## DomainRedirectInfo

Information on how to redirect to domain.

JSON representation  
---  
      
    
    {
      "url": string,
      "urlText": string,
      "openInSameTab": boolean
    }  
  
Fields  
---  
`url` |  `string` Required. URL to the domain page.  
`urlText` |  `string` Required. Text to display in UI on the redirect URL.  
`openInSameTab` |  `boolean` Optional. Flag to open the URL in new tab. Default: false.  
  
## SkippedDomain

Domains skipped during the best practice assessment.

JSON representation  
---  
      
    
    {
      "domain": {
        object ([Domain](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Domain))
      },
      "skipReason": enum ([Reason](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Reason))
    }  
  
Fields  
---  
`domain` |  `object (`[Domain](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Domain)`)` Output only. Details of the domain skipped.  
`skipReason` |  `enum (`[Reason](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Reason)`)` Output only. Reason for skipping the domain from assessment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
