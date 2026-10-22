---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options/
title: Setting Advanced API Options \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:12.224439+00:00
---

# Setting Advanced API Options  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Setting Advanced API Options Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set up advanced configuration options, like input mappings and virtual properties, for type providers. To learn more about types, read the [Types Overview](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types). To learn more about type providers, read the [One-page Guide to Integrating with Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api).

If you are trying to integrate an API that does not satisfy the [API requirements](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements) defined by Deployment Manager, you can use input mappings and virtual properties to help resolve these inconsistencies. Input mappings let you provide explicit mappings of API parameters where there is ambiguity and virtual properties let you expose arbitrary properties that don't exist in the underlying APIs so you can simplify input and hide complexities of the API from your users.

Implementing advanced configuration options requires intimate familiarity with the API for which you are creating the type provider. Since each API can vary widely from others, this page provides general guidance and examples but does not provide specific API guidance.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Set up [v2beta API access](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta) if you want to use the API examples in this guide.
  * Understand how to [create a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).



## Common scenarios that require advanced configuration options

**Property name is reused with different values**

In certain APIs, the same property or parameter name might be reused in different methods but with different values. For example, an API might specify that the `name` parameter for creating a resource (a `POST` request), might have the value `foo/bar`, while the same `name` field for an update requests (`PATCH` or `PUT`) might require the value `foo/bar/baz`.

**Property values can be inferred from the API response**

Certain API methods require a server-generated value that is returned when you make a `GET` request to the resource. For example, an API might require an `etag` parameter to make update requests when mutating a resource. The `etag` value changes after each mutate request, so you get the current `etag` parameter by performing a `GET` request to the resource, before making the request to update the resource.

Using input mappings, you can tell Deployment Manager that the `etag` field can be retrieved from the API resource. Deployment Manager automatically performs a `GET` request to get this value when a user calls the method you specified in the input mappings.

**Simplify user input**

Deployment Manager supports virtual properties which are arbitrary properties that you can expose to your users through Deployment Manager for different uses. Treat virtual properties as properties do not exist on the underlying API but are arbitrary variables whose value you can inject as necessary in your input mappings. For example, imagine that there is an API property that must be base64 encoded before the value is sent to the underlying API. Rather than asking your users to provide the value in base64 encoding, you could create a virtual property that prompts users for the plain text value, then base64 encode the value with input mappings, and finally, supply the result to the underlying API.

## Specifying advanced options

To specify advanced options, provide the `collectionOverrides` property when creating your Type Provider resource, and define input mappings or virtual properties for each API collection as you need.

For example, using the gcloud CLI, you can provide advanced options using a YAML file and supply the YAML file with your `type-providers create` request. A sample YAML file might look like this:
    
    
    collectionOverrides:
    - collection: /emailAddresses/v1beta/people
      options:
        inputMappings:
        - methodMatch: ^create$
          fieldName: emailAddress.displayName
          value: $.resource.properties.displayName
          location: BODY
        - methodMatch: ^update$
          fieldName: displayName
          value: $.resource.properties.displayName
          location: PATH
        virtualProperties: |
          schema: http://json-schema.org/draft-04/schema#
          type: object
            properties:
              displayName:
                type: string
    credential:
      basicAuth:
        user: [USERNAME]
        password: [PASSWORD]
    

This configurations tells Deployment Manager:

  * For the `create` method, look for the field named `emailAddress.displayName` in the resource body and set that field's value to the user's input for the `displayName` property in the Deployment Manager configuration. So if a user sets their config like this:
        
        resources:
         - name: example
           type: myproject/emailAddress:/emailAddresses/v1beta/people
           properties:
           - displayName: John Doe
             ...
        

Deployment Manager will set the value for `emailAddress.displayName` to John Doe.

  * For the `update` method, the field is in the resource path instead of the resource body but the same input mapping is applied.




### Specifying input mappings

An input mapping allows you map or inject information for certain API fields so that Deployment Manager can more seamlessly interact with the underlying API, relieving the burden on your users to understand subtle API behavior.

Use input mappings to simplify how your users interact with the API. For example, you can use input mappings to automatically get server-generated values, such as fingerprints, IDs, or etags. This saves users the trouble of performing a separate `get` request on the resource every time they want to make an update.

