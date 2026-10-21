---
url: https://docs.cloud.google.com/recaptcha/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:24.194080+00:00
---

# Access control with IAM  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/access-control/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Fraud Defense offers Role-Based Access Control (RBAC) with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) and access control for the reCAPTCHA Enterprise API using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs).

## Role-based access control with IAM

IAM lets you give granular access to specific Google Cloud resources and prevents unwanted access to other resources, such as logs and analytics.

This section describes the IAM roles for Fraud Defense.

To learn how to assign IAM roles to a user or service account, read [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

### Roles and permissions

The following table lists the necessary IAM roles and their permissions for Fraud Defense:

Role | Permissions  
---|---  
  
#### reCAPTCHA Enterprise Admin 

(`roles/recaptchaenterprise.admin`) Access to view and modify reCAPTCHA Enterprise keys  |  `monitoring.timeSeries.list` `recaptchaenterprise.*`

  * `recaptchaenterprise.assessments.annotate`
  * `recaptchaenterprise.assessments.create`
  * `recaptchaenterprise.firewallpolicies.create`
  * `recaptchaenterprise.firewallpolicies.delete`
  * `recaptchaenterprise.firewallpolicies.get`
  * `recaptchaenterprise.firewallpolicies.list`
  * `recaptchaenterprise.firewallpolicies.update`
  * `recaptchaenterprise.keys.create`
  * `recaptchaenterprise.keys.createTagBinding`
  * `recaptchaenterprise.keys.delete`
  * `recaptchaenterprise.keys.deleteTagBinding`
  * `recaptchaenterprise.keys.get`
  * `recaptchaenterprise.keys.list`
  * `recaptchaenterprise.keys.listEffectiveTags`
  * `recaptchaenterprise.keys.listTagBindings`
  * `recaptchaenterprise.keys.retrievelegacysecretkey`
  * `recaptchaenterprise.keys.update`
  * `recaptchaenterprise.metrics.get`
  * `recaptchaenterprise.policies.get`
  * `recaptchaenterprise.policies.update`
  * `recaptchaenterprise.projectmetadata.get`
  * `recaptchaenterprise.projectmetadata.update`
  * `recaptchaenterprise.relatedaccountgroupmemberships.list`
  * `recaptchaenterprise.relatedaccountgroups.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### reCAPTCHA Enterprise Editor 

(`roles/recaptchaenterprise.editor`) Editor role for reCAPTCHA Enterprise  |  `monitoring.timeSeries.list` `recaptchaenterprise.assessments.*`

  * `recaptchaenterprise.assessments.annotate`
  * `recaptchaenterprise.assessments.create`

`recaptchaenterprise.firewallpolicies.*`

  * `recaptchaenterprise.firewallpolicies.create`
  * `recaptchaenterprise.firewallpolicies.delete`
  * `recaptchaenterprise.firewallpolicies.get`
  * `recaptchaenterprise.firewallpolicies.list`
  * `recaptchaenterprise.firewallpolicies.update`

`recaptchaenterprise.keys.create` `recaptchaenterprise.keys.delete` `recaptchaenterprise.keys.get` `recaptchaenterprise.keys.list` `recaptchaenterprise.keys.listEffectiveTags` `recaptchaenterprise.keys.listTagBindings` `recaptchaenterprise.keys.retrievelegacysecretkey` `recaptchaenterprise.keys.update` `recaptchaenterprise.metrics.get` `recaptchaenterprise.policies.*`

  * `recaptchaenterprise.policies.get`
  * `recaptchaenterprise.policies.update`

`recaptchaenterprise.projectmetadata.*`

  * `recaptchaenterprise.projectmetadata.get`
  * `recaptchaenterprise.projectmetadata.update`

`recaptchaenterprise.relatedaccountgroupmemberships.list` `recaptchaenterprise.relatedaccountgroups.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### reCAPTCHA Enterprise Viewer 

(`roles/recaptchaenterprise.viewer`) Access to view reCAPTCHA Enterprise keys and metrics  |  `monitoring.timeSeries.list` `recaptchaenterprise.firewallpolicies.get` `recaptchaenterprise.firewallpolicies.list` `recaptchaenterprise.keys.get` `recaptchaenterprise.keys.list` `recaptchaenterprise.keys.listEffectiveTags` `recaptchaenterprise.keys.listTagBindings` `recaptchaenterprise.metrics.get` `recaptchaenterprise.policies.get` `recaptchaenterprise.projectmetadata.get` `recaptchaenterprise.relatedaccountgroupmemberships.list` `recaptchaenterprise.relatedaccountgroups.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### reCAPTCHA Enterprise Agent 

(`roles/recaptchaenterprise.agent`) Access to create and annotate reCAPTCHA Enterprise assessments  |  `recaptchaenterprise.assessments.*`

  * `recaptchaenterprise.assessments.annotate`
  * `recaptchaenterprise.assessments.create`

`recaptchaenterprise.firewallpolicies.list` `recaptchaenterprise.relatedaccountgroupmemberships.list` `recaptchaenterprise.relatedaccountgroups.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Custom roles

You might require custom roles for use cases such as regulatory requirements. To create a custom role that includes Fraud Defense permissions, perform the appropriate action as shown in the following table:

Role description | Action  
---|---  
Role that only grants permissions for the reCAPTCHA Enterprise API | Choose from the permissions in the API permissions section.  
Role that grants permissions for the reCAPTCHA Enterprise API and console | Choose permissions groups in the Roles and permissions section.  
Role that grants the ability to create and annotate assessments | Include the permissions in the role `roles/recaptchaenterprise.agent` in the Roles and permissions section.  
  
For more information on custom roles, go to [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

### API permissions

The following table lists the permissions that the caller must have to call each method in the reCAPTCHA Enterprise API, `recaptchaenterprise.googleapis.com/v1`:

Method (REST/RPC) | Required Permissions | For resource type  
---|---|---  
`recaptchaenterprise.assessments.annotate` / `AnnotateAssessmentRequest` | `recaptchaenterprise.assessments.annotate` | project  
`recaptchaenterprise.assessments.create` / `CreateAssessmentRequest` | `recaptchaenterprise.assessments.create` | project  
`recaptchaenterprise.keys.create` / `CreateKeyRequest` | `recaptchaenterprise.keys.create` | project  
`recaptchaenterprise.keys.delete` / `DeleteKeyRequest` | `recaptchaenterprise.keys.delete` | project  
`recaptchaenterprise.keys.get` / `GetKeyRequest` | `recaptchaenterprise.keys.get` | project  
`recaptchaenterprise.keys.list` / `ListKeysRequest` | `recaptchaenterprise.keys.list` | project  
`recaptchaenterprise.keys.update` / `UpdateKeyRequest` | `recaptchaenterprise.keys.update` | project  
  
## VPC Service Controls

VPC Service Controls supports Fraud Defense to provide additional access control for the reCAPTCHA APIs. For more information, see [Supported products and limitations > Fraud Defense](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_recaptcha_enterprise).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
