---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure/
title: HTTP \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:25.944300+00:00
---

# HTTP  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HTTP

The HTTP connector provides connectivity to HTTP service and allows you to consume HTTP based APIs. The connector also supports SSL/TLS connectivity through custom configuration and supports various authentication mechanisms like OAuth 2.0 Client Credentials Grant, Basic, and Digest.

## Before you begin

Before using the HTTP connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create New** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **HTTP** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, to check the status of the connection, in the **Status Check** field, specify an endpoint URL. The URL can also include an endpoint attachment IP address. The status is active by default. 
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. **Use proxy** : Select the checkbox to configure a proxy server for the connection. 
        1. Click **\+ Add destination**.
        2. Select a **Destination Type**. 
           * **Host address** : Specify the hostname or IP address of the destination. 

If you want to establish private connection to your backend, do the following:

             * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
             * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.
**Note:**
             * Specify the hostname or the IP address without prefixing with `http` or `https`.
             * The default port is set to 80.
     10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     11. Optionally, if you want to use SSL, select **Enable SSL**. This displays the SSL configuration details. 
        1. Select a trust store type. It can be either **Public** , **Private** , or **Insecure Connection**. 
        2. Select the certificates as displayed based on your trust store selection.
        3. If you use a self-signed certificate or a private trust store certificate, store the root certificate as a Secret Manager Secret in PEM (Privacy Enhanced Mail) format, and then in **Custom Trust Store** , select the required secret.
        4. If you are using mTLS, select the key store certificates in the **Key Store** section.
        5. Optionally, select the TLS version.
        6. Enter the supported cipher suite. Enter multiple cipher suites, as comma separated values. For more information, see Supported cipher suites. 
