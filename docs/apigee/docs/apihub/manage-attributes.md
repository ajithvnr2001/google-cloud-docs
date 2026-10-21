---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes/
title: Manage attributes \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:36:05.826400+00:00
---

# Manage attributes  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage attributes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

## Overview

You can think of an attribute as metadata for a resource. For example, in the case of an API resource, the API can have an attribute called `Target Users` that specifies if the API is intended for public, private, or internal consumption. There are many other such attributes available.

Attributes are useful to you in the following ways:

  * You can filter your resource search results based on attributes. Therefore, having more attributes will make it easy for you to narrow down your search results.
  * You can create custom attributes and associate them to API hub resources.



Attributes in API hub can be of two types:

  * System attributes: System attributes are predefined by API hub.
  * User attributes: User attributes, also referred to as _Additional attributes_ , are defined by you based on your requirements.



API hub stores an attribute in the key-value format; where the key is the name of the attribute, and the value is the corresponding value of the attribute. The value of an attribute can be of the following data types:

  * String
  * Enum
  * JSON



## System attributes

System attributes are predefined by API hub for each resource type. These attributes may be mandatory or optional for a resource. If an attribute is mandatory for a resource, you must set the value of the attribute when you register the resource. For the list of supported system attributes, see [Supported system attributes](https://docs.cloud.google.com/apigee/docs/apihub/system-attributes#supported-system-attributes).

The values of `Enum` type system attributes can be immutable or mutable.

  * **Immutable:** You can't make any changes to the existing values. However, you can add new mutable values to the attribute. For example, the **Spec Type** attribute will have the values `OpenAPI`, `Proto`, and `WSDL`. You can't update these values, but you can add new custom values.
  * **Mutable:** You can add, edit, or delete the existing values. For example, the **Lifecycle** attribute can initially have values like `Dev`, `Stage`, `UAT`, or `Prod`. You can edit these existing values, and add new values. 



### Supported system attributes

Apigee API hub supports the following system attributes: 

Attribute | Description | Scope | Mandatory  
---|---|---|---  
**Accreditation** | Indicates the accreditation status of the API version. For example, `ISO 27001`, `PCI DSS 4.0.1`, or `CIS Benchmark 1.1`.  This is a mutable attribute.  | Version | No  
**API Functional Requirements Doc** | Link to the document outlining the functional requirements of the API.  | API | No  
**API Requirements Doc** | Link to the overall requirements document for the API.  | API | No  
**API Style** | Specifies the API design style. The predefined values include: 

  * `REST`
  * `gRPC`
  * `AyncAPI`
  * `SOAP`
  * `GraphQL`
  * `Model Context Protocol (MCP)`

This is an immutable attribute.  | API | No  
**API Technical Requirements Doc** | Link to the document detailing the technical requirements for the API.  | API | No  
**Business Unit** | Identifies the business unit responsible for or using the API. For example, `Finance`, `Supply chain`, or `Customer support`.  This is a mutable attribute.  | API | No  
**Compliance** | Details the compliance standards or regulations applicable to the API version.  This is a mutable attribute.  | Version | No  
**Deployment Type** | Describes the type of deployment environment. The predefined values include: 

  * `Apigee`
  * `Apigee hybrid`
  * `Apigee Edge Private Cloud`
  * `Apigee Edge Public Cloud`
  * `Mock server`
  * `Cloud API Gateway`
  * `Cloud Endpoints`
  * `Unmanaged`
  * `Application Integration`
  * `Others`

This is an immutable attribute.  | Deployment | Yes  
**Environment** | Specifies the environment where the deployment is active. For example, `Dev`, `Staging`, or `Prod`.  This is a mutable attribute.  | Deployment | No  
**Lifecycle** | Indicates the current stage in the API's lifecycle. For example, `Design`, `Deprecated`.  This is a mutable attribute.  | Version | No  
**Management URL** | The URL used to manage the API deployment.  | Deployment | No  
**Maturity Level** | Represents the maturity level of the API.  This is a mutable attribute.  | API | No  
**Plugin Type** | Specifies the type of plugin associated with the API.  This is a mutable attribute.  | API | Yes  
**Service Type** | Specifies the type of service. Use this attribute to classify what a service is, where **API Style** describes how you call it. The predefined values include: 

  * `Code`
  * `Model`
  * `Agent`
  * `Skill`

An API can have only one service type.  This is an immutable attribute.  | API | No  
**SLO** | Defines the Service Level Objectives for the API deployment.  This is a mutable attribute.  | Deployment | No  
**Source URI** | The URI of the source code or definition for the deployment. | Deployment | No  
**Spec Type** | Indicates the specification format. The predefined values include: 

  * `OpenAPI`
  * `Proto`
  * `WSDL`

This is an immutable attribute.  | Specification | Yes  
**Target Users** | Identifies the intended audience for the API.  This is a mutable attribute.  | API | No  
**Team** | The development team responsible for the API. For example, `Front end`, `Back end`, or `Data science`.  This is a mutable attribute.  | API | No  
  
### View system attributes

### Console

To view all the system attributes, in the Google Cloud console, go to the **API hub > Settings** page. You can view all the existing system attributes in the **System attributes** tab.

### REST API

To view all the system attributes of a resource issue a `GET` request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/attributes`

For more information about the API, see [ListAttributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/list).

The following example shows the API call to get the system attributes for all the resources.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-type: application/json" \
    -X GET \
    https://apihub.googleapis.com/v1/projects/test-project-1/locations/us-central1/attributes?filter=definition_type=SYSTEM_DEFINED
    

### Edit a system attribute of type Enum

**Caution:** Avoid adding sensitive data to system attributes.

You can perform the following operations for a mutable value:

  * Add a new value
  * Update an existing value
  * Delete an existing attribute value



The examples in this section show how to update the allowed values of a system attribute of `Enum` type.

**Note:** You can't change the name of a system attribute.

### Console

To add a value for a system attribute, do the following steps:

  1. In the Google Cloud console, go to the **API hub > Settings** page. 

This displays all the existing system attributes in the **System attributes** section of the **Attributes** tab.

  2. Click **Edit** for the attribute to which you want add a value. 

This opens the attribute's edit pane, which displays the existing attribute values.

  3. To add a new value, click **Add item** , and then enter the new value you want to add. **Note:** To delete an existing value, click **Delete** for the value that you want to delete. The `Delete` option is displayed only for the values that are mutable. Therefore, if the delete option isn't displayed for a value, you can infer that the value is immutable.
  4. Click **Save**.



### REST API

To update allowed values of a system defined attribute of `Enum` datatype, issue a PATCH request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/attributes/ATTRIBUTE`

For more information about the API, see [UpdateAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/patch).

The following example shows the API call to update the values of the `Business unit` attribute. 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"allowed_values": [
    {
    "id": "bu1",
    "display_name": "Business unit 1",
    "description": "The API can be used by business unit 1"
    },
    {
    "id": "bu2",
    "display_name": "Business unit 2",
    "description": "The API can be used by business unit 2"
    },
    {
    "id": "bu3",
    "display_name": "Business unit 3",
    "description": "The API can be used by business unit 3"
    }]}' \
    -X PATCH https://apihub.googleapis.com/v1/projects/test-15/locations/us-central1/attributes/system-business-unit?update_mask=allowed_values 
    

