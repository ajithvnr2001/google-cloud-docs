---
url: https://docs.cloud.google.com/channel/docs/guides/manage-entitlements/
title: Manage Google Workspace and Google Chrome entitlements \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:34.300189+00:00
---

# Manage Google Workspace and Google Chrome entitlements  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/guides/manage-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Manage Google Workspace and Google Chrome entitlements Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage customer entitlements for Google Workspace and Google Chrome products.

## Pre-requisite

Before you continue, determine whether your reseller account has a single Google Workspace billing account or multiple Google Workspace billing accounts. To learn more about this topic, read [Multiple Google Workspace Billing Account Starter Guide](https://docs.cloud.google.com/channel/docs/guides/multiple-billing-account-starter) .

## Create entitlement

### Before you begin

You need a [`Customer`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers#Customer) setup before you can proceed.

To create entitlement, follow these steps:

  1. With the Customer name, call [`listPurchasableSkus`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/listPurchasableSkus) to retrieve a list of [`PurchasableSkus`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/listPurchasableSkus#purchasablesku)
         
         ListPurchasableSkusRequest
         {
           "customer": "accounts/123/customers/abc",
           "createEntitlementPurchase": {
             "product": "products/-"
           }
         }
         ListPurchasableSkusResponse
         {
           "purchasableSkus": [
             {
               "sku": {
                 "name": "products/product_id/skus/sku_id1",
                 "product": {
                   "name": "products/product_id",
                 }
               }
             },
             {
               "sku": {
                 "name": "products/product_id/skus/sku_id2",
                 "product": {
                   "name": "products/product_id",
                 },
               }
             }
           ]
         }
         

  2. With the selected PurchasableSku, use the [`queryEligibleBillingAccounts`](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers/queryEligibleBillingAccounts) method to find a set of Google Workspace [`BillingAccount`](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers/queryEligibleBillingAccounts#BillingAccount) that can be used to pay for the entitlement.

     1. If you want to pay in a specific currency, select a BillingAccount with that currency.
    
    QueryEligibleBillingAccountsRequest
    {
      "customer": "accounts/123/customers/abc",
      "skus": ["products/product_id/skus/sku_id1"]
    }
    QueryEligibleBillingAccountsResponse
    {
      "skuPurchaseGroups": [
        {
          "skus": [
            "products/product_id/skus/sku_id1"
          ],
          "billingAccountPurchaseInfos": [
            {
              "billingAccount": {
                "name": "accounts/123/billingAccounts/billing_account_id1",
                "displayName": "Google_Workspace_USD_US_1",
                "currencyCode": "USD",
                "regionCode": "US"
              }
            },
            {
              "billingAccount": {
                "name": "accounts/123/billingAccounts/billing_account_id2",
                "displayName": "Google_Workspace_CAD_CA_1",
                "currencyCode": "CAD",
                "regionCode": "CA"
              }
            }
          ]
        }
      ]
    }
    

  3. With the selected PurchasableSku and BillingAccount, use the [`listPurchasableOffers`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/listPurchasableOffers) method to find the available [`PurchasableOffer`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/listPurchasableOffers#purchasableoffer)
         
         ListPurchasableOffersRequest
         {
           "customer": "accounts/123/customers/abc",
           "createEntitlementPurchase": {
             "sku": "products/product_id/skus/sku_id1",
             "billingAccount": "accounts/123/billingAccounts/billing_account_id2"
           }
         }
         ListPurchasableOffersResponse
         {
           "purchasableOffers": [
             {
               "offer": {
                 "name": "accounts/123/offers/offer_id1",
               },
               "sku": {
                 "name": "products/product_id/skus/sku_id1",
               },
               "plan": {
                 "paymentPlan": "FLEXIBLE",
                 "paymentCycle": {
                   "duration": 1,
                   "periodType": "MONTH"
                 }
               },
               "priceReferenceId": "price_reference_id_123"
             }
           ],
         }
         

  4. At this point you should have the BillingAccount that will pay for the [`Entitlement`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements#Entitlement) and the PurchasableOffer. Begin to create the entitlement by using the [`create`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create) method.

     1. Create an Entitlement and populate the offer, billingAccount and any other required parameters. Populate the price reference ID in the entitlement when it's present in the PurchasableOffer to ensure that the new entitlement has the above-quoted price. Without this price reference ID, there is no guarantee that the discount and effective price returned from the ListPurchasableOffersResponse will be the same in this CreateEntitlement call. Populating this price reference ID ensures a pricing match in this new entitlement.
    
    CreateEntitlementRequest
    {
      "parent": "accounts/123/customers/abc",
      "entitlement": {
        "offer": "accounts/123/offers/offer_id1",
        "maxUnits": 100,
        "billingAccount": "accounts/123/billingAccounts/billing_account_id2",
        "priceReferenceId": "price_reference_id_123"
      }
    }
    CreateEntitlementResponse
    {
      "name": "operations/operation_id1"
    }
    




## Change payment plan on Google Workspace entitlements

### Before you begin

Google Workspace entitlements with a Free or Trial payment [`plan`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/Offer#Plan) do not have a Google Workspace billing account. In order to change the payment plan for an Entitlement to a paid payment plan, there are a couple of additional steps to select a Google Workspace billing account.

To change payment plan on Google Workspace entitlements, follow these steps:

The first two steps are only required if the existing Entitlement has a Free or Trial payment plan.

  1. With the Offer, use the [`lookupOffer`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/lookupOffer) method to find [`Sku`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/Sku) information on the Offer.
         
         LookupOfferRequest
         {
           "entitlement": "accounts/123/customers/abc/entitlements/entitlement_id1"
         }
         LookupOffer respones
         {
           "name": "accounts/123/offers/offer_id1",
           "sku": {
             "name": "products/product_id/skus/sku_id1",
            }
         }
         

  2. With the Customer and Sku, use the queryEligibleBillingAccounts method to find a set of BillingAccount that can be used to pay for this Entitlement. If you want to pay in a specific currency, select a BillingAccount with that currency.
         
         QueryEligibleBillingAccountsRequest
          {
            "customer": "accounts/123/customers/abc",
            "skus": ["products/product_id/skus/sku_id1"]
          }
          QueryEligibleBillingAccountsResponse
          {
            "skuPurchaseGroups": [
              {
                "skus": [
                  "products/product_id/skus/sku_id1"
                ],
                "billingAccountPurchaseInfos": [
                  {
                    "billingAccount": {
                      "name": "accounts/123/billingAccounts/billing_account_id1",
                      "displayName": "Google_Workspace_USD_US_1",
                      "currencyCode": "USD",
                      "regionCode": "US"
                    }
                  },
                  {
                    "billingAccount": {
                      "name": "accounts/123/billingAccounts/billing_account_id2",
                      "displayName": "Google_Workspace_CAD_CA_1",
                      "currencyCode": "CAD",
                      "regionCode": "CA"
                    }
                  }
                ]
              }
            ]
          }
          ```
         

  3. With the Entitlement and BillingAccount, use the `listPurchasableOffers` method to find any PurchasableOffer. The BillingAccount is not needed if the existing entitlement already has a paid plan, in this case, the existing BillingAccount will be used. To change the payment plan, the purchase_option field needs to be [`changeOfferPurchase`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/listPurchasableOffers#ChangeOfferPurchase)
         
         ListPurchasableOffersRequest
         {
           "customer": "accounts/123/customers/abc",
           "changeOfferPurchase": {
             "entitlement": "accounts/123/customers/abc/entitlements/entitlement_id1",
             "billingAccount": "accounts/123/billingAccounts/billing_account_id2"
           }
         }
         ListPurchasableOffersResponse
         {
           "purchasableOffers": [
             {
               "offer": {
                 "name": "accounts/123/offers/offer_id1",
               },
               "sku": {
                 "name": "products/product_id/skus/sku_id1",
               },
               "plan": {
                 "paymentPlan": "FLEXIBLE",
                 "paymentCycle": {
                   "duration": 1,
                   "periodType": "MONTH"
                 }
               },
               "priceReferenceId": "price_reference_id_123"
             }
           ],
         }
         

  4. At this point you should have the Entitlement, Offer and the BillingAccount. Begin to change the payment plan by using the [`changeOffer`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/changeOffer) method. Populate the price reference ID in the entitlement when it's present in the PurchasableOffer to ensure that the new entitlement has the above-quoted price. Without this price reference ID, there is no guarantee that the discount and effective price returned from the ListPurchasableOffersResponse will be the same in this ChangeOffer call. Populating this price reference ID ensures a pricing match in this new entitlement.
         
         ChangeOfferRequest
         {
           "name": "accounts/abc/customers/123/entitlements/entitlement_id1",
           "offer": "accounts/abc/offers/offer_id1",
           "billing_account": "accounts/abc/billingAccounts/billing_account_id2",
           "parameters": [{
             "name": "max_units",
             "value": {
               "int64Value": "100"
             }
           }],
           "priceReferenceId": "price_reference_id_123"
         }
         ChangeOfferResponse
         {
           "name": "operations/operation_id1"
         }
         




## Upgrade or downgrade Google Workspace entitlements

To upgrade or downgrade Google Workspace entitlements, follow these steps:

  1. With the Entitlement, call the `listPurchasableSkus` method to retrieve a list of PurchasableSkus that can be used for upgrade or downgrade.
         
         ListPurchasableSkusRequest
         {
           "customer": "accounts/123/customers/abc",
           "changeOfferPurchase": {
             "entitlement": "accounts/123/customers/abc/entitlements/entitlement_id1",
             "changeType": "UPGRADE"
           }
         }
         ListPurchasableSkusResponse
         {
           "purchasableSkus": [
             {
               "sku": {
                 "name": "products/product_id/skus/sku_id1",
                 "product": {
                   "name": "products/product_id",
                 }
               }
             },
             {
               "sku": {
                 "name": "products/product_id/skus/sku_id2",
                 "product": {
                   "name": "products/product_id",
                 },
               }
             }
           ]
         }
         

  2. With the PurchasableSku, use the `queryEligibleBillingAccounts` method to find a set of BillingAccounts that can be used to pay for the Entitlement.

     1. If you want to pay in a specific currency, select a BillingAccount with that currency.
    
    QueryEligibleBillingAccountsRequest
     {
       "customer": "accounts/123/customers/abc",
       "skus": ["products/product_id/skus/sku_id1"]
     }
     QueryEligibleBillingAccountsResponse
     {
       "skuPurchaseGroups": [
         {
           "skus": [
             "products/product_id/skus/sku_id1"
           ],
           "billingAccountPurchaseInfos": [
             {
               "billingAccount": {
                 "name": "accounts/123/billingAccounts/billing_account_id1",
                 "displayName": "Google_Workspace_USD_US_1",
                 "currencyCode": "USD",
                 "regionCode": "US"
               }
             },
             {
               "billingAccount": {
                 "name": "accounts/123/billingAccounts/billing_account_id2",
                 "displayName": "Google_Workspace_CAD_CA_1",
                 "currencyCode": "CAD",
                 "regionCode": "CA"
               }
             }
           ]
         }
       ]
     }
     ```
    

  3. With the Entitlement and BillingAccount, use the `listPurchasableOffers` method to find any PurchasableOffer.
         
         ListPurchasableOffersRequest
           {
             "customer": "accounts/123/customers/abc",
             "changeOfferPurchase": {
               "entitlement": "accounts/123/customers/abc/entitlements/entitlement_id1",
               "billingAccount": "accounts/123/billingAccounts/billing_account_id2"
             }
           }
           ListPurchasableOffersResponse
           {
             "purchasableOffers": [
               {
                 "offer": {
                   "name": "accounts/123/offers/offer_id1",
                 },
                 "sku": {
                   "name": "products/product_id/skus/sku_id1",
                 },
                 "plan": {
                   "paymentPlan": "FLEXIBLE",
                   "paymentCycle": {
                     "duration": 1,
                     "periodType": "MONTH"
                   }
                 },
                 "priceReferenceId": "price_reference_id_123"
               }
             ],
           }
           ```
         

  4. At this point you should have the Entitlement, PurchasableOffer and the BillingAccount. Begin to upgrade or downgrade by using the `changeOffer` method.

     1. Create an Entitlement object and populate the name, offer, billingAccount and any required parameters. Populate the price reference ID in the entitlement when it's present in the PurchasableOffer to ensure that the new entitlement has the above-quoted price. Without this price reference ID, there is no guarantee that the discount and effective price returned from the ListPurchasableOffersResponse will be the same in this ChangeOffer call. Populating this price reference ID ensures a pricing match in this new entitlement.
    
    ChangeOfferRequest
       {
         "name": "accounts/abc/customers/123/entitlements/entitlement_id1",
         "offer": "accounts/abc/offers/offer_id1",
         "billing_account": "accounts/abc/billingAccounts/billing_account_id2",
         "parameters": [{
           "name": "max_units",
           "value": {
             "int64Value": "100"
           }
         }],
         "priceReferenceId": "price_reference_id_123"
       }
       ChangeOfferResponse
       {
         "name": "operations/operation_id1"
       }
       ```
    




## Transfer entitlements

This section helps you transfer entitlements for existing Google Workspace and Chrome customers from their previous partner.

For help transferring customers in the Partner Sales Console, see our guides on transferring customers to a [partner account](https://support.google.com/channelservices/answer/9547629) or a [Google account](https://support.google.com/channelservices/answer/9818236)

Google Workspace customers can only purchase entitlements from a single partner or a single partner and Google.

During the transfer, existing entitlements are automatically canceled before they are created again under the new partner. If a customer has commitment plan entitlements, those will start a new commitment term after the transfer.

### Before you begin

To manage entitlements for a customer, you need a customer-generated [transfer token](http://admin.google.com/TransferToken). Contact the customer and provide your [Partner Public Identifier](https://support.google.com/channelservices/answer/9547629#zippy=%2Cfind-your-reseller-public-identifier-account-id) so they can generate a transfer token. After they create a token, the customer needs to send their transfer token back to you to complete the process. These tokens expire 14 days after creation. You also need the customer's domain or Cloud Identity ID.

When the customer creates their transfer token, they select the entitlements they want to transfer to their new reseller. You need to transfer all the selected entitlements during the process.

To transfer entitlements, follow these steps:

If you only have the customer's domain, you can use the Cloud Channel API to return their Cloud Identity ID. Call [`checkCloudIdentityAccountsExist`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/checkCloudIdentityAccountsExist) with the customer's domain and, if the domain exists, the API will return the customer's Cloud Identity ID.

  1. Begin the transfer by using the [`customers.import`](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers/import) method to import the customer's data.
         
         ImportCustomerRequest
         {
           "parent": "accounts/abc",
           "domain": "domain"
         }
         

  2. With the customer's Cloud Identity ID, call [`listTransferableSkus`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableSkus) to retrieve a list of the customer's [`transferableSku`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableSkus#TransferableSku) Check each object's [`transferEligibility`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableSkus#TransferEligibility) to make sure you can purchase the associated SKU.
         
         ListTransferableSkusRequest
         {
           "parent": "accounts/abc",
           "cloudIdentityId": "cloud_identity_id"
         }
         ListTransferableSkusResponse
         {
           "transferableSku": [
             {
               "sku": {
                    "name": "products/product_id/skus/voice_sku_id1",
               },
             },
             {
               "sku": {
                    "name": "products/product_id/skus/google_workspace_sku_id2",
               },
             },
             {
               "sku": {
                    "name": "products/product_id/skus/google_workspace_chrome_sku_id3",
               },
             }
           ],
         }
         

  3. Now that you have a list of TransferableSkus, you need to determine what BillingAccount to use to pay for the entitlements. Use the `queryEligibleBillingAccounts` method to find a set of BillingAccount that can be used for each TransferableSku.

     1. Note that certain TransferableSkus must share the same Google Workspace billing account, which is why `queryEligibleBillingAccounts` returns a sku group that informs you which TransferableSkus need to use the same BillingAccount. If there are multiple Google Workspace billing account for a given SKU group, you can pick one of the Google Workspace billing account and use it for every TransferableSku in the group.
    
    QueryEligibleBillingAccountsRequest
    {
      "customer": "accounts/123/customers/abc",
      "skus": ["products/product_id/skus/voice_sku_id1","products/product_id/skus/google_workspace_sku_id2","google_workspace_chrome_sku_id3"]
    }
    QueryEligibleBillingAccountsResponse
     {
       "skuPurchaseGroups": [
         {
           "skus": [
             "products/product_id/skus/voice_sku_id1"
           ],
           "billingAccountPurchaseInfos": [
             {
               "billingAccount": {
                 "name": "accounts/123/billingAccounts/voice_billing_account_id1",
                 "displayName": "Google_Workspace_Voice_USD_US_1",
                 "currencyCode": "USD",
                 "regionCode": "US"
               }
             }
           ]
         },
         {
           "skus": [
             "products/product_id/skus/google_workspace_sku_id2","google_workspace_chrome_sku_id3"
           ],
           "billingAccountPurchaseInfos": [
             {
               "billingAccount": {
                 "name": "accounts/123/billingAccounts/gw_billing_account_id1",
                 "displayName": "Google_Workspace_USD_US_1",
                 "currencyCode": "USD",
                 "regionCode": "US"
               }
             },
             {
               "billingAccount": {
                 "name": "accounts/123/billingAccounts/gw_billing_account_id2",
                 "displayName": "Google_Workspace_CAD_CA_1",
                 "currencyCode": "CAD",
                 "regionCode": "CA"
               }
             }
           ]
         }
       ]
     }
     ```
    

  4. For each TransferableSku and BillingAccount pairs, use the [`listTransferableOffers`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableOffers) method to find available [`TransferableOffers`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableOffers#TransferableOffer) . At this point you should have the customer's list of tuples consisting of TransferableSku, BillingAccounts, and TransferableOffer.
         
         ListTransferableOffersRequest
         {
           "parent": "accounts/abc",
           "cloudIdentityId": "cloud_identity_id",
           "sku": "products/product_id/skus/voice_sku_id1",
           "billingAccount": "ccounts/123/billingAccounts/voice_billing_account_id1"
         }
         ListTransferableOffersResponse
            {
              "transferableOffers": [
                {
                  "offer": {
                    "name": "accounts/123/offers/voice_offer_id1",
                  },
                  "sku": {
                    "name": "products/product_id/skus/voice_sku_id1",
                  },
                  "plan": {
                    "paymentPlan": "FLEXIBLE",
                    "paymentCycle": {
                      "duration": 1,
                      "periodType": "MONTH"
                    }
                  },
                  "priceReferenceId": "price_reference_id_voice_offer_12"
                }
              ],
            }
         

  5. For each tuple create a new corresponding Entitlement object, each Entitlement needs an Offer, BillingAccount and any required parameters. Populate the price reference ID in the entitlement when it's present in the PurchasableOffer to ensure that the new entitlement has the above-quoted price. Without this price reference ID, there is no guarantee that the discount and effective price returned from the ListPurchasableOffersResponse will be the same in this TransferEntitlements call. Populating this price reference ID ensures a pricing match in this new entitlement. To perform the transfer, call the [`transferEntitlements`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/transferEntitlements) method.
         
         TransferEntitlementsRequest
         {
           "parent": "accounts/abc/customers/123",
           "entitlements": [
             { 
               "offer": "accounts/123/offers/voice_offer_id1",
               "maxUnits": 100,
               "billingAccount": "accounts/123/billingAccounts/voice_billing_account_id1",
               "priceReferenceId": "price_reference_id_voice_offer_12"
             },
             {
               "offer": "accounts/123/offers/gw_offer_id2",
               "maxUnits": 150,
               "billingAccount": "accounts/123/billingAccounts/gw_billing_account_id1"
             }
             {
               "offer": "accounts/123/offers/gw_chrome_offer_id3",
               "maxUnits": 200,
               "billingAccount": "accounts/123/billingAccounts/gw_billing_account_id1",
               "priceReferenceId": "price_reference_id_chrome_offer_34"
             }   
           ]
         }
         TransferEntitlementsResponse
         {
           "name": "operations/operation_id1"
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