**Note:**
        * All your certificates must be X.509 certificates and must be in PEM format.
        * You can't directly select a certificate when configuring SSL. You must store all your certificates and private keys as a Secret Manager Secret, and then select the required secret during SSL configuration.
        * The default scheme is `HTTP`. If you enable SSL, the default scheme is set to `HTTPS`. However, you can override the default scheme by configuring the `scheme` attribute in your payload. See Examples.
        * A keystore is required only for mutual TLS.
        * The private truststore does not support certificate chains. Upload only the root CA certificate.
        * If a certificate and private key are stored in a single file, you must separate them into individual secrets before using them in the UI.
     12. Click **Next**. 
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **\+ Add destination**.

  6. Click **Next**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the HTTP connection:

     * Custom Authentication
     * [OAuth 2.0 - Client credentials grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4)
     * [Basic Authentication](https://www.rfc-editor.org/rfc/rfc7617)
     * [Digest Authentication](https://www.rfc-editor.org/rfc/rfc7616)
     * [OAuth 2.0 - Authorization code](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1)
     * [Service account](https://docs.cloud.google.com/iam/docs/service-account-creds)
     * [Service account ID token authentication](https://docs.cloud.google.com/docs/authentication/get-id-token)
     * API key authentication

To understand how to configure these authentication types, see Configure authentication.

  2. Click **Next**.


* **Review** : Review your connection and authentication details.
* Click **Create**. **Note:** If the connection creation is successful, the status of the newly created connection will be `Active` in your [Connections page](https://console.cloud.google.com//connectors/connections) in the [Cloud console](https://console.cloud.google.com/). However, the `Active` state only indicates that the configuration provided by you is valid, and doesn't indicate that the connectivity to your backend system is established.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Custom Authentication**

Custom authorization details can be added as a request header during action execution of the [Connectors](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) task.

  * **OAuth 2.0 - Client credentials grant**
    * **Client ID** : The client id to be used for authenticating HTTP request.
    * **Client Secret** : Secret Manager Secret containing the client secret for authenticating HTTP request.
    * **Request format for access token** : Request format to be used in requests made to fetch access token from auth server. Select `body` to pass client ID and Secret as a request body, or `header` to pass them as encoded header.
    * **Token Request Path** : Request path to be appended to the auth server URL to fetch access token URL.
    * **Default Expiration Time** : Default expiration time (in seconds) for the access token. This time will be used in case access token response does not have expiration time. If the value is not provided, token will be refreshed in 6 hours.
  * **Basic Authentication**
    * **Username** : Username used for making HTTP request.
    * **Password** : Secret Manager Secret containing the password associated with the provided username.
  * **Digest Authentication**
    * **Username** : Username used for making HTTP request.
    * **Password** : Secret Manager Secret containing the password associated with the provided username.
  * **OAuth 2.0 - Authorization code**
    * **Client ID:** Client ID as provided by your external application.
    * **Scopes:** Permission scopes supported by your external application. 
    * **Client secret:** Select the [Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). You should have created the Secret Manager secret prior configuring this authorization.
    * **Secret version:** Secret Manager secret version for client secret.
    * Optionally enable **PKCE** (Proof Key for Code Exchange) if your backend server supports it.
    * **Authorization URL:** Enter the authorization URL for your external application.
    * **Access token URL:** Enter the URL for getting the access token of your external application.

For the `Authorization code` authentication type, after creating the connection, you should perform a few additional steps for configuring authentication. For more information, see Additional steps after connection creation.

When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

**Note:** If you are using `Authorization code` authentication type and have made any cofiguration changes in your external application, you must re-authorize your HTTP connection. To understand how to re-authorize, see Re-authorization for Authorization code. 
  * **Service account**

Select this option to authenticate using the service account that you provided in the preceding steps when configuring this connection. Ensure that you have provided the service account that has the relevant IAM roles and permissions required for authentication. 

    * **Scopes** : Select the required OAuth 2.0 scopes from the drop-down. For more information, see [Access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).
  * **Service account ID token authentication**

Select this option to authenticate using the ID token generated from the service account that you provided in the preceding steps. This authentication uses JSON Web Tokens (JWT) for authentication. The ID token provider, signs and issues the JWTs for authentication using a service account.

    * **Audience** : Enter the recipients to whom the JWT is intended for.
    * **Header Name** : Enter the header name for generated ID token to be used in the HTTP header. If you don't specify any value for this field, by default the key value is set to `Authorization`.
  * **API key authentication**

Select this option to authenticate using a API key.

    * **API key** : Select the Secret Manager secret of the API key.
    * **Secret version** : Select the secret version.
    * **API key parameter name** : Enter a parameter name for the API key. An API key is sent to your backend server as a key-value pair. The value you enter here will be used as the key name for the API key that you have previously selected.
    * **API key location** : Select where you want to add API key in the request.



### Supported cipher suites

TLS version | Supported cipher suites  
---|---  
1.2 | 

  * TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  * TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
  * TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
  * TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
  * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  * TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  * TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
  * TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  * TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA
  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA
  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA256

  
1.3 | 

  * TLS_AES_256_GCM_SHA384
  * TLS_CHACHA20_POLY1305_SHA256
  * TLS_AES_128_GCM_SHA256

  
  
### Additional steps after connection creation

If you selected `OAuth 2.0 - Authorization code` for authentication, you must do the following additional steps after creating the connection:

  1. In the [Connections page](https://console.cloud.google.com/connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application.
  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).




## Re-authorization for Authorization code

If you are using `Authorization code` authentication type and have made any cofiguration changes in your backend HTTP application, you must re-authorize your HTTP connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions.

**Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

  * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. 

However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.

  * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
    * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)

Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.

  * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## System limitations

  * The HTTP connector does not support the `multipart/form-data` content type.

  * The HTTP connector can process 100 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 
    * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
    * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.




## Supported actions

The HTTP connector supports the following actions:

  * HttpRequest



### HttpRequest action

The HTTP connector guarantees at least one attempt to send the request to the configured endpoint. This is subject to [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla). The following tables describe the input and output parameters of the HttpRequest action.

#### Input parameters of the HttpRequest action

Parameter name | Data type | Required | Description  
---|---|---|---  
Url | Struct | No | [URL](https://datatracker.ietf.org/doc/rfc1808/) for which you want to send the request. The URL has the format `<scheme>://<netloc>/<path>;<params>?<query>#<fragment>`. If you provide `netloc`, it overrides the hostname provided during connection creation.  
Method | String | No | HTTP request method such as GET, POST, DELETE, or PUT. The default value is GET.  
Headers | Struct | No | HTTP request headers.  
Body | String | No | HTTP request body.  
RequestHasBytes | Boolean | No | Whether to send request as bytes. If set to `true`, you must send the request as a Base64 encoded string in the `Body` parameter. The default value is `false`.  
ResponseHasBytes | Boolean | No | Whether to receive the response as bytes. If set to `true`, you will receive the response as a Base64 encoded string in the `ResponseBody` output parameter. The default value is `false`.  
HttpVersion | String | No | HTTP version to be used when making a request. The supported values are 1.1 and 2. If you specify version 2, ALPN (Application-Layer Protocol Negotiation) negotiation takes place and version 1.1 will be used if the server doesn't support version 2. The default value is 2.  
ResponseFormat | String | No | Specifies the format of the response from the connector. The supported values are `v1` and `v2`. The default value is `v1`. **Sample v1 response:**
    
    
    [{
    "ResponseBody": "{\n \"status\": 200\n}"
    }, {
    "StatusCode": 200.0
    }, {
    "HttpVersion": "2"
    }, {
    "ResponseHeaders": {
    ":status": "200",
    "content-length": "19"
    }
    }]

**Sample v2 response:**
    
    
    [{
    "ResponseBody": "{\n \"status\": 200\n}",
    "StatusCode": 200.0,
    "HttpVersion": "2",
    "ResponseHeaders": {
    ":status": "200",
    "content-length": "19"
    }
    }]

| FailOnError | Boolean | No | Specifies the behavior of the connection when there is an error in your backend application. 

  * `true` \- Throws an exception. The exception thrown by your backend is propagated in the connection's response.
  * `false` \- Does not throw an exception. But returns the error code and the error message in the response.

The default value is `true`. | Timeout | Integer | No |  Timeout value for HTTP request in seconds. Maximum allowed value is 150 seconds.   
  
#### Output parameters of the HttpRequest action

Parameter name | Data type | Description  
---|---|---  
ResponseBody | String | Response received from the HTTP server.  
StatusCode | Integer | Status code received from the HTTP Server.  
HttpVersion | String | Version negotiated for the HTTP Request.  
ResponseHeaders | Struct | HTTP response headers in the form of `key,value` pairs.  
  
## Examples

This examples in this section describe the following operations:

  * Configure a request payload
  * Send bytes content
  * Get bytes content



The following table lists the sample scenarios and the corresponding configuration in the Connectors task:

Task | Configuration  
---|---  
Configure a request payload | 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `HttpRequest` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Url": {
             "scheme": "https",
             "netloc": "httpbin.org",
             "path": "post",
             "query": "example=A&sort=value",
             "fragment": "exampleFragment"
           },
           "Method": "POST",
           "Headers": {
             "Accept": ["application/json", "application/xml"],
             "a": "b"
           },
           "Body": "{\"thisIsRequestJSON\":\"someValue\"}"
         }

  4. Click **Save**.

This example makes a POST request to the `https://httpbin.org/post?example=A&=value#exampleFragment` URL. And because `netloc` is provided in the payload, it overrides the hostname provided during the connection creation.   
Send bytes content |  To send bytes (like files) content, you must set the `RequestHasBytes` request attribute to `true`, and set the `body` attribute to the Base64 encoded string that you want to send, as shown in the following sample. 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `HttpRequest` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Url": {
             "scheme": "https",
             "netloc": "httpbin.org",
           },
           "Method": "POST",
           "Headers": {
             "Accept": ["application/json", "application/xml"],
             "a": "b"
           },
           **"Body" : "SGVsbG8gV29ybGQ="**,
           **"RequestHasBytes" :true**
         }

  4. Click **Save**.

This example makes a POST request to the `httpbin.org` server, and in the request body sends the file content in the form of a Base64 encoded string. The server can decide on how to process the file content.  
Get bytes content |  To get bytes (as Base64 string) from the server, you must set the `ResponseHasBytes` request attribute to `true` as shown in the following sample. 

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `HttpRequest` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "Url": {
             "scheme": "https",
             "netloc": "httpbin.org",
           },
           "Method": "GET",
           "ResponseHasBytes":true
         }

  4. Click **Save**.

