---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-api-deployments/
title: Manage deployments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:21.249804+00:00
---

# Manage deployments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-api-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage deployments Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This document describes how to create and manage API deployments. See also [Introduction to API deployments](https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro). After you create a deployment entity, you can link it to one or more API versions.

## Create a deployment

You can create a deployment entity in the console or with the REST API. 

### Console

To create a new deployment:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Under the **Deployments** tab, click **Add Deployment**. 
  6. Specify deployment details in the **Create deployment** form: 
     * **Deployment ID** : Click **Specify Unique ID** to optionally provide a unique ID for the deployment. If you omit the ID, API hub creates one for you. **Note:** The ID must be 4-500 characters, and valid characters are `/[A-Z][a-z][0-9]-/.` The ID is the last component of the fully qualified, unique API resource name, which is in the format: `projects/PROJECT/locations/LOCATION/deployments/DEPLOYMENT_ID`
     * **Deployment name** : (Required) Provide a display name for the deployment.
     * **Description** : Enter a description of the deployment.
     * **Deployment type** : (Required) Select the type of deployment. Possible values are defined in a system attribute, and you can modify them in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes).
     * **Resource URI** : (Required) Enter the unique Uniform Resource Identifier (URI) that directly points to and identifies the deployed API resource. This URI is used for programmatic management of the resource. **Tip:** For deployments on Apigee, it is best practice to use the following format: `organizations/([^/]+)/environments/([^/]+)/apis/([^/]+)`. 
     * **Environment** : The environment mapping to this deployment. The environment maps to the system-defined environment attribute.
     * **Documentation** : Enter a link to documentation for the deployment. The link must begin with `https://` or `http://`.
     * **SLO** : Provide the SLO for this deployment. This maps to the SLO system-defined attribute. You can modify values for this attribute in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes).
     * **Management URL** : Provide a supplementary URL for broader administrative purposes related to this deployment. 

For example, this could be a link to a monitoring dashboard, a team's playbook for the API, or a separate administrative console. 

This URL is mapped to the `management_url` system-defined attribute. You can modify values for this attribute in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes). 

     * **Source project** : The project where the deployment is created.
     * **Source environment** : The environment where the deployment is created.
     * **Endpoints** : (Required) Provide the endpoints at which this deployment resource is listening for API requests. This could be a list of complete URIs, hostnames or IP addresses.
     * **Link to a version** : Link the deployment to one or more API versions.
     * **User defined attributes** : User-defined key/value pairs. You can add user-defined attributes in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes).
  7. Click **Create**. 



### REST

To add a new deployment using the [Create a deployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/create) API:
    
    
      curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "display_name": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "deployment_type": {
        "enum_values": {
          "values": [
            {
              "id": "DEPLOYMENT_TYPE"
            }
          ]
        }
      },
      "resource_uri": "RESOURCE_URI",
      "endpoints": [
        "ENDPOINT"
      ]
    }' https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/deployments?deployment_id=DEPLOYMENT_ID
    

