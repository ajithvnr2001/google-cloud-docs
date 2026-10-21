---
url: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-settings/
title: Create and edit attributes \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:24:48.322973+00:00
---

# Create and edit attributes  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create and edit attributes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

## Overview

The entities you create in API hub, such as API resources, versions, and deployments, can have system and user-defined attributes associated with them. It's a good practice to start off your API hub journey by setting up and editing key attributes that align with your organizational needs and standards. When you register APIs, create versions, and perform other actions, you can apply attributes and values to build metadata-rich, searchable entities. 

## Before you begin

  1. API hub must be provisioned in a Google Cloud project to which you have access. See [Provision API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision).
  2. In the Google Cloud console, on the project selector page, select the project in which API hub is provisioned.

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)



## Edit system attributes

System attributes are predefined by API hub for each resource type. While the attributes themselves are predefined, you can edit their default values. To learn more, see [System attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes). 

  1. In the Google Cloud console, go to the **Settings** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/settings)
  2. In the **System attributes** section, click the Edit icon in the **Lifecycle** row.
  3. In the **Allowed values** section, click **Add item**.
  4. In the **Value** field, enter a value for the attribute, such as "Production", and add a description in the **Description** field. 
  5. Click **Save**. 



## Create user defined attributes

User defined attributes are name/value pairs defined by you based on your requirements. To learn more, see [User attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#user-attributes). 

  1. In the **User Defined Attributes** section of the **Settings** page, click **Create attribute**.
  2. In the **Add a new attribute** form, edit the Allowed values as follows: Field | Value  
---|---  
Name | Enter a name for the attribute. For example: Latency  
Description |  Enter a brief description of the attribute.  
Maximum allowed values | Specify the number of elements the attribute can hold. An element can have a minimum of one attribute, and a maximum of 20.  
Resource type | Select the type of API hub resource to which the attribute can be associated. Valid choices are: Version, Spec, Operation, Deployment, and Dependency.  
Data type |  Choose the data type for the attribute. Data types include `String`, `Enum`, and `JSON`. If the `Enum` data type is selected, click **\+ Add item** , and enter the allowed values for the attribute. **Notes:**
     * If you select the `Enum` data type, you must enter at least one allowed value.
     * If you select the `JSON` data type, you must enter a valid JSON value for the attribute.  
  3. Click **Create**. 



Add more user-defined attributes before continuing to the next quickstart, if you wish.

## Next step

[Create an Eventarc trigger](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-create-event-triggers)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
