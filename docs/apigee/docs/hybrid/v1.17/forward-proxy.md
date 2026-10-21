---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy/
title: Configure forward proxying for API proxies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:11:12.854766+00:00
---

# Configure forward proxying for API proxies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure forward proxying for API proxies Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/forward-proxy.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/forward-proxy.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/forward-proxy.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/forward-proxy.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/forward-proxy.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/forward-proxy.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/forward-proxy.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/forward-proxy.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/forward-proxy.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/forward-proxy.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/forward-proxy.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/forward-proxy.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/forward-proxy.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/forward-proxy.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/forward-proxy.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/forward-proxy.html)



**Note:** Both Apigee and Apigee hybrid support [forward proxy functionality](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#forward-proxying). Use the instructions on this page to configure forward proxies for hybrid rather than the general Apigee functionality. 

Forward proxies provide a single point through which multiple machines send requests to an external server. They can enforce security policies, log and analyze requests, and perform other actions so that requests adhere to your business rules.

Using a forward proxy in Apigee hybrid, you can intercept and manage all egress traffic from your Kubernetes cluster. This includes API proxy requests to Target Endpoints and communication with `*.googleapis.com` that the hybrid runtime makes for its debug and analytics pipeline and for policies like [MessageLogging](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) and the AI policies (such as [SanitizeUserPrompt](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy) and [SemanticCacheLookup](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy)).

To use an HTTP forward proxy between hybrid and the TargetEndpoint, you must configure the outbound proxy settings in your overrides file. These environment-scoped properties route target requests from hybrid to the HTTP forward proxy. You also need to ensure `use.proxy` is set to "true" for any TargetEndpoint that you want to go through an HTTP forward proxy. See the bottom of the page for instructions.

To configure a hybrid environment for forwarding proxying, add the [`envs.httpProxy` property](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs) to your overrides file and apply it to the cluster. For example:
    
    
    envs:
      - name: test
        httpProxy:
          scheme: HTTP
          host: 10.12.0.47
          port: 3128
          ...

**NOTE:** The `scheme` must be HTTP and must be uppercase.

For details on each of the `envs.httpProxy` configuration properties refer to the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs).

Forward proxying is configured for an environment; all traffic going from API proxies in that environment to backend targets goes through the specified HTTP forward proxy. If the traffic for a specific target of an API proxy should go directly to the backend target, bypassing the forward proxy, then set the following property in the TargetEndpoint to override the HTTP forward proxy:
    
    
    <Property name="use.proxy">false</Property>

For more information on setting the TargetEndpoint properties, including how to configure the connection to the target endpoint, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).

Set `use.proxy` to "true" for any TargetEndpoint that you want to go through an HTTP forward proxy:
    
    
    <Property name="use.proxy">true</Property>

If you have a firewall on the backend which is configured to expect **Host Header** always to include the _backend_ server host name, while the Message Processor is sending the _proxy server_ hostname, perform the following to configure this option:

Set the property `use.proxy.host.header.with.target.uri `to true in the TargetEndpoint as shown in the following example:

**Sample TargetEndpoint configuration:**
    
    
      <TargetEndpoint name="default">
        <HTTPTargetConnection>
          <URL>https://mocktarget.apigee.net/json</URL>
          <Properties>
            <Property name="use.proxy.host.header.with.target.uri">true</Property>
          </Properties>
        </HTTPTargetConnection>
      </TargetEndpoint>

For details on the `use.proxy.host.header.with.target.uri` property, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).

**Important note on external calls:** Configuring non-API proxy forwarding using [`httpProxy`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#httpproxy) without also setting [`envs.httpProxy`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs) will not apply the proxy configuration to Apigee Runtime's external calls to services like Pub/Sub or other Google Cloud APIs. 

If you only specify `httpProxy`, you must also ensure that `*.googleapis.com` is allowlisted for your Apigee Runtime pods to enable connectivity to these services. 

## AI policies and the forward proxy

The Model Armor policies ([SanitizeUserPrompt](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy) and [SanitizeModelResponse](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy)) and the semantic cache policies ([SemanticCacheLookup](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy) and [SemanticCachePopulate](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy)) make outbound calls while processing requests and responses. These include the Model Armor sanitization calls, and the Agent Platform text embeddings, Vector Search `findNeighbors`, and `upsertDatapoints` calls.

When a forward proxy is configured for the environment with [`envs.httpProxy`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs), all of these above calls are routed through the forward proxy by default, with no policy-level configuration required. This behavior is true even for endpoints that are not under `*.googleapis.com`, such as the public Vector Search endpoint that SemanticCacheLookup calls.

These policy calls to external services are treated the same as the runtime's trace and analytics traffic: setting [`envs[].managementCallsSkipProxy`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-managementcallsskipproxy) to `true` makes them skip the forward proxy and egress directly instead. Skipping the forward proxy applies to all of the calls listed above (i.e., sanitization, text embeddings, `findNeighbors`, and `upsertDatapoints`). This proxy-level forward proxy behavior is separate from a TargetEndpoint, whose forward proxy behavior is controlled by its own `use.proxy` property.

**Note:** When a SemanticCacheLookup policy is configured to use a private Vector Search endpoint through Private Service Connect (PSC), the similarity search call is sent over a direct gRPC connection to the private endpoint and does not go through the forward proxy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
