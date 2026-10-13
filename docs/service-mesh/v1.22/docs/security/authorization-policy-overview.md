---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/security/authorization-policy-overview/
title: Authorization policy overview \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:41.090362+00:00
---

# Authorization policy overview  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/security/authorization-policy-overview/

You are viewing archived v1.22 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authorization policy overview

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Unlike a monolithic application that might be running in one place, globally-distributed microservices apps make calls across network boundaries. This means more points of entry into your applications, and more opportunities for malicious attacks. And because Kubernetes pods have transient IPs, traditional IP-based firewall rules aren't adequate to secure access between workloads. In a microservices architecture, a new approach to security is needed. Building on security features such as [Kubernetes service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and Istio security policies, Cloud Service Mesh provides even more capabilities to help you secure your applications.

This page gives application operators an overview of the `AuthorizationPolicy` custom resource (CR). Authorization policies let you enable access control on workloads at the application (L7) and transport (L3/4) layers. You configure authorization policies to specify permissions—what is this service or user allowed to do?

## Authorization policies

Requests between services in your mesh (and between end-users and services) are allowed by default. You use the `AuthorizationPolicy` CR to define granular policies for your workloads. After you apply the authorization policies, Cloud Service Mesh distributes them to the sidecar proxies. As requests come into a workload, the sidecar proxy checks the authorization policies to determine if the request should be allowed or denied.

See [Supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features) for details of which fields of the `AuthorizationPolicy` CR are supported by platform.

### Policy scope