Similarly, you can also use input mappings to handle ambiguous or confusing situations where the same API field has different values for different methods. For example, a request to create a resource might require a `name` property that the user can specify, but the same API might require a `name` property in a different format for `update` methods. You can use input mappings to tell Deployment Manager which value is appropriate for each API method.

To specify input mappings for a type provider, provide the `options.inputMappings` property. You can define input mappings that apply for the entire API or you can explicitly provide input mappings for each collection:
    
    
    # Input mappings for the entire API
    "options": {
      "inputMappings": [
          {
              "fieldName": "[NAME]",
              "location":  "[PATH | BODY | QUERY | HEADER]",
              "methodMatch": "[REGEX_MATCHING_CERTAIN_METHODS]",
              "value": "[VALUE_TO_INJECT]"
          },
          {
              "fieldName": "[NAME]",
              "location":  "[PATH | BODY | QUERY | HEADER]",
              "methodMatch": "[REGEX_MATCHING_CERTAIN_METHODS]",
              "value": "[VALUE_TO_INJECT]"
          }
       ]
    },
    # Input mappings for specific collections
    "collectionOverrides": [
        {
            "collection": "[SPECIFIC_COLLECTION]",
            "options": {
                "inputMappings": [
                    {
                        "fieldName": "[NAME]",
                        "location": "[PATH | BODY | QUERY | HEADER]",
                        "methodMatch": "[REGEX_MATCHING_CERTAIN_METHODS]",
                        "value": "[VALUE_TO_INJECT]"
                    },
                    {
                        "fieldName": "[NAME]",
                        "location": "[PATH | BODY]",
                        "methodMatch": "[REGEX_MATCHING_CERTAIN_METHODS]",
                        "value": "[VALUE_TO_INJECT]"
                    },
                    ...[additional fields if necessary]...
                ]
            }
        }
    ]
    

Each of the important parts of this syntax is described below.

**Collection**

