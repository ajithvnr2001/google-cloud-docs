---
url: https://docs.cloud.google.com/identity/docs/how-to/create-posix-groups/
title: Creating and deleting POSIX groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:21.722986+00:00
---

# Creating and deleting POSIX groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-posix-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating and deleting POSIX groups

**Caution:** POSIX groups are [deprecated](https://docs.cloud.google.com/identity/docs/deprecations). As of September 26, 2024, you can no longer create new POSIX groups. For more information, see [POSIX groups deprecation](https://docs.cloud.google.com/identity/docs/deprecations/posix-groups).

This document explains how to create and delete a POSIX group.

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** You must use the beta version of the Cloud Identity Groups API to create and delete POSIX groups.

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/setup) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * Read the [Groups API overview](https://docs.cloud.google.com/identity/docs/groups).

  * [Set up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).




## Creating a POSIX group

You can create a POSIX group from an existing Google group, or by creating a new Google group and adding POSIX information.

### Creating a POSIX group from an existing Google group

The following examples show how to create a POSIX group from an existing Google group:

###  gcloud 

Use the [`gcloud beta identity groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/update) to update an existing Google group to a POSIX group:
    
    
    gcloud beta identity groups update EMAIL \
       --add-posix-group=gid=GROUP_ID,name=POSIX_NAME
    

Replace the following:

  * `EMAIL`: the email address of the group to update
  * `GROUP_ID`: the group ID (GID) you want to assign to the POSIX group
  * `POSIX_NAME`: the name you want to assign to the POSIX group



###  REST 

To update a Google Group to a POSIX group, call the [`groups.patch()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/patch) with the POSIX groups field specified.
    
    
    PATCH 'https://cloudidentity.googleapis.com/v1beta1/groups/GROUP_RESOURCE_NAME?updateMask=posix_group
    
    {
      "posixGroups": [
        {
          "name": "POSIX_NAME",
          "gid": GROUP_ID
        }
      ]
    }
    

Replace the following:

  * `GROUP_RESOURCE_NAME`: the resource name of the Google group. To find a group's resource name, run the [`gcloud identity groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/describe)
  * `POSIX_NAME`: the name you want to assign to the POSIX group
  * `GROUP_ID`: the group ID (GID) you want to assign to the POSIX group



###  Python 

The following example shows a helper function to update a Google Group to a POSIX group using the Python client library:
    
    
    def add_posix_group_data_to_group(service, group_name, posix_name, posix_gid):
      group = {
        "posix_groups": [
              {
                  "name": posix_name,
                  "gid": posix_gid,
              }
          ]
      }
      try:
        request = service.groups().patch(name=group_name, body=group)
        request.uri = request.uri + '&updateMask=posix_groups'
        response = request.execute()
        print(response)
      except Exception as e:
        print(e)
    

### Creating a POSIX group from a new Google group

The following examples show how to create a POSIX group from a new Google group:

###  gcloud 

Use the [`gcloud beta identity groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/create) to create a POSIX group:
    
    
    gcloud beta identity groups create EMAIL \
      --organization=ORGANIZATION_ID \
      --labels=cloudidentity.googleapis.com/groups.discussion_forum \
      --posix-group=gid=GROUP_ID,name=POSIX_NAME
    

Replace the following:

  * `EMAIL`: the email address of the group to be created
  * `ORGANIZATION_ID`: the organization the group belongs to. Either an ID ("123456789") or the associated domain ("example.com").
  * `GROUP_ID`: the group ID (GID) you set for the group
  * `POSIX_NAME`: the name you set for the group



### REST

To create a group, call the [`groups.create()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/create) with the email address, organization ID, POSIX groups, and labels for the new group.
    
    
    POST 'https://cloudidentity.googleapis.com/v1beta1/groups?initialGroupConfig=WITH_INITIAL_OWNER
    
    {
    "parent": "customers/CUSTOMER_ID",
    "groupKey": {"id": "EMAIL"},
    "labels": {"cloudidentity.googleapis.com/groups.discussion_forum": ""},
    "posixGroups": [
      {
        "name": "POSIX_NAME",
         "gid": GROUP_ID,
      }
    ]
    }
    

Replace the following:

  * `initialGroupConfig=WITH_INITIAL_OWNER`: Either `?initialGroupConfig=WITH_INITIAL_OWNER` or empty. Any empty group can only be created by organization admins.
  * `CUSTOMER_ID`: the customer ID for your organization. To find the customer ID run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list)
  * `EMAIL`: the email address of the group to be created
  * `POSIX_NAME`: the name you want to assign to the POSIX group
  * `GROUP_ID`: the group ID (GID) you want to assign to the POSIX group



### Python

The following example shows a helper function to create a POSIX group using the Python client library:
    
    
    def create_posix_group(customer_id, email, query, posix_name, posix_gid):
      service = build_service()
      groupDef = {
          "parent": "customerId/{}".format(customer_id),
          "groupKey": {"id": email},
          "labels": {"cloudidentity.googleapis.com/groups.discussion_forum": ""},
          "posixGroups": [
              {
                  "name": posix_name,
                  "gid": posix_gid,
              }
          ]
      }
      request = service.groups().create(body=groupDef)
      request.uri += "&initialGroupConfig=WITH_INITIAL_OWNER"
      response = request.execute()
      return response
    

## Deleting a POSIX group

The following examples show how to remove POSIX information from a Google group.

**Note:** When you remove POSIX information from a Google group, the Google group isn't deleted.

###  gcloud 

Use the [`gcloud beta identity groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/update) and specify the `--remove-posix-groups` flag with the `GROUP_ID` or `POSIX_NAME` value:
    
    
    gcloud beta identity groups update \
       EMAIL \
       --remove-posix-groups=GROUP_ID_or_POSIX_NAME
    

Replace the following:

  * `EMAIL`: the email address of the group to be deleted
  * `GROUP_ID_or_POSIX_NAME`: the group ID or POSIX group name of the group to be deleted



###  REST 

To update a Google Group to a POSIX group, call the [`groups.patch()` method](https://docs.cloud.google.com/identity/docs/reference/rest/tt1/groups/patch) with the POSIX groups field specified.
    
    
    PATCH 'https://cloudidentity.googleapis.com/v1beta1/groups/GROUP_RESOURCE_NAME?updateMask=posix_group
    
    {
      "posixGroups": []
    }
    

Replace the following:

  * `GROUP_RESOURCE_NAME`: the resource name of the Google group. To find a group's resource name, run the [`gcloud identity groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/describe)



###  Python 

The following example shows a helper function to update a Google Group to a POSIX group using the Python client library:
    
    
    def remove_posix_data_from_group(service, group_name, posix_name, posix_gid):
      group = {
        "posix_groups": []
      }
      try:
        request = service.groups().patch(name=group_name, body=group)
        request.uri = request.uri + '&updateMask=posix_groups'
        response = request.execute()
        print(response)
      except Exception as e:
        print(e)
    

## What's next

After the POSIX group exists, you can retrieve it and list its memberships. For more information, see [Retrieving and listing POSIX groups](https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-posix-groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
