---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/set-service-perimeter/
title: Adding Cloud Service Mesh (In-cluster) services to the service perimeters \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:19.342094+00:00
---

# Adding Cloud Service Mesh (In-cluster) services to the service perimeters  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/set-service-perimeter/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Adding Cloud Service Mesh (In-cluster) services to the service perimeters

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

If you have created a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) in your organization, you must add the [Certificate Authority](https://docs.cloud.google.com/service-mesh/v1.24/docs/unified-install/plan-install#choose_a_certificate_authority) (Cloud Service Mesh certificate authority or Certificate Authority Service), Mesh Configuration, Stackdriver logging, Cloud Monitoring, and Cloud Trace services to the perimeter, in the following cases:

  * The cluster on which you have installed Cloud Service Mesh is in a project that is included in a service perimeter.
  * The cluster on which you have installed Cloud Service Mesh is a _service project_ in a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc).



By adding these services to the service perimeter, your Cloud Service Mesh cluster can access these services. Access to the services is also restricted within your cluster's Virtual Private Cloud (VPC) network.

Not adding the aforementioned services may cause the Cloud Service Mesh installation to fail or cause functions to be missing. For example, if you don't add Cloud Service Mesh certificate authority to the service perimeter, the workloads can not get certificates from the Cloud Service Mesh certificate authority.

## Before you begin

The setup for the VPC Service Controls service perimeter is at the [organization level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Ensure that you have been granted the [proper roles for administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control). If you have multiple projects, you can apply the service perimeter to all of the projects by [adding each project to the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

## Adding Cloud Service Mesh services to an existing service perimeter

### Console

  1. Follow the steps in [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to edit the perimeter.
  2. On the **Edit VPC Service Perimeter** page, under **Services to protect** , click **Add Services**.
  3. On the **Specify services to restrict** dialog, click **Filter services**. Depending on your Certificate Authority (CA), enter either **Cloud Service Mesh Certificate Authority API** or **Certificate Authority Service API**.
  4. Select the service's checkbox.
  5. Click **Add Cloud Service Mesh Certificate Authority API**.
  6. Repeat steps 2 - 5, to add: 
     * **Mesh Configuration API**
     * **Cloud Monitoring API**
     * **Cloud Trace API**
  7. Click **Save**.



### gcloud

To update the list of restricted services, use the `update` command and specify the services to add as a comma-delimited list:

**Note:** If your service mesh uses Certificate Authority Service, then replace `meshca.googleapis.com` with `privateca.googleapis.com` in the following command.
    
    
    gcloud access-context-manager perimeters update PERIMETER_NAME \
      --add-restricted-services=meshconfig.googleapis.com,meshca.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com,OTHER_SERVICES \
      --policy=POLICY_NAME

Where:

  * PERIMETER_NAME is the name of the service perimeter that you want to update.

  * OTHER_SERVICES is an optional comma-separated list of one or more services to include in the perimeter in addition to the services populated in the preceding command. For example: `storage.googleapis.com,bigquery.googleapis.com`.

  * POLICY_NAME is the numeric name of your organization's access policy. For example, `330193482019`.




Refer to [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) for additional information. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


