---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/select-pricing/
title: Choosing a pricing model \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:09.563802+00:00
---

# Choosing a pricing model  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/select-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Choosing a pricing model Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about the pricing models you can choose for virtual machine (VM) products. Review the information to decide on a pricing model for your product.

Pricing models take up to four business days to review. You can continue integrating your product while the pricing model is reviewed.

You can choose one of the following pricing models for your product:

  * Free: Customers only pay for the Google Cloud resources that they use, such as the cost for running VM instances. If you are offering your product at no cost, skip to Adding your pricing model to Producer Portal.

  * Bring your own license (BYOL): Customers pay you directly for the product itself, and are billed separately for the Google Cloud resources that they use. You are responsible for making sure that your customers are using a valid license for your app.

  * Usage-based pricing: Customers pay for your software based on measurements that you choose, called _metrics_ , such as the amount of RAM used by a VM product.




You can also create customized quotes for specific customers. For steps to create a custom quote, see [Creating private offers for specific customers](https://docs.cloud.google.com/marketplace/docs/partners/create-offers).

After you've decided on your pricing model, you must add it to your product in Producer Portal so that it can be processed.

## Bring your own license (BYOL) pricing

If you want to bill customers yourself, you can choose a Bring your own license (BYOL) pricing model. You must provide a way for your customers to get a license from you, typically through a website. Cloud Marketplace asks that customers get your license ID before deploying a BYOL product. After the deployment, you are responsible for validating the license ID entered by the partner.

Google will bill the customer independently for infrastructure usage costs of running the product.

If you want to use a BYOL pricing model, skip to Adding your pricing model to Producer Portal.

## Usage-based pricing

VM products are priced by usage, so customers pay for your software based on measurements that you choose, such as the number of vCPUs used.

### Define your pricing structure

For usage-based pricing, select one of the following options:

  * **Instance-based pricing** : Charge a single hourly rate for your product. Customers are charged based on the length of time that the product is used, with a minimum length of one minute. After the first minute, products are charged in increments of one second.

  * **Resource-based pricing** : Charge a rate based on the resources in the product. Depending on their workloads, users can choose the number of vCPUs and the RAM that they can add to their VMs. For products with heavy computation needs, users can also add GPUs to their VMs.

You can charge by the number of vCPUs, size of the system's memory, number of GPUs, or a combination of these options.

If you choose resource-based pricing, for each type of resource, choose one of the following models:

    * **Flat rate** : Set a per-unit price for resources. For example, you can set a price for every vCPU used in the product.
    * **Tiered** : Set a price by tiers. For example, you can set one price for 1 to 5 vCPUs and another for 6 to 10 vCPUs.



Google bills users on a monthly basis for software and infrastructure use.

## Add your pricing model to Producer Portal

After you have decided on your pricing model, you can add it to Producer Portal.

**Caution:** You can't modify your pricing model while it's under review. After you submit your pricing model for review, you can't change your pricing model for 30 days.

To add your pricing model to Producer Portal and submit it for review:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
           

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the name of your product.

  3. On the **Overview** page, under **Pricing review** , click **Edit**.

  4. Set up your pricing structure based on the pricing model:

###  BYOL 

     1. Enter a name for your pricing plan.

     2. In the **Pricing option** drop-down list, select **BYOL** and then click **Set up**.

     3. In the **Price model** pane, in the **License Acquisition URL** field, enter the URL that customers must use to get their license. Click **Next**.

     4. Optionally, add a pricing description that customers see when comparing VM products on Cloud Marketplace. Click **Next**.

     5. Complete the tax category information. Click **Next**.

     6. (For partners with a US payment profile) Complete the withholding tax information. Click **Next**.

     7. In the **Terms & Policies** pane, enter the URL for your end user license agreement (EULA).

     8. Click **Submit**.

###  Free 

     1. Enter a name for your pricing plan.

     2. In the **Pricing option** drop-down list, select **Free** and then click **Set up**.

     3. In the **Price model** pane, review the details and click **Next**.

     4. Optionally, add a pricing description that customers see when comparing VM products on Cloud Marketplace. Click **Next**.

     5. Complete the tax category information. Click **Next**.

     6. (For partners with a US payment profile) Complete the withholding tax information. Click **Next**.

     7. In the **Terms & Policies** pane, enter the URL for your end user license agreement (EULA).

     8. Click **Submit**.

###  Usage-based pricing 

     1. Enter a name for your pricing plan.

     2. In the **Pricing option** drop-down list, select **Usage-based pricing**.

     3. Complete the remaining steps to create either a resource-based or instance-based pricing model:

###  Resource-based pricing 

        1. In the **Metrics** drop-down list, select the unit that this metric measures. It can be either the number of CPUs, the amount of RAM, or the number of GPUs used for the product. You can select any combination of these metrics for your product.
        2. Click **Set up**.
        3. In the **Price model** pane, click **Edit usage fees**.
        4. For each metric, select the type of rate:

           * **Flat rate** : The flat cost, per unit of measure per hour, for this metric.
           * **Tiered rate** : The cost per hour, which varies across multiple tiers of usage. For example, you can set one price for 0 to 128 GB of RAM per hour, and another price for 129-256 GB of RAM per hour.
        5. Complete the metric details.

If you're using a tiered rate, click **Add tier**. From there, you can set minimum and maximum values for each tier. By default, the first tier starts at 0. The upper limit of each tier is updated when you add the lower limit of the next tier.

After entering details for each metric, click **Done**.

        6. Click **Pricing preview** to see a summary table that displays the details and usage fees for your pricing model. Exit the preview and click **Next**.

        7. Optionally, add a pricing description that customers see when comparing VM products on Cloud Marketplace. Click **Next**.

        8. Complete the tax category information. Click **Next**.

        9. (Partners with US Payment Profile **only**) Complete the withholding tax information. Click **Next**

        10. In the **Terms & Policies** pane, enter the URL for your end user license agreement (EULA).

        11. Click **Submit**.

###  Instance-based pricing 

        1. In the **Metrics** drop-down list, select **Hourly instance fee**.

        2. Click **Set up**.

        3. In the **Price model** pane, click **Edit usage fees** to add the price per hour that you want to charge customers for using your product. Click **Done**.

        4. Click **Pricing preview** to see a summary table that displays the details and usage fees for your pricing model. Exit the preview and click **Next**.

        5. Optionally, add a pricing description that customers see when comparing VM products on Cloud Marketplace. Click **Next**.

        6. Complete the tax category information. Click **Next**.

        7. (For partners with a US payments profile only) Complete the withholding tax information. Click **Next**.

        8. In the **Terms & Policies** pane, enter the URL for your end user license agreement (EULA).

        9. Click **Submit**.

After you submit your pricing model, it can take up to four business days to process.




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

## Update the price of products after launch

If it's been at least 30 days since your pricing model was published and approved, you can update the price of your product.

To update the price of your product, follow these steps:

  1. In the list of products, click the name of your product.
  2. Go to the pricing section of your product.
  3. Click **Edit content**.
  4. Make your updates to your pricing.
  5. When you're done, click **Submit price model**.



Your product's price is updated after the new pricing is reviewed and approved.

It takes up to four business days for price updates to be reviewed and approved. If you're decreasing your price, your price decrease does not require any additional waiting period. If you're increasing your price, it takes an additional 45 days from the Operations team's confirmation of receipt of your request for the price increase to take effect. This time window includes 15 days to draft and send a message to active users, and 30 days for users to review the price change.

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

[ Previous arrow_back  Setting up your Google Cloud environment  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/set-up-environment)

[ Next Building your VM image  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/build-vm-image)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
