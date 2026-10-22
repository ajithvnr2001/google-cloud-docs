---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/liquid-troubleshooting/
title: Troubleshooting Liquid errors \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:39.677083+00:00
---

# Troubleshooting Liquid errors  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/liquid-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting Liquid errors Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you troubleshoot Liquid errors in your LookML.

## Debugging tree

Use the following decision tree to troubleshoot common Liquid issues:

The following sections describe the scenarios in the tree in further detail.

## Error: Variable not found

### Check that the field is accessible in the Explore

This error can appear if you're referencing a field that isn't accessible in the Explore.

First, check for typos in your field name. Then, check to make sure that the view that the field is defined in is joined into the Explore.

## Error: Liquid parse exception

This error can appear while validating LookML in the IDE, or while running a query. The following sections describe common causes for this error.

### Close any single or double quotes

Check for any single quotes or double quotes that are opened but not closed. For example, the following code would throw an error:
    
    
    {% if value == "Shirt %}
      This is a shirt.
    {% endif %}
    

To resolve the error, close the quotes.
    
    
    {% if value == "Shirt" %}
      This is a shirt.
    {% endif %}
    

### Use double == for comparison

Don't use a single = when checking if a value is equal to another value. The following code would throw an error:
    
    
    {% if value = "Shirt" %}
      This is a shirt.
    {% endif %}
    

To resolve the error, use two == instead.
    
    
    {% if value == "Shirt" %}
      This is a shirt.
    {% endif %}
    

### Use the correct tag syntax

Don't use output syntax around an `if` statement, or tag syntax around a single value. The following code would throw an error:
    
    
    {{ if value == "Shirt" }}
      This is a {% value %}.
    {{ endif }}
    

Instead output syntax to insert individual values, and use tag syntax to perform logical comparisons and operations.
    
    
    {% if value == "Shirt" %}
      This is a {{ value }}.
    {% endif %}
    

### Don't nest Liquid tags

Don't use Liquid tags inside other Liquid tags. For example, the following code would throw an error:
    
    
    {% if value > {{ view_name.field_name._value }} %}
      This value is larger.
    {% endif %}
    

To resolve the error, remove the nested tags:
    
    
    {% if value > view_name.field_name._value %}
      This value is larger.
    {% endif %}
    

## Liquid is showing the incorrect value

For these cases, the LookML will usually validate without any errors, but you will see unexpected results when running a query on an Explore.

### Capitalize yesno values

If you're using Liquid to check the value of a `yesno` field, check for uncapitalized values. The following code wouldn't match any results for the `yes` condition:
    
    
    {% if value == "yes" %}
      This is a shirt or shoes.
    {% endif %};;
    

Instead, capitalize the "Yes" and "No" values.
    
    
    {% if value == "Yes" %}
      This is a shirt or shoes.
    {% endif %};;
    

### Check if the Liquid parameter is supported

If you reference a Liquid parameter in a LookML parameter that doesn't support that Liquid parameter, Looker will ignore the Liquid parameter.

For example, the following code would return nothing, since the `parameter parameter_name` syntax isn't supported for the `html` LookML parameter.
    
    
    html: {% parameter parameter_name %};;
    

Check the [Liquid variable reference](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#liquid_variable_definitions) to see which Liquid parameters are supported in which LookML parameters. For this example, you could rewrite the code as follows:
    
    
    html: {{ parameter_name._parameter_value }};;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
