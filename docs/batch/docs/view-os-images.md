---
url: https://docs.cloud.google.com/batch/docs/view-os-images/
title: View VM OS images for Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:20.803402+00:00
---

# View VM OS images for Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/view-os-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  View VM OS images for Batch Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the operating system (OS) images available for the virtual machine (VM) instances that run Batch jobs.

Specifically, this page describes how to view a list and details of VM OS images from Batch. To learn more about VM OS images and which VM OS images you can use with Batch, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview). If you want to view other VM OS images, such as public images from Compute Engine or custom images, see the [Compute Engine images documentation](https://docs.cloud.google.com/compute/docs/images) instead.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).



## View a list of VM OS images from Batch

You can view a list of all the VM OS images from Batch using the gcloud CLI or Batch API.

###  gcloud 

To list all supported VM OS images from Batch, use the following [`gcloud compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list):
    
    
    gcloud compute images list \
        --project=batch-custom-image \
        --no-standard-images
    

  * The `--project=batch-custom-image` flag is required to list images from Batch.
  * The `--no-standard-images` flag omits the standard images from Compute Engine.
  * Optional: if you need to see deprecated Batch images, also include the `--show-deprecated` flag.



The output for each VM OS image is similar to the following:
    
    
    NAME: IMAGE_NAME
    PROJECT: IMAGE_PROJECT_ID
    FAMILY: IMAGE_FAMILY
    ...
    

This output includes the following values:

  * `IMAGE_NAME`: the name of the image. An image name represents a specific version of a VM OS image. For example, the image name `batch-cos-stable-official-20260730-00-p01` represents image version `-20260730-00-p01` (the version from July 30, 2026) for the image family `batch-cos-stable-official`.
  * `IMAGE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the image. For example, all images from Batch images are in the `batch-custom-image` project.
  * `IMAGE_FAMILY`: the family of the image. An image family includes one or more specific images and represents the type and [major version](https://en.wikipedia.org/wiki/Software_versioning) of the OS. For example, the `batch-debian-12-official` image family contains Batch images based on OS version 12 of [Debian from Compute Engine](https://docs.cloud.google.com/compute/docs/images/os-details#debian).



###  API 

To list all supported VM OS images from Batch, make the following request to the [`images.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/batch-custom-image/global/images?filter=(-deprecated%3A*)%20OR%20(deprecated.state%3D%22ACTIVE%22)
    

  * The `batch-custom-image` project is required to list images from Batch.
  * The `?filter=(-deprecated%3A*)%20OR%20(deprecated.state%3D%22ACTIVE%22)` query parameter omits deprecated images by using [URL-encoding](https://en.wikipedia.org/wiki/URL_encoding) to set the `filter` field to `(-deprecated:*) OR (deprecated.state="ACTIVE")`. 
    * Optional: if you need to see deprecated Batch images, remove the `?filter=(-deprecated%3A*)%20OR%20(deprecated.state%20%3D%20%22ACTIVE%22)` query parameter.



The output for each VM OS image is similar to the following:
    
    
    {
      ...
      "name": "IMAGE_NAME",
      ...
      "family": "IMAGE_FAMILY",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/IMAGE_PROJECT_ID/global/images/IMAGE_NAME",
      ...
    }
    

This output includes the following values:

  * `IMAGE_NAME`: the name of the image. An image name represents a specific version of a VM OS image. For example, the image name `batch-cos-stable-official-20260730-00-p01` represents image version `-20260730-00-p01` (the version from July 30, 2026) for the image family `batch-cos-stable-official`.
  * `IMAGE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the image. For example, all images from Batch images are in the `batch-custom-image` project.
  * `IMAGE_FAMILY`: the family of the image. An image family includes one or more specific images and represents the type and [major version](https://en.wikipedia.org/wiki/Software_versioning) of the OS. For example, the `batch-debian-12-official` image family contains Batch images based on OS version 12 of [Debian from Compute Engine](https://docs.cloud.google.com/compute/docs/images/os-details#debian).



## View details of a VM OS image from Batch

You can view all the details of a VM OS image using the gcloud CLI or Batch API.

###  gcloud 

To view the details of a VM OS image from Batch, use the [`gcloud compute images describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe) and specify `batch-custom-image` as the image project:
    
    
    gcloud compute images describe IMAGE_NAME --project=batch-custom-image
    

Replace `IMAGE_NAME` with the name of the VM OS image from Batch that you want to describe.

###  API 

To view the details of a VM OS image from Batch, make a request to the [`images.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/get) and specify `batch-custom-image` as the image project:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/batch-custom-image/global/images/IMAGE_NAME
    

Replace `IMAGE_NAME` with the name of the VM OS image from Batch that you want to describe.

## What's next

  * Learn more about VM OS images for Batch: 
    * [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview)
    * [Specify the VM OS image for a job](https://docs.cloud.google.com/batch/docs/specify-vm-os-image)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
