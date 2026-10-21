---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/pull-image/
title: Pull an image with Docker \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:11.142176+00:00
---

# Pull an image with Docker  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/pull-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Pull an image with Docker Stay organized with collections  Save and categorize content based on your preferences. 

Pull an image from a Harbor project in the Docker client to download the specified container image from your Harbor registry to your local machine. This lets you run the containerized application locally or use it as a base image for building other images.

## Before you begin

To pull an image with Docker, you must have access to the following:

  * The necessary identity and access role. Ask your Organization IAM Admin to grant you the Harbor Instance Viewer (`harbor-instance-viewer`) role.
  * An account with the `Limited Guest` role from Harbor's role-based access controls. For more information, see [Configure access for APIs and within a Harbor instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-access-control#configure-access-within-harbor-instance).
  * An existing Harbor project. For more information, see [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/create-harbor-projects).
  * An existing container image in the existing Harbor project.



## Pull an image

Follow these steps to pull an image from a Harbor project in the Docker client:

  1. Make sure that you are [authenticated](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication) to the Harbor instance.
  2. Pull the image from a Harbor project:
         
         docker pull INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE:TAG
         

or
         
         docker pull INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE@IMAGE_DIGEST
         




Replace the following values:

  * `INSTANCE_URL`: the URL of the Harbor instance. For example, `harbor-1.org-1.zone1.google.gdc.test.` You can get the URL of the Harbor instance using the [GDC console or gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).
  * `HARBOR_PROJECT_NAME`: the name of the Harbor project. For example, `my-project`.
  * `IMAGE`: the image's name. For example, `nginx`.
  * `TAG`: the tag for the image version that you want to pull. For example, `staging`.
  * `IMAGE_DIGEST`: the sha256 hash value of the image contents. Each version of an image has a unique image digest. In the Harbor instance UI, click the specific image to see its digest. For more information, see [View Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
