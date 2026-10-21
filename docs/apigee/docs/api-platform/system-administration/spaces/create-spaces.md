---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces/
title: Create and manage Apigee Spaces \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:08:38.672941+00:00
---

# Create and manage Apigee Spaces  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create and manage Apigee Spaces Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to create Apigee Spaces in your Apigee organization to manage [Identity and Access Management](https://docs.cloud.google.com/iam/docs) (IAM) policies for Apigee API resources at scale.

This guide outlines the steps required to: 

  * Create a Space
  * Manage members and roles in a Space
  * List all spaces in an organization
  * Get Space details
  * Update a Space
  * Delete a Space



For more on the benefits of using Apigee Spaces to manage your API resources, see [Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

## Before you begin

Before getting started with Spaces: 

  * **Provision Apigee**. Confirm that the Apigee Subscription or Pay-as-you-go organization you want to use is provisioned. For more information on the steps required to provision Apigee, see [Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro).
  * **Get your authentication credentials**. Before running commands to create and manage Spaces on the command line, get your `gcloud` authentication credentials using the following command: 
        
        export TOKEN=$(gcloud auth print-access-token)




## Required roles and permissions

Make sure that you have the following role or roles on the project: **Apigee > Apigee Organization Admin**

#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



## Create a Space

To perform this task, you need the `apigee.spaces.create` permission. This permission is included in the `Apigee Organization Admin` role.

Create a Space in your Apigee organization using the Apigee console or the API, as described in the following sections.

### Apigee console

To create a Space using the Apigee UI:

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to the **Spaces** page.   
[Go to Spaces](https://console.cloud.google.com/apigee/spaces)
  2. Click **Create**. The **Add Space Details** panel opens.
  3. In the **Name** field, enter a unique identifier for the Space. The name must be fewer than 63 characters long, start with a lowercase letter, and contain only lowercase characters. For full naming requirements, see [AIP-122: Resource names](https://google.aip.dev/122).
  4. (Optional) In the **Display Name** field, enter a human-readable label for the Space.
  5. Click **Add**.



After creation, organization members will see the Space as an available parameter when creating API resources.

### Apigee API

To create a Space in your Apigee organization, use the following command:
    
    
    curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
        "https://apigee.googleapis.com/v1/organizations/ORG_NAME/spaces" \
        --data-raw '{
           "name":"SPACE_NAME",
           "displayName":"DISPLAY_NAME"
        }'

Where:

  * ORG_NAME is the name of your Apigee organization.
  * SPACE_NAME is the name and unique identifier of the Space. The name must be fewer than 63 characters long, start with a lowercase letter, and contain only lowercase characters. For full naming requirements, see [AIP-122: Resource names](https://google.aip.dev/122).
  * DISPLAY_NAME is the human-readable name of the Space as it appears in the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee).



## Manage members and roles in a Space

After you create a Space, you can add team members to the Space and assign the IAM roles required to create and manage API resources.

### Add an organization member to a Space

To perform this task, you need the `apigee.spaces.setIamPolicy` permission.

**Note:** The IAM role `apigee.spaceContentEditor` contains many of the permissions required to manage Space resources. We recommend that you grant this role, at a minimum, to Space users. However, you may need to grant additional roles to users to perform specific tasks. For more information, see [IAM permission hierarchy in Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/iam-permission-hierarchy-spaces).

### Apigee console

To grant a member access to a Space using the Apigee UI:

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to the **Spaces** page.
  2. Click the name of the Space you want to manage.
  3. In the **Access details** section, click **Grant access**.
  4. In the **Add members** field, enter the email addresses of the users or groups you want to add.
  5. Under **Assign role** , select either **Content Editor** or **Content Viewer**.
  6. Click **Add**.

**Note:** If you have the `resourcemanager.projects.setIamPolicy` permission, the system automatically grants each new member the **Apigee Space Console User** role at the project level, allowing them to access the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee). If you do not have this permission, you will see a warning, and a project administrator must manually grant this role to the users.

### Apigee API

To add an organization member to a Space and assign an IAM role, use the following command:
    
    
    curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-type: application/json" \
        "https://apigee.googleapis.com/v1/organizations/ORG_NAME/spaces/SPACE_NAME:setIamPolicy" -d \
          '{
            "policy":{
              "bindings":[
                {
                  "members": ["user:USER_EMAIL"],
                  "role": "roles/IAM_ROLE"
                }
              ]
            }
          }'

Where:

  * ORG_NAME is the name of your Apigee organization.
  * SPACE_NAME is the name of the Space.
  * USER_EMAIL is the email address of the user you are adding to the Space. To add a Google Group instead of a single user, change the prefix from `user:` to `group:` and provide the group's email address.
  * IAM_ROLE is the name of the IAM role you are assigning to the member.



### Remove members from a Space

To perform this task, you need the `apigee.spaces.setIamPolicy` permission.

### Apigee console

To remove a member from a Space using the Apigee UI:

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to the **Spaces** page and click the name of the Space.
  2. In the **Access details** table, select the checkbox next to one or more members you want to remove.
  3. Click **Remove access**.
  4. In the confirmation dialog, click **Confirm**.



### Apigee API

