---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans
title: REST Resource: organizations.apiproducts.rateplans \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:20.254772+00:00
---

# REST Resource: organizations.apiproducts.rateplans  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.apiproducts.rateplans Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RatePlan
    * JSON representation
  * BillingPeriod
  * PaymentFundingModel
  * Money
    * JSON representation
  * ConsumptionPricingType
  * RateRange
    * JSON representation
  * RevenueShareType
  * RevenueShareRange
    * JSON representation
  * State
  * Methods



## Resource: RatePlan

Rate plan details.

JSON representation  
---  
      
    
    {
      "name": string,
      "apiproduct": string,
      "displayName": string,
      "description": string,
      "billingPeriod": enum ([BillingPeriod](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#BillingPeriod)),
      "paymentFundingModel": enum ([PaymentFundingModel](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#PaymentFundingModel)),
      "currencyCode": string,
      "setupFee": {
        object ([Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money))
      },
      "fixedRecurringFee": {
        object ([Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money))
      },
      "fixedFeeFrequency": integer,
      "consumptionPricingType": enum ([ConsumptionPricingType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#ConsumptionPricingType)),
      "consumptionPricingRates": [
        {
          object ([RateRange](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RateRange))
        }
      ],
      "revenueShareType": enum ([RevenueShareType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RevenueShareType)),
      "revenueShareRates": [
        {
          object ([RevenueShareRange](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RevenueShareRange))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#State)),
      "startTime": string,
      "endTime": string,
      "createdAt": string,
      "lastModifiedAt": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the rate plan.  
`apiproduct` |  `string` Name of the API product that the rate plan is associated with.  
`displayName` |  `string` Display name of the rate plan.  
`description` |  `string` Description of the rate plan.  
`billingPeriod` |  `enum (`[BillingPeriod](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#BillingPeriod)`)` Frequency at which the customer will be billed.  
`paymentFundingModel  
**(deprecated)**` |  `enum (`[PaymentFundingModel](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#PaymentFundingModel)`)` This item is deprecated!DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the `billingType` field inside `DeveloperMonetizationConfig` resource.Flag that specifies the billing account type, prepaid or postpaid.  
`currencyCode` |  `string` Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.  
`setupFee` |  `object (`[Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money)`)` Initial, one-time fee paid when purchasing the API product.  
`fixedRecurringFee` |  `object (`[Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money)`)` Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.  
`fixedFeeFrequency` |  `integer` Frequency at which the fixed fee is charged.  
`consumptionPricingType` |  `enum (`[ConsumptionPricingType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#ConsumptionPricingType)`)` Pricing model used for consumption-based charges.  
`consumptionPricingRates[]` |  `object (`[RateRange](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RateRange)`)` API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `BANDED` and the ranges are defined as follows:
    
    
      {
        "start": 1,
        "end": 100,
        "fee": 2
      },
      {
        "start": 101,
        "end": 200,
        "fee": 1.50
      },
      {
        "start": 201,
        "end": 0,
        "fee": 1
      },
    }
    

Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`):

  * 50 calls cost 50 x $2 = $100
  * 150 calls cost 100 x $2 + 50 x $1.5 = $275
  * 250 calls cost 100 x $2 + 100 x $1.5 + 50 x $1 = $400
  * 500 calls cost 100 x $2 + 100 x $1.5 + 300 x $1 = $650

  
`revenueShareType` |  `enum (`[RevenueShareType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RevenueShareType)`)` Method used to calculate the revenue that is shared with developers.  
`revenueShareRates[]` |  `object (`[RevenueShareRange](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RevenueShareRange)`)` Details of the revenue sharing model.  
`state` |  `enum (`[State](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#State)`)` Current state of the rate plan (draft or published).  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time when the rate plan becomes active in milliseconds since epoch.  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time that the rate plan was created in milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time the rate plan was last modified in milliseconds since epoch.  
  
## BillingPeriod

Billing period that defines the frequency at which the customer will be billed.

Enums  
---  
`BILLING_PERIOD_UNSPECIFIED` | Billing period not specified.  
`WEEKLY` | Weekly billing period.**Note** : Not supported by Apigee at this time.  
`MONTHLY` | Monthly billing period.  
  
## PaymentFundingModel

Billing account type.

Enums  
---  
`PAYMENT_FUNDING_MODEL_UNSPECIFIED` | Billing account type not specified.  
`PREPAID` | Prepaid billing account type. Developer pays in advance for the use of your API products. Funds are deducted from their prepaid account balance.**Note** : Not supported by Apigee at this time.  
`POSTPAID` | Postpaid billing account type. Developer is billed through an invoice after using your API products.  
  
## Money

Represents an amount of money with its currency type.

JSON representation  
---  
      
    
    {
      "currencyCode": string,
      "units": string,
      "nanos": integer
    }  
  
Fields  
---  
`currencyCode` |  `string` The three-letter currency code defined in ISO 4217.  
`units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.  
`nanos` |  `integer` Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.  
  
## ConsumptionPricingType

Pricing models used for consumption-based charges.

Enums  
---  
`CONSUMPTION_PRICING_TYPE_UNSPECIFIED` | Pricing model not specified. This is the default.  
`FIXED_PER_UNIT` | Fixed rate charged for each API call.  
`BANDED` | Variable rate charged for each API call based on price tiers.Example:

  * 1-100 calls cost $2 per call
  * 101-200 calls cost $1.50 per call
  * 201-300 calls cost $1 per call
  * Total price for 50 calls: 50 x $2 = $100
  * Total price for 150 calls: 100 x $2 + 50 x $1.5 = $275
  * Total price for 250 calls: 100 x $2 + 100 x $1.5 + 50 x $1 = $400.

  
`TIERED` | **Note** : Not supported by Apigee at this time.  
`STAIRSTEP` | **Note** : Not supported by Apigee at this time.  
  
## RateRange

API call volume range and the fees charged when the total number of API calls is within the range.

JSON representation  
---  
      
    
    {
      "start": string,
      "end": string,
      "fee": {
        object ([Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money))
      }
    }  
  
Fields  
---  
`start` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Starting value of the range. Set to 0 or `null` for the initial range of values.  
`end` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Ending value of the range. Set to 0 or `null` for the last range of values.  
`fee` |  `object (`[Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money)`)` Fee to charge when total number of API calls falls within this range.  
  
## RevenueShareType

Revenue share type.

Enums  
---  
`REVENUE_SHARE_TYPE_UNSPECIFIED` | Revenue share type is not specified.  
`FIXED` | Fixed percentage of the total revenue will be shared. The percentage to be shared can be configured by the API provider.  
`VOLUME_BANDED` | Amount of revenue shared depends on the number of API calls. The API call volume ranges and the revenue share percentage for each volume can be configured by the API provider.**Note** : Not supported by Apigee at this time.  
  
## RevenueShareRange

API call volume range and the percentage of revenue to share with the developer when the total number of API calls is within the range.

JSON representation  
---  
      
    
    {
      "start": string,
      "end": string,
      "sharePercentage": number
    }  
  
Fields  
---  
`start` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Starting value of the range. Set to 0 or `null` for the initial range of values.  
`end` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Ending value of the range. Set to 0 or `null` for the last range of values.  
`sharePercentage` |  `number` Percentage of the revenue to be shared with the developer. For example, to share 21 percent of the total revenue with the developer, set this value to 21. Specify a decimal number with a maximum of two digits following the decimal point.  
  
## State

State of the rate plan.

Enums  
---  
`STATE_UNSPECIFIED` | State of the rate plan is not specified.  
`DRAFT` | Rate plan is in draft mode and only visible to API providers.  
`PUBLISHED` | Rate plan is published and will become visible to developers for the configured duration (between `startTime` and `endTime`).  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/create)`

|  Create a rate plan that is associated with an API product in an organization.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/delete)`

|  Deletes a rate plan.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/get)`

|  Gets the details of a rate plan.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/list)`

|  Lists all the rate plans for an API product.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/update)`

|  Updates an existing rate plan.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
