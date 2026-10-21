---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-allow-xhtml-style-empty-tags-in-custom-visualizations-legacy-feature/
title: Allowing XHTML-style empty tags in custom visualizations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:38.194543+00:00
---

# Allowing XHTML-style empty tags in custom visualizations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-allow-xhtml-style-empty-tags-in-custom-visualizations-legacy-feature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Allowing XHTML-style empty tags in custom visualizations Stay organized with collections  Save and categorize content based on your preferences. 

A cross-site scripting (XSS) vulnerability, [CVE-2020-11022](https://nvd.nist.gov/vuln/detail/cve-2020-11022), exists in jQuery versions later than or equal to 1.2 and earlier than 3.5.0. This flaw allows an attacker with the ability to supply input to the `parseHTML()` function to inject JavaScript into the page when that input is rendered and to have it delivered by the browser. In Looker 21.18 and earlier, the version of jQuery that was provided as a global variable to a sandboxed [custom visualization](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations) included this vulnerability. 

Starting in Looker 21.20, the built-in jQuery instance that is available to custom visualizations has been updated, and this vulnerability has been addressed. As a result of addressing this vulnerability, Looker will no longer recognize self-closing XHTML tags, such as `<div />` in custom visualizations. 

In Looker 21.20, a new [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule), **Allow XHTML-style Empty Tags in Custom Visualizations** , is included in the **Legacy Features** page in Looker's **Admin** section. Enabling this legacy feature disables protection against CVE-2020-11022, causing self-closing XHTML tags to be recognized in custom visualizations, but also exposing the jQuery vulnerability. If you enable this legacy feature, we strongly recommend that you audit your custom visualizations for self-closing tags, correct any self-closing tags, and disable the legacy feature. This legacy feature is scheduled to be disabled in Looker 22.20, and self-closing XHTML tags will not be allowed. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
