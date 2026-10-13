---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development/
title: Best practices for API proxy design and development with Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:12.136381+00:00
---

# Best practices for API proxy design and development with Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Best practices for API proxy design and development with Apigee Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document provides a set of best practices for developing API proxies with Apigee.

The topics that are covered here include design, coding, policy use, monitoring, and debugging. The information has been gathered by the experience of developers working with Apigee to implement successful API programs. This is a living document and will be updated from time to time.

In addition to the guidelines here, you might also find [Introduction to antipatterns](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/intro) useful.

## Development standards

### Comments and Documentation

  * Provide inline comments in the `ProxyEndpoint` and `TargetEndpoint` configurations. Comments enhance readability for a Flow, especially where policy file names are not sufficiently descriptive to express the underlying functionality of the Flow.
  * Make comments useful. Avoid obvious comments.
  * Use consistent indentation, spacing, vertical alignment, and so on.



### Framework-style coding

Framework-style coding involves storing API proxy resources in your own version control system for reuse across local development environments. For example, to reuse a policy, store it in source control so that developers can sync to it and use it in their own proxy development environments.

  * To enable DRY (don't repeat yourself), where possible, policy configurations and scripts should implement specialized, reusable functions. For example, a dedicated policy to extract query parameters from request messages could be called `ExtractVariables.ExtractRequestParameters`.
  * Clean up unused policies and resources (JavaScript, Java, XSLT, ) from API proxies, especially large resources that have the potential to slow down import and deploy procedures.



### Naming Conventions

  * The policy `name` attribute and the XML policy file name must be identical.
  * The Script and [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) policy `name` attribute and the name of the resource file should be identical.
  * `DisplayName` should accurately describe the policy’s function to someone who has never worked with that API proxy before.
  * Name policies according to their function. Apigee recommends that you establish a consistent naming convention for your policies. For example, use short prefixes followed by a sequence of descriptive words separated by dashes. For example, `AM-xxx` for [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). See also [apigeelint tool](https://github.com/apigee/apigeelint).
  * Use proper extensions for resource files, `.js` for JavaScript, `.py` for python, and `.jar` for Java JAR files.
  * Variable names should be consistent. If you choose a style, such as camelCase or under_score, use it throughout the API proxy.
  * Use variable prefixes, where possible, to organize variables based on their purpose, for example, `Consumer.username` and `Consumer.password`.



## API proxy development

### Initial Design Considerations

**Warning:** Do not call the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) from inside API proxies. The API is used for administrative management purposes, not API flow logic. Due to longer-lived cache entries on the Apigee API servers, you may not see updated data immediately in your proxy flows, particularly if you are doing quick writes and then reads. Coding workarounds for this behavior can impact your proxies' performance. 

Use [policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy) in API proxies instead.

  * For guidance on RESTful API design, download the e-book [ Web API Design: The Missing Link](https://cloud.google.com/apigee/resources/ebook/web-api-design-register/).
  * Leverage Apigee policies and functionality wherever possible to build API proxies. Avoid coding all proxy logic in JavaScript, Java, or Python resources.
  * Construct Flows in an organized manner. Multiple Flows, each with a single condition, are preferable to multiple conditional attachments to the same PreFlow and Postflow.
  * As a 'failsafe', create a default API proxy with a ProxyEndpoint BasePath of `/`. This can be used to redirect base API requests to a developer site, to return a custom response, or perform another action more useful than returning the default `messaging.adaptors.http.flow.ApplicationNotFound`.
  * For optimal performance, Apigee recommends using no more than 3,000 API proxy basepaths per Apigee environment or environment group. Exceeding this recommendation can result in increased latency for all new and existing API proxy deployments.
  * Use TargetServer resources to decouple TargetEndpoint configurations from concrete URLs, supporting promotion across environments.  
See [Load balancing across backend servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers).
  * If you have multiple RouteRules, create one as the 'default', that is, as a RouteRule with no condition. Ensure that the default RouteRule is defined last in the list of conditional Routes. RouteRules are evaluated top-down in ProxyEndpoint. See [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).
  * API proxy bundle size: API proxy bundles cannot be larger than 15MB.
  * API versioning: For Apigee's thoughts and recommendations on API versioning, see [Versioning](https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf) in the _Web API Design: The Missing Link_ e-book.



### Enabling CORS

Before publishing your APIs, you'll need to add the CORS policy to the **request PreFlow of the ProxyEndpoint** to support client-side cross-origin requests.

CORS (Cross-origin resource sharing) is a standard mechanism that allows JavaScript XMLHttpRequest (XHR) calls executed in a web page to interact with resources from non-origin domains. CORS is a commonly implemented solution to the [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy) that is enforced by all browsers. For example, if you make an XHR call to the Twitter API from JavaScript code executing in your browser, the call will fail. This is because the domain serving the page to your browser is not the same as the domain serving the Twitter API. CORS provides a solution to this problem by allowing servers to _opt-in_ if they wish to provide cross-origin resource sharing.

For information about enabling CORS on your API proxies before publishing the APIs, see [Adding CORS support to an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-cors-support-api-proxy).

**Note:** Most browsers support CORS. You can find a comprehensive list of supported browsers [here](https://caniuse.com/cors). For an in-depth description of CORS, see the [Cross-Origin Resource Sharing W3C Recommendation](https://www.w3.org/TR/2020/SPSD-cors-20200602/). 

If you are using a [cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/cache/persistence-tools) on your API proxy, you must ensure that the response of the CORS policy is not cached.

## Message payload size

The message payload size in request or response flows for Apigee is restricted _by default_ to 10MB. Users who require large payload processing can configure a higher limit using the `<Properties>` element in the [ProxyEndpoint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-proxyendpointconfigurationelements) or [TargetEndpoint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint-targetendpointconfigurationelements) configurations of their API proxies.

For more information on using `response.payload.parse.limit` or the `request.payload.parse.limit` properties to configure a maximum payload size up to 30MB for request or response flows, see the [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).

Note that exceeding the specified message size results in a `protocol.http.TooBigBody` error. 

Consider the following recommended strategies for handling large message sizes in Apigee:

  * We highly recommend isolating API proxies that frequently handle large payloads in a dedicated environment to avoid a potential "noisy neighbor" scenario. System CPU and memory resources are consumed in greater quantities by proxies that manage large payloads, especially when used in conjunction with policies that interact with large payloads.
  * We also recommend limiting the use of policies to interact with large payloads. Using policies to repeatedly parse and copy request or response payloads can negatively impact system performance. 
  * Organizations that handle large volumes of high payload requests are encouraged to provide additional IP addresses to avoid port exhaustion due to horizontal scaling.
  * Consider streaming requests and responses. Note that when you stream, policies no longer have access to the message content. See [Streaming requests and responses](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-streaming).
  * If your organization uses [Pay-as-you-go billing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview), we recommend using [configurable limits for large payloads](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference) only for API proxies deployed in Comprehensive environment.



## Fault Handling

  * Leverage FaultRules to handle all fault handling. (RaiseFault policies are used to stop message Flow and send processing to the FaultRules Flow.)
  * Within the FaultRules Flow, use an [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) to build the fault response, not a [RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy). Conditionally execute AssignMessage policies based on the fault type that occurs.
  * Always includes a default 'catch-all' fault handler so that system-generated faults can be mapped to customer-defined fault response formats.
  * If possible, always make fault responses match any standard formats available in your company or project.
  * Use meaningful, human-readable error messages that suggest a solution to the error condition.



See [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

## Persistence

### Key/Value Maps

  * Use key/value maps only for limited data sets. They are not designed to be a long-term data store.
  * Consider performance when using key/value maps as this information is stored in the Cassandra database.



See [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy).

### Response Caching

  * Do not populate the response cache if the response is not successful or if the request is not a GET. Creates, updates, and deletes should not be cached. `<SkipCachePopulation>response.status.code != 200 or request.verb != "GET"</SkipCachePopulation>`
  * Populate cache with a single consistent content type (for example, XML or JSON). After retrieving a responseCache entry, then convert to the needed content type with JSONtoXML or XMLToJSON. This will prevent storing double, triple, or more data.
  * Ensure that the cache key is sufficient to the caching requirement. In many cases, the `request.querystring` can be used as the unique identifier.
  * Do not include the API key (`client_id`) in the cache key, unless explicitly required. Most often, APIs secured only by a key will return the same data to all clients for a given request. It is inefficient to store the same value for a number of entries based on the API key.
  * Set appropriate cache expiration intervals to avoid dirty reads.
  * Whenever possible, try to have the response cache policy that populates the cache execute at the ProxyEndpoint response PostFlow as late as possible. In other words, have it execute after translation and mediation steps, including JavaScript-based mediation and conversion between JSON and XML. By caching mediated data, you avoid the performance cost of executing the mediation step each time you retrieve cached data. 

Note that you might want to instead cache unmediated data if mediation results in a different response from request to request.

  * The response cache policy to lookup the cache entry should occur in the ProxyEndpoint request PreFlow. Avoid implementing too much logic, other than cache key generation, before returning a cache entry. Otherwise, the benefits of caching are minimized.
  * In general, you should always keep the response cache lookup as close to the client request as possible. Conversely, you should keep the response cache population as close to the client response as possible.
  * When using multiple, different response cache policies in a proxy, follow these guidelines to ensure discrete behavior for each: 
    * Execute each policy based on mutually exclusive conditions. This will help ensure that only one of multiple response cache policies executes.
    * Define different cache resources for each response cache policy. You specify the cache resource in the policy's `<CacheResource>` element.



See [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy).

## Policy and custom code

### Policy or custom code?

  * Use built-in policies first and foremost (when possible). Apigee policies are hardened, optimized, and supported. For example, use the standard [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) and [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) policies instead of JavaScript (when possible) to create payloads, extract information from payloads (XPath, JSONPath), and so on.
  * JavaScript is preferred over Python and Java. However, if performance is the primary requirement, Java should be used over JavaScript.



### JavaScript

  * Use JavaScript if it's more intuitive than Apigee policies (for example, when setting `target.url` for many different URI combinations).
  * Complex payload parsing such as iterating through a JSON object and Base64 encoding/decoding.
  * [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) has a time limit, so infinite loops are blocked.
  * Always use JavaScript Steps and put files in `jsc` resources folder. [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) type pre-compiles the code at deployment time.



### Java

**Warning:** For JavaCallout policies, reliance on Java libraries that are included with Apigee is not supported. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release.

  * Use Java if performance is the highest priority, or if the logic cannot be implemented in JavaScript.
  * Include Java source files in source code tracking.



See [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) for information on using Java in API proxies.

### Python

  * Do not use Python unless absolutely required. Python scripts can introduce performance bottlenecks for simple executions, as it is interpreted at runtime.



## Script Callouts (Java, JavaScript, Python)

  * Use a global try/catch, or equivalent.
  * Throw meaningful exceptions and catch these properly for use in fault responses.
  * Throw and catch exceptions early. Do not use the global try/catch to handle all exceptions.
  * Perform null and undefined checks, when necessary. An example of when to do this is when retrieving optional flow variables.
  * Avoid making HTTP/S requests inside of a script callout. Instead, use the [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) as the policy handles connections gracefully.



### JavaScript

  * JavaScript on the API Platform supports XML via [E4X](https://svn.wso2.org/repos/wso2/tags/carbon/0.1alpha/mashup/java/xdocs/e4xquickstart.html).



See [JavaScript object model](https://docs.cloud.google.com/apigee/docs/api-platform/reference/javascript-object-model).

### Java

**Warning:** For JavaCallout policies, reliance on Java libraries that are included with Apigee is not supported. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release.

  * When accessing message payloads, try to use `context.getMessage()` vs. `context.getResponseMessage` or `context.getRequestMessage`. This ensures that the code can retrieve the payload, in both request and response flows.
  * Import libraries to the Apigee organization or environment and do not include these in the JAR file. This reduces the bundle size and will let other JAR files access the same library repository.
  * Import JAR files using the Apigee resources API rather than including them inside the API proxy resources folder. This will reduce deployment times and allow the same JAR files to be referenced by multiple API proxies. Another benefit is class loader isolation.
  * Do not use Java for resource handling (for example, creating and managing thread pools).



### Python

  * Throw meaningful exceptions and catch these properly for use in Apigee fault responses



See [PythonScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy).

## ServiceCallouts

  * There are many valid use cases for using proxy chaining, where you use a service callout in one API proxy to call another API proxy. If you use proxy chaining, be sure to avoid _infinite loop_ recursive callouts back into the same API proxy. 

If you're connecting between proxies that are in the same organization and environment, be sure to see [Chaining API proxies together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies) for more on implementing a local connection that avoids unnecessary network overhead.

  * Build a ServiceCallout request message using the AssignMessage policy, and populate the request object in a message variable. (This includes setting the request payload, path, and method.)
  * The URL that is configured within the policy requires the protocol specification, meaning the protocol portion of the URL, `https://` for example, cannot be specified by a variable. Also, you must use separate variables for the domain portion of the URL and for the rest of the URL. For example: `https://example.com`.
  * Store the response object for a ServiceCallout in a separate message variable. You can then parse the message variable and keep the original message payload intact for use by other policies.



See [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy).

## Accessing entities

### AccessEntity Policy

  * For better performance, look up apps by `uuid` instead of app name.



See [AccessEntity policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy).

### Logging

  * Use a common syslog policy across bundles and within the same bundle. This will keep a consistent logging format.



See [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy).

## Monitoring

Cloud customers are not required to check individual components of Apigee (Routers, Message Processors, and so on). Apigee's Global Operations team is thoroughly monitoring all of the components, along with API health checks, given health check requests by the customer.

### Apigee Analytics

Analytics can provide non-critical API monitoring as error percentages are measured.

See [Analytics dashboards](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards).

### Debug

The trace tool in the [Apigee UI](https://apigee.google.com) is useful for debugging runtime API issues, during development or production operation of an API.

See [Using the Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace).

## Security

  * Use IP address restriction policies to limit access to your test environment. Allow access for the IP addresses of your development machines or environments and disallow all others. See [AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy).
  * Always apply content protection policies (JSON and or XML) to API proxies that are deployed to production. See [JSONThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy).
  * See the following topics for more security best practices: 
    * [XMLThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy)
    * [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection)
    * [SOAPMessageValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-validation-policy)



## Custom Logic in API Proxies

A common requirement when building API Proxies is to include some logic for processing requests and/or responses. While many requirements can be met from a predefined set of steps/actions/policies like verifying a token or applying a quota or responding with a cached object, one often may require access to programmability. For example, looking up a location (endpoint) from a routing table based on a key found in a request and dynamically applying a target endpoint or a custom/proprietary authentication method, etc. 

Apigee provides a developer with multiple options to deal with such custom logic. This document will explore those options and when to use which: 

Policy | Policy use cases  
---|---  
JavaScript and PythonScript |  When to use:

  * The JavaScript and PythonScript policies are equivalent in capability. A developer's familiarity in a language is typically the motivation of picking one over the other.
  * The JavaScript and PythonScript policies are best suited for processing logic inline that is not overly complex and does not require the use of third-party libraries.
  * These policies are not as performant as the JavaCallout policy.

When not to use:

  * Apigee's API gateway is not an application server (nor does it provide the full JavaScript runtime like `node.js`). If the callout always takes over a second to process, the logic most likely does not belong in the gateway and should be part of the underlying service instead.

[ Best Practice](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#policyandcustomcode-python): Apigee recommends JavaScript over PythonScript, since JavaScript offers better performance.  
JavaCallout |  When to use:

  * The performance of processing the logic inline is critical.
  * Existing Java libraries provide much of the logic.

When not to use:

  * Apigee's API gateway is not an application server and is not meant to load frameworks like Spring, JEE, etc. If the callout typically takes over a second to process, the logic can be considered as functional (business logic). Consider externalizing as a service.
  * To protect the Apigee API gateway from abuse, there are restrictions placed on the type of code that can be executed. For example, Java code that tries to access certain crypto libraries or access the file system is blocked from execution.
  * Java applications, especially those that rely on third party libraries, can bring in many (and large) JAR files. These can slow down the bootup time of the gateways.

  
ExternalCallout |  When to use:

  * Ideally suited to externalize custom logic and allow the custom logic to access (and if necessary modify) the message context.
  * External callouts implement gRPC and may have better performance than a ServiceCallout.
  * When using Apigee or Apigee hybrid on Google Cloud consider using Cloud Functions or Cloud Run to host such logic.
  * As an effective replacement for the Hosted Targets feature in Apigee Edge.

When not use:

  * For lightweight logic that can execute quickly, inline.

  
ServiceCallout |  When to use:

  * Complex logic is best implemented outside the gateway. This logic can have its own life cycle (releases and versioning) and does not affect the functioning of the gateway.
  * When the REST/SOAP/GraphQL endpoint already exists or can be easily implemented
  * When using Apigee or Apigee hybrid on Google Cloud, consider using Cloud Functions or Cloud Run to host such logic.
  * As an effective replacement for the Hosted Targets feature in Apigee Edge.

When not use: 

  * For lightweight logic that can execute quickly, inline
  * The API proxy must transfer context (like variables) or receive context from the external implementation

  
  
To summarize: 

  1. If the logic is simple or trivial, use JavaScript (preferably) or PythonScript.
  2. If inline logic requires better performance than JavaScript or PythonScript, use JavaCallout.
  3. If the logic must be externalized, then use ExternalCallout.
  4. If you already have external implementations and/or developers are familiar with REST, use ServiceCallout.



The following figure illustrates this process: 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/best-practices-custom-logic.svg)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
