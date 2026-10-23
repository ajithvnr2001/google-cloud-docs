---
url: https://docs.cloud.google.com/looker/docs/looker-core-feature-differences/
title: Feature availability in Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:30.425228+00:00
---

# Feature availability in Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-feature-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Feature availability in Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

Looker (Google Cloud core) features vary by instance type, edition, and network configuration. Understanding these differences is crucial for planning your Looker deployment and gaining appropriate feature access.

## Feature availability by instance type

The interface and functionality of a Looker (Google Cloud core) instance is virtually indistinguishable from a [Looker (original) instance](https://docs.cloud.google.com/looker/docs/intro), but the two instance types are not identical. Some differentiating characteristics include the following:

  * The administrative functions that are available in the instance Admin section
  * The database dialects that the instance can connect to



### Administrative compatibility by instance type

All administrative functions and settings for Looker (original) instances are managed in the [Admin section of the Looker (original) instance](https://docs.cloud.google.com/looker/docs/set-up-and-administer-looker). However, for Looker (Google Cloud core) instances, these settings are divided between the [Admin section of the Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker) and the [Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console).

### Database connection compatibility by instance type

The list of supported database dialects that you can [connect to your instance](https://docs.cloud.google.com/looker/docs/looker-core-dialects#setup_database) differs between Looker (original) and Looker (Google Cloud core).

For a list of database dialects that are supported by Looker (original) instances, see the [Looker dialects](https://docs.cloud.google.com/looker/docs/dialects) documentation page.

For a list of database dialects that are supported by Looker (Google Cloud core) instances, see the [Connecting Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) documentation page.

## Feature compatibility by edition type

Some Looker (Google Cloud core) features vary depending on the [instance edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions). See the [Looker (Google Cloud core) features and entitlements](https://docs.cloud.google.com/looker/docs/looker-core-edition-types) documentation page for more information.

## Feature compatibility by network configuration

Looker (Google Cloud core) instances can be configured with one of several [network configurations](https://docs.cloud.google.com/looker/docs/looker-core-networking-options). The following table shows feature compatibility for each network configuration. Select the checkboxes to filter the table.

Public connections — The feature is supported for instances with a public secure connection. 

Private connections — The feature is supported for instances with a private connection (using [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) or [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa)). 

Hybrid connections — The feature is supported for instances with both a hybrid connection (using [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) or [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa)). 

Not supported — The feature is not supported for instances with any network configuration. 

Select all Clear all

Feature | Network configuration support | Notes | [BI connectors](https://docs.cloud.google.com/looker/docs/bi-connectors) | 

  * Public connections
  * Private connections
  * Hybrid connections

| Enabled by default.The Looker connector, when used with Data Studio Pro or Looker reports, can't connect to a Looker (Google Cloud core) instance that is inside of a VPC Service Controls perimeter.  
---|---|---  
[Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration) | 

  * Public connections
  * Private connections
  * Hybrid connections

| Continuous Integration is available with private and hybrid connections only on instances that use Private Service Connect. Continuous Integration is also supported on Looker (Google Cloud core) instances that are enabled for [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek) or that are within a [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) perimeter. To use the CI GitHub app or the dbt Cloud integration on an instance with private connections, hybrid connections, or a VPC Service Controls perimeter, you must configure your network to allow ingress and egress traffic for GitHub and your dbt Cloud host URL.  
[Knowledge Catalog metadata management and lineage](https://docs.cloud.google.com/looker/docs/looker-core-dataplex) | 

  * Public connections
  * Private connections
  * Hybrid connections

|   
[conversational analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview), [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) | 

  * Public connections
  * Private connections
  * Hybrid connections

| conversational analytics is available for any network connection type, including instances within VPC Service Controls perimeters. Use of Advanced Analytics is not supported for Looker (Google Cloud core) instances that use CMEK or that are within a VPC Service Controls perimeter.   
[Custom Themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) | 

  * Public connections
  * Private connections
  * Hybrid connections

|  Available for the **Enterprise** and **Embed** editions. Not available for the **Standard** edition.  
[Deliver content to S3, SFTP, Webhook](https://docs.cloud.google.com/looker/docs/scheduling) | 

  * Public connections
  * Private connections
  * Hybrid connections

| For private connections instances, your Google Cloud project must be [configured to route traffic](https://docs.cloud.google.com/vpc/docs/routes) to the selected destination.  
[Dialect support](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) | 

  * Public connections
  * Private connections
  * Hybrid connections

| See the list of [supported database dialects](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported-dialects-for) for Looker (Google Cloud core).  
[Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) | 

  * Public connections
  * Private connections
  * Hybrid connections

|  Available for the **Enterprise** and **Embed** editions. Not available for the **Standard** edition.  
[Extension Framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) | 

  * Public connections
  * Private connections
  * Hybrid connections

|   
[Git connections](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) | 

  * Public connections
  * Private connections
  * Hybrid connections

|  You can connect a Looker (Google Cloud core) instance with any network configuration to customer-hosted Git repositories on the public internet. If your instance uses a private connections or hybrid connections, you must [configure the Google Cloud project](https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config) to connect to Git.  
[IP Allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) | 

  * Public connections
  * Hybrid connections

| For private connections instances, control access with your VPC settings.  
[LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), [email/password](https://docs.cloud.google.com/looker/docs/admin-panel-authentiation-password) authentication |  Not supported |   
[Local project import](https://docs.cloud.google.com/looker/docs/importing-projects#importing_local_projects) | 

  * Public connections
  * Private connections
  * Hybrid connections

|   
[Looker **Log** Admin panel page](https://docs.cloud.google.com/looker/docs/admin-panel-server-log) | Not supported | Google Cloud uses Cloud Logging. See [View instance logs for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-logging) for more information.  
[Looker Action Hub](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) | 

  * Public connections
  * Hybrid connections

|  [Custom actions](https://docs.cloud.google.com/looker/docs/action-hub#building_a_custom_action) can also be developed for a private action hub server. Data that your users send by using an action will be passed temporarily from your Looker (Google Cloud core) instance through the Looker Action Hub server. The Looker Action Hub is disabled by default. To enable an individual action, see the instructions in [Admin settings - Actions](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#enabling_an_action).  
[Preview Features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) | 

  * Public connections
  * Private connections
  * Hybrid connections

| Looker preview features are enabled on Looker (Google Cloud core). Preview features that are categorized as [Labs features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#labs-features) are not available in Looker (Google Cloud core).  
Looker [Legacy](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) features | Not supported | All Looker Legacy features are disabled on Looker (Google Cloud core).  
[Looker support access](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access) | 

  * Public connections

| If your instance uses a private connections or hybrid connections, see [Getting support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-support).  
[Looker Usage dashboard](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage) | Not supported | Use System Activity [dashboards](https://docs.cloud.google.com/looker/docs/system-activity-dashboards) and [Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) to view usage information.  
[Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp) | 

  * Public connections
  * Private connections
  * Hybrid connections

| This feature is in [preview](https://cloud.google.com/products#product-launch-stages).  
[Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) | 

  * Public connections
  * Private connections
  * Hybrid connections

| Marketplace is available with private and hybrid connections only on instances that use Private Service Connect.  
[Mobile application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) | 

  * Public connections
  * Private connections
  * Hybrid connections

| Available through the [Looker mobile app](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app).  
[Private embedding](https://docs.cloud.google.com/looker/docs/private-embedding) | 

  * Public connections
  * Private connections
  * Hybrid connections

| Available for all editions.  
[Restrict TLS cipher suites](https://docs.cloud.google.com/looker/docs/looker-core-tls-cipher-suites) | Public connections |   
[SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml), [OpenID Connect ](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect)authentication | 

  * Public connections
  * Private connections
  * Hybrid connections

|   
[Signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) | 

  * Public connections
  * Private connections
  * Hybrid connections

|  Available for the **Embed** edition. Not available for the **Standard** and **Enterprise** editions.  
[VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) |  Private connections |   
[Sudo](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_users) |  Not supported |   
[Sample LookML project](https://docs.cloud.google.com/looker/docs/looker-core-sample-project) | 

  * Public connections
  * Private connections
  * Hybrid connections

| To use the sample LookML project, the [BigQuery API](https://docs.cloud.google.com/looker/docs/looker-core-sample-project#before_you_begin_enable_the_bigquery_api) must be enabled for your Google Cloud project.  
[Google-managed certificates](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-google-managed-certs) | 

  * Private connections

| Google-managed certificates are available only for private connections instances that use Private Service Connect.  
[Global access](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#using_global_access) | 

  * Private connections

| Global access is available only for private connections instances that use Private Service Connect.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
