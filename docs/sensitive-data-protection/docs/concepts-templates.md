---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates/
title: Templates \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:20.240057+00:00
---

# Templates  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Templates Stay organized with collections  Save and categorize content based on your preferences. 

You can use _templates_ to create and persist configuration information to use with Sensitive Data Protection. Templates are useful for decoupling configuration information such as what you inspect for and how you de-identify it from the implementation of your requests. Templates provide a robust way to manage large-scale rollouts of Sensitive Data Protection capabilities.

Sensitive Data Protection supports two types of templates:

  * [_Inspection templates_](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect): Templates for saving configuration information for inspection scan jobs, including what predefined or custom detectors to use.
  * [_De-identification templates_](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid): Templates for saving configuration information for de-identification jobs, including both infoType and structured dataset transformations.



## When to use templates

The following are some common use cases:

  * **Standardize governance across multiple projects** : Standardize inspection rules (such as organizational infoType detector sets) at the organization or folder level to enforce consistent data security across multiple teams.
  * **Decouple security configuration from application code** : Allow security and compliance administrators to modify infoTypes or transformation rules without requiring developers to update API calls or redeploy applications.
  * **Enforce separation of duties and access control** : Use Identity and Access Management permissions to restrict who can edit sensitive transformation configurations (such as cryptographic keys used in de-identification) while granting broader teams permission to run jobs that reference the template.
  * **Apply uniform protection across batch and streaming workloads** : Apply the same de-identification or inspection policies across both real-time content API calls and scheduled storage repository scans (such as BigQuery and Cloud Storage).
  * **Streamline compliance updates** : Add newly mandated sensitive data types (such as a new national ID detector) to a single template so that all future inspection and profiling jobs automatically inherit the change.



## Advantages of templates

Templates enable you to use a single source for your job configuration information. Consider a typical inspection scan request to Sensitive Data Protection. Whether you're inspecting text, an image, or structured data in a Google Cloud storage repository, your inspection request will include two basic pieces of information:

  * The data to scan: Either the data itself or information about the location of the data.
  * What to scan for: The predefined or custom infoTypes to turn on, likelihood limits, and so on.



Say you scheduled several storage inspection jobs to run, all of which scanned a Google Cloud storage repository for phone numbers and then created a report of the findings. The following are conceptual summary descriptions of these jobs. Note that `"inspectJob"` represents the data to scan, and `"inspectConfig"` represents what to scan for.

> **Inspection job #1:**
> 
>   * `"inspectJob"`: _Q2 2017 marketing database._
>   * `"inspectConfig"`: _PHONE_NUMBER infoType._
> 

> 
> **Inspection job #2:**
> 
>   * `"inspectJob"`: _Customer alert contact database._
>   * `"inspectConfig"`: _PHONE_NUMBER infoType._
> 

> 
> **Inspection job #3:**
> 
>   * `"inspectJob"`: _Top secret VIP partner strategy database._
>   * `"inspectConfig"`: _PHONE_NUMBER infoType._
> 

> 
> **Inspection job #4:**
> 
>   * `"inspectJob"`: _Government contract database._
>   * `"inspectConfig"`: _PHONE_NUMBER infoType._
> 


Each job's data source is different, but its instructions for what to scan for are identical. Now suppose that we want to also scan for email addresses. In this case, you would have to edit each job's configuration and add email addresses to `"inspectConfig"`. If instead you had used a template to configure what to scan for, you would only have to edit one configuration—that of the template. The next time any of these jobs ran, it would know to scan for both phone numbers and email addresses, because the `"inspectConfig"` had been set to a template.

## The InspectTemplate and DeidentifyTemplate objects

Templates are represented in Sensitive Data Protection by the [`InspectTemplate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.inspectTemplates) and [`DeidentifyTemplate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates) objects. Both template objects contain a configuration—a set of infoType detectors—to be used anywhere you otherwise would normally specify the [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) or [`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig) objects.

### Template configuration fields

Each template object contains the configuration object that the template implements, plus several additional configuration fields:

  * The template's name and display name, and a description.
  * The [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) or [`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig) object: The configuration information for the inspection or de-identification job.
  * Read-only timestamps for creation time (`"createTime"`) and a last updated time (`"updateTime"`).



### Template methods

Each template object also includes several built-in management methods. These enable you to maintain the template without having to update every request or integration. Each management method is linked in the following table, and is organized by whether the template applies organization-wide or project-wide, and whether the template is a de-identification template or an inspection template:

  
| `organization.` | `project.`  
---|---|---  
`deidentify  
Templates.` | `inspect  
Templates.` | `deidentify  
Templates.` | `inspect  
Templates.`  
Create a new template | `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates/create)` | `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.inspectTemplates/create)` | `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/create)` | `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/create)`  
Update an existing template | [`patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates/patch) | [`patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.inspectTemplates/patch) | [`patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/patch) | [`patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/patch)  
Delete an existing template | [`delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates/delete) | [`delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.inspectTemplates/delete) | [`delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/delete) | [`delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/delete)  
Retrieve an existing template, including its configuration and status | [`get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates/get) | [`get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.inspectTemplates/get) | [`get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/get) | [`get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/get)  
List all existing job templates | [`list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates/list) | [`list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.inspectTemplates/list) | [`list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/list) | [`list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/list)  
  
## Using templates

Templates are available for both inspection and de-identification configuration information, and can be used in both content API calls (text and images) and Sensitive Data Protection jobs (storage repositories).

Templates have powerful Identity and Access Management (IAM) controls so you can restrict management of them to only approved users. For more information, see:

  * [Sensitive Data Protection IAM roles](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles)
  * [Sensitive Data Protection IAM permissions](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-permissions)



## Resources

To learn how to create and use templates with Sensitive Data Protection, see:

  * [Creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect)
  * [Creating Sensitive Data Protection de-identification templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
