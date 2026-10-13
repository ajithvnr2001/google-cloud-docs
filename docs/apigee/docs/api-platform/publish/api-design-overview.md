---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/api-design-overview/
title: API design overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:21.477977+00:00
---

# API design overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/api-design-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API design overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

In the Design phase, you define the requirements for your API. As an API designer, you plan the services you'd like to expose to consumers, and design APIs to access those services. You create one of the following documents to capture your API requirements: 

  * An **OpenAPI document**
  * A **GraphQL schema**



The following sections provide more information about OpenAPI and GraphQL documents and the role they play in the lifecycle of your API. For a comparison of the two API design options, see REST and GraphQL compared in this [blog post](https://cloud.google.com/blog/products/api-management/interacting-with-apis-rest-and-graphql).

## What is the OpenAPI Specification? 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/OpenAPI_Pantone.png)  
"The OpenAPI Initiative (OAI) is focused on creating, evolving and promoting a vendor neutral API Description Format based on the Swagger Specification." For more information about the OpenAPI Initiative, see <https://openapis.org>.

An **OpenAPI document** uses a standard format to describe a RESTful API. Written in either JSON or YAML format, an OpenAPI document is machine readable, yet also easy for humans to read and understand. The OpenAPI Specification enables formal description of elements of an API such as its base path, paths and verbs, headers, query parameters, content types, response models, and more. In addition, an OpenAPI document is commonly used to generate API documentation.

Here's a fragment from an OpenAPI document that describes Apigee's simple hello world sample. For more information, view the OpenAPI Specification on [GitHub](https://github.com/apigee/api-platform-samples/tree/master/default-proxies/helloworld/openapi).

**Tip:** Apigee supports **OpenAPI Specification 3.0** , though a subset of features are not yet supported. See [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues) and select **Integrated portal** in the **Filter by RELEASE** drop-down.
    
    
    openapi: 3.0.0
    info:
      description: OpenAPI Specification for the Apigee mock target service endpoint.
      version: 1.0.0
      title: Mock Target API
    paths:
      /:
        get:
          summary: View personalized greeting
          operationId: View a personalized greeting
          description: View a personalized greeting for the specified or guest user.
          parameters:
            - name: user
              in: query
              description: Your user name.
              required: false
              schema:
                type: string
          responses:
            "200":
              description: Success
      /help:
        get:
          summary: Get help
          operationId: Get help
          description: View help information about available resources in HTML format.
          responses:
            "200":
              description: Success
    ...
    

Many excellent sources of information about OpenAPI Specifications exist. A good place to start is the [OpenAPI Initiative](https://openapis.org/) site, where you'll find overviews, blogs, and links to the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/tree/master/versions). Refer to the Specification for detailed descriptions of the schema elements and data types.

There are a number of JSON and YAML example OpenAPI documents that you can download from the [OpenAPI Specification repository](https://github.com/OAI/OpenAPI-Specification/tree/master/examples).

**Note:** To try out a working example, see [ Creating an API proxy from an OpenAPI Specification](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/create-api-proxy-openapi-spec).

## What is a GraphQL schema? 

A **GraphQL schema** describes the data available in your API for a client to query.

Benefits of using GraphQL include: 

  * A single endpoint provides access to all fields for a given operation 
  * The powerful query language, called Schema Definition Language, enables you to access exactly the data you need, preventing over-fetching or under-fetching of data 
  * Processing of queries happens in parallel



For more information about GraphQL, see [graphql.org](https://graphql.org).

The following provides an example of a GraphQL schema that defines the data entry point (Query type), available write operations (Mutation type), and data types.
    
    
    type Query {
      Greeting: String
      students: [Student]
    }
    type Mutation {
      createStudent(firstName: String!, lastName: String!): Student!
    }
    type Subscription {
      newStudent: Student!
    }
    type Student {
      Id: ID!
      firstName: String!
      lastName: String!
      password: String!
      collegeId: String!
    }
    

You can query the GraphQL schema to return the exact data you need as a JSON payload. 

![GraphQL query and results](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/graphql-query.png)

## What happens if I modify a document?

Each OpenAPI or GraphQL document serves as the source of truth throughout the API lifecycle. The same document is used at each phase in the API lifecycle, from development to publishing to monitoring. 

When you edit or delete a document, it has impact down the line:

  * If you edit a document, you need to manually edit the related artifacts including the API proxy and any API products that expose its resources, and regenerate the [API reference documentation](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis) to reflect the changes implemented in the document.
  * If you delete a document, you need to manually delete the related artifacts including the API proxy and edit any API products to delete related resources, and regenerate the [API reference documentation](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis) to reflect the removal of the document and its resources.



## What happens when I create an API proxy from an OpenAPI document?

You can create your API proxies from your OpenAPI documents. In just a few clicks, you'll have an API proxy with the paths, parameters, conditional flows, and target endpoints generated automatically. Then, you can add features such as OAuth security, rate limiting, and caching.

You can create an API proxy from an OpenAPI document using the Create Proxy Wizard, as described in [Using OpenAPI Specifications to generate proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#openapi). For a hands-on experience, step through the [Creating an API proxy from an OpenAPI Specification](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/create-api-proxy-openapi-spec) tutorial.

When you [publish your API](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis), you take a **snapshot** of the OpenAPI document to generate API reference documentation. That snapshot represents a specific revision of the description document.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
