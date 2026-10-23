---
url: https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity/
title: Authenticate by using an agent identity in GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:15.312228+00:00
---

# Authenticate by using an agent identity in GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Authenticate by using an agent identity in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Agent Identity for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Google Kubernetes Engine (GKE) agents that have an agent identity can use that identity to authenticate to Google Cloud APIs and to external tools and services. The agents can use their own identity or act on behalf of end users. This document shows agent application developers how to configure their applications to authenticate to various resources. You should already be familiar with how to [request an agent identity for a GKE agent](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity).

Depending on the resource that the agent needs to access, your platform administrator might need to configure the auth manager credential vault to run additional workflows. For example, for an agent to authenticate to GitHub on behalf of an end user, a 3-legged OAuth auth provider in the auth manager must handle user sign-in, authorization, and redirection. As a developer, you modify your agent to call the correct auth provider and handle resuming the conversation for the end user.

## Limitations

  * See the [Agent Identity limitations](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity#limitations).
  * You can use the Google authentication library to get bound access and ID tokens only for Python. The authentication library might not get bound tokens for other languages. If you use a different language, then switch to unbound tokens by setting the `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN` environment variable to `false`.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Connect to an existing cluster that has a running workload that uses Agent Identity. To request an agent identity for a workload, see [Request an agent identity for a GKE agent](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity).
  * To authenticate to external tools and services by using the auth manager, ask your platform administrator to do the following: 
    * [Set up an auth provider](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2) for the authentication workflow.
    * [Give your agent access to the auth provider](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access#authorize-auth-manager).



### Required roles

To get the permissions that you need to configure deployed agents in GKE clusters, ask your administrator to grant you the [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authenticate to Google Cloud APIs

To authenticate to Google Cloud APIs as the agent's own identity, the agent can use an agent identity access token from the metadata server on your nodes. The changes that you might need to make to your code depend on how you call Google Cloud APIs, as follows.

### Use the Cloud Client Libraries

If you use a version of the Cloud Client Libraries that includes version 2.61.0 or later of the `google-auth` library, then Application Default Credentials (ADC) automatically gets an agent identity access token. You don't need to make additional changes to your code. If you enable certificate injection for the Pods by setting the `iam.gke.io/inject-podcertificates: "true"` annotation, then the access token is bound to the X.509 certificate by default unless you disable bound tokens.

To get unbound access tokens when you use the Cloud Client Libraries, you do one of the following:

  * Enable certificate injection in your Pod and set the `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN` environment variable to `false`.
  * Don't enable certificate injection in your Pod.



### Use direct calls to Google Cloud API endpoints

If you don't use the Cloud Client Libraries to interact with a service, then you can use the agent's identity to authenticate to a Google Cloud API by doing the following:

  1. Get an access token from the metadata server on the node. You can get a token by using one of the following methods:

     * **Bound access tokens** : use the `google-auth` Python library, which discovers the Pod's X.509 certificate and automatically gets bound access tokens by default. For other programming languages, use unbound tokens.

     * **Unbound access tokens** : if the Pod doesn't have the agent identity credential bundle, then use the Google authentication library for your programming language. The authentication library automatically gets unbound access tokens and refreshes expiring tokens for you. For Python applications in Pods that have the credential bundle, set the `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN` environment variable in your Pod specification to `false`, such as in the following example:
           
           # Multiple lines are omitted here.
           spec:
             containers:
             - name: example-agent
               image: example-image
               **env :
               - name: GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN
                 value: "false"**
           # Multiple lines are omitted here.
           

This environment variable prevents the library from getting bound access tokens and ID tokens.

  2. For bound access tokens, send the request to the API's mTLS endpoint and include the agent identity X.509 certificate chain in the HTTP transport. If you use the Google authentication library for Python, then the library handles HTTP transport configuration for you.




The following example demonstrates how to use the Google authentication library for Python to get a bound access token and make a request to the Cloud Storage mTLS endpoint:
    
    
    import google.auth
    from google.auth.transport.requests import AuthorizedSession
    
    
    def call_storage_api_mtls(bucket_name: str) -> None:
        # Discover the Pod's X.509 certificate chain by using the auth library
        credentials, project = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        # Configure the mTLS session by using the Pod's certificate chain
        session = AuthorizedSession(credentials)
        session.configure_mtls_channel()
        # Call the Google Cloud mTLS endpoint
        mtls_url = f"https://storage.mtls.googleapis.com/storage/v1/b/{bucket_name}/o"
        response = session.get(mtls_url)
        response.raise_for_status()
        print(response.json())
    

## Authenticate to external tools and services

To authenticate to external tools and services, you can configure your agent to get the required credentials from the Agent Identity auth manager. A platform administrator configures various auth providers in the auth manager, each of which manages specific authentication workflows and credentials. You modify your application code to call a specific auth provider and, depending on the authentication workflow, to handle user consent and conversation resumption. The specific changes that you make to your agent depend on what you need to access, as follows:

  * To access external services on behalf of an end user, you do the following: 
    1. [Modify the agent](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2#authenticate-agent) to call a 3-legged OAuth auth provider.
    2. [Modify your client-side application](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2#update-client) to handle user sign-in and redirection.
  * To access external services by using the agent's own authority, you [modify your agent to call a 2-legged OAuth auth provider](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2#authenticate-agent).
  * To access external APIs by using an API key, you [modify your agent to call an API key auth provider](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2#authenticate-agent).



The auth manager handles the corresponding authentication workflows and gives the agent access to the encrypted credentials, which can then be included in requests to the external service. For more information about what your platform administrator must do to configure these auth providers and grant access to your agent identity, see [Authentication workflows for agents](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity#authentication-workflows).

## Authenticate to other agents

In multi-agent architectures, agents frequently collaborate by directly invoking peer agents or downstream services. You can establish direct communication between agent workloads by using _identity tokens_. You can get a bound or an unbound ID token from the GKE metadata server and use that token to authenticate directly to other agents.

To get an ID token and use the token in an HTTP request, use the Google authentication library for Python. The library automatically handles certificate discovery and ID token acquisition. If you use a different programming language, then the Google authentication library might not get bound ID tokens. Switch to unbound ID tokens instead.

### Get an ID token

To request an ID token in your agent code, use the Google authentication library for your programming language. You can use the library to request bound or unbound ID tokens, as follows:

  * **Bound ID tokens** : use the `iam.gke.io/inject-podcertificates: "true"` annotation to enable certificate injection for your Pod. The authentication library for Python automatically requests a certificate-bound ID token from the GKE metadata server. Use bound ID tokens when you authenticate between agents that run on Google Cloud by using mTLS.
  * **Unbound ID tokens** :

    * Enable certificate injection for your Pod and do one of the following: 
      * In your application code, in the `id_token.fetch_id_token` function, set the `bind_id_token` argument to a value of `False`. This argument causes the authentication library to request unbound ID tokens. Access token requests aren't affected.
      * In your Pod specification, set the `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN` environment variable to a value of `false`. This environment variable prevents the library from requesting bound access tokens and ID tokens.
    * Don't enable certificate injection for your Pod. The authentication library gets an unbound ID token, because there's no credential bundle in the Pod.

Use unbound ID tokens when you authenticate to Google Cloud APIs, external services, or other agents by using a non-mTLS connection.




The following examples show you how to request a bound or unbound ID token for an agent that has credential injection enabled:

  * Request a bound ID token:
        
        import google.auth.transport.requests
        from google.oauth2 import id_token
        
        # Application Default Credentials automatically requests a certificate-bound
        # ID token.
        def get_bound_id_token(target_audience: str) -> str:
            auth_req = google.auth.transport.requests.Request()
            return id_token.fetch_id_token(auth_req, audience=target_audience)
        

The bound identity token includes the SHA-256 certificate fingerprint of the Pod's X.509 certificate chain in the `cnf.x5t#S256` parameter.

  * Request an unbound ID token:
        
        import google.auth.transport.requests
        from google.oauth2 import id_token
        
        def get_unbound_id_token(target_audience: str) -> str:
            auth_req = google.auth.transport.requests.Request()
            return id_token.fetch_id_token(
                auth_req,
                audience=target_audience,
                # Always get an unbound ID token, even if the Pod has a credential
                # bundle.
                bind_id_token=False,
            )
        




### Use the ID token in a request to another agent

After you get an ID token for your agent, you can use the token to authenticate directly to another agent. How you authenticate the connection depends on whether you use a bound ID token, as follows:

  * For bound ID tokens, establish an mTLS connection with the receiving agent and authenticate the connection by using both of the following credentials from the `/var/run/secrets/workload-spiffe-credentials/` directory in the Pod: 
    * The agent identity credential bundle that's in the `x509.credential-bundle.private-key.pem` file, which contains the leaf certificate chain for the Pod.
    * The cluster trust bundle that's in the `TRUST_DOMAIN.spiffe-trust-bundle.pem` file. This file contains the root CA certificate for the _receiving agent_ , and is used to validate the receiving agent's certificate chain during the mTLS handshake. The calling and receiving agents must be in the same agent identity pool.
  * For unbound ID tokens, establish a non-mTLS connection with the receiving agent.



The following examples show you how to send a request to another agent by using a bound or unbound ID token:

  * **Bound ID token** : include the bound identity token in the `Authorization: Bearer` header of the request that you send to the receiving agent's mTLS endpoint. Authenticate the TLS connection by using the Pod's X.509 certificate and private key:
        
        import ssl
        import urllib3
        
        BUNDLE_PATH = "/var/run/secrets/workload-spiffe-credentials/x509.credential-bundle.private-key.pem"
        TRUST_BUNDLE_PATH = "/var/run/secrets/workload-spiffe-credentials/TRUST_DOMAIN.spiffe-trust-bundle.pem"
        
        def call_peer_agent_bound_mtls(target_mtls_url: str, target_audience: str) -> None:
        
            # Configure the mTLS context by using the certificate chain and trust
            # bundle from the Pod.
            ctx = ssl.create_default_context(cafile=TRUST_BUNDLE_PATH)
            ctx.load_cert_chain(BUNDLE_PATH)
            http = urllib3.PoolManager(ssl_context=ctx, assert_hostname=False)
        
            # Call a peer agent's mTLS endpoint by using the bound ID token and Pod
            # certificate chain.
            bound_id_token = get_bound_id_token(target_audience)
            response = http.request(
                "POST",
                target_mtls_url,
                headers={"Authorization": f"Bearer {bound_id_token}"},
                json={"task": "analyze_data"},
                timeout=10,
            )
            print(response.json())
        

Replace `TRUST_DOMAIN` with the trust domain for your agent identity pool.

  * **Unbound ID token** : include the token in the `Authorization: Bearer` header of your request to the peer agent:
        
        import requests
        
        def call_peer_agent_unbound(target_url: str, target_audience: str) -> None:
            unbound_id_token = get_unbound_id_token(target_audience)
            # Send the request by using a standard TLS connection or plain HTTP.
            response = requests.post(
                target_url,
                headers={"Authorization": f"Bearer {unbound_id_token}"},
                json={"task": "analyze_data"},
                timeout=10,
            )
            response.raise_for_status()
            print(response.json())
        




### Validate the request in the receiving agent

In the receiving agent, validate the ID token that's in the incoming request by doing the following. You can use cryptographic libraries like [Tink](https://developers.google.com/tink/create-jwts-signature) to perform these verification steps instead of writing custom code.

  1. Extract the identity token from the request `Authorization: Bearer` header.
  2. Verify that the `iss` (issuer) claim in the ID token is the agent identity pool for the calling agent. The issuer is one of the following, depending on whether the calling agent is in a project that's in an organization: 
     * **Project that's in an organization** : `https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/agents.global.org-ORGANIZATION_ID.system.id.goog`, where `ORGANIZATION_ID` is the organization ID of the organization that contains the calling agent's project.
     * **Project that isn't in an organization** : `https://sts.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/agents.global.proj-PROJECT_NUMBER.system.id.goog`, where `PROJECT_NUMBER` is the project number of the calling agent's GKE cluster.
  3. Discover the URI of the JSON Web Key Set (JWKS) for the issuer and cache the public JSON Web Keys (JWKs). The endpoint for the JWKS has the format `ISSUER_URL/openid/jwks`, where `ISSUER_URL` is the issuer URL.
  4. Validate the token signature by using the following information from the JOSE header of the ID token: 
     * The public JWK that matches the `kid` header parameter.
     * The cryptographic algorithm that matches the `alg` header parameter, such as `RS256`.
  5. Verify that the SHA-256 certificate fingerprint that's in the `cnf.x5t#S256` parameter matches the fingerprint of the X.509 certificate that the calling agent used to authenticate the mTLS connection.
  6. Verify the following claims in the ID token: 
     * The expiration time in the `exp` claim is in the future.
     * The audience in the `aud` claim is the receiving agent.
  7. Authorize the request based on the SPIFFE ID that's in the `sub` (subject) claim of the token.



## What's next

  * [Manage access to Google Cloud APIs for agents](https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access)
  * [Set up tracing for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/tracing)
  * [Set up logging for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/logging)
  * [Set up monitoring for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/monitoring)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
