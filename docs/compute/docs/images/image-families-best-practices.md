---
url: https://docs.cloud.google.com/compute/docs/images/image-families-best-practices/
title: Image families best practices \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:35:14.305415+00:00
---

# Image families best practices  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-families-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Image families best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document provides best practices for using image families to manage evolving versions of operating system (OS) images on Compute Engine. Image families let you group related images, which enables your automation tools to reference the latest versions while maintaining the ability to roll back.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




## Public image families

Compute Engine provides image families to help you ensure that your automation systems can reference the latest images. As an administrator, you can group a set of images as an image family. Then users of the images only have to keep track of the image-family name, rather than an exact image name. Because image names must be unique, image-build pipelines often create image names with information encoded in them, such as the application name, date, and version, for example, `my-application-v3-20210101`. In automation tools, you can reference the image family name instead of having to update the image name at intervals. Using image families ensures that you always access the latest image in the family, for example, `my-application`.

![Image families.](https://docs.cloud.google.com/static/solutions/images/using-image-families.svg)

[Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) are grouped into image families. A public image family always points to the latest version of an image that is available in each zone. When new images are released globally, their initial availability in image families is zone dependent, which improves zonal fault tolerance for your workflows during Google image updates.

During image rollout, the latest version of an image in an image family might differ in different zones. For example, the [`debian-12` image family](https://docs.cloud.google.com/compute/docs/images/os-details#debian) in the `debian-cloud` project always points to the most recent Debian 12 image, but the most recent Debian 12 image in zone `us-central1-a` and `southamerica-east1-b` might be different.

When you create VMs from image families using the Google Cloud CLI, Compute Engine uses the latest image that is available in your VM's zone for your request. When you create VMs using the Google Cloud console, Compute Engine only displays the public images available in your selected zone. If you want to create VMs using the latest globally available image, use the gcloud CLI [`instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and specify `--image-family-scope=global`.

### Viewing the latest available image version

You can view the latest globally available image in an image family, or view the latest image that is available in a particular zone.

#### Globally

To view the latest globally available image in an image family, use one of the following methods:

###  gcloud 

Use the [`gcloud compute images describe-from-family` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family):
    
    
    gcloud compute images describe-from-family IMAGE_FAMILY_NAME  \
       --project=IMAGE_PROJECT
    

Replace the following:

  * `IMAGE_FAMILY_NAME`: the name of the image family that you want to search. For a full list of image family names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the name of the image project. For a full list of image project names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).



###  REST 

Make a `GET` request to the [`images.getFromFamily` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getFromFamily):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY_NAME
    

Replace the following:

  * `IMAGE_PROJECT`: the name of the image project. For a full list of image project names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_FAMILY_NAME`: the name of the image family that you want to search. For a full list of image family names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).



#### Per zone

To view the latest available image in an image family for a specific zone, use one of the following methods:

###  gcloud 

Use the [`gcloud compute images describe-from-family` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe-from-family) with the `--zone` flag:
    
    
    gcloud compute images describe-from-family IMAGE_FAMILY_NAME  \
       --project=IMAGE_PROJECT \
       --zone=ZONE
    

Replace the following:

  * `IMAGE_FAMILY_NAME`: the name of the image family that you want to search. For a full list of image family names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the name of the image project. For a full list of image project names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `ZONE`: the zone you want to query.



###  REST 

Make a `GET` request to the [`imageFamilyViews` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/imageFamilyViews):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/IMAGE_PROJECT/zones/ZONE/imageFamilyViews/IMAGE_FAMILY_NAME
    

Replace the following:

  * `IMAGE_PROJECT`: the name of the image project. For a full list of image project names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `ZONE`: the zone you want to query.
  * `IMAGE_FAMILY_NAME`: the name of the image family that you want to search. For a full list of image family names, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).



## Custom image families

You can create custom image families for your [custom images](https://docs.cloud.google.com/compute/docs/images/create-custom). The image family points to the most recent image that you used to create the image family. To roll an image family back to a previous image version, you can deprecate the most recent image in that family, provided that the previous image is not deprecated. For more information, see [Setting image versions in an image family](https://docs.cloud.google.com/compute/docs/images/set-version-custom).

To create an image with an image family, or to create an image family if one doesn't exist, you must add an additional `--family` flag to the image create step, for example:
    
    
    gcloud compute images create my-application-v3-20210101 \
        --source-disk my-application-disk-1 \
        --source-disk-zone us-central1-f \
        --family my-application
    

After you run this command, any calls to run an instance based on the image `my-application` points to the newly created image, `my-application-v3-20210101`.

When selecting a name for your image family, review [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

## How to use image families

While image families let you reference the latest image, the latest image might introduce incompatibility with your application, which can cause issues in a production environment if it is not validated. If you want to make the most of the benefits of image families while reducing the risks, then we recommend that you test the latest referenced image from the image family before using it in your production environment.

In summary, you can consider the following approach:

  * Set up a testing environment separate from your production environment.
  * In the testing environment, complete the following steps: 
    * Create a custom image family from the source image family.
    * Verify the stability of the new image in the custom image family against your workloads.
  * Once verified, move this custom image family to a production environment.



For example, the process might resemble the following procedure.

  1. In your test project, create an image from the source image family. This new image source family must also have its own custom image family to reference in the test environment. To create the image with a custom image family, run the following command:
         
         gcloud compute images create test-image-name \
         --source-image-project source-project \
         --source-image-family source-image-family \
         --project test-project \
         --family test-image-family
         

Replace the following:

     * `test-image-name`: name of your test image.
     * `source-project`: project that the source image family belongs to.
     * `source-image-family`: name of the source image family.
     * `test-project`: name of the test project that you want to add the image family to.
     * `test-image-family`: name of your test image family.
  2. Using your custom image family `test-image-family`, create a VM to test your workload. To create the VM, run the following command:
         
         gcloud compute instances create test-instance-name \
         --image-family your-test-image-family \
         --project test-project
         

Replace the following:

     * `test-instance-name`: name of your test instance.
     * `test-image-family`: name of your test image family.
     * `test-project`: name of your test project.
  3. When you have validated that this image works well for your workload, copy the image to your production environment.
         
         gcloud compute images create prod-image-name \
         --source-image-family test-image-family \
         --source-image-project test-project \
         --project prod-project \
         --family prod-image-family
         

Replace the following:

     * `prod-image-name`: name of your production image.
     * `test-image-family`: name of your test image family.
     * `test-project`: project that the test image family belongs to.
     * `prod-project`: name of your project that is in the production environment.
     * `prod-image-family`: name of the image family that you want to use in your production environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
