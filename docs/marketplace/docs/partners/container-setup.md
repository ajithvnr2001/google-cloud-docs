---
url: https://docs.cloud.google.com/marketplace/docs/partners/container-setup/
title: Setting up the technical components \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:58.468892+00:00
---

# Setting up the technical components  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/container-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Setting up the technical components Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines how to create the key technical components required for distributing your container image product with Google Cloud Marketplace.

If you have questions during the onboarding process, talk to your Cloud Marketplace Partner Engineer. If you don't know who your assigned Partner Engineer is, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

## Artifact Registry and IAM setup

Before you can create your product in Producer Portal, you need to create a staging Artifact Registry repository and push the images you want to distribute in your product to that repository. In your project, you must grant the Project Editor role to `cloud-commerce-marketplace-onboarding@twosync-src.google.com`.

### Getting started with Container Registry

To push tagged container images to Container Registry, follow the steps in **Before you begin** in the [Artifact Registry documentation](https://docs.cloud.google.com/container-registry/docs/quickstart#before-you-begin). Then use the steps below to enable the Artifact Analysis API.

**For existing VM partners** : Your staging Artifact Registry repository can be within your dev project instead of your public project.

After you install `gcloud` and Docker, you must enable the following APIs from the [API Library page](https://console.cloud.google.com/apis/library?&q=Container):

  * Artifact Registry API
  * Artifact Analysis API



The Artifact Registry API lets you to push to Artifact Registry, and the Artifact Analysis API allows for security scanning.

If you have trouble accessing either of these APIs, contact your Partner Engineer.

### Tagging and pushing images

  1. Choose your Artifact Registry staging repository path. It is recommended that your repository follow the structure `us-docker.pkg.dev/YOUR-PARTNER-ID/YOUR-SOLUTION-ID`.

     * Staging repository must be within `us-docker.pkg.dev` or `gcr.io` (other regions, such as `europe-docker.pkg.dev` or `eu.gcr.io`, are not yet supported).
     * Save or copy your staging repository path for product creation in Producer Portal.
  2. Build the image you want to push to your Artifact Registry staging repository.

  3. Tag the image via Docker with `latest`.

`docker tag image_name staging_repo_path:tag`

For example, `docker tag test-image us-docker.pkg.dev/testpartner/testsolution:latest`

Note that the image tagged `latest` is pulled if a user does not specify a tag.

  4. Push your image using `gcloud`:

`gcloud docker push staging_repo_path:tag`

  5. Repeat for any additional tags or images you'd like to add to your staging repository. A single image may have multiple tags.

     * Remember that pushing an image to your staging repository won't automatically make it visible to users; this only happens to the images of the tags that you select, after they are published.
     * A repository's scope is the single level of the folder its path specifies. Any images which are within another folder in the repository are not actually in the repository itself. In other words, if an image is in `us-docker.pkg.dev/testpartner/testsolution/1.0`, it is NOT in the `us-docker.pkg.dev/testpartner/testsolution` repository. `us-docker.pkg.dev/testpartner/testsolution/1.0` is a separate repository.



## Creating your product in Producer Portal

This section describes how to create and publish your container image product in Producer Portal.

To publish your product in Producer Portal, you create an entry for your product, and then you submit the following information for review:

  * **Product details** : Add listing and marketing information about your product.
  * **Container images** : Provide the Google Container Registry repository that includes your container images.



You can submit these reviews at any time and in any order.

To create your product's Cloud Marketplace entry:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. At the top of the page, click **Add product**.

  3. Select **Container image**.

  4. Under **Product name** , name your product and check the Product ID. The Product ID is used in the URL for your Cloud Marketplace listing.

**Caution:** The Product ID and product type cannot be changed after the product is created. You can change your product name before you submit it.
  5. Click **Create**. It might take a few seconds to create your product.




### Adding product details

The product details include your product listing on Cloud Marketplace, marketing information, and links to documentation.

To add your product details:

  1. In the list of products, click the product ID.

  2. On the **Overview** page of your product, go to **Product details** , and click **Edit**.

  3. Complete the **PRODUCT INFO** tab of the **Product details** section. While completing **PRODUCT INFO** , you can add Category IDs. Category IDs allow customers to find your product under select categories or filters as they search Cloud Marketplace.

  4. To add tutorials, documentation, and, optionally, additional license agreements, complete the **DOCUMENTATION** tab of the **Product details** section. Your documentation must meet the [requirements for user guides](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes/create-app-package#user-guide).

  5. To add search metadata or keywords, or to customize the URL of the details page for your product, complete the **PRODUCT METADATA** tab of the **Product details** section.

  6. When you are ready to submit your product details for processing, click **Submit**.




It takes approximately 2-5 days for the Partner Engineering team to review and approve your product details. You can start editing details now and submit the review later.

### Adding your container images

You're required to create one version corresponding to the Container Registry tag `latest` (case-sensitive). This is the default version in product page.

To add your container images:

  1. In the list of products, click the product ID.

  2. On the **Overview** page of your product, go to **Container images** , and click **Edit**.

  3. In the **Container images** section, enter the URL for your staging Artifact Registry repository.

  4. Click **Specify Release**. It might take a few seconds to read the repository and load your tags.

  5. Select the **Display tag** for the release you want to include in your product. You must include the `latest` release in your product, but you can add additional versions. We recommend limiting the number of releases available to your product for your users' convenience.

  6. Optionally add a **Version title** and a short description of the release. These help your users deploy the version they want.

  7. Enter operating system that this release supports. You can specify the operating system version, if necessary.

  8. After you've added all the information for the release, click **Done**.

  9. To add another version, click **Add Release** , and enter the information for that release.

  10. When you're done adding supported releases to your product, click **Save and Validate**. The images are copied into a public repository, and then we run a series of tests against the images.

  11. Click **Submit** to submit the container images for review.




### Preview your container image product

To preview your Cloud Marketplace listing before it's visible to users:

  1. In the list of products, click the product ID.

  2. On the **Overview** page of your product, click **Full preview**.




If you've changed any tags in your staging repository since you validated your container images in Producer Portal, the images referenced in the preview might be inaccurate.

### Publish your container image product

To publish your product on Cloud Marketplace, you must:

  * Complete the **Product details** and **Container images** reviews.

  * Be approved as a [Google Cloud Build partner](https://docs.cloud.google.com/partners/become-a-partner).




After all reviews have been approved, you can publish and launch the product within a few minutes. To publish your product:

  1. In the list of products, click the product ID.

  2. On the **Overview** page of your product, click **Publish**.




[ Previous arrow_back  Offering container image products  ](https://docs.cloud.google.com/marketplace/docs/partners/container)

[ Next Updating, deprecating, and deleting container image products  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/container-updates)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
