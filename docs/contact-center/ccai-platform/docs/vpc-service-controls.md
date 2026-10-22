---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/vpc-service-controls/
title: VPC Service Controls \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:47.156907+00:00
---

# VPC Service Controls  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

You can use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) with Contact Center AI Platform (CCAI Platform) to help mitigate the risk of data exfiltration from your contact center. When you include a CCAI Platform instance within a VPC Service Controls perimeter, the instance is prevented from exchanging data with Google Cloud services (such as Cloud Storage or Dialogflow CX) that are outside of the perimeter. You can further secure your instance by including CCAI Platform API in your list of restricted services. You can then create an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) to allow only your administrators to access your instance.

Note that including an instance in your perimeter doesn't restrict the instance from exchanging data with third-party (non-Google Cloud) services. To restrict data exchange with third-party services, Google recommends using Private Service Connect to set up private ingress and private egress for your instance. For more information, see [Private Service Connect](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc).

## Create a perimeter and restrict access to an instance

You can create a perimeter and restrict the ability for users to create and edit CCAI Platform instances in the Google Cloud console. After doing this, use an access level to explicitly grant access to the users who you want to create and edit instances. For more information, see Allow access to your protected resources.

To create a perimeter and restrict access to an instance, follow the instructions in [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) while meeting these requirements:

  * When you are adding resources in the **Resources to protect** pane, select the project that contains the CCAI Platform instance that you want to include in the perimeter.

  * When you are restricting services in the **Restricted Services** pane, select **CCAI Platform API**.




Your instance is now within a perimeter, and you have specified CCAI Platform API as a restricted service. This means that no user can create or edit a CCAI Platform instance within your perimeter unless you use an access level to explicitly grant them access to do so. For more information, see Allow access to your protected resources.

## Agent adapter dependencies

The agent adapter depends on the following services:

  * [Identity Platform](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_identity_platform)

  * [Cloud Storage](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage)

  * [Firestore](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_firestore)




If you choose to restrict these services by including them in the list of restricted services in your perimeter, the following APIs cannot be called from outside the perimeter:

  * `identitytoolkit.googleapis.com` (from the Identity Platform service)

  * `securetoken.googleapis.com` (from the Identity Platform service)

  * `storage.googleapis.com` (from the Cloud Storage service)

  * `firestore.googleapis.com` (from the Firestore service)




The agent adapter depends on these APIs, so if you restrict them you need to allow access to them for your agent adapter users. For more information, see Allow access to your protected resources.

## Allow access to your protected resources

This section shows you how to allow access to your protected resources.

### Configure an access level

Configure an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) to allow access to any resources that you restricted in Create a perimeter and restrict access to an instance.

To create an access level, follow the instructions in [Create an access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels#create_an_access_level) while meeting these requirements:

  * Specify a condition that allows your administrators to access the restricted CCAI Platform API service. This will let them manage instances in the Google Cloud console. The condition must include an [access level attribute](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes) of your administrators.

  * Optional (if you restricted the Identity Platform, Cloud Storage, or Firestore services): specify a condition that allows the users of the agent adapter to access the restricted Identity Platform, Cloud Storage, or Firestore services. The condition must include an [access level attribute](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes) of your users of the agent adapter.




### Private Google Access

If your use case requires it, you can use Private Google Access to allow access to restricted resources within a perimeter instead of using an access level. For more information, see [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
