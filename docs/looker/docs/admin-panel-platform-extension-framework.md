---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework/
title: Admin settings - Extension Framework \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:38.432974+00:00
---

# Admin settings - Extension Framework  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Extension Framework Stay organized with collections  Save and categorize content based on your preferences. 

The **Extension Framework** page in the **Platform** section of the **Admin** menu lets you enable or disable Looker extension framework options.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Extension Framework

When enabled, the **Extension Framework** option lets developers build and run Looker-hosted applications as well as install and run extensions from the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace), such as the [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) and the [Data Dictionary](https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary). This feature is enabled by default.

When this feature is disabled, any extensions that have been installed are hidden and unavailable to users.

Pricing, terms, and other details for Marketplace content and extensions such as the API Explorer and Data Dictionary are listed within the relevant store page. Before users can install and use Marketplace extensions, a Looker admin must enable the [Marketplace](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) feature.

## Enhanced Extension Loading

To address potential [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) violations, there is a new, enhanced loading mechanism for the Looker extension framework, which includes the following changes:

  * To fix Content Security Policy (CSP) violations, HTML is generated to load an extension on the server rather than in the browser.
  * The `base` tag is removed, which potentially could impact custom code splitting.
  * The new loader uses a `<!DOCTYPE html>` preamble. This may impact components that use `height: 100%;`. You can mitigate this by using `height: 100vh`.



To use the enhanced loading mechanism, a Looker admin can enable **Enhanced Extension Loading**.

**Warning:** The enhanced loader may cause errors with existing extensions. Disable this option to use the legacy extension framework loader.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
