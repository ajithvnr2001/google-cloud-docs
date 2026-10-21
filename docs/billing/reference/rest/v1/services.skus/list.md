---
url: https://docs.cloud.google.com/billing/reference/rest/v1/services.skus/list/
title: Method: services.skus.list \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:33:31.148235+00:00
---

# Method: services.skus.list  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/reference/rest/v1/services.skus/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Method: services.skus.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Sku
    * JSON representation
  * Category
    * JSON representation
  * PricingInfo
    * JSON representation
  * PricingExpression
    * JSON representation
  * TierRate
    * JSON representation
  * Money
    * JSON representation
  * AggregationInfo
    * JSON representation
  * AggregationLevel
  * AggregationInterval
  * GeoTaxonomy
    * JSON representation
  * Type
  * Try it!



Lists all publicly available SKUs for a given cloud service.

### HTTP request

`GET https://cloudbilling.googleapis.com/v1/{parent=services/*}/skus`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the service. Example: "services/6F81-5844-456A"  
  
### Query parameters

Parameters  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional inclusive start time of the time range for which the pricing versions will be returned. Timestamps in the future are not allowed. The time range has to be within a single calendar month in America/Los_Angeles timezone. Time range as a whole is optional. If not specified, the latest pricing will be returned (up to 12 hours old at most).Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional exclusive end time of the time range for which the pricing versions will be returned. Timestamps in the future are not allowed. The time range has to be within a single calendar month in America/Los_Angeles timezone. Time range as a whole is optional. If not specified, the latest pricing will be returned (up to 12 hours old at most).Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`currencyCode` |  `string` The ISO 4217 currency code for the pricing info in the response proto. Will use the conversion rate as of startTime. Optional. If not specified USD will be used.  
`pageSize` |  `integer` Requested page size. Defaults to 5000.  
`pageToken` |  `string` A token identifying a page of results to return. This should be a `nextPageToken` value returned from a previous `skus.list` call. If unspecified, the first page of results is returned.  
  
### Request body

The request body must be empty.

### Response body

