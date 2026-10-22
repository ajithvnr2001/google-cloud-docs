---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider/
title: Adding an API as a type provider \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:11.884802+00:00
---

# Adding an API as a type provider  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Adding an API as a type provider Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to add an API to Google Cloud Deployment Manager as a type provider. To learn more about types and type providers, read the [Types overview](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types) documentation.

A type provider exposes all of the resources of a third-party API to Deployment Manager as base types that you can use in your configurations. These types must be directly served by a RESTful API that supports [Create, Read, Update, and Delete (CRUD)](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements).

If you want to use an API that is not automatically provided by Google with Deployment Manager, you must add the API as a type provider. You can add any API as a type provider as long as that API has an [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification) (formerly Swagger©), or a [Google Discovery](https://developers.google.com/discovery/v1/reference/apis) document.

**Note:** Deployment Manager only supports using Google Discovery documents and OpenAPI 1.2 and 2.0 specifications for API descriptor documents. Any API that you want to add to Deployment Manager must also meet the requirements described in the [API requirements for integrating an API](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements) documentation.

This document does not describe how to stand up your own API service. The assumption is that there is already an API that you want to add, or that you have already created a running API that is accessible from a public endpoint. For example, to deploy a sample API using Google Cloud Endpoints, you can follow the [Cloud Endpoints Quickstart](https://docs.cloud.google.com/endpoints/docs/quickstart-compute-engine).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Set up [v2beta API access](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta) if you want to use the API examples in this guide.



## Components of a type provider

A type provider consists of:

  * **Name** : The desired name of the type provider. You will use this name to reference the type and its relevant API resources.
  * **Descriptor document** : The URL of the descriptor document for the type. Supported documents include Google Discovery documents or OpenAPI 1.2 specifications.
  * **Authentication:** Any authentication credentials needed for the API. You can specify [basic authentication](https://wikipedia.org/wiki/Basic_access_authentication). If your API is running on Cloud Endpoints or Google Kubernetes Engine (GKE), you can also use the service account credentials of the project as authentication.
  * **Advanced options** : Any advanced input mappings or API options.



### Name

The name of the type provider. You will use this name to refer to the type in future configurations and templates. For example, if you created a type provider and named it `my-awesome-type-provider`, then you would use it in subsequent templates like so:
    
    
    resources:
      name: a-deployment
      type: my-project/my-awesome-type-provider:some-collection
      properties:
      …
    

where `my-project` is the project ID the type belongs to and `some-collection` is the path to the API resource you are creating.

### Descriptor document

The descriptor document for a type provider can be either an OpenAPI 1.2 or 2.0 specification, or a Google Discovery document. For example, you can find the Google Discovery document for the Compute Engine Beta API at this URL:
    
    
    https://content.googleapis.com/discovery/v1/apis/compute/beta/rest
    

See a [full list of Google Discovery documents](https://content.googleapis.com/discovery/v1/apis/).

[OpenAPI 1.2](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/1.2.md) and [OpenAPI 2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) documents are also acceptable.

### Authentication

If your API requires authentication, you can provide the authentication details here. Deployment Manager supports basic authentication credentials, such as a username and password. For Google Kubernetes Engine and Google Cloud Endpoints, you can use the `Authorization` header to supply an access token from the project's service account.

To specify basic authentication credentials, provide the username and password in the `credentials` section:
    
    
    credential:
      basicAuth:
        user: [USERNAME]
        password: [PASSWORD]
    

You only have to specify the username and password the first time you create a type provider.

If you have a cluster running on Google Kubernetes Engine (GKE) in the same project in which you are using Deployment Manager, you can add the cluster as a type provider and use Deployment Manager to access the GKE API. In this scenario, you can get the OAuth 2.0 access token of the project's [Google APIs service account](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed_service_accounts) and provide the access token in the `Authorization` header. Unlike in the previous credentials section, you must provide this as an input mapping in your request:
    
    
    - fieldName: Authorization
      location: HEADER
      value: >
        $.concat("Bearer ", $.googleOauth2AccessToken())
    

The `googleOauth2AccessToken()` method will automatically get an access token when the user calls this type provider. For a full example, see the [GKE Cluster and Type sample](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/examples/v2/gke).

You can use the same method to authenticate to Google Cloud Endpoints.

### (Optional) Custom Certificate Authority root

If you want to add an API as a type provider to Deployment Manager, and that API's HTTPS endpoint uses a certificate that is not supplied by a publicly trusted Certificate Authority (CA) to encrypt the connection, you can add the API to your configuration as in the following example:
    
    
    customCertificateAuthorityRoots:
    - $(ref.my-gke-cluster.masterAuth.clusterCaCertificate)
    

where `my-gke-cluster` is the GKE cluster you are using. For a detailed example, refer to the [GKE Provider Cluster sample](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/blob/master/google/resource-snippets/container-v1/gke_provider_cluster.jinja).

### Advanced type options

Certain APIs might have idiosyncrasies that make it difficult for Deployment Manager to map all the properties of the API to Deployment Manager. In an ideal scenario, you supply a descriptor document and Deployment Manager automatically figures out the API request paths and the relevant API properties without additional work on your part. For more complex APIs, Deployment Manager can understand the majority of the API, but you might need to explicitly specify input mappings to API behavior that is not obvious.

To learn more about input mappings, read the documentation for [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).

## Creating a type provider

To create a type provider, make a request to Deployment Manager with a request payload containing the desired type provider name, the descriptor URL, and any necessary authentication credentials.

###  gcloud 

To create a type provider using the gcloud CLI, use the `type-providers create` command:
    
    
    gcloud beta deployment-manager type-providers create [TYPE_PROVIDER_NAME] --descriptor-url=[URL]
    

where:

  * `[TYPE_PROVIDER_NAME]` is the name you want to give this type.
  * `[URL]` is the fully-qualified URL to the descriptor document supporting this type. For example:
        
        http://petstore.swagger.io/v2/swagger.json
        




If you want to provide authentication credentials or [advanced API options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options), you can create an API options file written in YAML and provide it using the `--api-options-file` flag. For example, the file might look this:
    
    
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
          required:
          - displayName
    credential:
      basicAuth:
        user: [USERNAME]
        password: [PASSWORD]
    

The `gcloud` command would be:
    
    
    gcloud beta deployment-manager type-providers create [TYPE_NAME] --api-options-file=[FILE_NAME] \
        --descriptor-url [url]
    

If you want to authenticate by using a custom Certificate Authority (CA), you can add the CA as a flag to the `gcloud` command, as in the following example:
    
    
    gcloud beta deployment-manager type-providers create [TYPE_NAME] --api-options-file=[FILE_NAME] \
        --descriptor-url [url] \
        --custom-certificate-authority-roots=[CA_NAME]
    

###  API 

To create a base type in the API, make a `POST` request that contains the `descriptorUrl` and an optional [configuration options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options) in the request body. For example:
    
    
    POST https://www.googleapis.com/deploymentmanager/v2beta/projects/[PROJECT_ID]/global/typeProviders
    
    { "description":"",
      "descriptorUrl":"https://www.example.com/api/v1beta1.json",
      "name":"my-type-provider",
      "collectionOverrides":[
        {
          "collection":"emailAddresses/v1beta/people",
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
                "location":"PATH",
                "methodMatch":"^update$",
                "value":"$.resource.properties.displayName"
              }
            ],
            "virtualProperties":"schema: http://json-schema.org/draft-04/schema#\ntype: object\nproperties:\n  displayName:\n    type: string\nrequired:\n- displayName\n"
          }
        }
      ],
      "credential":{
        "basicAuth":{
          "password":"example-password",
          "user":"example-user"
        }
      }
    }
    

For more information, see the documentation for the [`insert`](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/insert) method.

## Testing your type provider

To verify your type provider type works as expected:

  1. [Call your new type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider) in a configuration.
  2. [Deploy](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider#using_a_type_provider) each collection provided by the type provider to ensure the API works as expected. A collection is an API resource from the specified type provider. 
  3. [Make an update](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments) to each collection.
  4. [Delete](https://docs.cloud.google.com/deployment-manager/docs/deployments/deleting-deployments) each collection.



When a user instantiates a type from your type provider, they are actually making a request to Deployment Manager, not explicitly to the underlying API. In turn, Deployment Manager constructs the request with the information provided to make a request to the API on the user's behalf. The most common problem you might see is that the API has properties that are hard for Deployment Manager to automatically recognize. For example, some APIs require properties that can only be extracted from an API response. Other APIs might use the same field name with different values depending on the operation. In these cases, you would need to explicitly tell Deployment Manager how to handle these scenarios.

If your API has any of these traits, [use input mappings](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options) to clarify the ambiguity for Deployment Manager.

## What's next

  * Learn how to [call a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider).
  * [Share your type provider with other projects](https://docs.cloud.google.com/deployment-manager/docs/configuration/sharing-types-across-projects).
  * Learn more about [types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types).
  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).
  * Learn more about [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).



© 2016 Swagger. All rights reserved.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
