---
url: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/configure-vpc-sc/
title: Configure VPC Service Controls for the Data Engineering Agent \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:53.048973+00:00
---

# Configure VPC Service Controls for the Data Engineering Agent  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/configure-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Configure VPC Service Controls for the Data Engineering Agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to configure VPC Service Controls to support the Data Engineering Agent. You can use VPC Service Controls with the Data Engineering Agent to mitigate the risk of data exfiltration.

To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Limitations

  * Gemini Data Analytics (`geminidataanalytics.googleapis.com`), Dataform (`dataform.googleapis.com`), BigQuery (`bigquery.googleapis.com`), Knowledge Catalog (`dataplex.googleapis.com`), and Cloud Storage (`storage.googleapis.com`) must all be restricted within the same VPC Service Controls service perimeter.
  * The same limitations that apply to Dataform within a VPC Service Controls perimeter also apply when using Gemini Data Analytics. This includes the requirement to set the `dataform.restrictGitRemotes` organization policy. For more information, see [Limitations](https://docs.cloud.google.com/dataform/docs/vpc-service-controls#limitations).



## Security considerations

When you set up a VPC Service Controls perimeter for Gemini Data Analytics, review the permissions granted to your service agents and accounts, including Dataform service agents and any custom service accounts, to ensure alignment with your security architecture. The permissions granted to these accounts determine their access to resources within the perimeter.

## Before you begin

  * Ensure that the users or service accounts using Gemini Data Analytics have the necessary IAM permissions. You can grant the role `roles/geminidataanalytics.dataAgentStatelessUser`, which includes the required permission `geminidataanalytics.locations.useDataEngineeringAgent`. These IAM roles are required to interact with the Gemini Data Analytics API, even when calls originate within a VPC Service Controls perimeter.
  * Before configuring a VPC Service Controls service perimeter, you must set the `dataform.restrictGitRemotes` organization policy. This policy ensures that VPC Service Controls enforces checks when you use Dataform features through Gemini Data Analytics. For more information, see [Restrict remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes).



### Enable APIs

Enable the Gemini Data Analytics, Dataform, BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=geminidataanalytics.googleapis.com,dataform.googleapis.com,bigquery.googleapis.com)

### Required roles

To get the permissions that you need to configure VPC Service Controls service perimeters, ask your administrator to grant you the [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about VPC Service Controls permissions, see [Access control with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

## Configure VPC Service Controls

When you [create a new service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters), you must include the following APIs in the same service perimeter:

  * `geminidataanalytics.googleapis.com`
  * `dataform.googleapis.com`
  * `bigquery.googleapis.com`
  * `dataplex.googleapis.com`
  * `storage.googleapis.com`



If you have an existing service, you can [update the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to include the three required APIs within the same service perimeter.

## What's next

  * To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * To learn more about VPC Service Controls integration in Dataform, see [Configure VPC Service Controls for Dataform](https://docs.cloud.google.com/dataform/docs/vpc-service-controls).
  * To learn more about VPC Service Controls integration in BigQuery, see [VPC Service Controls for BigQuery](https://docs.cloud.google.com/bigquery/docs/vpc-sc).
  * To learn more about the Organization Policy Service, see [Introduction to the Organization Policy Service Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
