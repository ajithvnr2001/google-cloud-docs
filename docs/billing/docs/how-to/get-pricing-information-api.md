---
url: https://docs.cloud.google.com/billing/docs/how-to/get-pricing-information-api/
title: Get Google Cloud pricing information \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:13:34.638824+00:00
---

# Get Google Cloud pricing information  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/get-pricing-information-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Get Google Cloud pricing information Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Google Cloud Pricing API is a set of API resources that helps you get the prices and other information for Google Cloud services.

This page shows you a few examples of API requests that you can make to get information about publicly listed services and SKUs, as well as services and SKUs that are available only to your Cloud Billing account as part of a contract with Google Cloud.

You can use the Pricing API to get a list of services, or the price for a specific stock keeping unit (SKU). A SKU distinctly identifies a resource that you can purchase. An example of a SKU is `Nvidia Tesla T4 GPU attached to Spot Preemptible VMs running in Warsaw`. If you have a contract with custom pricing, you can also use the Pricing API to get the custom prices associated with your Cloud Billing account.

For a full list of available resources in the Pricing API, and for detailed information on the request and response formats, [see the API reference](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest).

## Before you begin

Enable the Cloud Billing API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbilling.googleapis.com)

APIs are enabled in a Google Cloud project. The Pricing API is part of the Cloud Billing API. When you are prompted to confirm the project you intend to use for the Pricing API, we recommend you use a Google Cloud project that is set up to contain all of your FinOps and billing administration needs for a Cloud Billing account. This project can contain all of the billing-specific APIs, including the Cloud Billing API.

