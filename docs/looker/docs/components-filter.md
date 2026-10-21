---
url: https://docs.cloud.google.com/looker/docs/components-filter/
title: Looker filter components \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:17:57.565122+00:00
---

# Looker filter components  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/components-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker filter components Stay organized with collections  Save and categorize content based on your preferences. 

> Looker filter components provide Looker's rich filter functionality for custom data applications that are built on top of Looker.

## Looker components

[Looker components](https://docs.cloud.google.com/looker/docs/components-getting-started) are React-based, prebuilt pieces of Looker's application. Application developers can use components in data applications and extensions that are built on top of Looker.

Components can be used with the [Looker extension framework](https://docs.cloud.google.com/looker/docs/extension-framework) and [Looker's Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk).

## Looker filter components

Filter components provide Looker's rich filter functionality for custom-built data applications and customized embedded Looker dashboards. Using the Looker API (through an [SDK](https://docs.cloud.google.com/looker/docs/embed-sdk) or [Extension](https://docs.cloud.google.com/looker/docs/extension-framework)) to fetch JSON for a given dashboard, developers can include the filter component in their application and pass in the properties of each filter in the dashboard. The component will then render each filter according to its field and stored UI configuration.

The filter components package offers 12 types of filter controls, similar to the controls [available for Looker's own dashboards](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#dashboard_filter_controls):

  * Button group
  * Checkbox
  * Tag list
  * Range slider
  * Button toggle
  * Radio button



  * Drop-down menu
  * Slider
  * Single day
  * Date range
  * Timeframe
  * Advanced



Filter components are delivered through two packages that work together: [`@looker/filter-components`](https://github.com/looker-open-source/components/tree/main/packages/filter-components#readme) and [`@looker/filter-expressions`](https://github.com/looker-open-source/components/tree/main/packages/filter-expressions#readme). The `@looker/filter-components` package renders a filter component by using [a field, a filter type, and current filter expressions](https://github.com/looker-open-source/components/blob/main/packages/filter-components/USAGE.md#filter), which are available from any dashboard filter. The `@looker/filter-expressions` package transforms filter expressions into data structures that can be used by `@looker/filter-components`.

## Why use filter components?

Filter components free up developer time and allow analysts who are working in Looker to build and maintain robust, customizable user experiences. Looker filter components provide the following benefits:

  * **High-quality filter experiences** — Filter components provide Looker's rich filter logic and a wide range of filter controls to best fit the types of filters you need.
  * **Speed development** — Filter components provide "out-of-the-box" access to filters, allowing developers to focus on other tasks and speeding overall development.
  * **Customization** — Filter controls can be customized to the look and feel of your application, extension, or embedded dashboard. Developers can use filter components to provide more customization than ever before.
  * **Linked to Looker dashboards** — A filter component can be connected directly to a filter on a Looker dashboard, and a version of that filter will be rendered in the Looker application, extension, or embed that is using the component. Any user who has edit access to the Looker dashboard that is connected to the filter component can edit the filter on the Looker dashboard, which updates the filter in the application, extension, or embed. This frees up developer time because a developer is not required every time there is a business reason to adjust a filter.
  * **Tied to the Looker model** — Filter components are aware of changes to the Looker model on which they are built, which means filter fields and other options are dynamic and will update along with updates to the underlying model.



## Installing and using filter components

Download the [`@looker/filter-components`](https://www.npmjs.com/package/@looker/filter-components) and [`@looker/filter-expressions`](https://www.npmjs.com/package/@looker/filter-expressions) packages from the `@looker/components` NPM repository.

Information on installing and using the filter components packages can be found in the README document for each package, available in NPM or [GitHub](https://github.com/looker-open-source/components/tree/main/packages/filter-components).

A [filter components demo application](https://github.com/looker-open-source/components/tree/%40looker/components%403.0.8/apps/filter-demo) is available on GitHub. Instructions for using the demo appear in its README document.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
