---
url: https://docs.cloud.google.com/oracle/database/docs/manage-instances/
title: Manage Exadata Infrastructure instances \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:00.284436+00:00
---

# Manage Exadata Infrastructure instances  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage Exadata Infrastructure instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage an Exadata Infrastructure instance in Google Cloud.

In Oracle Database@Google Cloud, you can modify an Exadata Infrastructure instance using Oracle Cloud Infrastructure (OCI). To create an instance, see [Create instances](https://docs.cloud.google.com/oracle/database/docs/create-instances). To learn more about how to manage an Exadata Infrastructure instance, see [Manage Exadata Cloud Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/ecs-manage-infrastructure.html#GUID-8438DDD4-C40D-4509-9E6B-441E7E46BB25).

To learn more about Oracle Database@Google Cloud, see [Product overview](https://docs.cloud.google.com/oracle/database/docs/overview).

## Before you begin

  * [Set up gcloud CLI and enable the API](https://docs.cloud.google.com/oracle/database/docs/set-up).

  * Enable the Oracle Database@Google Cloud API for the project.

[Enable the Oracle Database@Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  * Confirm that you have the required roles necessary to modify an instance: `cloudExadataInfrastructureViewer`.

For more information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

  * Confirm you have the required [Oracle Cloud Infrastructure (OCI) permissions](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/preparing-for-ecc-deployment.html#GUID-EA03F7BC-7D8E-4177-AFF4-615F71C390CD) to manage an Exadata Infrastructure instance.




## Manage instances

### Console

  1. Go to the **Exadata Database Service** page in the Google Cloud console.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. In the **Exadata Infrastructure** section, click the name of the instance you want to modify.

  3. Click **Manage in OCI**.

You'll be redirected to the OCI page to modify your instance. Modifying an instance isn't supported in Google Cloud console.

For more information on how to manage an Exadata Infrastructure instance in OCI, see [Manage Exadata Cloud Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/ecs-manage-infrastructure.html#GUID-8438DDD4-C40D-4509-9E6B-441E7E46BB25).




## What's next

  * Learn how to [create](https://docs.cloud.google.com/oracle/database/docs/create-instances) or [delete](https://docs.cloud.google.com/oracle/database/docs/delete-instances) an instance.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance.
  * [Use monitoring metrics](https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics) to monitor your instances. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