[Learn more about the benefits to using a FinOps-focused project](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#set-up-billing-project) for your billing administration use cases.

## Get public service and pricing information

The following examples show API calls that you can use to get publicly listed information about Google Cloud services, and SKUs.

To get information about public services, SKUs, or prices, you must [create an API key](https://docs.cloud.google.com/docs/authentication/api-keys#create).

### Get a list of public Google Cloud services

The following example lists all public Google Cloud services, including the metadata for each service.

You don't need any specific IAM permissions to make this API call.

Before using any of the request data, make the following replacements: 

  * API_KEY: Your Google Cloud API key.
  * PAGE_SIZE (Optional): The number of services to return. The default is 50.
  * PAGE_TOKEN (Optional): The page token, which you get from the `nextPageToken` in an earlier response.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v2beta/services?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         "https://cloudbilling.googleapis.com/v2beta/services?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell

Execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v2beta/services?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

The response contains a list of services, and information about each service. The example below shows the format for Compute Engine.

The results are paginated, and are limited to 50 services per page. The response includes a `nextPageToken` that you can use to get the next page of results. To fetch the next batch, set `pageToken=PAGE_TOKEN`. To reduce the number of SKUs per page, set `pageSize=PAGE_SIZE`. When all items have been listed, no token is returned. 
    
    
    {
      "services": [
        {
          "name": "services/6F81-5844-456A",
          "serviceId": "6F81-5844-456A",
          "displayName": "Compute Engine",
        },
        ...
      ]
      "nextPageToken": "alphanumeric-page-token"
    }
    

### Get a list of SKUs for a public Google Cloud service

The following example lists the public SKUs for a specified service.

You don't need any specific IAM permissions to make this API call.

Before using any of the request data, make the following replacements: 

  * API_KEY: Your Google Cloud API key.
  * FILTER: The services to filter the SKUs by. For example, to list SKUs for Compute Engine, use the filter `service="services/6F81-5844-456A"`. 
  * PAGE_SIZE (Optional): The maximum number of SKUs to return. The default is 50, and the maximum is 5000. 
  * PAGE_TOKEN (Optional): The page token, which is in `nextPageToken` in the response.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v2beta/skus?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         "https://cloudbilling.googleapis.com/v2beta/skus?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER"

#### PowerShell

Execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v2beta/skus?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER" | Select-Object -Expand Content

The following response shows some example SKUs returned for Compute Engine. The results are paginated, and are limited to 50 SKUs per page. The response includes a `nextPageToken` that you can use to get the next page of results. To fetch the next batch, set `pageToken=PAGE_TOKEN`. To change the number of SKUs per page, set `pageSize=PAGE_SIZE`. When all items have been listed, no token is returned. 
    
    
    {
      "skus": [
        {
          "name": "skus/0008-F633-76AA",
          "skuId": "0008-F633-76AA",
          "displayName": "Example L4 GPU attached to Spot Preemptible VMs running in Hong Kong",
          "service": "6F81-5844-456A",
          "productTaxonomy": {
            "taxonomyCategories": [
              {
                "category": "GCP"
              },
              {
                "category": "Compute"
              },
              {
                "category": "GPUs"
              },
              {
                "category": "GPUs Preemptible"
              },
              {
                "category": "L4"
              }
            ]
          },
          "geoTaxonomy": {
            "type": "REGIONAL",
            "regionalMetadata": {
              "region": {
                "region": "asia-east2"
              }
            }
          }
        },
        {
          "name": "skus/000F-0B14-D302",
          "skuId": "000F-0B14-D302",
          "displayName": "Example Sole Tenancy Instance Ram running in Turin",
          "service": "6F81-5844-456A",
          "productTaxonomy": {
            "taxonomyCategories": [
              {
                "category": "GCP"
              },
              {
                "category": "Compute"
              },
              {
                "category": "GCE"
              },
              {
                "category": "VMs On Demand"
              },
              {
                "category": "Memory: Per GB"
              },
              {
                "category": "C3"
              }
            ]
          },
          "geoTaxonomy": {
            "type": "REGIONAL",
            "regionalMetadata": {
              "region": {
                "region": "europe-west12"
              }
            }
          }
        }
      ],
      "nextPageToken": "alphanumeric-nextpageToken"
    }
    

### Get the prices for all public Google Cloud SKUs

Before using any of the request data, make the following replacements: 

  * SKU_ID: A specific SKU ID to get the price for. To get prices for all SKUs, use `-`. 
  * API_KEY: Your Google Cloud API key.
  * PAGE_SIZE (Optional): The number of services to return. The default is 50.
  * PAGE_TOKEN (Optional): The page token, which you get from the `nextPageToken` in an earlier response.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v1beta/skus/SKU_ID/prices?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         "https://cloudbilling.googleapis.com/v1beta/skus/SKU_ID/prices?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell

Execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v1beta/skus/SKU_ID/prices?key=API_KEY&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

The response contains pricing information for each SKU ID.The example below shows the format for all public SKUs, with a page size of `2`.

The results are paginated, and by default, contain 50 prices per page. The response includes a `nextPageToken` that you can use to get the next page of results. To fetch the next batch, set `pageToken=PAGE_TOKEN`. To reduce the number of results per page, set `pageSize=PAGE_SIZE`. When all items have been listed, no token is returned. 
    
    
    {
      "prices": [
        {
          "name": "skus/0000-9B70-F099/price",
          "currencyCode": "USD",
          "valueType": "rate",
          "rate": {
            "tiers": [
              {
                "startAmount": {
                  "value": "0"
                },
                "listPrice": {
                  "currencyCode": "USD",
                  "nanos": 690000000
                }
              }
            ],
            "unitInfo": {
              "unit": "h",
              "unitDescription": "hour",
              "unitQuantity": {
                "value": "1"
              }
            },
            "aggregationInfo": {
              "level": "LEVEL_ACCOUNT",
              "interval": "INTERVAL_MONTHLY"
            }
          }
        },
        {
          "name": "skus/0002-17F9-0731/price",
          "currencyCode": "USD",
          "valueType": "rate",
          "rate": {
            "tiers": [
              {
                "startAmount": {
                  "value": "0"
                },
                "listPrice": {
                  "currencyCode": "USD"
                }
              },
              {
                "startAmount": {
                  "value": "1"
                },
                "listPrice": {
                  "currencyCode": "USD",
                  "nanos": 390000000
                }
              },
              {
                "startAmount": {
                  "value": "1024"
                },
                "listPrice": {
                  "currencyCode": "USD",
                  "nanos": 340000000
                }
              }
            ],
            "unitInfo": {
              "unit": "GiBy.mo",
              "unitDescription": "gibibyte month",
              "unitQuantity": {
                "value": "1"
              }
            },
            "aggregationInfo": {
              "level": "LEVEL_ACCOUNT",
              "interval": "INTERVAL_MONTHLY"
            }
          }
        }
      ],
      "nextPageToken": "1234alphanumericCode"
    }
    

### Get the price of a public SKU

The following example gets the price of a publicly listed SKU. You can get a [full list of Google Cloud SKU IDs on the SKUs page](https://docs.cloud.google.com/skus).

You don't need any specific IAM permissions to make this API call.

Before using any of the request data, make the following replacements: 

  * API_KEY: Your Google Cloud API key.
  * SKU_ID: The SKU identifier, which you can get using the [`skus.list` method](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest#rest-resource:-v2beta.skus). The ID is the string after the `skus/` identifier.
  * CURRENCY: (Optional) The ISO-4217 currency code for the price. If not specified, the price is in the same currency as your Cloud Billing account.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v1beta/skus/SKU_ID/price?key=API_KEY¤cyCode=CURRENCY

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         "https://cloudbilling.googleapis.com/v1beta/skus/SKU_ID/price?key=API_KEY¤cyCode=CURRENCY"

#### PowerShell

Execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v1beta/skus/SKU_ID/price?key=API_KEY¤cyCode=CURRENCY" | Select-Object -Expand Content

The following example shows the pricing details for the SKU ID `0012-B7F2-DD14`. 
    
    
    {
      "name": "skus/0012-B7F2-DD14/price",
      "currencyCode": "USD",
      "valueType": "rate",
      "rate": {
        "tiers": [
          {
            "startAmount": {
              "value": "0"
            },
            "listPrice": {
              "currencyCode": "USD",
              "nanos": 1397000
            }
          }
        ],
        "unitInfo": {
          "unit": "GiBy.h",
          "unitDescription": "gibibyte hour",
          "unitQuantity": {
            "value": "1"
          }
        },
        "aggregationInfo": {
          "level": "ACCOUNT",
          "interval": "MONTHLY"
        }
      }
    }
    

## Get information specific to your Cloud Billing account

The following examples show API calls that get information that is specific to your Cloud Billing account, such as specific SKUs, or pricing information that might be part of your custom pricing contract.

Depending on the API resource that you're using, you must have these permissions for the Cloud Billing account:

  * To get information about services using [`billingAccounts.services`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest#rest-resource:-v1beta.billingaccounts.services), you need:

    * `billing.billingAccountServices.get`
    * `billing.billingAccountServices.list`
  * To get information about SKUs using [`billingAccounts.skus`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest#rest-resource:-v1beta.billingaccounts.skus), you need:

    * `billing.billingAccountSkus.get`
    * `billing.billingAccountSkus.list`
  * To get information about SKU Groups using [`billingAccounts.skugroups`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest#rest-resource:-v1beta.billingaccounts.skugroups), you need:

    * `billing.billingAccountSkuGroups.get`
    * `billing.billingAccountSkuGroups.list`
  * To get information about SKUs that are part of SKU Groups using [`billingAccounts.skugroups.skus`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest#rest-resource:-v1beta.billingaccounts.skugroups.skus), you need:

    * `billing.billingAccountSkuGroupSkus.get`
    * `billing.billingAccountSkuGroupSkus.list`
  * To get information about SKU prices using [`billingAccounts.skus.price`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest#rest-resource:-v1beta.billingaccounts.skus.price), you need:

    * `billing.billingAccountPrice.get`



If you're calling the API using a service account, the service account must have the permissions.

The following predefined roles have the permissions to get information specific to your Cloud Billing account:

  * Billing Account Administrator
  * Billing Account Viewer



### Get a list of SKU groups for your Cloud Billing account

If you have a pricing contract with Google Cloud, your contract might refer to _SKU groups_ , which contain SKUs that fall into a specific category. For example, the [BigQuery](https://docs.cloud.google.com/skus/sku-groups/bigquery) SKU group contains SKUs for BigQuery analysis and storage in various locations.

The following example lists the SKU groups that are available to your Cloud Billing account.

To make this API call, you need the `billing.billingAccountSkuGroups.list` IAM permission on your Cloud Billing account.

Before using any of the request data, make the following replacements: 

  * BILLING_ACCOUNT_ID: Your Cloud Billing account ID.
  * PAGE_SIZE (Optional): The maximum number of SKU groups to return. The default is 50, and the maximum is 5000.
  * PAGE_TOKEN (Optional): The page token, which is in `nextPageToken` in the response.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skuGroups?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skuGroups?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skuGroups?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

The response is a list of SKU groups, in the format shown below.

The results are paginated, and are limited to 50 SKU groups per page. The response includes a `nextPageToken` that you can use to get the next page of results. To fetch the next batch, set `pageToken=PAGE_TOKEN`. To reduce the number of SKUs per page, set `pageSize=PAGE_SIZE`. When all items have been listed, no token is returned. 
    
    
    {
        "billingAccountSkuGroups": [
          {
            "name": "billingAccounts/012345-567890-ABCDEF/skuGroups/001234-group-id-1",
            "displayName": "SKU group name 1"
          },
          {
            "name": "billingAccounts/012345-567890-ABCDEF/skuGroups/0045657-group-id-2",
            "displayName": "SKU group name 2"
          },
          ...
          "nextPageToken": "A1234-alphanumeric-page-token"
    }
    

### Get a list of SKUs in a SKU group for your Cloud Billing account

The following example lists the SKUs in a SKU group that might be part of your custom pricing contract.

To make this API call, you need the `billing.billingAccountSkuGroupSkus.list` IAM permission on your Cloud Billing account.

Before using any of the request data, make the following replacements: 

  * SKU_GROUP_ID: The SKU group ID, which you get from the [`billingAccount.skuGroups.list method`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skuGroups/list).
  * BILLING_ACCOUNT_ID: Your Cloud Billing account ID.
  * PAGE_SIZE (Optional): The number of SKU groups to get. The default is 5000.
  * PAGE_TOKEN (Optional): The page token, which is in `nextPageToken` in the response.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skuGroups/SKU_GROUP_ID/skus?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skuGroups/SKU_GROUP_ID/skus?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skuGroups/SKU_GROUP_ID/skus?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

The following example shows the first 2 SKUs for the `Network Data Transfer` SKU group, with the ID `28934b47-792e-4afa-a025-7720d410482f`.

The results are paginated, and are limited to 5000 SKU groups per page. The response includes a `nextPageToken` that you can use to get the next page of results. To fetch the next batch, set `pageToken=PAGE_TOKEN`. To reduce the number of SKUs per page, set `pageSize=PAGE_SIZE`. When all items have been listed, no token is returned. 
    
    
    {
      "billingAccountSkuGroupSkus": [
        {
          "name": "billingAccounts/12345-ABCDE-EXAMPLE/skuGroups/28934b47-792e-4afa-a025-7720d410482f/skus/0009-6F35-3126",
          "skuId": "0009-6F35-3126",
          "displayName": "Network Internet Data Transfer from EMEA to Seoul",
          "service": "9662-B51E-5089",
          "productTaxonomy": {
            "taxonomyCategories": [
              {
                "category": "GCP"
              },
              {
                "category": "Network"
              },
              {
                "category": "Data Transfer"
              },
              {
                "category": "Cloud SQL"
              },
              {
                "category": "Premium"
              }
            ]
          },
          "geoTaxonomy": {
            "type": "REGIONAL",
            "regionalMetadata": {
              "region": {
                "region": "europe-west1"
              }
            }
          }
        },
        {
          "name": "billingAccounts/12345-ABCDE-EXAMPLE/skuGroups/28934b47-792e-4afa-a025-7720d410482f/skus/000B-47CC-2924",
          "skuId": "000B-47CC-2924",
          "displayName": "API Gateway Network Internet Data Transfer Intercontinental from/to Oceania",
          "service": "36A9-155B-23F0",
          "productTaxonomy": {
            "taxonomyCategories": [
              {
                "category": "GCP"
              },
              {
                "category": "Network"
              },
              {
                "category": "Data Transfer"
              },
              {
                "category": "API Gateway"
              },
              {
                "category": "Premium"
              }
            ]
          },
          "geoTaxonomy": {}
        }
      ],
      "nextPageToken": "alphanumeric-nextPageToken"
    }
    

### Get the prices for all Google Cloud SKUs for your Cloud Billing account

Before using any of the request data, make the following replacements: 

  * SKU_ID: A specific SKU ID to get the price for. To get prices for all SKUs, use `-`. 
  * API_KEY: Your Google Cloud API key.
  * PAGE_SIZE (Optional): The number of services to return. The default is 50.
  * PAGE_TOKEN (Optional): The page token, which you get from the `nextPageToken` in an earlier response.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skus/SKU_ID/prices?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skus/SKU_ID/prices?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skus/SKU_ID/prices?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

The response contains a list of SKU IDs and their prices, including SKUs that are only available to your Cloud Billing account, and pricing information for each SKU. The example below shows the format for all SKUs, with a page size of `2`.

The results are paginated, and by default, contain 50 prices per page. The response includes a `nextPageToken` that you can use to get the next page of results. To fetch the next batch, set `pageToken=PAGE_TOKEN`. To change the number of results per page, set `pageSize=PAGE_SIZE`. When all items have been listed, no token is returned. 
    
    
    {
      "billingAccountPrices": [
        {
          "name": "billingAccounts/01ABCD-EFGH23-UVWXYZ/skus/0000-9B70-F099/price",
          "currencyCode": "USD",
          "valueType": "rate",
          "rate": {
            "tiers": [
              {
                "startAmount": {
                  "value": "0"
                },
                "listPrice": {
                  "currencyCode": "USD",
                  "nanos": 690000000
                },
                "contractPrice": {
                  "currencyCode": "USD",
                  "nanos": 690000000
                },
                "effectiveDiscountPercent": {
                  "value": "0"
                }
              }
            ],
            "unitInfo": {
              "unit": "h",
              "unitDescription": "hour",
              "unitQuantity": {
                "value": "1"
              }
            },
            "aggregationInfo": {
              "level": "LEVEL_ACCOUNT",
              "interval": "INTERVAL_MONTHLY"
            }
          },
          "priceReason": {
            "type": "default-price",
            "defaultPrice": {}
          }
        },
        {
          "name": "billingAccounts/01ABCD-EFGH23-UVWXYZ/skus/0002-17F9-0731/price",
          "currencyCode": "USD",
          "valueType": "rate",
          "rate": {
            "tiers": [
              {
                "startAmount": {
                  "value": "0"
                },
                "listPrice": {
                  "currencyCode": "USD"
                },
                "contractPrice": {
                  "currencyCode": "USD"
                },
                "effectiveDiscountPercent": {
                  "value": "0"
                }
              },
              {
                "startAmount": {
                  "value": "1"
                },
                "listPrice": {
                  "currencyCode": "USD",
                  "nanos": 390000000
                },
                "contractPrice": {
                  "currencyCode": "USD",
                  "nanos": 390000000
                },
                "effectiveDiscountPercent": {
                  "value": "0"
                }
              },
              {
                "startAmount": {
                  "value": "1024"
                },
                "listPrice": {
                  "currencyCode": "USD",
                  "nanos": 340000000
                },
                "contractPrice": {
                  "currencyCode": "USD",
                  "nanos": 340000000
                },
                "effectiveDiscountPercent": {
                  "value": "0"
                }
              }
            ],
            "unitInfo": {
              "unit": "GiBy.mo",
              "unitDescription": "gibibyte month",
              "unitQuantity": {
                "value": "1"
              }
            },
            "aggregationInfo": {
              "level": "LEVEL_ACCOUNT",
              "interval": "INTERVAL_MONTHLY"
            }
          },
          "priceReason": {
            "type": "default-price",
            "defaultPrice": {}
          }
        }
      ],
      "nextPageToken": "1234alphanumericCode"
    }
    

### Get the prices for SKUs for your Cloud Billing account

The following example gets the price that you're paying for a SKU. If the SKU is part of a custom pricing contract, the response includes information about the discount on the list price.

To make this API call, you need the `billing.billingAccountPrice.get` IAM permission on your Cloud Billing account.

**Note:** The API supports prices that are based on usage rates. If you make the API call with a SKU that has a different pricing model, you get a `404` error.

Before using any of the request data, make the following replacements: 

  * SKU_ID: The SKU identifier, which you can get using the [`billingAccounts.skus` method](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#BillingAccountSku). The ID is the string after the `skus/` identifier.
  * BILLING_ACCOUNT_ID: Your Cloud Billing account ID.
  * CURRENCY: (Optional) The ISO-4217 currency code for the price. If not specified, the price is in the same currency as your Cloud Billing account.



HTTP method and URL: 
    
    
    GET https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skus/SKU_ID/price?currencyCode=CURRENCY

To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skus/SKU_ID/price?currencyCode=CURRENCY"

#### PowerShell

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudbilling.googleapis.com/v1beta/billingAccounts/BILLING_ACCOUNT_ID/skus/SKU_ID/price?currencyCode=CURRENCY" | Select-Object -Expand Content

The response contains details about how you're charged for the SKU, in the [`priceReason`](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus.price#PriceReason) object. The following example shows the pricing details for the SKU ID `0012-B7F2-DD14`. In this example, the Cloud Billing account has a pricing contract, but is paying the list price for this SKU. 
    
    
    {
      "name": "billingAccounts/015978-D9414D-B80267/skus/0012-B7F2-DD14/price",
      "currencyCode": "USD",
      "valueType": "rate",
      "rate": {
        "tiers": [
          {
            "startAmount": {
              "value": "0"
            },
            "listPrice": {
              "currencyCode": "USD",
              "nanos": 1270000
            },
            "contractPrice": {
              "currencyCode": "USD",
              "nanos": 1270000
            }
          }
        ],
        "unitInfo": {
          "unit": "GiBy.h",
          "unitDescription": "gibibyte hour",
          "unitQuantity": {
            "value": "1"
          }
        },
        "aggregationInfo": {
          "level": "ACCOUNT",
          "interval": "MONTHLY"
        }
      },
      "priceReason": {
        "type": "default-price",
        "defaultPrice": {}
      }
    }
    

## Related topics

  * [Read the API reference](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest) .

  * [Export your Cloud Billing pricing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)

  * [View and download your price lists in the pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)

  * [Get detailed information about public Google Cloud SKUs](https://docs.cloud.google.com/skus).

  * [Get detailed information about public Google Cloud SKU groups](https://docs.cloud.google.com/skus/sku-groups)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
