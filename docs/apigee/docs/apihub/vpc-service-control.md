---
url: https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control/
title: VPC Service Controls for API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:03.718769+00:00
---

# VPC Service Controls for API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  VPC Service Controls for API hub Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page provides an overview of using VPC Service Controls for API hub, covering service perimeter configuration, perimeter verification, and known limitations.

## VPC Service Controls for API hub

API hub integrates with VPC Service Controls to provide enhanced network security for your API hub instance provisioned in Google Cloud. VPC Service Controls enables you to establish a service perimeter around your API hub resources, constraining ingress and egress traffic. This perimeter helps to: 

  * **Limit unauthorised access:** Control which Google Cloud services and VPC networks can access your API hub resources.
  * **Prevent data exfiltration:** Mitigate the risk of unauthorized download or export of API definitions, metadata, and other sensitive data stored within API hub.
  * **Meet compliance requirements:** Support your organization's compliance and regulatory obligations by enforcing strict access controls.



For more information about VPC Service Controls, see the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

  * Read about [configuring service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
  * Read about [management of VPC networks in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management).
  * Ensure that you have the required IAM role permissions to configure service perimeters. See [VPC Service Controls access control with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).



## Configure VPC Service Controls for API hub

To configure VPC Service Controls, you can use the Google Cloud console, the `gcloud` tool, or the [Access Context Manager APIs](https://docs.cloud.google.com/access-context-manager/docs/apis). Perform the following steps: 

  1. Create an access policy for API hub. For more information, see [Create an access policy](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#create-access-policy).
  2. Create a service perimeter that includes the API hub (`apihub.googleapis.com`) service. For more information, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).



For information about the other optional VPC Service Controls configurations, see [Service perimeter configuration stages](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#stages).

## Verify service perimeters

Verify and list the service perimeters created for API hub using the following `gcloud` command: 
    
    
    gcloud access-context-manager perimeters describe PERIMETER_NAME. 
    

For more information about managing service perimeters, see [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).

## Limitations

All Apigee runtime projects associated with an API hub instance must reside within the same VPC Service Controls service perimeter as the API hub host project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
