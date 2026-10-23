---
url: https://docs.cloud.google.com/endpoints/docs/openapi/openapi-limitations/
title: OpenAPI 2.0 feature limitations \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:24.444873+00:00
---

# OpenAPI 2.0 feature limitations  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/openapi-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options)



Send feedback 

#  OpenAPI 2.0 feature limitations Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

The following sections describe the limitations of OpenAPI 2.0 features on Endpoints.

## Scopes ignored

Although Endpoints accepts OpenAPI documents that have scopes defined in a security scheme object, when a request is sent to your API, neither the Extensible Service Proxy (ESP), Extensible Service Proxy V2 (ESPv2), nor Cloud Endpoints Frameworks check the defined scopes.

## Multiple security requirements

You can specify more than one security requirement in your OpenAPI document. This section describes the security schemes that ESP and ESPv2 support.

### Security requirements containing an API key

ESP and ESPv2 don't support alternative (logical OR) security requirements when one of the security schemes is an API key. For example, ESP and ESPv2 don't support the following security requirement list:
    
    
    security:
    - petstore_auth: []
    - api_key: []
    

This definition requires an operation to accept requests that follow the `petstore_auth` requirements **or** the `api_key` requirements.

Note, however, that ESP and ESPv2 support security requirement conjunctions (logical AND), so you can require both an API key and OAuth2 authentication. For example, the following security requirement list is supported:
    
    
    security:
    - petstore_auth: []
      api_key: []
    

This definition requires an operation to accept requests that simultaneously follow the `petstore_auth` requirements **and** the `api_key` requirements.

### Security requirements for OAuth2

ESP and ESPv2 support security alternative (logical OR) security requirements, but only for OAuth2 authentication security schemes. For example, the following security requirement list is supported:
    
    
    security:
      - firebase1: []
      - firebase2: []
    

## Security definition validation

ESP and ESPv2 don't validate that all the security requirements (either at the API level or method level), also are present under the `securityDefinitions` section. As a result, if the API specification uses an undefined security schema, unauthenticated requests may come through the API, on the level where the undefined security key is configured. Make sure that all security keys used by your API and its methods are defined under the security definitions in your OpenAPI document.

## URL path templating

Endpoints only supports URL path template parameters that correspond to entire path segments (delimited by slashes `/`). URL path template parameters that correspond to partial path segments aren't supported.

For example, the following URL path templates are supported:

  * `/items/{itemId}`
  * `/items/{itemId}/subitems`



The following URL path templates aren't supported and will be rejected:

  * `/items/overview.{format}`
  * `/items/prefix_{id}_suffix`



## Operations on URL root path `/`

Endpoints accepts OpenAPI documents that include operations on the root path `/`. However, requests on the root path are rejected by ESP. Note, this limitation is only for ESP, ESPv2 supports root path `/`.

For example, the following OpenAPI document snippet is accepted:
    
    
    paths:
      /:
        post:
          operationId: "root"
          responses:
            200:
              description: "Success"
              schema:
                type: string
    

But subsequent requests for `POST /` are rejected with the following error:
    
    
    {
       "code": 5,
       "details": [
           {
               "@type": "type.googleapis.com/google.rpc.DebugInfo",
               "detail": "service_control",
               "stackEntries": []
           }
       ],
       "message": "Method does not exist."
    }
    

## File upload

Endpoints does not accept the `type: file` for file upload parameters, `type: string` should be used instead.

For example, the following `type: file` snippet is not allowed:
    
    
    paths:
      /upload:
        post:
          summary: Uploads a file.
          consumes:
            - multipart/form-data
          parameters:
            - in: formData
              name: upfile
              type: file
              description: The file to upload.
    

Whereas the following with `type: string` is allowed:
    
    
    paths:
      /upload:
        post:
          summary: Uploads a file.
          consumes:
            - multipart/form-data
          parameters:
            - in: formData
              name: upfile
              type: string
              description: The file to upload.
    

## Parameters, schemas, and types

ESP and ESPv2 ignore most parameter and type definitions.

Endpoints accepts OpenAPI documents that include required parameter and type definitions, but ESP and ESPv2 don't enforce these definitions and forwards incoming requests to your API. The following is a partial list that provides examples of the definitions that ESP and ESPv2 don't enforce:

  * Form Data parameters, such as: 
        
        parameters:
        - name: avatar
          in: formData
          description: "The avatar of the user"
          type: string

  * Required parameters, such as: 
        
        parameters:
        - name: message
          in: query
          description: "Message to send"
          required: true
          type: string

  * Array collection formats, such as: 
        
        parameters:
        - name: items
          in: query
          description: "List of item IDs"
          required: true
          type: array
          items:
            type: string
          collectionFormat: tsv

  * Type composition, such as: 
        
        definitions:
          base:
            properties:
              message:
                type: string
          extended:
            description: "Extends the base type"
            allOf:
            - $ref: "#/definitions/base"
            - type: object
              properties:
                extension:
                  type: string

  * Different response objects per status code, such as: 
        
        responses:
          200:
            description: "Echo"
            schema:
              $ref: "#/definitions/EchoResponse"
          400:
            description: "Error"
            schema:
              type: string




## External type references

Endpoints doesn't support references to types outside of an OpenAPI document. For example, Endpoints rejects OpenAPI documents that include:
    
    
    parameters:
    - name: user
      description: User details
      in: body
      schema:
        $ref: "https://example.com/mytype.json"
    

## Custom port in service host address

Endpoints doesn't allow for custom ports in the `host` field of an OpenAPI document. For example, Endpoints rejects OpenAPI documents such as:
    
    
    swagger: 2.0
    host: example.com:8080
    schemes:
    - http
    

## YAML alias limitations

Endpoints can support up to 200 YAML alias nodes in an OpenAPI document. If there are more than 200 YAML aliases in an OpenAPI document, we recommend dereferencing aliases where possible to comply with this limit.

## Known bugs

The following is a list of known issues.

### OpenAPI documents rejected

When you deploy your OpenAPI document by using `gcloud endpoints services deploy`, Endpoints rejects OpenAPI documents that include:

  * Array body parameters, such as: 
        
        parameters:
        - name: message
          description: "Message to echo"
          in: body
          schema:
            type: array
            items:
              type: string

  * Paths with trailing slashes, for example: 
        
        paths:
          "/echo/":
            post:
              description: "Echo back a given message."
        

To fix this issue, remove the trailing slash from `/echo/`:
        
        paths:
          "/echo":
            post:
              description: "Echo back a given message."
        




### API key definition limitations

When specifying an API key in the security definitions object in your OpenAPI document, Endpoints requires one of the following schemes:

  * The `name` is `key` and the `in` is `query`
  * The `name` is `api_key` and the `in` is `query`
  * The `name` is `x-api-key` and the `in` is `header`



For example:
    
    
    "securityDefinitions": {
      "api_key_0": {
            "type": "apiKey",
            "name": "key",
            "in": "query"
        },
      "api_key_1": {
            "type": "apiKey",
            "name": "api_key",
            "in": "query"
        }
      "api_key_2": {
            "type": "apiKey",
            "name": "x-api-key",
            "in": "header"
        },
    }
    

When you deploy an OpenAPI document with other types of API key security definitions, Endpoints might accept them and output a warning. However, the API key security definitions are ignored in incoming requests.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
