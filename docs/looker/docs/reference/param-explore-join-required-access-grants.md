---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants/
title: required_access_grants (for joins) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:25.555884+00:00
---

# required_access_grants (for joins)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  required_access_grants (for joins) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `required_access_grants` parameter that is part of a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join).
> 
> `required_access_grants` can also be part of an Explore, described on the [`required_access_grants` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-required-access-grants) parameter documentation page.
> 
> `required_access_grants` can also be part of a view, described on the [`required_access_grants` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants) parameter documentation page.
> 
> `required_access_grants` can also be part of a dimension, dimension group, measure, filter, or parameter, described on the [`required_access_grants`](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      join: view_name {
        required_access_grants: [access_grant_name, access_grant_name, ...]
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `required_access_grants` |  Default Value None Accepts Square brackets containing a comma-separated list of access grant names  
---|---  
  
## Definition

`required_access_grants` pairs with the model-level [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter to limit access of a join to only those users who have been assigned a specific [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) value.

`required_access_grants` works like this:

  1. You define an access grant using the [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter. As part of the definition, you associate the access grant with a [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes). You also specify which user attribute values provide access to the access grant.
  2. Next, you use `required_access_grants` to restrict a join to only users who have access to every access grant listed.



This LookML requires that users have access to both the `can_view_financial_data` and the `view_payroll` access grants to see the `payroll` join:
    
    
    join: payroll {
      ...
      required_access_grants: [can_view_financial_data, view_payroll]
    }
    

Users who don't have access to _all_ of the access grants assigned to the join will not see any of the fields added to an Explore through the restricted join. They will not see those fields in the field picker while exploring. If users view a Look that includes fields they don't have access to, they see a warning message saying, "`<view.field>` no longer exists on `<view>`, or you do not have access to it, and it will be ignored." The warning message is suppressed on dashboard tiles.

For more information on how to define an access grant, see the [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter documentation page.

## Example

Expose the `payroll` join to only those users who have access to the `pr_dept` access grant:
    
    
    explore: financial {
      join: payroll {
        ...
        required_access_grants: [pr_dept]
      }
    }
    

## Additional considerations

### Viewing restricted joins with calculated fields on saved Looks and dashboards

Since users who do not have access to a restricted join cannot see the fields added by the join, this can change the data they see in a saved Look or dashboard tile.

For example, a measure that uses a dimension from a restricted join will not have access to the data for that dimension, so the measure aggregation occurs without that data. Thus, users who do not have access to the restricted join will see different data for the measure than users who do have access to the restricted join.

[Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) based on a field in a restricted join display an error for users who do not have access to the restricted join, since the table calculation does not have access to the field in the restricted join.

### Restricting access to underlying LookML structures

Restricting access to a join does not restrict access to its underlying LookML structures. An unrestricted view or field that is part of other joins will still be available if those joins are unrestricted. Use the `required_access_grants` parameter at the [view](https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants) or [field](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) level to restrict those items individually.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
