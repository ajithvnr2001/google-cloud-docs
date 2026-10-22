---
url: https://docs.cloud.google.com/channel/docs/concepts/workspace/products-skus/
title: Google Workspace products, SKUs, and plans \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:23.252700+00:00
---

# Google Workspace products, SKUs, and plans  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/concepts/workspace/products-skus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Google Workspace products, SKUs, and plans Stay organized with collections  Save and categorize content based on your preferences. 

## Plans

Several payment plans are available, including:

  * Annual/Monthly: Annual commitment with monthly, post-paid payments
  * Annual/Yearly: Annual commitment with yearly pre-payment
  * Flexible: Non-commitment plan with post-paid monthly payments
  * Perpetual: One-time, non-recurring payment
  * Free trial plan 
    * Trial length is variable up to a maximum of 30 days.



For more information on these plans, see our page on [Choosing a payment plan for your customers](https://support.google.com/channelservices/answer/9548930).

**Key Point:** These plans do not define the billing relationship between a reseller and their customers. Resellers define their own billing terms with their customers.

## Products and SKUs

The Cloud Channel API supports the following Google Workspace and Chrome Enterprise products and their related Stock Keeping Units (SKUs).

### Google Chrome SKUs

Google Chrome Enterprise provides the OS, browser, and devices your business needs to cloud-power your workforce.  
For more information, visit the [Chrome Enterprise site](https://chromeenterprise.google/).

Google Chrome Enterprise includes the following SKUs:

  * Chrome Enterprise Upgrade (Annual)
  * Chrome Enterprise Upgrade (Perpetual)
  * Chrome Education Upgrade (Perpetual)
  * Chrome Non-profit Upgrade (Perpetual)



### Google Workspace SKUs

Google Workspace offers a rich suite of business-grade hosted email and collaboration tools that can benefit organizations of any size.  
For more information, see the [benefits of Google Workspace](https://workspace.google.com/).

Google Workspace includes the following core SKUs:

  * Business Starter
  * Business Standard
  * Business Plus
  * Enterprise Standard
  * Enterprise Plus
  * Enterprise Essentials (only available as an `ANNUAL_MONTHLY` plan)



Google Workspace also includes these add-on SKUs:

  * Enterprise Archived User
  * Google Drive Storage
  * Google Vault



### Cloud Identity SKUs

Cloud Identity is a unified identity, access, app, and endpoint management (IAM/EMM) platform. For more information, see [the Cloud Identity site](https://docs.cloud.google.com/identity).

Cloud Identity includes the following SKUs:

  * Cloud Identity Free
  * Cloud Identity Premium



## Upgrades and Downgrades

  * For new customers, create a new entitlement with the [entitlements.create](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create) method.

  * You can upgrade an entitlement using the [entitlements.changeOffer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/changeOffer) method with an offer for the SKU that you want to upgrade to. It isn't possible to upgrade Annual/Yearly subscriptions, but you can switch to Flexible using the [entitlements.changeRenewalSettings](https://docs.cloud.google.com/channel/docs/concepts/workspace/channel/docs/reference/rest/v1/accounts.customers.entitlements/changeRenewalSettings) method, then perform an adjustment after the renewal event.

  * You can downgrade an entitlement using the [entitlements.changeOffer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/changeOffer) method with an offer for the SKU that you want to downgrade to. It isn't possible to downgrade Annual/Monthly and Annual/Yearly entitlements during term, and it cannot be done via renewal settings: the downgrade must be done manually on or after renewal time. We recommend that you switch to Flexible via [entitlements.changeRenewalSettings](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/changeRenewalSettings), then perform an adjustment after the renewal event. See more details about downgrades on this [Help Center article](https://support.google.com/a/answer/6073179).

  * Transfer and SKU switch operations cannot be combined. For example, if you have a potential customer who is using Business Starter and wants to buy Enterprise Standard from you, you must transfer the customer first with the existing Business Starter SKU and then switch the SKU to Enterprise Standard.

  * Upgrades/downgrades start a new entitlement and terminates the previous one. For commit plans, a new commitment starts when the call to [entitlements.changeOffer](https://docs.cloud.google.com/channel/docs/concepts/workspace/channel/docs/reference/rest/v1/accounts.customers.entitlements/changeOffer) is made, and does not co-term with the existing entitlement.


**Caution:** Payment plans impact how upgrades and downgrades work. Read above for details.

### Upgrade/Downgrade matrix for G Suite SKUs

This matrix sums up acceptable upgrade and downgrade paths.

From ↓ to → | **G Suite Basic** | **G Suite Business**  
---|---|---  
**G Suite Basic** |  | Upgradeable  
**G Suite Business** | Downgradeable |   
  
### Upgrade/Downgrade matrix from G Suite SKUs to Google Workspace SKUs

This matrix sums up acceptable upgrade and downgrade paths.

From ↓ to → | **Business Starter** | **Business Standard** | **Business Plus** | **Enterprise Standard** | **Enterprise Plus**  
---|---|---|---|---|---  
**G Suite Basic** | Upgradeable | Upgradeable | Upgradeable | Upgradeable | Upgradeable  
**G Suite Business** | Downgradeable | Upgradeable | Upgradeable | Upgradeable | Upgradeable  
  
### Upgrade/Downgrade matrix for Google Workspace SKUs

This matrix sums up acceptable upgrade and downgrade paths.

From ↓ to → | **Business Starter** | **Business Standard** | **Business Plus** | **Enterprise Standard** | **Enterprise Plus**  
---|---|---|---|---|---  
**Business Starter** |  | Upgradeable | Upgradeable | Upgradeable | Upgradeable  
**Business Standard** | Downgradeable |  | Upgradeable | Upgradeable | Upgradeable  
**Business Plus** | Downgradeable | Downgradeable |  | Upgradeable | Upgradeable  
**Enterprise Standard** | Downgradeable* | Downgradeable* | Downgradeable* |  | Upgradeable  
**Enterprise Plus** | Downgradeable* | Downgradeable* | Downgradeable* | Downgradeable |   
**Enterprise Essentials** |  |  |  | Upgradeable** | Upgradeable**  
  
* Downgrade from Enterprise SKUs to Business SKUs is only allowed if the customer has 300 or fewer seats (in applicable regions).

** Upgrade from Enterprise Essentials to Enterprise Standard or Enterprise Plus is only permitted if the domain is verified.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
