---
url: https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-dynamic-groups/
title: Retrieving a dynamic group and listing members \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:13:15.227655+00:00
---

# Retrieving a dynamic group and listing members  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-dynamic-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Retrieving a dynamic group and listing members

You can retrieve dynamic groups by name or email. After you retrieve a group, you can list its memberships.

**Note:** Dynamic groups are only available to Cloud Identity premium accounts.

## Retrieving a dynamic group by name

The following sample shows how to retrieve a dynamic group by name:

### REST

To retrieve a dynamic group by name, call [`groups.get()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/get) with the resource name of the group.

### Python

The following example shows how to retrieve a dynamic group by name using the python library:
    
    
    def get_dynamic_group_by_name(name):
      service = build_service()
      response = service.groups().get(name=name).execute()
      return response
    

## Retrieving a dynamic group by email

The following sample shows how to retrieve a dynamic group by email:

### REST

To retrieve a dynamic group by email, call [`groups.get()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/get) with the group email address.

### Python

The following example shows how to retrieve a dynamic group by email using the python library:
    
    
    def get_dynamic_group_by_email(email):
      service = build_service()
    
      # First we use the email to get the groups name calling lookup()
      lookup_group_name_request = service.groups().lookup()
      param = "&groupKey.id=" + email
      lookup_group_name_request.uri += param
      lookup_group_name_response = lookup_group_name_request.execute()
      name = lookup_group_name_response.get("name")
    
      # Then we can call get() by passing in the group's name
      response = service.groups().get(name=name).execute()
      return response
    

## Listing memberships of a dynamic group

The following sample shows how to list the memberships of a dynamic group:

### REST

To list memberships of a group, call [`groups.memberships.get()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/get) with the resource name of the group.

### Python

The following example shows how to list memberships of a dynamic group using the python library:
    
    
    def get_dynamic_group_memberships(name):
      service = build_service()
    
      members_request = service.groups().memberships().list(parent=name)
      members_request.uri += "&view=FULL"
      response = members_request.execute()
      return response
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
