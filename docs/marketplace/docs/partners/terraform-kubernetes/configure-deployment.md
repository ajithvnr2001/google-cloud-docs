---
url: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/configure-deployment/
title: Configure your Terraform Kubernetes app's deployment \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:24.410529+00:00
---

# Configure your Terraform Kubernetes app's deployment  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/configure-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Configure your Terraform Kubernetes app's deployment Stay organized with collections  Save and categorize content based on your preferences. 

You offer Terraform Kubernetes apps through Google Cloud Marketplace as Helm charts, which customers use to deploy your apps. After you've uploaded your app's Helm chart to Artifact Registry, use Producer Portal to configure your app's deployment and submit it for review.

**Note:** If you have questions during the onboarding process, talk to your Cloud Marketplace Partner Engineer. If you don't know who your assigned Partner Engineer is, use the [Google Cloud Support Portal](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about the Google Cloud Support Portal, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

## Before you begin

  * Create a public Git repository for the configuration files, user guide, and other resources to run your app. You can host the repository with a provider such as GitHub, Cloud Source Repositories, or on your own server. We recommend a dedicated repository for each product that you're distributing.
  * Verify that you've [prepared your Terraform Kubernetes app](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment) for Cloud Marketplace, including uploading your app's Helm chart to Artifact Registry and Terraform module to Cloud Storage.



## Configure your app's Helm chart and container images

Specify your app's Helm chart and container images in Producer Portal.

For steps to upload a Helm chart to Artifact Registry, see [Prepare your Terraform Kubernetes app](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/set-up-environment).

### Specify your app's Helm chart

To specify your app's Helm chart, complete the following steps:

  1. In Artifact Registry, navigate to the Helm chart that you want to use.
  2. Click to copy your Helm chart's URL.
  3. In Producer Portal, in the **Deployment configuration** tab, for **Specify Helm chart** , paste your Helm chart's URL.



The format of your Helm chart's URL should be as follows:
    
    
    us-docker.pkg.dev/PROJECT_NAME/PRODUCT_NAME/CHART_NAME
    

### Specify your app's releases

You can offer multiple _releases_ , or versions, of your app through Cloud Marketplace, and let your users select between the available releases. To specify your app's releases, complete the following steps:

  1. In Producer Portal, in the **Deployment configuration** tab, under **Image release** , click **Specify releases**.
  2. Under **New release** , add the following information: 
     * A _display tag_ , which should match the tag of the corresponding Helm chart that you uploaded to Artifact Registry.
     * A _version title_ , which Cloud Marketplace shows to your users.
     * A short _description_ , which explains how this release differs from other available releases.
  3. For **Module** , specify the Cloud Storage location of the corresponding Terraform module for this release.
  4. For each additional release that you want to add, click **Add release** and then complete the previous steps.
  5. For **Default release** , select which release should be the default release for your app's Cloud Marketplace listing.
  6. Click **Save and validate**.



After you click **Save and validate** , Cloud Marketplace automatically runs validation tests on your releases. Under **Proposed releases** , you see a brief description of the progress of the validation tests, including an estimate of how long they might take to complete. Validation involves testing to ensure that the provided Terraform module successfully runs `terraform plan`.

Your releases must pass validation before you can publish them to Cloud Marketplace.

## What's next

  * [Publish your product to Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/publish). To publish your product, you submit various parts of your product for review. The Cloud Marketplace team reviews each submission and works with you to resolve any issues before approving it. When all of your submissions are approved, you can publish and launch the product within a few minutes.



[ Previous arrow_back  Add pricing information  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/select-pricing)

[ Next Track your products' associated consumption  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/partner-consumption-tracking)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
