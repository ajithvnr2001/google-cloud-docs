---
url: https://docs.cloud.google.com/docs/quotas/configure-vpc-service-controls/
title: Configure VPC Service Controls for Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:31.390192+00:00
---

# Configure VPC Service Controls for Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Configure VPC Service Controls for Cloud Quotas Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Virtual Private Cloud (VPC) Service Controls lets you set up a secure perimeter to guard against data exfiltration. Configure Cloud Quotas with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) so that API requests to Cloud Quotas stay within the VPC service perimeter boundary.

## Limitations

Because VPC Service Controls enforces boundaries at the project level, Cloud Quotas requests that originate from clients within the perimeter can only access organization resources if the organization sets up an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). To set up an egress rule, see the VPC Service Controls instructions for [configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies)

## Enforced actions

VPC Service Controls is only enforced on the following Cloud Quotas actions:

  * [Quota preference](https://docs.cloud.google.com/docs/quotas/api-overview#quota_preference) creation, update, get and list.
  * [Quota info](https://docs.cloud.google.com/docs/quotas/api-overview#quota_info) get and list.



For examples of setting [`QuotaPreference`](https://docs.cloud.google.com/docs/quotas/api-overview#quota_preference) and [`QuotaInfo`](https://docs.cloud.google.com/docs/quotas/api-overview#quota_info), see the description of the [API resource model](https://docs.cloud.google.com/docs/quotas/api-overview#api_resource_model). For reference information, see the [REST API overview](https://docs.cloud.google.com/docs/quotas/reference/rest).

## Set up

Follow these steps to restrict the Cloud Quotas API to your VPC service perimeter:

  1. Follow the instructions to [set up the Cloud Quotas API](https://docs.cloud.google.com/docs/quotas/development-environment).

  2. Follow the [VPC Service Controls Quickstart](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter) to complete the following tasks:

     1. [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter#set-up-perimeter).
     2. [Add projects to the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter#add-projects-perimeter) that you want to protect.
     3. Restrict the Cloud Quotas API. For example, see these instructions that add [other Google Cloud APIs to the VPC service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter#secure-services-perimeter).



After setting up your service perimeter, VPC Service Controls checks calls to the Cloud Quotas API to help make sure that the calls originate from within the same perimeter.

## What's next

  * Learn about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * See the Cloud Quotas entry in the [VPC Service Controls supported products table](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_quotas).
  * Refer to the description of the Cloud Quotas [API resource model](https://docs.cloud.google.com/docs/quotas/api-overview#api_resource_model) for examples.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
