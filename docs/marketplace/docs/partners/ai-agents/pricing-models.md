---
url: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models/
title: Pricing models for AI agents from Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:18.549091+00:00
---

# Pricing models for AI agents from Google Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Pricing models for AI agents from Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

For AI agents that you offer through Google Cloud Marketplace, you can choose from the following pricing models:

  * **Free** : Customers only pay for the Google Cloud resources that they use.
  * **Subscription-based pricing** : Customers pay a flat monthly fee for using your AI agent. For partial months, the cost is prorated.
  * **Usage-based pricing** : Customers pay for your AI agent based on measurements that you choose, called _metrics_. If you choose a usage-based pricing model, then your product must measure and report usage information to Google.
  * **Combined pricing** : Customers pay a base subscription fee for using your AI agent, and additional charges based on their usage.



For any pricing model you choose, you can also offer a free trial of your product.

Because pricing models take up to four business days to process, we recommend that you decide on a pricing model and [submit it for review](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing) before you complete the remaining technical integration steps.

If your pricing model includes any generic units that measure usage, you must include a list of all usage sub-metrics that might count towards consumption of the generic unit, and information about the conversion rate and pricing of each of those sub-metrics.

You can have up to 24 total pricing plans for each product. If your pricing model is based on usage, each plan can measure eight metrics. If you need more plans, or need to track more metrics, contact your Google Partner Engineer.

