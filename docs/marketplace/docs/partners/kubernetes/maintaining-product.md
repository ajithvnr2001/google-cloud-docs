---
url: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/maintaining-product/
title: Maintaining your product \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:12.193927+00:00
---

# Maintaining your product  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/maintaining-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Maintaining your product Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the guidelines for maintaining and updating your product after it is live on Cloud Marketplace.

## Managing updates for your app

The process for updating your product is similar to creating your initial app package. First, you must generate a new set of container images for the update, and push them to your Container Registry staging repository. Depending on whether you are adding a new version or updating an existing version, use the steps below to update your app.

### Adding a new version

In your Container Registry staging repository, tag your app images with a new minor version tag. Then, follow the steps to [submit your app](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/submitting#add_your_solution_in_partner_portal) in Producer Portal.

### Updating an existing version

In your Container Registry staging repository, tag your images with the current minor version tag. Then, use the steps below to update the app in Producer Portal.

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID.

  3. On the **Overview** page of your product, go to the **Container images** section, and click **Edit**.

  4. By **Proposed Releases** , click **Edit**. It might take a few seconds to read the repository and load your tags.

  5. Click the release that you want to update.

  6. In **Display tag** , select the release that uses the corresponding digest to the image you updated in your Container Registry.

  7. After you've updated all the information for the release, click **Done**.

  8. When you're done adding supported releases to your product, click **Save and Validate**.

  9. Click **Submit** to submit the container images for review.

  10. After all reviews have been approved, you can publish and launch the product by opening the **Overview** page of your product, and clicking **Publish**.




As with initial submission, the Cloud Marketplace team performs automated testing and reviews your submission.

After the updated version is published, it becomes the default for new customers. Current customers will see new images pushed to existing tags. Deployments from the Cloud Marketplace product page are always pinned to image digests, and are not automatically updated. We also recommend pinning images to digests for customers who deploy your app through the command line.

To help your users update their app images, we recommend adding the upgrade steps to your [user guide](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package#user-guide).

### Migrating off of deprecated Kubernetes APIs

As Kubernetes APIs evolve, old APIs are eventually deprecated and removed. This means that your app can become incompatible with current GKE clusters. Typically existing objects are persisted, so customers' running deployments are unaffected.

To prevent failures in new app deployments:

  1. Review the current GKE versions in the [GKE release notes](https://cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) and upcoming versions in the [GKE release schedule](https://cloud.google.com/kubernetes-engine/docs/release-schedule).
  2. Update your app manifests to remove any dependencies on deprecated Kubernetes API versions which are removed in any current or upcoming GKE versions in the Regular or Stable channel. Refer to the Kubernetes [deprecated API migration guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide). 
     * For example, update uses of the `batch/v1beta1` `CronJob` to `batch/v1`, as `batch/v1beta1` will be removed in Kubernetes version 1.25, according to the [guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#cronjob-v125).
     * If you're unable to update the manifests for earlier releases of your app, we recommend removing the release or setting the [`k8sVersion` cluster constraint](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/schema.md#clusterconstraints) in your schema.
  3. Complete testing of all rebuilt container images using the [mpdev tool](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/mpdev-references.md), ideally on a cluster with a Kubernetes version that doesn't support the deprecated API you're removing. 
     * For example, use a Kubernetes version 1.22 cluster to test updating from the `apiextensions.k8s.io/v1beta1` `CustomResourceDefinition`, which was removed in Kubernetes version 1.22.
  4. Follow the instructions for Adding a new version or Updating an existing version to submit your changes in the portal.



## Pricing changes

Pricing changes take effect after a certain waiting period, and are not immediate. For specifics, refer to your contract.

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID.

  3. On the **Overview** page of your product, go to **Pricing review** , and click **Edit**.

  4. Make any changes to your pricing.

  5. Click **Submit** to submit the pricing for review.

  6. After all reviews have been approved, you can publish and launch the product by opening the **Overview** page of your product and clicking **Publish**.




## Deprecating apps

As you develop your software, you might want to make certain releases unavailable on Cloud Marketplace.

### Removing an app release

When you remove a release from your product, it is immediately removed from the product details page when the product is published. However, removing a release does not remove the images published to the public Container Registry.

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID.

  3. On the **Overview** page of your product, go to the **Container images** section, and then click **Edit**.

  4. Next to **Proposed Releases** , click **Edit**. It might take a few seconds to read the repository and load your tags.

  5. Highlight the release that you want to remove.

  6. Click delete **Delete** to remove the version.

  7. Click **Done**.

  8. When you're done removing releases to your product, click **Save and Validate**.

  9. Click **Submit** to submit the container images for review.

  10. After all reviews have been approved, you can publish and launch the product by opening the **Overview** page of your product, and clicking **Publish**.




[ Previous arrow_back  Submitting your app to Google Cloud Marketplace  ](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/submitting)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