It's important to understand how API hub interprets the request payload for the [UpdateAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/patch) API. 

  * If the value you specify in the payload is already present, API hub checks if the value has been updated in the payload, and then overwrites the value if it's updated.
  * If the value isn't available in the payload, API hub interprets that value should be deleted, and deletes the value from API hub.
  * If a new value is available in the payload, API hub adds the new value to the attribute.



### Limitations

The following limitations apply to system attributes:

  * You can't update or change the **API style** attribute to `MCP` while existing API operations are present in the API resource. 

To change the **API style** attribute to `MCP`, you must delete all the existing API operations associated with the API resource. 

  * Specification files are not parsed or validated automatically for API versions with the `MCP` API style.



## User defined attributes

**Key Term:** The terms _user defined attributes_ and _additional attributes_ are used interchangeably in this document. **Additional attributes** is the term used in the Apigee API hub UI. 

User defined attributes are defined by you based on your requirements.

### View user defined attributes

### Console

To view all the user defined attributes, in the Google Cloud console, go to the **API hub > Settings** page. You can view all the user defined attributes in the **Additional attributes** section of the **Attributes** tab.

### REST API

To view all the user defined attributes of a resource issue a `GET` request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/attributes`

For more information about the API, see [ListAttributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/list).

The following example shows the API call to get the user attributes for the API resource.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-type: application/json" \
    -X GET \
    https://apihub.googleapis.com/v1/projects/test-project-1/locations/us-central1/attributes?filter=definition_type=USER_DEFINED
    

### Add a new user defined attribute

**Caution:** Avoid adding sensitive data to user defined attributes.

### Console

To add a new user defined attribute, do the following steps:

  1. In the Google Cloud console, go to the **API hub > Settings** page. 

This displays all the user defined attributes in the **Additional attributes** section of the **Attributes** tab.

  2. Click **Create attribute**. 

This opens the **Add a new attribute** pane.

  3. Enter the following details: 
     * **ID:** Enter an unique identifier for the attribute. 
       * If you leave the field empty, API hub automatically generates an unique ID for you.
       * If you manually want to enter a value, ensure that the value is unique across all the attributes. **Note:** Ensure that the length of the unique ID is less than 500 characters. 
     * **Name:** Enter a name for the attribute.
     * **Description:** Optionally, enter a attribute description.
     * **Maximum allowed values:** Enter a number from 1 through 20. This setting specifies the maximum number of values that the attribute can have.
     * **Resource type:** Select a resource type.
     * **Data type:** Choose the data type for the attribute. Data types include `String`, `Enum`, and `JSON`. If the `Enum` data type is selected, click **\+ Add item** , and enter the allowed values for the attribute. **Notes:**
       * If you select the `Enum` data type, you must enter at least one allowed value.
       * If you select the `JSON` data type, you must enter a valid JSON schema for the attribute.
  4. Click **Create**.



### REST API

To add a new user defined attribute, issue a `POST` request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/attributes?attribute_id=NEW_ATTRIBUTE_NAME`

