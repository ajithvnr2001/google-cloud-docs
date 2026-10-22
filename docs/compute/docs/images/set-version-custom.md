---
url: https://docs.cloud.google.com/compute/docs/images/set-version-custom/
title: Set the image version in an image family \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:04.497921+00:00
---

# Set the image version in an image family  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/set-version-custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set the image version in an image family Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Use image families to simplify image versioning. Add an image to an image family to set it as the most recent image version. If you determine that you must roll back the image family to a previous image version, deprecate the most recent image in the family.

For best practices when working with image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

Optionally, you can specify the image's storage location by using the Google Cloud console, the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) with the `--storage-location` flag, or the [`images().insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert).

## Before you begin

  * Read the [Images](https://docs.cloud.google.com/compute/docs/images) document.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Set the image version in an image family

###  Console 

  1. In the Google Cloud console, go to the **Create an image** page.

[Go to Create an image](https://console.cloud.google.com/compute/imagesAdd)

  2. Specify the **Name** of your image. For example, `image-v1`.

  3. Specify the **Source** from which you want to create an image. This can be a persistent disk, a snapshot, another image, or a disk.raw file in Cloud Storage.

  4. If you are creating an image from a disk attached to a running VM, check **Keep instance running** to confirm that you want to create the image while the VM is running. You can prepare your VM before creating the image.

  5. In the **Based on source disk location (default)** drop-down list, specify the location to store the image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you do not make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.

  6. Specify the image **Family** for the new image. For example, add `my-image-family` to organize the image as part of an [image family](https://docs.cloud.google.com/compute/docs/images#image_families).

  7. Optional: specify other image properties:

     * **Description** : a description for your custom image.
     * **Label** : a [label](https://docs.cloud.google.com/compute/docs/labeling-resources) to group together resources.
  8. Specify the encryption key. You can choose between a Google-owned and Google-managed encryption key, a [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) key or a [customer- supplied encryption (CSEK)](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) key. If no encryption key is specified, images are encrypted using a Google-owned and Google-managed encryption key.

  9. Click **Create** to create the image.




###  gcloud 
    
    
    gcloud compute images create image-v1 \
        --source-disk disk-1 \
        --source-disk-zone us-central1-f \
        --family my-image-family
    

The image family points to `image-v1`. Add a second image to the family:
    
    
    gcloud compute images create image-v2 \
        --source-disk disk-2 \
        --source-disk-zone us-central1-f \
        --family my-image-family
    

###  REST 

Make a `POST` request to the [`images().insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/images/insert). Specify the image family in the request body.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    
    {
      "name": "image-v2",
      "sourceDisk": "/zones/us-central1-f/disks/disk-2",
      "family":"my-image-family",
    
    }
    

The image family points to `image-v2` because it is the most recent image that you added to the image family.

###  gcloud 

You can see which image a family points to by running the [`gcloud compute images describe-from-family` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family).

For example:
    
    
    gcloud compute images describe-from-family my-image-family
    
    family: my-image-family
    id: '8904691942610171306'
    kind: compute#image
    name: image-v2
    selfLink: https://compute.googleapis.com/compute/v1/projects/my-project/global/images/image-v2
    sourceDisk: https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/disks/disk-v2
    sourceDiskId: '1677449456001963379'
    sourceType: RAW
    status: READY
    

###  REST 

Make a `GET` request to the [`images().getFromFamily` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getFromFamily). Specify the image family in the request body.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/family
    
    {
      "resourceId":"my-image-family",
    
    }
    

If you determine that you must roll back the image family so that it no longer points to `image-v2`, deprecate `image-v2` and the family will again point to `image-v1`.
    
    
    gcloud compute images deprecate image-v2 \
        --state DEPRECATED \
        --replacement image-v1
    

Check to make sure that the image family is pointing to `image-v1`.
    
    
    gcloud compute images describe-from-family my-image-family
    
    family: my-image-family
    id: '2741732787056801255'
    kind: compute#image
    name: image-v1
    selfLink: https://compute.googleapis.com/compute/v1/projects/my-project/global/images/image-v1
    sourceDisk: https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/disks/disk-v1
    sourceDiskId: '1677449456001963379'
    sourceType: RAW
    status: READY
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
