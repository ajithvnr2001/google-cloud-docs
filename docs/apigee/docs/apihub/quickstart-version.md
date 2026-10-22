---
url: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-version/
title: Create an API version \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:09.847335+00:00
---

# Create an API version  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create an API version Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page shows you how to add a version to an API resource. 

## Before you begin

Before you do the steps in this quickstart, you need to do the steps in [Register an API](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api). 

## Add a version

You can think of a version as the state of an API at a point in time. Fundamentally, versions help you group and organize your APIs based on underlying sets of operations, deployments, and other attributes.To learn more, see [Versions overview](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro).

To add a version to your API resource:

  1. In the **APIs** page in API hub, locate and select the API resource you created in the previous quickstart to view its details page.
  2. In the **API details** page, under the **Versions** section, click **Add Version** to display the _Add a new version_ form. 

In the form:

     1. Enter a name. You can use any name you wish. The name will appear in the user interface. Name is a required field. 
     2. Optionally, add a description and make other selections such as Lifecycle, Compliance, and Accreditation if you wish. Note that values for these system attribute settings can be customized in [Settings](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes). The **Documentation** field lets you supply a link to external documentation for the version.
     3. Skip the remaining attributes, and click **Create**.

**Note:** You can also add deployments and API specifications to a version. For details, see [Introduction to deployments](https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro) and [Introduction to API specifications](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro).

You have created and linked a version to an API resource. 

## View version details

After you create a version, you can view its details.

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Versions are linked to API resources, so find the API resource you'd like to inspect. If you don't see it, type the name of the API in the **Filter**.
  3. Click the API name to view its details.
  4. In the **Versions** section, locate and select the version you wish to inspect.
  5. The version details page appears. To edit the version's attributes, click **Edit version**.



## Next step

[Create and edit attributes](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
