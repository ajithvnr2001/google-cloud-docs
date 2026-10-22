---
url: https://docs.cloud.google.com/looker/docs/looker-core-admin-looker/
title: Looker (Google Cloud core) admin settings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:26.361757+00:00
---

# Looker (Google Cloud core) admin settings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-admin-looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker (Google Cloud core) admin settings Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the Admin panel settings available within a Looker (Google Cloud core) instance. Learn about the different sections for user management, authentication, platform configuration, and more to effectively handle instance administration. To reach the Admin panel, select **Admin** from the main menu within the Looker (Google Cloud core) instance.

## Required permission

To manage users within a Looker (Google Cloud core) instance, you must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets) within Looker.

## Administrative settings available within the Looker (Google Cloud core) instance

You can refer to the list of [Administrative tutorials](https://docs.cloud.google.com/looker/docs/set-up-and-administer-looker#administrative-tutorials) for how to perform various administrative tasks for users of your instance. Additionally, the following documentation pages describe Looker's administration functions for the latest version of Looker. Exceptions for Looker (Google Cloud core) instances are noted on this page.

  * [**General** pages](https://docs.cloud.google.com/looker/docs/admin-panel-general-pages) — View a list of pages about setting system-wide options, creating a custom help page for your users, setting a default homepage for your instance or for a user or group.

> The following **General** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The [**Preview Features**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) page is available in Looker (Google Cloud core). However, the preview features that are categorized as [Labs features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#labs-features) are not available and are not visible inside Looker (Google Cloud core) instances.
>     * The [**Legacy features**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) Admin panel page is not available for Looker (Google Cloud core) instances. Legacy features default to off in Looker (Google Cloud core).
>     * The [**Support Access**](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access) Admin panel page is available in Looker (Google Cloud core). However, support access is only available for public IP instances. See the [Getting support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-support) documentation page for information about accessing support.
>     * The [**Technical Contacts**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#technical_contacts) setting is now managed [within the Google Cloud console](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).
>     * The [**Email Domain Allowlist**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) setting has moved into the Google Cloud console. See the [Edit the Looker (Google Cloud core) instance configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#edit_instance_settings) documentation for instructions on setting the email domain allowlist.
>     * The [**Host URL**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#host_url) setting has moved into the Google Cloud console. See the [Set up a custom domain for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) documentation page for information on setting up a custom domain.
>     * The [**License Key**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#license_key) setting is not available in Looker (Google Cloud core) instances.
>     * The [**Export**](https://docs.cloud.google.com/looker/docs/admin-panel-export) page is not available in Looker (Google Cloud core). To export a Looker (Google Cloud core) instance, follow the steps on the [One-time data import or export for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-import-export) documentation page.

  * [**System Activity** pages](https://docs.cloud.google.com/looker/docs/system-activity-pages) — View information about the System Activity dashboards, which show user activity, content activity, and performance data for your Looker instance.

> The following **System Activity** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * Performance recommendations are not available for Looker (Google Cloud core) instances.
>     * [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) is available for **Enterprise** and **Embed** [editions](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core), but not for the **Standard** edition.

  * [**Users** pages](https://docs.cloud.google.com/looker/docs/admin-panel-users-pages) — View a list of pages about configuring users, groups, roles, and user attributes; managing user and group access to saved content; and viewing and resetting locked user accounts.

> The following **Users** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The **Users** page functions slightly differently in Looker (Google Cloud core). See the [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management#the_users_page) documentation page for details on using the **Users** page with Looker (Google Cloud core).
>     * The [**Custom Welcome Email**](https://docs.cloud.google.com/looker/docs/admin-panel-users-custom-welcome-email) Admin panel page is not available in Looker (Google Cloud core) instances.

  * [**Database** pages](https://docs.cloud.google.com/looker/docs/admin-panel-database-pages) — View a list of pages about configured database connections, database query history, persistent derived tables, and datagroups.

> The following **Database** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The [**SSH Server** tab](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#ssh_servers_tab) is not available for Looker (Google Cloud core) instances.

  * [**Alerts & Schedules** pages](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-pages) — View a list of pages about managing user alerts and schedules, viewing alert and schedule histories, specifying an emailed data policy, and monitoring data that is sent to external email addresses.

  * [**Platform** pages](https://docs.cloud.google.com/looker/docs/admin-panel-platform-pages) — View a list of pages about setting system-wide options for integrated services, Looker's API, embedded content, email deliveries, and custom visualization types.

> The following **Platform** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The Looker Action Hub on the [**Actions** page](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) is available only for [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#both_public_and_private_ip_connections) network connections.
> 
>     * The [**BI Connectors** page](https://docs.cloud.google.com/looker/docs/bi-connectors) is available only for [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#both_public_and_private_ip_connections) network connections. Additionally, all BI connectors are enabled by default for Looker (Google Cloud core) instances that use public public secure connections or hybrid connections.
> 
>     * The [**Marketplace** page](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) isn't available in Looker (Google Cloud core) instances that use private services access connections. However, Looker (Google Cloud core) instances that use Private Service Connect connections can [connect to Marketplace](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#connect-to-marketplace).
> 
>     * The [**Themes**](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) and [**Private Label**](https://docs.cloud.google.com/looker/docs/privatelabel) pages are available for the [**Enterprise**](https://docs.cloud.google.com/looker/docs/looker-core-overview#enterprise_edition) and [**Embed**](https://docs.cloud.google.com/looker/docs/looker-core-overview#embed_edition) editions of Looker (Google Cloud core), but not for the **Standard** edition.
> 
>     * The [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed) page is available for the [**Embed**](https://docs.cloud.google.com/looker/docs/looker-core-overview#embed_edition) edition of Looker (Google Cloud core), but not for the **Standard** or **Enterprise** editions.
> 
>     * The [**Gemini in Looker**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) page is available for all [editions](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core). For Looker (Google Cloud core) instances, Gemini in Looker is [enabled and administered](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) in the Google Cloud console.

  * [**Authentication** pages](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-pages) — View a list of pages about configuring various authentication methods, including passwords and two-factor authentication, along with configuring options to allow users to stay logged in to Looker.

> The following **Authentication** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * When Workforce Identity Federation is enabled for your Looker (Google Cloud core) instance, the [**Workforce authentication**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-workforce-identity) page is available to configure attribute mapping, group mirroring, default roles, and login behavior.
>     * The [**SAML**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml) and [**OpenID Connect**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect) pages are available only if you choose Google OAuth as the [primary authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication#primary-authentication-methods) for your Looker (Google Cloud core) instance.
>     * Setting up the Google OAuth client and credentials now happens [within the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth). For Looker (Google Cloud core), the [**Google authentication**](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) page is used only to set the [default Looker role](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#setting_a_default_looker_role_within_the_instance) and [merge options](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#specify_the_method_used_to_merge_oauth_users_to_a_account).
>     * The [**Passwords**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-password), [**Two-Factor**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-two-factor), and [**LDAP**](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap) pages are not available for Looker (Google Cloud core).

  * The [**Server** pages](https://docs.cloud.google.com/looker/docs/admin-panel-server-pages) are not available for Looker (Google Cloud core).




## What's next

  * [Administer your Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)
  * [User authentication methods for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
