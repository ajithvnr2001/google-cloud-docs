---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants/
title: required_access_grants (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:28.130006+00:00
---

# required_access_grants (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  required_access_grants (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `required_access_grants` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `required_access_grants` can also be part of an Explore, described on the [`required_access_grants` (for Explores) ](https://docs.cloud.google.com/looker/docs/reference/param-explore-required-access-grants) parameter documentation page.
> 
> `required_access_grants` can also be part of a join, described on the [`required_access_grants` (for joins) ](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants) parameter documentation page.
> 
> `required_access_grants` can also be part of a dimension, dimension group, measure, filter, or parameter, described on the [`required_access_grants` (for fields) ](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) parameter documentation page.

## Usage
    
    
    view: view_name {
      required_access_grants: [access_grant_name, access_grant_name, ...]
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `required_access_grants` |  Default Value None Accepts Square brackets containing a comma-separated list of access grant names  
---|---  
  
## Definition

`required_access_grants` pairs with the model-level [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter to limit access for a view to only those users who have a specific [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) value assigned to them.

`required_access_grants` works like this:

  1. You define an access grant using the [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter. As part of the definition, you associate the access grant with a [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes). You also specify which user attribute values provide access to the access grant.
  2. Next, you use `required_access_grants` to restrict a view to only those users who have access to every access grant listed.



For example, the following LookML requires that users have access to both the `can_view_financial_data` and the `view_payroll` access grants to see the `payroll` view:
    
    
    view: payroll {
      ...
      required_access_grants: [can_view_financial_data, view_payroll]
    }
    

Users who don't have access to _all_ of the access grants assigned to the view will not see any of the fields in the restricted view. They will not see those fields in the field picker while exploring. If the user views a Look that includes fields from the restricted view, they will see a warning message saying, "`<view.field>` no longer exists on `<view>`, or you do not have access to it, and it will be ignored." The warning message is suppressed on dashboard tiles.

For more information on how to define an access grant, see the [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter documentation page.

## Example

Expose the `payroll` dimension to only those users who have access to the `accounting` access grant:
    
    
    view: payroll {
      ...
      required_access_grants: [accounting]
    }
    

## Additional considerations

### Viewing restricted views with calculated fields on saved Looks and dashboards

Since users who do not have access to a restricted view cannot access the fields in the view, this can cause changes in viewed data in a saved Look or dashboard tile.

For example, a measure that uses a dimension from a restricted view will not have access to the data from that view, so the measure aggregation occurs without that data. Thus, users who do not have access to the restricted view sees different results than users who do have access to the restricted view.

[Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) based on a field in a restricted view display an error for users who do not have access to the restricted view, since the table calculation does not have access to the field in the restricted view.

### Restricting access to underlying LookML structures

Restricting access to a view does not restrict access to its underlying LookML structures. So an unrestricted field that is part of other views will still be available if those views are unrestricted. Use the `required_access_grants` parameter at the [field](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) level level to restrict fields individually.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
