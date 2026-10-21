---
url: https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook/
title: Looker cookbook: Maximizing code reusability with DRY LookML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:34.073422+00:00
---

# Looker cookbook: Maximizing code reusability with DRY LookML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Looker cookbook: Maximizing code reusability with DRY LookML Stay organized with collections  Save and categorize content based on your preferences. 

This cookbook contains a series of use cases (referred to in the Looker cookbooks as "recipes") for applying DRY (don't repeat yourself) principles to your LookML development, which can help you in the following areas:

  * Reduce duplicated code: Make your projects more manageable and less error-prone by writing DRY LookML code that is easier to understand, modify, and maintain.
  * Create reusable values and logic: Define values that can be used throughout your projects so that you only have to update them in one place if there is a change.
  * Simplify complex logic: Break code down into smaller, reusable parts.
  * Improve the organization and readability of your models and projects: Make code easier for other LookML developers to read, understand, and modify LookML.



Whether you are new to LookML or an experienced LookML developer, this cookbook provides you with recipes and techniques that will help you write clean and effective code now that will save you time and effort in the future.

## Recipes and applications

All the examples in this cookbook are written for LookML developers and require [permissions to develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets).

**Recipe name** |  **Applications**  
---|---  
[Defining LookML fields in a single location](https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-1) |  Define LookML fields once with `${TABLE}.name` and use substitution operators (`${view_name.field_name}`) to refer to them in other parts of your code.   
[Defining sets in a single location](https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-2) |  Create sets to contain any number of dimensions, measures, or filter fields from the current view or from other views. Reuse sets of common fields for drilling into data and for including or omitting fields from Explores.   
[Defining reusable measures for complex calculations](https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-3) |  Create intermediate fields to reuse calculations in multiple measures to make complex calculations more readable and easier to maintain.   
[Defining a string once to use throughout your LookML project](https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-4) |  Define and maintain reusable string values such as names, numbers, or formatting strings in one place by defining LookML constants. Use the `@{constant_name}` syntax to reference the constant throughout your LookML project.   
[Customizing a single base view for multiple use cases](https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-5) |  LookML refinements allow you to make changes to existing views and Explores without having to edit the original LookML code. You can use refinements to tailor a single view for multiple use cases, such as to meet the needs of multiple teams. This recipe requires more advanced knowledge of LookML.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
