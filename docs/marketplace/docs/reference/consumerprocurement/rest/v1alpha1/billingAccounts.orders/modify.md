---
url: https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/modify/
title: Method: billingAccounts.orders.modify \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:02.875610+00:00
---

# Method: billingAccounts.orders.modify  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/modify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Reference ](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest)



Send feedback 

#  Method: billingAccounts.orders.modify Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Modification
    * JSON representation
  * AutoRenewalBehavior
  * Try it!



Modifies an existing `[Order](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#Order)` resource.

### HTTP request

`POST https://cloudcommerceconsumerprocurement.googleapis.com/v1alpha1/{name=billingAccounts/*/orders/*}:modify`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the order to update.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "modifications": [
        {
          object ([Modification](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/modify#Modification))
        }
      ],
      "displayName": string,
      "etag": string
    }  
  
Fields  
---  
`modifications[]` |  `object (`[Modification](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/modify#Modification)`)` Optional. Modifications for an existing Order created by an Offer. Required when Offer based Order is being modified, except for when going from an offer to a public plan.  
`displayName` |  `string` Optional. Updated display name of the order, leave as empty if you do not want to update current display name.  
`etag` |  `string` Optional. The weak etag, which can be optionally populated, of the order that this modify request is based on. Validation checking will only happen if the invoker supplies this field.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `consumerprocurement.orders.modify`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Modification

Modifications to make on the order.

JSON representation  
---  
      
    
    {
      "lineItemId": string,
      "changeType": enum ([LineItemChangeType](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#LineItemChangeType)),
      "newLineItemInfo": {
        object ([LineItemInfo](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#LineItemInfo))
      },
      "autoRenewalBehavior": enum ([AutoRenewalBehavior](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/modify#AutoRenewalBehavior))
    }  
  
Fields  
---  
`lineItemId` |  `string` Required. ID of the existing line item to make change to. Required when change type is [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_UPDATE] or [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_CANCEL].  
`changeType` |  `enum (`[LineItemChangeType](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#LineItemChangeType)`)` Required. Type of change to make.  
`newLineItemInfo` |  `object (`[LineItemInfo](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#LineItemInfo)`)` Optional. The line item to update to. Required when changeType is [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_CREATE] or [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_UPDATE].  
`autoRenewalBehavior` |  `enum (`[AutoRenewalBehavior](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/modify#AutoRenewalBehavior)`)` Optional. Auto renewal behavior of the subscription for the update. Applied when changeType is [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_UPDATE]. Follows plan default config when this field is not specified.  
  
## AutoRenewalBehavior

Indicates the auto renewal behavior customer specifies on subscription.

Enums  
---  
`AUTO_RENEWAL_BEHAVIOR_UNSPECIFIED` | If unspecified, the auto renewal behavior will follow the default config.  
`AUTO_RENEWAL_BEHAVIOR_ENABLE` | Auto Renewal will be enabled on subscription.  
`AUTO_RENEWAL_BEHAVIOR_DISABLE` | Auto Renewal will be disabled on subscription.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
