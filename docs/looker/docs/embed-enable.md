---
url: https://docs.cloud.google.com/looker/docs/embed-enable/
title: Getting started with embedding \u2014 enabling signed embedding \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:03.609821+00:00
---

# Getting started with embedding — enabling signed embedding  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/embed-enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Getting started with embedding — enabling signed embedding Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are using a Looker (Google Cloud core) instance, to enable signed embedding you must use the Embed edition of Looker (Google Cloud core). If you are using a Looker (original) instance, signed embedding must be enabled for your instance. [Contact a Google Cloud sales specialist](https://cloud.google.com/contact) to enable this feature.

[Signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) is a way to present private embedded Looks, visualizations, Explores, dashboards, or LookML dashboards to your users without requiring them to have a separate Looker login. Instead, users will be authenticated through your own application.

Before you can use signed embedding on your Looker instance, you must enable signed embedding in the Looker Admin panel and then create an embed secret. The embed secret validates that a signed embedding request is legitimate and hasn't been forged by someone else. To enable signed embedding, follow these steps:

  1. In the **Admin** section of Looker, navigate to the **Embed** page.
**Note:** You must be a [Looker admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or have the [`manage_embed_settings` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_embed_settings) to view the **Embed** page. 
  2. In the **Embed SSO Authentication** drop-down, if the option is set to **Disabled** select **Enabled** and then click **Update**.

Looker will display additional **Embed** options.

  3. ​​To generate your embed secret key, select the **Set Secret** button in the **Embed Secret** section.
**Important:** Be sure to copy the embed secret key to a secure location. You won't be able to retrieve the key from Looker again without resetting it. Resetting the embed secret key will break any embeds that used the old key. **Important:** Any user, with any permission level, who has access to the secret key can create a URL to access any model that the Looker instance is connected to. [Protect the signed embed secret](https://docs.cloud.google.com/looker/docs/security-best-practices-embedded-analytics#single_sign-on_embedding) as you would admin credentials to your embedded Looker instance, and keep signed embedding disabled if you're not using it. 
  4. If your application will be using [JavaScript events](https://docs.cloud.google.com/looker/docs/embedded-javascript-events) passing to communicate between the iframe where Looker is embedded and the parent application, add the domain name of your parent application to the **Embedded Domain Allowlist** field.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
