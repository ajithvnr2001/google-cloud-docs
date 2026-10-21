---
url: https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist/
title: Admin settings - IP Allowlist \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:53.838746+00:00
---

# Admin settings - IP Allowlist  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - IP Allowlist Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances don't include this page. For Looker (Google Cloud core) instances that use public secure connections or hybrid connections, you can add particular IP ranges to an allowlist by [editing your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings) in the Google Cloud console or with the Google Cloud CLI.

The **IP Allowlist** page in the **Admin** menu lets you specify which IP addresses and subnet masks can access your Looker instance. When the allowlist is enabled, it filters traffic at the application level to accept connections _only_ from approved IP addresses and refuses all other attempts. This feature is available only for Looker-hosted instances and doesn't appear on customer-hosted deployments. To enable regional IP addresses to allow for database connections, see [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_1_ip_address_allowlist).

## Viewing the IP Allowlist page

To view the **IP Allowlist** page, from the **Server** section of the **Admin** menu, select **IP Allowlist**.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

The **IP Allowlist** page lists the rules that configure which IP addresses and subnet masks can access your Looker instance. Each rule also defines whether users from those IP addresses can sign in only from the Looker UI, only from the Looker API, or from both sources. When the IP allowlist is disabled, your Looker instance can accept connections from any IP address.

In addition to viewing existing IP allowlist rules, you can perform the following tasks:

  * Enable or disable the IP allowlist with the **Enable Allowlist** setting. When the allowlist is active, only users from listed IP address can connect.
  * Define a new rule, which adds more IP addresses to the allowlist.
  * Enable, disable, edit, or delete an existing rule.
  * Grant access to essential Google Cloud services.



## Enabling the IP allowlist setting

**Important:** The first IP allowlist rule to define for your instance is one that allows your detected IP address to access the instance. Adding your detected IP address to the IP allowlist rules prevents you from being denied access to the instance once you turn on the **Enable Allowlist** setting.

If no IP allowlist rules have been defined for your Looker instance, the **IP Allowlist** page displays the following message: "Your IP address is not allowlisted." You must define an IP allowlist rule for the IP address that you are using to access the Looker instance before you can turn on the **Enable Allowlist** setting.

To add your IP address to your instance allowlist, follow these steps:

  1. Select the **Your IP address is not allowlisted** text. Looker displays a dialog that displays your source public IP address with the following message: "No currently enabled rules allow access via your IP address. You must first create or enable a rule to allowlist yourself before you can enable the IP Allowlist feature. Your detected IP address is 192.168.1.1."
  2. Copy your detected IP address.
  3. Add a rule that includes your IP address.
  4. After saving the rule, turn on the **Enable Allowlist** setting.
  5. Optionally, enable the **Allow Google Cloud services** setting to grant essential Google Cloud services access to the instance.



## Adding a new rule

Select **Add Rule** to add an IP address or a range of addresses to the allowlist. Looker displays the **New IP Allowlist Rule** dialog. To add a new rule, follow these steps:

![](https://docs.cloud.google.com/static/looker/docs/images/admin-ip-allowlist-new-rule-2308.png)

  1. Enter a name for the new rule in the **Label** field.
  2. Enter a range of approved IP addresses in the **IP Range** field using an IP address and a subnet mask, as described in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
  3. Specify whether the new rule applies only to login attempts from the Looker UI, only to login attempts from the Looker API, or to login attempts from both sources in the **UI or API?** drop-down menu.
  4. Select **Save**.



## Things to know

While configuring your IP allowlist, keep the following considerations in mind:

  * Adding more than 50 rules may negatively impact Looker's performance.
  * Certain Looker Action Hub features such as the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) and [OAuth-enabled actions](https://docs.cloud.google.com/looker/docs/action-hub#configuring_an_action_for_oauth) don't work when the IP allowlist is enabled.
  * To integrate [Git pull requests](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project) with any LookML projects, you need to add to the allowlist the range of IP addresses from which your Git provider makes outbound requests. For example, GitHub IP addresses are [available from their meta API endpoint](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses). IPs are subject to change and will be different for other Git providers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