For more information about the API, see [CreateAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/create).

The following example shows the API call to create the `attribute-01` user defined attribute.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json"  \
    -d '{
    "display_name" : "custom attribute",
    "description" : "custom attribute details",
    "definition_type" : "USER_DEFINED",
    "scope" : "API",
    "data_type" : "ENUM",
    "allowed_values" : [
    {
    "id" : "value-1",
    "display_name" : "Value 1",
    "description" : "Value 1 test description",
    "immutable" : false,
    },
    {
    "id" : "value-2",
    "display_name" : "Value 2",
    "description" : "Value 2 test description",
    "immutable" : false,
    },
    ],
    "cardinality" : 4,
    "mandatory" : false
    }' \
    -X POST  https://apihub.googleapis.com/v1/projects/test-15/locations/us-central1/attributes?attribute_id=attribute-01
    

### Edit a user defined attribute

**Caution:** Avoid adding sensitive data to user defined attributes.

You can perform the following edits on a user defined attribute:

  * Update the attribute name
  * Add new attribute value
  * Delete an existing attribute value



### Console

To edit a user defined attribute, do the following steps:

  1. In the Google Cloud console, go to the **API hub > Settings** page. 

This displays all the existing user defined attributes in the **Additional attributes** section of the **Attributes** tab.

  2. Click **Edit** for the attribute you want to edit. 

This opens the attribute's edit pane, which displays the existing attribute values.

  3. You can edit the name, description, and maximum allowed values. For `Enum` types, you can add new values. To add a new value for an `Enum` type, click **Add item** , and then enter the new value you want to add. 
  4. Click **Save**.



### REST API

To edit a user defined attribute, issue a `PATCH` request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/attributes/ATTRIBUTE`

For more information about the API, see [UpdateAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/patch).

The following example shows the API call update the `API Visibility` user defined attribute.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"name": "projects/test-15/locations/us-central1/attributes/API Visibility",
        display_name" : "API Visibility Updated", "allowedValues": [
        {
        "id": "internal",
        "displayName": "Internal",
        "description": "The API is visible internally in an organization"
        },
        {
        "id": "external",
        "displayName": "External",
        "description": "The API is visible externally in an organization"
        },
        {
        "id": "public",
        "displayName": "Public",
        "description": "The API is visible public in an organization"
        }
        ]}' \
        -X PATCH https://autopush-apihub.sandbox.googleapis.com/v1/projects/common-dev-15/locations/us-central1/attributes/API Visibility?update_mask=display_name,allowed_values
        

It's important to understand how API hub interprets the request payload for the [UpdateAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.attributes/patch) API. 

  * If the value you specify in the payload is already present, API hub checks if the value has been updated in the payload, and then overwrites the value if it's updated.
  * If the value isn't available in the payload, API hub interprets that value should be deleted, and deletes the value from API hub.
  * If a new value is available in the payload, API hub adds the new value to the attribute.



## Filter resources based on attributes

Filtering APIs based on system and user attributes provides greater flexibility and control when searching and managing your APIs. You can quickly locate specific APIs based on criteria relevant to your organization.

### Console

To filter APIs based on attributes, do the following:

  1. In the Google Cloud console, go to the **API hub > APIs** page.
  2. In the **Filter** field, click filter_list**Add filter**.
  3. Select from system attributes under **System Attributes** , or scroll down to the **Additional Attributes** section, and then select the required user defined attributes from the list of attributes.
  4. Click **Apply** to filter the APIs.
**Tip:** Click view_column **(Column display options)** in the table header to choose the attributes to display in the table.


### REST API

To filter APIs based on attributes, issue a `GET` request to the following API: 

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/apis`

You can use system or user-defined attributes in the `filter` query parameter. For more information about the API, see [ListApis](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/list).

The following example shows the API call to filter resources based on a user defined attribute value of `String` data type.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-type: application/json" \
    -X GET \
    https://apihub.googleapis.com/v1/projects/test-project-1/locations/us-central1/apis?filter=attributes.projects/test-project-1/locations/us-central1/attributes/cdcb1260-ed63-4e5b-935d-4394f178da4f.string_values.values:helloworld
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
