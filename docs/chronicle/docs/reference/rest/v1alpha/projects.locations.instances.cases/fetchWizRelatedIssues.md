---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues/
title: Method: cases.fetchWizRelatedIssues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:31.094035+00:00
---

# Method: cases.fetchWizRelatedIssues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.fetchWizRelatedIssues Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * WizRelatedIssue
    * JSON representation
  * RelatedEntity
    * JSON representation
  * GreenAgentRemediationAnalysis
    * JSON representation
  * RemediationStep
    * JSON representation
  * StepContent
    * JSON representation
  * WizRemediationAction
    * JSON representation
  * WizRemediationActionType



**Full name** : projects.locations.instances.cases.fetchWizRelatedIssues

Fetches Wiz related security issues for a specific case.

### HTTP request

`GET https://{endpoint}/v1alpha/{name}:fetchWizRelatedIssues`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The case to fetch Wiz related issues for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}  
  
### Query parameters

Parameters  
---  
`alertIdentifiers[]` |  `string` Optional. An optional list of specific alert identifiers used to filter or correlate the Wiz issues.  
  
### Request body

The request body must be empty.

### Response body

Response message for CaseService.FetchWizRelatedIssues.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "relatedIssues": [
        {
          object ([WizRelatedIssue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#WizRelatedIssue))
        }
      ],
      "wizIntegrationConfigured": boolean,
      "wizAlertCount": integer
    }  
  
Fields  
---  
`relatedIssues[]` |  `object (`[WizRelatedIssue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#WizRelatedIssue)`)` Output only. The Wiz related issues.  
`wizIntegrationConfigured` |  `boolean` Output only. Whether Wiz integration is configured.  
`wizAlertCount` |  `integer` Output only. The number of Wiz alerts in the case.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.cases.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## WizRelatedIssue

Represents a security issue from Wiz related to a support case.

JSON representation  
---  
      
    
    {
      "issueId": string,
      "description": string,
      "relatedEntity": {
        object ([RelatedEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#RelatedEntity))
      },
      "url": string,
      "title": string,
      "greenAgentRemediationAnalysis": {
        object ([GreenAgentRemediationAnalysis](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#GreenAgentRemediationAnalysis))
      },
      "riskCategories": [
        string
      ]
    }  
  
Fields  
---  
`issueId` |  `string` Output only. The unique identifier for the issue in Wiz.  
`description` |  `string` Output only. Detailed explanation of the vulnerability or finding.  
`relatedEntity` |  `object (`[RelatedEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#RelatedEntity)`)` Output only. The specific asset affected.  
`url` |  `string` Output only. A direct link to view the issue within the Wiz dashboard.  
`title` |  `string` Output only. The headline or name of the security finding.  
`greenAgentRemediationAnalysis` |  `object (`[GreenAgentRemediationAnalysis](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#GreenAgentRemediationAnalysis)`)` Output only. An AI-driven remediation plan detailing how to resolve the issue.  
`riskCategories[]` |  `string` Output only. The risk categories of the Wiz issue.  
  
## RelatedEntity

Represents the asset details for a WizRelatedIssue.

JSON representation  
---  
      
    
    {
      "entityName": string,
      "entityType": string
    }  
  
Fields  
---  
`entityName` |  `string` Output only. Name of the affected asset, IP, or endpoint.  
`entityType` |  `string` Output only. Type of the affected asset (e.g. HOSTNAME).  
  
## GreenAgentRemediationAnalysis

AI-driven remediation analysis for a Wiz security issue.

JSON representation  
---  
      
    
    {
      "title": string,
      "reasoning": string,
      "remediationSteps": [
        {
          object ([RemediationStep](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#RemediationStep))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Output only. A concise summary of the overall remediation strategy.  
`reasoning` |  `string` Output only. The justification for the remediation steps based on the vulnerability impact.  
`remediationSteps[]` |  `object (`[RemediationStep](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#RemediationStep)`)` Output only. An array of sequential steps required to fix the issue.  
  
## RemediationStep

A single step in the remediation process.

JSON representation  
---  
      
    
    {
      "title": string,
      "content": [
        {
          object ([StepContent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#StepContent))
        }
      ],
      "actions": [
        {
          object ([WizRemediationAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#WizRemediationAction))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Output only. The title of the specific remediation step.  
`content[]` |  `object (`[StepContent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#StepContent)`)` Output only. The instructional content for the step.  
`actions[]` |  `object (`[WizRemediationAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#WizRemediationAction)`)` Output only. Automated workflows or actions that can be triggered for this step.  
  
## StepContent

Instructional content for a remediation step.

JSON representation  
---  
      
    
    {
      "text": string,
      "markdownContent": string
    }  
  
Fields  
---  
`text` |  `string` Output only. Plaintext instructions (often null/empty if markdown is used).  
`markdownContent` |  `string` Output only. Rich text instructions, including code blocks, commands, and formatting.  
  
## WizRemediationAction

Automated response action or workflow that can be triggered for a step.

JSON representation  
---  
      
    
    {
      "type": enum ([WizRemediationActionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#WizRemediationActionType)),
      "label": string,
      "description": string,
      "id": string
    }  
  
Fields  
---  
`type` |  `enum (`[WizRemediationActionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases/fetchWizRelatedIssues#WizRemediationActionType)`)` Output only. The action type (e.g., RUN_RESPONSE_ACTION).  
`label` |  `string` Output only. A human-readable label for the action button in the UI.  
`description` |  `string` Output only. Further details about what the action does.  
`id` |  `string` Output only. The unique ID of the action or workflow to execute.  
  
## WizRemediationActionType

Core action type.

Enums  
---  
`WIZ_REMEDIATION_ACTION_TYPE_UNSPECIFIED` | Action type is unspecified.  
`RUN_RESPONSE_ACTION` | Runs a response action.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
