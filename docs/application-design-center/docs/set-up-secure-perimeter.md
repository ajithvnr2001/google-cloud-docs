---
url: https://docs.cloud.google.com/application-design-center/docs/set-up-secure-perimeter/
title: Deploy resources in a service perimeter \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:33.031357+00:00
---

# Deploy resources in a service perimeter  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/set-up-secure-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Deploy resources in a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To guard against data exfiltration, create a service perimeter around your App Design Center resources. The perimeter protects App Design Center resources in your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), including application templates and applications. You create a service perimeter using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) with [Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

**Warning:** If you share a catalog between two spaces in your perimeter, and later remove the receiving space from your perimeter, sharing will continue. To stop sharing the catalog, see [Stop sharing a catalog with a space](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs#manage-spaces-shared-with-a-catalog).

## Configure a service perimeter

To configure your service perimeter, do the following:

  1. Complete the steps in [Use VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls), including the following:

     1. Create the worker pool in a project in the perimeter.

     2. The Cloud Build job needs to access the public internet to download Terraform modules and providers. To create network rules to allow access, see [Enable public internet calls on the VPC network](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#enable-public-internet).

     3. In the service perimeter, add [management projects](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) where you set up App Design Center.

  2. Grant the WorkerPool User (`roles/cloudbuild.workerPoolUser`) role to your deployment service account.

For instructions, see [IAM permissions](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool#permissions).

  3. If you are using a restricted VIP to restrict access to a VPC Service Controls-enabled service, configure DNS to resolve `*.googleapis.com` to the restricted VIP.

For instructions, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain).

  4. If you have existing application deployments, redeploy your applications to integrate them with your VPC Service Controls perimeter:

     1. [Preview](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/preview) and [deploy](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/deploy) your applications using the `--worker-pool` flag.

     2. Specify the worker pool in the following format: `projects/{project}/locations/{location}/workerPools/{workerPoolId}`.




## What's next

To preview and deploy applications, specify your worker pool in the following commands:

  * [gcloud design-center spaces applications preview](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/preview)

  * [gcloud design-center spaces applications deploy](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/deploy)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