Response message for `skus.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "skus": [
        {
          object ([Sku](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Sku))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`skus[]` |  `object (`[Sku](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Sku)`)` The list of public SKUs of the given service.  
`nextPageToken` |  `string` A token to retrieve the next page of results. To retrieve the next page, call `skus.list` again with the `pageToken` field set to this value. This field is empty if there are no more results to retrieve.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-billing`
  * `https://www.googleapis.com/auth/cloud-billing.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Sku

Encapsulates a single SKU in Google Cloud

JSON representation  
---  
      
    
    {
      "name": string,
      "skuId": string,
      "description": string,
      "category": {
        object ([Category](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Category))
      },
      "serviceRegions": [
        string
      ],
      "pricingInfo": [
        {
          object ([PricingInfo](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#PricingInfo))
        }
      ],
      "serviceProviderName": string,
      "geoTaxonomy": {
        object ([GeoTaxonomy](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#GeoTaxonomy))
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name for the SKU. Example: "services/6F81-5844-456A/skus/D041-B8A1-6E0B"  
`skuId` |  `string` The identifier for the SKU. Example: "D041-B8A1-6E0B"  
`description` |  `string` A human readable description of the SKU, has a maximum length of 256 characters.  
`category` |  `object (`[Category](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Category)`)` The category hierarchy of this SKU, purely for organizational purpose.  
`serviceRegions[]` |  `string` List of service regions this SKU is offered at. Example: "asia-east1" Service regions can be found at <https://cloud.google.com/about/locations/>  
`pricingInfo[]` |  `object (`[PricingInfo](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#PricingInfo)`)` A timeline of pricing info for this SKU in chronological order.  
`serviceProviderName` |  `string` Identifies the service provider. This is 'Google' for first party services in Google Cloud Platform.  
`geoTaxonomy` |  `object (`[GeoTaxonomy](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#GeoTaxonomy)`)` The geographic taxonomy for this sku.  
  
## Category

Represents the category hierarchy of a SKU.

JSON representation  
---  
      
    
    {
      "serviceDisplayName": string,
      "resourceFamily": string,
      "resourceGroup": string,
      "usageType": string
    }  
  
Fields  
---  
`serviceDisplayName` |  `string` The display name of the service this SKU belongs to.  
`resourceFamily` |  `string` The type of product the SKU refers to. Example: "Compute", "Storage", "Network", "ApplicationServices" etc.  
`resourceGroup` |  `string` A group classification for related SKUs. Example: "RAM", "GPU", "Prediction", "Ops", "GoogleEgress" etc.  
`usageType` |  `string` Represents how the SKU is consumed. Example: "OnDemand", "Preemptible", "Commit1Mo", "Commit1Yr" etc.  
  
## PricingInfo

Represents the pricing information for a SKU at a single point of time.

JSON representation  
---  
      
    
    {
      "effectiveTime": string,
      "summary": string,
      "pricingExpression": {
        object ([PricingExpression](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#PricingExpression))
      },
      "aggregationInfo": {
        object ([AggregationInfo](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#AggregationInfo))
      },
      "currencyConversionRate": number
    }  
  
Fields  
---  
`effectiveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp from which this pricing was effective within the requested time range. This is guaranteed to be greater than or equal to the startTime field in the request and less than the endTime field in the request. If a time range was not specified in the request this field will be equivalent to a time within the last 12 hours, indicating the latest pricing info.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`summary` |  `string` An optional human readable summary of the pricing information, has a maximum length of 256 characters.  
`pricingExpression` |  `object (`[PricingExpression](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#PricingExpression)`)` Expresses the pricing formula. See `PricingExpression` for an example.  
`aggregationInfo` |  `object (`[AggregationInfo](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#AggregationInfo)`)` Aggregation Info. This can be left unspecified if the pricing expression doesn't require aggregation.  
`currencyConversionRate` |  `number` Conversion rate used for currency conversion, from USD to the currency specified in the request. This includes any surcharge collected for billing in non USD currency. If a currency is not specified in the request this defaults to 1.0. Example: USD * currencyConversionRate = JPY  
  
## PricingExpression

Expresses a mathematical pricing formula. For Example:-

`usageUnit: GBy` `tieredRates:` `[startUsageAmount: 20, unitPrice: $10]` `[startUsageAmount: 100, unitPrice: $5]`

The above expresses a pricing formula where the first 20GB is free, the next 80GB is priced at $10 per GB followed by $5 per GB for additional usage.

JSON representation  
---  
      
    
    {
      "usageUnit": string,
      "displayQuantity": number,
      "tieredRates": [
        {
          object ([TierRate](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#TierRate))
        }
      ],
      "usageUnitDescription": string,
      "baseUnit": string,
      "baseUnitDescription": string,
      "baseUnitConversionFactor": number
    }  
  
Fields  
---  
`usageUnit` |  `string` The short hand for unit of usage this pricing is specified in. Example: usageUnit of "GiBy" means that usage is specified in "Gibi Byte".  
`displayQuantity` |  `number` The recommended quantity of units for displaying pricing info. When displaying pricing info it is recommended to display: (unitPrice * displayQuantity) per displayQuantity usageUnit. This field does not affect the pricing formula and is for display purposes only. Example: If the unitPrice is "0.0001 USD", the usageUnit is "GB" and the displayQuantity is "1000" then the recommended way of displaying the pricing info is "0.10 USD per 1000 GB"  
`tieredRates[]` |  `object (`[TierRate](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#TierRate)`)` The list of tiered rates for this pricing. The total cost is computed by applying each of the tiered rates on usage. This repeated list is sorted by ascending order of startUsageAmount.  
`usageUnitDescription` |  `string` The unit of usage in human readable form. Example: "gibi byte".  
`baseUnit` |  `string` The base unit for the SKU which is the unit used in usage exports. Example: "By"  
`baseUnitDescription` |  `string` The base unit in human readable form. Example: "byte".  
`baseUnitConversionFactor` |  `number` Conversion factor for converting from price per usageUnit to price per baseUnit, and startUsageAmount to startUsageAmount in baseUnit. unitPrice / baseUnitConversionFactor = price per baseUnit. startUsageAmount * baseUnitConversionFactor = startUsageAmount in baseUnit.  
  
## TierRate

The price rate indicating starting usage and its corresponding price.

JSON representation  
---  
      
    
    {
      "startUsageAmount": number,
      "unitPrice": {
        object ([Money](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Money))
      }
    }  
  
Fields  
---  
`startUsageAmount` |  `number` Usage is priced at this rate only after this amount. Example: startUsageAmount of 10 indicates that the usage will be priced at the unitPrice after the first 10 usage_units.  
`unitPrice` |  `object (`[Money](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Money)`)` The price per unit of usage. Example: unitPrice of amount $10 indicates that each unit will cost $10.  
  
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
  
## AggregationInfo

Represents the aggregation level and interval for pricing of a single SKU.

JSON representation  
---  
      
    
    {
      "aggregationLevel": enum ([AggregationLevel](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#AggregationLevel)),
      "aggregationInterval": enum ([AggregationInterval](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#AggregationInterval)),
      "aggregationCount": integer
    }  
  
Fields  
---  
`aggregationLevel` |  `enum (`[AggregationLevel](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#AggregationLevel)`)`  
`aggregationInterval` |  `enum (`[AggregationInterval](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#AggregationInterval)`)`  
`aggregationCount` |  `integer` The number of intervals to aggregate over. Example: If aggregationLevel is "DAILY" and aggregationCount is 14, aggregation will be over 14 days.  
  
## AggregationLevel

The level at which usage is aggregated to compute cost. Example: "ACCOUNT" aggregation level indicates that usage for tiered pricing is aggregated across all projects in a single account.

Enums  
---  
`AGGREGATION_LEVEL_UNSPECIFIED` |   
`ACCOUNT` |   
`PROJECT` |   
  
## AggregationInterval

The interval at which usage is aggregated to compute cost. Example: "MONTHLY" aggregation interval indicates that usage for tiered pricing is aggregated every month.

Enums  
---  
`AGGREGATION_INTERVAL_UNSPECIFIED` |   
`DAILY` |   
`MONTHLY` |   
  
## GeoTaxonomy

Encapsulates the geographic taxonomy data for a sku.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Type)),
      "regions": [
        string
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list#Type)`)` The type of Geo Taxonomy: GLOBAL, REGIONAL, or MULTI_REGIONAL.  
`regions[]` |  `string` The list of regions associated with a sku. Empty for Global skus, which are associated with all Google Cloud regions.  
  
## Type

The type of Geo Taxonomy: GLOBAL, REGIONAL, or MULTI_REGIONAL.

Enums  
---  
`TYPE_UNSPECIFIED` | The type is not specified.  
`GLOBAL` | The sku is global in nature, e.g. a license sku. Global skus are available in all regions, and so have an empty region list.  
`REGIONAL` | The sku is available in a specific region, e.g. "us-west2".  
`MULTI_REGIONAL` | The sku is associated with multiple regions, e.g. "us-west2" and "us-east1".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
