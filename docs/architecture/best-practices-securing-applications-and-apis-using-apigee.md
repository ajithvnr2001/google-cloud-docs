---
url: https://docs.cloud.google.com/architecture/best-practices-securing-applications-and-apis-using-apigee/
title: Best practices for securing your applications and APIs using Apigee \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:02.986702+00:00
---

# Best practices for securing your applications and APIs using Apigee  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/best-practices-securing-applications-and-apis-using-apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for securing your applications and APIs using Apigee Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-04-01 UTC

This document describes best practices that can help you to secure your applications and APIs using [Apigee API management](https://docs.cloud.google.com/apigee) and the following Google Cloud products:

  * [Google Cloud Armor](https://cloud.google.com/security/products/armor)
  * [reCAPTCHA ](https://cloud.google.com/security/products/recaptcha)
  * [Cloud CDN](https://cloud.google.com/cdn)



This document is intended for API architects, security architects, and engineering leads who manage the infrastructure of an application and who want to expose secure, scalable, and performant APIs.

This document uses a series of example architectures to demonstrate best practices for using Apigee API management. This document also discusses best practices for using [web app and API protection (WAAP)](https://docs.cloud.google.com/solutions/web-app-and-api-protection), a comprehensive security solution that you can use to help secure your applications and APIs.

This document assumes that you are familiar with networking, APIs, and Google Cloud.

### Apigee API management

[Apigee](https://docs.cloud.google.com/apigee) is a platform for developing and managing APIs. By adding a proxy layer to your services, Apigee provides an abstraction or facade that helps you to secure your backend service APIs.

Users can interact with applications using OAuth 2.0 and allow-listed IP address ranges. As shown in the following image, users can interact with an application, and data and services are exposed in a bidirectional flow.

![Security points between user interaction with an application and the backend.](https://docs.cloud.google.com/static/architecture/images/apigee-api.png)

The security points are as follows:

  * Users: 
    * OAuth 2.0
    * IP address access control
  * Applications 
    * API keys
    * OAuth 2.0
    * TLS
  * Developers and partners 
    * SSO
    * RBAC
  * APIs 
    * OAuth 2.0
    * OpenID Connect
    * Quotas
    * Spike arrest
    * Threat protection
  * API team 
    * IAM RBAC
    * Federated logic
    * Data masking
    * Audit logs
  * Backend 
    * Private networking
    * Mutual TLS
    * IP address access control



As the preceding image shows, you can use different security mechanisms in an application, such as API key or OAuth 2.0 with Transport Layer Security (TLS). You can also add rate limiting, threat protection policies, and configure mutual TLS to the backend of your API layer.

To help you to manage access for an API team within the Apigee platform, Apigee has role-based access control (RBAC) and federated login.

We recommend that you use the Apigee [default policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy) to secure your APIs. The policies are as follows:

  * **Traffic Management**. Helps you to configure caching, control quotas, mitigate the effects of spikes, and control API traffic.
  * **Message level protection**. Lets you inspect and validate request payloads to help protect your backend from malicious attackers.
  * **Security**. Helps you to control access to your APIs.



You can attach one or more of these policies to your proxy layer. The following table lists the security use case for each policy, categorized by policy type.

Policy type | Policy name | Security use case  
---|---|---  
Traffic management | [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) | Applies rate limiting to the number of requests sent to the backend.  
Traffic management | [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) | Helps your organization to enforce quotas (the number of API calls made) for each consumer.  
Traffic management | [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) | Caches responses, reducing the number of requests to the backend.  
Message-level protection | [OASValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy) | Validates incoming requests or response messages against an OpenAPI 3.0 Specification (JSON or YAML).  
Message-level protection | [SOAPMessageValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-validation-policy) | Validates XML messages against a schema of your choice. Validates SOAP messages against a WSDL and determines whether JSON and XML messages are correctly formed.  
Message-level protection | [JSONThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy) | Helps to mitigate the risk of content-level attacks by letting you specify limits on JSON structures like arrays and strings.  
Message-level protection | [XMLThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy) | Helps you to address XML vulnerabilities and mitigate the risk of attacks by evaluating message content and detecting corrupt or malformed messages before they can be parsed.  
Message-level protection | [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) | Evaluates content against predefined regular expressions and rejects it if the expression is true.  
Security | [BasicAuthentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy) | Base64 encodes and decodes user credentials.  
Security | [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) | Enforces the verification and the validation of API keys at runtime. Only allows applications with approved API keys associated with your [API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product) to access your APIs.  
Security | [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) | Performs OAuth 2.0 grant type operations to generate and validate access tokens.   
Security | [JWS and JWT policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview) | Generates, verifies, and decodes JSON Web Tokens (JWT) and JSON Web Signatures (JWS).  
Security | [HMAC policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/hmac-policy) | Computes and verifies hash-based message authentication code (HMAC) for authentication and application-level integrity checks.  
Security | [SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy) | 

  * Validates incoming messages that contain a digitally signed SAML assertion. 
  * Generates SAML assertions to outbound XML requests.

  
Security | [CORS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy) | Lets you set [cross-origin resource sharing (CORS)](https://docs.cloud.google.com/livestream/docs/how-to/configure-cors) headers for APIs that are consumed by web applications.  
  
We recommend that you use [Cloud Armor](https://docs.cloud.google.com/armor) for IP address-based and geo-based access control. However, in cases where it's not possible, you can use the [AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy). To help you to secure the connections from Apigee to your backend, Apigee also provides [keystore management](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls), which lets you configure the keystore and truststore for TLS handshakes.

You can use Apigee to create [API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product) that let you bundle your API operations and make them available to application developers for consumption. An API product bundles together one or more operations. An operation specifies an API proxy and resource paths that can be accessed on that proxy. An operation can also limit access by HTTP methods and by quota.

You use API products to control access to your APIs. By defining one or more API products in a developer application, you can restrict access to proxies with an API key. For example, mobile applications which are used by customers can only perform a POST operation on the `/v1/payments` endpoint, in this case, `https://$DOMAIN/v1/payments`. In another example, call center applications which are used by call center staff can perform operations like PUT or DELETE on the `/payments` endpoint, such as `https://$DOMAIN/v1/payments/1234`, to revert or reverse payments.

## Initial architecture

This section describes an example microservices architecture with the services deployed in the data center and cloud provider. The following architecture best practices demonstrate how you can iterate and improve the initial architecture.

![Example microservices architecture with the services
deployed in the data center and cloud provider.](https://docs.cloud.google.com/static/architecture/images/initial-architecture.svg)

The initial architecture is as follows:

  * The payments and accounts services are hosted in the data center, and the money-transfer service is hosted in Google Cloud.
  * The [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) controls and configures ingress to the services.
  * The external Application Load Balancer forwards the request to the appropriate backend or third-party service and handles the TLS handshake.



In its initial state, the example architecture has the following constraints:

  * It's unlikely to scale.
  * It's unlikely to protect a system from malicious attacks
  * It doesn't reflect consistent best practices for security and logging because these services are developed and maintained by different teams within the organization.



## Architecture best practices

Apigee can add value and make it easier to expose your services to your consumers by implementing a standard set of security policies across all APIs. This section discusses best practices for using Apigee to help secure your APIs.

### Use Apigee as a proxy layer

The following diagram shows the initial architecture with the addition of Apigee as a proxy (facade) layer:

![Apigee as a proxy layer.](https://docs.cloud.google.com/static/architecture/images/apigee-proxy.svg)

Apigee is provisioned in a Google Cloud project and the runtime is provisioned and peered in a tenant project using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). To help secure your system, instead of sending data through the internet, you can use Apigee as a proxy layer to establish a direct (private) connection to your data center using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

The request flow is as follows:

  1. The client sends the request to the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with the credentials for the application—for example, a key, token, or certificate.
  2. The load balancer routes the request to Apigee.
  3. Apigee processes the request, executes the security policies as described in Apigee API management, and allows or denies the request. Apigee can also be used to route the request to different backends based on the client, the request, or both the client and the request.
  4. Apigee forwards the request to the GKE backends directly through internal IP addresses. The communication between Apigee and the money-transfer service can happen over an RFC 1918 address (internal IP address) because they are within the peered network.
  5. Apigee sends the request to the private data center backends through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).
  6. Apigee sends the request to third-party services through Apigee NAT IP address provisioning.



### Use Cloud Armor as a WAF layer with Apigee

You can add [Cloud Armor](https://docs.cloud.google.com/armor) to the architecture to increase your security perimeter. Cloud Armor is part of the global load-balancing infrastructure for Google Cloud. It provides web application firewall (WAF) capabilities and helps to prevent distributed denial of service (DDoS) attacks. It can also help you to mitigate the threat to applications from the risks listed in the [OWASP Top 10](https://owasp.org/www-project-top-ten/).

You can configure rules and policies in Cloud Armor to evaluate every call made by the client that hits the external Application Load Balancer. You can also automate the configuration of Cloud Armor policies. For more information about how to configure rules in Cloud Armor, see the Cloud Armor [How-to guides](https://docs.cloud.google.com/armor/docs/how-to).

The following diagram shows the example architecture with both Apigee and Cloud Armor in place:

![Architecture with Cloud Armor.](https://docs.cloud.google.com/static/architecture/images/apigee-cloud-armor.svg)

The flow of events in this architecture is similar to those discussed in Use Apigee as a proxy layer earlier in this document. The request flow is as follows:

  1. The client sends the request to the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with the credentials for the application—for example, a key, token, or certificate.
  2. Cloud Armor filters the request because the external Application Load Balancer has it enabled. It enforces and evaluates all the configured rules and policies. If any rule is violated, Cloud Armor rejects the request and gives you an error message and status code.
  3. If there are no Cloud Armor rule violations, the external Application Load Balancer routes the request to Apigee.
  4. Apigee processes the request, executes the security policies, and allows or denies the request. It can also be used to route the request to different backends based on the client, the request, or both the client and the request.
  5. Apigee forwards the request to the GKE backends directly through internal IP addresses. The communication between Apigee and the money-transfer service can happen over an RFC 1918 address (internal IP address) because they are within the peered network.
  6. Apigee sends the request to the private data center backends through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).
  7. Apigee sends the request to third-party services through Apigee NAT IP address provisioning.



### Use WAAP

To further enhance your security profile, you can also use WAAP, which brings together Cloud Armor, reCAPTCHA, and Apigee to help protect your system against DDoS attacks and bots. It also provides WAF and API protection.

We recommend WAAP for enterprise use cases where the API calls are made from a website and mobile applications. You can set applications to load the reCAPTCHA libraries to generate a reCAPTCHA token and send it along when they make a request.

This following diagram shows the workflow:

![Request flow for WAAP.](https://docs.cloud.google.com/static/architecture/images/waap-workflow.png)

The request flow in the preceding diagram is as follows:

  * (1) All HTTP(S) requests by customers and API consumers are sent to the external Application Load Balancer.
  * (2) The first point of contact on the WAAP solution is Cloud Armor.
  * (2a) If none of these rules are triggered by the Cloud Armor policies, a request is sent to the reCAPTCHA API to evaluate whether the incoming traffic is a legitimate request or not.
  * (3a) If it's a legitimate request, then the request is forwarded to the backend.
  * (2b) If the request isn't legitimate, Cloud Armor can deny the request and send a 403 response code to the user.
  * (3b) For any API requests, after the Cloud Armor OWASP rules and DDoS protection are evaluated, the request is then forwarded to Apigee to check the validity of the API request.
  * (4) Apigee determines whether the API keys or access tokens used in the request are valid. If Apigee determines that the request isn't legitimate, Apigee can send a 403 response code.
  * (5) If the request is legitimate, Apigee forwards the request to the backend.



The following diagram shows the architecture of WAAP with Cloud Armor, reCAPTCHA, and Apigee for the API requests.

![Request flow for WAAP with Cloud Armor,
reCAPTCHA, and Apigee.](https://docs.cloud.google.com/static/architecture/images/apigee-cloud-armor-recaptcha.svg)

The request flow in the preceding diagram is as follows:

  1. The client sends the request to the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with the credentials for the application—for example, a key, token, or certificate.
  2. Because the external Application Load Balancer has Cloud Armor enabled, Cloud Armor selects the request. It enforces and evaluates all the configured rules and policies. If any rule is violated, Cloud Armor rejects the request with an error message and status code.
  3. For website calls such as a form submission for a login page, Cloud Armor is integrated with reCAPTCHA. reCAPTCHA evaluates incoming traffic and adds risk scores to legitimate traffic. For traffic that isn't legitimate, Cloud Armor can deny the request.
  4. If there are no Cloud Armor rule violations, the external Application Load Balancer routes the API request to Apigee.
  5. Apigee processes the request, executes the security policies, and allows or denies the request. Apigee can also be used to route the request to different backends based on the client, the request, or both the client and the request.
  6. Apigee forwards the request to the GKE backends directly through internal IP addresses. The communication between Apigee and the money-transfer service can happen over the RFC 1918 address, which is an internal IP address, because they are both within the peered network.
  7. Apigee sends the request to the private data center backends through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).
  8. Apigee sends the request to third-party services through [Apigee NAT IP address provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-provisioning#set-up-apigee-nat-ip-provisioning).



### Use Cloud CDN for caching

[Cloud CDN](https://docs.cloud.google.com/cdn) uses the Google global network to serve content closer to users, which accelerates response times for your websites and applications. Cloud CDN also offers caching capabilities that help you to secure the backend by returning the response from its cache. By caching frequently accessed data at a [Google Front End (GFE)](https://docs.cloud.google.com/docs/security/infrastructure/design#google_front_end_service) , which is at the edge of the Google network, it keeps the data as close as possible to users and allows for the fastest possible access.

Cloud CDN also helps organizations seamlessly handle seasonal spikes in traffic —for example, spikes that might occur during the holiday or back-to-school seasons. This approach to caching helps to improve reliability and user experience in an ecosystem. It can also help to minimize web server load, compute, and network usage. To implement this architecture, you must enable Cloud CDN on the load balancer which serves traffic for Apigee.

Cloud CDN can be used with any of the options discussed in this document. The following diagram shows the initial example architecture of WAAP with the addition of Cloud CDN.

![Request flow with Cloud CDN.](https://docs.cloud.google.com/static/architecture/images/apigee-cdn.svg)

The request flow shown in the preceding diagram is as follows:

  1. The client uses reCAPTCHA libraries to get a token and sends the request to the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with the credentials for the application—for example, a key, token, or certificate.
  2. Cloud CDN checks the cache with the cache key and returns the response if the cache hit is true.
  3. If the cache hit is false, Cloud Armor filters the request because the external Application Load Balancer has Cloud Armor enabled. Cloud Armor enforces and evaluates all the configured rules and policies. If any rule is violated, it rejects the request with an error message and status code.
  4. Cloud Armor is integrated with reCAPTCHA, which evaluates the legitimate incoming traffic with risk scores. For traffic that isn't legitimate, Cloud Armor can deny the request.
  5. If there are no Cloud Armor rule violations, the external Application Load Balancer routes the request to Apigee.
  6. Apigee processes the request, executes the security policies as described in Apigee API management, and allows or denies the request. It can also be used to route the request to different backends based on the client, the request, or both the client and the request.
  7. Apigee forwards the request to the GKE backends directly through internal IP addresses. The communication between Apigee and the money-transfer service can happen over the RFC 1918 address, which is an internal IP address, because they are within the peered network.
  8. Apigee sends the request to the private data center backends through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).
  9. Apigee sends the request to third-party services through Apigee NAT IP address provisioning.
  10. When a response flows back to the client, Cloud CDN caches it so that it can return the response from the cache for future calls.



## What's next

  * Learn more about [Apigee provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro).
  * Read about [multi-layer API security with Apigee and Cloud Armor](https://cloud.google.com/blog/products/api-management/api-security-with-apigee-and-google-cloud-armor).
  * Learn how to deliver [high-performing global APIs with Apigee X and Cloud CDN](https://cloud.google.com/blog/products/api-management/api-performance-and-availability-with-apigee-x-and-cloud-cdn).
  * Read and ask questions in the [Apigee community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee).
  * Explore the [Apigee repository](https://github.com/apigee/devrel) on GitHub.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-01 UTC."],[],[]] 
