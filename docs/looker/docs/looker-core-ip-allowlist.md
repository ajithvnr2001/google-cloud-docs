---
url: https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist/
title: Configure an IP allowlist for Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:24.011570+00:00
---

# Configure an IP allowlist for Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Configure an IP allowlist for Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create an IP allowlist for a Looker (Google Cloud core) instance that uses [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip). An IP allowlist is a networking feature that increases security by restricting access to your instance to only the IP addresses that you specify.

## Before you begin

  1. Ensure that you have an existing Looker (Google Cloud core) instance that uses public secure connections or hybrid connections.
  2. To get the permissions that you need to modify a Looker instance, ask your administrator to grant you the Looker Admin (`roles/looker.admin`) Identity and Access Management (IAM) role on the project.



## Configure an IP allowlist

To configure an IP allowlist for your instance, perform the following steps:

### Console

  1. In the Google Cloud console, go to the Looker (Google Cloud core) **Instances** page.

[Go to Instances](https://console.cloud.google.com/looker/instances)

  2. Click the name of the instance that you want to edit.

  3. On the instance **Details** tab, click **Edit**.

  4. In the **Configure inbound connections** section, select the **Enable IP allowlist** checkbox to create the allowlist.

  5. Click **Add Item** to add an IP allowlist rule.

  6. In the **Rule name** field, enter a name for the rule.

  7. In the **IP range** field, enter the range of approved IP addresses in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

  8. Click **Save**.




## Remove an IP allowlist rule from the allowlist

To remove an IP allowlist rule from the allowlist, perform the following steps:

### Console

  1. In the Google Cloud console, go to the Looker (Google Cloud core) **Instances** page.

[Go to Instances](https://console.cloud.google.com/looker/instances)

  2. Click the name of the instance that you want to edit.

  3. On the instance **Details** tab, click **Edit**.

  4. Hold the pointer over the rule you want to remove and click the **Delete item** trash icon that appears.




## Allow connections to Google services

If your Looker (Google Cloud core) instance uses an IP allowlist, you must grant access to the IP ranges used by other Google Cloud services before you can use those services with Looker (Google Cloud core).

Selecting the **Link Google services with this instance** checkbox adds the following Google services to the instance's IP allowlist:

  * [Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup)
  * [Data Studio connector](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker)
  * [Connected Sheets](https://docs.cloud.google.com/looker/docs/connected-sheets)
  * [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub)



To connect to other Google Cloud services, you must add their IP ranges to the IP allowlist as new rules.

## IP allowlist considerations

When you configure an IP allowlist, keep the following points in mind:

  * Allowlist rules apply to all ingress traffic for both UI and API logins.
  * Adding more than 50 rules might negatively impact your instance's performance.
  * Certain features, such as the Slack integration and OAuth-enabled actions, don't work when the IP allowlist is enabled.
  * Enabling an IP allowlist means that you must add to the allowlist the IP ranges for any Google services that you want to use within Looker (Google Cloud core). For some services, you can use the **Link Google services with this instance** checkbox, but for other services not covered by that checkbox, you must add the service's IP range directly to the allowlist.



## What's next

  * Learn about [setting up a custom domain for your instance](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain).
  * Learn about [connecting your instance to external services](https://docs.cloud.google.com/looker/docs/looker-core#connect_to_external_services).
  * Learn how to [manage users in Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
