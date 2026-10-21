---
url: https://docs.cloud.google.com/app-lifecycle-manager/tenants/
title: Tenants and tenant projects \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:17.798835+00:00
---

# Tenants and tenant projects  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/tenants/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Tenants and tenant projects Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide provides an overview of App Lifecycle Manager tenants and how you can use them to organize your App offering.

## Tenants and tenant projects

An App Lifecycle Manager _tenant resource_ represents a logical customer, client, or _tenant_ of your App offering. It acts primarily as an organizational tool that helps you to group the units belonging to a specific tenant.

If your App offering has multiple tenants, we recommend that you provision each of your tenant's resources into a separate Google Cloud project. To separate your tenant resources into dedicated Google Cloud projects, you'll need to create at least two projects:

  * _Producer project:_ The project where your App offering is configured. You only need _one producer project_ for your SaaS application.
  * _Tenant projects_ : The projects with App Lifecycle Manager resources for a specific tenant. We recommend that you make _one project for each of your tenants_.

**Note:** You are responsible for creating both the _producer_ and _tenant_ projects. You need to create both projects before you can associate them using App Lifecycle Manager.

Using separate projects for each tenant lets you set configurations (IAM policies, or network peering, for example) within tenant projects, and helps you track costs and manage resources for each tenant.

### Actuation service accounts in a tenant project

The _actuation service account_ needs permissions in the tenant project to create and manage the resources defined in your Terraform configuration. We recommend that you set up a separate actuation account for each of your tenants.

For more information about actuation service accounts and its potentially required permissions, see [actuation service account](https://docs.cloud.google.com/app-lifecycle-manager/overview#actuation-sa).

### APIs in a tenant project

When App Lifecycle Manager uses Infrastructure Manager and the actuation service account to create resources (a VM, for example) in a tenant project, the necessary APIs must be enabled _in that tenant project_. Otherwise, provisioning will fail.

You must enable APIs for _all_ resource types your Terraform configuration uses within a tenant project.

## Use a provisional unit kind to automate your tenant set-up

When you manually create projects, enable APIs, and configure IAM for each new tenant, it's time consuming and prone to errors. You can automate the tenant set up process using App Lifecycle Manager by creating a _provisional unit kind_ containing a Terraform configuration that:

  * Creates a new Google Cloud project for the tenant.
  * Enables the necessary APIs within that new project.
  * Creates a dedicated actuation service account for the provisioned tenant (either in the producer project or the tenant project).
  * Grants the necessary IAM permissions to service accounts _within the tenant project_.
  * Sets up networking, logging, or other baseline infrastructure.



Your provisional unit kind should:

  * Define Terraform `output` variables for the `tenant_project_id`, `tenant_project_number`, and the `actuation_sa` email it creates.
  * Receive `tenant_project_id`, and `tenant_project_number` as `input` variables.



Configure your application unit kind to depend on the provisional unit kind and map the output variables to the corresponding input variables of the application unit.

After you configure your unit kind dependencies, App Lifecycle Manager verifies that the underlying tenant infrastructure unit is provisioned (creating a tenant project and setting up its permissions) before the unit containing your application is provisioned.

See [Manage dependencies between units](https://docs.cloud.google.com/app-lifecycle-manager/dependencies) and [use variables](https://docs.cloud.google.com/app-lifecycle-manager/variables) for more details on implementing this pattern.

## What's next

  * Learn how to [create tenant projects and resources](https://docs.cloud.google.com/app-lifecycle-manager/create-tenants).
  * Find out how to [associate units with tenants](https://docs.cloud.google.com/app-lifecycle-manager/associate-tenants)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
