---
url: https://docs.cloud.google.com/domains/docs/access-control/
title: Roles and permissions \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:44.068886+00:00
---

# Roles and permissions  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page describes the Cloud Domains API roles and the access control options that are available to you in Cloud Domains.

Google Cloud offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) so that you grant only the necessary access to your resources. IAM lets you control _who_ has _what_ permissions to _which_ resources by setting IAM policies. IAM policies grant specific roles to a user, which gives the user certain permissions.

For example, a particular user might need to create and modify the contact settings for a domain, so you would give that user the Cloud Domains Admin role (`roles/domains.admin`). On the other hand, a user might need to only view existing resource domains, so they would get a Cloud Domains Viewer role (`roles/domains.viewer`). For Cloud Domains, you can configure both project-level and resource-level access.

Following are some examples of permissions for the Viewer role:

  * View all domains registered in a project.
  * View registration details such as DNS or expiry time.
  * Search domain availability and get registration parameters.



Following are some examples of permissions for the Admin role:

  * Register a new domain.
  * Update registration settings, including DNS settings and contact settings.



To understand role types, see the [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Enable the Cloud Domains API

To view and assign Cloud Domains IAM roles, you must enable the Cloud Domains API for your project. You cannot see the Cloud Domains roles in the Google Cloud console until you enable the API.

[Enable the API](https://console.cloud.google.com/apis/library/domains.googleapis.com)

For lists of the roles and permissions that Cloud Domains supports, see the following sections.

## Roles

The following table lists the Cloud Domains API IAM roles with a corresponding list of all the permissions that each role includes. Each permission is applicable to a particular resource type. For more details about each permission, see the Permissions section.

Role | Permissions  
---|---  
  
#### Cloud Domains Admin 

(`roles/domains.admin`) Full access to Cloud Domains Registrations and related resources.  |  `domains.*`

  * `domains.locations.get`
  * `domains.locations.list`
  * `domains.operations.cancel`
  * `domains.operations.get`
  * `domains.operations.list`
  * `domains.registrations.configureContact`
  * `domains.registrations.configureDns`
  * `domains.registrations.configureManagement`
  * `domains.registrations.create`
  * `domains.registrations.createTagBinding`
  * `domains.registrations.delete`
  * `domains.registrations.deleteTagBinding`
  * `domains.registrations.get`
  * `domains.registrations.getIamPolicy`
  * `domains.registrations.list`
  * `domains.registrations.listEffectiveTags`
  * `domains.registrations.listTagBindings`
  * `domains.registrations.setIamPolicy`
  * `domains.registrations.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Domains Editor 

(`roles/domains.editor`) Editor role for Cloud Domains  |  `domains.locations.*`

  * `domains.locations.get`
  * `domains.locations.list`

`domains.operations.*`

  * `domains.operations.cancel`
  * `domains.operations.get`
  * `domains.operations.list`

`domains.registrations.configureContact` `domains.registrations.configureDns` `domains.registrations.configureManagement` `domains.registrations.create` `domains.registrations.delete` `domains.registrations.get` `domains.registrations.getIamPolicy` `domains.registrations.list` `domains.registrations.listEffectiveTags` `domains.registrations.listTagBindings` `domains.registrations.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Domains Viewer 

(`roles/domains.viewer`) Read-only access to Cloud Domains Registrations and related resources.  |  `domains.locations.*`

  * `domains.locations.get`
  * `domains.locations.list`

`domains.operations.get` `domains.operations.list` `domains.registrations.get` `domains.registrations.getIamPolicy` `domains.registrations.list` `domains.registrations.listEffectiveTags` `domains.registrations.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Permissions

The following table lists the permissions that the caller must have to call each method.

Method (locations.registrations.) | Description | Required permissions  
---|---|---  
[searchDomains](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/searchDomains) | Search for an available domain. | `domains.registrations.list`  
[retrieveRegisterParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/retrieveRegisterParameters) | Get parameters to register a new domain. | `domains.registrations.list`  
[register](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/register) | Register a domain. | `domains.registrations.create`  
[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/list) | List the registration resources in a project. | `domains.registrations.list`  
[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/get) | Get the details of a registration resource. | `domains.registrations.get`  
[patch](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/patch) | Edit the details of a registration resource. | `domains.registrations.update`  
[configureManagementSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureManagementSettings) | Configure the management settings of a registration resource. | `domains.registrations.configureManagement`  
[configureDnsSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureDnsSettings) | Configure the DNS settings of a registration resource. | `domains.registrations.configureDns`  
[configureContactSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureContactSettings) | Configure the contact settings of a registration resource. | `domains.registrations.configureContact`  
[delete](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/delete) | Delete a domain. | `domains.registrations.delete`  
[retrieveAuthorizationCode](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/retrieveAuthorizationCode) | Retrieve the authorization code for a domain transfer. | `domains.registrations.configureManagement`  
[resetAuthorizationCode](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/resetAuthorizationCode) | Reset the authorization code for a domain transfer. | `domains.registrations.configureManagement`  
[renewDomain](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/renewDomain) | Renew a domain that has expired within the previous 30 days. | `domains.registrations.configureManagement`  
[initiatePushTransfer](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/initiatePushTransfer) | Transfer a `.uk` or `.co.uk` domain to another registrar. | `domains.registrations.configureManagement`  
  
## Access control using the Google Cloud console

You can use the Google Cloud console to manage access control for your projects.

For detailed instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next

  * To get started using Cloud Domains, see the [Quickstart](https://docs.cloud.google.com/domains/docs/buy-register-domain).
  * To improve the security of your Cloud Domains configuration, see [VPC Service Controls support](https://docs.cloud.google.com/domains/docs/vpc-sc-support).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
