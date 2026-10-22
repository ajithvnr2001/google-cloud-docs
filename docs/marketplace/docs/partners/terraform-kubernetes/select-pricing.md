---
url: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/select-pricing/
title: Add your app's pricing information \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:26.856706+00:00
---

# Add your app's pricing information  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/select-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Add your app's pricing information Stay organized with collections  Save and categorize content based on your preferences. 

When your customers deploy your Terraform Kubernetes apps on Google Kubernetes Engine, they're charged for the following:

  * Their usage of your app, depending on the pricing model that you've set up.
  * Their usage of Google Cloud resources, such as the cost for running Google Kubernetes Engine clusters.



You can choose one of the following pricing models for your app:

  * **Free** : Customers only pay for the Google Cloud resources that they use.
  * **Usage-based** : Customers pay to run your app on GKE pods. Your product's pricing is based on usage of GKE resources allocated to these pods, such as vCPUs, GPUs, TPUs, or memory.



To set up your app's pricing model, use Producer Portal to add your app's pricing information.

## Before you begin

If your Terraform Kubernetes app includes usage-based pricing models, [prepare your app to track usage](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment#prepare-usage-tracking).

## Add your app's pricing information in Producer Portal

To add pricing information for your Terraform Kubernetes app, complete the following steps:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
           

  2. In the list of products, click the name of your product.

  3. On the **Overview** page of your product, go to the **Pricing** section and click **Edit**.




### Define your pricing structure

Create a name for your pricing plan and follow the steps to define the pricing structure. You can have one pricing plan for each product.

After you define the pricing structures for your selected pricing model, click **Set up** to set them up and continue on to the remaining features of the **Pricing** page.

#### Free

For **Pricing option** , select **Free**.

#### Usage-based pricing

To set up usage-based pricing, complete the following steps:

  1. For **Pricing option** , select **Usage-based pricing**.

  2. From the **Metrics** list, select the Google Kubernetes Engine metrics that you want to use from the following options:

     * vCPU
     * GPU
     * TPU
     * Memory

You can pick one metric or multiple metrics. For more information about these options, see [GKE pricing](https://docs.cloud.google.com/kubernetes-engine/pricing?e=13802955&hl).

  3. Click **Set up** to set up the pricing structures that you selected and continue on to the remaining features of the **Pricing** page.

  4. Click **Edit usage fees**.

  5. For each of the metrics that you selected, enter a price per unit per hour and click **Done**.

  6. After you've added a price for each of your metrics, click **Done**.




### Add pricing descriptions to your plans

After defining your pricing structure, you can describe your default configuration or provide other special instructions by using the **Features** tab of the **Pricing details** section.

### Answer tax category questions

In Producer Portal, in the **Pricing details** section, use the **Tax category** tab to answer questions about your product. Your answers to these questions are used by Google for internal classification purposes only.

### (For partners with a US payment profile) Answer tax withholding questions

If you have a [payment profile](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) with a US address, then after you've answered the questions about your product's tax category, you must answer additional questions related to tax withholding. Your answers to these questions help Google categorize your product for tax purposes. This information is captured to ensure accurate withholding and reporting on your earned income. To answer these questions, in Producer Portal, from the **Pricing details** section, visit the **Tax withholding** tab.

**Note:** If you don't have a payment profile with a US address, you don't see the **Tax withholding** tab.

### Add an end user license agreement

In Producer Portal, from the **Pricing details** section, visit the **Terms & Policies** tab to add an end user license agreement (EULA). We recommend that you use the Google standard EULA if your product allows it. This might help users adopt your product more quickly.

If your product requires a specialized EULA, add your EULA's URL to the **EULA URL** field.

## Submit your app's pricing for review

To submit your app's pricing information for review, in Producer Portal, navigate to your app's **Pricing** section and click **Submit**.

You can't modify your pricing information while it's under review.

## Update the price of products after launch

If it's been at least 30 days after your pricing model has been approved and published, you can update the price of your product. To update the price of your product, complete the following steps:

  1. In the list of products, click the name of your product.
  2. Go to your product's **Pricing** section.
  3. Click **Edit content**.
  4. Make your updates to your pricing.
  5. When you're done, click **Submit price model**.



After the new pricing is reviewed and approved, your product's price is updated. It might take up to four business days for Google to review and publish pricing updates.

If you're decreasing your price, Cloud Marketplace doesn't require any additional waiting period. If you're increasing your price, it takes an additional 45 days for the price increase to take effect after the Cloud Marketplace team confirms that they've received your price increase request. This time window includes the mandatory 30 days of advance notification for users to review the price change.

**Note:** Google Google Cloud Marketplace has the discretion to change the questions in the **Tax category** section of Producer Portal. In such cases, as part of submitting any future pricing updates, you must review the **Tax category** questions again and adjust your answers if required.

## Delete a pricing plan

To delete a pricing plan in Producer Portal, you must make sure that it has no deployments associated with it, including both active and cancelled deployments. This means that you can't delete a pricing plan on your own if it has previously been purchased.

To delete a plan that has deployments associated with it, contact your Google Partner Engineer.

[ Previous arrow_back  Add your Terraform Kubernetes app to Producer Portal  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/add-product)

[ Next Configure your app's deployment  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/configure-deployment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
