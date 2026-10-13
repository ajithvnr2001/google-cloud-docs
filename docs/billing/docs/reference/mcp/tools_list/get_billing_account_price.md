---
url: https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/get_billing_account_price/
title: MCP Tools Reference: cloudbilling.googleapis.com \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:15.860424+00:00
---

# MCP Tools Reference: cloudbilling.googleapis.com  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/get_billing_account_price/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  MCP Tools Reference: cloudbilling.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_billing_account_price`

Gets the latest price for a specific SKU available to a Cloud Billing account.

The following code sample shows how to use `curl` to call the `get_billing_account_price` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudbilling.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_billing_account_price",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `GetBillingAccountPrice`.

### GetBillingAccountPriceRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "currencyCode": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the billing account price to retrieve. Format: billingAccounts/{billing_account}/skus/{sku}/price  
`currencyCode` |  `string` Optional. ISO-4217 currency code for the price. If not specified, the currency of the billing account is used.  
  
## Output Schema

Encapsulates the latest price for a `billing account SKU`.

### BillingAccountPrice

JSON representation  
---  
      
    
    {
      "name": string,
      "currencyCode": string,
      "skuPrices": [
        {
          object ([SkuPrice](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.SkuPrice))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for the latest billing account price.  
`currencyCode` |  `string` ISO-4217 currency code for the price.  
`skuPrices[]` |  `object (`[SkuPrice](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.SkuPrice)`)` consumption model price for the `SKU`.  
  
### SkuPrice

JSON representation  
---  
      
    
    {
      "consumptionModel": string,
      "consumptionModelDescription": string,
      "valueType": string,
      "priceReason": {
        object ([PriceReason](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.PriceReason))
      },
    
      // Union field value can be only one of the following:
      "rate": {
        object ([Rate](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Rate))
      }
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`consumptionModel` |  `string` Resource name of the consumption model.  
`consumptionModelDescription` |  `string` Description of the consumption model. Example: "Default", "BigQuery CUD - 1 Year".  
`valueType` |  `string` Type of the price. The possible values are: ["unspecified", "rate"].  
`priceReason` |  `object (`[PriceReason](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.PriceReason)`)` Background information on the origin of the price.  
Union field `value`. Value of the price. `value` can be only one of the following:  
`rate` |  `object (`[Rate](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Rate)`)` Rate price metadata. `Billing account SKUs` with `Rate` price are offered by pricing tiers. The price can have 1 or more rate pricing tiers.  
  
### Rate

JSON representation  
---  
      
    
    {
      "tiers": [
        {
          object ([RateTier](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.RateTier))
        }
      ],
      "unitInfo": {
        object ([UnitInfo](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.UnitInfo))
      },
      "aggregationInfo": {
        object ([AggregationInfo](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.AggregationInfo))
      }
    }  
  
Fields  
---  
`tiers[]` |  `object (`[RateTier](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.RateTier)`)` All tiers associated with the `Rate` price.  
`unitInfo` |  `object (`[UnitInfo](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.UnitInfo)`)` Unit info such as name and quantity.  
`aggregationInfo` |  `object (`[AggregationInfo](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.AggregationInfo)`)` Aggregation info for tiers such as aggregation level and interval.  
  
### RateTier

JSON representation  
---  
      
    
    {
      "startAmount": {
        object ([Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal))
      },
      "listPrice": {
        object ([Money](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Money))
      },
      "contractPrice": {
        object ([Money](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Money))
      },
      "effectiveDiscountPercent": {
        object ([Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal))
      }
    }  
  
Fields  
---  
`startAmount` |  `object (`[Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal)`)` Lower bound amount for a tier. Tiers 0-100, 100-200 will be represented with two tiers with `start_amount` 0 and 100.  
`listPrice` |  `object (`[Money](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Money)`)` List price of one tier.  
`contractPrice` |  `object (`[Money](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Money)`)` Negotiated contract price specific for a billing account.  
`effectiveDiscountPercent` |  `object (`[Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal)`)` Percentage of effective discount calculated using the current list price per pricing tier. Formula used: effective_discount_percent = (list_price - contract_price) / list_price × 100 If list_price and contract_price are zero, this field is the same as `discount_percent` of `FixedDiscount` and `FloatingDiscount`. If your contract does NOT have the feature LIST_PRICE_AS_CEILING enabled, the effective_discount_percent can be negative if the SKU has a `FixedDiscount` and the current list price is lower than the list price on the date of the contract agreement. See the `FixedDiscount.fix_time` on when the discount was set. If you have questions regarding pricing per SKU, contact your Account team for more details.  
  
### Decimal

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string` The decimal value, as a string.The string representation consists of an optional sign, `+` (`U+002B`) or `-` (`U+002D`), followed by a sequence of zero or more decimal digits ("the integer"), optionally followed by a fraction, optionally followed by an exponent. An empty string **should** be interpreted as `0`.The fraction consists of a decimal point followed by zero or more decimal digits. The string must contain at least one digit in either the integer or the fraction. The number formed by the sign, the integer and the fraction is referred to as the significand.The exponent consists of the character `e` (`U+0065`) or `E` (`U+0045`) followed by one or more decimal digits.Services **should** normalize decimal values before storing them by:

  * Removing an explicitly-provided `+` sign (`+2.5` -> `2.5`).
  * Replacing a zero-length integer value with `0` (`.5` -> `0.5`).
  * Coercing the exponent character to upper-case, with explicit sign (`2.5e8` -> `2.5E+8`).
  * Removing an explicitly-provided zero exponent (`2.5E0` -> `2.5`).

Services **may** perform additional normalization based on its own needs and the internal decimal implementation selected, such as shifting the decimal point and exponent value together (example: `2.5E-1` <-> `0.25`). Additionally, services **may** preserve trailing zeroes in the fraction to indicate increased precision, but are not required to do so.Note that only the `.` character is supported to divide the integer and the fraction; `,` **should not** be supported regardless of locale. Additionally, thousand separators **should not** be supported. If a service does support them, values **must** be normalized.The ENBF grammar is:
    
    
    DecimalString =
      '' | [Sign] Significand [Exponent];
    
    Sign = '+' | '-';
    
    Significand =
      Digits ['.'] [Digits] | [Digits] '.' Digits;
    
    Exponent = ('e' | 'E') [Sign] Digits;
    
    Digits = { '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' };
    

Services **should** clearly document the range of supported values, the maximum supported precision (total number of digits), and, if applicable, the scale (number of digits after the decimal point), as well as how it behaves when receiving out-of-bounds values.Services **may** choose to accept values passed as input even when the value has a higher precision or scale than the service supports, and **should** round the value to fit the supported scale. Alternatively, the service **may** error with `400 Bad Request` (`INVALID_ARGUMENT` in gRPC) if precision would be lost.Services **should** error with `400 Bad Request` (`INVALID_ARGUMENT` in gRPC) if the service receives a value outside of the supported range.  
  
### Money

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
  
### UnitInfo

JSON representation  
---  
      
    
    {
      "unit": string,
      "unitDescription": string,
      "unitQuantity": {
        object ([Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal))
      }
    }  
  
Fields  
---  
`unit` |  `string` Shorthand for the unit. Example: GiBy.mo.  
`unitDescription` |  `string` Human-readable description of the unit. Example: gibibyte month.  
`unitQuantity` |  `object (`[Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal)`)` Unit quantity for the tier. Example: if the RateTier price is $1 per 1000000 Bytes, then `unit_quantity` is set to 1000000.  
  
### AggregationInfo

JSON representation  
---  
      
    
    {
      "level": enum ([Level](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Level)),
      "interval": enum ([Interval](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Interval))
    }  
  
Fields  
---  
`level` |  `enum (`[Level](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Level)`)` Level at which usage is aggregated to compute cost. Example: "ACCOUNT" level indicates that usage is aggregated across all projects in a single account.  
`interval` |  `enum (`[Interval](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Interval)`)` Interval at which usage is aggregated to compute cost. Example: "MONTHLY" interval indicates that usage is aggregated every month.  
  
### PriceReason

JSON representation  
---  
      
    
    {
      "type": string,
    
      // Union field metadata can be only one of the following:
      "defaultPrice": {
        object (DefaultPrice)
      },
      "fixedPrice": {
        object (FixedPrice)
      },
      "fixedDiscount": {
        object ([FixedDiscount](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.FixedDiscount))
      },
      "floatingDiscount": {
        object ([FloatingDiscount](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.FloatingDiscount))
      },
      "migratedPrice": {
        object ([MigratedPrice](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.MigratedPrice))
      },
      "mergedPrice": {
        object (MergedPrice)
      },
      "listPriceAsCeiling": {
        object (ListPriceAsCeiling)
      }
      // End of list of possible types for union field metadata.
    }  
  
Fields  
---  
`type` |  `string` Type of the price reason. It can have values such as 'unspecified', 'default-price', 'fixed-price', 'fixed-discount', 'floating-discount', 'migrated-price', 'merged-price', 'list-price-as-ceiling'.  
Union field `metadata`. Metadata of the price reason. `metadata` can be only one of the following:  
`defaultPrice` |  `object (`DefaultPrice`)` Default price which is the current list price.  
`fixedPrice` |  `object (`FixedPrice`)` Fixed price applicable during the terms of a contract agreement.  
`fixedDiscount` |  `object (`[FixedDiscount](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.FixedDiscount)`)` Discount off the list price, anchored to the list price as of a fixed time.  
`floatingDiscount` |  `object (`[FloatingDiscount](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.FloatingDiscount)`)` Discount off the current list price, not anchored to any list price as of a fixed time.  
`migratedPrice` |  `object (`[MigratedPrice](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.MigratedPrice)`)` Price migrated from other SKUs.  
`mergedPrice` |  `object (`MergedPrice`)` Price after merging from multiple sources.  
`listPriceAsCeiling` |  `object (`ListPriceAsCeiling`)` Contract feature that the list price (DefaultPrice) will be used for the price if the current list price drops lower than the custom fixed price. Available to new contracts after March 21, 2022. Applies to all fixed price SKUs in the contract, including `FixedPrice`, `FixedDiscount`, `MigratedPrice`, and `MergedPrice`.  
  
### FixedDiscount

JSON representation  
---  
      
    
    {
      "discountPercent": {
        object ([Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal))
      },
      "fixTime": string,
      "discountScopeType": string,
    
      // Union field discount_scope can be only one of the following:
      "skuGroup": string
      // End of list of possible types for union field discount_scope.
    }  
  
Fields  
---  
`discountPercent` |  `object (`[Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal)`)` Percentage of the fixed discount.  
`fixTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time that the fixed discount is anchored to.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`discountScopeType` |  `string` Type of the fixed discount scope which indicates the source of the discount. It can have values such as 'unspecified' and 'sku-group'.  
Union field `discount_scope`. The scope of the fixed discount. `discount_scope` can be only one of the following:  
`skuGroup` |  `string` SKU group where the fixed discount comes from.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### FloatingDiscount

JSON representation  
---  
      
    
    {
      "discountPercent": {
        object ([Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal))
      },
      "discountScopeType": string,
    
      // Union field discount_scope can be only one of the following:
      "skuGroup": string
      // End of list of possible types for union field discount_scope.
    }  
  
Fields  
---  
`discountPercent` |  `object (`[Decimal](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_prices#Output.Schema.Decimal)`)` Percentage of the floating discount.  
`discountScopeType` |  `string` Type of the floating discount scope which indicates the source of the discount. It can have values such as 'unspecified' and 'sku-group'.  
Union field `discount_scope`. The scope of the floating discount. `discount_scope` can be only one of the following:  
`skuGroup` |  `string` SKU group where the floating discount comes from.  
  
### MigratedPrice

JSON representation  
---  
      
    
    {
      "sourceSku": string
    }  
  
Fields  
---  
`sourceSku` |  `string` Source SKU where the discount is migrated from. Format: billingAccounts/{billing_account}/skus/{sku}  
  
### Level

Different aggregation levels.

Enums  
---  
`LEVEL_UNSPECIFIED` | Default unspecified value.  
`LEVEL_ACCOUNT` | Usage is aggregated at an account level.  
`LEVEL_PROJECT` | Usage is aggregated at a project level.  
  
### Interval

Different aggregation intervals.

Enums  
---  
`INTERVAL_UNSPECIFIED` | Default unspecified value.  
`INTERVAL_MONTHLY` | Usage is aggregated every month.  
`INTERVAL_DAILY` | Usage is aggregated every day.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
