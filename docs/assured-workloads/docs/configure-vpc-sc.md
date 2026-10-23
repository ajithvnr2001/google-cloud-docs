---
url: https://docs.cloud.google.com/assured-workloads/docs/configure-vpc-sc/
title: Configure VPC Service Controls for Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:06.549532+00:00
---

# Configure VPC Service Controls for Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/configure-vpc-sc/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VPC Service Controls for Assured Workloads

## Overview

Assured Workloads helps you comply with different regulatory compliance frameworks by implementing logical controls that segment networks and users from in-scope sensitive data. Many of the US compliance frameworks are built upon [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), but have their own particular controls based on the sensitivity of the information and the framework's governing body. For customers who must comply with [FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high) or [DoD IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il4), we recommend that you use VPC Service Controls to create a strong boundary around the regulated environment.

VPC Service Controls provides an extra layer of security defense for Google Cloud services that is independent of Identity and Access Management (IAM). While Identity and Access Management enables granular identity-based access control, VPC Service Controls enables broader context-based perimeter security, such as controlling data ingress and egress across the perimeter. The controls VPC Service Controls are a logical boundary around Google Cloud APIs that are managed at the [organization level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) and applied and enforced at the [project level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). For a high-level overview of VPC Service Controls benefits and configuration stages, please see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview#benefits). For more information about the regulatory guidance, see [Control ID SC-7](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#/control?version=5.1&number=SC-7).

## Before you begin

  * Ensure that you've read and understand the purpose and usage of [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and its [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
  * Read about how access control in [VPC Service Controls works with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).
  * If you want to configure external access to your protected services when you create your perimeter, first [create one or more access levels](https://docs.cloud.google.com/access-context-manager/docs/create-access-level) before you create the perimeter.
  * Ensure that the Google Cloud services and their resources are [in scope for IL4](https://cloud.google.com/security/compliance/disa) or [in scope for FedRAMP High](https://cloud.google.com/security/compliance/fedramp) and are [supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).



## Configure VPC Service Controls for Assured Workloads

To configure VPC Service Controls, you can use the Google Cloud console, the Google Cloud CLI (gcloud CLI), or the [Access Context Manager APIs](https://docs.cloud.google.com/access-context-manager/docs/reference/rest). The following steps show you how to use the Google Cloud console.

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, select the _Dry run mode_. While you can create in either a _Dry run mode_ or an _Enforced mode_ , we recommend using the _Dry run mode_ first for either a new or updated service perimeter. _Dry run mode_ will also allow you to create a test run of your new service perimeter to see how it performs before you choose to enforce it within your environment.

  4. Click **New perimeter**.

  5. On the **New VPC Service Perimeter** page, in the **Perimeter Name** box, type a name for the perimeter.

  6. In the **Details** tab, select the desired perimeter type and configuration type.

  7. In the **Projects** tab, select the projects that you want to include within the service perimeter boundary. For your IL4 workloads, these should be the projects that are within your Assured Workloads IL4 folder.

**Note:** At this time, you can only select projects (and not folders) when setting up a service perimeter.
  8. In the **Restricted Services** tab, add services to include within the service perimeter boundary. You should only select services that are in scope for your Assured Workloads folder.

  9. (Optional) In the **VPC Accessible Services** tab, you can further restrict services within your service perimeter from communicating with each other. Assured Workloads will implement [resource usage restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) as a guardrail to ensure that services scoped to Assured Workloads can be deployed within your Assured Workloads folder. If you have overridden these controls, then you may need to implement _VPC Accessible Services_ to restrict non-Assured Workloads services from communicating with your workloads.

  10. Click **Ingress Policy** to set one or more rules that specify the direction of allowed access from different identities and resources. [Access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) only apply to requests for protected resources coming from outside the service perimeter. Access levels cannot be used to permit protected resources or VMs to access data and services outside the perimeter. You can to assign an identity different service methods to specific services in order to transfer regulated data into your workload's service perimeter.

  11. (Optional) Click **Egress Policy** to set one or more rules that specify the direction of allowed access to different identities and resources. [Access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) only apply to requests from protected resources to services outside the service perimeter.

  12. Click **Save**.




## Use VPC Service Controls with Terraform

You can use the Terraform to synchronize your Assured Workloads folder with a VPC Service Controls permit if you want your Assured Workloads regulated boundary to be aligned with your VPC Service Controls boundary. For more information, see the [Automatically Secured Folder Terraform example on GitHub](https://github.com/terraform-google-modules/terraform-google-vpc-service-controls/tree/master/examples/automatic_folder).

## What's next

  * Learn about the [FedRAMP High control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high).
  * Learn about the [IL4 control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il4).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
