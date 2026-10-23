---
url: https://docs.cloud.google.com/marketplace/docs/partners/container-updates/
title: Updating, deprecating, and deleting container image products \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:34.336108+00:00
---

# Updating, deprecating, and deleting container image products  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/container-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Updating, deprecating, and deleting container image products Stay organized with collections  Save and categorize content based on your preferences. 

## Updating images in Container Registry

Following the same process that you performed when you pushed your image to your Container Registry staging repository, add your new image to Container Registry with the proper tag.

  1. Build the image that you want to push to your Container Registry staging repository.
  2. Tag your image using Docker with the tag of the existing version you'd like to update (or with a new tag if you want the image under a new version):

`docker tag {image_name} {staging_repo_path}:{tag}`

For example, `docker tag test-image gcr.io/testpartner/testsolution:latest`

  3. Push your image using `gcloud`:

`gcloud docker push {staging_repo_path}:{tag}`

  4. Repeat for any additional tags you'd like to add or update to your staging repository. Note that a single image can have multiple tags.

Remember that pushing an image to your staging repository doesn't automatically make it visible to users (even if you use a tag that is already associated with a version); this only happens after you update the version in Producer Portal and your product is published.




You can manage tags directly (add, edit, or delete) on images already in your Container Registry staging repository using the [Container Registry UI](https://cloud.google.com/container-registry/).

### Updating your products in Producer Portal

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID.

  3. On the **Overview** page of your product, go to the **Container images** section, and click **Edit**.

  4. By **Proposed Releases** , click **Edit**. It might take a few seconds to read the repository and load your tags.

  5. Click the release that you want to update.

  6. In **Display tag** , select the version that uses the corresponding digest to the image you updated in your staging Container Registry repository.

  7. After you've updated all the information for the release, click **Done**.

  8. When you're done updating supported releases to your product, click **Save and Validate**.

  9. Click **Submit** to submit the container images for review.

  10. After all reviews have been approved, you can publish and launch the product by opening the **Overview** page of your product and clicking **Publish**.




## Removing versions

When you remove a release from your product, it is immediately removed from the product details page when the product is published. However, removing a release does not remove the images published to the public Container Registry.

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. In the list of products, click the product ID.

  3. On the **Overview** page of your product, go to the **Container images** section, and click **Edit**.

  4. By **Proposed Releases** , click **Edit**. It might take a few seconds to read the repository and load your tags.

  5. Highlight the release that you want to remove.

  6. Click delete to remove the version.

  7. Click **Done**.

  8. When you're done removing releases to your product, click **Save and Validate**.

  9. Click **Submit** to submit the container images for review.

  10. After all reviews have been approved, you can publish and launch the product by opening the **Overview** page of your product, and clicking **Publish**.




[ Previous arrow_back  Setting up the technical components  ](https://docs.cloud.google.com/marketplace/docs/partners/container-setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
