---
url: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vpcsc/
title: Enforce certificate-based access with VPC Service Controls \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:18.078317+00:00
---

# Enforce certificate-based access with VPC Service Controls  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Enforce certificate-based access with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

To protect Google Cloud services in your projects and mitigate the risk of data exfiltration, you can specify VPC Service Controls service perimeters at an organization, folder, or project level. Applying a service perimeter provides you with fine-grained control over the ingress policy as well as which services and resources to protect.

For more information about the benefits of service perimeters, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Applying a CBA ingress policy to service perimeters

Applying CBA access levels to service perimeters allows you to grant access to perimeter-protected resources from only trusted devices. For more information about creating a CBA access level, see [Create access levels for certificate-based access](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels).

The following diagram illustrates a basic example of restricting access to Cloud Storage sensitive data from unknown devices by associating a CBA access level with a service perimeter:

![Associate a CBA access
level with a service perimeter to restrict access](https://docs.cloud.google.com/access-context-manager/images/cba-vpcsc.svg)

To apply a CBA ingress policy to a service perimeter, complete the following steps:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Edit VPC Service Perimeter** page, click **Access Levels**.

  4. For the **Choose Access Level** , select the CBA access level.

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
