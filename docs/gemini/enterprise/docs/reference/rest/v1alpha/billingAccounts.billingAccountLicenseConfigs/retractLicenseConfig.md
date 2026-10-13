---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/billingAccounts.billingAccountLicenseConfigs/retractLicenseConfig/
title: Method: billingAccounts.billingAccountLicenseConfigs.retractLicenseConfig \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:20.149643+00:00
---

# Method: billingAccounts.billingAccountLicenseConfigs.retractLicenseConfig  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/billingAccounts.billingAccountLicenseConfigs/retractLicenseConfig/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: billingAccounts.billingAccountLicenseConfigs.retractLicenseConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



This method is called from the billing account side to retract the `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)` from the given project back to the billing account.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{billingAccountLicenseConfig=billingAccounts/*/billingAccountLicenseConfigs/*}:retractLicenseConfig`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`billingAccountLicenseConfig` |  `string` Required. Full resource name of `[BillingAccountLicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/billingAccounts.billingAccountLicenseConfigs#BillingAccountLicenseConfig)`.Format: `billingAccounts/{billingAccount}/billingAccountLicenseConfigs/{billingAccountLicenseConfigId}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "licenseConfig": string,
      "fullRetract": boolean,
      "licenseCount": string
    }  
  
Fields  
---  
`licenseConfig` |  `string` Required. Full resource name of `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)`.Format: `projects/{project}/locations/{location}/licenseConfigs/{licenseConfigId}`.  
`fullRetract` |  `boolean` Optional. If set to true, retract the entire license config. Otherwise, retract the specified license count.  
`licenseCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of licenses to retract. Only used when fullRetract is false.  
  
### Response body

Response message for `[LicenseConfigService.RetractLicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/billingAccounts.billingAccountLicenseConfigs/retractLicenseConfig#google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "licenseConfig": {
        object ([LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig))
      }
    }  
  
Fields  
---  
`licenseConfig` |  `object (`[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)`)` The updated LicenseConfig.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `billingAccountLicenseConfig` resource:

  * `discoveryengine.billingAccountLicenseConfigs.retract`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
