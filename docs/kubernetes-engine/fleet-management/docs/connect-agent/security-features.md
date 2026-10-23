---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/security-features/
title: Connect security features \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:51.616565+00:00
---

# Connect security features  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/security-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Connect security features Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the security measures built into Connect.

An effective hybrid and multi-cloud platform delivers central management, observability, and access to services across environments. GKE Enterprise provides a uniform and comprehensive experience across those capabilities, no matter what Kubernetes provider you use. Connect is a lightweight agent that provides the following at economies of scale, and across providers:

  * Multi-cluster management and cluster visibility
  * Application services deployment and lifecycle management



This document discusses the following:

  * How the design of Connect puts security first
  * Best practices for the Connect Agent deployment
  * How to improve your Kubernetes deployment security posture



## Architecture of Connect

Connect allows end users and Google Cloud services to access Kubernetes API servers that aren't on the public internet. The Connect Agent runs in the Kubernetes cluster (one agent per cluster), and connects to a Connect proxy. Google Cloud services that need to interact with the Kubernetes cluster connect to the proxy, which forwards requests to the agent. The agent, in turn, forwards them to the Kubernetes API server as depicted in the following diagram.

[ ![Architecture of how users access Kubernetes API servers that aren't on the internet \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-1-agent-forwards-requests.svg)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-1-agent-forwards-requests.svg) Architecture of how users access Kubernetes API servers that aren't on the internet (click to enlarge)

When the agent is deployed, it establishes a persistent TLS 1.2+ connection to Google Cloud to wait for requests. Google Cloud services, when enabled by admins, can generate requests for your Kubernetes clusters. These requests might also come from direct user interaction with the Google Cloud console, Connect Gateway, or other Google Services.

The Google Cloud service sends the request to the proxy. The proxy then forwards the request to the deployed agent responsible for a cluster, and finally the agent forwards the request to the Kubernetes API server. The Kubernetes API server applies Kubernetes authentication, authorization, and audit-logging policies, and returns a response. The response is passed back through the agent and the proxy to the Google Cloud service. At each step in the process, components perform per-connection and per-request authentication and authorization.

The Kubernetes API server applies the same authentication, authorization, and audit-logging policies to all requests, including requests through Connect. This process ensures that you're always in control of the access to your cluster.

## Connect and defense-in-depth

[Defense-in-depth](https://wikipedia.org/wiki/Defense_in_depth_\(computing\)) is intrinsic to everything Google Cloud does within its infrastructure and security practices. We take a layered approach to every aspect of securing our organization and our customers in order to protect valuable data, information, and users. This is the same principle by which we've designed Connect.

In addition to Google's own defense-in-depth strategy and design, you should evaluate the content provided here alongside your security posture and standards. This section calls out additional measures that you can take that complement Kubernetes hardening best practices.

## Component-to-component security

Each component of a Connect request authenticates its peers, and only shares data with peers that are both authenticated and authorized for that data, as illustrated in the following diagram.

[ ![Architecture of how Connect components authenticate \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-2-sharing-data.svg)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-2-sharing-data.svg) Architecture of how Connect components authenticate (click to enlarge)

Each component of a Connect request uses the following to authenticate each other:

  * Transport Layer Security (TLS)
  * [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security)
  * OAuth



Each component of a Connect request uses the following to authorize each other:

  * Identity and Access Management (IAM)
  * Allowlists



Each connection between the Kubernetes cluster and Google Cloud is encrypted, and at least one peer of each connection uses certificate-based authentication. This process helps to ensure that all token credentials are encrypted in transit, and only received by authenticated and authorized peers.

### User authentication to Google Cloud

When using the Google Cloud console, users go through the [standard Google login flow](https://developers.google.com/identity/). Google Cloud provides a TLS certificate that the user's browser authenticates, and the user logs in to a Google Cloud or Google Workspace account to authenticate to Google Cloud.

Access to a project through the Google Cloud console or other APIs is controlled by IAM permissions.

### Google Cloud service-to-service authentication

Google Cloud uses ALTS for internal service-to-service authentication. ALTS allows Google Cloud services, such as the proxy, to create an authenticated, integrity-protected connection.

Google Cloud services must be internally authorized to use the proxy to connect to a remote Connect instance because the proxy uses a [allowlist of service identities](https://docs.cloud.google.com/security/infrastructure/design#inter-service_access_management) to limit access.

### Authenticating Google Cloud

The agent uses TLS to authenticate and encrypt each connection. The agent authenticates Google Cloud TLS certificates by using a set of root certificates built into the binary, to avoid inadvertently trusting certificates added to the agent's container. The agent only executes API calls against correctly authenticated endpoints. This process helps to ensure that service account certificates and the Kubernetes API requests are sent by Google Cloud, and that any responses are sent only to Google Cloud.

For the list of domains that the agent communicates with during normal operation, see [Ensure network connectivity](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/connect/prerequisites#ensure_network_connectivity).

You can configure the agent to [connect to Google Cloud](https://cloud.google.com/hybrid-connectivity/) through an HTTP proxy. In this configuration, the agent uses the `HTTP/1.1 CONNECT` against the HTTP proxy and establishes a TLS connection to Google Cloud. The HTTP proxy only sees the encrypted traffic between the agent and Google Cloud. The end-to-end integrity and security of connection between the agent and Google Cloud is unaffected.

### Authenticating the agent

The agent authenticates to Google Cloud by using [Fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity). Fleet Workload Identity Federation lets you authenticate from fleet workloads to Google Cloud APIs by using built-in Google Cloud and Kubernetes authentication mechanisms. When the agent wants to authenticate to Google Cloud, it exchanges its Kubernetes Service Account token for an access token that represents its workload identity.

### Kubernetes API server

The agent uses the Kubernetes [client library](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/#programmatic-access-to-the-api) to create a TLS connection to the Kubernetes API server. The Kubernetes runtime provides the agent's container with a TLS certificate authority (CA) certificate that the agent uses to authenticate the API server.

The API server authenticates each request separately, as described in the next section.

## Request security

Each request sent from Google Cloud through Connect includes credentials that identify the request's sender: both the Google Cloud service that generated the request, and (where applicable) the end user for whom the request is sent. These credentials allows the Kubernetes API server to provide authorization and auditing controls for each request.

### Service-to-agent authentication

Each request sent to the agent includes a short-lived token identifying the Google Cloud service that sent the request, as illustrated in the following diagram.

[ ![Architecture of requests with a token identifying the Google Cloud services \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-3-user-credentials.svg)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-3-user-credentials.svg) Architecture of requests with a token identifying the Google Cloud services (click to enlarge)

The token is signed by a Google Cloud service account associated exclusively with the Google Cloud service. The agent [fetches the service account's public keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) to validate the token. This token isn't forwarded to the API server.

The agent validates Google Cloud certificates using CA roots embedded in the binary. This process helps to ensure that it is receiving authentic and unaltered requests from Google Cloud.

### End-user authentication

Google Cloud services that access clusters on behalf of a user require that user's credentials to authenticate to the API server, as illustrated in the following diagram.

[ ![Architecture of Google Cloud services that authenticate a user's credentials \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-4-short-lived-token.svg)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-4-short-lived-token.svg) Architecture of Google Cloud services that authenticate a user's credentials (click to enlarge)

This policy helps to ensure that the same set of permissions are applied to the user when accessing through Connect. Some Google Cloud services authenticate to the API server on behalf of a user. For example, a user can access the Google Cloud console to view workloads in Fleet-enrolled clusters. When a user accesses these services, they provide credentials that the Kubernetes API server recognizes: [any of the tokens](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#authentication-strategies) that the Kubernetes API server supports.

The Google Cloud console stores these credentials as part of a user's profile. These credentials are encrypted at rest, are only accessible with the user's Google Cloud or Google Workspace credentials, and are only used for connections through Connect. These credentials cannot be downloaded again. The credentials are deleted when the user logs out of the cluster, when the cluster registration is deleted in Google Cloud, when the project is deleted, or when the user account is deleted. For more information, see [Data deletion on Google Cloud](https://docs.cloud.google.com/security/deletion).

When a user interacts with the Google Cloud console, it generates requests for the Kubernetes API server. The service sends the user's credentials along with the request through Connect. The agent then presents the request and credentials to the Kubernetes API server.

The Kubernetes API server authenticates the user's credentials, performs authorization on the user's identity, produces an audit event for the action ([if configured](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)), and returns the result. Because the user-provided credentials are used to authenticate the request, the Kubernetes API server applies the same authorization and auditing policy for Connect requests as it does for other requests.

### Service-to-Kubernetes authentication

Google Cloud services that access the Kubernetes API server outside of a user's context use Kubernetes impersonation to authenticate to the Kubernetes API server. This method allows the Kubernetes API server to provide per-service authorization checks and audit logging, as illustrated in the following diagram.

[ ![Architecture of per-service authorization checks \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-5-per-service-authorization.svg)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-5-per-service-authorization.svg) Architecture of per-service authorization checks (click to enlarge)

Services at Google Cloud can use Connect outside of a user's context. For example, a multicluster ingress service can automatically synchronize ingress resources across clusters. These services don't have credentials that the Kubernetes API server can authenticate: most API servers aren't configured to authenticate Google Cloud service's credentials. However, an API server can delegate limited authentication privileges to another service through [impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation), and the agent can authenticate Google Cloud services sending requests through Connect. Together, these allow requests through the agent to authenticate as Google Cloud service accounts.

When a Google Cloud service sends a request on its own behalf (rather than in a user's context), the agent adds its own [Kubernetes credentials](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/), and [Kubernetes impersonation headers](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) that identify the Google Cloud service, to the request. The impersonation headers claim a user name of the Google Cloud service account authenticated by the agent.

The Kubernetes API server authenticates the agent's credentials, and also checks that the agent [can impersonate](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb) the Google Cloud service account. The ability to impersonate is typically controlled by role-based access control (RBAC) rules, and can be limited to specific identities, such as Google Cloud service accounts.

If the agent is authorized to impersonate the requested identity, the API server then performs [authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) checks for the Google Cloud service account, and serves the request. The audit log for the request includes both the agent's identity and the impersonated Google Cloud service account.

## In-cluster security

The agent ultimately sends Kubernetes API requests to the Kubernetes API server, as illustrated in the following diagram.

[ ![Architecture of Kubernetes API requests sent to Kubernetes API server \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-6-agent-sends-requests.svg)](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/docs/connect-agent/images/security-features-of-connect-for-anthos-6-agent-sends-requests.svg) Architecture of Kubernetes API requests sent to Kubernetes API server (click to enlarge)

The Kubernetes API server authenticates, authorizes, and audit-logs these requests, just as it does for all other requests it serves.

As a proxy for these requests, the agent has access to sensitive data, such as credentials, requests, and responses. Kubernetes and the Kubernetes ecosystem provide a set of tools to prevent other actors from getting that access, and for helping to ensure that the agent only accesses what it's supposed to.

### Kubernetes authentication

The Kubernetes API server authenticates the sender of each incoming request to determine what permissions to apply in the authorization stage. As previously described, the request either includes a user's credentials, or includes the agent's Kubernetes credentials and impersonation headers.

Cluster admins remain in control of authentication mechanisms recognized by the Kubernetes API server. Admins might be able to revoke a user's credentials, and can revoke or reduce the privilege of the agent's credentials.

### Kubernetes authorization

The Kubernetes API server checks that the authenticated identity is allowed to take the requested action on the requested resource.

The cluster admin can use any of the [Kubernetes authorization mechanisms](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) to configure authorization rules. Connect doesn't perform any authorization checks on behalf of the cluster.

### Agent security

The agent has access to its own (Kubernetes and Google Cloud) credentials, as well as the credentials, requests, and responses that pass through it. As such, the agent occupies a trusted position in a connected cluster.

The agent is designed with the following security fundamentals:

  * The agent is written in [Go](http://golang.org), which provides garbage-collected memory management, and prevents many [unsafe](https://godoc.org/unsafe) memory operations.
  * The agent is deployed in a [distroless](https://github.com/GoogleContainerTools/distroless) container image. The agent's image doesn't include a [shell](https://wikipedia.org/wiki/Shell_\(computing\)), [libc](https://wikipedia.org/wiki/C_standard_library), or other code that is extraneous to the agent's execution path.
  * The agent's image is built by Google's shared build infrastructure from checked-in code. Only this build system can deploy agent images to [Container Registry](http://gcr.io). Google Cloud developers cannot deploy new images on their own. This process helps to ensure that all edits to the agent's source can be traced back to an author and reviewer for non-repudiation.



The agent runs as a standard [deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) in a Kubernetes cluster that deploys at the time that you register your cluster. As a result, all of the options and best practices available for monitoring and securing deployments, `ReplicaSets`, and pods are available for the agent.

These mechanisms are designed to make it difficult to compromise the agent container. However, privileged access to the agent's node can still compromise the agent's environment; therefore, it is important for administrators to follow standard Kubernetes security guidelines for protecting cluster infrastructure.

## Data security with VPC Service Controls

VPC Service Controls provides an additional layer of security defense for Google Cloud services that is independent of Identity and Access Management (IAM). While IAM enables granular _identity-based access control_ , VPC Service Controls enables broader _context-based perimeter security_ , including controlling data egress across the perimeter—for example, you can specify that only certain projects can access your BigQuery data. You can find more about how VPC Service Controls works to protect your data in the VPC Service Controls [Overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

You can use VPC Service Controls with Connect for extra data security, once you ensure that the necessary services to use Connect can be accessed from within your specified service perimeter.

If you want to use VPC Service Controls, you need to enable the following APIs:

  * `cloudresourcemanager.googleapis.com`
  * `gkeconnect.googleapis.com`
  * `gkehub.googleapis.com`



You also need to set up [private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity) for access to the relevant APIs. You can find out how to do this in [Set up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
