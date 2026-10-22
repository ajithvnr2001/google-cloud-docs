---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool/
title: Playbook tools \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:07.366105+00:00
---

# Playbook tools  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook tools Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Generative AI App Builder still refers to playbooks as **agents**. This will be updated to **playbook** soon in the console.

Using tools, you can connect playbooks to external systems. These systems can augment the knowledge of playbooks and empower them to execute complex tasks efficiently.

You can use built-in tools or build customized tools to suit your requirements.

## Tool testing

Once you have created a tool, you can use the tool testing feature to verify that it works. When viewing a tool, click the **Test** button above the tool pane. This opens the tool for input in the simulator. Provide tool input, then click **View Output** to verify the correct tool output.

You can also use the tool testing feature when you add a tool to an example.

## Built-in tools

Built-in tools are hosted by Google. You can activate these tools in agents without the need for manual configuration.

The supported built-in tools are:

  * `Code Interpreter`: A Google first-party tool that combines the capability of code generation and code execution and allows the user to perform various tasks, including: data analysis, data visualization, text processing, solving equations or optimization problems.



Your agent is optimized to determine how and when these tools should be invoked, but you can provide additional examples to fit your use cases.

Examples should have a schema like the following:
    
    
    {
      "toolUse": {
        "tool": "projects/PROJECT_ID/locations/LOCATION_ID/agents/AGENT_ID/tools/df-code-interpreter-tool",
        "action": "generate_and_execute",
        "inputParameters": [
          {
            "name": "generate_and_execute input",
            "value": "4 + 4"
          }
        ],
        "outputParameters": [
          {
            "name": "generate_and_execute output",
            "value": {
              "output_files": [
                {
                  "name": "",
                  "contents": ""
                }
              ],
              "execution_result": "8",
              "execution_error": "",
              "generated_code": "GENERATED_CODE"
            }
          }
        ]
      }
    }
    

## OpenAPI tools

