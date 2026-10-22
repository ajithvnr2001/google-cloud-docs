---
url: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing/
title: Add your AI agent's pricing information \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:48.187830+00:00
---

# Add your AI agent's pricing information  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/choose-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Add your AI agent's pricing information Stay organized with collections  Save and categorize content based on your preferences. 

After you've added your AI agent in Producer Portal, use the **Pricing** tab in Producer Portal to complete the following steps:

  * Add pricing information for your AI agent's Google Cloud Marketplace listing.
  * Submit your AI agent's pricing information to Google for review. To publish your AI agent, you must have successfully completed the **Pricing** review.



Because pricing models take up to four business days to process, we recommend that you decide on a pricing model and submit it for review before you complete the remaining technical integration steps.

For details about the available pricing models for AI agents, see [Pricing models for AI agents](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models).

## Add pricing information in Producer Portal

To add your AI agent's pricing information, use [Producer Portal](https://console.cloud.google.com/producer-portal). In Producer Portal, select your AI agent and complete the following steps:

  1. On the **Overview** page of your product, go to the **Pricing** section.

  2. Click **Edit** , and then perform each of the following tasks.




### Define your pricing structures

For each pricing model that you want to support, create a name for your pricing plan and follow the steps to define the pricing structure.

After you define the pricing structures for all of the pricing models you want to support, click **Set up** to set up the pricing structures and continue on to the remaining features of the **Pricing** page. Setting up your pricing structures also unblocks the technical integration steps, so that you can add your pricing details and begin implementing and testing your integration in parallel.

#### Free

  1. In the **Pricing model** drop-down list, select **Free**.



#### Subscription-based pricing

  1. In the **Pricing model** drop-down list, select **Subscription only**.



#### Usage-based pricing

  1. In the **Pricing model** drop-down list, select **Usage-based only**.

  2. In the **Metrics** drop-down list, select **Add or update metrics** to add a metric.

  3. For each metric that you add, you must enter a **Display name** , a **Reporting unit** , and a **Display unit** , and then click either **Done** or **Add another metric**. The **Reporting unit** specifies how your metric tracks usage for billing, while the **Display unit** specifies how your metric's pricing is displayed. For example, you might want to charge your users by per second of usage, but display your product's price per hour to your customers.




#### Combined pricing

  1. In the **Pricing model** drop-down list, select **Subscription + usage**.

  2. In the **Metrics** drop-down list, select **Add or update metrics** to add a metric.

  3. For each metric that you add, you must enter a **Display name** , a **Reporting unit** , and a **Display unit** , and then click either **Done** or **Add another metric**. The **Reporting unit** specifies how your metric tracks usage for billing, while the **Display unit** specifies how your metric's pricing is displayed. For example, you might want to charge your users per second of usage, but display your product's price per hour to your customers.




### Adding pricing details for your pricing structures

After you define your pricing structures, you can add the pricing details for your pricing structures.

To add pricing details for the pricing structures you defined, navigate to the **Pricing** section of Producer Portal.

#### Subscription-based pricing and combined pricing

For subscription-based pricing models, and for subscription-based elements of combined pricing models:

  1. Click **Edit subscription fees**.

  2. Enter your price in the **Price** field.

  3. Click **Done**.




#### Usage-based pricing and combined pricing

For usage-based pricing models, and for usage-based elements of combined pricing models:

  1. Click **Edit usage**.

  2. For single-rate pricing, add a **Display quantity** and a **Price**.

  3. For tiered pricing, enter a **Display quantity** , and click **Add tier** for each additional tier that you would like to add. Once you see the correct number of tiers, add a **Price** , and a lower limit for the tier in the **From** field. The upper limit for each tier is updated when you add the lower limit of the next tier.

  4. Click **Done**.




### Best practices for defining pricing

For best results when defining pricing, consider the following best practices:

  * Give your plans names that directly reflect what they offer. Avoid generic terms, such as "test plan" or "new plan".
  * Keep your plans' names under 58 characters. You can use hyphens (`-`) and spaces, but not other special characters.
  * Don't define your pricing as $0. When you define private subscription plans, use only non-zero values.
  * Use names that are clear for customers to understand for your metering units and reporting units. Avoid generic terms, like "unit" or "token".
  * Don't include separate line items for professional services (setup, support, maintenance) or hardware.
  * Don't offer "proof of concept" free plans.
  * Your products must be production-ready, and not alpha or beta versions.
  * Your pricing plans must each have at least one defined feature. Feature names can be up to 128 characters long.



### Add features to your plans

After you add your pricing details, you can add features to specific plans by using the **Features** tab of the **Pricing details** section. For each combination of a feature and a plan, you can choose **Yes** , **No** , **N/A** , or input a custom value, to indicate the level of support for that feature by the plan.

### Answer tax category questions

After you add features to your pricing plans, you use the **Tax category** tab of the **Pricing details** section to answer questions about your product.

Your answers to these questions help Google categorize your product for tax purposes. This information is captured to ensure accurate withholding and reporting on your earned income.

### Adding an end user license agreement (EULA)

Add an end user license agreement (EULA) in the **Terms & Policies** tab. We recommend that you use the Google standard EULA if your product allows it. This may help users adopt your product more quickly.

If your product requires a specialized EULA, add your EULA's URL to the **EULA URL** field.

### Submit your pricing model for review

When you're ready to submit your pricing model for processing, click **Submit**.

You can't modify your pricing model while it's under review.

## Update the price of products after launch

If it's been at least 30 days after your pricing model has been published and approved, you can update the price of your product. To update the price of your product, use [Producer Portal](https://console.cloud.google.com/producer-portal). In Producer Portal, complete the following steps:

  1. In the list of products, click the name of your product.
  2. Go to the pricing section of your product.
  3. Click **Edit content**.
  4. Make your updates to your pricing.
  5. When you're done, click **Submit price model**.



Your product's price is updated after the new pricing is reviewed and approved.

Price updates take up to four business days to be reviewed and take effect. If you're decreasing your price, your price decrease doesn't require any additional waiting period. If you're increasing your price, it takes an additional 45 days for the price increase to take effect after the Operations team confirms that they've received your request. This time window includes 15 days to draft and send a message to active users, and 30 days for users to review the price change.

**Note:** Sometimes, Google changes the questions that we ask in the **Tax category** section of Producer Portal. If we've changed the questions since the last time you submitted your product's pricing for review, then when you update your product's pricing, you must re-review the **Tax category** questions and adjust your answers as needed.

## Delete a pricing plan

If you want to delete a pricing plan in Producer Portal, you must make sure that it has no entitlements associated with it, including both active and cancelled entitlements. This means that you can't delete a pricing plan on your own if it has previously been purchased.

To delete a plan that has entitlements associated with it, contact your Google Partner Engineer.

## What's next

  * Review the available [pricing models for AI agents](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/pricing-models).
  * [Add your AI agent's Agent Card](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/agent-card) in Producer Portal.



[ Previous arrow_back  Update existing AI agent listings for enhanced discovery  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/update-ai-agent-listing)

[ Next Add your Agent Card  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents/agent-card)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
