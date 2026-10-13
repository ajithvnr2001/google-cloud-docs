---
url: https://docs.cloud.google.com/oracle/database/docs/purchase-and-billing/
title: Purchase and billing \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:08.137811+00:00
---

# Purchase and billing  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/purchase-and-billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Purchase and billing Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the purchase and billing process for Oracle Database@Google Cloud, and how to view and manage your expenses using the Google Cloud console.

## Choose an offer type

Oracle Database@Google Cloud provides the following offer types. The offer type you select determines how you're billed.

Offer type | What it is | How billing works  
---|---|---  
Public (Pay-As-You-Go) | The standard, on-demand pricing model. It's suitable for testing the service, or for workloads with fluctuating or short-term needs. | You're charged at the public list price for the resources you consume. For example, OCPUs per hour and storage per GB. These charges appear as line items in your Google Cloud invoice. This model requires an existing financial agreement with Google Cloud.  
Private | For customers with significant or long-term database requirements, a private offer lets you negotiate custom pricing and terms directly with the Oracle sales team. This can include discounts based on contract length, committed use discounts (CUDs), or the number of Exadata hardware deployments. | After you and Oracle agree on the terms, Oracle extends a private offer to you through the Google Cloud Marketplace. You then accept this offer, and the negotiated pricing is reflected on your Google Cloud invoice. This lets you benefit from custom pricing while maintaining the convenience of consolidated billing through Google Cloud.  
  
For more information, see How billing works. For information on pricing, see [Oracle Database@Google Cloud pricing](https://www.oracle.com/cloud/google/oracle-database-at-google-cloud/pricing/).

## Purchase and onboard

To purchase and onboard to Oracle Database@Google Cloud, follow these steps:

  1. After you choose an offer type, place an order through Cloud Marketplace.

[Go to Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/oracle/oracle-database-at-google-cloud)

  2. Complete the [Oracle onboarding tasks](https://docs.oracle.com/en-us/iaas/Content/database-at-gcp/oagcp-onboard.htm), which include creating a new Oracle Cloud Infrastructure (OCI) account or linking to an existing OCI account. This step links Oracle Database@Google Cloud to your OCI account so that you can use the services, manage resources and billing.




After you completed the onboarding tasks, you can [set up your Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment#deploy-odb-environment) and create resources.

## How billing works

Google Cloud manages billing. The billing process for Oracle Database@Google Cloud involves the following steps:

  1. **Usage metering:** as you use Oracle Database@Google Cloud services, Oracle meters the usage. Key metrics might include OCPU hours, storage consumption, or other service-specific units.
  2. **Usage data transfer to Google Cloud:** Oracle shares the aggregated billing data with [Cloud Billing](https://docs.cloud.google.com/billing/docs).

For information on pricing, see [Oracle Database@Google Cloud pricing](https://www.oracle.com/cloud/google/oracle-database-at-google-cloud/pricing/).

  3. **Invoice generation:** Cloud Billing consolidates your Google Cloud charges and OCI charges according to the pricing model of your active offer (public or private). The resulting charges are then added as distinct line items in your monthly Google Cloud invoice.




### Billing for prepaid private offers

If your private offer includes a one-time upfront charge for a fixed term or entitlement, then the billing process is as follows:

  * **One-time upfront charge:** Google Cloud processes a single charge to you upon your acceptance of the offer. This charge covers the agreed-upon fixed fee for the service duration or entitlement.

  * **Zero Dollar Line Items:** Because this is a prepaid offer, all subsequent cost line items related to this service in the Cloud Billing typically appear as $0.00. This is the expected behavior, reflecting that your initial payment covers your costs.

  * **Potential Overage Charges:** Future charges incur if your usage exceeds the capacity, limits, or duration defined within the fixed-fee, prepaid offer. Any such overage appears as new line items in the invoice, reflecting consumption beyond the prepaid entitlement.




This model provides predictable costs within the scope of the agreement, with additional charges applying only to usage surpassing the prepaid terms.

For more information, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

## View and manage your costs

You can monitor your Oracle Database@Google Cloud expenses directly within the Google Cloud console.

  * **Billing reports:** to view billing reports, go to the **Billing** section of the Google Cloud console.

[Go to Billing](https://console.cloud.google.com/billing)

**Note:** Google Cloud receives only aggregated billing data from OCI. To learn how to view detailed OCI charges, see [OCI cost analysis documentation](https://www.oracle.com/cloud/google/oracle-database-at-google-cloud/pricing/).
  * **Filtering and analysis:** the Google Cloud cost management tools let you filter and group expenses. You can analyze your Oracle costs by project, service, or other labels, enabling effective financial governance and cost optimization.

  * **Budgeting and alerts:** you can set budgets and create alerts for your Oracle Database@Google Cloud spending, and stay on top of your expenditures. For more information, see [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).




## What's next

  * [Set up Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment#deploy-odb-environment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
