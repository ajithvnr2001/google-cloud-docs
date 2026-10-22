---
url: https://docs.cloud.google.com/billing/v1/how-tos/catalog-api/
title: Get publicly available Google Cloud pricing information \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:08.029575+00:00
---

# Get publicly available Google Cloud pricing information  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/v1/how-tos/catalog-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Get publicly available Google Cloud pricing information Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use the Cloud Billing Catalog API to:

  * Get a list of all public services including relevant metadata about each service.
  * Get a list of all public SKUs within a service including: 
    * Human readable description of the SKU.
    * Public pricing of the SKU.
    * Regions where the SKU is available for purchase.
    * Categorization data about the SKU.



If you have **custom contract pricing** , you can use the [Pricing API](https://docs.cloud.google.com/billing/docs/how-to/get-pricing-information-api) to get prices that are applicable to your Cloud Billing account.

## Before you begin

Before you can use the Cloud Billing Catalog API, you'll need to enable the Cloud Billing API and get an API key.

Enable the Cloud Billing API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbilling.googleapis.com)

When you are prompted to confirm the Google Cloud project you intend to use for the Cloud Billing Catalog API, we recommend you use a project that is set up to contain all of your FinOps and billing administration needs for a Cloud Billing account, including where the Cloud Billing API is enabled.

