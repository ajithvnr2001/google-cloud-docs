---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications/
title: Manage API specifications \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:29:10.022877+00:00
---

# Manage API specifications  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage API specifications Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This document describes how to manage API specifications in API hub. See also [Introduction to API specifications](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro). 

## Add an API spec to a version

You can add one or more API specifications to an [API version](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro). Choose from these options:

  * Add a spec when you create a version
  * Add a spec to an existing version



### Add a spec when you create a version

Using the UI only, you can add an API spec at the same time you create a version. You can either provide the URL to a specification that you can access or upload a specification file directly from your system.

### Console

To add a spec to a new version:

  1. Follow the steps listed in [Create an API version](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions#addversion) to get started. When you reach the **Add a new version** page, you can optionally add a specification file to the version: 
     1. Enter a display name for the specification file. You can use any name you wish.
     2. Select the specification file type. Specification type is a configurable system attribute. See also [System attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes). 
     3. Provide either a URI that points to a valid API specification file to which you have access, or browse to an API spec file on your system.
     4. (Optional) If you want to apply strict validation to the uploaded spec, select the **Restrict upload of spec file containing errors** checkbox. When this option is selected, a spec that contains validation errors will not be uploaded. By default, specs containing errors are uploaded.
**Note:** API [specification parsing](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro#specificationparsing) is only supported for [OpenAPI specifications](https://swagger.io/specification/) (v.2.0, v3.0 and v3.1) in JSON and YAML formats.


* Complete filling out the **Add a new version** page, and click **Create** when you are done.

### Add a spec to an existing version

You can use the UI or REST API to add an API specification to an existing version. 

### Console

To add a spec directly to a version:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version you wish to modify. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Select an API. 
  5. Click **Add specification file**.
  6. Specify the specification file details in the **Add specification file** form. You must provide a display name. The other attributes are optional. For more information on attributes, see [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes). 
     * **Specification file ID** : Click **Specify Unique ID** to optionally provide a unique ID for the specification file. If you omit the ID, API hub creates one for you. **Note:** Specification ID must be 4-500 characters long and can contain only uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and hyphens (-). The ID forms the last part of the API resource name: `projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID`. The full resource name is limited to 1000 characters.
     * **Display name** : Enter a display name for the specification file. You can use any name you wish.
     * **Specification file type** : Select the specification file type. Specification type is a configurable system attribute. See also [System attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes). 
     * **Specification document** : Provide either a URI that points to a valid API specification file to which you have access, or browse to an API spec file on your system.
     * (Optional) If you want to apply strict validation to the uploaded spec, select the **Restrict upload of spec file containing errors** checkbox. When this option is selected, a spec that contains validation errors will not be uploaded. By default, specs containing errors are uploaded.
     * **Version** : Select the version to add the specification file to.
  7. Click **Create**. **Note:** API [specification parsing](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro#specificationparsing) is only supported for [OpenAPI specifications](https://swagger.io/specification/) (v.2.0, v3.0 and v3.1) in JSON and YAML formats.



### REST

To add an API spec to a version, use the [Add API spec](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs/create) API:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      'https://apihub.googleapis.com/v1/projects/API_PROJECT/locations/API_LOCATION/apis/API_ID/versions/VERSION_ID/specs?spec_id=SPEC_ID' \
      -d "DATA_FILE or URI"

Replace the following:

  * API_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * API_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of an API resource. 
  * VERSION_ID: The ID of a version attached to the API resource. 
  * SPEC_ID: (Optional) The identifier of the spec. If not provided, a system-generated ID will be used. **Note:** The ID must be 4-500 characters, and valid characters are `/[A-Z][a-z][0-9]-/.` The ID is the last component of the fully qualified, unique API resource name, which is in the format: `projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID`
  * DATA_FILE or URI: Either a Base64-encoded file containing a valid API spec or a link to a spec. See the REST example. 



### REST example

In this example, create a new spec in API hub with a Base64-encoded OpenAPI spec. Upon upload, API hub parses the spec and creates a new spec entity that includes descriptive metadata plus sets of operation and definition entities. 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d "@data.json" \
      https://apihub.googleapis.com/v1/projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/specs?spec_id=dstreetcarts-spec

Sample output:
    
    
    {
        "name": "projects/common-dev-1/locations/us-central1/apis/streetcarts/versions/streetcartsv1/specs/dstreetcarts-spec",
        "displayName": "Test Spec 1",
        "specType": {},
        "contents": {
          "contents": [Base64-encoded contents of an OpenAPI 3.0.2 file] },
        "details": {
          "description": "This is a sample Pet Store Server based on the OpenAPI 3.0 specification.\nYou can find out more about Swagger at [https://swagger.io](https://swagger.io).",
          "openApiSpecDetails": {
            "format": "OPEN_API_SPEC_3_0",
            "version": "1.0.11"
          }
        },
        "createTime": "2024-04-04T22:39:05.674986Z",
        "updateTime": "2024-04-04T22:39:05.674986Z"
      }

To return spec details:
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" \
      https://apihub.googleapis.com/v1/projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1

Output:
    
    
    {
      "name": "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1",
      "displayName": "Test Version 3",
      "documentation": {},
      "specs": [
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/specs/dstreetcarts-spec"
      ],
      "apiOperations": [
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/operations/listpets",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/operations/createpets",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/operations/deletepet",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/operations/getpetbyid",
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/operations/updatepet"
      ],
      "definitions": [
        "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/definitions/pet"
      ],
      "createTime": "2024-04-04T14:53:57.299213423Z",
      "updateTime": "2024-04-04T14:53:58.027321138Z"
    }

## List specifications

This section explains how to list the specifications associated with an API version.

### Console

To list specifications with the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Under the **Versions** tab, locate the version you wish to inspect. 
  6. Select a version.
  7. Any specifications linked to the version are listed in the **Specification file** section.



### REST

To list specifications associated with an API version, use the [List specifications](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs/list) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/specs"
          -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 
  * VERSION_ID: The unique ID of the version. 



## Get specification details

This section explains how to get the details about an API specification associated with a version. 

### Console

To view details of a specification using the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version containing the specification you wish to inspect. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Under the **Versions** tab, locate the version you wish to inspect. 
  6. Select a version. 
  7. In the **Specification file** section, select a specification to view its details. 



### REST

To view details of a specification, use the [Get specification details](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs/get) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 
  * VERSION_ID: The unique ID of the version. 
  * SPEC_ID: The unique ID of the specification. 



Sample output:
    
    
    {
      "name": "projects/myproject/locations/us-central1/apis/streetcarts/versions/streetcartsv1/specs/dstreetcarts-spec",
      "displayName": "Test Spec 1",
      "details": {
        "description": "This is a sample Pet Store Server based on the OpenAPI 3.0 specification.\nYou can find out more about Swagger at [https://swagger.io](https://swagger.io).",
        "openApiSpecDetails": {
          "format": "OPEN_API_SPEC_3_0",
          "version": "1.0.11"
        }
      },
      "createTime": "2024-04-04T22:39:05.098508600Z",
      "updateTime": "2024-04-04T22:39:06.661264958Z"
    }

## Delete an API specification

This section explains how to delete an API specification from a version. Deleting a spec will also delete the associated operations from the version. 

### Console

To delete API resources with the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version that contains the spec you wish to delete. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Under the **Versions** tab, locate the version that contains the specification you wish to delete. 
  6. Select the version.
  7. In the **Specification file** section, select **Delete** from the **Actions** menu in the row of the specification you wish to delete.
  8. Click **Delete**.



### REST

To delete an API resource from API hub, use the [Delete API resource](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/delete) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X DELETE -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 
  * VERSION_ID: The unique ID of the version. 
  * SPEC_ID: The unique ID of the specification to delete. 



## Edit specification metadata

You can edit some of the metadata associated with a specification stored in API hub. For a list of metadata you can edit, see [Spec patch API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs/patch). 

### Console

You can make changes to an existing specification through the Google Cloud console. For example, you can change the display name, upload a new specification file, change the file type, and edit attributes:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version that contains the spec you wish to edit. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details.
  5. Under the **Versions** tab, locate the version that contains the specification you wish to edit.
  6. Select the version.
  7. In the Versions page, locate the specification you wish to edit.
  8. Select **Edit** from the **Actions** menu in the row of the specification you wish to edit.
  9. In the specification editing panel, you can change any of the following specification metadata: 
     * Display name
     * Specification file type
     * Specification document: Browse to a new specification file to upload.
     * (Optional) If you want to apply strict validation to the uploaded spec, select the **Restrict upload of spec file containing errors** checkbox. When this option is selected, a spec that contains validation errors will not be uploaded. By default, specs containing errors are uploaded.
     * User-defined attributes (if any)
  10. Click **Save**. 



### REST

To edit a specification with the REST API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID"
        -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X PATCH -H "Content-Type: application/json"
        '{
          "display-name": DISPLAY_NAME.  # Use the request body to specify attribute changes
          "contents": {
             "contents": Base64-encoded string
             "mimeType": MIME_TYPE
          }
        }'

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 
  * VERSION_ID: The unique ID of the version. 
  * SPEC_ID: The unique ID of the specification. 
  * **Request Body** : Use the request body to specify attributes to change. See [Specification resource definition](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs#Spec). 



## View specification lint results

API hub provides an in-built (Spectral) linter (validator) which validates your API's Open API specification. See [Validate API specifications](https://docs.cloud.google.com/apigee/docs/apihub/validate-spec).

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version that contains the spec you wish to inspect. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Under the **Versions** tab, locate the version that contains the specification you wish to inspect. 
  6. Click **See Results** in the Lint results column to view lint results.



## Get specification contents

This feature lets you review the contents of a specification that was uploaded to API hub.

### Console

To view details of a specification using the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version that contains the spec you wish to delete. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Under the **Versions** tab, locate the version that contains the specification you wish to inspect. 
  6. Click the spec name to view its contents.



### REST

The API retrieves the raw, Base64-encoded contents of an API spec that was uploaded to API hub. Use the [Get specification contents](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs/getContents) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/specs/SPEC_ID:contents"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 
  * VERSION_ID: The unique ID of the version. 
  * SPEC_ID: The unique ID of the specification. 



Sample output:
    
    
    {
      "contents": "Base64-encoded file contents"
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
