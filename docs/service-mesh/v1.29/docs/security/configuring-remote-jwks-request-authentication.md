---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/security/configuring-remote-jwks-request-authentication/
title: Configure JWT authentication with remote JWKS \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:52.591198+00:00
---

# Configure JWT authentication with remote JWKS  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/security/configuring-remote-jwks-request-authentication/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure JWT authentication with remote JWKS

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

Cloud Service Mesh lets you secure your services by validating JSON Web Tokens (JWT) using the Istio `RequestAuthentication` custom resource. A key part of this configuration is the `jwksUri` field, which specifies the URI of the JSON Web Key Set (JWKS) provider. This JWKS contains the public keys used to validate incoming JWTs.

**Important** : In Cloud Service Mesh, the data plane (Envoy proxies) is responsible for fetching the JWKS keys directly from the `jwksUri`. The Cloud Service Mesh control plane (managed by Traffic Director) does not make external calls to fetch these keys. This means that all network communication to external JWKS providers originates from your workload's Envoy proxy.

## Prerequisites for External JWKS Access

To follow this guide, you need:

  * **Organizational Policy for Internet Access** : If your `jwksUri` points to an external internet endpoint, your Google Cloud organization policy must allow outbound internet access from your workloads. Specifically, verify that the organizational policy `constraints/compute.disableInternetNetworkEndpointGroup` is **not enforced**. If this policy is enabled, JWKS fetching from external `jwksUri`s will fail.

  * **A Labeled Kubernetes Workload** : The `RequestAuthentication` and `AuthorizationPolicy` resources use a `selector` to target specific workloads. You must have a workload, such as a Kubernetes Deployment, running in your cluster with labels that the policies can match. For example, the [`httpbin`](https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/httpbin/httpbin.yaml) sample is configured to run with the `app: httpbin` label. Feel free to use the setup with [`httpbin`](https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/httpbin/httpbin.yaml) and [`curl`](https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/curl/curl.yaml) from the [Istio JWT Token](https://istio.io/latest/docs/tasks/security/authorization/authz-jwt/) guide.




## Methods for Enabling JWKS Fetching

The method you use to enable JWKS fetching depends on your Cloud Service Mesh control plane:

  * **For Cloud Service Mesh with MCP** : You **must** use the manual configuration with `ServiceEntry` and `DestinationRule` to enable external JWKS fetching. The automated configuration is not supported.
  * **For Cloud Service Mesh with Traffic Director** : You can use either the manual or the automated configuration method.



There are two primary ways to configure Cloud Service Mesh to allow your Envoy proxies to fetch JWKS keys from an external `jwksUri`:

### 1\. Manual Configuration with `ServiceEntry` and `DestinationRule` (Recommended)

This is the recommended approach for most production scenarios, and it is **required** for Cloud Service Mesh with MCP. This method gives you explicit control over how your mesh interacts with the external JWKS provider. 

#### Define the external service with a `ServiceEntry`

First, you must create an Istio `ServiceEntry` to make the external JWKS provider a known service within your mesh. This resource enables DNS resolution and proper routing for the Envoy proxies in your data plane.

For a `RequestAuthentication` policy that uses `jwksUri: "https://your-auth-provider.com/.well-known/jwks.json"`, you would create the following `ServiceEntry`:
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: ServiceEntry
    metadata:
      name: "external-jwks-provider-se"
      namespace: your-namespace 
    spec:
      hosts:
      - "your-auth-provider.com" # Hostname from your jwksUri
      location: MESH_EXTERNAL
      ports:
      - number: 443
        name: https
        protocol: TLS
      resolution: DNS
    

#### Configure connection settings with a `DestinationRule`

Second, you may need a `DestinationRule` to specify client-side TLS settings for connections to the JWKS provider, especially if the provider requires a specific TLS or mTLS configuration.

  * **For providers using publicly trusted certificates** , create a `DestinationRule` with `tls.mode` set to `SIMPLE` to enable standard server-side TLS validation.
  * **For providers requiring client certificates (mTLS)** , set `tls.mode` to `MUTUAL` and provide the paths to the certificates and keys that Envoy must present.



This `DestinationRule` configures the connection policy for the `ServiceEntry` defined in the previous step:
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: DestinationRule
    metadata:
      name: "external-jwks-provider-dr"
      namespace: your-namespace 
    spec:
      host: "your-auth-provider.com" # Must match a host in the ServiceEntry
      trafficPolicy:
        tls:
          # Use SIMPLE for standard server-side TLS.
          mode: SIMPLE 
          
          # If the JWKS provider uses a custom CA, provide the CA cert bundle.
          # caCertificates: /path/to/provider-ca-cert.pem
    
          # For providers requiring mTLS from Envoy, uncomment the following:
          # mode: MUTUAL
          # clientCertificate: /path/to/client-cert.pem
          # privateKey: /path/to/client-key.pem
          # caCertificates: /path/to/provider-ca-cert.pem
    

When these resources are present and correctly configured, Envoy uses them to establish a secure connection and fetch the JWKS keys.

### 2\. Automated Configuration by Cloud Service Mesh (Traffic Director Only)

If Cloud Service Mesh does not find a user-defined `ServiceEntry` that covers the hostname and port of an HTTPS `jwksUri` in a `RequestAuthentication` policy, it will automatically configure the necessary setup for Envoy to fetch the JWKS keys. This automation simplifies setup for common scenarios where default connectivity to the `jwksUri` (HTTPS, standard TLS) is sufficient.

**Conditions for Automated Configuration** : This automated behavior applies if:

  * You are using Cloud Service Mesh with Traffic Director.
  * The `jwksUri` uses the `https` scheme.
  * The `jwksUri` points to an external, non-cluster-local service.
  * No _visible_ `ServiceEntry` (considering the `RequestAuthentication` policy's namespace and the `ServiceEntry`'s `exportTo` field) already manages the `jwksUri`'s hostname and port.



If these conditions are met, your Envoy proxies will be configured to fetch the JWKS without requiring you to create explicit `ServiceEntry` or `DestinationRule` resources for that `jwksUri`.

## Configuring `RequestAuthentication`

Regardless of the method used for JWKS fetching, you define JWT validation rules using a `RequestAuthentication` policy.
    
    
    apiVersion: security.istio.io/v1
    kind: RequestAuthentication
    metadata:
      name: "jwt-example"
      namespace: your-namespace # Replace with your application's namespace
    spec:
      selector:
        matchLabels:
          app: your-app # Replace with your application's label (e.g. httpbin)
      jwtRules:
      - issuer: "testing@secure.istio.io"
        jwksUri: "https://raw.githubusercontent.com/istio/istio/release-1.26/security/tools/jwt/samples/jwks.json"
    

Key fields in `jwtRules` (refer to the [Istio RequestAuthentication documentation](https://istio.io/latest/docs/reference/config/security/request_authentication/) for full details):

  * `issuer`: The issuer of the JWT.
  * `jwksUri`: The HTTPS URI of the provider's public key set (JWKS).
  * `fromHeaders` (Optional): Specifies header locations from which the JWT is expected.
  * `fromParams` (Optional): Specifies query parameters from which the JWT is expected.
  * `forwardOriginalToken` (Optional): If true, the original token is forwarded to the upstream service.



## Enforcing JWT Authentication with `AuthorizationPolicy`

To reject requests that lack a valid JWT, you must pair your `RequestAuthentication` policy with an `AuthorizationPolicy`. The following policy allows requests to the `your-app` workload only if they present a valid JWT from the specified issuer and subject.
    
    
    apiVersion: security.istio.io/v1
    kind: AuthorizationPolicy
    metadata:
     name: "require-jwt-for-your-app"
     namespace: your-namespace # Replace with your application's namespace
    spec:
     selector:
       matchLabels:
         app: your-app # Replace with your application's label (e.g. httpbin)
     action: ALLOW
     rules:
     - from:
       - source:
           # This principal is typically in the format "issuer/subject"
           requestPrincipals: ["testing@secure.istio.io/sub-from-jwt"] # Replace with the expected principal
    

For more detailed examples and use cases on using JWT claims in authorization, see the [Istio Authorization for JWT Tokens task](https://istio.io/latest/docs/tasks/security/authorization/authz-jwt/).

## What's Next

  * Learn more about the [Istio RequestAuthentication API](https://istio.io/latest/docs/reference/config/security/request_authentication/).
  * Review the general [Cloud Service Mesh AuthorizationPolicy overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/authorization-policy-overview).
  * Explore [Istio examples of AuthorizationPolicy for JWT](https://istio.io/latest/docs/tasks/security/authorization/authz-jwt/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
