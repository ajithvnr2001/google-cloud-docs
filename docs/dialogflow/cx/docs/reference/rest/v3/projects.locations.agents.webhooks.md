---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks
title: REST Resource: projects.locations.agents.webhooks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:25.139396+00:00
---

# REST Resource: projects.locations.agents.webhooks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.webhooks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Webhook
    * JSON representation
    * GenericWebService
      * JSON representation
    * SecretVersionHeaderValue
      * JSON representation
    * OAuthConfig
      * JSON representation
    * ServiceAgentAuth
    * ServiceAccountAuthConfig
      * JSON representation
    * WebhookType
    * HttpMethod
    * ServiceDirectoryConfig
      * JSON representation
  * Methods



## Resource: Webhook

Webhooks host the developer's business logic. During a session, webhooks allow the developer to use the data extracted by Dialogflow's natural language processing to generate dynamic responses, validate collected data, or trigger actions on the backend.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "timeout": string,
      "disabled": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "genericWebService": {
        object ([GenericWebService](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.GenericWebService))
      },
      "serviceDirectory": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.ServiceDirectoryConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the webhook. Required for the `[Webhooks.UpdateWebhook](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/patch#google.cloud.dialogflow.cx.v3.Webhooks.UpdateWebhook)` method. `[Webhooks.CreateWebhook](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/create#google.cloud.dialogflow.cx.v3.Webhooks.CreateWebhook)` populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.  
`displayName` |  `string` Required. The human-readable name of the webhook, unique within the agent.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`disabled` |  `boolean` Indicates whether the webhook is disabled.  
Required. The webhook configuration. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`genericWebService` |  `object (`[GenericWebService](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.GenericWebService)`)` Configuration for a generic web service.  
`serviceDirectory` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.ServiceDirectoryConfig)`)` Configuration for a [Service Directory](https://cloud.google.com/service-directory) service.  
End of mutually exclusive fields.  
  
### GenericWebService

Represents configuration for a generic web service.

JSON representation  
---  
      
    
    {
      "uri": string,
      "username": string,
      "password": string,
      "secretVersionForUsernamePassword": string,
      "requestHeaders": {
        string: string,
        ...
      },
      "secretVersionsForRequestHeaders": {
        string: {
          object ([SecretVersionHeaderValue](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.SecretVersionHeaderValue))
        },
        ...
      },
      "allowedCaCerts": [
        string
      ],
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.OAuthConfig))
      },
      "serviceAgentAuth": enum ([ServiceAgentAuth](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.ServiceAgentAuth)),
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.ServiceAccountAuthConfig))
      },
      "webhookType": enum ([WebhookType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.WebhookType)),
      "httpMethod": enum ([HttpMethod](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.HttpMethod)),
      "requestBody": string,
      "parameterMapping": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`uri` |  `string` Required. The webhook URI for receiving POST requests. It must use https protocol.  
