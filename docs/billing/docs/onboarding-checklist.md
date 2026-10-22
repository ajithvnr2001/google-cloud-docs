---
url: https://docs.cloud.google.com/billing/docs/onboarding-checklist/
title: Guide to Cloud Billing Resource Organization and Access Management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:45.566404+00:00
---

# Guide to Cloud Billing Resource Organization and Access Management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/onboarding-checklist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Guide to Cloud Billing Resource Organization and Access Management Stay organized with collections  Save and categorize content based on your preferences. 

This document teaches you how to set up your various Google Cloud resources to avoid common issues and enable best practices for access control and cost management. The guide walks through design decisions and configuration options that help set you up for success in administering your cloud resources.

## Goals of this guide

  * Provide a conceptual overview of the various resources involved with billing.
  * Show you how to set up your Cloud Billing resources efficiently and for ease of management, to align your strategic priorities with cloud usage and maintain a well-functioning account.
  * Help you avoid the most common billing-related issues faced by Google Cloud customers.
  * Teach you about best practices when configuring resource access permissions to ensure redundancy and security.
  * Provide step-by-step instructions to help you set up your financial governance tools for greater clarity, accountability, and control.

**Note:** If you're an enterprise developer already familiar with Google Cloud and the services it offers, and are looking for guidance in launching your application, see the [launch checklist documentation](https://docs.cloud.google.com/docs/platform-launch-checklist) and [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).  
  
If you're getting started with Google Cloud, you create a self-serve billing account as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

## Overview

This guide is organized into two main sections. The first section provides you with a conceptual overview of the various resources and roles involved with managing Google Cloud billing. The second section walks you through the steps necessary to configure your Google Cloud resources optimized for your billing needs.

