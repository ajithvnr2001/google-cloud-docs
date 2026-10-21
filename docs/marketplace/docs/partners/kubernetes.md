---
url: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/
title: Offering Kubernetes apps \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:11.365916+00:00
---

# Offering Kubernetes apps  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Offering Kubernetes apps Stay organized with collections  Save and categorize content based on your preferences. 

A Kubernetes app is a containerized app that your users can run on a Kubernetes cluster in Google Kubernetes Engine, or on their own infrastructure. The Kubernetes app that you submit to Cloud Marketplace is a bundle of container images, configuration files, and display metadata.

This page is an overview of what you need to do to distribute and maintain a containerized app on Cloud Marketplace. If you already have a Kubernetes app on Cloud Marketplace and want to learn about maintaining it, see the [guidelines for maintaining your app after it's live](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/maintaining-product).

For an overview of Kubernetes concepts, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/).

If you're new to Google Kubernetes Engine, see the [Google Kubernetes Engine overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview), or try the [Google Kubernetes Engine Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).

**Note:** Starting January 20, 2025, Google Cloud Marketplace is requiring that all new or updated deployments of Google Kubernetes Engine app product listings contain an annotation in their image manifest that identifies the service name of the product. For more information, see [Migrate to annotating container images with their service name](https://docs.cloud.google.com/marketplace/docs/partners/migrations/container-image-annotations).

## Before you begin

  * If you're new to offering software on Cloud Marketplace, [sign up to become a vendor](https://docs.cloud.google.com/marketplace/docs/partners/offer-products#initiate-onboarding). 
  * For your first (and all subsequent) listings you must complete the [Cloud Marketplace Onboarding Validation Form](https://docs.google.com/forms/d/e/1FAIpQLSesllyRR-HvLFZthYA8Cv4nQRUTOthHGgs-76DY9o2IntUL3A/viewform). 
  * To get access to Producer Portal, complete the _Cloud Marketplace Project Info Form_ , provided by the Cloud Marketplace team. 
  * Review the [open source compliance](https://docs.cloud.google.com/marketplace/docs/partners/open-source-compliance) recommendations and restrictions. 



## Checklist

At a high level, you must do the following:

  1. Create a public Git repository for your app's configuration, user guide, and other resources to run your app. You can host the repository with a provider such as GitHub, Cloud Source Repositories, or on your own server.

  2. [Set up your Google Cloud environment](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment).

  3. [Review the pricing options, and select a pricing model](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/select-pricing). Pricing models take up to four business days to review. You can continue integrating your product while the pricing model is reviewed.

  4. Create your app package, which must meet the [technical requirements](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package) for the container images and configuration files that are part of your product.

  5. [Submit the app to Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/submitting). The Cloud Marketplace team reviews your app, which includes verifying that your app installs and uninstalls successfully, running unit tests, and scanning your containers for vulnerabilities using [Artifact Analysis](https://docs.cloud.google.com/container-registry/docs/get-image-vulnerabilities). After your app is reviewed, it is published on Cloud Marketplace.

  6. [Review the guidelines for maintaining](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/maintaining-product) your product after it is live.




If you have questions during the onboarding process, contact your Cloud Marketplace Partner Engineer. If you don't know who your assigned Partner Engineer is, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

[ Next Setting up your Google Cloud environment  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
