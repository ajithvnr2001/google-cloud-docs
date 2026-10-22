---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/graphql/
title: Using GraphQL \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:00.549024+00:00
---

# Using GraphQL  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/graphql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using GraphQL Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The [GraphQL policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy) can parse GraphQL request payloads into message flow variables, verify the request against a GraphQL schema, or both.

The GraphQL policy parses GraphQL payloads into message flow variables, verifies GraphQL requests against a schema, or both.

Use the GraphQL policy to:

  * Ensure that your APIs only process requests that conform to the schema you provide.
  * Impose restrictions on the payload by setting a maximum on the number of fragments allowed.
  * Associate GraphQL with API products.
  * Leverage the Oauth2, VerifyAPIKey, and Quota policy features, just as in REST.



GraphQL supports the following types of payloads:

  * POST of graphQL payloads with `Content-Type : application/graphql`
  * POST of graphQL payloads with `Content-Type: applcation/json`
  * GET of graphQL payloads where the payload is a query parameter

**Note:** For `application/json` payloads of the form 
    
    
    {
    "query": "...",
    "operationName": "...",
    "variables": { "myVariable": "someValue", ... }
    }

Apigee currently ignores the optional `operationName` and `variables` fields. 

For a quick summary of the options for the GraphQL policy, see GraphQL options below.

To learn more about GraphQL, see [GraphQL.org](https://graphql.org/).

## Example

The following example shows how to upload a GraphQL schema to Apigee, and use it to validate requests with GraphQL content.

**Caution:** Verifying the payload against the schema is generally an expensive operation, and we recommend choosing to perform schema validation with care. Schema validation operations can be CPU intensive, especially when the payload and the schema are complex, and can result in significant latencies.**Note:** You can only provide one schema per policy. If you need to include multiple schemas, add multiple GraphQL policies to your proxy. 

### Create a schema file

To run the example, first create a GraphQL schema file with the following contents:
    
    
    type Query {
      allPersons(last: Int): [Person!]!
    }
    
    type Mutation {
      createPerson(name: String!, age: Int!): Person!
    }
    
    type Subscription {
      newPerson: Person!
    }
    
    type Person {
      name: String!
      sex: String!
      age: Int!
      posts: [Post!]!
    }
    
    type Post {
      title: String!
      author: Person!
    }

Save the file with whatever name you'd like to use, followed by the extension `.graphql`.

### Add the GraphQL policy in the Apigee UI

First, create the GraphQL policy as follows:

  1. In the Apigee UI, go to the **Proxy development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. In the list of proxies, select the API proxy for which you want to use the GraphQL policy.
  3. Click the **Develop** tab.
  4. In the left-hand pane, click the **+** button next to the **Policies** folder.
  5. In the **Create policy** dialog, click in the **Select policy type** field and scroll down to **Mediation** and select [**GraphQL**](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy).

![GraphQL Create Policy dialog.](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/graphql-create-policy.png)

Enter a **Display name** and **Name**.

Next, select a GraphQL schema file as follows:

     1. Click the **Schema File** field. This displays the following choices: 
        * **No Schema**. If you select this option, Apigee will not use a schema to validate requests.
        * **Import GraphQL schema (.graphql)**
     2. Select **Import GraphQL schema (.graphql)**. This displays the following:

![Choose a schema file.](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/choose-schema-file.png)
     3. Click **Choose File** and select the schema file you created previously (which must have the extension `.graphql`). The file appears in the **Schema name** field.

![Schema selected.](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/schema-selected.png)
  6. Click **Create** to create the policy.



Now that you have created the **GraphQL** policy, you can attach it to a step in the PreFlow:

  1. Select **Proxy Endpoints > default > PreFlow** in the left-hand pane: 

![Target endpoints for PreFlow select in the Proxy Explorer.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/select-proxy-endpoints-preflow.png)

  2. Click the **+** button next to **PreFlow** in the **Response** pane at the bottom-right of the Visual Editor: 

![Click + button next to PreFlow in the Response pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/add-policy-to-response-preflow.png)

  3. In the **Add policy step** dialog, select the **GQL-** policy. **Note:** This example uses the default name, **GQL** , for the GraphQL policy. You can change the name in the **DisplayName** element in the XML for the policy, by adding a descriptive phrase after **GQL-**. See [ Change the policy name](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy#change-the-policy-name).
  4. Click **Add** to attach the policy.
  5. Click **Save** to save the current revision with your changes.
  6. To deploy your changes, click the **Overview** tab and select **Deploy**.



See GraphQL options below for the options you can set for the GraphQL policy.

Now you can test the GraphQL policy with the following `curl` command:
    
    
    curl --location --request POST 'https://PROXY_BASEPATH/HOST_NAME' --data-raw 'query query_name {allPersons {name}}' -k

Where PROXY_BASEPATH is the proxy basepath and HOST_NAME is the name of your proxy, including the latest revision number. When you run the command, Apigee validates the request against the schema and returns the following output.
    
    
    {
      "query query_name {allPersons {name}}": "",
      "id": 101
    }

Here's another example of a request:
    
    
    curl --location --request POST 'https://PROXY_BASEPATH/HOST_NAME' --data-raw 'query ilovegql {DEADBEEF}' -k

This time the request validation fails with the following error message.
    
    
    {"fault":{"faultstring":"steps.graphQL.SchemaValidationFailed","detail":{"errorcode":"steps.graphQL.SchemaValidationFailed"}}}

## GraphQL options

The GraphPolicy has the following options:

  * `OperationType`: The operation type. The options are: 
    * `query`: The GraphQL equivalent of the REST `GET` operation.
    * `mutation`: The GraphQL equivalent of the REST `PUT` operation.
    * `query_mutation`: Both `query` and `mutation`.
  * `MaxDepth`: The maximum depth of the query, when represented as a tree. `MaxDepth` allows you to block deep queries in the payload, so that Apigee does not need to create very large flow variables to hold the values. However, the payload is sent as is, regardless of the value of `MaxDepth`.
  * `MaxCount`: The maximum number of fragments that can be in the payload. You can use this to prevent the GraphQL back-end server of the customer from executing highly complex queries, forcing clients to break their logic into smaller payloads. 
  * `Action`: One the following GraphQL actions: 
    * `parse`Apigee parses the GraphQL payload into the flow variables. You can then use the contents of the flow variables in policies such as JavaCallout. Note that `parse` also verifies the payload.
    * `verify`: Apigee verifies that the GraphQL payload conforms to the schema uploaded to the proxy. You can use `verify` to ensure that you do not get requests that don't conform to your schema. This can save valuable CPU time in the backend. 
    * `parse_verify`: Parse and verify the payload. 
  * `ResourceURL`: The path to the GraphQL schema file that Apigee uses to verify the GraphQL request.`



To learn more about these options, see the [GraphQL policy reference page](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
