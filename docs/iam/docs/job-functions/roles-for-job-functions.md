---
url: https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions/
title: Predefined roles for job functions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:26.923345+00:00
---

# Predefined roles for job functions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Predefined roles for job functions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) that are designed to be granted to users with specific job functions in Google Cloud.

When granting access to Google Cloud resources, you might not know which service-specific IAM roles your users need. Instead, you might know their general job function—for example, database administrator or site reliability engineer. To make it easier to give these users the permissions that they need, Identity and Access Management (IAM) offers predefined roles that are designed for specific job functions. These roles contain all of the permissions typically required to access the services that are relevant to a certain job function. Assign these roles to the users in your Google Cloud organization whose responsibilities align most with the job functions described on this page.

**Note:** Predefined roles for job functions are typically less granular than other predefined roles. If your organization has strict standards for secure access management, consider using more granular [predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) or creating [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Administrators

The following sections describe some common administrative job functions and their corresponding predefined roles.

### Databases administrator

The Databases Admin (`roles/iam.databasesAdmin`) role is designed for administrative users that are responsible for configuring and maintaining an organization's information technology infrastructure. These users ensure that an organization's computer systems, servers, and data security systems are secure, efficient, up to date, and backed up.

The Databases Admin role contains the permissions necessary for administrative access to all structured and unstructured datastores in Google Cloud. These permissions let users do the following:

  * Manage and maintain data services such as Cloud SQL, Datastore, BigQuery, and Cloud Storage.
  * Create dashboards and alerts.
  * View logs to debug data services.
  * View data from related Google Cloud services like Dataflow, Cloud Key Management Service, and Pub/Sub.



For a list of the specific permissions included in this role, see the [Databases Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) on the Identity and Access Management roles and permissions page.

### Infrastructure administrator

The Infrastructure Administrator (`roles/iam.infrastructureAdmin`) role is designed for administrative users whose responsibilities involve managing the efficiency, security, and reliability of an organization's core infrastructure services. These users are often generalists that work across different infrastructure components, including servers, networks, and storage.

The Infrastructure Administrator role contains the permissions necessary for managing key infrastructure services in Google Cloud. These permissions let users do the following:

  * Manage and maintain all compute, networking, and storage services.
  * Create custom dashboards and alerts.
  * View logs for debugging infrastructure services.



For a list of the specific permissions included in this role, see the [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) role on the Identity and Access Management roles and permissions page.

### Network administrator

The Network Administrator (`roles/iam.networkAdmin`) role is designed for administrative users whose responsibilities involve configuring an organization's network devices or software, maintaining their performance, and troubleshooting network issues such as vulnerabilities and resource access.

The Network Administrator role contains the permissions necessary for full control of Google Cloud networking resources. These permissions let users do the following:

  * Manage and maintain network infrastructure in the cloud.
  * Create customized dashboards and alerts.
  * View logs for debugging network issues.



For a list of the specific permissions included in this role, see the [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) role on the Identity and Access Management roles and permissions page.

## Data and AI practitioners

The following sections describe some common data- and AI-related job functions and their corresponding predefined roles.

### Data scientist

The Data Scientist (`roles/iam.dataScientist`) role is designed for users whose responsibilities include collecting and validating data, classifying data types, and identifying patterns in data sets. These users use the analyzed data to build models that can suggest potential solutions to business problems.

The Data Scientist role contains the permissions necessary to analyze data from Google Cloud resources and build data processing, transformation, and analysis pipelines. These permissions let users do the following:

  * Manage Vertex AI, data platform, and other associated Compute Engine services.
  * Use eventing and data streaming services.
  * Use monitoring, impersonation, key use, and debugging capabilities.



For a list of the specific permissions included in this role, see the [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) role on the Identity and Access Management roles and permissions page.

### ML engineer

The ML Engineer (`roles/iam.mlEngineer`) role is designed for users who specialize in developing machine learning (ML) models and techniques. Their goal is to standardize ML practices as well as operationalize and scale ML models for deployment.

The ML Engineer role contains the permissions necessary for full control of all AI Platform capabilities. These permissions let users do the following:

  * Build and deploy AI based applications using any Google Cloud AI service, including Vertex AI, Model Armor, and Google Kubernetes Engine.
  * Create and manage data for machine learning applications.
  * View monitoring, logging, and associated key data.



For a list of the specific permissions included in this role, see the [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) role on the Identity and Access Management roles and permissions page.

## Operations and support personnel

The following sections describe some common operations- and support-related job functions and their corresponding predefined roles.

### Development and Operations (DevOps)

The DevOps (`roles/iam.devOps`) role is designed for users that are responsible for streamlining an organization's software development lifecycle. These users help build and deploy cloud applications as well as monitor their reliability and performance.

The DevOps role contains the permissions necessary to build and deploy applications, create, manage, and perform administrative tasks on associated Google Cloud resources. These permissions let users do the following:

  * Perform administrative tasks on virtual machines.
  * Manage and maintain storage objects and source repositories.
  * Ability to manage some relevant Google Cloud resources including Cloud SQL, Cloud Build, Cloud Monitoring, Cloud Logging, and service accounts.



For a list of the specific permissions included in this role, see the [DevOps](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) role on the Identity and Access Management roles and permissions page.

### Site reliability engineer

The Site Reliability Engineer (`roles/iam.siteReliabilityEngineer`) role is designed for users who ensure an organization's applications and services are reliable, scalable, and perform efficiently. Their responsibilities involve conducting safe, efficient updates and releases, and ensuring that changes to code don't impact the reliability of an app or service.

The Site Reliability Engineer role contains the permissions necessary for operational monitoring, performance optimization, and reliability management of applications built on Google Cloud. These permissions let users do the following:

  * Review monitoring and logging data.
  * Debug asset performance.
  * View data from assets deployed to production.



For a list of the specific permissions included in this role, see the [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) role on the Identity and Access Management roles and permissions page.

### Support user

The Support User (`roles/iam.supportUser`) role is designed for users whose responsibilities involve helping customers resolve technical issues and answer questions they might have about a product or service.

The Support User role contains the permissions necessary to access Google Cloud resource information and gather the insights required for troubleshooting customer issues. These permissions let users do the following:

  * Create and manage support cases in their organization.
  * View resource configurations and resource log information for troubleshooting issues.
  * Read resource, monitoring, and logging information for filing support cases.



For a list of the specific permissions included in this role, see the [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) role on the Identity and Access Management roles and permissions page.

## Security practitioners

The following sections describe some common security-focused job functions and their corresponding predefined roles.

### Security auditor

The Security Auditor (`roles/iam.securityAuditor`) role is designed for users who are responsible for assessing whether an organization's security posture protects against cyber threats and complies with relevant standards and regulations.

The Security Auditor role contains the read-only permissions necessary to perform comprehensive security evaluations of Google Cloud environments, associated policies, and configurations. These permissions let users do the following:

  * Browse and view Google Cloud resources, folder and project hierarchy, and logs.
  * Read security configurations.
  * Read key resource metadata.



For a list of the specific permissions included in this role, see the [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) role on the Identity and Access Management roles and permissions page.

## What's next

  * Learn how to [grant a role to a principal](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).
  * Learn how to [find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).
  * Learn how to [create and maintain custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
