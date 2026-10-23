---
url: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-4/
title: Maximizing code reusability with DRY LookML: Defining a string once to use throughout your LookML project \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:57.768976+00:00
---

# Maximizing code reusability with DRY LookML: Defining a string once to use throughout your LookML project  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Maximizing code reusability with DRY LookML: Defining a string once to use throughout your LookML project Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Looker cookbook: Maximizing code reusability with DRY LookML](https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook).

You can use the LookML `constant` parameter within your project's manifest file to define a string that can be used throughout your project. LookML constants can be useful when you need to define a specific string — such as a number, a name, or HTML formatting for field values — and reuse that value throughout your project.

This page includes the following examples of using LookML constants to define and maintain reusable strings values in once place:

  * Using the same string in the labels of multiple Explores: This technique helps you save time if you reuse common strings, such as words, phrases, or location names in your definitions.
  * Applying the same formatting to negative values for multiple fields: This technique helps you save time by defining conditional formatting specifications to use on multiple fields.



## Ingredients

  * Your project's [manifest file](https://docs.cloud.google.com/looker/docs/lookml-project-files#project_manifest_files)
  * The LookML [`constant`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant) parameter
  * `@{constant_name}` syntax to reference existing constants
  * The LookML [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) parameter
  * [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference)



## Prerequisites

  * [A configured LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models)
  * [Permissions to develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets)



## Example: Using the same string in the labels of multiple Explores

Suppose you want to create two Explores, labeled **San Francisco Users** and **San Francisco Orders** in the UI, but you don't want to manually type the text for each label.

![](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-constant-example-1-2304.png)

To do this, you can define a constant `place_name` with the value `"San Francisco"` in the [project manifest file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files) for your project:
    
    
    constant: place_name {
      value: "San Francisco"
    }
    
    

This constant can then be referenced in any part of your project where a string is accepted, using the syntax `@{place_name}`. In this example, you can define the `users` and `orders` Explores, specifying `"@{place_name} Users"` and `"@{place_name} Orders"` as values for the [`label` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-label), as in the following example:
    
    
    explore: users {
      label: "@{place_name} Users"
    }
    
    explore: orders {
      label: "@{place_name} Orders"
    }
    
    

In this example, Looker displays **San Francisco Users** and **San Francisco Orders** in the Explore menu and in the titles of the Explores, rather than the default **Users** and **Orders** labels.

Suppose you want to update all the references to **San Francisco** to **Bay Area**.

![](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-constant-example-2-2304.png)

Rather than having to update each reference manually, you only have to make a single update to the `place_name` constant in the manifest file for your project:
    
    
    constant: place_name {
      value: "Bay Area"
    }
    
    

Since you defined the `place_name` constant, you don't have to manually change **San Francisco** to **Bay Area** in multiple places. The references to **San Francisco** with the `place_name` constant will be replaced with **Bay Area** , so Looker will display **Bay Area Users** and **Bay Area Orders** in the Explore menu and in the titles of the Explores.

## Example: Applying the same formatting to negative values for multiple fields

Imagine that you want negative data values to be displayed in red and within parentheses wherever they appear in charts or queries.

![](https://docs.cloud.google.com/static/looker/docs/images/lookml-constant-html-formatting-2100.png)

By setting this formatting as the value for a LookML constant, you can specify the formatting just once by using [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) and [HTML](https://docs.cloud.google.com/looker/docs/reference/param-field-html). Then, you can reference the constant whenever you want to apply that formatting to a field.

For example, you can create a constant called `negative_format` that you can use to apply this formatting to a field:
    
    
    constant: negative_format {
      value: "{% if value < 0 %}
                <p style='color:red;'>({{rendered_value}})</p>
              {% else %}
                {{rendered_value}}
              {% endif %}"
    }
    
    

This code creates the constant `negative_format`, which specifies that negative data values should have a red font and be surrounded by parentheses. You can then apply this formatting to dimensions and measures in your dataset by using the [`html` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-html).

For example, you can create **Total Amount** measure of [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) and specify `@{negative_format}` as the value for the `html` parameter:
    
    
    measure: total_amount {
      type: sum
      value_format_name: usd
      sql: ${amount} ;;
      html: @{negative_format} ;;
    }
    
    

In your table, negative values for the **Total Amount** measure will be formatted as specified in the `negative_format` constant definition, with a red font and surrounded by parentheses.

If you want to apply the same formatting to negative values for other fields, you can reference the `negative_format` constant in the `html` parameter for those fields.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
