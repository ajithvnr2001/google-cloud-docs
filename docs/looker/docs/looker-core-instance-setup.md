---
url: https://docs.cloud.google.com/looker/docs/looker-core-instance-setup/
title: Prepare a Looker (Google Cloud core) instance for users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:33.573393+00:00
---

# Prepare a Looker (Google Cloud core) instance for users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-instance-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Prepare a Looker (Google Cloud core) instance for users Stay organized with collections  Save and categorize content based on your preferences. 

As a Looker admin, you configure your Looker (Google Cloud core) instance to ensure that your team has the necessary access, environment, and data models for their analytics workflows. This guide explains how to set up your instance to facilitate your team's use of Looker (Google Cloud core).

## Set up tasks

You can perform the following setup tasks for your instance:

  * Create a LookML project
  * Set a Looker homepage
  * Set up announcements for your users
  * Understand Looker roles and permissions
  * Configure an email domain allowlist
  * Configure business user features
  * Add and manage Looker (Google Cloud core) users
  * Share performance recommendations



## Create a LookML model

Once an instance contains a [database connection](https://docs.cloud.google.com/looker/docs/looker-core-dialects#setup_database), you are ready to set up a LookML model.

LookML models are located inside LookML projects. A LookML project contains collections of LookML files that describe how your database tables are related to each other and how Looker should interpret those tables. Once a model is set up, users can interact with the data, including [exploring data](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), creating [dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards), and setting up [alerts](https://docs.cloud.google.com/looker/docs/alerts-overview), among other things.

You can set up a LookML model within a Looker (Google Cloud core) instance if you have one of the following roles:

  * [Admin Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets)
  * [Developer Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets)



The steps for creating LookML models and projects are listed on the [Generating a LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model) documentation page. Alternatively, you can follow the **Set up Looker** guide that appears dynamically within the Looker (Google Cloud core) instance.

If you want to [customize the LookML](https://docs.cloud.google.com/looker/docs/lookml-validation) in your model, you can [access your project files](https://docs.cloud.google.com/looker/docs/accessing-project-files) in two ways:

  * from the **Develop** menu in the [main navigation panel](https://docs.cloud.google.com/looker/docs/finding-content)
  * by expanding **Edit project files** and clicking **edit project** in the **Set up Looker** guide



Click the name of your project to open its LookML files. See the [Introduction to LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) documentation page to learn more about LookML development.

Additionally, the [Best practice: Create a positive experience for Looker users](https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-positive-experience-for-looker-users) article provides recommendations on how to use LookML to improve the experiences of Looker (Google Cloud core) users.

Looker (Google Cloud core) also provides a sample LookML project that can help you learn to write LookML, query data, and view dashboards. The sample LookML project is provided on Looker (Google Cloud core) instances of all [edition types](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions). See the [Use the sample LookML project on a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-sample-project) documentation page for more information about accessing and using the sample LookML project on your instance.

## Set a Looker homepage

The homepage appears when users log in to Looker (Google Cloud core), navigate to the homepage by clicking **Home** in the main navigation panel, or click the Looker logo in the instance. By default, the homepage for your instance is the [prebuilt Looker homepage](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage), which displays a user's favorite content, that user's recently viewed content, and the recently viewed content at the organization. However, those with the Admin Looker role can change this default to a URL within Looker (Google Cloud core). Learn more about homepage settings on the [Admin settings - Homepage](https://docs.cloud.google.com/looker/docs/admin-panel-general-homepage) documentation page.

## Set up announcements for your users

If your instance uses the [prebuilt Looker homepage](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage), admins and users who have the [`manage_homepage` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_homepage) can customize announcements to users with the announcement sidebar. See the [Making announcements to your users](https://docs.cloud.google.com/looker/docs/making-announcements-to-your-users) documentation page for more information about the announcement sidebar.

**Tip:** Adding announcements with links to the [Build a Look with sample data](https://docs.cloud.google.com/looker/docs/looker-core-create-look-quickstart) Quickstart and the [Sample LookML project](https://docs.cloud.google.com/looker/docs/looker-core-sample-project) documentation page can be helpful for business users who are new to exploring in Looker (Google Cloud core) or developers who are new to using LookML.

## Understand Looker roles and permissions

Looker roles govern what users can do within a Looker (Google Cloud core) instance, and they are not the same as Google [IAM roles](https://docs.cloud.google.com/looker/docs/looker-core-access-control#iam-vs-looker-roles). For example, in order to [explore data](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) within a Looker (Google Cloud core) instance, users must have a role that contains the [`explore` Looker permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore). Learn more about roles and permissions on the [Admin settings - Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) documentation page.

Looker roles can be granted by default during first log in (see the documentation for [Google OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#default-role), [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#default_groups_and_roles), or [OIDC](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect#default_groups_and_roles)), through group mirroring with [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#enabling_mirror_saml_groups) or [OIDC](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect#enabling_mirror_openid_connect_groups), or manually by an Admin on the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#roles_2) or [**Groups**](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#adding_roles_to_groups) pages.

## Configure an email domain allowlist

The **Email Domain Allowlist for Scheduled Content** setting in the Google Cloud console defines the email domains to which your Looker (Google Cloud core) users can [deliver](https://docs.cloud.google.com/looker/docs/scheduling) Looker content — [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks), [dashboards](https://docs.cloud.google.com/looker/docs/dashboards), [queries](https://docs.cloud.google.com/looker/docs/delivering-looks-explores) with visualizations — or [alert notifications](https://docs.cloud.google.com/looker/docs/alerts-overview) through email. By default, there are no domains in the allowlist at the time of instance creation and Looker (Google Cloud core) users who have the [appropriate Looker permissions to email content](https://docs.cloud.google.com/looker/docs/configuring-deliveries#granting_scheduling_permissions_for_users) can email content to any domain.

To limit content deliveries and alert notifications to email addresses with a specific domain, [edit the Looker (Google Cloud core) instance configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings) to restrict the domain(s) to which users can send emails. Users who have the [`schedule_external_look_emails`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_external_look_emails) permission can send emails to any domain regardless of the **Email Domain Allowlist for Scheduled Content** settings. To learn more about the email domain allowlist and how it interacts with permissions and user attributes, see the [Email domain allowlist for scheduled content](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) documentation.

**Note:** By default, Looker (Google Cloud core) instances that use only private connections or hybrid connections allow email deliveries to external domains. To restrict the domains to which Looker users can send email deliveries, you can set up an [email domain allowlist](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings).

## Configure business user features

Some features in Looker (Google Cloud core) can be configured by an admin to allow or restrict their usage to certain users. See the [Managing business user features](https://docs.cloud.google.com/looker/docs/managing-business-user-features) documentation page to understand how you can set up features for your users.

## Add and manage Looker (Google Cloud core) users

Once your instance is configured, you can [choose an authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication) and add and manage users. See the [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management) documentation page for more information.

## Share performance recommendations

Looker (Google Cloud core) performance can be enhanced through Admin settings, LookML developer patterns, and business user practices. See the [Looker performance documents](https://docs.cloud.google.com/looker/docs/performance-documentation) page for a list of documentation pages that contain tips and best practices for each kind of user. Share this information with your users to keep your Looker (Google Cloud core) instance as performant as possible.

## What's next

  * [User authentication methods for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
