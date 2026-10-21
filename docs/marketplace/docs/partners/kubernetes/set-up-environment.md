---
url: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment/
title: Setting up your Google Cloud environment \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:11.230510+00:00
---

# Setting up your Google Cloud environment  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Setting up your Google Cloud environment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to set up your Google Cloud environment so that you can distribute your Kubernetes apps.

## Create your workspace

We recommend that you create a new project in the [Google Cloud console](https://console.cloud.google.com/) primarily for your Cloud Marketplace products.

To manage products that you submit to Cloud Marketplace, we recommend that you create a new project with a project ID ending in `-public`. To create a project for your products, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

If you already have a project set up to sell on Cloud Marketplace that you want to use, verify that the Identity and Access Management (IAM) roles are granted correctly for Kubernetes, and skip to Set up a container registry.

## Grant roles for your project

To finish setting up your project, complete the following steps:

  1. After you've created your project, grant the following roles at the project level:

     * Project Editor, to `cloud-commerce-marketplace-onboarding@twosync-src.google.com`
     * Service Management Administrator (`roles/servicemanagement.serviceAdmin`), to `cloud-commerce-marketplace-onboarding@twosync-src.google.com` and `managed-services@cloud-marketplace.iam.gserviceaccount.com`
     * Config Editor (`roles/servicemanagement.configEditor`), to `cloud-commerce-producer@system.gserviceaccount.com`

To grant access to your project, see [Granting, changing and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. Grant the following roles at the service level, to `cloud-commerce-procurement@system.gserviceaccount.com`:

     * Service Consumer (`roles/servicemanagement.serviceConsumer`)
     * Service Controller (`roles/servicemanagement.serviceController`)

For steps to grant access at the service level, see [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access).

  3. Set a security contact. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

  4. Complete the _Project Info form_ that the Cloud Marketplace team gives you.




## Set up a container registry

You need a Container Registry repository to host the container images for your app. Artifact Analysis continuously scans the app images for vulnerabilities so that you can review and address issues before submitting your product to Cloud Marketplace.

To set up Container Registry, Docker, and the Google Cloud SDK, follow the [Container Registry quickstart](https://docs.cloud.google.com/container-registry/docs/quickstart).

After you set up Container Registry, in the project that contains your registry, grant the Project Viewer role to `cloud-commerce-marketplace-onboarding@twosync-src.google.com`.

### Enable the Container Analysis API

You must enable the Artifact Analysis API, which scans your container images in Container Registry for vulnerabilities. For an overview of vulnerability scanning in Artifact Analysis, see see the [Container Registry Documentation](https://docs.cloud.google.com/container-registry/docs/container-analysis#vulnerability_scanning).

## Add your product to Cloud Marketplace

To create and publish your product in Cloud Marketplace, you use Producer Portal. Your Partner Engineer enables it for you after you complete the [Cloud Marketplace Project Info Form](https://docs.google.com/forms/d/e/1FAIpQLSfddn4mwKnqtLNQ-m7IgRZ-bgTz4BOsrEDWCf3XBjc_ogKNnA/viewform).

To publish your product in Producer Portal, you create an entry for your product, and then you submit the following information for review:

  * **Product details** : Add listing and marketing information about your product.
  * **Pricing** : Choose and specify your pricing model to determine how customers pay you for your product.
  * **Container images** : Provide the Google Container Registry repository that includes your container images.
  * **Open Source Compliance** : Ensure that your product complies with Google's policies for open source software.



You can submit these reviews at any time and in any order. Some reviews might take up to two weeks for approval, so we recommend reviewing the requirements and getting started as early as possible.

To create your product's Cloud Marketplace entry:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. At the top of the page, click **Add product**.

  3. Select **Kubernetes**.

  4. Under **Product name** , name your product and check the Product ID. The Product ID is used in the URL for your Cloud Marketplace listing.

**Caution:** The Product ID and product type cannot be changed after the product is created. You can change your product name before you submit it.
  5. Click **Create**. It might take a few seconds to create your product.




You add your pricing model and marketing information for your solution in later steps.

## Create a development cluster in Kubernetes Engine

You use Google Kubernetes Engine to manage and scale Kubernetes clusters. To create a test cluster and deploy a basic app to it, follow the [Google Kubernetes Engine quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).

**Note:** If you are not actively using your cluster for testing, consider deleting the cluster. If you want to keep the cluster and save on costs, you can resize the cluster, and change the number of nodes to zero. For steps to resize your cluster, see the [Google Kubernetes Engine documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-container-cluster).

## Install the `mpdev` development tool

The `mpdev` tool is a container that bundles utilities to test and publish your app images. While installing `mpdev` is not required to submit an app for release, you can run `mpdev` to verify your development environment, and to test whether your app installs correctly on your development cluster.

[Install `mpdev` from the Cloud Marketplace tools GitHub repository](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/tool-prerequisites.md).

For information on using `mpdev` to check your environment and test your app, see the [mpdev reference on GitHub](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/mpdev-references.md).

## Organizing your releases

In general, every version of your app must adopt [Semantic Versioning 2.0](https://semver.org/), which follows the `MAJOR.MINOR.PATCH` numbering convention. Every version must have a unique version number, such as `1.0.1`, `1.0.2`, `1.3.1`, and so on. Optionally, add a hyphen after the version number to add a pre-release modifier, such as `1.3.1-alpha201910`. Pre-release modifiers can be used to store and highlight any additional information that you find useful, such as build dates denoting when versions were created.

We recommend that you release your software in _tracks_. Each track is a series of versions with backwards-compatible updates. Your release tracks should be based on a minor version, such as `4.1.x`. As a best practice, avoid using generic version names such as `latest`.

For example, if you're releasing version `2.0` of your software on Cloud Marketplace, and expect that versions `2.0.1`, `2.0.5`, and so on will be backwards-compatible with `2.0`, organize these releases under the `2.0` release track.

When you release a backwards-incompatible version of your app, or a version that requires users to go through manual migration steps, release it on a new track, so that users can plan their updates.

## Choose your product identifiers

You must select the following identifiers for your company, product, and container images, which are used to create your Cloud Marketplace URLs, and the URIs for your container images:

  * Your company's name. For example, if the name of your company is Examplesoft Inc., you can use the identifier `examplesoft`.

  * Your product's name. For example, if the product's name is Example Pro, use the identifier `example-pro`.

  * The release track of your product, such as `4.0`.

See the requirements for organizing your releases.

  * Your container images. Select a unique identifier for each container image in your app. The following identifiers are required for all apps:

    * The primary image: This container image is the main image for your product, and uses the same identifier as the product. For example, if your product identifier is `example-pro`, the primary image uses the same identifier.
    * `deployer`: The deployment container image for the track. The deployment container runs when users deploy your app from Google Cloud console You create a deployment image when you [create your app package](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package).

**Caution:** The identifiers you select appear in product URLs and container image URIs. It is difficult to change these identifiers after your product has been published to Cloud Marketplace customers.

For example, the company Examplesoft Inc. chooses the following identifiers for their product, Example Pro:

| Name | Identifier  
---|---|---  
Company | Examplesoft Inc | examplesoft  
Product | Example Pro | example-pro  
Image [1] (primary) | Example Pro server | n/a  
Image [2] | Example Queue | example-queue  
Image [deployer] | n/a | deployer  
Release track [1] | Version 4.x.x | 4.0  
Release track [2] | Version 5.x.x | 5.0  
  
For these identifiers, the following information is automatically generated:

  * The product URL in Cloud Marketplace: `https://console.cloud.google.com/marketplace/details/examplesoft/example-pro`

  * The container image URIs:

    * `marketplace.gcr.io/examplesoft/example-pro:4.0`
    * `marketplace.gcr.io/examplesoft/example-pro/example-queue:4.0`
    * `marketplace.gcr.io/examplesoft/example-pro/deployer:4.0`
    * `marketplace.gcr.io/examplesoft/example-pro:5.0`
    * `marketplace.gcr.io/examplesoft/example-pro/example-queue:5.0`
    * `marketplace.gcr.io/examplesoft/example-pro/deployer:5.0`



[ Previous arrow_back  Overview and checklist  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes)

[ Next Choosing a pricing model  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/select-pricing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