An agent can connect to an external API using an OpenAPI tool by providing the [OpenAPI](https://www.openapis.org/) schema. By default, the agent will call the API on your behalf. 

You can test the tool is set up correctly using the Test tool feature available on the tool page. This feature is also available in the example view when you add a tool invocation to the example.

Alternatively, you can execute OpenAPI tools on the client side.

Example schema:
    
    
    openapi: 3.0.0
    info:
      title: Simple Pets API
      version: 1.0.0
    servers:
      - url: 'https://api.pet-service-example.com/v1'
    paths:
      /pets/{petId}:
        get:
          summary: Return a pet by ID.
          operationId: getPet
          parameters:
            - in: path
              name: petId
              required: true
              description: Pet id
              schema:
                type: integer
          responses:
            200:
              description: OK
      /pets:
        get:
          summary: List all pets
          operationId: listPets
          parameters:
            - name: petName
              in: query
              required: false
              description: Pet name
              schema:
                type: string
            - name: label
              in: query
              description: Pet label
              style: form
              explode: true
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: X-OWNER
              in: header
              description: Optional pet owner provided in the HTTP header
              required: false
              schema:
                type: string
            - name: X-SESSION
              in: header
              description: Dialogflow session id
              required: false
              schema:
                $ref: "@dialogflow/sessionId"
          responses:
            '200':
              description: An array of pets
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/Pet'
        post:
          summary: Create a new pet
          operationId: createPet
          requestBody:
            description: Pet to add to the store
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Pet'
          responses:
            '201':
              description: Pet created
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Pet'
    components:
      schemas:
        Pet:
          type: object
          required:
            - id
            - name
          properties:
            id:
              type: integer
              format: int64
            name:
              type: string
            owner:
              type: string
            label:
              type: array
              items:
                type: string
    

You can optionally use the internal schema reference `@dialogflow/sessionId` as parameter schema type. With this parameter schema type, the Dialogflow session ID for the current conversation will be supplied as a parameter value.

For example:
    
    
    - name: X-SESSION
       in: header
       description: Dialogflow session id
       required: false
       schema:
         $ref: "@dialogflow/sessionId"
    

### OpenAPI tool limitations

The following limitations apply:

  * Supported parameter types are `path`, `query`, `header`. The `cookie` parameter type is not supported.
  * Parameters defined by OpenAPI schema support the following data types: `string`, `number`, `integer`, `boolean`, `array`. The `object` type is not supported.
  * You can't specify query parameters in the console example editor.
  * Request and response body must be empty or JSON.



### OpenAPI tool schema generation

When providing a schema, you can use the **Use Gemini** button to use generative AI to create your schema.

You can provide the following to guide the generation:

  * A URL of request
  * An HTTP method (GET, POST, etc)
  * Sample input
  * Sample output
  * A text prompt describing the tool



Once that is generated, you can edit as needed and add additional URLs and methods manually.

### OpenAPI tool API authentication

The following authentication options are supported when calling an external API.

#### Dialogflow Service Agent auth

Dialogflow can generate an [ID token](https://docs.cloud.google.com/docs/authentication/token-types#id) using [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). The token is added in the authorization HTTP header when Dialogflow calls an external API.

An ID token can be used to access Cloud Run functions and Cloud Run services after you grant the [roles/cloudfunctions.invoker](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker) and [roles/run.invoker](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker) roles to **service- agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com**. If the Cloud Run functions and Cloud Run services are in the same [resource project](https://docs.cloud.google.com/dialogflow/cx/docs/concept/multi-project), you don't need additional Identity and Access Management permission to call them.

#### Service Account auth

Service accounts can be used to authenticate tool requests to any Google APIs which support it.

If you haven't already, [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).

Because service accounts are principals, they can access resources in your project by [granting it a role](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-identities), just like you would for any other principal. The service account email will be used to [generate an access token](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials) which will be sent in the `Authorization` header of the tool request.

The user who is configuring the tool to use service accounts must have the following permissions:

  * `roles/iam.serviceAccountUser`



In order for Dialogflow CX to generate tokens, the [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent) must have the following permissions:

  * `roles/iam.serviceAccountTokenCreator`



The service account must also have permissions to access the service that is hosting the tool.

**Note:** If you are trying to use service accounts across multiple projects, ensure that your [organization policy supports it](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project). Both the permissions need to be granted in the project which contains the service account.

#### API key

  * You can configure API key authentication by providing the key name, request location (header or query string) and API key so that Dialogflow passes the API key in the request.
  * We recommend you to supply your API key using Secret Manager. After Aug 15, 2025, exported agents will no longer contain raw value API keys.



#### OAuth

  * The OAuth client credentials flow is supported for server-to-server authentication: 
    * This flow can be used if the Generative AI App Builder is the resource owner and no end-user authorization is needed.
    * The client ID, client secret, and token endpoint from an OAuth provider need to be configured in Dialogflow.
    * We recommend that you supply your client secret using Secret Manager. After Aug 15, 2025, exported agents will no longer contain raw value client secrets.
    * Dialogflow exchanges an OAuth access token from an OAuth provider and passes it in the auth header of the request.



#### Bearer Token

  * You can configure Bearer authentication to dynamically pass the Bearer token from the client. This token is included in the auth header of the request.
  * When setting up tool authentication, you can designate a session parameter to act as the Bearer token. For example, use `$session.params.<parameter-name-for-token>` to specify the token.
  * At runtime, assign the Bearer token to the session parameter:
        
        DetectIntentRequest {
          ...
          query_params {
            parameters {
              <parameter-name-for-token>: <the-auth-token>
            }
          }
          ...
        }
        

  * If you need to configure a static token instead of fetching the token from a session parameter, we recommend you to supply your token using Secret Manager. After Aug 15, 2025, exported agents will no longer contain raw value Bearer tokens.




#### Mutual TLS authentication

  * See the [Mutual TLS authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls) documentation.
  * Custom client certificates are supported. You can set up client certificates at the agent level under the security tab in agent settings. The certificate (PEM format) and private key (PEM format) are required fields. Once set, this client certificate will be used during mutual TLS for all tools and webhooks.



#### Custom CA certificate

  * See the [Custom CA certificates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca) documentation.



#### Secret Manager authentication

If you use OAuth, API key, or Bearer token, you can store the credentials as **secrets** using [Secret Manager](https://docs.cloud.google.com/secret-manager). Here are the necessary steps to authenticate your tool using secrets:

  1. [Create your secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) if you don't have one already.
  2. Grant [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent) the [**Secret Manager Secret Accessor**](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) role on the new secret.
  3. Copy your credential into the clipboard.
  4. [Add a new secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) to your secret. Paste your credential as the secret value. 
     * Omit any newline character at the end.
  5. Copy the name of the secret version you just added. The name format is `projects/{project_id}/secrets/{secret_id}/versions/{version_id}"`.
  6. Open the tool edit screen, then: 
     * If you use OAuth, select **OAuth** as the **Authentication type** , then click **Secret version** under **Client secret** and paste the secret version name to the **Secret version** input box.
     * If you use API key, select **API key** as the **Authentication type** , then click **Secret version** under **API key**. Paste the secret version name to the **Secret version** input box.
     * If you use Bearer token, select **Bearer token** as the **Authentication type** , then click **Secret version** under **Bearer token**. Paste the secret version name to the **Secret version** input box.
  7. Click **Save**.

**Note:** We only support global Secret Manager. Usage of regional secrets is unsupported.

### OpenAPI tool private network access

OpenAPI tool integrates with [Service Directory private network access](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview), so it can connect to API targets inside your VPC network. This keeps the traffic within the Google Cloud network and enforces [IAM](https://docs.cloud.google.com/iam/docs/overview) and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

**Note:** Service Directory endpoints created by [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#configure-sd-manual) are not supported.

To set up an OpenAPI tool targeting a private network:

  1. Follow [Service Directory private network configuration](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access) to configure your VPC network and Service Directory endpoint.
  2. The **Dialogflow Service Agent** [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) with the following address must exist for your agent project: 
         
         service-agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com

Grant the **Dialogflow Service Agent** service account the following Identity and Access Management roles: 
     * `servicedirectory.viewer` of the Service Directory project
     * `servicedirectory.pscAuthorizedService` of the network project
  3. Provide Service Directory Service along with the OpenAPI schema and optional authentication information when creating the tool.



### OpenAPI tool session parameter access

Open API tool inputs are derived from the users conversation with the LLM using the schema as a guide. In some situations, inputs may need to be derived from session parameters collected during a flow or provided as a query parameter input along with the user input.

The session parameter that needs to be passed as an input can be specified as:
    
    
         parameters:
           - in: query
             name: petId
             required: true
             description: Pet id
             schema:
               type: integer
               x-agent-input-parameter: petId # Reads from the $session.params.petId
           - in: header
             name: X-other
             schema:
               type: string
               x-agent-input-parameter: $request.payload.header # Reads from the header specified in the request payload input
         requestBody:
           required: false
           content:
             application/json:
               schema:
                 type: object
                 properties:
                   name:
                     type: string
                     x-agent-input-parameter: petName # Reads from the $session.params.petName
                     description: Name of the person to greet (optional).
                   breed:
                     type: string
                     description: Bread of the pet.
    

If no such session parameter is available, the LLM generated input will be passed to the tool.

### OpenAPI tool default values

The Open API schema can be used to specify default values. The default values are only used if there is no LLM generated input value or session parameter based input value for that parameter or property.

The default values can be specified as part of the schema as follows:
    
    
         parameters:
           - in: query
             name: zipcode
             required: true
             description: Zip code to search for
             schema:
               type: integer
               default: 94043
         requestBody:
           content:
             application/json:
               schema:
                 type: object
                 properties:
                   breed:
                     type: string
                     description: Bread of the pet.
                   page_size:
                     type: integer
                     description: Number of pets to return.
                     default: 10
    

If no LLM generated value, session parameter value or default value is present, the input will be unspecified.

## Data store tools

For information about using data store tools with a playbook, see the [data store tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler) documentation.

## Connector tools

Connector tools can be used by an agent to perform actions using your Connections configured in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview). Each connector tool is configured with a single Connection and one or more actions. If needed, multiple tools can be created for a single Connection to group different actions together for your agent to use.

The connector tool supports the following [Connector types](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors):

  * [AlloyDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/alloydb/configure)
  * [Asana](https://docs.cloud.google.com/integration-connectors/docs/connectors/asana/configure)
  * [Azure AD (Entra ID)](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuread/configure)
  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Box](https://docs.cloud.google.com/integration-connectors/docs/connectors/box/configure)
  * [Cloud Search](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_cloud_search/configure)
  * [Cloud Spanner](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudspanner/configure)
  * [Cloud SQL - MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)
  * [Cloud SQL - PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)
  * [Cloud SQL - SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure)
  * [Cloud Storage](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure)
  * [Cloud Translation](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_translate/configure)
  * [Confluence](https://docs.cloud.google.com/integration-connectors/docs/connectors/confluence/configure)
  * [Couchbase](https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure)
  * [DocuSign](https://docs.cloud.google.com/integration-connectors/docs/connectors/docusign/configure)
  * [Dropbox](https://docs.cloud.google.com/integration-connectors/docs/connectors/dropbox/configure)
  * [Dynamics 365](https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365/configure)
  * [Elasticsearch](https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure)
  * [Email](https://docs.cloud.google.com/integration-connectors/docs/connectors/email/configure)
  * [Enterprise License Manager](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_enterprise_license_manager/configure)
  * [Firestore](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_firestore/configure)
  * [FreshBooks](https://docs.cloud.google.com/integration-connectors/docs/connectors/freshbooks/configure)
  * [FTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/ftp/configure)
  * [GitHub](https://docs.cloud.google.com/integration-connectors/docs/connectors/github/configure)
  * [Gmail](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_gmail/configure)
  * [Google Analytics](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_analytics/configure)
  * [Google Calendar](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_calendar/configure)
  * [Google Classroom](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_classroom/configure)
  * [Google Cloud Natural Language](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_natural_language/configure)
  * [Google Contacts](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_contacts/configure)
  * [Google Docs](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_docs/configure)
  * [Google Forms](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_forms/configure)
  * [Google Sheets](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_sheets/configure)
  * [Google Slides](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_slides/configure)
  * [Greenplum](https://docs.cloud.google.com/integration-connectors/docs/connectors/greenplum/configure)
  * [Instagram](https://docs.cloud.google.com/integration-connectors/docs/connectors/instagram/configure)
  * [Jira Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure)
  * [Jira Service Management](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiraservicemanagement/configure)
  * [Kintone](https://docs.cloud.google.com/integration-connectors/docs/connectors/kintone/configure)
  * [Magento](https://docs.cloud.google.com/integration-connectors/docs/connectors/magento/configure)
  * [Mailchimp](https://docs.cloud.google.com/integration-connectors/docs/connectors/mailchimp/configure)
  * [MariaDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/mariadb/configure)
  * [Meta Ads](https://docs.cloud.google.com/integration-connectors/docs/connectors/metaads/configure)
  * [Microsoft Teams](https://docs.cloud.google.com/integration-connectors/docs/connectors/msteams/configure)
  * [Monday](https://docs.cloud.google.com/integration-connectors/docs/connectors/monday/configure)
  * [MongoDB (version 2)](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure)
  * [Neo4j](https://docs.cloud.google.com/integration-connectors/docs/connectors/neo4j/configure)
  * [OneDrive](https://docs.cloud.google.com/integration-connectors/docs/connectors/onedrive/configure)
  * [Oracle DB (version 2](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure)
  * [PayPal](https://docs.cloud.google.com/integration-connectors/docs/connectors/paypal/configure)
  * [PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)
  * [Salesforce](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)
  * [Salesforce Marketing Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforcemarketingcloud/configure)
  * [SAP HANA](https://docs.cloud.google.com/integration-connectors/docs/connectors/saphana/configure)
  * [SAP SuccessFactors](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapsuccessfactors/configure)
  * [ServiceNow](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure)
  * [SharePoint](https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure)
  * [Shopify (version 1](https://docs.cloud.google.com/integration-connectors/docs/connectors/shopify/configure)
  * [Slack](https://docs.cloud.google.com/integration-connectors/docs/connectors/slack/configure)
  * [Stripe](https://docs.cloud.google.com/integration-connectors/docs/connectors/stripe/configure)
  * [Trello](https://docs.cloud.google.com/integration-connectors/docs/connectors/trello/configure)
  * [WordPress](https://docs.cloud.google.com/integration-connectors/docs/connectors/wordpress/configure)
  * [Workday](https://docs.cloud.google.com/integration-connectors/docs/connectors/workday/configure)
  * [Zendesk](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure)



Examples should be used to enhance the agent use of connector tools by demonstrating how the agent should call the tool and use the response.

### Create a connection

To create a connection and connect it to your agent, you can navigate to the **Tools > Create**, select the **Connector** tool type, your chosen connector type, and use the **Create Connection** button. This will navigate you to Integration Connectors creation with a number of fields pre-filled.

Alternatively, you can navigate to Integration Connectors and follow the [instructions to create a connection](https://docs.cloud.google.com/integration-connectors/docs/createconnection).

**Note:** Connections must be in the same location as your agent in order to use them to create a connector tool. Support for using connector tools in multi-region agents is coming soon (Integration Connectors does not support multi-region Connections).

### Connector actions

For each connector tool, there are two types of actions that can be made available to your agent (see [Entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) for more information):

  1. **Entity CRUD operations**  
  
Each of your Connections have "entities" corresponding to the objects of that data source (for BigQuery, these are tables; for Salesforce, these are objects, like 'Order' or 'Case').  
  
You can perform CRUD operations on each entity:  


     * **Create** : creates an entity with specified field values  

     * **List** : filter-based search of entity instances  

     * **Update** : filter-based method for altering entity field values  

     * **Delete** : deletes an entity  

     * **Get** retrieves a single entity using the entityId  

**Note:** The Get operation can only be used to fetch a single record from an entity that has a primary key. It is often more practical to use the List operation with a [filterClause](https://docs.cloud.google.com/application-integration/docs/connectors-task#filter) to retrieve an entity.

Learn more about entity CRUD operations details in the [Connectors docs](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop).

  2. **Connector-specific actions**  
  
Many Connectors support an ['ExecuteCustomQuery'](https://docs.cloud.google.com/integration-connectors/docs/examples/execute-custom-query) action, which allows for executing a SQL query against the data source, where each of the data source entities can be referenced as tables. See this list for [supported connectors](https://docs.cloud.google.com/integration-connectors/docs/examples/execute-custom-query).  
  
Additional actions differ based on the connector type - for example, see the [BigQuery connector actions](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure#actions) or the [Salesforce connector actions](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure#actions).




### Configuring input/output fields for CRUD operations

By selecting specific input or output fields for your connector tool action to use, you can limit the complexity of these actions for the agent.

For example, if you only need to create an entity with a subset of its fields, configuring this set of fields in your action simplifies the action for the agent.

Specifying a set of output fields reduces the tool response size (helpful if token limits are a concern) and simplifies the agent's handling of the output by exposing only the relevant fields.

### Authentication

If the connection you're using is configured to allow [authentication override](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override), then the tool can be configured to pass through credentials from specified session parameters.

You as the agent builder are responsible for how these credentials are populated to the session parameters and the tool will automatically pass them through to the data source to use for authentication when the tool's actions are called.

## Function tools

If you have functionality accessible by your client code, but not accessible by OpenAPI tools, you can use function tools. Function tools are always executed on the client side, not by the agent.

The process is as follows:

  1. Your client code sends a detect intent request.
  2. The agent detects that a function tool is required, and the detect intent response contains the name of the tool along with input arguments. This session is paused until another detect intent request is received with the tool result.
  3. Your client code calls the tool.
  4. Your client code sends another detect intent request that provides the tool result as output arguments.



The following example shows the input and output schema of a function tool:
    
    
    {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The city and state, for example, San Francisco, CA"
        }
      },
      "required": [
        "location"
      ]
    }
    
    
    
    {
      "type": "object",
      "properties": {
        "temperature": {
          "type": "number",
          "description": "The temperature"
        }
      }
    }
    

The following example shows the initial detect intent request and response using REST:
    
    
    HTTP method and URL:
    POST https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION_ID/agents/AGENT_ID/sessions/SESSION_ID:detectIntent
    {
      "queryInput": {
        "text": {
          "text": "what is the weather in Mountain View"
        },
        "languageCode": "en"
      }
    }
    
    
    
    {
      "queryResult": {
        "text": "what is the weather in Mountain View",
        "languageCode": "en",
        "responseMessages": [
          {
            "source": "VIRTUAL_AGENT",
            "toolCall": {
              "tool": "<tool-resource-name>",
              "action": "get-weather-tool",
              "inputParameters": {
                "location": "Mountain View"
              }
            }
          }
        ]
      }
    }
    

The following example shows the second detect intent request, which provides the tool result:
    
    
    {
      "queryInput": {
        "toolCallResult": {
          "tool": "<tool-resource-name>",
          "action": "get-weather-tool",
          "outputParameters": {
            "temperature": 28.0
          }
        },
        "languageCode": "en"
      }
    }
    

## Client side execution

Like function tools, OpenAPI and data store tools can be executed on the client side by applying an API override when interacting with the session.

For example:
    
    
    DetectIntentRequest {
      ...
      query_params {
        playbook_state_override {
          playbook_execution_mode: ALWAYS_CLIENT_EXECUTION
        }
      }
      ...
    }
    

The process is the following:

  1. Your client code sends a detect intent request that specifies client execution.
  2. The agent detects that a tool is required, and the detect intent response contains the name of the tool along with input arguments. This session is paused until another detect intent request is received with the tool result.
  3. Your client code calls the tool.
  4. Your client code sends another detect intent request that provides the tool result as output arguments.



[ Previous arrow_back  Playbook parameters  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter)

[ Next Playbook settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/playbook-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
