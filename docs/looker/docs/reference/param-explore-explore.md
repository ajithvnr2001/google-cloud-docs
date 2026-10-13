---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-explore/
title: explore \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.793108+00:00
---

# explore  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  explore Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `explore` parameter that is part of a [model](https://docs.cloud.google.com/looker/docs/reference/param-model).
> 
> `explore` can also be used as part of a dashboard filter, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#explore-for-filters) documentation page.
> 
> `explore` can also be used as part of a dashboard element. A representative example of its usage is provided on the [Column chart parameters for LookML dashboards](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-column-chart#explore) documentation page.

## Usage
    
    
    explore: explore_name { . . . }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `explore` |  Default Value None Accepts The name of an existing view, or a name for the `explore` when using [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) Special Rules `explore` names must be unique within a given model   
---|---  
  
## Definition

> If there is a plus sign (`+`) in front of the Explore name, such as `explore: +orders`, that is a _refinement_ of an Explore. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information.

`explore` adds an existing [view](https://docs.cloud.google.com/looker/docs/reference/param-view) to the Looker menu of Explores as described on the [LookML terms and concepts](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) documentation page. As a best practice, an Explore should be defined inside of a [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files).

Explores are typically named after an existing [view](https://docs.cloud.google.com/looker/docs/reference/param-view). However, if you want to have multiple Explores based on the same view, you can add a [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter to the Explore. In that case, the Explore can be given any [valid name](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#scoping_and_naming), which includes only lowercase and uppercase letters (a-z, A-Z), digits (0-9), and underscores.

`explore` plays an important role in the SQL that Looker generates. Suppose a user chooses **Customers** from the Explore menu and runs a query. This `customers` Explore is based on the view called `customers`, which is associated with a database table. That table is placed in the `FROM` clause of the user's SQL query.

`explore` can have [many child parameters](https://docs.cloud.google.com/looker/docs/reference/param-explore) that affect the display and filter behavior and that specify adding joins for the Explore. If an Explore includes one or more joins, then those joins can have [join parameters](https://docs.cloud.google.com/looker/docs/reference/param-join) that specify the preferred join behavior.

## Examples

Add an option to the Explore menu based on the view called `users`:
    
    
    explore: users {
      # additional explore parameters go here
    }
    

Add an option to the Explore menu called **Events** based on the view called `user_events`:
    
    
    explore: events {
      from: user_events
    }
    

## Common challenges

### `explore` needs to reference an existing view name

You cannot use the `explore` parameter to define the database table, dimensions, measures, and other fields that are part of a view. Instead, you first need to define a view using the [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view) parameter. Then you can reference the name of that view in `explore`.

### `explore` needs to reference the view name, not its filename

Typically, the name of a view is the same as the view file where the view is defined. This is not required — the view name and view filename can be different.

For example, you have a view called `users` defined inside of a file called `company_users`. The view file `company_users` looks like this:
    
    
    view: users { ... }
    

You then add the `users` view to the Explore menu with:
    
    
    explore: users { ... }
    

Even though the `users` view is inside of a file called `company_users`, the name of the file does not matter. Only the name of the view in the [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view) parameter matters.

> When you use a [measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) of `type: count` in an Explore, the visualization labels the resulting values with the view name rather than the word "Count." To avoid confusion, we recommend pluralizing your view name, selecting **Show Full Field Name** under **Series** in the visualization settings, or using a `view_label` with a pluralized version of your view name.

## Things to know

### `explore` is usually used with additional parameters

It's possible to use `explore` by itself, without additional parameters. In practice, you typically see `explore` used with additional options. For example, it's very common to [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) additional views into an Explore.

All of the additional parameters that are associated with `explore` are shown on the [Explore parameters](https://docs.cloud.google.com/looker/docs/reference/param-explore) page. The parameters that can be used for a `join` within an Explore are shown on the [Join parameters](https://docs.cloud.google.com/looker/docs/reference/param-join) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
