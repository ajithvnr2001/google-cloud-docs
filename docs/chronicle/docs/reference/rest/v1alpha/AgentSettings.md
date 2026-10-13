---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings/
title: AgentSettings \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:12.435349+00:00
---

# AgentSettings  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  AgentSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * QuotaInfo
    * JSON representation
  * AiSecurityTokenBillingSettings
    * JSON representation
  * BillingModel



This message represents the agent settings for an instance

JSON representation  
---  
      
    
    {
      "name": string,
      "autoInvestigationEnabled": boolean,
      "alertFilter": string,
      "autoInvestigationDelay": string,
      "quotaInfo": {
        object ([QuotaInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings#QuotaInfo))
      },
      "aiSecurityTokenBillingSettings": {
        object ([AiSecurityTokenBillingSettings](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings#AiSecurityTokenBillingSettings))
      },
      "enterpriseContext": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the AgentSettings. Format: projects/{project}/locations/{location}/instances/{instance}/agentSettings  
`autoInvestigationEnabled` |  `boolean` Optional. Whether auto investigation is enabled for the instance.  
`alertFilter` |  `string` Optional. A single AIP-160 string representing the instance provided alert filters used for auto investigation when default settings are disabled, e.g. “detection.rule_name = /enumeration/ AND detection.detection.rule_id != 1234 AND udm.metadata.event_type = /USER_LOGIN/”.  
`autoInvestigationDelay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The delay after which auto investigation will be triggered for an alert when default settings are disabled. This is only applied if `autoInvestigationEnabled` is true.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`quotaInfo` |  `object (`[QuotaInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings#QuotaInfo)`)` Output only. The quota information for the instance.  
`aiSecurityTokenBillingSettings  
**(deprecated)**` |  `object (`[AiSecurityTokenBillingSettings](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings#AiSecurityTokenBillingSettings)`)` This item is deprecated!Output only. Deprecated: Use GetAiBillingSettings and UpdateAiBillingSettings instead. Output only. Ignored if supplied in UpdateAgentSettings requests.  
`enterpriseContext` |  `string` Optional. Customer-provided context for investigations. Maximum allowed length: 4,000 characters.  
  
## QuotaInfo

Represents the information about an instance's quota status.

JSON representation  
---  
      
    
    {
      "autoInvestigationsQuotaLimit": string,
      "manualInvestigationsQuotaLimit": string
    }  
  
Fields  
---  
`autoInvestigationsQuotaLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The quota limit for auto investigations for the instance.  
`manualInvestigationsQuotaLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The quota limit for manual investigations for the instance.  
  
## AiSecurityTokenBillingSettings

This item is deprecated!

Deprecated: Use AiBillingSettings, GetAiBillingSettings, and UpdateAiBillingSettings instead. Billing and Token controls for AI features.

JSON representation  
---  
      
    
    {
      "paidTokenEnabled": boolean,
      "billingModel": enum ([BillingModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings#BillingModel)),
      "includedTokenCount": string,
      "updateTime": string,
      "totalPaidTokenAllocation": string,
      "usedIncludedTokens": string,
      "usedPaidTokens": string,
      "dailyPaidTokenLimit": string
    }  
  
Fields  
---  
`paidTokenEnabled` |  `boolean` Required. Bool representing whether customer has opted their tenant in to Paid Security Tokens. They will only be able to toggle this on if they have a valid BillingModel set.  
`billingModel` |  `enum (`[BillingModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentSettings#BillingModel)`)` Output only. The billing model describes how they're billed based on the SKU purchased by the customer.  
`includedTokenCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total daily baseline complimentary token budget included with the purchased package tier.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last mutation to these settings.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`totalPaidTokenAllocation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total reservoir of paid Security Tokens allocated to this tenant.  
`usedIncludedTokens` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Used tokens from the baseline complimentary budget today.  
`usedPaidTokens` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total paid tokens consumed from the allocation.  
`dailyPaidTokenLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Granular daily cap in paid Security Tokens.  
  
## BillingModel

The billing model describes how they're billed based on the SKU purchased by the customer.

Enums  
---  
`BILLING_MODEL_UNSPECIFIED` | Default unspecified billing model.  
`SUBSCRIPTION` | Subscription-based billing model.  
`PAYGO` | Pay-As-You-Go billing model.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
