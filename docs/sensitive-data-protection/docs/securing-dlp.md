---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/securing-dlp/
title: Securing Sensitive Data Protection resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:20.414770+00:00
---

# Securing Sensitive Data Protection resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/securing-dlp/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Securing Sensitive Data Protection resources Stay organized with collections  Save and categorize content based on your preferences. 

Using VPC Service Controls, you can control how Sensitive Data Protection accesses your data. VPC Service Controls enables you to define a security perimeter around your projects and resources, including Sensitive Data Protection resources. This lets you control communication to Sensitive Data Protection and between Sensitive Data Protection and other Google Cloud services.

VPC Service Controls provides additional security for your Google Cloud resources to help mitigate the risk of data exfiltration. Using VPC Service Controls, you can add projects to service perimeters that protect resources and services from requests that originate outside the perimeter.

To learn more about service perimeters, see the [Service perimeter configuration page](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) in the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Set up a service perimeter around Sensitive Data Protection

To learn how to set up a new service perimeter to prohibit external access to Sensitive Data Protection resources, follow the instructions in [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters). Be aware of the following Sensitive Data Protection-specific options:

  * When you're asked to add the projects that you want to secure, select the project (or projects) that contains the Sensitive Data Protection resources that you want to protect.
  * When you're asked to specify the services that you want to secure within the perimeter, type `dlp` into the **Filter services** field, and then choose **Sensitive Data Protection** from the list.



When you secure Sensitive Data Protection inside a service perimeter, be aware that any services that Sensitive Data Protection interacts with will need to be secured within the same perimeter.

For information about how to allow Sensitive Data Protection to discover data within a VPC Service Controls perimeter, see [Allow sensitive data discovery within service perimeters](https://docs.cloud.google.com/sensitive-data-protection/docs/allow-discovery-vpcsc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