You can apply a policy to the entire service mesh, to a namespace, or to an individual workload.

  * To apply a mesh-wide policy, specify the root namespace, `istio-system`, in the `metadata:namespace` field:
        
        apiVersion: "security.istio.io/v1beta1"
        kind: "AuthorizationPolicy"
        metadata:
          name: "mesh-wide"
          namespace: istio-system
        spec:
        ...
        

  * To apply a policy to a namespace, specify the namespace in the `metadata:namespace` field:
        
        apiVersion: "security.istio.io/v1beta1"
        kind: "AuthorizationPolicy"
        metadata:
          name: "currencyservice"
          namespace: currencyservice
        spec:
        ...
        

  * To restrict a policy to a specific workload, include a [`selector`](https://istio.io/v1.22/docs/reference/config/type/workload-selector/#WorkloadSelector) field.
        
        apiVersion: "security.istio.io/v1beta1"
        kind: "AuthorizationPolicy"
        metadata:
          name: "frontend"
          namespace: demo
        spec:
          selector:
            matchLabels:
              app: frontend
           ...
        




### Basic structure

An authorization policy includes the policy scope, an `action`, and a list of `rules`:

  * As described in the previous section, the policy scope can be the entire mesh, a namespace, or a specific workload. If you include it, the `selector` field specifies the target of the policy.

  * The `action` field specifies whether to `ALLOW` or `DENY` the request. If you don't specify an action, by default, the action is set to `ALLOW`. For clarity, we recommend that you always specify the action. (Authorization policies also support [`AUDIT`](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/authz-audit-policies) and [`CUSTOM`](https://istio.io/v1.22/docs/tasks/security/authorization/authz-custom/) actions. The `AUDIT` action is only supported on some plaforms. See [Supported features](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features) for details.)

  * The [`rules`](https://istio.io/v1.22/docs/reference/config/security/authorization-policy/#Rule) specify when to trigger the action.

    * The `from` field in the `rules` specifies the [sources](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Source) of the request.

    * The `to` field in the `rules` specifies the [operations](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation) of the request.

    * The `when` field specifies additional [conditions](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Condition) needed to apply the rule.




In the following example:

  * The policy is applied to requests to the `frontend` service in the `demo` namespace.

  * Requests are allowed when "hello:world" is in the request header; otherwise, requests are denied.



    
    
    apiVersion: "security.istio.io/v1beta1"
    kind: "AuthorizationPolicy"
    metadata:
      name: "hello-world"
      namespace: demo
    spec:
      selector:
        matchLabels:
          app: frontend
      action: ALLOW
      rules:
      - when:
        - key: request.headers[hello]
          values: ["world"]
    

## Access control on request operation

You can control access to specific request [operations](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation) such as HTTP methods or TCP ports by adding a `to` section under `rules`. In the following example, only the `GET` and `POST` HTTP methods are allowed to the `currencyservice` in the `demo` namespace.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
     name: currencyservice
     namespace: demo
    spec:
     selector:
       matchLabels:
         app: currencyservice
     action: ALLOW
     rules:
     - to:
       - operation:
           methods: ["GET", "POST"]
    

## Access control on authenticated identity

In the previous examples, the policies allow requests from unauthenticated workloads. If you have [`STRICT` mutual TLS](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/configuring-mtls) (mTLS) enabled, you can restrict access based on the identity of the workload or namespace that the request is from in the [`source`](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Source) section.

  * Use the `principals` or `notPrincipal` field to control access at the workload level.

  * Use the `namespaces` or `notNamespaces` field to control access at the namespace level.




All of the preceding fields require that you have `STRICT` mTLS enabled. If you are unable to set `STRICT` mTLS, see Reject plaintext requests for an alternative solution.

### Identified workload

In the following example, requests to the `currencyservice` are allowed only from the `frontend` service. Requests to the `currencyservice` from other workloads are denied.
    
    
    apiVersion: "security.istio.io/v1beta1"
    kind: "AuthorizationPolicy"
    metadata:
      name: "currencyservice"
      namespace: demo
    spec:
      selector:
        matchLabels:
          app: currencyservice
      action: ALLOW
      rules:
      - from:
        - source:
            principals: ["example-project-1234.svc.id.goog/ns/demo/sa/frontend-sa"]
    

To specify a service account, the `principals` must be in the following format:
    
    
    principals: ["PROJECT_ID.svc.id.goog/ns/NAMESPACE/sa/SERVICE_ACCOUNT_NAME"]
    

If you are using in-cluster Cloud Service Mesh with Citadel CA, then `cluster.local` is the trust domain. In all other cases, `PROJECT_ID.svc.id.goog`is the trust domain for the mesh.

### Identified namespace

The following example shows a policy that denies requests if the source is not the `foo` namespace:
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
     name: httpbin-deny
     namespace: foo
    spec:
     selector:
       matchLabels:
         app: httpbin
         version: v1
     action: DENY
     rules:
     - from:
       - source:
           notNamespaces: ["foo"]
    

## Value matching

Most fields in authorization policies support all the following matching schemas:

  * Exact match: exact string match.
  * Wildcard match using the `"*"` wildcard character: 
    * Prefix match: a string with an ending `"*"`. For example, `"test.example.*"` matches `"test.example.com"` or `"test.example.com.cn"`.
    * Suffix match: a string with a starting `"*"`. For example, `"*.example.com"` matches `"eng.example.com"` or `"test.eng.example.com"`.
  * Presence match: To specify that a field must be present and not empty, use the `fieldname: ["*"]` format. This is different from leaving a field unspecified, which means match anything, including empty.



There are a few exceptions. For example, the following fields only support exact match:

  * The `key` field under the `when` section
  * The `ipBlocks` under the `source` section
  * The `ports` field under the `to` section



The following example policy allows access at paths with the `/test/*` prefix or the `*/info` suffix:
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: tester
      namespace: default
    spec:
      selector:
        matchLabels:
          app: products
      action: ALLOW
      rules:
      - to:
        - operation:
            paths: ["/test/*", "*/info"]
    

## Exclusion matching

To match negative conditions like `notValues` in the `when` field, `notIpBlocks` in the `source` field, `notPorts` in the `to` field, Cloud Service Mesh supports exclusion matching. The following example requires a valid request `principals`, which is derived from JWT authentication, if the request path is not `/healthz`. Thus, the policy excludes requests to the `/healthz` path from the JWT authentication:
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: disable-jwt-for-healthz
      namespace: default
    spec:
      selector:
        matchLabels:
          app: products
      action: ALLOW
      rules:
      - to:
        - operation:
            notPaths: ["/healthz"]
        from:
        - source:
            requestPrincipals: ["*"]
    

## Reject plaintext requests

In Cloud Service Mesh, auto mTLS is enabled by default. With auto mTLS, a client sidecar proxy automatically detects if the server has a sidecar. The client sidecar sends mTLS to workloads with sidecars and sends plaintext to workloads without sidecars. For the best security, we recommend that you [enable STRICT mTLS](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/configuring-mtls).

If you are unable to enable mTLS with `STRICT` mode for a workload or namespace, you can:

  * create an authorization policy to explicitly allow traffic with non-empty `namespaces` or non-empty `principals`, or
  * reject traffic with empty `namespaces` or `principals`.



Because the `namespaces` and `principals` can only be extracted with a mTLS request, these policies effectively reject any plaintext traffic.

The following policy denies the request if the principal in the request is empty (which is the case for plaintext requests). The policy allows requests if the principal is non-empty. The `["*"]` means a non-empty match, and using with `notPrincipals` means matching on empty principal.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: require-mtls
      namespace: NAMESPACE
    spec:
      action: DENY
      rules:
      - from:
        - source:
            notPrincipals: ["*"]
    

## Authorization policy precedence

You can configure separate `ALLOW` and `DENY` authorization policies, but you need to understand the policy precedence and default behavior to make sure that the policies do what you want. The following diagram describes the policy precedence.

![authorization policy precedence](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/authorization-policy-decision-tree.svg)

The example policies in the following sections illustrate some of the default behavior and the situations where you might find them useful.

### Allow nothing

The following example shows an `ALLOW` policy that doesn't match anything. By default, if there are no other `ALLOW` policies, requests are always _denied_.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: allow-nothing
    spec:
      action: ALLOW
    

It is a good security practice to start with the allow-nothing policy and incrementally add more `ALLOW` policies to open more access to a workload.

### Deny all access

The following example shows a `DENY` policy that matches everything. Because `DENY` policies are evaluated before `ALLOW` policies, all requests are denied even if there is an `ALLOW` policy that matches the request.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: deny-all
    spec:
      action: DENY
      rules:
      - {}
    

A deny-all policy is useful if you want to temporarily disable all access to a workload.

### Allow all access

The following example shows an `ALLOW` policy that matches everything, and allows full access to a workload. The allow-all policy makes other `ALLOW` policies useless because it always allows the request.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: allow-all
    spec:
      action: ALLOW
      rules:
      - {}
    

An allow-all policy is useful if you want to temporarily expose full access to a workload. If there are any `DENY` policies, requests could still be denied since `DENY` policies are evaluated before `ALLOW` policies.

## Best practices

  1. Create a Kubernetes service account for each service, and specify the service account in the Deployment. For example:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: frontend-sa
           namespace: demo
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: frontend
           namespace:demo
         spec:
           selector:
             matchLabels:
               app: frontend
           template:
             metadata:
               labels:
                 app: frontend
             spec:
               serviceAccountName: frontend-sa
             ...
         

  2. Start with an allow-nothing policy and incrementally add more `ALLOW` policies to open more access to workloads.

  3. If you are using JWTs for your service:

     1. Create a `DENY` policy to block unauthenticated requests, for example:
            
            apiVersion: security.istio.io/v1beta1
            kind: AuthorizationPolicy
            metadata:
              name: requireJWT
              namespace: admin
            spec:
              action: DENY
              rules:
              -  from:
                - source:
                    notRequestPrincipals: ["*"]
            

     2. Apply an allow-nothing policy.

     3. Define `ALLOW` policies for each workload. For examples, see [JWT Token](https://istio.io/latest/docs/tasks/security/authorization/authz-jwt/).




## What's next

Learn more about Cloud Service Mesh security features:

  * [Configuring Cloud Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/end-user-auth)
  * [Configuring audit policies for your services](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/authz-audit-policies)
  * [Configuring transport security](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/configuring-mtls)
  * [Integrating Identity-Aware Proxy with Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/iap-integration)
  * [Best Practices for using Cloud Service Mesh egress gateways on GKE clusters](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/egress-gateways-best-practices)



Learn more about authorization policies from the Istio documentation:

  * [Authorization policy examples](https://istio.io/v1.22/docs/ops/configuration/security/security-policy-examples/)
  * [Authorization policy troubleshooting](https://istio.io/v1.22/docs/reference/config/security/authorization-policy/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
