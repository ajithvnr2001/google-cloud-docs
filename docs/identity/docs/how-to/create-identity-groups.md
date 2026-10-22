---
url: https://docs.cloud.google.com/identity/docs/how-to/create-identity-groups/
title: Creating and searching for identity-mapped groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:15.616087+00:00
---

# Creating and searching for identity-mapped groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-identity-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating and searching for identity-mapped groups

This page explains how to create and search for _identity-mapped groups_. An identity-mapped group is a type of group that mirrors a group in an external identity source, such as an Active Directory group. Identity-mapped groups are used when creating an identity connector for Google Cloud Search.

For more information about identity-mapped groups, see [Groups API overview](https://docs.cloud.google.com/identity/docs/groups#group-types).

The following sections demonstrate how to manage identity-mapped groups.

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * [Create the identity source](https://support.google.com/a/answer/9039510) in the Google Admin console.

  * Read the [Groups API overview](https://docs.cloud.google.com/identity/docs/groups).

  * [Set up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).




## Creating an identity-mapped group

###  REST 

To create an identity-mapped group, call [`groups.create()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/create) with an instance of the new group. The group instance must include a `groupKey` , `Parent`, and `label` set to `system/groups/external`. The `groupKey` is a combination of `namespace` and `groupId` that uniquely identifies the group.

###  Python 

The following example shows a helper function to create an identity group using the Python client library. Use the identity source ID, obtained when you created the identity source in the Google Admin console, to call the helper function and create a group:
    
    
    def create_identity_group(service, identity_source_id, group_id, group_display_name,
      group_description):
      namespace = "identitysources/" + identity_source_id
      group_key = {"id": group_id, "namespace": namespace}
      group = {
        "parent": namespace,
        "description": group_description,
        "displayName": group_display_name,
        "groupKey": group_key,
        "labels": {
          # Set the label to specify creation of an identity group.
          "system/groups/external": ""
        }
      }
    
      try:
        response = service.groups().create(body=group).execute()
        print response
      except Exception, e:
        print e
    
      myNewGroup = create_identity_group(
        idSvc,
        "ABC1234",
        "zebra",
        "Zebra external group",
        "The Zebra group is an identity group representing the Zooland
          external identity"
      )
    

Providing the namespace ensures that you won't experience any naming collisions, and places the identity-mapped group in the proper context of other groups from the same external identity source.

### Searching for identity-mapped groups

###  REST 

To search for identity-mapped groups, call [`groups.search()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search) with a query string. To search for all groups, you only need to provide the label `system/groups/external`.

###  Python 

The following example shows a helper function used to search for identity-mapped groups using the Python client library:
    
    
    def search_identity_groups(service, identity_source_id, pageSize, view):
      # Set the label to search for all identity groups
      searchQuery = "&query=namespace=identitysources/" + identity_source_id \
        + "%20AND%20" + "labels:system/groups/external" \
        + "&pageSize=" + pageSize + "&view=" + view
      try:
        searchGroupsRequest = service.groups().search()
        searchGroupsRequest.uri += searchQuery
        response = searchGroupsRequest.execute()
        print response
      except Exception, e:
        print e
    

## What's next

After a group exists, you can create memberships for it. To create memberships for an identity-mapped group, refer to [Managing identity-mapped group memberships](https://docs.cloud.google.com/identity/docs/how-to/memberships-identity-groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
