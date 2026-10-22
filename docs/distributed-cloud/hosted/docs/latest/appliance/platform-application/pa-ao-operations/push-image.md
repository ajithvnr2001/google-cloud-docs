---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/push-image/
title: Push an image \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:04.857611+00:00
---

# Push an image  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/push-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Push an image Stay organized with collections  Save and categorize content based on your preferences. 

Push images to Harbor for enhanced security with role-based access control, automated vulnerability scanning, and simplified image management for your containerized applications. To push a local image to a Harbor instance, tag it with the repository name and then push the image.

## Before you begin

To push an image, you must configure your environment with the necessary resources and permissions, including an existing Harbor project. For more information, see [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/create-harbor-projects).

### Required IAM roles

To push images to Harbor registry instances, contact your Project IAM Admin to request the following role:

  * **Harbor Instance Viewer** (`harbor-instance-viewer`): get, list, and watch Harbor instances in the project namespace. This role includes the required permissions to view the details of existing Harbor instances so you can retrieve the registry URLs required for pushing images.



### Required Harbor RBAC roles

Unlike GDC IAM roles, pushing images requires specific permissions within Harbor's internal role-based access control (RBAC) system. Request the necessary permissions from your administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Developer** : required to push images to a Harbor repository. For more information on all available roles, see the Harbor documentation on User permissions by role: <https://goharbor.io/docs/2.12.0/administration/managing-users/user-permissions-by-role/>.



## Tag the local image

Follow these steps to tag a local image with the repository name:

  1. You must be authenticated to the Harbor instance. For more information, see [Configure Docker authentication to Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication).
  2. Set the name of the image. The format of a full image name is:
         
         INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE
         

Replace the following:

     * `INSTANCE_URL`: the URL of the Harbor instance. For example, `harbor-1.org-1.zone1.google.gdc.test`. Get the URL of the Harbor instance using [GDC console or gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).
     * `HARBOR_PROJECT_NAME`: the name of the Harbor project. For example, `my-project.`
     * `IMAGE_NAME`: the image's name. For example, `nginx.`

An example of the full image name might look like the following:
    
    harbor-1.org-1.zone1.google.gdc.test/my-project/nginx
    

  3. Tag the local image with the repository name:
         
         docker tag SOURCE-IMAGE
         INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE:TAG
         
         




Replace the following:

  * `SOURCE-IMAGE`: the local image name or image ID. For example, `nginx`.
  * `TAG`: the tag name. For example, `staging`. If you don't specify a tag, Docker applies the latest tag by default.



## Push the tagged image to a Harbor registry instance

After the image is tagged, push it to the Harbor registry instance:

  1. Make sure that you are [authenticated](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication) to the Harbor instance.
  2. Push the tagged image with the command:


    
    
    docker push
    INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE:TAG
    

When you push an image, it is stored in the specified instance and Harbor project.

After pushing your image, go to the [Harbor instance UI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances) to view the image.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
