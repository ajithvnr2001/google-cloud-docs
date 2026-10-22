---
url: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/customer-view-deployment-packages/
title: Understand how customers see your app's deployment packages \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:35.734276+00:00
---

# Understand how customers see your app's deployment packages  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/customer-view-deployment-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Understand how customers see your app's deployment packages Stay organized with collections  Save and categorize content based on your preferences. 

If you offer Terraform Kubernetes apps through Google Cloud Marketplace which are based on auto-generated standard packages, your customers see the following screen layouts when they get your product and deploy it.

## Customer view of deploying a package

### Terraform UI

The standard customer input elements are shown on the left side of the following screenshot and include zone, machine type, disk options, and networking options. If your product supports Terraform UI deployment, your customers can switch between Terraform UI or Terraform CLI.

The customer must specify a deployment service account, which Infra Manager uses to run the command `Terraform apply`.

![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/terraform-kubernetes-config-ui.png)

If a customer's deployment requires multiple network interface cards, they can add additional network interfaces by clicking **Add network interface**.

To deploy your product, your customers must fill out the input fields, and then click **Deploy**.

### Terraform CLI

The following screenshot shows the standard customer input elements, which include the following:

  * Service account
  * gcloud CLI configuration instructions



![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/terraform-kubernetes-config-cli.png)

To deploy your product, your customer must do the following:

  * Copy the provided command.
  * Replace any placeholders, such as deployment name and service account.



If your Terraform module requires inputs that don't have a default value, you must describe these inputs in the user guide that you provide to your customers.

## Customer view of a deployed package

The following screenshot shows how your product appears to customers after they've successfully deployed it. This includes the following standard output elements:

  * Site address
  * Temporary administrator password
  * Instance information



![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/standard-outputs-terraform.png)

If a deployment fails, customers can click **View logs** to be redirected to the logs of the Cloud Build job that actuated the Terraform configuration.

**Note:** When your customers deploy your VM product from Cloud Marketplace, the deployment is created with the label `marketplace-suppress-benign-warnings`, which blocks warnings that are irrelevant for Cloud Marketplace products. 

If customers remove the label from the deployment, they see the blocked warnings.

For information about labels in deployments, see [Adding labels to a deployment](https://docs.cloud.google.com/deployment-manager/docs/creating-managing-labels).

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes)

[ Next Prepare your Terraform Kubernetes app  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
