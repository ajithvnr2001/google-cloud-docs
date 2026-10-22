---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:57.396623+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The Shopify connector for Gemini Enterprise lets you perform create, update, and read operations on Shopify.

## Supported Shopify versions

The Shopify connector supports the latest cloud version of Shopify.

## Supported actions

When the Shopify connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create customer | Creates a new customer in Shopify.  
Update customer | Updates an existing customer in Shopify.  
Create order | Creates a new order in Shopify.  
Send fulfillment request | Sends a fulfillment request for an order on your Shopify site.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search using the Shopify data store, you need to enable following scopes:

Scope | Purpose  
---|---  
`read_customers` | Retrieve customer profiles, contact info, and history.  
`write_customers` | Create or update customer profiles.  
`read_orders` | View full order details (transactions, items, and status).  
`write_orders` | Create an order.  
`read_products` | View product and product variant information.  
`read_fulfillments` | View fulfillments and fulfillment services.  
`read_assigned_fulfillment_orders` | View fulfillment orders, including their fulfillment order IDs.  
`write_assigned_fulfillment_orders` | Send a fulfillment request for an order on your Shopify site.  
  
For information on how to configure these scopes, see [Set redirect URL and scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify/shopify-configuration#set-redirect-url-and-scopes).

## Limitations

This section outlines known issues and limitations that may affect your use of the Shopify data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Shopify data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Shopify data store is supported only in the `global`, `us`, and `eu` locations.


  * The **Send fulfillment request** action acts on a fulfillment order, not on an order. Shopify accepts the request only if the fulfillment order is assigned to a third-party fulfillment service. Fulfillment orders that you fulfill yourself aren't supported.



## What's next

  * To create and configure a connector with Shopify, see [Set up a Shopify data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
