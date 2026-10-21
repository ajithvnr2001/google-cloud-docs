---
url: https://docs.cloud.google.com/marketplace/docs/partners/container/
title: Offering container image products \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:13.636366+00:00
---

# Offering container image products  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Offering container image products Stay organized with collections  Save and categorize content based on your preferences. 

This page is an overview of what you need to do to distribute and maintain a container image product on Cloud Marketplace.

## Before you begin

  * Review the [open source compliance](https://docs.cloud.google.com/marketplace/docs/partners/open-source-compliance) recommendations and restrictions. 
  * [Create](https://support.google.com/cloud/answer/6251787) your Google Cloud project and grant the Project Editor role to `cloud-commerce-marketplace-onboarding@twosync-src.google.com`.
  * Complete the **Project Info form** that the Cloud Marketplace team sends you. To fill out the form, you might need to request access to it.



After you send us the required information, we give you access to Producer Portal, which you use in the next step, technical integration.

## Overview of technical integration

![Overview of the container onboarding process](https://docs.cloud.google.com/static/marketplace/docs/partners/images/container-overview-process.png)

As a partner, you use Producer Portal to create Google Cloud Marketplace products. You enter product details, configure what images are shown, and preview how your listing appears in Cloud Marketplace.

Users pull container images from a Google-owned container registry repository, `marketplace.gcr.io/YOUR-PARTNER-PUBLISHED-NAME/YOUR-PRODUCT-PUBLISHED-NAME`. You give Google your product images by using a _staging_ repository with the suffix `gcr.io`, which you provide during product creation. You specify which Container Registry tags you'd like to present in Cloud Marketplace. When your product is published, Google copies the specified images from your staging `gcr.io` repository to the official `marketplace.gcr.io` repository, from which users download your container images.

**Note:** Starting January 20, 2025, Google Cloud Marketplace is requiring that all new or updated deployments of container image products contain an annotation in their image manifest that identifies the service name of the product. For more information, see [Migrate to annotating container images with their service name](https://docs.cloud.google.com/marketplace/docs/partners/migrations/container-image-annotations).

![Overview of container product architecture](https://docs.cloud.google.com/static/marketplace/docs/partners/images/container-overview.png)

## Requirements for container image products

Your product's container image must contain the following annotation in its image manifest:
    
    
    com.googleapis.cloudmarketplace.product.service.name=services/SERVICE_NAME
    

Replace SERVICE_NAME with the name of your service (for example, `example.endpoints.example-project.cloud.goog`). To find your product's service name, in Producer Portal, visit the **Overview** page and see the **Service name** column. For more information about annotations, see the Open Container Initiative's documentation of [annotations](https://github.com/opencontainers/image-spec/blob/main/annotations.md) on GitHub.

### Best practices for container image products

We recommend the following best practices for all container image products:

  * Create Getting Started documentation
  * Add User Support documentation

**Note** : The Cloud Marketplace Partners documentation focuses on onboarding your product; you should be aware that you are expected to maintain fresh, up-to-date, and secure products after launch. For more detailed information, refer to your Google Cloud Marketplace Partner Agreement.

## Reviewing and launching

After you submit your product, `cloud-partner-eng` will review your submission and work with you to resolve any issues before approving it. When the product is approved, it is launched within 15 minutes of approval.

[ Next Setting up the technical components  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/container-setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
