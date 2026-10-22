---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/manage-space-resources/
title: Manage API resources with Apigee Spaces \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:54.610992+00:00
---

# Manage API resources with Apigee Spaces  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/manage-space-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage API resources with Apigee Spaces Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic describes how to create and manage API resources in a Space. You can create API proxies, shared flows, and API products in a Space. Resources created in the Space inherit the same permissions as the Space.

Creating resources in a Space is the same as creating resources under an Apigee organization, except that you can select a Space when you create the resource. You can create API resources from the command line using the Apigee APIs, or by using the Apigee UI.

This guide outlines the steps required to: 

  * Create API proxies in a Space
  * Create shared flows in a Space
  * Create API products in a Space
  * List all API resources in a space



For an overview of Apigee Spaces, see [Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

For more information about the Apigee API resource types, see: 

  * [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy)
  * [Creating reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows)
  * [Introduction to API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product)



## Before you begin

Before you begin creating API resources in Apigee Spaces, make sure you complete the following tasks: 

  * Provision your Apigee Subscription or Pay-as-you-go organization. For more information on the steps required to provision Apigee, see [Set up Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/setup).
  * Create a Space in your Apigee organization. For more information, see [ Create Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces). **Note** : You must create at least one Space in your Apigee organization before you can create API resources assigned to a Space using the Apigee UI. Once a Space is created, you can select a Space when creating new resources and view an assigned Space when listing resources in the Apigee UI.
  * Assign members to a Space. For more information, see [ Manage members and roles in a Space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces#members-roles).



## Required roles and permissions

With the introduction of Apigee Spaces, the way that IAM checks the permissions required to perform some operations on API resources has changed. If the API resource exists in a Space, IAM will check for the appropriate permissions at the Space level, for the Space member performing the operation. For more information, see [ Apigee Spaces roles and permissions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/spaces-roles-permissions) and [ IAM permission hierarchy for Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/iam-permission-hierarchy-spaces).

### Assigning roles and permissions to Space members

There are three custom roles available for Space members: 

  * `apigee.spaceContentEditor`: Provides full access to resources that can be associated with a Space.
  * `apigee.spaceContentViewer`: Provides read-only access to resources that can be associated with a Space.
  * `apigee.spaceConsoleUser`: Provides the minimum permissions required to manage resources in a Space using the Google Cloud console. This role should be granted at the Google Cloud project level to users with access to resources in that Space.



The custom roles described in this section _do not_ give Space members the ability to deploy or undeploy API proxies or shared flows. If you want to allow a Space member to manage deployments, set an IAM policy at the Apigee environment or Google Cloud project level granting the `apigee.environment.admin` role to the Space member.

You can assign roles to a Space member using the Apigee UI or the API.

### Apigee console

To assign roles using the console:

  * **For Space permissions** : Grant the **Content Editor** role in the Apigee UI. For detailed steps, see [Add an organization member to a Space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces#add-member).
  * **For environment deployments** : Grant the `apigee.environment.admin` role at the environment or project level on the IAM page in the Google Cloud console. For instructions on granting IAM project roles, see [View and assign roles using IAM in the console](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/spaces-roles-permissions#view-space-roles).



### Apigee API

To assign roles using the API:

  * **For Space permissions** : Add the `apigee.spaceContentEditor` role to the space using the `setIamPolicy` API. For details, see [Add an organization member to a space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces#add-member-api).
  * **For environment deployments** : Add the `apigee.environmentAdmin` role to the target environment. For details, see the [environments/setIamPolicy method](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/setIamPolicy).



#### To check for the roles at the Google Cloud project level:

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### To grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. In the **Select a role** list, select a role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



To check for the IAM policies applied at the Space level, see [ Manage members and roles in a Space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces#members-roles).

## Manage API proxies in a Space

Apigee organization members assigned to a Space can create API proxies as Space resources. Members assigned only to other Spaces will not be able to access or manage these proxies. 

Create an API proxy as a Space resource using the Apigee UI or the API, as described in the following sections.

### Apigee console

**Note** : You must create at least one Space in your Apigee organization before you can create API resources assigned to a Space using the Apigee console. Once a Space is created, you can select a Space when creating new resources and view an assigned Space when listing resources in the Apigee console.

To create an API proxy as a Space resource using the Apigee console: 

  1. Follow the steps outlined in [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy#apigee-in-cloud-console).
  2. In **Step 5** , you will see an additional field under **Proxy details** where you can select a **Space** for the API proxy. Select a Space from the list box. If you do not wish to assign the API proxy to a space, you can skip this field.
  3. Click **Next** to proceed to the optional deployment step of proxy creation or click **Create** to create the proxy without deploying it.



### Apigee API

To create an API proxy as a Space resource using the Apigee APIs, use the following command: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/apis?name=PROXY_NAME&space=SPACE_NAME&action=import" \
        -X POST -H "Authorization: Bearer $TOKEN" \
        -H "Content-type: multipart/form-data" \
        -F "file=@PROXY_BUNDLE"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * PROXY_NAME is the name of the API proxy you are creating. The name must be globally unique and not just unique within the Space.
  * SPACE_NAME is the name of the Space where you are creating the API proxy.
  * PROXY_BUNDLE is the name of the API proxy bundle file.



For example, with the following command, a **red** team member creates an API proxy named **proxy-1** as a **red** Space resource in the **acme** organization using the **proxy-bundle.zip** file: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**acme** /apis?name=**proxy-1** &space=**red** &action=import" \
        -X POST -H "Authorization: Bearer $TOKEN" \
        -H "Content-type: multipart/form-data \
        -F "file=@**proxy -bundle.zip"**

The following example shows the response to the command: 
    
    
    {
      "basepaths": ["/proxy-1"],
      "revision": 1,
      "apiProxyId": "proxy-1",
      "resourceName": "organizations/**acme** /apis/proxy-1/revisions/1",
      "space": "**red** ",
      "createTime": ...,
      "updateTime": ...
    }

## Manage shared flows as Space resources

Members assigned to a Space can also create shared flows as Space resources. Members of other Spaces will not be able to access or manage these shared flows.

Create a shared flow as a Space resource using the Apigee UI or the API, as described in the following sections.

### Apigee console

To create a shared flow as a Space resource using the Apigee console: 

  1. follow the steps outlined in [Creating a shared flow in the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows#creating-a-shared-flow) to create a new shared flow from scratch or upload an existing flow bundle.
  2. In **Step 4** , you will see an additional field in the **Create a shared flow** dialog where you can select a **Space** for the API proxy. Select a Space from the list box. If you do not wish to assign the API proxy to a space, you can skip this field.
  3. Click **Create** to create the shared flow.



### Apigee API

To create a shared flow as a Space resource using the Apigee APIs, use the following command: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/sharedflows?name=FLOW_NAME&space=SPACE_NAME&action=import" \
        -X POST -H "Authorization: Bearer $TOKEN" \
        -H "Content-type: multipart/form-data" \
        -F "file=@SHARED_FLOW_BUNDLE"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * FLOW_NAME is the name of the shared flow you are creating. The name must be globally unique and not just unique within the Space.
  * SPACE_NAME is the name of the Space where you are creating the shared flow.
  * SHARED_FLOW_BUNDLE is the name of the shared flow bundle file.



For example, with the following command, a **red** team member creates a shared flow named **flow-1** associated with the **red** Space in the **acme** organization: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**acme** /sharedflows?name=**flow-1** &space=**red** &action=import" \
        -X POST -H "Authorization: Bearer $TOKEN" \
        -H "Content-type: multipart/form-data" \
        -F "file=@**sharedflow-bundle.zip** "

The following example shows the response to the command: 
    
    
    {
      "name": "organizations/**acme** /sharedflows/flow-1",
      "revision": 1,
      "sharedFlowId": "flow-1",
      "space": "**red** ",
      "createTime": ...,
      "updateTime": ...
    }

## Manage an API product as a Space resource

Members assigned to a Space can create an API product to bundle their API proxies. When creating API products, Space members can select any API proxies accessible to them, including proxies created directly under the organization and API proxies created as resources in Spaces where they have membership. Members of other Spaces will not be able to access or manage these API products.

Create an API product as a Space resource using the Apigee UI or the API, as described in the following sections.

### Apigee console

To create an API product as a Space resource using the Apigee console: 

  1. Follow the steps in [Creating an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add).
  2. In **Step 4** , you will see an additional field in the **Product details** page where you can select a **Space** for the API product. Select a Space from the list box. If you do not wish to assign the API product to a space, you can skip this field.
  3. Complete the remaining configuration information, then click **Save**.



### Apigee API

To create an API product as a Space resource using the API, send a request to the [`apiproducts/create`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/create) endpoint and add the `space` property.

For example, the following command would create an API product named **product-1** in the `acme` organization and associated with the **red** Space: 
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/**acme** /apiproducts" \
        -H "Authorization: Bearer $TOKEN" \
        -H "Content-type: application/json" -d \
          `{
            "name": "**product-1** ",
            "displayName": "product-1",
            "approvalType": "auto",
            "attributes": [
              {
                "name": "access",
                "value": "internal"
              }
            ],
            "environments": [
              "test"
            ],
            "operationGroup": {
              "operationConfigs": [
                {
                  "apiSource": "proxy-1",
                  "operations": [
                    {
                      "resource": "/",
                      "methods": [
                        "GET"
                      ]
                    }
                  ]
                }
              ],
              "operationConfigType": "proxy"
            },
            "space": "**red** "
          }'

The following example shows the response to the command: 
    
    
    {
      "name": "**product-1** ",
      "displayName": "product-1",
      "approvalType": "auto",
        "attributes": [
          {
            "name": "access",
            "value": "internal"
          }
        ],
        "environments": [
        "test"
      ],
      "createdAt": "1741977778448",
      "lastModifiedAt": "1741977778448",
      "operationGroup": {
        "operationConfigs": [
          {
            "apiSource": "proxy-1",
            "operations": [
              {
                "resource": "/",
                "methods": [
                  "GET"
                ]
              }
            ]
          }
        ],
        "operationConfigType": "proxy"
      },
      "space": "**red** "
    }

## Change or unassign a Space on an existing resource

You can change the Space assigned to an existing API proxy, shared flow, or API product, or unassign the Space entirely.

### Apigee console

**To change the Space on an API proxy or shared flow:**

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to **API Proxies** or **Shared Flows**.
  2. Click the resource you want to edit.
  3. On the **Overview** tab, click **Edit** by **Proxy Details** or **Sharedflow details**.
  4. In the side panel, select a different Space from the **Space** dropdown, or select **No space assigned** to unassign it.
  5. Click **Save**.



**To change the Space on an API product:**

  1. In the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), go to **API Products** and click the product you want to edit.
  2. Click **Edit**.
  3. In the basic details section, select a different Space from the **Space** dropdown, or select **No space assigned**.
  4. Click **Save**.



### Apigee API

To move an API resource between Spaces or unassign it using the API, see [Move API resources in Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/move-space-resources).

## List all API resources associated with a space

For all list operations, including `ListApiProxies`, `ListSharedFlows`, and `ListApiProducts`, you can specify a Space name to list all the resources associated with that Space. If you do not specify a Space name, the list operation will return all resources in the organization that you have permission to access, whether or not those resources are associated with a Space.

It is important to note that, when using the Apigee Spaces feature, the results of `list` operations for API resources assigned to a Space will be limited to results for the Spaces the principal can access. For example, if `acme-team@acme.com` is given the `apigee.spaceContentEditor` role for the **red** Space, team `acme-team` members using the `list` operation will only see API proxies that are associated with the **red** space and not _all_ API #proxies in the organization.

To perform this task, you must have the `apigee.apiResources.list` permission. This permission is included in the `Apigee > Apigee Organization Admin` role.

### List API resources associated with a specific Space

List all API resources associated with a specific Space in the Apigee UI, or using the API, as described in the following sections.

### Apigee console

To list all API resources associated with a specific Space in the Apigee console, open the overview page for the relevant resource type (API proxies, shared flows, or API products). In the **Filter** box, select the **Space** option from the list, then enter the name of the Space. The list of resources assigned to that space displays. Note that only resources associated with a Space where the user is a member are displayed.

### Apigee API

To list all API resources associated with a specified Space, use the following command: 
    
    
    curl -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/organizations/ORG_NAME/RESOURCE_TYPE?space=SPACE_NAME"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * RESOURCE_TYPE is the type of the resource you are listing. Valid values include: 
    * `apis`
    * `sharedFlows`
    * `apiProducts`
  * SPACE_NAME is the name of the Space where you are listing the resource.



For example, with the following command, a **red** team member lists all API proxies associated with the **red** Space in the **acme** organization: 
    
    
    curl -H  "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/organizations/**acme** /apis?space=**red** "

The following example shows the response to the command: 
    
    
    {
      "proxies": [
        {
          "basepaths": "/proxy-1",
          "revision": "1",
          "apiProxyId": "proxy-1",
          "resourceName": "organizations/**acme** /apis/proxy-1/revisions/1",
          "space": "**red** ",
          "createTime": ...,
          ....
        }
      ]
    }

### List API resources without specifying a Space

List all API resources without specifying a Space in the Apigee UI, or using the API, as described in the following sections.

### Apigee console

To view a list of all API resources of a given type in the Apigee console, regardless of Space association, open the overview page for the relevant resource type (API proxies, shared flows, or API products). A list of all available resources displays. Note that only resources that the user has permission to view are displayed. This includes resources associated with a Space or Spaces where the user is a member, or resources not associated with a Space. 

### Apigee API

You can also list API resources without specifying a Space using the following command: 
    
    
    curl -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/organizations/ORG_NAME/RESOURCE_TYPE"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * RESOURCE_TYPE is the type of the resource you are listing. Valid values include: 
    * `apis`
    * `sharedFlows`
    * `apiProducts`



For example, a user with `Organization Admin` access to all organization resources can use the following command to list all API proxies in the **acme** organization: 
    
    
    curl -H  "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/organizations/**acme** /apis"

If the **acme** organization has three proxies, the command will return details about all three proxies. For example: 
    
    
    {
      "proxies": [
        {
          "basepaths": "/proxy-1",
          "revision": "1",
          "apiProxyId": "proxy-1",
          "resourceName": "organizations/**acme** /apis/proxy-1/revisions/1",
          "space": "**red** ",
          "createTime": ...,
          ....
        },
        {
          "basepaths": "/proxy-2",
          "revision": "1",
          "apiProxyId": "proxy-2",
          "resourceName": "organizations/**acme** /apis/proxy-2/revisions/1",
          "space": "**blue** ",
          "createTime": ...,
          ....
        },
        {
          "basepaths": "/proxy-3",
          "revision": "1",
          "apiProxyId": "proxy-3",
          "resourceName": "organizations/**acme** /apis/proxy-3/revisions/1",
          "space": "**green** ",
          "createTime": ...,
          ....
        }
      ]
    }

If another user with only `apiAdmin` access to resources in space **red** uses the same command, the command will only return details about **proxy-1**. The response would look like this: 
    
    
    {
      "proxies": [
        {
          "basepaths": "/proxy-1",
          "revision": "1",
          "apiProxyId": "proxy-1",
          "resourceName": "organizations/**acme** /apis/proxy-1/revisions/1",
          "space": "**red** ",
          "createTime": ...,
          ....
        }
      ]
    }

## What's next

  * Learn more about [Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).
  * Learn how to [Create and manage Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces).
  * Review [Identity and Access Management (IAM) documentation](https://docs.cloud.google.com/iam/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
