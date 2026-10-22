---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking/
title: Masking and hiding data \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:11.590800+00:00
---

# Masking and hiding data  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Masking and hiding data Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When you debug APIs calls in Apigee, the content can sometimes contain sensitive data, such as credit cards or personally identifiable health information (PHI) that must be masked.

Apigee provides different ways of masking or hiding sensitive data from [debug sessions](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace). If you use masking for data collected in debug sessions, Apigee performs the masking in the gateway nodes, before transmitting the debug session data to the control plane.

## Masking sensitive data

Apigee enables you to define mask configurations to mask specific data in trace and debug sessions. When data is masked, it is replaced with asterisks in the trace output. You can mask sensitive data and keep non-sensitive data unchanged. For example:
    
    
    <ServiceRequest>
      <request-id>B540A938-F551</request-id>
      <customer-name>**********</customer-name>
    </ServiceRequest>

The mask configuration is a singleton resource that you define at the environment level. By default, no data masking is in effect.

Data masking applies only to data captured in a debug session for an API proxy. Data masking does not affect the data that gets sent to targets or client applications. If you change your data masking configuration, you must start a new debug session to see the effect of your change.

### Structure of a mask configuration

Mask configurations are JSON-formatted files that enable you to identify sensitive data in the following sources:

  * **XML payloads:** Using XPath, you identify XML elements to be filtered from request or response message payloads.
  * **JSON payloads:** Using JSONPath, you identify JSON properties to be filtered from request or response message payloads.
  * **Flow variables:** You can specify a list of variables that should be masked in debug output. When you specify the `request.content`, `response.content`, or `message.content` flow variables, the request/response body is also masked.



The following provides an example of the basic structure of a mask configuration in JSON format. For more information about the mask configuration fields shown in the example, see [DebugMask](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/DebugMask). 
    
    
    {
      "namespaces": {
        "myco": "http://example.com"
      },
      "requestXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "responseXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "faultXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "requestJSONPaths": [
        "$.store.book[*].author"
      ],
      "responseJSONPaths": [
        "$.store.book[*].author"
      ],
      "faultJSONPaths": [
        "$.store.book[*].author"
      ],
      "variables": [
        "request.header.user-name",
        "request.formparam.password",
        "myCustomVariable"
      ]
    }

### Viewing the mask configuration in an environment using the API

To view the mask configuration in an environment, issue a GET to the following resource: 
    
    
    /organizations/{org}/environments/{env}/debugmask

For example:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/myorg/environments/test/debugmask" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response: 
    
    
    {
      "name": "organizations/myorg/environments/test/debugmask"
      "namespaces": {
        "myco": "http://example.com"
      },
      "requestXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "responseXPaths": [
        "/myco:Greeting/myco:User"
      ]
    }

### Updating the mask configuration in an environment using the API

To update the mask configuration singleton resource in an environment, issue a PATCH to the following resource:
    
    
    /organizations/{org}/environments/{env}/debugmask

Optionally, you can pass the following query parameters:

  * Set the `updateMask` query parameter to specify a field mask that includes a comma-separated list of fully-qualified names of fields in the debug mask. For example: `"requestJSONPaths"`
  * Set the `replaceRepeatedFields` query parameter to specify whether to replace existing values in the debug mask when doing an update. By default, values are appended (`false`)



For example: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/myorg/environments/test/debugmask" \
      -X PATCH \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d \
      '{
         "namespaces": {
           "ns1": "http://example.com"
         },
         "requestXPaths": [
           "/ns1:employee/ns1:name"
         ]
       }'

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

### Masking namespace-scoped XML

If you want to mask XML data and that data uses XML namespaces, your mask configuration must reference those namespaces with the `namespaces` element. This is true whether the XML payload uses a default namespace, or a namespace prefix.

For example, suppose you want to mask the employee name in the request payload, and the XML does not use XML namespaces:
    
    
    <employee>
      <name>Shanmu Tharman</name>
      <age>50</age>
    </employee>

Therefore, the debugmask configuration doesn't require the `namespaces` element:
    
    
    {
      "requestXPaths": [
        "/employee/name"
      ]
    }

If the XML payload uses namespaces with prefixes:
    
    
    <cym:employee xmlns:cym="http://cymbalgroup.com" xmlns:id="http://cymbalgroup.com/identity">
      <id:name>Shanmu Tharman</id:name>
      <id:age>50</id:age>
    </cym:employee>

Then the mask configuration should contain the `namespaces` element. You may choose any valid namespace prefix in the debugmask configuration; the namespace prefix in the debugmask configuration may be the same as the namespace prefix used in the XML, but that is not required.
    
    
    {
      "namespaces": {
        "cym": "http://cymbalgroup.com",
        "idns": "http://cymbalgroup.com/identity"
      },
      "requestXPaths": [
        "/cym:employee/idns:name"
      ]
    }

If the XML Payload uses a namespace with no prefix, meaning the default namespace:
    
    
    <employee xmlns="http://cymbalgroup.com" xmlns:id="http://cymbalgroup.com/identity">
      <id:name>Shanmu Tharman</id:name>
      <id:age>50</id:age>
    </employee>

Then the debugmask configuration must still define a prefix in the `namespaces` element corresponding to that default namespace. You can use any unique prefix you like.
    
    
    {
      "namespaces": {
        "p1": "http://cymbalgroup.com",
        "id": "http://cymbalgroup.com/identity"
      },
      "requestXPaths": [
        "/p1:employee/id:name"
      ]
    }

### Other Configuration Notes

  * With the `*XPaths` and `*JSONPaths` configuration elements, you can mask data that appears in the `request`, `response`, or `fault` messages. But the full message content may also be captured by debug sessions. You may also want to configure `request.content` or `response.content` in the `variables` section to prevent sensitive data from being displayed.

  * If you use the [ ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) to make a request, the information in the request and response for that callout will not be masked using the configuration elements like `requestXPaths` or `responseJSONPaths`. If you wish to mask that data, you should specify a variable name for the request and response messages in the ServiceCallout policy, and then specify those variables in the `variables` section of the debugmask. For example, if your ServiceCallout policy uses:
        
        <ServiceCallout name='SC-1'>
          <Request variable='rbacRequest'>
            <Set>
              <Payload contentType='application/json'>{ ... }</Payload>
               ...
        

Then you should include `rbacRequest.content` in the `variables` element for the debugmask configuration.
        
        {
          ...
          "variables": [
            "request.content",
            "response.content",
            "rbacRequest.content"
          ]
        }




## Hiding sensitive data

In addition to masking, you can prevent sensitive data from even appearing in the Trace tool and debug sessions by choosing a name that begins with `private.` for your custom variables.

For example, when using the [Key Value Map Operations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) to retrieve a value from a key value map, you may choose the variable name as follows to ensure the value does not appear in Trace or debug sessions:
    
    
    <KeyValueMapOperations name='KVM-Get-1'>
        <Scope>environment</Scope>
        <ExpiryTimeInSecs>300</ExpiryTimeInSecs>
        <MapName>settings</MapName>
        <Get assignTo='private.privatekey'>
          <Key>
            <Parameter>rsa_private_key</Parameter>
          </Key>
        </Get>
      </KeyValueMapOperations>

Variables without the `private.` prefix are displayed in clear text in Trace and debug sessions even if the data originates from an encrypted data store such as a key value map. Use masking if you want to mask these values.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
