---
url: https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity/
title: About Agent Identity for GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:09.124170+00:00
---

# About Agent Identity for GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About Agent Identity for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Agent Identity for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agent workloads often require different defensive measures, access control, and authentication workflows than other types of workloads. You can use [_Agent Identity_](https://docs.cloud.google.com/iam/docs/agent-identity-overview) to give each agent an attested, short-lived, per-Pod identity. This identity helps you to identify agent workloads and to track and manage what those workloads do across Google Cloud. This document describes how Agent Identity works in Google Kubernetes Engine (GKE), including how to integrate with other Google Cloud products, the types of authentication that your agents can use, and how to govern your workloads by using these identities.

This document is intended for platform administrators and security engineers who want to improve the security of agents that run on GKE clusters while integrating the agents with Google Cloud products and services.

You should already be familiar with the following topics:

  * [The SPIFFE standard](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity)
  * [The OAuth 2.0 protocol](https://oauth.net/2/)



## What is Agent Identity?

Google Cloud provides various identity types for your workloads, each of which is intended for a specific set of use cases and workload types. Agent Identity is an identity type that's designed for AI agent workloads. An agent that uses Agent Identity gets a unique identity that's based on the SPIFFE standard. This identity is bound to the lifecycle of the agent, identifies the workload as an agent, and is recognized by the various Gemini Enterprise Agent Platform services like Agent Registry and Agent Gateway. You can track and manage a workload that has an agent identity across all of the services that the workload accesses, regardless of where that workload runs. A workload that uses Agent Identity can authenticate to MCP servers, resources inside and outside of Google Cloud, other agents, and endpoints by using its own identity or on behalf of an end user. For more information about Agent Identity, see [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

You can use Agent Identity to improve security and governance for AI agents that you deploy in GKE clusters and to enable specific workflows for your agents such as the following:

  * Integrate agents on GKE with products like Agent Registry and Agent Gateway.
  * Manage roles for agent workloads across projects, folders, or organizations in Identity and Access Management (IAM) policies.
  * Reduce the impact of compromised agents on nodes and other Pods in the cluster.
  * Set up various authentication workflows, such as agents acting on behalf of end users, by using Agent Identity auth manager.



### Comparison with Workload Identity Federation for GKE

Both Agent Identity and Workload Identity Federation for GKE provide ways to give identities to workloads. Agent Identity is designed for the threat model and specific requirements that apply to AI agents, which results in various functional differences. The following table provides a high-level comparison of these differences:

Agent Identity | Workload Identity Federation for GKE  
---|---  
[Agent identity access tokens](https://docs.cloud.google.com/docs/authentication/token-types#agent-identity-access-tokens) can be cryptographically bound to per-Pod X.509 certificates. A bound access token requires an mTLS connection and doesn't work when used outside of the original Pod. | [Federated access tokens](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens) aren't cryptographically bound to Pod identities, works over non-mTLS connections, and can be used outside of the original Pod.  
Integrates with the Agent Identity auth manager to support OAuth workflows and use third-party credentials without manual credential management. | Requires manual implementation of OAuth workflows and management of third-party credentials when authenticating to external tools and services.  
Works well for autonomous workloads like AI agents. | Works well for deterministic microservices like web servers, APIs, and batch jobs.  
Requires GKE version 1.37.0-gke.3503000 or later. | Available in all GKE versions.  
Bound agent identity access tokens always use the `https://www.googleapis.com/auth/cloud-platform` access scope. Custom scopes aren't supported. | Federated access tokens support custom access scopes.  
Applications can get agent identity ID tokens to authenticate directly to other workloads or downstream services. | Applications can't get ID tokens unless the Kubernetes ServiceAccount is configured to impersonate an IAM service account.  
  
## Integration with Agent Platform

Gemini Enterprise Agent Platform includes multiple products and services that are designed for building, governing, and operating agents at scale. If you run agent workloads on GKE, then you can use the Agent Platform products by assigning agent identities to the workloads and registering the workloads as agents in Agent Registry. To integrate and use Agent Platform services with your GKE agents, your application operators add annotations and labels to the Kubernetes specifications of the agent workloads. Other than verifying that Workload Identity Federation for GKE is enabled, you don't need to make changes to your cluster or node pool configuration. You can then manage and govern your GKE agents in the same way that you'd govern an agent that runs on Agent Runtime or Cloud Run.

Registration in Agent Registry also helps to prevent potential disruptions when you move projects between organizations. During a project move, Agent Registry checks whether any agents use an agent identity that's based on the organization-level trust domain, which would change after the move. If an organization-level agent identity is in use, then the project move is blocked. This check happens only with Deployments that you register in Agent Registry. The check doesn't happen with other workload controllers or static Pods.

## How it works in GKE

In GKE, Agent Identity uses concepts such as the GKE metadata server and identity pools, similarly to Workload Identity Federation for GKE. To use Agent Identity, you must also enable Workload Identity Federation for GKE in the cluster. Google Cloud automatically creates an _agent identity pool_ at the project or organization level. The agent identity pool is a [SPIFFE trust domain](https://spiffe.io/docs/latest/spiffe-specs/spiffe_trust_domain_and_bundle/#2-trust-domains) and is the root of trust for agent identities and credentials. Application developers can request an agent identity for their agent by adding annotations and labels to their Pod specification. When the workload is deployed to a cluster, GKE assigns the following credentials to the workload:

  * A [SPIFFE identity](https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/#2-spiffe-identity) that identifies the workload. All of the Pods in a managed workload, such as a Deployment, share that workload's SPIFFE ID. The SPIFFE ID identifies the agent across Google Cloud services. You can track any actions that the Pods perform, whether as the agent or on behalf of an end user, by using the SPIFFE ID. The SPIFFE ID has the following syntax:
        
        spiffe://TRUST_DOMAIN/resources/container/projects/PROJECT_NUMBER/locations/CONTROL_PLANE_LOCATION/clusters/CLUSTER_NAME/ns/NAMESPACE/sa/SERVICEACCOUNT_NAME
        

This ID string has the following attributes:

    * `TRUST_DOMAIN`: the SPIFFE trust domain, which has one of the following values, depending on whether or not the project that contains the cluster is in an organization: 
      * **Projects that are in an organization** : `agents.global.org-ORGANIZATION_ID.system.id.goog`, where `ORGANIZATION_ID` is the ID of the organization.
      * **Projects that aren't in an organization** : `agents.global.proj-PROJECT_NUMBER.system.id.goog`, where `PROJECT_NUMBER` is the project number of the cluster project.
    * `PROJECT_NUMBER`: the project number of the cluster project.
    * `CONTROL_PLANE_LOCATION`: the region or zone that the cluster's control plane is in.
    * `CLUSTER_NAME`: the name of the cluster that the Pod is in.
    * `NAMESPACE`: the name of the Kubernetes namespace that the Pod is in.
    * `SERVICEACCOUNT_NAME`: the name of the Kubernetes ServiceAccount that's assigned to the Pod.
  * An agent identity credential bundle (`x509.credential-bundle.private-key.pem`) that's mounted as a volume in each Pod and can be used for mTLS authentication to Google Cloud APIs. This file includes the following credentials:

    * An X.509 certificate chain that includes the SPIFFE ID for the agent workload as the Subject Alternative Name (SAN) parameter and expires in 24 hours. The certificate chain is used to get bound access tokens and identity tokens for authentication to other services.
    * A private key that the `kubelet` process automatically creates for each Pod. The key cryptographically binds a Pod's X.509 certificate to the Pod. This key proves that the Pod that made a request owns the X.509 certificate that was used to establish the TLS connection.
  * A root CA trust bundle (`TRUST_DOMAIN.spiffe-trust-bundle.pem`) that's mounted as a volume in each Pod and can be used to configure mTLS authentication between agents that use the same trust domain. During an mTLS handshake, an agent uses the root CA trust bundle to validate the certificate chain that's presented by a peer agent.




### Workload-level configuration

To assign an agent identity and per-Pod credentials to a workload, GKE looks for the following annotations in the Pod specification:

  * `iam.gke.io/identity: "spiffe://TRUST_DOMAIN/*"`: GKE uses this annotation to assign the Pods a SPIFFE ID from the corresponding trust domain.
  * `iam.gke.io/inject-podcertificates: "true"`: GKE uses this annotation to add the agent identity credential bundle and the cluster trust bundle to each Pod in the workload. If this annotation is omitted, then you can't get access tokens that are bound to specific Pods. The injected credentials are used for mTLS authentication from your Pods to any Google Cloud APIs or peer agents.

**Best practice** : Use this annotation for all agent workloads. Your Pods need the credentials to get bound tokens and to establish mTLS connections with Google Cloud APIs and peer workloads. Platform administrators should enforce the use of this annotation in agent workloads by using admission control mechanisms like Kubernetes ValidatingAdmissionPolicies.



Additionally, Agent Registry uses the following label and annotation to [automatically register](https://docs.cloud.google.com/agent-registry/automatic-registration#gke) your GKE agents:

  * **`registry.gke.io/functional-type: "AGENT"` label**: identifies the workload as an AI agent and add the agent to Agent Registry. This label is supported only by Deployments and must be specified in the `metadata.labels` field of the Deployment manifest.
  * **`iam.gke.io/spiffe-identity-type: "agent-identity"` annotation**: indicates that the agent uses Agent Identity. This annotation is specified in the Pod specification. If the `registry.gke.io/functional-type: "AGENT"` label is specified for a Deployment, then this annotation is required in the Pod specification.



To integrate your GKE agents with Agent Platform, register your workloads with Agent Registry in addition to using Agent Identity. Consider enforcing registration of agent workloads or automating registration in your deployment pipeline.

### Access tokens for agents

In GKE, each Pod that uses Agent Identity gets a unique credential bundle that contains the X.509 certificate and the Pod's private key, which doesn't leave the Pod. To access any Google Cloud APIs or external services, an agent Pod in a GKE cluster requests an [_agent identity access token_](https://docs.cloud.google.com/docs/authentication/token-types#agent-identity-access-tokens) from the GKE metadata server that runs on each node. The Pod uses the agent identity access token to authenticate as the agent identity.

The access token can be bound or unbound, as follows:

  * **Bound access token** : cryptographically bound to the X.509 certificate of the Pod and can be used only over mTLS connections that were authenticated by using that X.509 certificate. Any access token request that includes the X.509 certificate in the payload results in a bound token.
  * **Unbound access token** : not cryptographically bound to a specific Pod and can be used over non-mTLS connections. Unbound access tokens are more vulnerable to token replay attacks, because a leaked token can be used by a different Pod.



Agents use the bound or unbound access tokens to authenticate their requests to Google Cloud APIs. Identity administrators can control what access an agent has by specifying the principal identifier of that agent identity access token in IAM policies, as described in Control access to Google Cloud resources for agents.

**Best practice** : Enable certificate injection and use bound access tokens in most scenarios, so that your agents establish mTLS connections with Google Cloud APIs and reduce the risk of token replay attacks. Unbound access tokens aren't cryptographically linked to specific Pods in the workload, which increases the risk of token replay attacks.

If Pods have the `iam.gke.io/inject-podcertificates: "true"` annotation, then the Cloud Client Libraries and Google authentication libraries use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to automatically get a bound agent identity access token for Pods. This automatic process might not occur in every library or programming language. To request unbound access tokens instead, developers use one of the following methods:

  * Specify the `iam.gke.io/inject-podcertificates: "true"` annotation and set the `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN` environment variable to a value of `false` in the Pod specification. GKE adds the X.509 credential bundle to the Pod, but the environment variable causes ADC to get unbound access tokens.

This method lets the Pods continue to establish mTLS connections with other workloads by using the certificates while also using unbound access tokens to access Google Cloud APIs.

  * Don't specify the `iam.gke.io/inject-podcertificates: "true"` annotation in the Pod specification. GKE doesn't add the X.509 credential bundle to the Pod, so ADC gets unbound access tokens for the Pods.

  * Send a direct HTTP `GET` request to the token endpoint of the GKE metadata server, which returns an unbound access token.




## Authentication workflows for agents

Unlike non-agent workloads, agents might need to authenticate to services on behalf of an end user or as the agent's own identity, depending on what task the agent is attempting. Agent Identity supports authentication to the following types of resources by using various credentials and authentication models:

  * Google Cloud APIs
  * External tools and services
  * Agent-to-agent authentication



### Authentication to Google Cloud APIs

An agent can use its own identity to authenticate to Google Cloud APIs, such as to BigQuery or Agent Platform. To authenticate, the Pod gets an agent identity access token from the GKE metadata server on the node. This access token can optionally be _bound_ to the X.509 certificate of the Pod, which means that the access token can be used only over an mTLS connection that's authenticated by using the X.509 certificate.

If your application uses version 2.61.0 or later of the `google-auth` Python authentication library, then Application Default Credentials (ADC) automatically requests bound access tokens for Pods that have the agent identity credential bundle. If you use the [**Cloud Client Libraries**](https://docs.cloud.google.com/sdk/docs/libraries-reference) for Python, ensure that you use a version that includes version 2.61.0 or later of the `google-auth` library. For other programming languages or for versions of the `google-auth` Python library that are earlier than 2.61.0, request unbound access tokens instead.

If you get a bound access token, then you must use the Pod's X.509 certificate to establish an mTLS connection with the destination API's [mTLS endpoint](https://docs.cloud.google.com/access-context-manager/docs/understand-mtls). If you get an unbound access token, then you can use that token in requests to the non-mTLS endpoint of that API.

To configure your application code to get bound or unbound access tokens by using these methods, see [Authenticate by using an agent identity in GKE](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity).

If you're a platform administrator or a security administrator, then you don't need to configure additional authentication for agents that authenticate to Google Cloud APIs. You can control access to resources by using IAM policies, as described in Control access to Google Cloud resources for agents.

### Agent authentication to external services

Agents often need to access external tools and services by using specific credentials, such as API keys or OAuth tokens. The agent might need to authenticate as its own identity or on behalf of an end user. You can provide agents with specific credentials by using the [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/auth-manager-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)). The auth manager centralizes credential acquisition and authentication workflow configuration for agents that you run across Google Cloud.

In the auth manager, you configure _auth providers_ to handle specific authentication workflows. When an agent in GKE needs to authenticate by using a specific credential, the Pod uses its agent identity access token to authenticate to the auth manager. The auth provider then handles any additional authentication steps and returns the requested credential to the Pod. The auth manager exchanges the external credentials for short-lived access tokens, so that long-lived refresh tokens and API secrets aren't stored in the agent container.

You can use the auth manager for the following use cases, each of which involves specific setup and configuration in the auth manager and in application code:

  * Access external services on behalf of an end user.
  * Access external services as its own identity.
  * Access APIs by using an API key.



You can monitor and revoke the credentials that the auth manager creates. You can also track which credentials specific agents use, because the agent authenticates to the auth manager by using its agent identity access token. The following sections describe the use cases for the auth manager and the corresponding [authentication models](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models). Depending on the authentication model that you use, you and your application developers need to make specific changes to the agent code and to client-side applications.

#### Access to external services on behalf of an end user

An end user might ask an agent to perform certain actions on the user's behalf, such as writing messages in a Slack channel or opening a pull request in a GitHub repository. In these scenarios, the user _delegates_ their authority to the agent by explicitly consenting to the agent acting on the user's behalf. To set up user consent and credential retrieval, you use _3-legged OAuth_ , which involves the following steps:

  1. The auth provider redirects the user to authenticate to the external service.
  2. The user logs in and approves the access that the agent needs.
  3. The external service returns a credential to the auth provider.



To configure 3-legged OAuth for an agent that runs on GKE, the platform administrator and application developer follow these steps:

  1. The platform administrator sets up the auth provider: 
     1. Create a 3-legged OAuth auth provider in the auth manager.
     2. Configure the auth provider to redirect to the third-party authorization server.
     3. Configure the third-party service to send the user access token to the auth provider.
     4. [Authorize the agent to access the auth provider](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access#authorize-auth-manager).
  2. The application developer modifies the application: 
     1. Modify the agent code to authenticate by using the auth provider.
     2. Modify the client-side application code to handle user sign-in, redirection, and conversation resumption.



For more information about how to configure the auth provider and modify your agent and client-side applications, see [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2).

#### Access to external services as the agent identity

An agent might need to access external services like ServiceNow or Salesforce by using the agent's own identity. For example, an inventory management agent might monitor sales data and order inventory to avoid stock issues during peak sales events. In these scenarios, you use _2-legged OAuth_ , which involves the following steps:

  1. The auth manager requests an access token from the external service.
  2. The external service validates the request and returns the access token to the auth manager.



To configure 2-legged OAuth for an agent that runs on GKE, you do the following:

  1. The platform administrator sets up the auth provider: 
     1. Get an OAuth client ID, client secret, and token endpoint from the external service.
     2. Create a 2-legged OAuth auth provider in the auth manager that has the external service's OAuth information.
     3. [Authorize the agent to access the auth provider](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access#authorize-auth-manager).
  2. The application developer modifies the agent code to authenticate by using the auth provider.



For more information about how to configure the auth provider and modify your agent code, see [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2).

#### Access to APIs by using an API key

You can store API keys in the auth manager for agents to use to authenticate to external APIs. Although you can store API keys in other vaults such as Secret Manager, the auth manager method lets you track and manage agent access to API keys in a central location. To store and use API keys in the auth manager, you do the following:

  1. The platform administrator sets up the auth provider: 
     1. Create an API key auth provider in the auth manager.
     2. Generate and store the API key in the auth provider.
     3. [Authorize the agent to access the auth provider](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access#authorize-auth-manager).
  2. Modify the agent code to authenticate by using the auth provider.



For more information, see [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2).

### Agent-to-agent authentication

This section describes an advanced authentication workflow. You should already be familiar with the following topics:

  * [JSON Web Tokens (JWTs)](https://www.rfc-editor.org/info/rfc7519/): agent identity ID tokens are signed JWTs.
  * [JSON Object Signing and Encryption (JOSE) headers](https://www.rfc-editor.org/info/rfc7515#section-4): ID tokens have a JOSE header that describes the algorithm and the signing key for the ID token.
  * [JSON Web Keys (JWKs)](https://www.rfc-editor.org/info/rfc7517/): JWKs are used to sign ID tokens. The public JWKs for an agent identity pool are published as a JSON Web Key Set (JWKS). You use these public keys to validate incoming ID tokens from other agents.



In multi-agent architectures, agents frequently collaborate by directly invoking peer agents or downstream services. You can directly establish communication between agent workloads by using an [Agent Identity _identity token_](https://docs.cloud.google.com/docs/authentication/token-types#agent-identity-id-tokens), which is a signed JWT that you can get from the GKE metadata server. To authenticate a connection between agent services, application developers do the following:

  1. Get an agent identity ID token from the GKE metadata server for the calling agent. This ID token must set the `aud` claim to the receiving agent's endpoint.
  2. Include the ID token in the `Authorization: Bearer` request header of the HTTP request.
  3. In the receiving agent, validate the incoming ID token by using the public JWKs for the agent identity pool and the various header and body parameters in the ID token.



For more information about how to request, use, and validate ID tokens in your application code, see [Authenticate to other agents](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity#authenticate-other-agents).

Agent-to-agent authentication doesn't require additional Google Cloud configuration from a platform administrator, because this workflow bypasses IAM authorization checks. Instead, the agents communicate directly with each other and authorize actions based on the agent identities.

## Control access to Google Cloud resources for agents

Security administrators can control which resources an agent can access by using IAM policies that reference the agent's principal identifier. To control access to resources for an agent that runs on GKE and has an agent identity, you include one of the following principal identifiers in your IAM policy:

  * All agents in a specific trust domain:
        
        principalSet://TRUST_DOMAIN/*
        

In this identifier, `TRUST_DOMAIN` is the trust domain for your resource hierarchy, which depends on whether the agent is in a project that's in an organization:

    * **Projects that are in an organization** : `agents.global.org-ORGANIZATION_ID.system.id.goog`, where `ORGANIZATION_ID` is the ID of the organization.
    * **Projects that aren't in an organization** : `agents.global.proj-PROJECT_NUMBER.system.id.goog`, where `PROJECT_NUMBER` is the project number of the cluster project.
  * A single agent in a trust domain:
        
        principal://TRUST_DOMAIN/resources/container/projects/PROJECT_NUMBER/locations/CONTROL_PLANE_LOCATION/clusters/CLUSTER_NAME/ns/NAMESPACE_NAME/sa/SERVICEACCOUNT_NAME
        

In this identifier, the following parameters identify the specific agent:

    * `PROJECT_NUMBER`: the project number of the cluster's project.
    * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane.
    * `CLUSTER_NAME`: the name of the cluster that the agent is in.
    * `NAMESPACE_NAME`: the name of the Kubernetes namespace that the agent is in.
    * `SERVICEACCOUNT_NAME`: the name of the Kubernetes ServiceAccount that the agent workload uses.



For more information about how to find principal identifiers for GKE agents and manage access, see [Manage access to Google Cloud APIs for agents](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access).

Agent Identity supports all of the IAM policy types, such as allow policies, deny policies, and Principal Access Boundary (PAB) policies. To manage access for an agent in a GKE cluster that uses Agent Identity, you include the agent's principal identifier in the corresponding policy type. For more information about how to configure each type of IAM policy, see the following topics:

  * [Create and apply Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-create)
  * [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access)
  * [Manage access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources)



## View and manage agents across Google Cloud

If application developers register their agents in Agent Registry, then you can view the GKE agents alongside the other agents that you run in Google Cloud. Agent Registry shows the agent's SPIFFE identity, where the agent runs, and any additional information about the agent. All API requests authenticated by using Agent Identity generate [Agent Registry audit logs](https://docs.cloud.google.com/agent-registry/audit-logging). Depending on the authentication workflow that the agent uses, Cloud Audit Logs provides the following information:

  * **Authentication by using the agent's own identity** : the generated audit logs include the agent's principal identifier, which you can use to find the cluster, namespace, and ServiceAccount of the agent.
  * **Delegated operations on behalf of end users** : the generated audit logs include information about the end user who authorized the action and the SPIFFE ID of the agent that executed the call. This identity association in the audit logs helps you to validate that the end user authorized specific actions.



In addition to Cloud Audit Logs, application developers can configure their agent workloads to emit traces, logs, and metrics that become visible in Google Cloud Observability. For more information about how to configure the workloads, see the following documents:

  * [Set up tracing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/tracing)
  * [Set up logging](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/logging)
  * [Set up monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/monitoring)



## Improve security for GKE agents

Security administrators can manage agent-specific security measures separately from constraints for other types of workloads by referencing the agent identities. Consider the following defensive measures for when you run agents:

  * To limit the impact of a compromised agent, configure a [Principal Access Boundary Policy (PAB Policy)](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) for agent identities.
  * To improve the security of the auth manager auth providers, configure [organization policies for agent identities](https://docs.cloud.google.com/iam/docs/agent-identity-custom-constraints).
  * To centralize agent management and track agent actions across resources, enforce Agent Registry registration by using annotations and labels by using [admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/), such as ValidatingAdmissionPolicies and MutatingAdmissionPolicies.
  * To manage security for direct agent-to-agent traffic, use the following controls: 
    * To control traffic between Pods in the same cluster, use [Kubernetes NetworkPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).
    * To reduce the risk of data exfiltration during a compromise, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
    * To control network traffic across VPC networks and between agents that run in different environments, use [VPC network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [Cloud Next Generation Firewall (Cloud NGFW)](https://docs.cloud.google.com/firewall/docs/about-firewalls).
    * To enforce IAM policies on traffic between agents that are registered in Agent Registry, use [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#choose-mode).



## Limitations

  * You can automatically register only Deployments in Agent Registry. Other workload controllers and static Pods don't support automatic registration.
  * Bound agent identity access tokens use only the `https://www.googleapis.com/auth/cloud-platform` OAuth scope. You can't specify a different scope for the bound access tokens.
  * The automatic retrieval of bound access or ID tokens is supported only in Python applications that use version 2.61.0 or later of the `google-auth` library. If you use the Cloud Client Libraries for Python, then you must use a version that includes version 2.61.0 or later of the `google-auth` library.
  * Certain Cloud Client Libraries might not automatically route your requests to mTLS endpoints.
  * For agent-to-agent authentication, you can use bound ID tokens only to authenticate between agents that are in the same agent identity trust domain.



## What's next

  * [Request an agent identity for a GKE agent](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity)
  * [Manage access to Google Cloud APIs for agents](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access)
  * [Authenticate by using an agent identity in GKE](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
