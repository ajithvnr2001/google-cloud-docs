---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/move-space-resources/
title: Move API resources in Apigee Spaces \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:18:52.747428+00:00
---

# Move API resources in Apigee Spaces  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/move-space-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Move API resources in Apigee Spaces Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic describes how to move API resources (API proxies, shared flows, and API products) between Apigee Spaces in an Apigee organization. Users can move resources between organization and Space levels or move resources between Spaces. To move, manage, or view the API resources in an organization or Space, the user must have the appropriate permissions for the relevant organization or Space. 

## Move API resources from an organization to a Space

API resources created in an Apigee organization can be moved from the organization level to a Space or the other way around. An API resource moved to a Space inherits the IAM policy of that Space. In order to move the API resource from the organization level to a Space, the user must have the following permissions: 

  * `apigee.RESOURCE_TYPE.move` on the source scope (the organization or Space where the resource currently exists). 

Valid values for RESOURCE_TYPE include `apis`, `sharedflows`, or `apiproducts`, depending upon the type of API resource moved.

  * `apigee.RESOURCE_TYPE.create` on the target scope (the organization or Space where the resource is to be moved). 

Valid values for RESOURCE_TYPE include `apis`, `sharedflows`, or `apiproducts`, depending upon the type of API resource moved.


**Note** : The [IAM](https://docs.cloud.google.com/iam/docs/overview) system traverses upward through the resource hierarchy to see if the permission exists. As a result, a user with the `Apigee Organization Admin` role will always have the required permissions, regardless of any IAM policy that may be set for the Space.

To move an organization-level API resource to a Space, use the following command: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/RESOURCE_TYPE/RESOURCE_ID:move?space=SPACE_NAME" \
      -X POST -H "Authorization: Bearer $TOKEN"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * RESOURCE_TYPE is the type of the resource you are listing. Valid values include: 
    * `apis`
    * `sharedflows`
    * `apiproducts`
  * RESOURCE_ID is the name of the API proxy, shared flow, or API product you want to move.
  * SPACE_NAME is the name of the Space where you are moving the resource.



For example, with the following command, a user with the **Apigee Organization Admin** role for the **acme** organization moves an API proxy named **demo** from the organization level to the **red** Space: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**acme** /**apis** /**demo** :move?space=**red** " \
      -X POST -H "Authorization: Bearer $TOKEN"

The response should look similar to the following: 
    
    
    {
      "metaData": {
        "createdAt": "1739489725993",
        "lastModifiedAt": "1741724822852",
        "subType": "Proxy"
      },
      "name": "demo",
      "revision": [
        "1",
        "2"
      ],
      "apiProxyType": "PROGRAMMABLE",
      "space": "red"
    }

Once the **demo** API proxy is moved to the **red** Space, members of the **red** Space can access the proxy, even if they do not have permission to access organization-level resources. Members of other Spaces, who are not members of the **red** Space, can't view or access the **demo** proxy.

Attempting to access the **demo** proxy without the correct organization- or Space-level permissions results in the following error: 
    
    
      {
        "error": {
          "code": 403,
          "message": "Permission denied on resource \"organizations\/acme\/apis\/demo\" (or it may not exist).",
          "status": "PERMISSION_DENIED"
        }
      }

To move an API resource from a Space to the organization level, use the following command, which omits the `space` query parameter: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/RESOURCE_TYPE/RESOURCE_ID:move" \
      -X POST -H "Authorization: Bearer $TOKEN"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * RESOURCE_TYPE is the type of the resource you are listing. Valid values include: 
    * `apis`
    * `sharedflows`
    * `apiproducts`
  * RESOURCE_ID is the name of the API proxy, shared flow, or API product you want to move.



## Move API resources between Spaces

API resources can be moved between Spaces in an Apigee organization. An API resource moved to a Space inherits the IAM policy of that Space. In order to move the API resource between Spaces in an Apigee organization, the user must have the following permissions: 

  * `apigee.RESOURCE_TYPE.move` for the Space where the API resource currently exists. 

Valid values for RESOURCE_TYPE include `apis`, `sharedflows`, or `apiproducts`, depending upon the type of API resource being moved.

  * `apigee.RESOURCE_TYPE.create` for the Space where the API resource is to be moved. 

Valid values for RESOURCE_TYPE include `apis`, `sharedflows`, or `apiproducts`, depending upon the type of API resource being moved.




A user assigned the `apigee.spaceContentEditor` role for both Spaces will have the required permissions.

To move an API resource between Spaces in an Apigee organization, use the following command: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/RESOURCE_TYPE/RESOURCE_ID:move?space=SPACE_NAME" \
      -X POST -H "Authorization: Bearer $TOKEN"

Where: 

  * ORG_NAME is the name of your Apigee organization.
  * RESOURCE_TYPE is the type of the resource you are listing. Valid values include: 
    * `apis`
    * `sharedflows`
    * `apiproducts`
  * RESOURCE_ID is the name of the API proxy, shared flow, or API product you want to move.
  * SPACE_NAME is the name of the new Space.



For example, a user with the `apigee.proxies.move` permission for the **red** Space and the `apigee.proxies.create` permission for the **blue** Space can use the following command to move the **demo** API proxy from the **red** Space to the **blue** Space: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**acme** /**apis** /**demo** :move?space=**blue** " \
      -X POST -H "Authorization: Bearer $TOKEN"

The response should look similar to the following: 
    
    
    {
      "basepaths": ["/demo"],
      "revision": 1,
      "apiProxyId": "**demo** ",
      "space_id": "**blue** ",
      "createTime": ...,
      "updateTime": ...
    }

In this example, the user does not need to have permissions at the organization level, only the required permissions set by each Space's `setIamPolicy` bindings. 

Attempting to move the **demo** API proxy without the correct permissions for both Spaces results in the following error: 
    
    
      {
        "error": {
          "code": 403,
          "message": "Permission denied on resource \"organizations\/acme\/apis\/demo\" (or it may not exist).",
          "status": "PERMISSION_DENIED"
        }
      }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
