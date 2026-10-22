---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-versions/
title: Manage versions \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:15.361540+00:00
---

# Manage versions  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage versions Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This topic explains how to create and manage API versions. To learn about versions, see [Versions overview](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro). 

## Add a version to an API

You can add an [API version](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro) to an existing API in the console or with the REST API.

### Console

To add a new version:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API you wish to version. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Click the **Versions** tab and select the version you wish to add from the **Select a version** drop-down list.
  6. Click **Add version**.
  7. Specify version details in the **Add a new version** form. You must provide a display name. The other attributes are optional. For more information on attributes, see [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes). 
     * **Version ID** : Click **Specify Unique ID** to optionally provide a unique ID for the version. If you omit the ID, API hub creates one for you. **Note:** Version ID must be 4-500 characters long and can contain only uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and hyphens (-). The ID forms the last part of the API resource name: `projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID`. The full resource name is limited to 700 characters.
     * **Name:** (Required) You must supply a display name. 
     * **Description** : Add a description of the version.
     * **Life Cycle** : Select the life cycle stage of the API. 
     * **Compliance** : Select a compliance attribute.
     * **Accreditation** : Select an accreditation attribute.
     * **Documentation** : Enter the URL to documentation for the API.
     * **Add a Specification file** : Import an API [specification file](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro) to associate with the version. See [Add an API spec to a version](https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications#addspec).
     * **Link to a deployment** : Select one or more [deployments](https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro) to associate with the API. 
     * **User-defined attributes** : User-defined attributes are attributes that you define based on your organizational or team needs. See [User attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#user-attributes).
  8. Click **Create**.



### REST

To add a new version using the [Create an API version](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions/create) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions?version_id=VERSION_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X POST -H "Content-Type: application/json" \
      '{
        "display-name": "DISPLAY_NAME",
        "description": "DESCRIPTION"               # description is an optional attribute
        }'
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource to add the version to. 
  * VERSION_ID: (Optional) The unique identifier of the API version. If not provided, a system-generated ID will be used. **Note:** The ID must be 4-500 characters, and valid characters are `/[A-Z][a-z][0-9]-/.` The ID is the last component of the fully qualified, unique API resource name, which is in the format: `projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID`
  * DISPLAY_NAME: (Required) The display name of the version. You can use any name you wish. 
  * DESCRIPTION: (Optional) You can add a number of optional attributes to describe the version, including a description, an owner name, a link to documentation, and more. These optional attributes are listed and described in the [Version resource definition](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions#Version).



Sample output:
    
    
    {
      "name": "projects/myproject/locations/myproject/apis/docs-api-1/versions/myversion1",
      "displayName": "My Version 1",
      "createTime": "2024-04-02T18:48:41.162360Z",
      "updateTime": "2024-04-02T18:48:41.162360Z"
    }

## List API versions

This section explains how to list the versions associated with a registered API.

### REST

To view all the versions associated with a registered API, use the [List API versions](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions/list) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -H "Content-Type: application/json"
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 



Sample output:
    
    
    {
      "versions": [
        {
          "name": "projects/myproject/locations/us-central1/apis/streetcarts-test/versions/streetcarts-testv1",
          "displayName": "Streetcarts Test v1"
        }
      ]
    }

## Get API version details

This section explains how to get the details about an API version, including its attributes, operations, deployments, and specification files. 

### Console

To view version details in the console:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API you wish to inspect. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Click the **Versions** tab and select the version you wish to view from the **Select a version** drop-down list.
  6. Click a version to view its details. 

The **Version details** page displays the following information about the version: 

     * **Version details** : General information about the version, including its display name, documentation, and system-defined attributes.
     * **Operations** : A list of API operations that are part of the version.
     * **Specification files** : A list of specifications that are part of the version.
     * **Deployments** : A list of deployments that are associated with the version.
     * **Documentation** : The documentation attribute associated with the version.
     * **Additional attributes** : Any user-defined attributes associated with the version.



### REST

To view details of a version using the [Get API version details](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions/get) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 
  * VERSION_ID: The unique ID of the version. 



Sample output:
    
    
    {
      "name": "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1",
      "displayName": "Test Version 3",
      "documentation": {},
      "specs": [
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/specs/docs-spec-1"
      ],
      "apiOperations": [
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/operations/listpets",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/operations/createpets",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/operations/deletepet",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/operations/getpetbyid",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/operations/updatepet"
      ],
      "definitions": [
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcarts_testv1/definitions/pet"
      ],
      "createTime": "2024-04-04T14:53:57.299213423Z",
      "updateTime": "2024-04-04T14:53:58.027321138Z"
    }

## Delete an API version

This section explains how to delete an API version associated with an API resource. 

### Console

When you delete a version in the UI, all of the underlying specifications associated with the version (if any) are deleted.

To delete a version:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API that includes the version you wish to delete.
  4. Click an API to view its details. 
  5. Click the **Versions** tab and select the version you wish to delete from the **Select a version** drop-down list.
  6. Click delete **Delete version**.



### REST

By default, a version can only be deleted if all underlying specifications are deleted. If you want to delete all specifications under a version in one step, set the `force` query parameter to `true` in the Delete REST API.

To delete a version using the [Delete API version](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions/delete) API:
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      'https://apihub.googleapis.com/v1/projects/API_PROJECT/locations/API_LOCATION/apis/API_ID/versions/VERSION_ID'

Replace the following:

  * API_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * API_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource.
  * VERSION_ID: The ID of the version to delete.



To delete a version and all underlying specifications, set the `force` query parameter to `true`. For example:
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      'https://apihub.googleapis.com/v1/projects/API_PROJECT/locations/API_LOCATION/apis/API_ID/versions/VERSION_ID?force=true'

## Edit a version

### Console

To edit a version:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Click the **Versions** tab and select the version you wish to edit from the **Select a version** drop-down list.
  6. Click edit **Edit**.
  7. After making edits, click **Save** to save your changes. For a description of the editable attributes, see the [version resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions#Version) in the REST API reference.



### REST

To edit a version with the REST API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID?updateMask=LIST_OF_ATTRIBUTES"
        -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X PATCH -H "Content-Type: application/json" \
        '{
          "display-name": DISPLAY_NAME,  # Use the request body to specify attribute changes
          "description": "DESCRIPTION"
    
        }'

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API that has the version you wish to edit.
  * VERSION_ID: The ID of the version to edit.
  * DESCRIPTION: You can add other editable attributes in the request body, like the description and others. The editable attributes are listed in the Apigee hub API reference. the [Patch version API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/patch).
  * LIST_OF_ATTRIBUTES: A comma-separated list of fully qualified attribute names. For example: `?updateMask="description"`. 



Sample output: 
    
    
    {
      "name": "projects/myproject/locations/us-central1/apis/streetcarts-test/versions/streetcarts-testv1",
      "displayName": "Streetcarts Test v1",
      "description": "This is a revision of the test version.",
      "documentation": {},
      "createTime": "2024-04-18T19:57:11.870761Z",
      "updateTime": "2024-04-18T20:23:42.465324Z"
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
