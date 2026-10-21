---
url: https://docs.cloud.google.com/looker/docs/color-collections/
title: Color collections \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:28.192829+00:00
---

# Color collections  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/color-collections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Color collections Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

A color collection is a set of coordinating palettes that work well together. Looker contains 16 built-in color collections, which let users create themed visualizations and dashboards.

Each collection contains categorical, sequential, and diverging palette types. When you create a new visualization and select a color collection, Looker defaults to the palette type that works best for that type of visualization. However, you can change to a different palette in the collection or make edits to the palette you're using.

Looker admins can [set a default color collection](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#setting_a_default_color_collection) for all visualizations. Admins can also [create custom color collections](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#creating_a_custom_color_collection).

## Color collection IDs

Color collection IDs and palette IDs can be used in LookML dashboards to apply colors to various parts of visualizations. Collection IDs and palette IDs for any new custom color collections are based on each collection's name. This lets LookML dashboards that use those collections render consistently across instances if both instances have the same custom collections named identically.

For example, a custom color collection with the name Company Custom Colors would have the following IDs:

  * **collection ID** : `company-custom-colors`
  * **categorical palette ID** : `company-custom-colors-categorical-0`
  * **sequential palette ID** : `company-custom-colors-sequential-0`
  * **diverging palette ID** : `company-custom-colors-diverging-0`



Because IDs are based on collection names, no two collections on a single instance can have the same name. Additionally, the collection ID and palette IDs don't change if a color collection's name is changed.

Looker's built-in color collections receive instance-specific alphanumeric IDs.

## Looker's color collection palettes

Each color collection contains categorical, sequential, and diverging palettes.

  * Categorical palettes are useful for illustrating the differences between series when the data isn't inherently ordered.
  * Sequential palettes are useful for visualizing ordered or numeric data that spans from low to high values.
  * Diverging palettes are useful for displaying data that has a meaningful or neutral central value, such as zero, with positive and negative values on either side.



The Modern and Dalton color collections accommodate various forms of color vision deficiency.

![](https://docs.cloud.google.com/static/looker/docs/images/all-collections-2612.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
