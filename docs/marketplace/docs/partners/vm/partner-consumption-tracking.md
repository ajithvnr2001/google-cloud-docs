---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking/
title: Track your VM products' associated consumption with labels \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:03.326282+00:00
---

# Track your VM products' associated consumption with labels  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Track your VM products' associated consumption with labels Stay organized with collections  Save and categorize content based on your preferences. 

Many Google Cloud Marketplace products drive customer usage of Google Cloud infrastructure and resources. You can integrate labels into your products that give Google insights into your products' impact in terms of their associated customer Google Cloud usage, which Google can use to showcase impact and guide go to market (GTM) investments.

This document describes how to set up partner consumption tracking for virtual machine (VM) products that you offer through Cloud Marketplace.

## Label schema

Labels are key-value pairs that you can assign to Google Cloud resources. For more information about labels, see the [Overview of labels](https://docs.cloud.google.com/resource-manager/docs/labels-overview).

When you use labels for partner consumption tracking, your labels use the following format:
    
    
    goog-partner-solution = SOLUTION_URN
    

### Find your product's consumption tracking label

For each product that you offer through Cloud Marketplace, you can find its associated consumption tracking label in Producer Portal. To find the label, take the following steps:

  1. In Producer Portal, visit the **Overview** page.
  2. In the list of your products, find the product whose consumption you want to track.
  3. Copy and save the value listed for **Consumption tracking label**.
  4. When you integrate your product's consumption tracking, use the consumption tracking label that you saved.



The direct link to the Producer Portal **Overview** page is:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

## Integrate the consumption tracking label with your VM product

To integrate the consumption tracking label with your VM product, you must use Terraform, an infrastructure-as-code tool created by HashiCorp, to set up your product to add the label to Google Cloud resources as it deploys them. For more information about Terraform, see [What is Terraform](https://developer.hashicorp.com/terraform/intro) in the Terraform documentation.

**Note:** Your product must add the label at the resource level, instead of at the project level.

With Terraform, you can add a default label at the Google provider level that applies to all Google Cloud resources that Terraform deploys. For more information about using default labels with Terraform, see the [Google Cloud Provider Configuration Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#default_labels) in the Terraform documentation.

[ Next Testing your VM product  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/test-product)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
