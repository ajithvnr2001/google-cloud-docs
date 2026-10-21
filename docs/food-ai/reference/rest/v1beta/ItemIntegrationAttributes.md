---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes/
title: ItemIntegrationAttributes \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:03:25.722845+00:00
---

# ItemIntegrationAttributes  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  ItemIntegrationAttributes Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * StreamIntegrationAttributes
    * JSON representation
  * Tax
    * JSON representation
  * ToastIntegrationAttributes
    * JSON representation



Metadata associated with an item used for downstream integrations.

JSON representation  
---  
      
    
    {
      "customIntegrationAttributes": {
        object
      },
      "streamAttributes": {
        object ([StreamIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes#StreamIntegrationAttributes))
      },
      "toastAttributes": {
        object ([ToastIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes#ToastIntegrationAttributes))
      }
    }  
  
Fields  
---  
`customIntegrationAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`streamAttributes` |  `object (`[StreamIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes#StreamIntegrationAttributes)`)` Optional. Represents metadata associated with this item used for Stream integration. If Stream integration isn't enabled for the store, this field is ignored.  
`toastAttributes` |  `object (`[ToastIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes#ToastIntegrationAttributes)`)` Optional. Represents metadata associated with this item used for Toast integration. If Toast integration isn't enabled for the store, this field is ignored.  
  
## StreamIntegrationAttributes

Represents attributes for an Item from a Stream menu.

JSON representation  
---  
      
    
    {
      "taxes": [
        {
          object ([Tax](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes#Tax))
        }
      ],
      "itemFamilyId": string
    }  
  
Fields  
---  
`taxes[]` |  `object (`[Tax](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes#Tax)`)` Optional. Represents tax rates which apply to this item.  
`itemFamilyId` |  `string` Optional. Represents the item family that contains this item variant in Stream's menu.  
  
## Tax

Tax rate information associated with this item.

JSON representation  
---  
      
    
    {
      "streamId": string,
      "isInclusive": boolean,
      "rate": number,
      "displayName": string,
      "isDefault": boolean
    }  
  
Fields  
---  
`streamId` |  `string` Required. The ID of the tax in the Stream menu.  
`isInclusive` |  `boolean` Optional. Determines if the tax amount is already included in the item price  
`rate` |  `number` Required. The rate of the tax as a percentage.  
`displayName` |  `string` Optional. The name of the tax.  
`isDefault` |  `boolean` Optional. Whether the tax is the default tax.  
  
## ToastIntegrationAttributes

Represents attributes for an Item from a Toast menu.

JSON representation  
---  
      
    
    {
      "menuGroupGuid": string
    }  
  
Fields  
---  
`menuGroupGuid` |  `string` Optional. Represents the menu group guid of the item in Toast's menu.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
