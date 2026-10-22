---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement/
title: What's a policy? \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:03.982532+00:00
---

# What's a policy?  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  What's a policy? Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee enables you to _program_ API behavior without writing any code, by using _policies_. A policy is like a module that implements a specific, limited management function. Policies are designed to let you add common types of management capabilities to an API easily and reliably. Policies provide features like security, rate-limiting, transformation, and mediation capabilities, saving you from having to code and maintain this functionality on your own.

You're not limited to the set of policy types provided by Apigee. You can also write custom scripts and code (such as JavaScript applications), that extend API proxy functionality and enable you to innovate on top of the basic management capabilities supported by Apigee policies.

This topic provides an overview of policy types and use in Apigee. For information on specific policies, see the [Policies reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

## Policy types and categories

Technically, a policy is an XML-formatted configuration file. Each policy's structure (for example, the required and optional configuration elements) is defined by an [ XML schema](https://en.wikipedia.org/wiki/XML_schema). If you are proficient with XML tools, it is worthwhile to familiarize yourself with the policy schemas in the [API Platform samples](https://github.com/apigee/api-platform-samples/) on GitHub.

Apigee policies are grouped into the following functional categories. The policies available for each policy category are listed in the [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

### AI

Policies in the AI category let you optimize and secure the performance of AI workloads and models.

### Extension

Policies in the extension category enable you to tap into the extensibility of Apigee to implement custom behavior in the programming language of you choice.

### Mediation

Policies in the mediation category enable you to actively manipulate messages as they flow through API proxies. They enable you to transform message formats, from XML to JSON (and vice-versa), or to transform one XML format to another XML format. They also enable you to parse messages, to generate new messages and to change values on outbound messages. Mediation policies also interact with basic services exposed by Apigee, enabling you to retrieve data about apps, developers, security tokens, and API products at runtime. 

### Security

Policies in the security category support authentication, authorization, as well as content-based security.

### Traffic management

Policies in the traffic management category enable you to control the flow of request and response messages through an API proxy. These policies support both operational- and business-level control. They give you control over raw throughput, and can also control traffic on a per-app basis. Traffic management policy types enable you to enforce quotas, and they also help you to mitigate denial of service attacks.

## Attaching policies

In order for a policy to apply to your API proxy, you must attach it to the proxy in a flow. For information, see the other topics in this section, including [Attaching and configuring policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#new-proxy-editor) and [Attaching and configuring policies in XML files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files). 

## Deploying policy changes

For policy changes to take effect, you must deploy the API proxy revision to an environment. After you attach a policy or make changes to an existing policy, use the Apigee UI or the Apigee API to [deploy the changes](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview).

## Verifying policy enforcement

To verify that a policy is enforced properly, the API must be invoked by an HTTP client. To verify a `Quota` configuration, set a quota (for example, at one request per minute), then submit multiple requests to the API exceeding the quota limit that you set in the quota policy. (The URI path, configured as the base path setting in the ProxyEndpoint, in the request below is `/weather`).
    
    
    http://ORG_NAME-test.apigee.net/weather/forecastrss?w=12797282

After you submit more than one request within a minute, you should see the following error message:
    
    
    {
       "fault":{
          "faultstring":"policies.ratelimit.QuotaViolation",
          "detail":{
             "errorcode":"policies.ratelimit.QuotaViolation"
          }
       }
    }

This indicates that the `Quota` policy is being enforced by Apigee.

## Policy-based fault handling

Note the format of the error message above. It contains a `faultstring` property and an `errorcode` property. In many cases, you need to implement some behavior to handle these errors. For example, you may wish to issue a customized message to a developer whose app has exceeded the `Quota`.

For more on fault handling, see [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

## Best practices: Common policy sets

To meet basic management requirements, API proxies usually enforce the following policies:

### Basic API key validation

**ProxyEndpoint Request Flow:**

  1. `SpikeArrest`
  2. `XMLThreatProtection` or `JSONThreatProtection`
  3. API key validation
  4. `Quota`
  5. `ResponseCache`

**ProxyEndpoint Response Flow:**

  1. `ResponseCache`



### Basic transformation: JSON to XML

**Request Flow:**

  1. `SpikeArrest`
  2. `JSONThreatProtection`
  3. API key validation
  4. `Quota`
  5. JSONToXML

**Response Flow:**

  1. `XMLToJSON`
  2. `ResponseCache`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
