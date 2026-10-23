---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/customer-view-deployment-packages/
title: Understand how customers see your deployment packages \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:58.883903+00:00
---

# Understand how customers see your deployment packages  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/customer-view-deployment-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Understand how customers see your deployment packages Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces the screen layouts that your customers see when they deploy your product, for products based on auto-generated standard packages.

To see the customer view directly for yourself, follow the instructions at [Test your VM product](https://docs.cloud.google.com/marketplace/docs/partners/vm/test-product).

## Customer view of deploying a package

### Terraform UI

The standard customer input elements are shown on the left side of the following screenshot and include zone, machine type, disk options, and networking options. If your product supports Terraform UI deployment, your customers can switch between Terraform UI or [Terraform CLI](https://docs.cloud.google.com/marketplace/docs/partners/vm/customer-view-deployment-packages#terraform-cli).

The customer must specify a deployment service account, which Infra Manager uses to run the command `Terraform apply`.

![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/standard-inputs-terraform-ui.png)

If a customer's deployment requires multiple network interface cards, they can add additional network interfaces by clicking **Add network interface**.

To deploy your product, your customers must fill out the input fields, and then click **Deploy**.

### Terraform CLI

The standard customer input elements are shown on the left side of the following screenshot and include service account and gcloud CLI configuration instructions.

![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/standard-inputs-terraform-cli.png)

If you configured a default Terraform module, your customers click **Generate Code** to generate a code snippet. If you configured a custom Terraform module for command-line deployment, your customers click **Download**.

### Deployment Manager

The standard customer input elements are shown on the left side of the following screenshot and include zone, machine type, disk options, and networking options.

![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/standard-inputs-dm.png)

If a customer's deployment requires multiple network interface cards, they can add additional network interfaces by clicking **Add network interface**.

To deploy your product, your customers must fill out the input fields, and then click **Deploy**.

## Customer view of a deployed package

### Terraform UI

The following image shows you how your product appears to your customers after they deploy it successfully.

The standard output elements are shown on the right side of the following screenshot and include site address, temporary administrator password, and instance information.

![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/standard-outputs-terraform.png)

If a deployment fails, customers can click **View logs** to be redirected to the logs of the Cloud Build job which actuated the Terraform configuration.

### Deployment Manager

The following image shows you how your product appears to your customers after they deploy it successfully.

The standard output elements are shown on the right side of the following screenshot and include site address, temporary administrator password, and instance information.

![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/standard-outputs-dm.png)

**Note:** When your customers deploy your VM product from Cloud Marketplace, the deployment is created with the label `marketplace-suppress-benign-warnings`, which blocks warnings that are irrelevant for Cloud Marketplace products. 

If customers remove the label from the deployment, they see the blocked warnings.

For information about labels in deployments, see [Adding labels to a deployment](https://docs.cloud.google.com/deployment-manager/docs/creating-managing-labels).

[ Previous arrow_back  Configure your VM image for Deployment Manager deployment  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-dm-deployment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
