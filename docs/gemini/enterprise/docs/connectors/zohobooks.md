---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohobooks/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:43:18.246765+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohobooks/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The Zoho Books connector for Gemini Enterprise lets you search, read, and perform write operations on your Zoho Books items, contacts, invoices, sales orders, estimates, purchase orders, and customer payments using natural language.

## Supported actions

When the Zoho Books connector is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create Contact | Create a new contact in zohobooks.  
Create Customer Payment | Create a new customer payment in zohobooks.  
Create Estimate | Create a new estimate in zohobooks.  
Create Invoice | Create a new invoice in zohobooks.  
Create Item | Create a new item in zohobooks.  
Create Purchase Order | Create a new purchase order in zohobooks.  
Create Sales Order | Create a new sales order in zohobooks.  
Create Tax | Create a new tax in zohobooks.  
Update Contact | Update an existing contact in zohobooks.  
Update Estimate | Update an existing estimate in zohobooks.  
Update Invoice | Update an existing invoice in zohobooks.  
Update Item | Update an existing item in zohobooks.  
Update Purchase Order | Update an existing purchase order in zohobooks.  
Update Sales Order | Update an existing sales order in zohobooks.  
**Note:** Additional read-only actions are also available.

## Limitations

The Zoho Books data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Zoho Books data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Zoho Books data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a data store with Zoho Books, see [Set up a Zoho Books data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohobooks/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