Replace the following:

  * DISPLAY_NAME: (Required) The display name of the deployment. You can use any name you wish.
  * DESCRIPTION: (Optional) A description of the deployment.
  * DEPLOYMENT_TYPE: (Required) The type of deployment. Possible values are defined in a system attribute, and you can modify them in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes).
  * RESOURCE_URI: (Required) Enter the unique Uniform Resource Identifier (URI) that directly points to and identifies the deployed API resource. This URI is used for programmatic management of the resource. **Tip:** For deployments on Apigee, it is best practice to use the following format: `organizations/([^/]+)/environments/([^/]+)/apis/([^/]+)`. 
  * ENDPOINT: (Required) The endpoints at which this deployment resource is listening for API requests. This could be a list of complete URIs, hostnames or IP addresses.
  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPLOYMENT_ID: (Optional) The identifier of the deployment. If not provided, a system-generated ID will be used. **Note:** Deployment ID must be 4-500 characters long and can contain only uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and hyphens (-). The ID forms the last part of the API resource name: `projects/PROJECT/locations/LOCATION/deployments/DEPLOYMENT_ID`.
  * **Optional Attributes** : In addition to the required display name, deployment type, resource URI, and endpoints, you can attach optional attributes and entities to a deployment. These additional items are described in the [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 



## Link a deployment to an API version

A version can have one or more deployments linked to it. This section explains how to link deployments to versions. You can link deployments to a version at the time you create the version, or, you can link deployments to an existing version by editing it. See [Add a version to an API](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions#addversion) and [Edit a version](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions#editversion). 

To link a deployment to a new or existing version, the deployment must already exist. See Create a deployment. 

### Console

To link a deployment to a version:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Select an API. 
  5. In the **Versions** table, locate the version you wish to edit. 
  6. Select **Edit** from the Actions menu at the right side of the version row or select the version and click **Edit version** in the details page. 
  7. Under **Link to a deployment** select one or more deployments to link to the version and click **Ok**.
  8. Click **Save**.



### REST

Example linking a deployment to a version:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_NAME/versions/VERSION_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X PATCH -H "Content-Type: application/json" \
      '{
        "deployments": "DEPLOYMENTS"
      }'

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_NAME: The name of the API that has the version you wish to edit.
  * VERSION_ID: The unique ID of the version to edit.
  * DEPLOYMENTS: The fully qualified resource name of one or more deployments. For example: `"projects/myproject/locations/us-central1/deployments/mydeployment-1, projects/myproject/locations/us-central1/deployments/mydeployment-2"`



For more information, see [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 

## List deployments

This section explains how to list the deployments. You can list all deployments associated with all the versions for an API, or list all deployments associated with a specific version. 

### Console

To list deployments with the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Select the **Deployments** tab to list all deployments associated with the API. 
  6. From the **Versions** tab, select a version if you want to see the deployments associated with that version. 



### REST

To list all deployments, use the [List deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/list) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/deployments"
            -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.



For more information, see [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 

## Get deployment details

This section explains how to get the details about an API deployment.

### Console

To view details of a deployment:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Select the **Deployments** tab to list all deployments associated with the API. 
  6. Select the deployment to view its details page. 



### REST

To view details of a deployment, use the [Get deployment details](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/get) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/deployments/DEPLOYMENT_ID"
        -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPLOYMENT_ID: The unique ID of the deployment. 



For more information, see [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 

## Delete an API deployment from an API

This section explains how to delete API deployment. Deleting an API deployment removes it from the API. It will no longer show up in the list of deployments, and you cannot filter APIs based on the deleted deployment.

**Note:** Ensure that you have unlinked the deployment from all APIs and API versions before deleting it.

### Console

To delete a deployment with the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Select the **Deployments** tab to list all deployments associated with the API. 
  6. Locate the deployment you wish to delete. 
  7. Select **Delete** from the deployment's **Action** menu. 



### REST

To delete a deployment from API hub, use the [Delete deployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/delete) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/deployments/DEPLOYMENT_ID"
        -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X DELETE -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPLOYMENT_ID: The unique ID of the deployment to delete. 



For more information, see [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 

## Unlink an API deployment from an API or version

This section explains how to unlink an API deployment from an API or version. When unlinked, a deployment no longer shows up in the list of deployments. To unlink a deployment from an API, you must unlink it from all versions of the API. 

### Console

To unlink a deployment from an API with the UI:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Select the **Deployments** tab to list all deployments associated with the API. 
  6. Locate the deployment you wish to unlink. 
  7. Select **Unlink from API** from the deployment's **Action** menu. 



### REST

To unlink a deployment from an API, use the [Patch deployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/patch) API: 
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "deployments": [
        "DEPLOYMENT_NAME",
        "DEPLOYMENT_NAME"
      ]
    }' -X PATCH https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_NAME/versions/VERSION_ID?update_mask=deployments
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_NAME: The name of the API that has the version you wish to edit.
  * VERSION_ID: The unique ID of the version to edit.
  * DEPLOYMENT_NAMES: The comma-separated list of deployment names that should remain linked with the version. The name of the deployment that is to be unlinked should **NOT** be present in this list.



For more information, see [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 

## Edit a deployment

This section explains how to edit a deployment.

### Console

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details. 
  5. Select the **Deployments** tab to list all deployments associated with the API. 
  6. Locate the deployment you wish to edit. 
  7. Select **Edit** from the deployment's **Action** menu, or click the deployment and then click **Edit Deployment** in the Deployment details panel. 



### REST

To edit a deployment, use the [Patch deployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/patch) API:
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "name": "projects/HUB_PROJECT/locations/HUB_LOCATION/deployments/DEPLOYMENT_ID",
      "display_name" : "DISPLAY_NAME",
      "description":"DESCRIPTION",
      "endpoints": ["ENDPOINT"]
      } ' -X PATCH https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/deployments/DEPLOYMENT_ID?update_mask=display_name,description,endpoints
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPLOYMENT_ID: The unique ID of the deployment to edit. 
  * DISPLAY_NAME: The display name of the deployment. 
  * DESCRIPTION: The description of the deployment. 
  * ENDPOINT: The endpoint of the deployment. 
  * DEPLOYMENT_ATTRIBUTES: Attach the attributes you wish to modify in the request body. The editable attributes are described in [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments/patch) in the REST API reference.
  * UPDATE_MASK: The comma-separated list of fields to update.



For more information, see [deployment resource description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.deployments) in the REST API reference. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
