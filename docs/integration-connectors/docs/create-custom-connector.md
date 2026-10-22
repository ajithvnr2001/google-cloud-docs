---
url: https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector/
title: Create a custom connector \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:37.190373+00:00
---

# Create a custom connector  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Create a custom connector

This page describes how to create a custom connector. To understand what is a custom connector, see [Custom connectors.](https://docs.cloud.google.com/integration-connectors/docs/custom-connectors)

**Note:** A custom connector is a global resource; which means that once it's created, you can use it any of the [locations supported for Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/locations).

To establish connectivity to your backend by using a custom connector, you need to do the following tasks:

  1. **Create a custom connector** \- In this task, you will define the contract between Integration Connectors and your endpoint (backend) by providing the endpoint's OpenAPI specification. Currently, only OpenAPI version 3.0 and all it's minor versions are supported. Specifying the specification, is a one time activity.
  2. **Create a custom connector connection** \- In this task, you will configure your backend's connection details, such as the hostname and authentication. For a specific custom connector, you can create as many connections as you require.



To understand the difference between a connector and a connection, see [Connector versus connection](https://docs.cloud.google.com/integration-connectors/docs/connectorvsconnection).

## Before you begin

  * To get the permissions that you need to create the custom connector, ask your administrator to grant you the [Custom Connectors Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Enable the Connector API:   
[Enable the Connector API](https://console.cloud.google.com/apis/library/connectors.googleapis.com)



## Create a custom connector

As described in [backend connectivity scenarios](https://docs.cloud.google.com/integration-connectors/docs/custom-connectors#backend-conn-scenarios), custom connectors can have any of the following connectivity patterns: 

  * Direct connectivity to your backend's public endpoint.
  * Indirect connectivity to your backend through an intermediary public endpoint.



The custom connector creation steps slightly vary for these two patterns.

### Create with direct connectivity

To create a custom connector with direct connectivity to your backend's endpoint, do the following steps:

### Console

  1. In the [Console](https://console.cloud.google.com/), go to the **Integration Connectors > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/connectors/custom-connectors)

  2. Click **Create new** to open the **Create custom connector** page.
  3. In the **Connector details** section, set the following fields: 
     1. **Connector name** : Enter a name for the connector.
     2. **Display name** : Enter a display name for the connector.
     3. **Description** : Enter a description.
     4. **Service account** : Select a service account that has the required roles.
     5. **Logo** : Upload the image to a Cloud Storage bucket to use it as the connector logo. **Note:** Ensure your Cloud Storage bucket has the [public access prevention](https://docs.cloud.google.com/storage/docs/using-public-access-prevention#console) disabled.
  4. Click **Next**.
  5. In the **Connector specification** section, set the following fields: 
     1. **Custom connector type** : Select the custom connector type.
     2. **Connector specification** : Either enter the public URL of your Open API specification or upload your specification file to a Cloud Storage bucket.
  6. Review the connector configuration details, and then click **Create**.



If the connector creation is successful, the newly created connector will be displayed in the [ Go to the Custom connectors page](https://console.cloud.google.com/connectors/custom-connectors), and if it's a new connector, a first version of the connector is also created. You can view the version details in the **Version** tab of the **Custom Connector details** page. For more information, see [](https://docs.cloud.google.com/integration-connectors/docs/custom-connector-versions). 

However, note that, to connect to your backend, you must create a connection for the newly created connector. For more information, see Create a custom connector connection.

### API

The following sample commands show how to create a custom connector by using the Integration Connectors APIs:

  1. Create the connector. 
         
         curl -X POST \
         -H "authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json"
         -d '{"customConnectorType":"OPEN_API", \
         "displayName":"CUSTOM_CONNECTOR_NAME", \
         "description": "an open api based custom connector for hrms"}' \
         "https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/customConnectors?custom_connector_id=UNIQUE_IDENTIFIER"
         

Replace the following: 

     * `CUSTOM_CONNECTOR_NAME`: A name for the custom connector.
     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `UNIQUE_IDENTIFIER`: A unique identifier for the connector. For example `custom-connector-1`.
  2. Configure the custom connector version. 
         
         curl -X POST \
         -H "authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{"spec_location": "SPECIFICATION_URL",}' \
         "https://connectors.googleapis.comv1/projects/PROJECT_ID/locations/global/customConnectors/openapi-customconnector/customConnectorVersions?custom_connector_version_id=VERSION_NUMBER"
         

Replace the following: 

     * `SPECIFICATION_URL`: The Open API specification URL. For example, `https://petstore3.swagger.io/api/v3/openapi.json`.
     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `VERSION_NUMBER`: A version number for the connector. For example, `2`.



### Create with indirect connectivity

To create a custom connector that connects to your backend through an intermediary endpoint, do the following steps:

### Console

  1. In the [Console](https://console.cloud.google.com/), go to the **Integration Connectors > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/connectors/custom-connectors)

  2. Click **Create new** to open the **Create custom connector** page.
  3. In the **Connector details** section, set the following fields: 
     1. **Connector name** : Enter a name for the connector.
     2. **Display name** : Enter a display name for the connector.
     3. **Description** : Enter a description.
     4. **Configure connector destination for backend access** : Enable this option. This shows the additional configuration sections in the page. 
     5. **Service account** : Select a service account that has the required roles.
     6. **Logo** : Upload the image to a Cloud Storage bucket to use it as the connector logo. **Note:** Ensure your Cloud Storage bucket has the [public access prevention](https://docs.cloud.google.com/storage/docs/using-public-access-prevention#console) disabled.
  4. Click **Next**.
  5. In the **Connector specification** section, set the following fields: 
     1. **Custom connector type** : Select the custom connector type.
     2. **Connector specification** : Either enter the public URL of your Open API specification or upload your specification file to a Cloud Storage bucket. 
  6. Click **Next**.
  7. In the **Connector destination** section, set the following fields: 
     1. **Destination type** : Select **Host address**.
     2. **Host** : Enter the host name where your intermediary service is running, and include the `http://` or `https://` scheme.
     3. **Port** : Enter the port number of your intermediary service.
  8. Click **Next**.
  9. In the **Connector authentication** section, select the intermediary service's authentication type, and then enter the corresponding details as prompted. This step is to configure the authentication from Integration Connectors to the intermediary service. 

The authentication configuration from the intermediary service to the backend can't be configured in Integration Connectors; it's up to the intermediary service on how it wants to authenticate with the backend.

You can use the following authentication types to authenticate to the intermediary service:

     * Service Account Authentication
     * API Key Authentication
     * OAuth 2.0 - Client Credentials Authentication
     * Basic Authentication
     * Digest Authentication

To understand how to configure these authentication types, see Configure authentication.

If access to the API's resources is unrestricted and doesn't require any authentication, select **No Authentication**. 

  10. Click **Next**.
  11. In the **Backend variables** section, enter the values that you want to send to your backend through the intermediary service. You must configure the values as key-value paris. To enter a key-value pair, click **Add variable** , and then set the following fields: 
     * **Key** : Enter the key name.
     * **Value type** : Select the datatype of the variable.
     * **Display name** : Enter a display name.
     * **Location** : Specify how you want the connector to send the variables to the intermediary service. The available options are; `Header`, `Request payload`, and `Query parameter`.
     * Optionally, select `Required` to specify that the variable is a mandatory variable.
**Note:** You will be prompted to enter the values of the configured variables when creating a connection.
  12. Click **Next**.
  13. Review the connector configuration details, and then click **Create**.



If the connector creation is successful, the newly created connector will be displayed in the [Custom connectors page](https://console.cloud.google.com/connectors/custom-connectors), and if it's a new connector, a first version of the connector is also created. You can view the version details in the **Version** tab of the **Custom Connector details** page. For information on creating and editing a custom connector version, see [Manage custom connector versions](https://docs.cloud.google.com/integration-connectors/docs/manage-custom-connector-versions). 

However, note that, to connect to your backend, you must create a connection for the newly created connector. For more information, see Create a custom connector connection.

#### Configure authentication

Enter the details based on the authentication you want to use.

  * **Service Account Authentication**

Select this option to authenticate using a Google Cloud service account. Ensure that you have provided the service account with the relevant IAM roles and permissions required for authentication. 

    * **Scopes** : Select the required OAuth 2.0 scopes from the drop-down. For more information, see [Access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).
  * **API key authentication**

Select this option to authenticate using a API key.

    * **API key** : Select the Secret Manager secret of the API key.
    * **Secret version** : Select the secret version.
    * **API key parameter name** : Enter a parameter name for the API key. An API key is sent to your backend server as a key-value pair. The value you enter here will be used as the key name for the API key that you have previously selected.
    * **API key location** : Select where you want to add API key in the request.
  * **OAuth 2.0 - Client credentials grant**
    * **Client ID** : The client id to use for authenticating to the intermediary service.
    * **Client Secret** : Secret Manager Secret containing the client secret for authenticating to the intermediary service.
    * **Request format for access token** : Request format to be used in requests made to fetch access token from auth server. Select `body` to pass client ID and Secret as a request body, or `header` to pass them as encoded header.
    * **Token Request Path** : Request path to be appended to the auth server URL to fetch access token URL.
  * **Basic Authentication**
    * **Username** : Username used for authenticating to the intermediary service.
    * **Password** : Secret Manager Secret containing the password associated with the provided username.
  * **Digest Authentication**
    * **Username** : Username used for authenticating to the intermediary service.
    * **Password** : Secret Manager Secret containing the password associated with the provided username.



### API

The following sample commands show how to create a custom connector by using the Integration Connectors APIs:

  1. Create the connector. 
         
         curl -X POST \
         -H "authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json"
         -d '{"customConnectorType":"OPEN_API", \
         "displayName":"CUSTOM_CONNECTOR_NAME", \
         "description": "an open api based custom connector for hrms"}' \
         "https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/customConnectors?custom_connector_id=UNIQUE_IDENTIFIER"
         

Replace the following: 

     * `CUSTOM_CONNECTOR_NAME`: A name for the custom connector.
     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `UNIQUE_IDENTIFIER`: A unique identifier for the connector. For example `custom-connector-1`.
  2. Configure the custom connector version and the authentication. 
         
         curl -X POST \
         -H "authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{"spec_location": "SPECIFICATION_URL", \
         "service_account":"test-sa", \
         "enable_backend_destination_config": true, \
         "auth_config": { \
         "auth_type":"USER_PASSWORD", \
         "auth_key": "basic", \
         "user_password": { \
         "username":"USERNAME", \
         "password": {"secret_version":"projects/PROJECT_ID/secrets/fidelity-secret/versions/SECRET_VERSION_NUMBER"} \
         }}, \
         "backend_variable_templates": [{ \
         "key":"authkey", \
         "value_type":"SECRET", \
         "display_name":"Authorization Key", \
         "required":true, \
         "location_type": "HEADER" \
         }], \
         "destination_configs":[{ \
         "key":"base_url", \
         "destinations": [{ \
         "host":"DESTINATION_HOST_ADDRESS" \
         }]} \
         ]}' \
         "https://connectors.googleapis.com/v1/projects/PROJECT_ID/locations/global/customConnectors/facade-connector/customConnectorVersions?custom_connector_version_id=CONNECTOR_VERSION_NUMBER"
         

Replace the following: 

     * `SPECIFICATION_URL`: The Open API specification URL. For example, `https://petstore3.swagger.io/api/v3/openapi.json`.
     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `USERNAME`: Username for authentication with the intermediary service.
     * `SECRET_VERSION_NUMBER`: The Secret Manager secret version number. For example, `2`.
     * `DESTINATION_HOST_ADDRESS`: Host address of the intermediary service. For example, `http://www.test.com:80`.
     * `CONNECTOR_VERSION_NUMBER`: The custom connector version number. For example, `1`.
**Note:** This sample API call uses `Username and Password` authentication. Based on your requirements, you can use a different authentication type.


## Create a custom connector connection

After creating your custom connector, to connect to your backend, you must create a connection of the custom connector type. The following are the high-level steps to create a new connection:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **Create new** to open the **Create connection** page.
  3. In the **Location** section, select a location for the connection from the **Region** field. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

  4. Click **Next**.
  5. In the **Connection details** section, set the following fields: 
     1. **Connector** : Select your custom connector from the drop down list of available connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection name** field, enter a name for the connection. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 63 characters.
     4. Optionally, enter a **Description** for the connection.
     5. Optionally, select **Enable cloud logging** to enable cloud logging.
     6. **Service account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. Optionally, click **Add label** to add a label to the connection in the form of a key-value pair.
  6. Click **Next**.
  7. If the connector uses an intermediary service to connect to your backend, do the following: 

In the **Destinations** section, set the following fields:

     1. **Destination type** : Select **Host address**.
     2. **Host** : Enter the host name where your intermediary service is running, and include the `http://` or `https://` scheme.
     3. **Port** : Enter the port number of your intermediary service.

The destination field contains the spec URL from the OpenAPI spec by default. When multiple server URLs exist, it shows the first one.

  8. Click **Next**.
  9. In the **Authentication** section, enter the authentication details for your backend. 
     * If you connect directly to your backend, Integration Connectors prompts you to configure the authentication for your backend.
     * If you connect indirectly to your backend through an intermediary service, Integration Connectors doesn't prompt you to configure authentication details. When creating the connector, you would have already configured the authentication between Integration Connectors and the intermediary service. Integration Connectors doesn't require you to configure the authentication between the intermediary service and the backend; it's up to the intermediary service on how it wants to authenticate with the backend. 
  10. Click **Next**.
  11. Review the connection configuration details, and then click **Create**.



If the connection creation is successful, it's listed in the [All connections page](https://console.cloud.google.com/connectors/connections), and the connection becomes available for in Application Integration. You can use the connection in your integration through the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

## Considerations

Consider the following points when creating a custom connector:

  * Integration Connectors supports only OpenAPI version 3.0 and all it's minor versions.
  * The Open API specification isn't validated during custom connector creation. When you create a connection for the custom connector, Integration Connectors validates the specification, and if it has errors, the connection will be in the `Error` state.
  * Integration Connectors doesn't differentiate between entities and actions. Hence, both the entities and actions of your backend will be listed as `Actions` in your custom connector.
  * Custom connectors aren't supported in Google Cloud projects that have [VPC Service Controls](https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors) enabled.
  * Both the Open API specification endpoint, and the backend endpoint should be publicly accessible. This means that you can't establish private connectivity to your backend.
  * Multi-part media type isn't supported in the Open API specification.
  * You can't edit the version details of a custom connector.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
