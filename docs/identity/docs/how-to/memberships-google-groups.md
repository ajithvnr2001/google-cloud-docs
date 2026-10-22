---
url: https://docs.cloud.google.com/identity/docs/how-to/memberships-google-groups/
title: Managing memberships for Google Groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:09.566942+00:00
---

# Managing memberships for Google Groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/memberships-google-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing memberships for Google Groups

After a group exists, you can create memberships for it. This page explains how to perform some fundamental membership operations with the Cloud Identity Groups API. To learn how to create a Google Group, refer to [Creating and searching for Google Groups](https://docs.cloud.google.com/identity/docs/how-to/create-google-groups).

## Before you begin

  * Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

  * Set up authentication and install the client libraries. See [Setting up the Cloud Identity Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup) to learn how.




## Add a membership to a Google Group

###  REST 

Use the `memberships.create` method to add a member to a group.

Before using any of the request data, make the following replacements: 

  * `GROUP_ID`: The numeric ID of the group that you want to add a member to. To find the ID of a single group, use the [`groups.lookup`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) method. To see all group IDs under a customer or namespace, use the [`groups.list`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/list) method. 
  * `MEMBER_ID`: The ID of the member. For Google-managed entities, use the member's email address. For external-identity-mapped entities, use a string that meets the identity source's requirements. 
  * `ROLE_NAME`: The name of the role that you want to grant to the member. Use `OWNER`, `MANAGER`, or `MEMBER`. 
  * `PROJECT_ID`: The alphanumeric ID of the Google Cloud project that you want to use to make the request. 



HTTP method and URL: 
    
    
    POST https://cloudidentity.googleapis.com/v1/groups/GROUP_ID/memberships

Request JSON body: 
    
    
    {
      "preferredMemberKey": {
        "id": "MEMBER_ID"
      },
      "roles": [
        {
          "name": "MEMBER"
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudidentity.googleapis.com/v1/groups/GROUP_ID/memberships"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudidentity.googleapis.com/v1/groups/GROUP_ID/memberships" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains an [`Operation`](https://docs.cloud.google.com/identity/docs/reference/rest/Shared.Types/Operation) indicting the status of your request. 

Finished operations contain the membership that was added. For example: 
    
    
    {
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.apps.cloudidentity.groups.v1.Membership",
        "name": "groups/GROUP_ID/memberships/123456789012345678901",
        "preferredMemberKey": {
          "id": "MEMBER_ID"
        },
        "roles": [
          {
            "name": "MEMBER"
          }
        ]
      }
    }
    

You can also use the `memberships.create` method to add a member as a manager or owner of the group:

  * To make someone a manager of the group, follow the procedure to add a member to the group, but use the following request body:
        
        {
          "preferredMemberKey": {
            "id": "MEMBER_ID"
          },
          "roles": [
            {
              "name": "MEMBER"
            }
            {
              "name": "MANAGER"
            }
          ]
        }

  * To make someone an owner of the group, follow the procedure to add a member to the group, but use the following request body:
        
        {
          "preferredMemberKey": {
            "id": "MEMBER_ID"
          },
          "roles": [
            {
              "name": "MEMBER"
            }
            {
              "name": "OWNER"
            }
          ]
        }




###  Python 

The following code shows you how to add a membership to a group. `expiryDetail` is an optional field that can be added to set an expiration for the membership. The value of `preferredMemberKey` is the member's email address.
    
    
    def create_google_group_membership(service, identity_source_id, group_id, member_key):
      param = "&groupKey.id=" + group_id + "&groupKey.namespace=identitysources/" + identity_source_id
      try:
        lookupGroupNameRequest = service.groups().lookup()
        lookupGroupNameRequest.uri += param
        # Given a group ID and namespace, retrieve the ID for parent group
        lookupGroupNameResponse = lookupGroupNameRequest.execute()
        groupName = lookupGroupNameResponse.get("name")
        # Create a membership object with a memberKey and a single role of type MEMBER
        membership = {
          "preferredMemberKey": {"id": member_key},
          "roles" : {
            "name" : "MEMBER",
            "expiryDetail": {
              "expireTime": "2021-10-02T15:01:23Z"
            }
          }
        }
        # Create a membership using the ID for the parent group and a membership object
        response = service.groups().memberships().create(parent=groupName, body=membership).execute()
        print(response)
      except Exception as e:
        print(e)
    

## List memberships of a Google Group

###  REST 

Use the `memberships.list` method to list the members of a group.

Before using any of the request data, make the following replacements: 

  * `GROUP_ID`: The numeric ID of the group that you want to list members for. To find the ID of a single group, use the [`groups.lookup`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) method. To see all group IDs under a customer or namespace, use the [`groups.list`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/list) method. 
  * `PROJECT_ID`: The alphanumeric ID of the Google Cloud project that you want to use to make the request. 



HTTP method and URL: 
    
    
    GET https://cloudidentity.googleapis.com/v1/groups/GROUP_ID/memberships

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://cloudidentity.googleapis.com/v1/groups/GROUP_ID/memberships"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudidentity.googleapis.com/v1/groups/GROUP_ID/memberships" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The response contains an array of all members in the group and their roles. 

###  Python 

The following code lists the memberships for a group:
    
    
    def list_google_group_memberships(service, group_id):
      param = "&groupKey.id=" + group_id
      try:
        lookup_group_name_request = service.groups().lookup()
        lookup_group_name_request.uri += param
        lookup_group_name_response = lookup_group_name_request.execute()
        group_name = lookup_group_name_response.get("name")
        # List memberships
        response = service.groups().memberships().list(parent=group_name).execute()
        print(response)
      except Exception as e:
        print(e)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
