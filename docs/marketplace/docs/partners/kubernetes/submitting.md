---
url: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/submitting/
title: Submit your app \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:40.217273+00:00
---

# Submit your app  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/submitting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Submit your app Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the process for submitting your product for testing and review.

## Before you begin

    * Make sure that you've reviewed and met all of the [prerequisites for listing your app](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes#before-you-begin).

    * Make sure that you've reviewed and met all of the [requirements for your packaging your app](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package).

    * [Configure payments](https://docs.cloud.google.com/marketplace/docs/partners/receive-payments) so that you can be paid for your app's usage.




## Upload your images

Refer to the verification guidelines in the [Cloud Marketplace tools GitHub repository](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/verification-integration.md) to ensure that your container images pass the automated tests for all apps on Cloud Marketplace.

After your container images pass the verification tests, make sure that all the images for a version are tagged with the release track and version numbers, according to the [guidelines for organizing your releases](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment#organize-releases).

Finally, build your images and push them to your Container Registry repository, which you created when you [set up your environment](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/set-up-environment).

**Note:** If you are developing using a continuous integration (CI) pipeline, upload the images as the final step, _after_ all tests have passed.

You can then add your release to your Cloud Marketplace listing in Producer Portal.

**Caution:** Make sure that you only add versions that you want customers to use, and not test versions. 

Before you publish your release for customers, you can preview the release in Cloud Marketplace and update its images. The Cloud Marketplace team also tests and approves your version before it is published to customers.

## Add your product in Producer Portal

Before publishing your product, you must submit all of its components for review. You can submit the following reviews in any order to the Cloud Marketplace team:

  * Product details
  * Pricing
  * Container images



Some reviews might take up to two weeks for approval, so we recommend that you review the requirements and get started as early as possible.

### Add your product details

The product details include your product listing on Cloud Marketplace, marketing information, and links to documentation.

To add your product details:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID that you created.

  3. On the **Overview** page of your product, go to the **Product details** , and click **Edit**.

  4. Complete the **Product info** tab of the **Product details** section. While completing **Product info** , you can add Category IDs. Category IDs allow customers to find your product under select categories or filters as they search Cloud Marketplace. You can select up to two Category IDs for a product.

  5. To add tutorials, documentation, and, optionally, additional license agreements, complete the **Documentation** tab of the **Product details** section. Your documentation must meet the [requirements for user guides](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package#user-guide).

  6. To add search metadata or keywords, or to customize the URL of the details page for your product, complete the **Product metadata** tab of the **Product details** section.

  7. When you are ready to submit your product details for processing, click **Submit**. It takes approximately 2-5 days for the Partner Engineering team to review and approve your product details. You can start editing details now and submit the review later.


**Note:** Cloud Marketplace might require additional approvals for some categories of products. If you want to add your solution listing to a category that isn't listed in Producer Portal, submit a request by using the [special category request form](https://docs.google.com/forms/d/1-VwD1yyr_w5yWYIbx0OFzQOp7XgSPpa6IgaWbltoR90/edit?resourcekey=0-93_HVNitkydC9bBb6oZiIg).

### Add your container images

Each release corresponds to a minor version of your software and to an image tag in your Container Registry staging repository.

To add your container images:

  1. In the list of products, click the product ID that you created.

  2. On the **Overview** page of your product, go to the **Container images** section.

  3. In the Container images section, enter the URL for your Container Registry repository.

  4. Click **Specify Release**. It might take a few seconds to read the repository and load your tags.

  5. In **Display tag** , select the release you want to include in your Kubernetes app.

  6. Add a short description of the release.

  7. In the **Public Git repo** box, enter the URL for the Git repository that you created when you [created your app package](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package).

  8. In the **Deploy documentation URL** box, enter a link to the documentation that describes the steps to deploy the app from a command line interface (CLI). For example, the documentation might be the readme in your Git repository.

  9. Click **Done** when you've added all the information for that release.

  10. To add more releases, click **Add Release** , and enter the information for that release.

  11. In **Select default releases** , select the release your customers see on the product details page.

  12. When you're done adding supported releases to your product, click **Save and Validate**. The images are copied into a public repository, and then we run a series of tests against the images.

  13. Click **Submit** to submit the container images for review.




## Preview your Kubernetes app

You can preview your Cloud Marketplace listing before it's visible to users, by clicking **Full Preview**. After your container image verification tasks have completed successfully, this preview option also lets you test deploying your product.

## Publish your Kubernetes app

To publish your product on Cloud Marketplace, you must:

  * Complete the **Product details** , **Pricing** , and **Container images** reviews.

  * Be approved as a [Google Cloud Build partner](https://partners.cloud.google.com/).




After all reviews have been approved, you can publish and launch the product within a few minutes. To publish your product:

  1. Go to your product's **Overview** page in Producer Portal.

  2. Click **Publish**.




[ Previous arrow_back  Packaging your app  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package)

[ Next Maintaining your app  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/maintaining-product)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
