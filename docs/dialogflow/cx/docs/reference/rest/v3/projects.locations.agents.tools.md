---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools
title: REST Resource: projects.locations.agents.tools \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:22.162541+00:00
---

# REST Resource: projects.locations.agents.tools  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.tools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Tool
    * JSON representation
    * OpenApiTool
      * JSON representation
    * Authentication
      * JSON representation
    * ApiKeyConfig
      * JSON representation
    * RequestLocation
    * OAuthConfig
      * JSON representation
    * OauthGrantType
    * ServiceAgentAuthConfig
      * JSON representation
    * ServiceAgentAuth
    * BearerTokenConfig
      * JSON representation
    * ServiceAccountAuthConfig
      * JSON representation
    * TLSConfig
      * JSON representation
    * CACert
      * JSON representation
    * ServiceDirectoryConfig
      * JSON representation
    * DataStoreTool
      * JSON representation
    * FallbackPrompt
    * FunctionTool
      * JSON representation
    * ToolType
  * Methods



## Resource: Tool

A tool provides a list of actions which are available to the `[Playbook](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook)` to attain its goal. A Tool consists of a description of the tool's usage and a specification of the tool which contains the schema and authentication information.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "toolType": enum ([ToolType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ToolType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "openApiSpec": {
        object ([OpenApiTool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.OpenApiTool))
      },
      "dataStoreSpec": {
        object ([DataStoreTool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.DataStoreTool))
      },
      "functionSpec": {
        object ([FunctionTool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.FunctionTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the Tool. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
`displayName` |  `string` Required. The human-readable name of the Tool, unique within an agent.  
`description` |  `string` Required. High level description of the Tool and its usage.  
`toolType` |  `enum (`[ToolType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ToolType)`)` Output only. The tool type.  
Specification of the Tool. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`openApiSpec` |  `object (`[OpenApiTool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.OpenApiTool)`)` OpenAPI specification of the Tool.  
`dataStoreSpec` |  `object (`[DataStoreTool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.DataStoreTool)`)` Data store search tool specification.  
`functionSpec` |  `object (`[FunctionTool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.FunctionTool)`)` Client side executed function specification.  
End of mutually exclusive fields.  
  
### OpenApiTool

An OpenAPI tool is a way to provide the Tool specifications in the Open API schema format.

JSON representation  
---  
      
    
    {
      "authentication": {
        object ([Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.Authentication))
      },
      "tlsConfig": {
        object ([TLSConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.TLSConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceDirectoryConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textSchema": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`authentication` |  `object (`[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.Authentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TLSConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.TLSConfig)`)` Optional. TLS configuration for the HTTPS verification.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
Schema representation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textSchema` |  `string` Required. The OpenAPI schema specified as a text.  
End of mutually exclusive fields.  
  
### Authentication

Authentication information required for API calls

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ApiKeyConfig))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.OAuthConfig))
      },
      "serviceAgentAuthConfig": {
        object ([ServiceAgentAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceAgentAuthConfig))
      },
      "bearerTokenConfig": {
        object ([BearerTokenConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.BearerTokenConfig))
      },
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceAccountAuthConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The auth configuration. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`apiKeyConfig` |  `object (`[ApiKeyConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ApiKeyConfig)`)` Config for API key auth.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.OAuthConfig)`)` Config for OAuth.  
`serviceAgentAuthConfig` |  `object (`[ServiceAgentAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceAgentAuthConfig)`)` Config for [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent) auth.  
`bearerTokenConfig` |  `object (`[BearerTokenConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.BearerTokenConfig)`)` Config for bearer token auth.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceAccountAuthConfig)`)` Configuration for service account authentication.  
End of mutually exclusive fields.  
  
### ApiKeyConfig

Config for authentication with API key.

JSON representation  
---  
      
    
    {
      "keyName": string,
      "apiKey": string,
      "secretVersionForApiKey": string,
      "requestLocation": enum ([RequestLocation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.RequestLocation))
    }  
  
Fields  
---  
`keyName` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`apiKey` |  `string` Optional. The API key. If the `secretVersionForApiKey` field is set, this field will be ignored.  
`secretVersionForApiKey` |  `string` Optional. The name of the SecretManager secret version resource storing the API key. If this field is set, the `apiKey` field will be ignored. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`requestLocation` |  `enum (`[RequestLocation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.RequestLocation)`)` Required. Key location in the request.  
  
### RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Default value. This value is unused.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
### OAuthConfig

Config for authentication with OAuth.

JSON representation  
---  
      
    
    {
      "oauthGrantType": enum ([OauthGrantType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.OauthGrantType)),
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
`oauthGrantType` |  `enum (`[OauthGrantType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.OauthGrantType)`)` Required. OAuth grant types.  
`clientId` |  `string` Required. The client ID from the OAuth provider.  
`clientSecret` |  `string` Optional. The client secret from the OAuth provider. If the `secretVersionForClientSecret` field is set, this field will be ignored.  
`secretVersionForClientSecret` |  `string` Optional. The name of the SecretManager secret version resource storing the client secret. If this field is set, the `clientSecret` field will be ignored. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`tokenEndpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
### OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
### ServiceAgentAuthConfig

Config for auth using [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).

JSON representation  
---  
      
    
    {
      "serviceAgentAuth": enum ([ServiceAgentAuth](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceAgentAuth))
    }  
  
Fields  
---  
`serviceAgentAuth` |  `enum (`[ServiceAgentAuth](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.ServiceAgentAuth)`)` Optional. Indicate the auth token type generated from the [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). The generated token is sent in the Authorization header.  
  
### ServiceAgentAuth

Indicate the auth token type generated from the [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).

Enums  
---  
`SERVICE_AGENT_AUTH_UNSPECIFIED` | Service agent auth type unspecified. Default to ID_TOKEN.  
`ID_TOKEN` | Use [ID token](https://cloud.google.com/docs/authentication/token-types#id) generated from service agent. This can be used to access Cloud Function and Cloud Run after you grant Invoker role to `service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com`.  
`ACCESS_TOKEN` | Use [access token](https://cloud.google.com/docs/authentication/token-types#access) generated from service agent. This can be used to access other Google Cloud APIs after you grant required roles to `service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com`.  
  
### BearerTokenConfig

Config for authentication using bearer token.

JSON representation  
---  
      
    
    {
      "token": string,
      "secretVersionForToken": string
    }  
  
Fields  
---  
`token` |  `string` Optional. The text token appended to the text `Bearer` to the request Authorization header. [Session parameters reference](https://cloud.google.com/dialogflow/cx/docs/concept/parameter#session-ref) can be used to pass the token dynamically, e.g. `$session.params.parameter-id`.  
`secretVersionForToken` |  `string` Optional. The name of the SecretManager secret version resource storing the Bearer token. If this field is set, the `token` field will be ignored. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
  
### ServiceAccountAuthConfig

Configuration for authentication using a service account.

JSON representation  
---  
      
    
    {
      "serviceAccount": string
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used to authenticate the tool call. Dialogflow uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the tool request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the [Dialogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).  
  
### TLSConfig

The TLS configuration.

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CACert](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.CACert))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CACert](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.CACert)`)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
### CACert

The CA certificate.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "cert": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. The name of the allowed custom CA certificates. This can be used to disambiguate the custom CA certificates.  
`cert` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, Dialogflow will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command:
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
    

A base64-encoded string.  
  
### ServiceDirectoryConfig

Configuration for tools using Service Directory.

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/<ProjectID>/locations/<LocationID>/namespaces/<NamespaceID>/services/<ServiceID>`. `LocationID` of the service directory must be the same as the location of the agent.  
  
### DataStoreTool

A DataStoreTool is a way to provide specifications needed to search a list of data stores.

JSON representation  
---  
      
    
    {
      "dataStoreConnections": [
        {
          object ([DataStoreConnection](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DataStoreConnection))
        }
      ],
      "fallbackPrompt": {
        object ([FallbackPrompt](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.FallbackPrompt))
      }
    }  
  
Fields  
---  
`dataStoreConnections[]` |  `object (`[DataStoreConnection](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DataStoreConnection)`)` Required. List of data stores to search.  
`fallbackPrompt` |  `object (`[FallbackPrompt](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool.FallbackPrompt)`)` Required. Fallback prompt configurations to use.  
  
### FallbackPrompt

This type has no fields.

A FallbackPrompt is a way to provide specifications for the Data Store fallback prompt when generating responses.

### FunctionTool

A Function tool describes the functions to be invoked on the client side.

JSON representation  
---  
      
    
    {
      "inputSchema": {
        object
      },
      "outputSchema": {
        object
      }
    }  
  
Fields  
---  
`inputSchema` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The JSON schema is encapsulated in a `[google.protobuf.Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` to describe the input of the function. This input is a JSON object that contains the function's parameters as properties of the object.  
`outputSchema` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The JSON schema is encapsulated in a `[google.protobuf.Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` to describe the output of the function. This output is a JSON object that contains the function's parameters as properties of the object.  
  
### ToolType

Represents the type of the tool.

Enums  
---  
`TOOL_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`CUSTOMIZED_TOOL` | Customer provided tool.  
`BUILTIN_TOOL` | First party built-in tool created by Dialogflow which cannot be modified.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/create)`

|  Creates a `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/delete)`

|  Deletes a specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/get)`

|  Retrieves the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/list)`

|  Returns a list of `[Tools](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/patch)`

|  Update the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