`[SPECIFIC_COLLECTION]` is the API collection for which this input mapping applies. For example, if you were providing input mappings for a Google Discovery document, like the [IAM Service Accounts](https://www.googleapis.com/discovery/v1/apis/iam/v1/rest) API, relevant collections are `projects.serviceAccounts` and `projects.serviceAccountKeys`.

For an API that uses OpenAPI specification, the collection path might be `/example-collection/{name}`. You can explore a functional [OpenAPI example](http://petstore.swagger.io/) on the OpenAPI GitHub repository.

**Field name**

`"fieldName"` is the API attribute or property for which you want to specify the input mapping. For example, `"fieldName": "fingerprint", "fieldName": "etag"` and so on.

**Location**

API properties can appear either as parameters in the URL path, or as part of the request or response body. Specify where this input mapping applies, such as the URL `PATH` or request `BODY` as the location. Supported values include:

  * `PATH`
  * `BODY`
  * `QUERY`
  * `HEADER`



**Method match**

Specify what methods this input mapping applies to. Use regex to specify multiple methods. For example:
    
    
    "methodMatch":"^create$"
    

For OpenAPI specifications, you can do:
    
    
    "methodMatch: ^(put|get|delete|post)$"
    

**Value**

Specify the value that Deployment Manager should inject for this field. This field uses [JSONPath notation](http://goessner.net/index.html). For example, this input mapping says that for the `name` field, Deployment Manager should take the user-supplied value and inject it into the format `projects/$.project/topics/$resource.properties.topic`:
    
    
    "inputMappings":[
    {
      "fieldName":"name",
      "location":"PATH",
      "methodMatch":"^post$",
      "value":"concat(\"projects/\", $.project, \"/topics/\", $.resource.properties.topic)"
    }...
    

  * When you use `$.resource.properties.[VARIABLE]`, you set value to a property that a user will be setting in their configuration. For example, for `$.resource.properties.topic`, the value will be the user-provided value for the property `topic` in their configuration:
        
        resources:
        - name: example
          type: example-type-provider:collectionA
          properties:
            topic: history # The value of "history" would be used for the `name` parameter because of the input mapping above
        

  * To reference the resource itself after a `get` request, use `$.resource.self.[VARIABLE]`. For example, for update requests, if you wanted to get the latest fingerprint, you can use this syntax to tell Deployment Manager to perform a `get` and grab the value:
        
        {
          'fieldName': 'fingerprint',
          'location': 'BODY',
          'methodMatch': '^(put)$',
          # self represents the resource by doing a GET on it.
          # This mappings gets latest fingerprint on the request.
          # Final PUT Body will be
          # {
          #   "name": "my-resource-name",
          #   "fingerprint": "<server generated fingerprint>"
          # }
          'value': '$.resource.self.fingerprint'
        }
        




### Using virtual properties

Virtual properties are arbitrary properties that you can expose to your users through Deployment Manager. These properties are not part of the underlying API but are arbitrary variables that can be used to pass information or hide inconsistencies of the API from your users. You can reference virtual properties in your input mappings as well.

Virtual properties follow the JSON 4 schema. Provide virtual properties as part of the `options` for a specific collection:
    
    
    "collection": "[SPECIFIC_COLLECTION]",
      "options": {
       "virtualProperties": "schema: http://json-schema.org/draft-04/schema#\ntype: object\nproperties:\n  [PROPERTY]:\n    type: [DATA_TYPE]\n  [ANOTHER_PROPERTY]:\n    type: [ANOTHER_DATA_TYPE]n"
       "inputMappings": [
        ...
       ]
      }
    

In a YAML definition file, this would look like:
    
    
    - collection: projects.serviceAccounts
      options:
        virtualProperties: |
          schema: http://json-schema.org/draft-04/schema#
          type: object
          properties:
            a-property:
              type : string
            b-property:
              type : string
          required:
          - a-property
          - b-property
        inputMappings:
        ...
    

For example, consider a fake API that generates email addresses. Let's assume the API has a method for creating an email that takes in a `emailAddress.displayName` property. When a user makes a request to create an email address, they provide a request like so:
    
    
    POST https://example.com/emailAddresses/v1beta/people/
    
    {
      "emailAddress": {
        "displayName": "john"
      }
    }
    

Now, lets say the API exposes a way to update the email address but the method for updating an email just requires the `displayName` property, rather than the `email.displayName` property:
    
    
    POST https://example.com/emailAddresses/v1beta/people/john
    
    {
      "displayName": "josh"
    }
    

How do you expect your users to provide this value when they use this type provider? You could ask them to specify the property differently depending on the operation:
    
    
    # Creating an email
    resources:
    - name: example-config
      type: projects/test-project:emailAddresses
      properties:
        emailAddress:
          displayName: john
    
    
    # Updating an email
    resources:
    - name: example-config
      type: projects/test-project:emailAddresses
      properties:
        displayName: john
    

Alternatively, you can create a virtual property that takes the same value, regardless of the operation, and then use input mappings to map the virtual property to the appropriate API parameter. For this example, assume you defined a virtual property named `displayName`. Your input mappings could then look like this:
    
    
    {
        "collectionOverrides":[
          {
            "collection":"emailAddresses",
            "options":{
              "inputMappings":[
                {
                  "fieldName":"emailAddress.displayName",
                  "location":"BODY",
                  "methodMatch":"^create$",
                  "value":"$.resource.properties.displayName"
                },
                {
                  "fieldName":"displayName",
                  "location":"BODY",
                  "methodMatch":"^update$",
                  "value":"$.resource.properties.displayName"
                }
              ],
              "virtualProperties":"schema: http://json-schema.org/draft-04/schema#\ntype: object\nproperties:\n  displayName:\n    type: string\nrequired:\n- displayName\n"
            }
          }
        ],
        "descriptorUrl":"https://example.com/emailAddresses/v1beta/",
        "options":{
          "nameProperty":""
        }
    }
    

Specifically, the virtual property is defined here:
    
    
    "virtualProperties":"schema: http://json-schema.org/draft-04/schema#\ntype: object\nproperties:\n  displayName:\n    type: string\nrequired:\n- displayName\n"
    

In human-readable format:
    
    
    "virtualProperties":
      "schema: http://json-schema.org/draft-04/schema#\n
       type: object\n
       properties:\n
         displayName:\n
         - type: string\n
       required:\n
       - displayName\n"
    

Now, your users can specify `displayName` as the top level property for both update and create requests, and Deployment Manager will know how to map the value correctly.
    
    
    # Creating an email
    resources:
    - name: example-config
      type: projects/test-project:emailAddresses
      properties:
        displayName: john
    
    
    # Updating an email
    resources:
    - name: example-config
      type: projects/test-project:emailAddresses
      properties:
        displayName: john
    

## What's next

  * Learn how to [use a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider).
  * Learn more about [types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types).
  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).
  * Learn how to [create a composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/composite-types/creating-composite-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
