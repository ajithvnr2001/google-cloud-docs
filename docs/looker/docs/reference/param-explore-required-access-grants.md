---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-required-access-grants/
title: required_access_grants (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.039909+00:00
---

# required_access_grants (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-required-access-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  required_access_grants (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `required_access_grants` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `required_access_grants` can also be part of a join, described on the [`required_access_grants` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants) parameter documentation page.
> 
> `required_access_grants` can also be part of a view, described on the [`required_access_grants` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants) parameter documentation page.
> 
> `required_access_grants` can also be part of a dimension, dimension group, measure, filter, or parameter, described on the [`required_access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      required_access_grants: [access_grant_name, access_grant_name, ...]
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `required_access_grants` |  Default Value None Accepts Square brackets containing a comma-separated list of access grant names  
---|---  
  
## Definition

`required_access_grants` pairs with the model-level [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter to limit access of an Explore to only those users who have a specific [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) value assigned to them.

`required_access_grants` works like this:

  1. You define an access grant using the [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter. As part of the definition, you associate the access grant with a [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes). You also specify which user attribute values provide access to the access grant.
  2. Next, you use `required_access_grants` to restrict an Explore to only those users who have access to every access grant listed.



This LookML requires that users have access to both the `can_view_financial_data` and the `view_payroll` access grants to see the `payroll` Explore:
    
    
    explore: payroll {
      ...
      required_access_grants: [can_view_financial_data, view_payroll]
    }
    

Users who don't have access to _all_ of the access grants that are assigned to the Explore won't see the Explore at all. They are restricted from viewing any Looks or dashboard tiles that are based on the Explore, and they won't see the Explore in the **Explore** menu. For more information on how to define an access grant, see the [`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) parameter documentation page.

## Example

Expose the `financial` Explore to only those users who have access to the `accounting` access grant:
    
    
    explore: financial {
      ...
      required_access_grants: [accounting]
    }
    

## Additional considerations

Restricting access to an Explore does not restrict access to its underlying LookML structures. So an unrestricted join, view, or field that is part of other Explores will still be available if those Explores are unrestricted. Use the `required_access_grants` parameter at the [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants), [view](https://docs.cloud.google.com/looker/docs/reference/param-view-required-access-grants), or [field](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) level to restrict those items individually.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-26 UTC."],[],[]] 
