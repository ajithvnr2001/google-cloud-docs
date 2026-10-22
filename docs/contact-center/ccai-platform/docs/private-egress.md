---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-egress/
title: Set up private egress \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:32.614856+00:00
---

# Set up private egress  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-egress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Set up private egress Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If your Contact Center AI Platform (CCAI Platform) instance is set up for data egress to services that support capabilities such as CRM apps, media storage, or co-browse, you can use Private Service Connect to set up private egress to these services, keeping your traffic private and within Google Cloud.

## Before you begin

The following list contains egress components for the types of data that an instance sends out, along with instructions for setting up data egress to services that receive that data:

  * **`CRM`**. For more information, see [CCAI Platform portal configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Custom_CRM#ccai_platform_portal_configuration).

  * **`MEDIA`**. For more information, see [External storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage).

  * **`DIRECT_ACCESS_POINT`**. For more information, see [API DAPs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#api-daps).

  * **`EMAIL`**. For more information, see [Email channel configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config).

  * **`COBROWSE`**. For more information, see [Set up co-browse](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-cobrowse).




Keep the following points in mind when setting up data egress from a CCAI Platform instance:

  * The host URL that you specify when you set up data egress must be a URL containing the fully qualified domain name (FQDN) of the target service. Specifying an IP address causes egress to be blocked.

  * The certificates of the FQDNs that you specify when setting up data egress must be publicly available.




## Publish a service

Publishing a service makes it available to receive private egress traffic from a CCAI Platform instance. To [publish a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service), you create a service attachment in the project that contains the service. The instance that you configure for private egress uses the service attachment details to connect to the service. Publishing a service also includes creating an internal load balancer that directs the egress traffic to the service.

To publish a service, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains the service that you want to publish.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Publish your service according to the instructions in [Publish a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).

  3. Save the service attachment value to use in Configure a CCAI Platform instance for private egress.




Keep the following points in mind when you publish a service:

  * When you create a service connection, set a connection limit of at least 10 additional endpoints. Google recommends setting the connection limit to a much higher number to ensure that you have the capacity to connect as many endpoints as required.

  * If you've set up data egress for multiple egress components, it's possible that the egress traffic for both components is directed to the same service. For example, you might send both `MEDIA` egress traffic and `CRM` egress traffic to the same external storage service. In that case, use the same service attachment for both types of egress traffic. Otherwise, the behavior of the egress traffic is undefined.




## Configure a CCAI Platform instance for private egress

You can create a new instance configured for private egress or update an existing instance for private egress, depending on your situation.

Do one of the following:

  * Create a new instance configured for private egress.

  * Configure an existing instance for private egress.




Keep the following points in mind when you configure a CCAI Platform instance for private egress:

  * When you configure an instance for private egress to a Google Cloud service such as Cloud Storage, you don't need to publish a service to implement private egress because the request will use [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).

  * If the instance that you configure for private egress is within a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter, then the service attachment from your published service needs to be within that perimeter. Otherwise you'll generate a VPC Service Controls violation.




### Create a new instance configured for private egress

To create a new instance configured for private egress, do the following:

  * Create an instance as described in [Get started with Contact Center AI Platform](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started) and include the optional steps for configuring private egress.



After your private egress settings are saved, they appear under **Private access** on your instance's detail page.

### Configure an existing instance for private egress

To configure an existing instance for private egress, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains the instance that you want to edit.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

The **CCAI Platform instances** page appears.

  3. In the **Name** column, click the instance that you want to edit. The **CCAI Platform Detail** page appears.

  4. Click **Edit** , and then click **Configure private access**.

  5. To configure private egress ([Preview](https://cloud.google.com/products/#product-launch-stages)), do the following:

     1. Under **Egress** , click **Add setting**. In the **Component type** field, select the component type for the type of data that you're configuring private egress for. For more information, see [Components](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints#components).

     2. In the **Service attachment** field, enter the service attachment that you created in Publish a service, and then click **Done**.

     3. Optional: Click **Add setting** and repeat the previous two steps for every additional private egress setting that you need.

     4. Click **Save**.




After your private egress settings are saved, they appear under **Private access** on your instance's detail page.

## What's next

  * [Set up private ingress](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-ingress)

  * [Custom constraints](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
