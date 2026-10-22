---
url: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/select-pricing/
title: Choosing a pricing model \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:23.966120+00:00
---

# Choosing a pricing model  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/select-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Choosing a pricing model Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about the pricing models you can choose for Kubernetes apps, and about submitting your pricing plan structure for review.

You can choose one of the following pricing models for your product:

  * **Free** : Customers only pay for the Google Cloud resources that they use, such as the cost for running Google Kubernetes Engine clusters. If you're offering your app free of charge, skip to Add your pricing model to Producer Portal.

  * **Bring your own license (BYOL)**: Customers pay you for the app directly, and are billed separately for the Google Cloud resources that they use. You're responsible for making sure that your customers are using a valid license for your app.

  * **Usage-based pricing**: Customers pay for your software based on measurements that you choose, called _metrics_ , such as the number of containers they run your app on.




If you choose usage-based pricing, you can also offer a free trial of your product. If you want to offer free trials with a BYOL pricing model, you must implement the trial license in your billing system.

After you have decided on your pricing model and set up your pricing plans, add it to your product in the portal so that it can be processed.

You can also create customized quotes for specific customers. For example, if you offer a usage-based plan for $5 per running container, you can create a custom quote that gives your customer the same plan for $2 per running container. For steps to create a custom quote, see [Creating custom quotes](https://docs.cloud.google.com/marketplace/docs/partners/create-quotes).

## Bring your own license (BYOL) pricing

If you want to bill customers yourself, you can choose a Bring your own license (BYOL) pricing model. You must provide a way for your customers to get a licence from you, typically through a website. After the customer gets their license, you are responsible for validating the license in your app.

If you want to use a BYOL pricing model, skip to Adding your pricing model in Producer Portal.

## Usage-based pricing

Kubernetes apps are priced by usage, so customers pay for your software based on measurements that you choose, called _metrics_ , such as the number of containers or storage time. A typical example of a metric is the time for which customers use your product. For example, you can charge $0.05 per hour of use. Similarly, you can charge customers by the quantity of data processed by your app, the number of API requests customers make, and so on.

While you are choosing your metrics, you must also choose a _reporting unit_ for each metric, which represents the granularity with which you measure your app's usage. By default, you must measure the reporting unit as an integer, and not as a fractional number.

For example, consider an app for which you charge $0.256 per gibibyte (1024 mebibytes) of data processed, and your reporting unit is by mebibyte. If a user processes 512 mebibytes of data, they are charged `(512 Mib / 1024 MiB) * $0.256`, or **$0.128** for their usage. However, if your reporting unit is by gibibyte, the customer's usage is reported as `1 GiB`, and they are charged the full $0.256 even if they use a fraction of a gibibyte.

The following table includes examples of the types of metrics you can use and the recommended reporting units:

**Metric type** | **Supported units** | **Recommended reporting unit** | **Example price**  
---|---|---|---  
Time | Second, minute, hour, day | 1 second (smallest possible) | $5 per **hour**  
Data processed |  Byte, Kibibyte (KiB), Mebibyte (MiB), Gibibyte (GiB) The units for data processed are based on binary multiples, where one Kibibyte is 1024 bytes, one Mebibyte is 1024 Kibibytes, and so on. | 1 Mebibyte (MiB) | $10 per **GiB**  
Storage time | _See units for time and data_ | 1 Mebibyte-second | $10 per **GiB-hour**  
Custom metric | N/A. You define the unit you want to measure, such as **API request**. | Depends on metric. | $10 per **1000 API requests**  
  
If you want to charge by a custom metric, ensure that the measurement is a _delta_ metric, where each usage report represents the change in the value since the previous report. For example, you can set a price per email, and every hourly usage report represents the number of emails sent in the previous hour.

### Define your pricing structure

After you have selected your metrics, you can select one of the following pricing structures:

  * **Single-rate pricing** : Customers pay a set price for their usage, and the charges increase in direct proportion to their usage. For example, if you charge $0.50 per hour of usage, and a customer uses your app for 20 hours, they are charged $10.

  * **Tiered pricing** : If you want to give customers sustained-use discounts, you can create pricing tiers. If your price is based on more than one metric, you can define a separate set of tiers for each metric that you base your price on.

The tiers are applied as you go, over the course of the billing month. At the start of each new billing month, the price is reset to the first tier.

For example, if you want to charge users for each API request, as well as for storage time, you might set the following pricing tiers for each metric:

Pricing tiers for API requests | Pricing tiers for storage time  
---|---  
    * $0.002 per API request for 0-1000 requests
    * $0.001 per API request for 1001-2000 requests
    * $0.0001 per API request for 2001+ requests
| 
    * $0.05 per GiB-hour for 0-1000 GiB-hours
    * $0.001 per GiB-hour for 1001-2000 GiB-hours
    * $0.0001 per GiB-hour for 2001+ GiB-hours  
  
For example, in the sample pricing model above, if a user makes 1500 API requests in a billing month, they will be charged $0.002 per request for the first 1000 API requests, then $0.001 per request for the remaining 500 API requests. However, their first API request of the next billing month would once again be charged at the $0.002 tier, as one of the new month's first 1000 API requests.




## Add your pricing model to Producer Portal

After you have selected your pricing model, you can add it to the portal. Pricing models take up to four business days to review. You can continue integrating your product while the pricing model is reviewed.

You can't modify your pricing model while it's under review.

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
           

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the name of your product.

  3. On the **Overview** page of your product, go to the **Pricing** section and click **EDIT**.




### Defining your pricing structures

For each pricing model you want to support, create a name for your pricing plan and follow the steps to define the pricing structure. You can have one pricing plan for each product.

After you define the pricing structures for all of the pricing models you want to support, click **SET UP** to set up the pricing structures and continue on to the remaining features of the **Pricing** page.

#### Free

  1. In the **Pricing model** drop-down list, select **Free**.



#### Bring your own license pricing

  1. In the **Pricing model** drop-down list, select **Bring your own license (BYOL)**.



#### Usage-based pricing

  1. In the **Pricing model** drop-down list, select **Usage-based only**.

  2. In the **Metrics** drop-down list, select **ADD OR UPDATE METRICS** to add a metric.

  3. For each metric that you add, you must enter a **Display name** , a **Reporting unit** , and a **Display unit** , and then click either **DONE** or **ADD ANOTHER METRIC**. The **Reporting unit** specifies how your metric tracks usage for billing, while the **Display unit** specifies how your metric's pricing is displayed. For example, you may want to charge your users by per second of usage, but display your product's price per hour to your customers.

  4. Optionally, you can choose to measure the reporting unit using fractions.




### Adding pricing details for your pricing structures

After you define your pricing structures, you can add the pricing details for your pricing structures.

To add pricing details for the pricing structures you defined, navigate to the **Pricing** section of Producer Portal.

#### Bring your own license pricing

  1. Enter the URL that customers use to get their license in the **License Acquisition URL** field.



#### Usage-based pricing

  1. Click **EDIT USAGE**.

  2. For single-rate pricing, add a **Display Quantity** and a **Price**.

  3. For tiered pricing, enter a **Display Quantity** , and click **ADD TIER** for each additional tier that you would like to add. Once you see the correct number of tiers, add a **Price** , and a lower limit for the tier in the **From** field. The upper limit for each tier is updated when you add the lower limit of the next tier.

  4. Click **DONE**.




### Adding pricing descriptions to your plans

After you add your pricing details, you can describe your pricing model, default configuration, or other special instructions by using the **FEATURES** tab of the **Pricing details** section.

### Answering tax category questions

After you add features to your pricing plans, you can use the **TAX CATEGORY** tab of the **Pricing details** section to answer questions about your product. Your answers to these questions are used by Google for internal classification purposes only.

### (For partners with a US payment profile) Answer tax withholding questions

If you have a [payment profile](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) with a US address, then after you've answered the questions about your product's tax category, you should answer additional questions related to tax withholding. Your answers to these questions help Google categorize your product for tax purposes. This information is captured to ensure accurate withholding and reporting on your earned income. To answer these questions, from the **Pricing details** section, visit the **Tax withholding** tab.

**Note:** If you don't have a payment profile with a US address, you don't see the **Tax withholding** tab.

### Adding an end user license agreement (EULA)

Add an end user license agreement (EULA) in the **Terms & Policies** tab. We recommend that you use the Google standard EULA if your product allows it. This might help users adopt your product more quickly.

If your product requires a specialized EULA, add your EULA's URL to the **EULA URL** field.

### Submitting your pricing model for review

When you're ready to submit your pricing model for processing, click **Submit**.

You can't modify your pricing model while it's under review.

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

If your product's pricing is usage-based, we recommend a trial credit limit that is twice the cost of the usage that you expect.

## Updating the price of products after launch

If it's been at least 30 days after your pricing model has been published and approved, you can update the price of your product.

To update the price of your product, follow these steps:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
           

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID.

  3. On the **Overview** page, under **Pricing review** , click **EDIT**.

  4. Make your updates to your pricing.

  5. When you're done, click **Submit**.




You do not need to republish your product. Your product's price is updated after the new pricing is reviewed and approved.

## Deleting a pricing plan

If you want to delete a pricing plan in Producer Portal, you must make sure that it has no deployments associated with it, including both active and cancelled deployments. This means that you can't delete a pricing plan on your own if it has previously been purchased.

To delete a plan that has deployments associated with it, contact your Google Partner Engineer.

[ Previous arrow_back  Setting up your Google Cloud environment  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment)

[ Next Packaging your app  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
