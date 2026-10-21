---
url: https://docs.cloud.google.com/identity/docs/how-to/test-query-dynamic-groups/
title: Formulating and testing a membership query \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:12:28.307661+00:00
---

# Formulating and testing a membership query  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/test-query-dynamic-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Formulating and testing a membership query

This document explains how to formulate and test your membership queries to ensure the correct users are returned.

## Before you begin

Perform the following tasks before proceeding with the information on this page:

  * Read the [Groups API overview](https://docs.cloud.google.com/identity/docs/overview).

  * Read the [dynamic groups overview](https://docs.cloud.google.com/identity/docs/concepts/overview-dynamic-groups).

  * [Set up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).




## Formulating and testing your query

Membership queries take the form of _`target_field condition`_ , and are formatted as [Common Expression Language](https://opensource.google/projects/cel) (CEL) expressions. See [Valid user attributes for dynamic groups](https://docs.cloud.google.com/identity/docs/how-to/dynamic-groups-attributes) for the list of `User` resource fields that can be used.

### Sample queries

The following example shows how to check for a specific value in a `user.addresses` field using the `exists()` CEL function:
    
    
    user.addresses.exists(ad, ad.locality=='Sunnyvale')
    

The `exists()` macro is used to create membership queries for fields of type list.

Here is an example of checking multiple values, (building) `area` and `building_id`, in a single list entry:
    
    
    user.locations.exists(loc, loc.area=='Sunnyvale' && loc.building_id=='Building 1')
    

The following example shows how to find users who are part of a given organizational unit:

  * **All direct users under a given org unit:** `user.org_unit_id==orgUnitId('03ph8a2z1enx4lx')`
  * **All direct and indirect users under a given org unit:** `user.org_units.exists(org_unit, org_unit.org_unit_id==orgUnitId('03ph8a2z1khexns'))`

**Note:** You can make a query case-insensitive by adding `equalsIgnoreCase()` to the value being queried. For example, a query on username would be written as:
    
    
    user.name.value.equalsIgnoreCase('jOhn DoE')`
    

### Negation in queries

You can use a NOT `!` operator in membership queries to exclude users with certain attributes. Here are some examples:

  * All users who do not belong to a given organizational unit:
        
        !(user.org_unit_id==orgUnitId('03ph8a2z1enx4lx'))
        

  * All users who do not belong to the `Marketing` organization:
        
        !user.organization.exists(org, org.title = "Marketing")
        




Some combinations of the NOT `!` operator and the `exists()` macro are not supported:

  * Any NOT `!` query using the `exists()` macro and using the AND `&&` operator within it:
        
        !user.organization.exists(org, (org.title == "Cloud" && org.department == "Sales"))
        

  * Any query using the `exists()` macro with the NOT `!` operator inside it:
        
        user.organization.exists(org, (org.title == "Cloud" || !(org.department == "Sales")))
        




## Testing membership queries

To test your membership queries, you can use the [simple query builder](https://admin.google.com/ac/dgpreview). It allows you to use drop-down menus and text fields to enter and test a query. After you are sure the membership query returns the correct results, you can create the corresponding CEL queries with the Groups API.

### Custom user attributes

**Note:** Custom attribute support is currently in beta. The query will fail if the `schemaName` or `fieldName` in the query contains a hyphen (-).

[Custom user attributes](https://developers.google.com/admin-sdk/directory/v1/guides/manage-schemas) can used in dynamic group queries as long as the custom schema already exists in `user.custom_schemas`, but they are not supported in the simple query builder drop-downs. To test a query for a custom user attribute, enter it in CEL query format directly into the **Enter cel query** text box. A sample custom schema looks like this:
    
    
    {
      "schemaName": "employmentData",
      "fields": [
        {
          "fieldName": "EmployeeNumber",
          "fieldType": "STRING",
          "multiValued": "false"
        },
        {
          "fieldName": "JobFamily",
          "fieldType": "STRING",
          "multiValued": "true"
        }
      ]
    }
    

**Single valued field**

`user.custom_schemas.employmentData.EmployeeNumber == 'value'`

**Multi-valued field**

`user.custom_schemas.employmentData.JobFamily.exists(fld, fld == 'value')`

## What's next

After you test your membership query, you can use it when creating a group. For more information, refer to [Creating a dynamic group](https://docs.cloud.google.com/identity/docs/how-to/create-dynamic-groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