This example makes a GET request to the `httpbin.org` server, and in the request body sets the `ResponseHasBytes` to `true`.  
**Note:** After you run your integration, the connector's response will be available in the Connector task's `connectorOutputPayload` output variable.

## Error codes

This section descries the error messages that you might get when using the HTTP connection.

Error message | Cause  
---|---  
Error connecting with the HTTP server | The HTTP connection failed to establish connection with the server because of SSL handshake failure or an incorrect HTTP server endpoint.  
Error response received from the HTTP server | The HTTP server you are trying to connect returns an error response with status code 4xx or 5xx. Sample response: 
    
    
    {
      "error": {
        "code": 400,
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "metadata": {
              "Body": "{\"thisIsResponseJSON\":\"someValue\"}"
              "Error": "Error response received from the HTTP server",
              "Headers": "{\":status\":[\"400\"], \"access-control-allow-credentials\":[\"true\"]}",
              "StatusCode": "400",
              "connection_type": "Http"
            }
          }
        ],
        "message": "Unable to execute HTTP Request",
        "status": "FAILED_PRECONDITION"
      }
    }  
  
Error while fetching access token | There was an error when retrieving access token for the `OAuth Client Credentials Grant` authentication type.  
Digest Auth Error | The connector runtime hasn't received a digest challenge or the challenge is of unsupported type.  
Error 400 | The HTTP server returns an error response with status code 400. Check the response body for more details.  
  
## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
  
## Use the HTTP connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).
  * To understand how to handle JSON payloads as strings in HTTP Connectors tasks, see [Handle JSON payloads as strings in HTTP Connectors tasks](https://docs.cloud.google.com/application-integration/docs/json-in-subtask).



## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