[Learn more about the benefits to using a FinOps-focused project](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#set-up-billing-project) for your billing administration use cases.

#### Get an API key

Calling the Cloud Billing Catalog API requires an API Key. You can find details about API Keys in [Using API Keys](https://docs.cloud.google.com/docs/authentication/api-keys).

## Listing public services from the catalog

In this step you will get a list of all public services including relevant metadata about each service.

The following code snippet lists all public services in the catalog.

Request:

`GET https://cloudbilling.googleapis.com/v1/services?key=<var>API_KEY</var>`

Response:
    
    
    {
      "services": [
        {
          "name": "[SERVICE_NAME]",
          "serviceId": "[SERVICE_ID]",
          "displayName": "[DISPLAY_NAME]",
        },
        [...]
      ],
      "nextPageToken": "[NEXT_PAGE_TOKEN]"
    }
    

Where:

  * `[SERVICE_NAME]` is the resource name for the service.
  * `[SERVICE_ID]` is the identifier for the service.
  * `[DISPLAY_NAME]` is the human readable display name for the service.



Results are paginated, and are limited to **5000** SKUs per page. The response includes a `nextPageToken` that you can use to get the next 5000 results. To fetch the next batch, set `pageToken=[NEXT_PAGE_TOKEN]`. To reduce the number of SKUs per page, set `pageSize=[CUSTOM_PAGE_SIZE]`. When all items have been listed, no token is returned.

## Getting the list of SKUs for a service

The following code snippet lists the SKUs in the catalog for the specified service:

Request:

`GET https://cloudbilling.googleapis.com/v1/services/SERVICE_ID/skus?key=<var>API_KEY</var>`

Where:

  * `SERVICE_ID` is the identifier of the parent service.



Response:
    
    
    {
      "skus": [
        {
            "name": "[SKU_NAME]",
            "skuId": "[SKU_ID]",
            "description": "[SKU_DESCRIPTION]",
            "category": {
                "serviceDisplayName": "[SVC_DISPLAY_NAME]",
                "resourceFamily": "[FAMILY]",
                "resourceGroup": "[GROUP]",
                "usageType": "[USAGE]",
            },
            "serviceRegions": [
              "[REGION]"
            ],
            "pricingInfo": [
              {
                  "effectiveTime": "[TIME]",
                  "summary": "[SUMMARY]",
                  "pricingExpression": {
                      "usageUnit": "[USAGE_UNIT]",
                      "usageUnitDescription": "[USAGE_UNIT_DESCRIPTION]",
                      "baseUnit": "[BASE_UNIT]",
                      "baseUnitDescription": "[BASE_UNIT_DESCRIPTION]",
                      "baseUnitConversionFactor": [BASE_CONVERSION_FACTOR],
                      "displayQuantity": [DISPLAY_QUANTITY],
                      "tieredRates": [
                        {
                            "startUsageAmount": [START_AMOUNT],
                            "unitPrice": {
                                "currencyCode": "[CURRENCY_CODE]",
                                "units": [UNITS],
                                "nanos": [NANOS],
                            },
                        }
                      ],
                  },
                  "aggregationInfo": {
                      "aggregationLevel": enum("[AGGREGATION_LEVEL]"),
                      "aggregationInterval": enum("[AGGREGATION_INTERVAL]"),
                      "aggregationCount": [AGGREGATION_COUNT],
                  },
                  "currencyConversionRate": [CONVERSION_RATE],
              }
            ],
            "serviceProviderName": "[SERVICE_PROVIDER]",
            "geoTaxonomy": {
              "type": "[TAXONOMY_TYPE]",
              "regions": [
              "[REGION]"
            ]
          }
        }
      ],
      "nextPageToken": "[NEXT_PAGE_TOKEN]"
    }
    

Where:

  * `[SKU_NAME]` is the resource name for the SKU in the form `services/{SERVICE_ID}/skus/{SKU_ID}`.
  * `[SKU_ID]` is the unique identifier for the SKU.
  * `[SKU_DESCRIPTION]` is a human readable description of the SKU.
  * `[SVC_DISPLAY_NAME]` is the display name of the service to which the SKU belongs.
  * `[FAMILY]` is the type of product the SKU refers to. For example, "Compute", "Storage", "Network", etc.
  * `[GROUP]` is a group classification for related SKUs. For example, "RAM, "GPU", "Prediction", etc.
  * `[USAGE]` represents how the SKU is consumed. For example, "OnDemand, "Preemptible, "Commit1Mo", "Commit1Yr", etc.
  * `[REGION]` is the list of [service regions](https://docs.cloud.google.com/about/locations) in which the SKU is offered. For example, "asia-east1".
  * `[TIME]` is a timestamp representing the time from which this pricing was effective in the form `2014-10-02T15:01:23.045123456Z`.
  * `[SUMMARY]` is a human readable summary of the pricing information,
  * `[USAGE_UNIT]` is the shorthand for the unit of usage in which the pricing is specified. For example, `usageUnit` of "GiBy" means that usage is specified in "Gibibytes".
  * `[USAGE_UNIT_DESCRIPTION]` is the unit of usage in human readable form, for example, "Gibibyte".
  * `[BASE_UNIT]` is the SKU's base unit, and is the unit used in usage exports. For example, `baseUnit` of "By" means the usage is specified in "Bytes".
  * `[BASE_UNIT_DESCRIPTION]` is the base unit in human readable form. For example, "byte".
  * `[BASE_CONVERSION_FACTOR]` is the conversion factor for converting price per usage_unit to price per base_unit, and converting start_usage amount to start_usage_amount in base_unit. For example, _start_usage_amount * base_unit_conversion_factor = start_usage_amount in base_unit._
  * `[DISPLAY_QUANTITY]` is the recommended quantity of units for displaying pricing info. When displaying pricing info, it is recommended to display: `(unitPrice * displayQuantity) per displayQuantity usageUnit`. This field does not affect the pricing formula and is for display purposes only. For example, if the `unitPrice` is "0.0001 USD", the `usageUnit` is "GB" and the `displayQuantity` is "1000", then the recommended way to display the pricing info is "0.10 USD per 1000 GB".
  * `[START_AMOUNT]` Usage is priced at the rate only after this amount is consumed. For example, a `startUsageAmount` of 10 indicates that the usage will be priced at the price defined below after the first 10 `usage_units`.
  * `[CURRENCY_CODE]` is the three-letter currency code defined as in ISO 4217.
  * `[UNITS]` is the whole units of the amount. For example if currencyCode is "USD", then 1 unit is one US dollar.
  * `[NANOS]` is the number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If units is positive, nanos must be positive or zero. If units is zero, nanos can be positive, zero, or negative. If units is negative, nanos must be negative or zero.



The cost of the SKU is `units + nanos`. For example, a cost of $1.75 is represented as `units=1` and `nanos=750,000,000`.

  * `[AGGREGATION_LEVEL]` is the level at which usage is aggregated to compute cost. Valid values are ACCOUNT, PROJECT, and AGGREGATION_LEVEL_UNSPECIFIED.
  * `[AGGREGATION_INTERVAL]` is the interval at which usage is aggregated to compute cost. Valid values are DAILY, MONTHLY, and AGGREGATION_INTERVAL_UNSPECIFIED.
  * `[AGGREGATION_COUNT]` is the number of intervals to aggregate over. For example, if `aggregationLevel` is "DAILY" and `aggregationCount` is 14, aggregation will be over 14 days.
  * `[CONVERSION_RATE]` is the conversion rate for currency conversion, from USD to the currency specified in the request. If the currency is not specified this defaults to 1.0.
  * `[SERVICE_PROVIDER]` identifies the service provider. This is 'Google' for first party services in Google Cloud Platform.
  * `[TAXONOMY_TYPE]` is the type of geographic taxonomy for a SKU: `GLOBAL`, `REGIONAL`, or `MULTI_REGIONAL`.
  * `[REGION]` is The list of regions associated with a SKU. This field is empty for Global SKUs since they are associated with all Google Cloudregions.



Results are paginated, and are limited to **5000** SKUs per page. The response includes a `nextPageToken` that you can use to get the next 5000 results. To fetch the next batch, set `pageToken=[NEXT_PAGE_TOKEN]`. To reduce the number of SKUs per page, set `pageSize=[CUSTOM_PAGE_SIZE]`. When all items have been listed, no token is returned.

## Related information

Pricing and SKU information is also available in the [pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) or the [Cloud Billing pricing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