### Section 1: Concepts

  * Resource Overview and Hierarchy: A high-level visual representation of the [various Google Cloud resources that impact your billing](https://docs.cloud.google.com/billing/docs/concepts) and how they relate to one another.
  * Roles Overview: A summary of the access roles, organized by resource, that are directly relevant to your billing set up.



### Section 2: Setup Guide

  * A step-by-step configuration walkthrough covering Google Cloud onboarding topics relevant to your billing setup, including guidance for customization based on your organization's needs.



## Cloud Billing Concepts

Before working through the setup guide section, familiarize yourself with these concepts. Understanding the key concepts will help you with configuration decisions for your cloud environment. If you need additional information, see the [overview of Cloud Billing concepts](https://docs.cloud.google.com/billing/docs/concepts).

### Resource Overview

#### What is a resource?

In the context of Google Cloud, resource can refer to the service-level resources that are used to process your workloads (for example, virtual machines) as well as to the account-level resources that sit above the services, such as projects, folders, and the organization.

#### What is resource management?

Resource management is focused on how you should configure and grant access to the various Google Cloud resources for your company or team, specifically the setup and organization of the account-level resources that sit above the service-level resources. Account-level resources are the resources involved in setting up and administering your Google Cloud account. This document provides prescriptive advice on configuring your account-level resources and the roles necessary to manage them to maintain a well-functioning account.

### Resource Hierarchy

Google Cloud resources are organized hierarchically. This hierarchy lets you map your organization's operational structure to Google Cloud, and to manage access control and permissions for groups of related resources. The following diagram shows an example resource hierarchy illustrating the core account-level resources involved in administering your Google Cloud account.

![Resource Hierarchy](https://docs.cloud.google.com/static/billing/docs/images/resource-hierarchy-overview.png)

  * The public **_domain_** is the mechanism to manage the users in your organization and is directly related to the organization resource.

  * The domain **_organization_** resource represents an entire organization (for example, a company) and is the top-level node of the hierarchy. The organization resource provides central visibility and control over all Google Cloud resources further down in the hierarchy.

  * Next in the hierarchy are folder **_folders_**. You can use folders to isolate requirements for different departments and teams in the parent organization. You can similarly use folders to separate production resources from development resources.

  * At the bottom of the hierarchy are **_projects_**. Projects contain the service-level resources (such as computing, storage, and networking resources) that process your workloads and constitute your apps.

  * Resources can be further categorized using label **_labels_**. You can label the service-level resources (for example, virtual machines), as well as your account-level resources (for example, projects).

  * monetization_on **_Cloud Billing accounts_** are linked to and **pay for projects**.

  * Cloud Billing accounts are connected to a payment **_Google payments profile_**. The payments profile is a Google-level resource and you pay for Google services (such as AdWords and Google Cloud) using the payment methods that are attached to that profile.




You can enforce granular permissions at different levels in the resource hierarchy to ensure that the right individuals have the correct access and permissions within your organization.

The structure you define is flexible and allows you to adapt to evolving requirements. If you're just beginning your Google Cloud journey, adopt the simplest structure that satisfies your initial requirements. See the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) overview for full details.

### Roles Overview

**What are roles?**

Roles grant one or more privileges to a user that allow performing a common business function.

**How do roles work in Google Cloud?**

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) to manage access control to your Google Cloud resources. IAM lets you control _who (users)_ has _what access (roles)_ to _which resources_ by setting IAM policies. To assign permissions to a user, you use IAM policies to grant specific roles to a user. Roles have one or more permissions bundled within them, controlling user access to resources.

You can set an IAM policy (roles) at the [organization level](https://docs.cloud.google.com/resource-manager/docs/access-control-org), the [folder level](https://docs.cloud.google.com/resource-manager/docs/access-control-folders), the [project level](https://docs.cloud.google.com/resource-manager/docs/access-control-proj), or (in some cases) on the service-level resource. Resources inherit the policies of the parent node. If you set a policy at the Organization level, it's inherited by all its child folders and projects. If you set a policy at the project level, it's inherited by all its child resources.

The diagram below represents the Google Cloud resource hierarchy in complete form, and calls out the important high-access roles at each level:

public Domain  
---  
|  The Google Workspace or Cloud Identity super administrators at the domain level are the first users who can access an organization after creation.   
---  
Role: Domain Super Admin  
The [ Super Admin](https://support.google.com/a/answer/2405986#super_admin) can grant the Organization Admin role (or any other role) and recover accounts at the Domain level.  |  Recommended Assignee  
The Super Admin is usually someone who manages accesses at a high level, like a Domain Administrator.   
Learn more about [ Google Workspace administrator roles](https://support.google.com/a/answer/33325?ref_topic=4514341) and [ Cloud Identity admin roles](https://support.google.com/cloudidentity/answer/33325).   
domain Organization  
---  
|  An [ **organization**](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) (for example, a company) is the root node in the Google Cloud resource hierarchy. The Organization resource is the hierarchical ancestor of project resources and Folders. The IAM access control policies applied on the Organization resource apply throughout the hierarchy on all resources in the organization.   
---  
Role: Organization Admin  
The Organization Admin can administer any resource and grant any role within the Organization.  |  Recommended Assignee  
The Organization Admin is usually someone who manages access control, like an IT Administrator.   
Learn more about [Organization roles](https://docs.cloud.google.com/resource-manager/docs/access-control-org).   
folder Folders  
---  
|  [ **Folder**](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) resources provide additional grouping mechanisms and isolation boundaries between projects. They can be seen as sub-organizations within the Organization. Folders can be used to model different legal entities, departments, and teams within a company. Folders can contain sub-folders and projects.   
---  
Role: Folder Administrator  
The Folder Administrator can create and edit the IAM policy of folders. They decide how roles are inherited by projects in the folders.  |  Recommended Assignee  
The Folder Administrator manages finer access control, and is typically a department head or team manager.   
Learn more about [Folder roles](https://docs.cloud.google.com/resource-manager/docs/access-control-folders).   
Projects  
---  
|  The [ **project**](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) resource is the base-level organizing entity. Organizations and folders may contain multiple projects. A project is _required_ to use Google Cloud, and forms the basis for creating, enabling, and using all Google Cloud services, managing APIs, enabling billing, adding and removing collaborators, and managing permissions.   
---  
Role: Project Creator  
The Project Creator role lets you create projects and inherently lets resources be spun up on Google Cloud and incur usage.  |  Recommended Assignee  
Project Creators in your organization might be team leads or service accounts (for automation).   
Role: Project Owner & User  
The Project Owner & User role lets you to see costs and usage in projects and label resources.  |  Recommended Assignee  
Project owners and users in your organization might be team leads or developers.   
Learn more about [Project roles](https://docs.cloud.google.com/resource-manager/docs/access-control-proj).   
monetization_on Cloud Billing account  
---  
|  [ Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) are linked to and pay for projects. Cloud Billing accounts are connected to a [ Google payments profile](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383).   
---  
Role: Billing Account Admin  
The Billing Account Admin can enable Billing Export, view cost and spend, set budgets and alerts, and link or unlink projects.  |  Recommended Assignee  
The Billing Admins in your organization may be someone more finance-minded.   
Role: Billing User  
Billing Users can link projects to Cloud Billing accounts, but can't unlink them. The role is usually issued broadly in concert with the Project Creator role.  |  Recommended Assignee  
Trusted Project Creators in your Organization typically need this role.   
Learn more about [Billing roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access).   
payment Google payments profile  
---  
|  [ Google payments profiles](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383) are managed outside of your Google Cloud Organization, in the Google payments center, a single location where you can manage the ways you pay for _all_ of your Google products and services, such as Google Ads, Google Cloud, and Google Fi phone service. Google payments profiles are connected to **Cloud Billing accounts**.   
---  
Google payments Admin  
The payments profile Admin can view and manage payment methods, make payments, view invoices, and see Google payments accounts.  |  Recommended Assignee  
The Google payments profile Admins in your organization are typically part of your Finance or Accounting teams.   
Learn more about [ Google payments profile user permissions](https://support.google.com/paymentscenter/answer/7162853?ref_topic=9017383#user_permissions).  
  
* * *

## Setup Guide

Each section in the setup guide provides information about decision points, offers best-practice recommendations, describes important roles, and provides a configuration checklist. Information about potential issues is also provided, with the ultimate goal of helping you configure your Google Cloud resources optimized for your billing needs. The guidelines help to ensure your setup is best protected against the most common access and billing issues faced by Google Cloud customers.

### Before you begin

Before working through the setup guide, familiarize yourself with the Cloud Billing concepts. Understanding the key concepts will help you with configuration decisions for your cloud environment. Watch the following video to learn more.

#### Best Practices: Google Cloud Resource Organization and Access Management (Cloud Next '19)

There are a variety of different ways that you can organize your resources and set up access controls when using Google Cloud. To ensure your team can continuously access and manage these resources effectively requires following some essential best practices. In this session, you'll learn each of the Google Cloud resources available and receive a best practices checklist that you can use to prevent you from running into some of the most common and problematic account configuration issues that customers experience.

#### The setup guide contains the following sections:

  * Domain and Organization
    * Domain (and Identity)
    * Organizations
  * Cloud Billing Accounts
  * Google payments Profiles and Accounts
  * Projects, Folders, and Labels



* * *

## Domain and Organization

The Domain and Organization sit at the top of the resource hierarchy. Together, the Google Cloud Domain and Organization let you centrally administer all of your users and Google Cloud resources.

  * The Domain lets you manage the users in your organization.

  * The Organization lets you manage your Google Cloud resources and which users have what type of access to those resources.




![Domain and Organization in the Resource Hierarchy](https://docs.cloud.google.com/static/billing/docs/images/domain-and-organization.png)

## Domain and Identity

Your company Domain is the primary identity of your organization and establishes your company's identity with Google services, including Google Cloud. The Domain is linked to either a Google Workspace or Cloud Identity account.

Identity is used for authentication and access management of your users to Google Cloud resources. When first starting out with Google Cloud, it's important to decide how you want to manage your user authentication and identity. We offer flexible ways to manage access with Google Workspace and Cloud Identity.

###  stars Key Decision: Cloud Identity and Google Workspace

#### For user authentication and identity, should you use Cloud Identity or Google Workspace?

The [ Organization resource](https://docs.cloud.google.com/billing/docs/onboarding-checklist#organizations) is closely associated with a [Google Workspace](https://support.google.com/a/answer/6043576) or [ Cloud Identity](https://support.google.com/cloudidentity/answer/7319251) account. You acquire an Organization resource only if you're also a Google Workspace or Cloud Identity customer. Each Google Workspace or Cloud Identity account can have exactly one Organization. Once an Organization resource is created for a domain, all Google Cloud projects created by members of the account domain will, by default, belong to the Organization resource.

Google Cloud uses [ Google Accounts](https://support.google.com/work/android/answer/6371476) for authentication and access management. Google recommends using fully managed corporate Google accounts for increased visibility, auditing, and control over access to Google Cloud resources. 

| Cloud Identity  
---  
[ Cloud Identity](https://docs.cloud.google.com/identity/docs/overview) provides free, managed Google Accounts that you can use with Google services including Google Cloud. Using Cloud Identity accounts for each of your users, you can manage all users across your entire domain from the Google Admin console. **Use case:** You don't need Google Workspace features like Drive or Gmail and only need the account management features offered by integrating your domain. **Recommend:** Obtain an Organization for free by using [Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).   
| Google Workspace  
---  
If you're a Google Workspace administrator, you can manage all of your users and settings through the Google Workspace Admin Console. By default, all new users are assigned a Google Workspace license. If you have a subset of developers who don't require Google Workspace licenses, you can add [Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) accounts instead. **Use case:** You want to take advantage of Google Workspace features like Drive or Gmail in addition to the account management features of Google Workspace. **Recommend:** Obtain an Organization by signing up for [Google Workspace](https://support.google.com/a/answer/53926).  
For more information, see [ Getting an Organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring) and [ Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).  
  
### Important Roles

public Domain Super Admin  
The [ Super Admin](https://support.google.com/a/answer/2405986#super_admin) can grant the Organization Admin role (or any other role) and recover accounts at the Domain level.  |  Recommended Assignee  
The Super Admin is usually someone who manages accesses at a high level, like a Domain Administrator.   
---|---  
Learn more about [ Google Workspace administrator roles](https://support.google.com/a/answer/33325?ref_topic=4514341) and [ Cloud Identity admin roles](https://support.google.com/cloudidentity/answer/33325).   
  
### Checklist

1\. Create the Resource  
---  
❑ | star Choose [Cloud Identity](https://docs.cloud.google.com/identity/docs/overview) or [Google Workspace](https://support.google.com/a/answer/6043576). 

  * **For Cloud Identity:**
    1. Review the [ Cloud Identity Overview](https://support.google.com/cloudidentity/answer/7319251) and get started at the [ Cloud Identity Signup](https://workspace.google.com/signup/gcpidentity/welcome#0) page.
    2. Follow the [Signup Process](https://support.google.com/cloudidentity/answer/7390066) to manage the Cloud Identity account. **Note:** Use your own work email to begin the signup, but in the last step, use an admin email account which you can access (for example, admin@yourdomain.com).
    3. Make sure that the admin@yourdomain.com account has an email address that can receive mail, because Cloud Identity will use that address to communicate with the Cloud Identity Admin.
    4. Follow the [ domain verification](https://support.google.com/cloudidentity/answer/7331243) process. We also have a [ video walkthrough](https://www.youtube.com/watch?v=x-0DvzK0IkM&t=28s).
  * **For Google Workspace customers, Cloud Identity is included.** If you have non-Google Workspace users in your domain that want to access Google Cloud:
    1. [ Enable Cloud Identity.](https://support.google.com/cloudidentity/answer/7319251)
    2. [ Disable Automatic Google Workspace licensing.](https://support.google.com/cloudidentity/answer/7338389)

**Caution:** If, during signup, you encounter an error message when attempting to use your domain, visit [ the domain troubleshooter](https://support.google.com/a/answer/80610).   
2\. Configure Access  
❑ | Review the [ patterns for adding or synchronizing users and groups](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment).   
❑ | Add users and groups using the [admin console](https://admin.google.com/), via [ Google Cloud Directory Sync](https://support.google.com/a/answer/106368), or using the [Admin SDK API](https://developers.google.com/admin-sdk/). **Caution:** non-Google Workspace customer using their @yourdomain.com email as a Google Account to use Docs, Sheets and other Google Workspace products as consumers will lose access to those services (even Viewing mode). Please review the article [ Add users who have existing Google accounts](https://support.google.com/a/answer/7044710).   
❑ | Set up more than one [ Super Admin](https://support.google.com/a/answer/2405986#super_admin) and ensure other project owners, administrators, and employees know who they are, so they can reach out in case of account access issues or if there is a need to delegate another Organization Admin. **Warning:** At some point, most customers are affected by loss of access to resources in Google Cloud. Ensure you are not unintentionally locked out of your Google Cloud resources by having redundant administrators, multiple Organization Admins, and more than one Super Admin.   
3\. Configure the Resource  
❑ | Check the number of licenses provided. By default, Google provides a [ fixed number of free-of-charge licenses](https://support.google.com/cloudidentity/answer/7295541). If you need additional licenses, [ contact us](https://support.google.com/cloudidentity/answer/7295541).   
❑ | Cloud Identity provides a diverse set of security and user management features. For a list of what's included, see the [ features and editions comparison chart](https://support.google.com/cloudidentity/answer/7431902).   
  
* * *

## Organizations

An Organization is the root node of the Google Cloud hierarchy of resources. An Organization is associated with exactly one Domain. All resources that belong to an Organization are grouped under the Organization node, which provides insight into and access control over every resource in the Organization.

###  stars Best Practice: Configure an Organization

Google Cloud users aren't required to have an [ Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). However, if you need to manage more than one user account, we strongly recommend [ configuring an Organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). The [ Organization resource provides many benefits](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#benefits_of_the_organization_resource), including: [ IAM policy inheritance](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#inheritance) and resource access recovery.

For more information, see [ Creating and managing Organizations](https://cloud.google.com/resource-manager/docs/creating-managing-organization).

### Important Roles

domain Role: Organization Admin  
The Organization Admin can administer any resource and grant any role within the Organization.  |  Recommended Assignee  
The Organization Admin is usually someone who manages access control, like an IT Administrator.   
---|---  
Learn more about [Organization roles](https://docs.cloud.google.com/resource-manager/docs/access-control-org).   
  
### Checklist

1\. Create the Resource  
---  
❑ | [ Obtain an Organization resource](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources). If you followed the steps for Domain and Identity, you already have an organization.   
2\. Configure Access  
❑ | Set up multiple [ Organization Administrators](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles) who will be responsible for defining IAM policies and delegating responsibility for resources throughout your organization, like Cloud Billing and Project management. **Note:** By default, the email account designated as the Admin in the sign up process for Cloud Identity (usually admin@yourdomain.com) is assigned as the first Organization Administrator. If you set up invoiced billing, the Technical Contact on the invoiced billing agreement will be delegated as the Organization Administrator.   
❑ | Grant IAM roles at the Organization level that you want everyone to use, while keeping in mind the [ security principle of least privilege](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control#best_practices). **Note:** To ensure that Cloud Billing accounts are only created by users that should handle payment information, settings, and cost attribution for the organization, minimize the number of users that are granted the role of Billing Account Creator. We recommend [ removing the Billing Account Creator](https://docs.cloud.google.com/resource-manager/docs/default-access-control) role from the Organization level.  
3\. Configure the Resource  
❑ | [ Migrate your Projects and Billing Accounts into your Organization](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing). **Note:** For larger-scale migration, we recommend using the [ Organization Setup Wizard](https://docs.cloud.google.com/resource-manager/docs/organization-setup). Have an Organization Admin enumerate all of your projects and billing accounts that need to be migrated along with a list of their owners for use in the Setup Wizard.Once migrated, if an owner of a project or billing account loses access to their account or leaves the company, ownership of the [project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [ billing account](https://docs.cloud.google.com/billing/docs/how-to/billing-access#update_billing_permissions) can be recovered by the Organization Admin.  
  
* * *

## Cloud Billing Accounts

Billing accounts pay for projects. A project and its service-level resources are always paid for by a single billing account. A billing account operates in a single currency and is linked to a Google payments profile.

![Cloud Billing Accounts in the Resource Hierarchy](https://docs.cloud.google.com/static/billing/docs/images/billing-account-in-hierarchy.png)

A billing account can be linked to one or more projects. Project usage is tracked and charged to the linked billing account. Projects that are _not_ linked to a billing account can't use Google Cloud or Google Maps Platform services. This is true even if you only use [services that are free](https://docs.cloud.google.com/free/docs/gcp-free-tier).

###  stars Key Decision: One Billing Account or Multiple Billing Accounts?

We recommend creating one central Cloud Billing account that lives in your Organization. For most customers, adding additional billing accounts creates unneeded extra overhead, making them more difficult to track and manage. And multiple billing accounts might not behave in the way you expect with [ Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) or might cause issues with any promotional credits.

You may need multiple Cloud Billing accounts if you have any of these requirements:

  * You need to split charges for legal or accounting reasons.
  * You need to pay in multiple currencies.
  * You need to allocate support costs differently, because support costs accumulate from across all applicable Billing subaccounts in the organization and charge only to the parent Billing Account.



###  stars Key Decision: Pay with Credit or Debit Card or Use Invoiced Billing?

When you first [ set up a Cloud Billing account using the Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account), by default, you create a self-serve billing account, connected to a credit or debit card as the payment instrument.

If you have a dedicated Finance or Accounting team, or if you anticipate a large amount of spend when you first start on Google Cloud, you might be better off using [ invoiced billing](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing). To learn if your organization is eligible for invoiced billing, [ contact Cloud Billing Support](https://docs.cloud.google.com/support/billing). You must be a billing administrator of your organization's current billing account to apply.

### Important Roles

monetization_on Role: Billing Account Admin  
The Billing Account Admin can: 

  * Manage payment instruments
  * Enable Billing Export
  * View costs and spend and set budget alerts
  * Link and unlink projects
  * Manage other user roles tied to the Billing Account

|  Recommended Assignee  
This role is typically filled by someone with financial control at your company, for example, a business lead that owns the P&L or a technical team member with budget management responsibility. Importantly, because this role is required to contact Billing Support, you shouldn't use a service account or mailing list as a billing administrator.  
---|---  
monetization_on Role: Billing User  
Billing Users can: 

  * Link projects to billing accounts, but can't unlink them
  * View costs

|  Recommended Assignee  
This role is usually issued broadly in concert with the Project Creator role. Trusted Project Creators in your organization typically need this role so they can link their projects to a billing account.   
Learn more about [Billing roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access).   
  
**Note: Want to control who can view costs?**

Different roles applied at different levels contain permissions that allow access to view costs.

For example, if you want a user to be able to view costs for an entire billing account, including all of its projects, set the `billing.accounts.getSpendingInformation` permission on the billing account level. The following predefined roles grant this permission by default: Billing Account Administrator, Billing Account Costs Manager, and Billing Account Viewer. 

If you want to limit a user to viewing only the costs for a _specific project_ , give the user the `billing.resourceCosts.get` permission on the project. The following predefined roles grant this permission by default: Project Owner, Project Editor, and Project Viewer.

For more information, see [ Overview of billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access) and [Custom roles for billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles).

### Checklist

1\. Create the Resource  
---  
❑ | star [Create](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account) or Identify your main Billing Account that you want to use. If you have an [invoiced account](https://docs.cloud.google.com/billing/docs/how-to/read-invoice), this step is already done for you.   
2\. Configure Access  
❑ | [ Grant access to view Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/billing-access) to people in finance and other departments and roles where users need to track spend or need to review cost anomalies.   
❑ | Assign multiple [ Billing Account Administrators](https://docs.cloud.google.com/billing/docs/how-to/billing-access) to each Billing Account – you might also consider using Organization-level permissions. **Note:** The Billing Account Administrator is an owner role for a billing account, and can be set at the Billing Account or at the Organization level. Billing Account Administrators can manage payment instruments, configure billing exports, view cost information, link and unlink projects and manage other user roles on the billing account.  
3\. Configure the Resource  
❑ | star Consolidate multiple Billing Accounts into your main Billing Accounts. 

  1. First identify your main Billing Accounts and the projects you want to link to those billing accounts. Learn how to [view projects linked to a billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked). 
  2. [ Link or move existing projects onto your main Billing Accounts](https://docs.cloud.google.com/billing/docs/how-to/modify-project). **Note:** If you have many projects to move, try our [gcloud tool](https://docs.cloud.google.com/sdk/gcloud) to [ link projects to a billing account](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link).

  
❑ | star Settle and close any other billing accounts that you no longer intend to use to avoid potential issues in the future. 

  1. [ View your old Billing Accounts](https://docs.cloud.google.com/billing/docs/how-to/view-linked) to verify that they no longer have any linked projects.
  2. After moving all your projects onto your main Billing Accounts, wait two days for the charges to stop on your old Billing Accounts. 
  3. After two days, settle any existing balances on the old billing accounts, and then [ close the old Billing Accounts](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account). 

  
❑ | attach_money Review the [recommended next steps](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#recommended_next_steps) after you create a Cloud Billing account. 

  * [Create a FinOps administration project](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#set-up-billing-project) to use for billing APIs and project-dependent billing tools.

  
❑ | attach_money [Set up budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) with multiple alert thresholds to reduce spending surprises and unexpected cost overruns.   
❑ | attach_money Set up automatic exports of billing data to use for monitoring and analyzing costs. Learn how to [ export billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). **Note:** Data is available in your dataset only from the time export is enabled. For cost management purposes, we recommend enabling Billing Export on your Billing Accounts early on, when you're just beginning to attach Projects to Billing Accounts. This way, your usage data will be tracked and available to you from day one, and ready for analysis using a variety of tools.   
  
##  stars Key Concepts: Billing Export, Billing Reports, and Invoices

Your usage is reported from your Projects to your Billing Accounts and your usage data is made available to you in a variety of ways, all of which can be used to help you understand the full picture of your spend.

  * Your invoice tells you what you owe.
  * Billing reports tell you why and where your costs came from.



To answer cost questions, we recommend looking at billing reports first.

Billing Export outputs your daily usage estimates to a dataset or file you specify. You can use it to run analysis on your usage data. [ Billing Export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) includes an `invoice.month` field so you can match your exported data to your invoices.

  * Late-reported usage might cause your data to not map directly to your invoice; that is, some product usage at the very end of a month may be charged to the next month's invoice.
  * Exported billing data doesn't include any tax accrued or credits issued to a billing account.



Billing Reports uses the same data that Billing Export uses, and displays an interactive chart that plots usage costs for all projects linked to a billing account. Use [ billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) to get an at-a-glance overview of your usage costs and discover and analyze trends.

  * You [ access billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports#getting_started) in the Google Cloud console.
  * If you have multiple billing accounts, the billing report displays usage costs for one billing account at a time, not aggregated across all billing accounts.
  * Depending on your level of access, your view of usage costs may be limited to viewing the costs of certain projects, rather than all of the projects linked to a billing account.



Invoices represent the canonical amount you're billed for each month and provide an exact breakdown of what usage you were billed for. Review your invoice PDF or CSV line items each month and review the [Google payments center](https://payments.google.com/) for credit memos and invoice payments history.

**Caution** : As of November 2019, the CSV invoice is deprecated and replaced by the Cost Table report. If your organization currently processes the invoice or statement CSV, [ download the Cost Table to CSV](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and process it in place of the invoice or statement CSV.

* * *

## Google payments Profiles and Accounts

Your business is represented by a [Google payments profile](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383), and you pay for Google services using the payment methods that are attached to that profile. The payments profile is a Google-level resource managed at [payments.google.com](https://support.google.com/paymentscenter/topic/9017382?ref_topic=9037778) and is linked to a Cloud Billing account.

![Google payments profile in the Resource Hierarchy](https://docs.cloud.google.com/static/billing/docs/images/payments-profile-in-hierarchy.png)

warning **Warning:** The payments profile _isn't_ a Google Cloud resource. A payments profile is a Google-level resource that is managed outside of your Google Cloud organization, requiring [ separate roles and permissions](https://support.google.com/paymentscenter/answer/7162853?ref_topic=9017383). Although some payments-related permissions are "acquired" with the [ Billing Account Administrator IAM role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) (for example, to view payment details, update payment methods, and make a manual payment), you need separate payments-specific user permissions to _fully manage_ Google payments profiles and payments accounts. For Google payments profiles, you can [ add and remove users or change permissions](https://support.google.com/paymentscenter/answer/7162853?ref_topic=9017383) in the Google payments center.

###  stars Key Decision: Use One or Multiple Google payments profiles?

Similar to Cloud Billing accounts, for administrative purposes, fewer payments profiles are generally recommended. For most customers, creating additional payments profiles adds more overhead and exposure to potential issues.

You might want to [ create multiple payments profiles](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383#multiple-profiles) if:

  * You want separate personal and business payments profiles tied to your Google Account.
  * You want to manage payments profiles for more than one business or organization.
  * You want payments profiles in multiple countries. You might have to create a new profile when changing countries.



Your Cloud Billing accounts need to be linked to an appropriate Google payments profile.

### Important Roles

payment Google payments profile Admin  
The payments profile Admin can: 

  * View and manage payment methods for the payments profile at large
  * Make payments
  * View payment accounts and invoices
  * Modify payments profile account settings
  * See the other Google services associated with the payments profile.

|  Recommended Assignee  
The Google payments profile Admins in your organization are typically part of your Finance or Accounting teams.   
---|---  
payment Google payments profile Read access  
The payments profile Read access user can: 

  * View the payments profile
  * View subscriptions and services
  * View invoices

|  Recommended Assignee  
Assign Read access to users who just need to receive email notifications (for invoices).   
Learn more about [ Google payments profile user permissions](https://support.google.com/paymentscenter/answer/7162853?ref_topic=9017383#user_permissions).  
**Caution:** Your Google payments profile contains important billing information but it's administered outside of your Organization hierarchy. Ensure its information is regularly reviewed and up to date by setting up more than one payments profile Admin who handles this information. We recommend tasking an administrator to make regular reviews of your payments profile's information. 

### Checklist

1\. Create the Resource  
---  
❑ | star [ Create a _Business type_ payments profile](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383) for use with Google Cloud. If an _invoiced_ Cloud Billing account was created for you, this step is already done for you. If you're setting up a Cloud Billing account online, you'll create (or select) a Google payments profile as part of the billing-account-creation process. **Note:** When creating a Cloud Billing account, you're given the option to select an existing Google payments account or to create a new payments profile. To simplify the management of your Cloud Billing account, whenever possible, we recommend [ reusing an existing _business_ payments profile](https://support.google.com/paymentscenter/answer/9001433?ref_topic=9017383) instead of creating a new Google payments profile.  
2\. Configure Access  
❑ | Assign more than one [ Google payments profile Admin](https://support.google.com/paymentscenter/answer/7162853?ref_topic=9017383) to be in charge of editing information like addresses, payment methods, tax information, and other account settings. **Caution:** Any permissions related to a Google payments profile apply to _all_ of the products associated with that profile. Whoever has these permissions should: 

  * Have the authority to view or edit information that can affect other products in that Google payments profile (for example, products other than Google Cloud might include Google Adwords);
  * Be aware of this scope of access when reviewing invoices or account alerts to ensure they apply to the correct product (for example, an account alert might be triggered by Google Adwords but doesn't apply to Google Cloud).

**Note:** To ensure users can receive monthly invoices and important communications about Google payments profile issues, [ new Google payments profile users and administrators](https://support.google.com/paymentscenter/answer/7162853?ref_topic=9017383) will need to verify their email address.   
❑ | For invoiced billing, assign multiple [ invoice delivery addresses](https://support.google.com/a/answer/1355902), both for email delivery and for paper invoice delivery, to ensure that you're always aware of when a new invoice has been sent out.   
❑ | For electronic notifications and monthly statements, [ add users](https://support.google.com/paymentscenter/answer/7162853#add-users) and set their [ email preferences](https://support.google.com/paymentscenter/answer/7162853#email_prefs) to receive documents and notices.   
3\. Configure the Resource  
❑ | Regularly review the information on your Google payments profile to ensure it's up to date, especially physical and email addresses, payments users, and payment instruments. **Warning:** Out-of-date information can lead to missed notifications, lost access, or missed payments.  
❑ | If not on invoiced billing: 

  * payment [ Add a backup payment method](https://cloud.google.com/billing/docs/how-to/payment-methods) as a safety net, in case the primary method is declined.
  * Regularly review your [ cost and payment history](https://cloud.google.com/billing/docs/how-to/view-history).

  
❑ | For invoiced billing: 

  * Each month, [ review your invoice](https://docs.cloud.google.com/billing/docs/how-to/read-invoice) carefully, and look for anomalies and unexpected changes.
  * Regularly check for any unapplied credits and payments to ensure that your monthly payments and credits are correctly applied to your invoices. For help, reach out to our collections team to [ apply any unmatched credits](https://support.google.com/a/answer/1355978) you might have.

  
  
* * *

## Projects, Folders, and Labels

Projects, folders, and labels help you create logical groupings of resources that support your management and cost attribution requirements.

![Projects, folders, and labels in the Resource Hierarchy](https://docs.cloud.google.com/static/billing/docs/images/projects-folders-labels-in-hierarchy.png)

### Overview

Projects are:

  * Required to use resources (such as Compute Engine virtual machines, Pub/Sub topics, and Cloud Storage buckets)
  * The base-level organizing entity in Google Cloud – all service-level resources are parented by projects
  * Used to form the basis for enabling services, APIs, and IAM permissions



Folders are:

  * A grouping mechanism for projects and can contain both projects and other folders
  * Used to group resources that share common IAM policies
  * Mapped under an Organization node (you must have an Organization node to use folders)



Labels are:

  * Used to categorize your Google Cloud resources (such as Compute Engine instances)
  * Key-value pairs you attach to resources, letting you filter resources based on their labels
  * Great for cost tracking at a granular-level because they're forwarded to the billing system so you can analyze your charges by label



###  stars Key Decision: Folders and Projects Strategy

#### Projects are required. Folders are optional, but recommended.

**Why use projects?** Projects are the basic organizing entity in Google Cloud. Projects are required to use service-level resources, such as Compute Engine and Cloud Storage. Service-level resources inherit project settings and permissions. You might need to create multiple projects, depending on the number of products or services you're running on Google Cloud. You'll want to define a meaningful naming strategy for your projects so you can easily identify them. For more details about projects, see [ Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Why use folders?** Folders group projects, centrally applying consistent policies and permissions across them. You might want to group your resources together logically using folders, depending on the number of people and teams you have who will be using Google Cloud, and the number of products and services you'll be running on Google Cloud. For example, you could set up separate folders for development, staging, and production projects for a service. Or, you might choose to spread the projects and services across folders that reflect different environments. You could use folders to organize your projects by departments within your company. One benefit of using folders is you can enforce different IAM policies on each folder. For more details about using folders, see [ Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).

**Why use labels?** Labels annotate resources within and across projects. Depending on your cost tracking requirements, you might want to apply labels to resources to identify them by what they are, what they do, or what team they're related to. For example, you might label all of your Compute Engine instances that are HTTP servers, or label all of the components that are related to your database service. For more details about using labels, see [ Creating and Managing Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

### Important Roles

Role: Project Creator  
The Project Creator role lets you create Projects and inherently lets resources be spun up on Google Cloud and incur usage.  |  Recommended Assignee  
Project Creators in your organization might be team leads or service accounts (for automation).   
---|---  
Role: Project Owner and User  
The Project Owner and User role lets you see costs and usage in a project and label resources.  |  Recommended Assignee  
Project owners and users in your organization might be team leads or developers.   
Learn more about [Project roles](https://docs.cloud.google.com/resource-manager/docs/access-control-proj).   
folder Role: Folder Administrator  
The Folder Administrator can create and edit the IAM policy of folders. They decide how roles are inherited by Projects in the folders.  |  Recommended Assignee  
The Folder Administrator manages finer access control, and is typically a department head or team manager.   
---|---  
Learn more about [Folder roles](https://docs.cloud.google.com/resource-manager/docs/access-control-folders).   
  
**Note: Want to control who can view costs?**

Different roles applied at different levels contain permissions that allow access to view costs.

For example, if you want a user to be able to view costs for an entire billing account, including all of its projects, set the `billing.accounts.getSpendingInformation` permission on the billing account level. The following predefined roles grant this permission by default: Billing Account Administrator, Billing Account Costs Manager, and Billing Account Viewer. 

If you want to limit a user to viewing only the costs for a _specific project_ , give the user the `billing.resourceCosts.get` permission on the project. The following predefined roles grant this permission by default: Project Owner, Project Editor, and Project Viewer.

For more information, see [ Overview of billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access) and [Custom roles for billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles).

### Checklist

1\. Create the Resource  
---  
❑ | star [ Create Projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to group resources together that share a common goal, theme, or purpose. If a product or service needs to use multiple Google Cloud resources, like Compute and Storage, use Projects to group them together. **Note:** Project Creators in your organization should be [ assigned the Billing Account User role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in_iam_name_short) on your Organization's Billing Account so that they can link projects to a Billing Account. All active Projects should have a linked Billing Account.   
❑ | star [ Name Projects meaningfully](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). Decide on a strategy for naming your projects. For example, you could name your project to reflect the service and the collection of resources it contains, such as _productname-prod_. The project name is a human-readable way to identify your projects. The project ID is generated from the project name you enter when you create the project in the Google Cloud Console.   
❑ | [ Set up folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) to mirror the way you work in your organization and on your infrastructure.   
2\. Configure Access  
❑ | [ Use Folders to specify IAM permissions](https://docs.cloud.google.com/resource-manager/docs/access-control-folders) for teams, products, services, or environments.   
❑ | [ Set project-level IAM permissions](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) as needed (if you aren't using folders or need another level of granularity).   
3\. Configure the Resource  
❑ | star [ Place a lien on critical projects](https://docs.cloud.google.com/resource-manager/docs/project-liens). To prevent projects from being accidentally deleted, add protections against project deletion with liens. You can place a lien upon a project to block the project's deletion until you remove the lien. This can be useful to protect important projects.   
❑ | attach_money [Use Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) to further categorize your resources. You can use labels to tag resources cross-Project and cross-Folder. Each resource can be tagged with multiple labels. Information about labels is forwarded to the billing system and picked up in [Billing Export](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) so they're useful in cost reporting and analysis. **attach_money Note:** Labels and Project Names are key in cost management. The names propagate to Billing Export and can be used to answer questions like "How much am I spending on databases?" and "What projects are costing me the most this month?"   
❑ | Decide whether or not you'll be purchasing [ Committed Use Discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for your Projects and understand how [ Sustained Use Discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) apply to your Compute Engine resources and bills.   
❑ | If needed, review how quotas work and [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).   
❑ | If needed, [ enable APIs for your projects](https://docs.cloud.google.com/apis/docs/overview). [Enabling an API](https://docs.cloud.google.com/apis/docs/enable-disable-apis) associates it with the current project, adds monitoring pages, and enables billing for that API if billing is enabled for the project.   
  
* * *

## Learn More

video_library [ Video library: Google Cloud Cost Management. Learn best practices for monitoring and managing your costs.](https://www.youtube.com/playlist?list=PLIivdWyY5sqKeXavu1XuBNBDLBO31kzM0)

### Cloud OnAir: Getting Started with Google Cloud Cost Management

To maximize the move to Google Cloud, organizations need a clear understanding of their Google Cloud costs. During this webinar, we'll share best practices for how to get started with managing your Google Cloud costs and usage. We'll demo how to set up billing accounts, organizations, projects, basic permissions, and budgets. We'll also introduce Billing reports to help you understand your current cost trends and forecast your spend at month-end so that you can prevent budget overruns.

### Creating Interactive Cost and KPI Dashboards Using BigQuery (Cloud Next '19)

Want more granular insight into your cloud costs, usage, and overall spend per KPI? During this session, you'll learn how to export billing data using BigQuery, write advanced billing and KPI-related queries, share custom views with internal stakeholders, and build detailed dashboards in Data Studio and Elastic to better understand your cost drivers. PerimeterX will join us on stage to speak to exactly how they use this functionality as a customer to tie their Google Cloud costs to key business metrics.

### Monitoring and Controlling Your Google Cloud Costs (Cloud Next '19)

Managing Google Cloud usage and cost trends is easier than you think. In this session, you'll learn how to quickly view your Google Cloud costs, forecast your month-end bill, and provide an overview of some of the controls you can put in place to prevent budget overruns. In addition, we'll provide a live demo of how to set up custom dashboards to further analyze your billing data.

### Saving Even More Money on Compute Engine (Cloud Next '19)

In the time since Next '18's _Saving More Money on Compute Engine_ , a lot has changed, but customers like you are still looking to control costs and get the most capability out of every cloud dollar. In this talk, you'll learn about the latest products and techniques for optimizing your usage to get the most compute for the lowest bill.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
