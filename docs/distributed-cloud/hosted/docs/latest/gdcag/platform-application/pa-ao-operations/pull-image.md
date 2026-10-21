---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/pull-image/
title: Pull an image with Docker \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:45:32.424244+00:00
---

# Pull an image with Docker  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/pull-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Pull an image with Docker Stay organized with collections  Save and categorize content based on your preferences. 

Pull an image from a Harbor project in the Docker client to download the specified container image from your Harbor registry to your local machine. This lets you run the containerized application locally or use it as a base image for building other images.

## Before you begin

To pull an image with Docker, you must configure your environment with the necessary resources and permissions, including an existing Harbor project with the container image you want to pull. For more information, see [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects).

### Required IAM roles

To pull images from Harbor registry instances, contact your Project IAM Admin to request the **Harbor Instance Viewer** (`harbor-instance-viewer`) role, which lets you get, list, and watch Harbor instances in the project namespace. This role includes the required permissions to view the details of existing Harbor instances so you can retrieve the registry URLs required for pulling images.

### Required Harbor RBAC roles

Unlike GDC IAM roles, pulling images requires specific permissions within Harbor's internal role-based access control (RBAC) system. Request the necessary permissions from your administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Limited Guest** : required to pull images from a Harbor repository. For more information on all available roles, see the Harbor documentation on User permissions by role: <https://goharbor.io/docs/2.8.0/administration/managing-users/user-permissions-by-role/>.



## Pull an image

Follow these steps to pull an image from a Harbor project in the Docker client:

  1. Make sure that you are [authenticated](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication) to the Harbor instance.
  2. Pull the image from a Harbor project:
         
         docker pull INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE:TAG
         

or
         
         docker pull INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE@IMAGE_DIGEST
         




Replace the following values:

  * `INSTANCE_URL`: the URL of the Harbor instance. For example, `harbor-1.org-1.zone1.google.gdc.test.` You can get the URL of the Harbor instance using the [GDC console or gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).
  * `HARBOR_PROJECT_NAME`: the name of the Harbor project. For example, `my-project`.
  * `IMAGE`: the image's name. For example, `nginx`.
  * `TAG`: the tag for the image version that you want to pull. For example, `staging`.
  * `IMAGE_DIGEST`: the sha256 hash value of the image contents. Each version of an image has a unique image digest. In the Harbor instance UI, click the specific image to see its digest. For more information, see [View Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).



## What's next

After you've confirmed the connection by pulling an image, you can use your artifacts to launch the application in your environment:

  * [Deploy a container app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/deploy-container-workloads)
  * [Configure tag retention rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-tag-retention-rules)
  * [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