To remove members from a Space, set a new IAM policy for the space with the revised list of members using the `setIamPolicy` method. Using this method creates a new IAM policy that replaces the existing policy.

For example, to update the members of the **blue** team Space, you can first check the current IAM policy using the following command:
    
    
    curl -X GET -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/acme/spaces/blue:getIamPolicy"

The output of the command returns the current IAM policy for the space, and should look something like this:
    
    
    {
      "version": "0",
      "bindings": [
        {
          "role": "roles/apigee.spaceContentEditor",
          "members": [
            "group:blue-team@acme.com",
            "user:user-a@acme.com",
            "user:user-b@acme.com",
            "user:user-c@acme.com"
          ]
        }
      ]
    }

To remove **user-b@acme.com** from the Space, use the following command:
    
    
    curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-type: application/json" \
      "https://apigee.googleapis.com/v1/organizations/acme/spaces/blue:setIamPolicy" -d \
        '{
          "policy":{
            "bindings":[
              {
                "members": [
                  "group:blue-team@acme.com",
                  "user:user-a@acme.com",
                  "user:user-c@acme.com"
                ],
                "role": "roles/apigee.spaceContentEditor"
              }
            ]
          }
        }'

The new IAM policy for the Space will no longer include **user-b@acme.com**.

To remove a member from a group included in a Space, first remove the member from the group and then rerun the `setIamPolicy` command to update the IAM policy for the Space with the correct membership for the group email alias.

## List all Spaces in an organization

To perform this task, you need the `apigee.spaces.list` permission.

### Apigee console

To view all Spaces, go to the **Spaces** page in the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee).

[Go to Spaces](https://console.cloud.google.com/apigee/spaces)

The Spaces table lists all Spaces in your organization, including their **Name** , **Display Name** , and total number of **Members**.

### Apigee API

To list all the Spaces in an Apigee organization, use the following command:
    
    
    curl -X GET -H "Authorization: Bearer $TOKEN" \
        "https://apigee.googleapis.com/v1/organizations/ORG_NAME/spaces"

Where:

  * ORG_NAME is the name of your Apigee organization.



## Get Space details

To perform this task, you need the `apigee.spaces.get` permission.

### Apigee console

To view Space details in the Apigee UI:

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to the **Spaces** page.
  2. Click the name of the Space you want to view. The details page displays the **Name** , **Display Name** , access details, and the **Members** list.



### Apigee API

To get the details of a Space, use the following command:
    
    
    curl -X GET -H "Authorization: Bearer $TOKEN" \
        "https://apigee.googleapis.com/v1/organizations/ORG_NAME/spaces/SPACE_NAME"

Where:

  * ORG_NAME is the name of your Apigee organization.
  * SPACE_NAME is the name of the Space.



## Update a Space

To perform this task, you need the `apigee.spaces.update` permission.

You can modify the **Display Name** of an existing Space. The unique Name cannot be changed after creation.

### Apigee console

To update a Space in the Apigee UI:

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to the **Spaces** page and click the name of the Space you want to update.
  2. Click the **edit** button (pencil icon) next to the "Space details" heading.
  3. Modify the **Display Name** as needed.
  4. Click **Save**.



### Apigee API

To update a Space using the API, use the following command:
    
    
    curl -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
        "https://apigee.googleapis.com/v1/organizations/ORG_NAME/spaces/SPACE_NAME" \
          --data-raw '{
            "displayName":"DISPLAY_NAME"
          }'

Where:

  * ORG_NAME is the name of your Apigee organization.
  * SPACE_NAME is the name of the Space.
  * DISPLAY_NAME is the new display name for the Space.



## Delete a Space

To perform this task, you need the `apigee.spaces.delete` permission.

### Apigee console

**Warning:** Deleting a Space immediately removes Space members' access to API Proxies, Shared flows, and API Products owned by the Space. This action cannot be undone.

To delete a Space using the Apigee UI:

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to the **Spaces** page.
  2. Click **Delete** in the row of the Space you want to delete.
  3. In the confirmation dialog, type the exact name of the Space to confirm.
  4. Click **Delete**.

**Note:** If the Space still contains active resources, the deletion will fail. Delete or move all resources in the Space before attempting to delete it.

### Apigee API

Before deleting a Space using the API, make sure that all the resources in the Space have been deleted or moved.
    
    
    curl -X DELETE -H "Authorization: Bearer $TOKEN" \
        "https://apigee.googleapis.com/v1/organizations/ORG_NAME/spaces/SPACE_NAME"

Where:

  * ORG_NAME is the name of your Apigee organization.
  * SPACE_NAME is the name of the Space.



If you attempt to delete a Space that still contains active resources, the deletion will fail with a response similar to the following:
    
    
    {
      "error": {
        "code": 400,
        "message": "Space \"red\" has resources associated with it. Please delete the resources before deleting the space.",
        "status": "FAILED_PRECONDITION"
      }
    }

To resolve this error, delete or move all resources in the Space before attempting to delete it.

## What's next

  * Learn more about [Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).
  * Learn to [Manage API resources with Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/manage-space-resources).
  * Review Identity and Access Management (IAM) [documentation](https://docs.cloud.google.com/iam/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
