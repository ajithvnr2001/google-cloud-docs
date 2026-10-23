---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/create-deployment-package/
title: Create your deployment package \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:02.331037+00:00
---

# Create your deployment package  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/create-deployment-package/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Create your deployment package Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to create a deployment package for your virtual machine (VM) product, as part of publishing your product to Google Cloud Marketplace.

A deployment is a set of resources that are created and managed together—such as the resources needed for your product. A deployment package is a specification for a set of resources that are typically deployed together, which streamlines the process of deploying that particular product.

## Specify which deployment options to offer to your customers

You can enable your customers to deploy your VM product by using either or both of the following options:

  * **Terraform** (Recommended): [Terraform](https://www.terraform.io/) is an open source tool for provisioning infrastructure. For more information, refer to the [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform) documentation.

With this option, your customers download and deploy Terraform modules, either directly from Cloud Marketplace or by using Terraform.

We recommend that you support Terraform, especially if the following cases are true for your product:

    * Your customers are familiar with Terraform.

    * Your customers want to manage their deployments as infrastructure as code (IaC).

    * Your product's architecture is complex and extensively configurable.

    * Your product requires features that aren't available through the [open source `mpdev` tool](https://github.com/GoogleCloudPlatform/marketplace-tools).

  * **Cloud Deployment Manager** : [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager) is an infrastructure deployment service that automates the creation and management of Google Cloud resources. For more information, visit the [Deployment Manager documentation](https://docs.cloud.google.com/deployment-manager/docs).

With this option, your customers deploy your product directly from Cloud Marketplace.




To specify which deployment options to offer your customers, complete the following steps:

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Configuration** , use the checkboxes to select or clear **Terraform** and **Deployment Manager**. You must select at least one of the two options.




## Select your VM image

To select your product's VM image, complete the following steps:

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Deployment image source** , use the checkbox to specify whether or not to **Use Marketplace owned images**.

If you turn on usage of Cloud Marketplace owned images, then during verification of your VM image, Cloud Marketplace copies your image to a Google-owned Google Cloud project. We recommend that you turn on usage of Cloud Marketplace owned images to ensure that your customers' usage of your products isn't unintentionally disrupted if you make changes to images that you own. For example, if you don't use Cloud Marketplace owned images, and you change an Identity and Access Management (IAM) policy for your product's published image, you might cause some of your customers to be unable to access the product.

**Note:** For your customers to use Terraform to deploy your product, you must turn on **Use Marketplace owned images**.
  3. Select your VM image.

The VM image you select must meet the following requirements:

     * The VM image must be associated with your current Google Cloud project.

     * The VM image must have the correct license for your product attached to it. You create and attach this license when you [create your VM image](https://docs.cloud.google.com/marketplace/docs/partners/vm/build-vm-image#create_a_licensed_vm_image).




## Next steps

After you've specified which deployment options to offer to your customers and selected your VM image, you must complete the remaining applicable steps to configure your deployment image source.

  * [Configure your VM image for Terraform deployment](https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-terraform-deployment).

  * [Configure your VM image for Deployment Manager deployment](https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-dm-deployment).




[ Previous arrow_back  Understand how customers see your deployment packages  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/customer-view-deployment-packages)

[ Next Track your products' associated consumption  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
