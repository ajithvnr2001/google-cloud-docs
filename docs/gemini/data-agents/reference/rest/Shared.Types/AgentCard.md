---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard/
title: AgentCard \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:44.283661+00:00
---

# AgentCard  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  AgentCard Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AgentInterface
    * JSON representation
  * AgentProvider
    * JSON representation
  * SecurityScheme
    * JSON representation
  * HTTPAuthSecurityScheme
    * JSON representation
  * OAuth2SecurityScheme
    * JSON representation
  * OAuthFlows
    * JSON representation
  * AuthorizationCodeOAuthFlow
    * JSON representation
  * ClientCredentialsOAuthFlow
    * JSON representation
  * ImplicitOAuthFlow
    * JSON representation
  * PasswordOAuthFlow
    * JSON representation
  * OpenIdConnectSecurityScheme
    * JSON representation
  * MutualTlsSecurityScheme
    * JSON representation
  * Security
    * JSON representation
  * StringList
    * JSON representation
  * AgentSkill
    * JSON representation
  * AgentCardSignature
    * JSON representation



AgentCard conveys key information: - Overall details (version, name, description, uses) - Skills; a set of actions/solutions the agent can perform - Default modalities/content types supported by the agent. - Authentication requirements Next ID: 19

JSON representation  
---  
      
    
    {
      "protocolVersion": string,
      "name": string,
      "description": string,
      "url": string,
      "preferredTransport": string,
      "additionalInterfaces": [
        {
          object ([AgentInterface](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentInterface))
        }
      ],
      "provider": {
        object ([AgentProvider](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentProvider))
      },
      "version": string,
      "documentationUrl": string,
      "capabilities": {
        object ([AgentCapabilities](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCapabilities))
      },
      "securitySchemes": {
        string: {
          object ([SecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#SecurityScheme))
        },
        ...
      },
      "security": [
        {
          object ([Security](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#Security))
        }
      ],
      "defaultInputModes": [
        string
      ],
      "defaultOutputModes": [
        string
      ],
      "skills": [
        {
          object ([AgentSkill](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentSkill))
        }
      ],
      "supportsAuthenticatedExtendedCard": boolean,
      "signatures": [
        {
          object ([AgentCardSignature](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentCardSignature))
        }
      ],
      "iconUrl": string
    }  
  
Fields  
---  
`protocolVersion` |  `string` The version of the A2A protocol this agent supports.  
`name` |  `string` A human readable name for the agent. Example: "Recipe Agent"  
`description` |  `string` A description of the agent's domain of action/solution space. Example: "Agent that helps users with recipes and cooking."  
`url` |  `string` A URL to the address the agent is hosted at. This represents the preferred endpoint as declared by the agent.  
`preferredTransport` |  `string` The transport of the preferred endpoint. If empty, defaults to JSONRPC.  
`additionalInterfaces[]` |  `object (`[AgentInterface](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentInterface)`)` Announcement of additional supported transports. Client can use any of the supported transports.  
`provider` |  `object (`[AgentProvider](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentProvider)`)` The service provider of the agent.  
`version` |  `string` The version of the agent. Example: "1.0.0"  
`documentationUrl` |  `string` A url to provide additional documentation about the agent.  
`capabilities` |  `object (`[AgentCapabilities](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCapabilities)`)` A2A Capability set supported by the agent.  
`securitySchemes` |  `map (key: string, value: object (`[SecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#SecurityScheme)`))` The security scheme details used for authenticating with this agent.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`security[]` |  `object (`[Security](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#Security)`)` protolint:disable REPEATED_FIELD_NAMES_PLURALIZED Security requirements for contacting the agent. This list can be seen as an OR of ANDs. Each object in the list describes one possible set of security requirements that must be present on a request. This allows specifying, for example, "callers must either use OAuth OR an API Key AND mTLS." Example: security { schemes { key: "oauth" value { list: ["read"] } } } security { schemes { key: "api-key" } schemes { key: "mtls" } }  
`defaultInputModes[]` |  `string` protolint:enable REPEATED_FIELD_NAMES_PLURALIZED The set of interaction modes that the agent supports across all skills. This can be overridden per skill. Defined as mime types.  
`defaultOutputModes[]` |  `string` The mime types supported as outputs from this agent.  
`skills[]` |  `object (`[AgentSkill](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentSkill)`)` Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
`supportsAuthenticatedExtendedCard` |  `boolean` Whether the agent supports providing an extended agent card when the user is authenticated, i.e. is the card from .well-known different than the card from v1.getCard.  
`signatures[]` |  `object (`[AgentCardSignature](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AgentCardSignature)`)` JSON Web Signatures computed for this AgentCard.  
`iconUrl` |  `string` An optional URL to an icon for the agent.  
  
## AgentInterface

Defines additional transport information for the agent.

JSON representation  
---  
      
    
    {
      "url": string,
      "transport": string,
      "tenant": string
    }  
  
Fields  
---  
`url` |  `string` The url this interface is found at.  
`transport` |  `string` The transport supported this url. This is an open form string, to be easily extended for many transport protocols. The core ones officially supported are JSONRPC, GRPC and HTTP+JSON.  
`tenant` |  `string` Tenant to be set in the request when calling the agent. Experimental, might still change for 1.0 release.  
  
## AgentProvider

Represents information about the service provider of an agent.

JSON representation  
---  
      
    
    {
      "url": string,
      "organization": string
    }  
  
Fields  
---  
`url` |  `string` The providers reference url Example: "https://ai.google.dev"  
`organization` |  `string` The providers organization name Example: "Google"  
  
## SecurityScheme

JSON representation  
---  
      
    
    {
    
      // Union field scheme can be only one of the following:
      "apiKeySecurityScheme": {
        object ([APIKeySecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/APIKeySecurityScheme))
      },
      "httpAuthSecurityScheme": {
        object ([HTTPAuthSecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#HTTPAuthSecurityScheme))
      },
      "oauth2SecurityScheme": {
        object ([OAuth2SecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#OAuth2SecurityScheme))
      },
      "openIdConnectSecurityScheme": {
        object ([OpenIdConnectSecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#OpenIdConnectSecurityScheme))
      },
      "mtlsSecurityScheme": {
        object ([MutualTlsSecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#MutualTlsSecurityScheme))
      }
      // End of list of possible types for union field scheme.
    }  
  
Fields  
---  
Union field `scheme`.`scheme` can be only one of the following:  
`apiKeySecurityScheme` |  `object (`[APIKeySecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/APIKeySecurityScheme)`)`  
`httpAuthSecurityScheme` |  `object (`[HTTPAuthSecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#HTTPAuthSecurityScheme)`)`  
`oauth2SecurityScheme` |  `object (`[OAuth2SecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#OAuth2SecurityScheme)`)`  
`openIdConnectSecurityScheme` |  `object (`[OpenIdConnectSecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#OpenIdConnectSecurityScheme)`)`  
`mtlsSecurityScheme` |  `object (`[MutualTlsSecurityScheme](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#MutualTlsSecurityScheme)`)`  
  
## HTTPAuthSecurityScheme

JSON representation  
---  
      
    
    {
      "description": string,
      "scheme": string,
      "bearerFormat": string
    }  
  
Fields  
---  
`description` |  `string` Description of this security scheme.  
`scheme` |  `string` The name of the HTTP Authentication scheme to be used in the Authorization header as defined in RFC7235. The values used SHOULD be registered in the IANA Authentication Scheme registry. The value is case-insensitive, as defined in RFC7235.  
`bearerFormat` |  `string` A hint to the client to identify how the bearer token is formatted. Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.  
  
## OAuth2SecurityScheme

JSON representation  
---  
      
    
    {
      "description": string,
      "flows": {
        object ([OAuthFlows](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#OAuthFlows))
      },
      "oauth2MetadataUrl": string
    }  
  
Fields  
---  
`description` |  `string` Description of this security scheme.  
`flows` |  `object (`[OAuthFlows](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#OAuthFlows)`)` An object containing configuration information for the flow types supported  
`oauth2MetadataUrl` |  `string` URL to the oauth2 authorization server metadata [RFC8414](https://datatracker.ietf.org/doc/html/rfc8414). TLS is required.  
  
## OAuthFlows

JSON representation  
---  
      
    
    {
    
      // Union field flow can be only one of the following:
      "authorizationCode": {
        object ([AuthorizationCodeOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AuthorizationCodeOAuthFlow))
      },
      "clientCredentials": {
        object ([ClientCredentialsOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#ClientCredentialsOAuthFlow))
      },
      "implicit": {
        object ([ImplicitOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#ImplicitOAuthFlow))
      },
      "password": {
        object ([PasswordOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#PasswordOAuthFlow))
      }
      // End of list of possible types for union field flow.
    }  
  
Fields  
---  
Union field `flow`.`flow` can be only one of the following:  
`authorizationCode` |  `object (`[AuthorizationCodeOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#AuthorizationCodeOAuthFlow)`)`  
`clientCredentials` |  `object (`[ClientCredentialsOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#ClientCredentialsOAuthFlow)`)`  
`implicit` |  `object (`[ImplicitOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#ImplicitOAuthFlow)`)`  
`password` |  `object (`[PasswordOAuthFlow](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#PasswordOAuthFlow)`)`  
  
## AuthorizationCodeOAuthFlow

JSON representation  
---  
      
    
    {
      "authorizationUrl": string,
      "tokenUrl": string,
      "refreshUrl": string,
      "scopes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`authorizationUrl` |  `string` The authorization URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS  
`tokenUrl` |  `string` The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`refreshUrl` |  `string` The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`scopes` |  `map (key: string, value: string)` The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ClientCredentialsOAuthFlow

JSON representation  
---  
      
    
    {
      "tokenUrl": string,
      "refreshUrl": string,
      "scopes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`tokenUrl` |  `string` The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`refreshUrl` |  `string` The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`scopes` |  `map (key: string, value: string)` The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ImplicitOAuthFlow

JSON representation  
---  
      
    
    {
      "authorizationUrl": string,
      "refreshUrl": string,
      "scopes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`authorizationUrl` |  `string` The authorization URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS  
`refreshUrl` |  `string` The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`scopes` |  `map (key: string, value: string)` The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## PasswordOAuthFlow

JSON representation  
---  
      
    
    {
      "tokenUrl": string,
      "refreshUrl": string,
      "scopes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`tokenUrl` |  `string` The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`refreshUrl` |  `string` The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`scopes` |  `map (key: string, value: string)` The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## OpenIdConnectSecurityScheme

JSON representation  
---  
      
    
    {
      "description": string,
      "openIdConnectUrl": string
    }  
  
Fields  
---  
`description` |  `string` Description of this security scheme.  
`openIdConnectUrl` |  `string` Well-known URL to discover the [[OpenID-Connect-Discovery]] provider metadata.  
  
## MutualTlsSecurityScheme

JSON representation  
---  
      
    
    {
      "description": string
    }  
  
Fields  
---  
`description` |  `string` Description of this security scheme.  
  
## Security

JSON representation  
---  
      
    
    {
      "schemes": {
        string: {
          object ([StringList](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#StringList))
        },
        ...
      }
    }  
  
Fields  
---  
`schemes` |  `map (key: string, value: object (`[StringList](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#StringList)`))` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## StringList

protolint:disable REPEATED_FIELD_NAMES_PLURALIZED

JSON representation  
---  
      
    
    {
      "list": [
        string
      ]
    }  
  
Fields  
---  
`list[]` |  `string`  
  
## AgentSkill

AgentSkill represents a unit of action/solution that the agent can perform. One can think of this as a type of highly reliable solution that an agent can be tasked to provide. Agents have the autonomy to choose how and when to use specific skills, but clients should have confidence that if the skill is defined that unit of action can be reliably performed.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "description": string,
      "tags": [
        string
      ],
      "examples": [
        string
      ],
      "inputModes": [
        string
      ],
      "outputModes": [
        string
      ],
      "security": [
        {
          object ([Security](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#Security))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Unique identifier of the skill within this agent.  
`name` |  `string` A human readable name for the skill.  
`description` |  `string` A human (or llm) readable description of the skill details and behaviors.  
`tags[]` |  `string` A set of tags for the skill to enhance categorization/utilization. Example: ["cooking", "customer support", "billing"]  
`examples[]` |  `string` A set of example queries that this skill is designed to address. These examples should help the caller to understand how to craft requests to the agent to achieve specific goals. Example: ["I need a recipe for bread"]  
`inputModes[]` |  `string` Possible input modalities supported.  
`outputModes[]` |  `string` Possible output modalities produced  
`security[]` |  `object (`[Security](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCard#Security)`)` protolint:disable REPEATED_FIELD_NAMES_PLURALIZED Security schemes necessary for the agent to leverage this skill. As in the overall AgentCard.security, this list represents a logical OR of security requirement objects. Each object is a set of security schemes that must be used together (a logical AND). protolint:enable REPEATED_FIELD_NAMES_PLURALIZED  
  
## AgentCardSignature

AgentCardSignature represents a JWS signature of an AgentCard. This follows the JSON format of an RFC 7515 JSON Web Signature (JWS).

JSON representation  
---  
      
    
    {
      "protected": string,
      "signature": string,
      "header": {
        object
      }
    }  
  
Fields  
---  
`protected` |  `string` Required. The protected JWS header for the signature. This is always a base64url-encoded JSON object. Required.  
`signature` |  `string` Required. The computed signature, base64url-encoded. Required.  
`header` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The unprotected JWS header values.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
