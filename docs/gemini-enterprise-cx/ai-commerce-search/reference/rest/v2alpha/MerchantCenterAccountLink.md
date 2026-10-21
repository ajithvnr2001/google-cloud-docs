---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink/
title: MerchantCenterAccountLink \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:55:39.532728+00:00
---

# MerchantCenterAccountLink  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  MerchantCenterAccountLink Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * MerchantCenterFeedFilter
    * JSON representation
  * State



Represents a link between a Merchant Center account and a branch. Once a link is established, products from the linked merchant center account will be streamed to the linked branch.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "merchantCenterAccountId": string,
      "branchId": string,
      "feedLabel": string,
      "languageCode": string,
      "feedFilters": [
        {
          object ([MerchantCenterFeedFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink#MerchantCenterFeedFilter))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink#State)),
      "projectId": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Immutable. Full resource name of the Merchant Center Account Link, such as `projects/*/locations/global/catalogs/default_catalog/merchantCenterAccountLinks/merchantCenterAccountLink`.  
`id` |  `string` Output only. Immutable. `[MerchantCenterAccountLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink)` identifier, which is the final component of `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink#FIELDS.name)`. This field is auto generated and follows the convention: `BranchId_MerchantCenterAccountId`. `projects/*/locations/global/catalogs/default_catalog/merchantCenterAccountLinks/id_1`.  
`merchantCenterAccountId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The linked [Merchant center account id](https://developers.google.com/shopping-content/guides/accountstatuses). The account must be a standalone account or a sub-account of a MCA.  
`branchId` |  `string` Required. The branch id (e.g. 0/1/2) within the catalog that products from merchantCenterAccountId are streamed to. When updating this field, an empty value will use the currently configured default branch. However, changing the default branch later on won't change the linked branch here.A single branch id can only have one linked merchant center account id.  
`feedLabel` |  `string` The FeedLabel used to perform filtering. Note: this replaces [region_id](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.feed_label).Example value: `US`. Example value: `FeedLabel1`.  
`languageCode` |  `string` Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). ISO 639-1.This specifies the language of offers in Merchant Center that will be accepted. If empty, no language filtering will be performed.Example value: `en`.  
`feedFilters[]` |  `object (`[MerchantCenterFeedFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink#MerchantCenterFeedFilter)`)` Criteria for the Merchant Center feeds to be ingested via the link. All offers will be ingested if the list is empty. Otherwise the offers will be ingested from selected feeds.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/MerchantCenterAccountLink#State)`)` Output only. Represents the state of the link.  
`projectId` |  `string` Output only. Google Cloud project ID.  
  
## MerchantCenterFeedFilter

Merchant Center Feed filter criterion.

JSON representation  
---  
      
    
    {
      "primaryFeedId": string,
      "primaryFeedName": string
    }  
  
Fields  
---  
`primaryFeedId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Merchant Center primary feed ID.  
`primaryFeedName` |  `string` Merchant Center primary feed name. The name is used for the display purposes only.  
  
## State

The state of the link.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`PENDING` | Link is created and LRO is not complete.  
`ACTIVE` | Link is active.  
`FAILED` | Link creation failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