You can also create customized quotes for specific customers. For example, if you offer a subscription-based Standard plan for $100 per month, you can create a custom quote that gives your customer the same plan for $50 per month. For steps to create a custom quote, see [Creating private offers for specific customers](https://docs.cloud.google.com/marketplace/docs/partners/create-offers).

## Subscription-based pricing

In a subscription-based pricing model, customers are charged a flat monthly rate. For partial months, the price is prorated. You can use a subscription-based pricing model if you set your price by non-variable measurements, such as the number of seats of service.

You can offer your product with different sets of features and levels of service. For example, you might have Standard, Pro, and Enterprise plans for your product, with progressively advanced features. You define the service levels that you plan to offer when you [submit your pricing for review](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing).

By default, you set up subscription plans with monthly billing. Optionally, your plans can include a customized _subscription period_ , where you can offer users a different price if they sign up for a specific time period, such as a year. If users choose a monthly plan, then their subscription automatically renews at the end of every month. However, if your customers sign up for the customized subscription period, then their subscription ends at the end of that period, and they must subscribe to your product again.

In a subscription-based pricing model, if customers want to make changes to their plans, then the effect and timing of those changes depends on their current subscription plan:

  * For monthly subscriptions, customers can upgrade or downgrade between service levels, or cancel their subscription entirely. By default, customer-canceled subscriptions terminate at the end of the current billing month.

  * If your customers sign up for a specific subscription period, then they can change their subscription plan to increase their service level or subscription period, such as:

    * Switch from a shorter subscription period to a longer period, within the same service level. For example, customers can switch from a Standard monthly plan to a Standard 1-year plan.

    * Upgrade from a lower to a higher service level, with the same or a longer subscription period. For example, customers can upgrade from a Standard 1-year plan to a Pro 1-year plan.

    * A combination of both of the previously described options.

In these scenarios, customers switch to their new plan immediately.

  * If customers have signed up for a specific subscription period and then shorten their subscription period, downgrade to a lower service level, or cancel their subscription, the change takes effect at the end of their current subscription period. For example, if a customer is on a Standard 1-year plan and wants to switch to a Standard monthly plan, the change takes effect after the one year is complete.




To set up subscription-based pricing, you must provide the subscription plans that you offer, such as Standard or Enterprise, and the features that are included in those plans. For example, the following pricing model offers three subscription plans, with access to different features in each plan:

Standard | Pro | Enterprise  
---|---|---  
$9.99 / month | $39.99 / month | $99.99 / month  
Features:

  * Unlimited calls
  * Access to Admin Console

|  Features:

  * Unlimited calls
  * Access to Admin Console
  * Multiple logins
  * Security

|  Features:

  * Unlimited calls
  * Access to Admin Console
  * Multiple logins
  * Security

  
  
The following pricing model modifies the previous example, adding discounted prices if customers sign up for one-year or three-year subscriptions.

Standard | Pro | Enterprise  
---|---|---  
  
  * Monthly subscription: $9.99 / month
  * One-year subscription: $7.49 / month
  * Three-year subscription: $5.99 / month

| 

  * Monthly subscription: $39.99 / month
  * One-year subscription: $29.99 / month
  * Three-year subscription: $19.99 / month

| 

  * Monthly subscription: $99.99 / month
  * One-year subscription: $89.99 / month
  * Three-year subscription: $74.99 / month

  
Features:

  * Unlimited calls
  * Access to Admin Console

|  Features:

  * Unlimited calls
  * Access to Admin Console
  * Multiple logins
  * Security

|  Features:

  * Unlimited calls
  * Access to Admin Console
  * Multiple logins
  * Security

  
  
## Usage-based pricing

You can charge your customers using measurements that apply to your product, called _metrics_. A typical example of a metric is the time for which customers use your product. For example, you can charge $0.05 per hour of use. Similarly, you can charge customers by the quantity of data processed by your product, or by the number of API requests that customers make.

While you are choosing your metrics, you must also choose a _reporting unit_ for each metric, which represents the granularity with which you measure your product's usage.

For example, consider a product for which you charge $0.256 per gibibyte (1024 mebibytes) of data processed, and your reporting unit is by mebibyte. If a user processes 512 mebibytes of data, they are charged `(512 Mib / 1024 MiB) * $0.256`, or **$0.128** , for their usage. However, if your reporting unit is by gibibyte, the customer's usage is reported as `1 GiB`, and they are charged the full $0.256, even if they only use a fraction of a gibibyte.

The following table includes examples of the types of metrics that you can use, and the reporting units that we recommend:

**Metric type** | **Supported units** | **Recommended reporting unit** | **Example price, shown on your Cloud Marketplace page**  
---|---|---|---  
Time | Second, minute, hour, day | 1 second (smallest possible) | $5 per **hour**  
Data processed |  Byte, Kibibyte (KiB), Mebibyte (MiB), Gibibyte (GiB) The units for data processed are based on binary multiples, where one kibibyte is 1024 bytes, one mebibyte is 1024 kibibytes, and one gibibyte is 1024 mebibytes. | 1 Mebibyte | $10 per **GiB**  
Storage time | _See units for time and data_ | 1 Mebibyte-second | $10 per **GiB-hour**  
Custom metric | N/A. You define the unit you want to measure, such as **API request**. | Depends on metric. | $10 per **1000 API requests**  
  
If you want to charge by a custom metric, ensure that the measurement is a _delta_ metric, where each usage report represents the change in the value since the previous report. For example, you can set a price per email, and every hourly usage report represents the number of emails sent in the previous hour.

### Defining your pricing structure

For usage-based pricing, you select one of the following options:

  * **Single rate** : Customers pay a set price for their usage, and the charges increase in direct proportion to their usage. For example, if you charge $0.50 per hour of usage, and a customer uses your product for 20 hours, they are charged $10.

The following is an example pricing model with three pricing plans, each with on-demand pricing and a different set of features:

Standard | Pro | Enterprise  
---|---|---  
$0.002 per email sent | $0.004 per email sent | $0.006 per email sent  
Features:
    * Access to Admin Console
| Features:
    * Access to Admin Console
    * Multiple logins
    * Security
| Features:
    * Access to Admin Console
    * Multiple logins
    * Security  
  * **Tiered pricing** : If you want to give customers discounts for continued usage, you can create pricing tiers. The tiers apply over the course of a billing month. At the start of a new billing month, the price is reset to the first tier. You can define tiers for each metric that you base your price on.

The following is an example of a pricing model with three pricing plans, each with tiered pricing:

Standard | Pro | Enterprise  
---|---|---  
    * $0.002 per email sent for 0-1000 emails
    * $0.001 per email sent for 1001-2000 emails
    * $0.0001 per email sent for 2001+ emails
| 
    * $0.005 per email sent for 0-1000 emails
    * $0.004 per email sent for 1001-2000 emails
    * $0.002 per email sent for 2001+ emails
| 
    * $0.008 per email sent for 0-1000 emails
    * $0.006 per email sent for 1001-2000 emails
    * $0.003 per email sent for 2001+ emails  
Features:
    * Access to Admin Console
| Features:
    * Access to Admin Console
    * Multiple logins
    * Security
| Features:
    * Access to Admin Console
    * Multiple logins
    * Security  
  
When a new billing month starts, the price is reset to the first tier.

You can define separate sets of tiers for each metric that you base your price on.




## Combined pricing

In a combined pricing model, customers pay a base subscription fee for using your software, and additional charges based on their usage. You can include a specific quantity of usage in your base fee. For example, the following pricing model has base subscription plans that include a number of API requests, and additional charges as customers increase their usage:

Standard | Pro | Enterprise  
---|---|---  
$9.99 / month subscription fee $0 per request for 1000 API requests $0.002 per request for 1000+ API requests | $39.99 / month subscription fee $0 per request for 2000 API requests $0.005 per request for 2000+ API requests | $99.99 / month subscription fee $0 per request for 10000 API requests $0.008 per request for 10000+ API requests  
Features: 

  * Access to Admin Console

| Features: 

  * Access to Admin Console
  * Multiple logins
  * Security

| Features: 

  * Access to Admin Console
  * Multiple logins
  * Security

  
  
## Offering trial software (Optional)

The process to offer a free trial of your software to Google Cloud users involves using Producer Portal to specify:

  * The trial period, in days (for example, 30 days).
  * The trial credit amount, in US dollars (for example, US$100).



Customers can choose any of your pricing plans, and the trial credit applies to the plan that they choose.

The trial ends when the customer reaches the credit limit or at the end of the trial period, whichever comes first. For example, if you offer a 15-day trial with a maximum credit of $100, the trial ends when users reach the $100 limit or at the end of 15 days.

At the end of the trial period, customers pay based on the pricing plan they chose. If the customer changed their plan during the trial, they pay based on their new plan.

If your product's pricing is usage-based, we recommend a trial credit limit that is twice the cost of the usage that you expect.

### Before you begin

Before you can create a free trial, you must have the following:

  * Access to Producer Portal, which requires: 
    * A signed [Marketplace vendor agreement](https://cloud.google.com/terms/marketplace-vendor-agreement?e=48754805).
    * An approved [Solution Validation form](https://docs.google.com/forms/d/e/1FAIpQLSesllyRR-HvLFZthYA8Cv4nQRUTOthHGgs-76DY9o2IntUL3A/viewform).
    * A complete [Cloud Marketplace Project Info Form](https://docs.google.com/forms/d/e/1FAIpQLSfddn4mwKnqtLNQ-m7IgRZ-bgTz4BOsrEDWCf3XBjc_ogKNnA/viewform) from the Google Cloud Marketplace team.
  * An approved pricing review, as described in [Submitting your pricing for review](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing#submit-pricing).



The direct link to Producer Portal is: 
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link or can't access the URL, verify that you have completed the prerequisites to gain access to the Producer Portal and selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

### Create a free trial

  1. In the **Producer Portal** , go to the **Overview** section.
  2. In the **Free trial** section, click **EDIT**.
  3. On the **Google Cloud Marketplace free trial** page, click **CONFIGURE TRIAL**.
  4. On the **Configure Free trial** dialog, set the following values:

Field name | Value  
---|---  
**Trial duration** | Number of days for the duration of the trial. The minimum allowed value is `5`.  
**Trial credit amount** | The credit amount in USD that your customer can use during the free trial. The minimum allowed value is `50`.  
  5. Click **CONFIRM**.

If successful, the message _Free trial configured_ appears, and the free trial status updates to show _Free trial active_.

  6. In the **Publish** section, click **PUBLISH** for your changes to take effect for your customers.




### Disable a free trial

  1. In the **Producer Portal** , go to the **Overview** section.
  2. In the **Free trial** section, click **EDIT**.
  3. On the **Google Cloud Marketplace free trial** page, click **DISABLE TRIAL**.
  4. On the **Disable Free trial** dialog, click **DISABLE** to confirm your choice.

If successful, the message _Free trial disabled_ appears, and the free trial status updates to show _Free trial inactive_.

  5. In the **Publish** section, click **PUBLISH** for your changes to take effect for your customers.


**Note:** Disabling the free trial will only affect new orders from customers, not existing orders.

## What's next

  * Learn about [offering AI agents through Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents).
  * [Add pricing information](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing) to your AI agent's Cloud Marketplace listing.



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents)

[ Next Add your AI agent  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/add-product)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
