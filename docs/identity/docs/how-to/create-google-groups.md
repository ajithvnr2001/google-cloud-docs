---
url: https://docs.cloud.google.com/identity/docs/how-to/create-google-groups/
title: Creating and searching for Google Groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:37.997781+00:00
---

# Creating and searching for Google Groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-google-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating and searching for Google Groups

This page explains how to perform some fundamental operations with the Cloud Identity Groups API.

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * Read the [Groups API overview](https://docs.cloud.google.com/identity/docs/groups).

  * [Set up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).


**Note:** When a method requires the `customer_id`, you must prepend a "C" to the ID that you can view in the Google Admin console (for example, 'C046psxkn').

## Creating a Google Group

###  REST 

To create a Google Group, call [`groups.create()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/create) with an instance of the new group. The group instance must include a `groupKey`, `Parent`, and `label` set to `cloudidentity.googleapis.com/groups.discussion_forum`.

You also need to set the `initialGroupConfig` parameter, which defines the initial owner of the group. You can use the following values for this parameter:

  * `WITH_INITIAL_OWNER`: Makes the person sending the request the owner of the group. You should use this value in most cases.
  * `EMPTY`: Creates a group with no initial owners. You can only use this value if you're a Google Workspace Super Admin or Groups Admin. For more information about Google Workspace roles, see [Pre-built administrator roles](https://support.google.com/a/answer/2405986).



###  Python 

The following example shows a helper function to create a Google Group using the Python client library:
    
    
    def create_google_group(service, customer_id, group_id, group_display_name, group_description):
      group_key = {"id": group_id}
      group = {
        "parent": "customers/" + customer_id,
        "description": group_description,
        "displayName": group_display_name,
        "groupKey": group_key,
        # Set the label to specify creation of a Google Group.
        "labels": {
          "cloudidentity.googleapis.com/groups.discussion_forum": ""
        }
      }
    
      try:
        request = service.groups().create(body=group)
        request.uri += "&initialGroupConfig=WITH_INITIAL_OWNER"
        response = request.execute()
        print(response)
      except Exception as e:
        print(e)
    

## Searching for a Google Group

###  REST 

To search for a Google Group, call [`groups.search()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search) with a query string. To search for all groups, you only need to provide the label `cloudidentity.googleapis.com/groups.discussion_forum`.

###  Python 

The following example shows a helper function used to search for a Google Group using the Python client library:
    
    
    from urllib.parse import urlencode
    
    def search_google_groups(service, customer_id):
      search_query = urlencode({
              "query": "parent=='customerId/{}' && 'cloudidentity.googleapis.com/groups.discussion_forum' in labels".format(customer_id)
      })
      search_group_request = service.groups().search()
      param = "&" + search_query
      search_group_request.uri += param
      response = search_group_request.execute()
    
      return response
    

## What's next

  * After a group exists, you can create memberships for it. To create memberships for a Google Group, refer to [Managing memberships for Google Groups](https://docs.cloud.google.com/identity/docs/how-to/memberships-google-groups).

  * You can [update a Google Group to a security group](https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
