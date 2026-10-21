---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/iam/
title: IAM permissions for Config Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:42.763532+00:00
---

# IAM permissions for Config Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  IAM permissions for Config Controller Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to grant Config Controller permissions to manage your Google Cloud resources.

## Least privilege

To use Identity and Access Management securely, Google Cloud recommends following the [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) best practice. In production environments, give any user accounts or processes only those privileges which are essentially vital to perform its intended functions.

## IAM permissions for Config Connector

IAM authorizes Config Connector to take actions on Google Cloud resources.

### (Recommended) Predefined or custom roles

To follow the least privilege best practice, grant the most limited [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meet your needs. For example, if you need Config Connector to manage your GKE cluster creation, grant the [Kubernetes Engine Cluster Admin role](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined) (`roles/container.clusterAdmin`).

You can use [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) to determine which roles to grant instead. You can also use the [Policy Simulator](https://docs.cloud.google.com/iam/docs/understanding-simulator) to ensure that changing the role won't affect the principal's access.

### Basic roles

It is recommended to have the same permissions in a non-production environment that you have in a production environment, following the least privilege best practice. Having the same permissions has the benefit of testing the production configurations in non-production, and detecting issues earlier.

That said, for certain situations you may want to speed up experimenting with Config Connector. For non-production environments, you can use one of the basic roles as an experiment, before deciding on the most limited permissions.

**Caution:** Basic roles include thousands of permissions across all Google Cloud services. In production environments, don't grant basic roles unless there is no alternative. Instead, grant the most limited [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meet your needs.

The [Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`) allows Config Connector to manage most of Google Cloud resources in your project, including IAM resources.

The [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`) allows most Config Connector capabilities except Project or Organization-wide configurations such as IAM modifications.

To learn more about IAM permissions for Config Connector:

  * Read [IAM permissions for Config Connector](https://docs.cloud.google.com/config-connector/docs/how-to/configure-iam-permissions).
  * Read [Config Connector permission troubleshooting guide](https://docs.cloud.google.com/config-connector/docs/troubleshooting#error_403_caller_is_missing_iam_permission).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