`username  
**(deprecated)**` |  `string` This item is deprecated!The user name for HTTP Basic authentication.  
`password  
**(deprecated)**` |  `string` This item is deprecated!The password for HTTP Basic authentication.  
`secretVersionForUsernamePassword` |  `string` Optional. The SecretManager secret version resource storing the username:password pair for HTTP Basic authentication. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`requestHeaders` |  `map (key: string, value: string)` The HTTP request headers to send together with webhook requests.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`secretVersionsForRequestHeaders` |  `map (key: string, value: object (`[SecretVersionHeaderValue](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.SecretVersionHeaderValue)`))` Optional. The HTTP request headers to send together with webhook requests. Header values are stored in SecretManager secret versions.When the same header name is specified in both `requestHeaders` and `secretVersionsForRequestHeaders`, the value in `secretVersionsForRequestHeaders` will be used.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`allowedCaCerts[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, Dialogflow will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command,
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
    

A base64-encoded string.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.OAuthConfig)`)` Optional. The OAuth configuration of the webhook. If specified, Dialogflow will initiate the OAuth client credential flow to exchange an access token from the 3rd party platform and put it in the auth header.  
`serviceAgentAuth` |  `enum (`[ServiceAgentAuth](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.ServiceAgentAuth)`)` Optional. Indicate the auth token type generated from the [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). The generated token is sent in the Authorization header.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.ServiceAccountAuthConfig)`)` Optional. Configuration for service account authentication.  
`webhookType` |  `enum (`[WebhookType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.WebhookType)`)` Optional. Type of the webhook.  
`httpMethod` |  `enum (`[HttpMethod](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.HttpMethod)`)` Optional. HTTP method for the flexible webhook calls. Standard webhook always uses POST.  
`requestBody` |  `string` Optional. Defines a custom JSON object as request body to send to flexible webhook.  
`parameterMapping` |  `map (key: string, value: string)` Optional. Maps the values extracted from specific fields of the flexible webhook response into session parameters. - Key: session parameter name - Value: field path in the webhook responseAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### SecretVersionHeaderValue

Represents the value of an HTTP header stored in a SecretManager secret version.

JSON representation  
---  
      
    
    {
      "secretVersion": string
    }  
  
Fields  
---  
`secretVersion` |  `string` Required. The SecretManager secret version resource storing the header value. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
  
### OAuthConfig

Represents configuration of OAuth client credential flow for 3rd party API authentication.

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string,
      "secretVersionForClientSecret": string,
      "tokenEndpoint": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`clientId` |  `string` Required. The client ID provided by the 3rd party platform.  
`clientSecret` |  `string` Optional. The client secret provided by the 3rd party platform.  
`secretVersionForClientSecret` |  `string` Optional. The name of the SecretManager secret version resource storing the client secret. If this field is set, the `clientSecret` field will be ignored. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`tokenEndpoint` |  `string` Required. The token endpoint provided by the 3rd party platform to exchange an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
### ServiceAgentAuth

Indicate the auth token type generated from the [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).

Enums  
---  
`SERVICE_AGENT_AUTH_UNSPECIFIED` | Service agent auth type unspecified. Default to ID_TOKEN.  
`NONE` | No token used.  
`ID_TOKEN` | Use [ID token](https://cloud.google.com/docs/authentication/token-types#id) generated from service agent. This can be used to access Cloud Function and Cloud Run after you grant Invoker role to `service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com`.  
`ACCESS_TOKEN` | Use [access token](https://cloud.google.com/docs/authentication/token-types#access) generated from service agent. This can be used to access other Google Cloud APIs after you grant required roles to `service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com`.  
  
### ServiceAccountAuthConfig

Configuration for authentication using a service account.

JSON representation  
---  
      
    
    {
      "serviceAccount": string
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used to authenticate the webhook call. Dialogflow uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the webhook request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the [Dialogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).  
  
### WebhookType

Represents the type of webhook configuration.

Enums  
---  
`WEBHOOK_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`STANDARD` | Represents a standard webhook.  
`FLEXIBLE` | Represents a flexible webhook.  
  
### HttpMethod

HTTP method to use when calling webhooks.

Enums  
---  
`HTTP_METHOD_UNSPECIFIED` | HTTP method not specified.  
`POST` | HTTP POST Method.  
`GET` | HTTP GET Method.  
`HEAD` | HTTP HEAD Method.  
`PUT` | HTTP PUT Method.  
`DELETE` | HTTP DELETE Method.  
`PATCH` | HTTP PATCH Method.  
`OPTIONS` | HTTP OPTIONS Method.  
  
### ServiceDirectoryConfig

Represents configuration for a [Service Directory](https://cloud.google.com/service-directory) service.

JSON representation  
---  
      
    
    {
      "service": string,
      "genericWebService": {
        object ([GenericWebService](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.GenericWebService))
      }
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/<ProjectID>/locations/<LocationID>/namespaces/<NamespaceID>/services/<ServiceID>`. `Location ID` of the service directory must be the same as the location of the agent.  
`genericWebService` |  `object (`[GenericWebService](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.GenericWebService)`)` Generic Service configuration of this webhook.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/create)`

|  Creates a webhook in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/delete)`

|  Deletes the specified webhook.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/get)`

|  Retrieves the specified webhook.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/list)`

|  Returns the list of all webhooks in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/patch)`

|  Updates the specified webhook.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
