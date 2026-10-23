---
url: https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges/
title: Creating a perimeter bridge \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:50.459793+00:00
---

# Creating a perimeter bridge  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Creating a perimeter bridge Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create service perimeter bridges.

## Before you begin

  * Read [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)
  * Read [Service Perimeter Configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#stages)
  * Read [Sharing across perimeters with bridges](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters)



## Create a perimeter bridge

###  Console 

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization.

  3. On the **VPC Service Controls** page, click **New perimeter**.

  4. On the **Create a service perimeter** page, in the **Title** field, enter a name for the perimeter.

You can search for a perimeter only using its name, so we recommend using a unique name for the perimeter. You can't search for a perimeter using its ID.

  5. Optional: In the **Description** field, enter a description for the perimeter.

  6. For **Perimeter type** , select **Bridge**.

  7. For **Enforcement mode** , select a perimeter enforcement mode. The available options are **Dry run** and **Enforced**.

For more information about the dry run and enforced modes, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  8. Click **Continue**.

  9. Select the projects that you want to secure within the perimeter:

     1. Click **Add projects**.

     2. In the **Add projects** pane, in each row corresponding to a project that you want to add to the perimeter, select the checkbox.

     3. Click **Add selected projects**.

  10. Click **Create**.




###  gcloud 

To create a perimeter bridge, use the following command:
    
    
    gcloud access-context-manager perimeters create BRIDGE_NAME \
      --title="BRIDGE_TITLE" --perimeter-type=bridge \
      --resources=PROJECTS \
      --policy=POLICY_NAME
    

Where:

  * BRIDGE_NAME is the name of the perimeter bridge you are creating.

  * BRIDGE_TITLE is the title of the bridge.

  * PROJECTS is a comma-delimited list of one or more project IDs. For example: `projects/100712` or `projects/100712,projects/233130`. Only numeric IDs are supported. You cannot use the project name.

  * POLICY_NAME is the numeric name of your organization's access policy. For example, `330193482019`.




###  API 

To create a perimeter bridge, call [`accessPolicies.servicePerimeters.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/create).
    
    
    POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NAME/servicePerimeters
    

Where:

  * POLICY_NAME is the numeric name of your organization's access policy. For example, `330193482019`.



### Request body

The request body must include a [`ServicePerimeter`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter) resource that defines the perimeter bridge.

For the `ServicePerimeter` resource, specify `PERIMETER_TYPE_BRIDGE` for `perimeterType`.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `POST` operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
