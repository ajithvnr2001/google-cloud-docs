---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers
title: REST Resource: organizations.locations.customers \u00a0|\u00a0 Sovereign Controls by Partners guides for partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:59.350138+00:00
---

# REST Resource: organizations.locations.customers  |  Sovereign Controls by Partners guides for partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners)
  * [ Sovereign Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/guides)
  * [ Reference ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest)



Send feedback 

#  REST Resource: organizations.locations.customers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Customer
    * JSON representation
  * CustomerOnboardingState
    * JSON representation
  * CustomerOnboardingStep
    * JSON representation
  * Step
  * Methods



## Resource: Customer

Contains metadata around a Cloud Controls Partner Customer

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "customerOnboardingState": {
        object ([CustomerOnboardingState](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers#CustomerOnboardingState))
      },
      "isOnboarded": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Format: organizations/{organization}/locations/{location}/customers/{customer}  
`displayName` |  `string` The customer organization's display name. E.g. "google.com".  
`customerOnboardingState` |  `object (`[CustomerOnboardingState](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers#CustomerOnboardingState)`)` Container for customer onboarding steps  
`isOnboarded` |  `boolean` Indicates whether a customer is fully onboarded  
  
## CustomerOnboardingState

Container for customer onboarding steps

JSON representation  
---  
      
    
    {
      "onboardingSteps": [
        {
          object ([CustomerOnboardingStep](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers#CustomerOnboardingStep))
        }
      ]
    }  
  
Fields  
---  
`onboardingSteps[]` |  `object (`[CustomerOnboardingStep](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers#CustomerOnboardingStep)`)` List of customer onboarding steps  
  
## CustomerOnboardingStep

Container for customer onboarding information

JSON representation  
---  
      
    
    {
      "step": enum ([Step](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers#Step)),
      "startTime": string,
      "completionTime": string,
      "completionState": enum ([CompletionState](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/CompletionState))
    }  
  
Fields  
---  
`step` |  `enum (`[Step](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers#Step)`)` The onboarding step  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The starting time of the onboarding stepA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`completionTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The completion time of the onboarding stepA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`completionState` |  `enum (`[CompletionState](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/CompletionState)`)` Output only. Current state of the step  
  
## Step

Enum for possible onboarding steps

Enums  
---  
`STEP_UNSPECIFIED` | Unspecified step  
`KAJ_ENROLLMENT` | KAJ Enrollment  
`CUSTOMER_ENVIRONMENT` | Customer Environment  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers/get)`

|  Gets details of a single customer  
  
### `[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers/list)`

|  Lists customers of a partner identified by its Google Cloud organization ID  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
