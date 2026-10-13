---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden/
title: hidden (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:22.281293+00:00
---

# hidden (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  hidden (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `hidden` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `hidden` can also be used as part of a field, described on the [`hidden` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      hidden: yes
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `hidden` |  Default Value `no` Accepts A Boolean (`yes` or `no`)  
---|---  
  
## Definition

`hidden` lets you hide an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) from the Explore menu. By default, `hidden` is off and the Explore will be displayed.

## Examples

Hide the **Order** Explore from the Explore menu:
    
    
    explore: order {
      hidden: yes
    }
    

## Common challenges

### `hidden` does not hide LookML or prevent Explore access via the URL

Depending upon permissions, some business users are able to see LookML. Even if an Explore is hidden from the Explore menu, such business users can see its existence in the LookML.

A business user could also gain access to the Explore if they were savvy enough to manually modify the URL.

For these reasons, `hidden` is not meant as a security feature, but rather as a presentation feature.

## Things to know

### `hidden` is useful for dashboard-only Explores

The most common use case for `hidden` is to create Explores that are only used to populate specific dashboard tiles, but are uninteresting for exploration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
