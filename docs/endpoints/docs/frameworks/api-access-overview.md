---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/api-access-overview/
title: Overview of API access \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:32.853586+00:00
---

# Overview of API access  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/api-access-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Overview of API access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the API access control options available to you in Cloud Endpoints.

## Overview

Endpoints uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to control access to your API. You can grant access to your API at the project level and at the individual Endpoints service level. For example, you can:

  * Grant access to principals on a per-service basis.
  * Grant permission to a user or service account to deploy an updated Endpoints configuration.
  * Grant access to your API users so they can enable your API in their own Google Cloud project.



## Roles that control access to services

You can grant the following roles for a specific service on the **Endpoints** > **Services** page in the Google Cloud console, by using the API, or by using the Google Cloud CLI.

IAM role name | Role title | Description  
---|---|---  
`roles/servicemanagement.serviceConsumer` | **Service Consumer** | Permissions for a principal to view and enable the API in their own project. You can grant the **Service Consumer** role only to Google Accounts, Google Groups, or service accounts.  
`roles/servicemanagement.serviceController` | **Service Controller** | Permissions to make calls to the `check` and ` report` methods in the [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/checking-status) API during runtime. This role is usually granted to service accounts. See the [Service Management API access control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control#roles) topic for information about this role.  
`roles/servicemanagement.configEditor` | **Service Config Editor** | Permission to deploy Endpoints configurations. This role is more restrictive than the **Project Editor** role granted on a service.   
`roles/servicemanagement.admin` | **Service Management Administrator** | All **Service Config Editor** permissions and permissions to manage access to the API. Comparable to the **Project Owner** role granted on a service.  
**Note:** Although you can grant other roles at the service level, we recommend that you use the roles listed in the previous table to manage your API.

## What's next

  * [Controlling who can enable your API](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers).
  * [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
