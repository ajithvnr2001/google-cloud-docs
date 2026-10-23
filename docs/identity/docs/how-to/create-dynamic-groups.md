---
url: https://docs.cloud.google.com/identity/docs/how-to/create-dynamic-groups/
title: Creating and updating a dynamic group \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:43.489759+00:00
---

# Creating and updating a dynamic group  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-dynamic-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating and updating a dynamic group

This page explains how to create and update a dynamic group.

**Note:** Dynamic groups are only available to Google Workspace Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity premium accounts. You can create up to 500 dynamic groups per customer. This limit can be increased on a case-by-case basis—contact [Google Workspace Support](https://support.google.com/a/answer/1047213) with your specific use case to request an increase.wss

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * Read the [Groups API overview](https://docs.cloud.google.com/identity/docs/groups).

  * Read the [dynamic groups overview](https://docs.cloud.google.com/identity/docs/concepts/overview-dynamic-groups).

  * [Set up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).

  * (Optional) [Formulate and test a membership query](https://docs.cloud.google.com/identity/docs/how-to/test-query-dynamic-groups).




## Creating a dynamic group

The following is an example of creating a dynamic group:

### REST

To create a dynamic group, call [`groups.create()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/create) with an instance of the group. The instance of the group must contain the `dynamicGroupMetadata` with the query used to populate the group.

### Python

To create a dynamic group, call the `service.groups().create` method with an instance of the group. The instance of the group must contain the `dynamicGroupMetadata` with the query used to populate the group. The following sample shows how to create a dynamic group containing all users existing in the Engineering department:
    
    
    def create_dynamic_group(customer_id, email, query):
      service = build_service()
      groupDef = {
          "parent": "customerId/{}".format(customer_id),
          "groupKey": {"id": email},
          "labels": {"cloudidentity.googleapis.com/groups.discussion_forum": ""},
          "dynamicGroupMetadata": {
              "queries": [
                  {
                      "resourceType": "USER",
                      "query": "user.organizations.exists(org, org.department=='engineering')"
                  }
              ]
          }
      }
      request = service.groups().create(body=groupDef)
      request.uri += "&initialGroupConfig=EMPTY"
      response = request.execute()
      return response
    

## Updating a dynamic group

The following is an example of updating a dynamic group:

### REST

To update a dynamic group, call [`groups.patch()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/patch) with an instance of the group. The instance of the group must contain the `dynamicGroupMetadata` with the new query used to populate the group.

### Python

To update a dynamic group, call the `service.groups().patch` method with the name of the group to update and an instance of the group. The instance of the group must contain the `dynamicGroupMetadata` with the query used to populate the group. The following sample shows how to update a dynamic group containing all users in Engineering to a group containing all users in either Engineering or Finance departments:
    
    
    # name (i.e. groups/01234abcdeef) uniquely identifies the group
    def update_dynamic_group(name, query):
      service = build_service()
      groupDef = {
        "dynamicGroupMetadata": {
        "queries": [
            {
              "resourceType": "USER",
              "query": "user.organizations.exists(org, org.department=='engineering' || org.department=='finance')"
            }
          ]
        }
      }
      request = service.groups().patch(name=name, body=groupDef)
      request.uri += "&updateMask=dynamicGroupMetadata"
      response = request.execute()
    
      return response
    

## What's next

After the dynamic group exists, you can retrieve it and list its memberships. For more information, refer to [Retrieving a dynamic group and listing members](https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-dynamic-groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
