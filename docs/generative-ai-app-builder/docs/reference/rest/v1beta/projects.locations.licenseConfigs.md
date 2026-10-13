---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs
title: REST Resource: projects.locations.licenseConfigs \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:52.000995+00:00
---

# REST Resource: projects.locations.licenseConfigs  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.licenseConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LicenseConfig
    * JSON representation
  * State
  * SubscriptionTerm
  * Methods



## Resource: LicenseConfig

Information about users' licenses.

JSON representation  
---  
      
    
    {
      "name": string,
      "licenseCount": string,
      "subscriptionTier": enum ([SubscriptionTier](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SubscriptionTier)),
      "state": enum ([State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#State)),
      "autoRenew": boolean,
      "startDate": {
        object ([Date](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/Date))
      },
      "subscriptionTerm": enum ([SubscriptionTerm](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#SubscriptionTerm)),
      "freeTrial": boolean,
      "geminiBundle": boolean,
      "earlyTerminated": boolean,
      "earlyTerminationDate": {
        object ([Date](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/Date))
      },
      "lastUserUpdateTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The fully qualified resource name of the license config. Format: `projects/{project}/locations/{location}/licenseConfigs/{licenseConfig}`  
`licenseCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Number of licenses purchased.  
`subscriptionTier` |  `enum (`[SubscriptionTier](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SubscriptionTier)`)` Required. Subscription tier information for the license config.  
`state` |  `enum (`[State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#State)`)` Output only. The state of the license config.  
`autoRenew` |  `boolean` Optional. Whether the license config should be auto renewed when it reaches the end date.  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/Date)`)` Required. The start date.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/Date)`)` Optional. The planed end date.  
`subscriptionTerm` |  `enum (`[SubscriptionTerm](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#SubscriptionTerm)`)` Required. Subscription term.  
`freeTrial` |  `boolean` Optional. Whether the license config is for free trial.  
`geminiBundle` |  `boolean` Output only. Whether the license config is for Gemini bundle.  
`earlyTerminated` |  `boolean` Output only. Indication of whether the subscription is terminated earlier than the expiration date. This is usually terminated by pipeline once the subscription gets terminated from subsv3.  
`earlyTerminationDate` |  `object (`[Date](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/Date)`)` Output only. The date when the subscription is terminated earlier than the expiration date.  
`lastUserUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. timestamp of the most recent user-initiated update (seat count change or subscription term change). Unlike `updateTime`, this field is only stamped when a customer explicitly updates the license (e.g. via the UI), and is not touched by system-driven writes (subscription pipeline, BALC propagation, etc.).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

License config state enumeration.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. The license config does not exist.  
`ACTIVE` | The license config is effective and being used.  
`EXPIRED` | The license config has expired.  
`NOT_STARTED` | The license config has not started yet, and its start date is in the future.  
`WITHDRAWN` | This is when a sub license config has returned all its seats back to BillingAccountLicenseConfig that it belongs to. Similar to EXPIRED.  
`DEACTIVATING` | The license config is in a grace period. Its subscription has ended, either through early termination or by reaching its end date, but the customer keeps access for a limited time. It becomes EXPIRED when the grace period ends.  
  
## SubscriptionTerm

Subscription term.

Enums  
---  
`SUBSCRIPTION_TERM_UNSPECIFIED` | Default value, do not use.  
`SUBSCRIPTION_TERM_ONE_MONTH` | 1 month.  
`SUBSCRIPTION_TERM_ONE_YEAR` | 1 year.  
`SUBSCRIPTION_TERM_THREE_YEARS` | 3 years.  
`SUBSCRIPTION_TERM_CUSTOM` | Custom term. Must set the endDate.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs/create)`

|  Creates a `[LicenseConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#LicenseConfig)` This method should only be used for creating NotebookLm licenses or Gemini Enterprise free trial licenses.  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs/get)`

|  Gets a `[LicenseConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#LicenseConfig)`.  
  
### `[list](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs/list)`

|  Lists all the `[LicenseConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#LicenseConfig)`s associated with the project.  
  
### `[patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs/patch)`

|  Updates the `[LicenseConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.licenseConfigs#LicenseConfig)`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
