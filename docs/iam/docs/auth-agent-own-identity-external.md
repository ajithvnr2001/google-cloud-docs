---
url: https://docs.cloud.google.com/iam/docs/auth-agent-own-identity-external/
title: Authenticate to external services using an agent's own identity \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:42.472295+00:00
---

# Authenticate to external services using an agent's own identity  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/auth-agent-own-identity-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Authenticate to external services using an agent's own identity Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agent Identity lets your agents on Google Cloud use their own identity to authenticate to external services and to workloads hosted on Cloud Run or Google Kubernetes Engine (GKE). By using OpenID Connect (OIDC) ID tokens, you can connect agents to third-party cloud platforms such as Amazon Web Services (AWS) and Microsoft Azure, custom APIs, API gateways, and on-premises backends.

When an agent acts on its own authority, Agent Identity issues an OIDC ID token, which is a JSON Web Token (JWT) that asserts the agent's [SPIFFE identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity) and is signed by the issuer keys for the agent's trust domain (managed workload identity pool). External systems can verify these ID tokens without Google Cloud credentials or SDKs through public endpoints hosted by the Google Cloud Security Token Service:

  * An **OpenID Connect Discovery 1.0 endpoint** (`/.well-known/openid-configuration`) that publishes the OpenID provider metadata and the public key endpoint (`jwks_uri`).
  * A **JSON Web Key Set (JWKS) endpoint** (`/openid/jwks`) that serves the active public keys used to verify signatures on agent ID tokens.



To authenticate your agent to Google Cloud APIs and resources using its own identity, see [Authenticate to Google Cloud using an agent's own identity](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity). To access services on behalf of an end user, see [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2).

## Before you begin

  1. [Verify that you have chosen the correct authentication method](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models). Review how [SPIFFE identities, trust domains](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity), and [agent credentials](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-credentials) work in the [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview).
  2. [Create and deploy an agent](https://docs.cloud.google.com/iam/docs/create-and-deploy-agent) with Agent Identity enabled.
  3. Ensure that your external service or identity provider meets the following requirements:

     * It supports validating [JSON Web Tokens (JWTs)](https://datatracker.ietf.org/doc/html/rfc7519) using [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) and [JSON Web Key Sets (JWKS)](https://datatracker.ietf.org/doc/html/rfc7517).
     * If it enforces certificate binding over mutual TLS (mTLS), it supports client certificate authentication under [TLS 1.3 (RFC 9846)](https://www.rfc-editor.org/info/rfc9846/) and validates the `cnf` (`x5t#S256`) claim according to [RFC 8705 Section 6.1](https://www.rfc-editor.org/info/rfc8705/#section-6.1).
     * It can send outbound HTTPS requests to `https://sts.googleapis.com` to retrieve the OpenID Provider metadata and public signing keys.
  4. Identify the following configuration values for your agent and target external service:

     * **Issuer URL (`iss` claim)**: The workload identity pool issuer URL for your organization (`https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN`) or project (`https://sts.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/TRUST_DOMAIN`).
     * **Allowed audience (`aud` claim)**: The audience URI that the external service or identity provider expects when validating ID tokens.
  5. Verify that you have the roles required to complete this task.




### Required roles

To get the permissions that you need to deploy an agent with Agent Identity, ask your administrator to grant you the following IAM roles on your project: 

  * Deploy an agent to Agent Runtime on Gemini Enterprise Agent Platform: [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) 
  * Deploy an agent service to Cloud Run: [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to deploy an agent with Agent Identity. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to deploy an agent with Agent Identity:

  * Deploy an agent to Agent Runtime on Gemini Enterprise Agent Platform: 
    * `aiplatform.reasoningEngines.create`
    * `aiplatform.reasoningEngines.update`
  * Deploy an agent service to Cloud Run: 
    * `run.services.create`
    * `run.services.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** External services and third-party verifiers don't need any IAM roles or Google Cloud credentials to verify OIDC ID tokens issued by Agent Identity. The OpenID Connect Discovery (`/.well-known/openid-configuration`) and JSON Web Key Set (`/openid/jwks`) endpoints are public and unauthenticated.

## Obtain an OIDC ID token for an agent

To configure your agent to obtain and send an OIDC ID token to an external service, complete the following tasks:

  1. Configure your agent with Agent Identity
  2. Request an OIDC ID token in application code



### Configure your agent with Agent Identity

Enable Agent Identity when you deploy your agent:

  * If you deploy your agent to Agent Runtime on Gemini Enterprise Agent Platform , set `identity_type` to `AGENT_IDENTITY`:
        
        remote_app = client.agent_engines.create(
            agent=app,
            config={
                "identity_type": types.IdentityType.AGENT_IDENTITY,
                "requirements": ["google-cloud-aiplatform[agent_engines,adk]"],
            },
        )
        

  * If you deploy a containerized agent service to Cloud Run, pass the `--identity-type=agent-identity` flag:
        
        gcloud run deploy SERVICE_NAME \
            --image=IMAGE_URL \
            --identity-type=agent-identity \
            --no-allow-unauthenticated

Replace the following:

    * `SERVICE_NAME`: The name of your Cloud Run service.
    * `IMAGE_URL`: The container image URL for your agent.



### Request an OIDC ID token in application code

In your agent's application code, use the Google Auth client library to request an OIDC ID token for your target external audience. The client library handles token generation, local caching, and automatic renewal from the metadata server.

By default, supported Google Auth client libraries cryptographically bind OIDC ID tokens to the agent's unique X.509 certificate by including the certificate fingerprint in the token's `cnf` (`x5t#S256`) claim. Receiving services can optionally validate this claim against the client certificate presented during a mutual TLS (mTLS) handshake, or ignore the claim if they don't enforce certificate binding.

Cloud Run automatically enforces certificate binding when the `cnf` claim is present in an ID token. If your agent calls a Cloud Run service using a bound ID token, you must call its mTLS endpoint (`*.mtls.run.app`) over an mTLS connection. To keep calling a standard `*.run.app` URL instead, opt out of certificate binding per request (for example, by setting `bind_id_token=False` in Python) or across the runtime environment with `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN=false`. For supported library versions and examples, see [Opt out of certificate-bound tokens](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity#opt-out-caa).

When calling an endpoint that enforces certificate binding over mTLS, configure the client session to present the agent's X.509 certificate during the mTLS handshake (for example, by calling `authed_session.configure_mtls_channel()` in Python).

The following examples use the `google-auth` library to request a certificate-bound OIDC ID token, optionally configure the mTLS channel, and attach the token as a `Bearer` token in an outgoing request:

### Python
    
    
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import id_token
    
    # 1. Specify the audience expected by the external receiver
    # (for example, AWS Bedrock AgentCore or your external service URL).
    target_audience = "https://EXTERNAL_SERVICE_AUDIENCE"
    
    # 2. Create ID token credentials and an AuthorizedSession, which handles
    # local token caching, automatic renewal before expiry, and the
    # Bearer header.
    credentials = id_token.fetch_id_token_credentials(audience=target_audience)
    authed_session = AuthorizedSession(credentials)
    
    # 3. Send the authenticated request to the external service.
    response = authed_session.post(
        "https://EXTERNAL_SERVICE_ENDPOINT",
        json={"prompt": "Hello from Agent"},
    )

Replace the following:

  * `EXTERNAL_SERVICE_AUDIENCE`: The audience URI expected by your receiving service (for example, `bedrock.us-east-1.amazonaws.com` or `api.example.com`).
  * `EXTERNAL_SERVICE_ENDPOINT`: The URL of the external API or backend endpoint that your agent calls.



### Python (mTLS)
    
    
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import id_token
    
    # 1. Specify the audience expected by the receiving service
    # (for example, a regional Cloud Run mTLS URL or an on-premises mTLS endpoint).
    target_audience = "https://EXTERNAL_SERVICE_AUDIENCE"
    
    # 2. Create certificate-bound ID token credentials and configure the mTLS
    # channel to present the agent's X.509 certificate.
    credentials = id_token.fetch_id_token_credentials(audience=target_audience)
    authed_session = AuthorizedSession(credentials)
    authed_session.configure_mtls_channel()
    
    # 3. Send the authenticated request over mTLS.
    response = authed_session.post(
        "https://EXTERNAL_SERVICE_ENDPOINT",
        json={"prompt": "Hello from Agent"},
    )

Replace the following:

  * `EXTERNAL_SERVICE_AUDIENCE`: The audience URI expected by your receiving service (for example, a regional Cloud Run mTLS URL or `api.example.com`).
  * `EXTERNAL_SERVICE_ENDPOINT`: The URL of the mTLS API or backend endpoint that your agent calls.



For client library instructions and examples in other languages, such as Go, Node.js, and Java, see [Get an ID token](https://docs.cloud.google.com/docs/authentication/get-id-token). Client libraries for these languages support `--identity-type=agent-identity`. Libraries that support certificate-bound ID tokens bind tokens by default and let you opt out for individual requests.

## Verify Agent Identity ID tokens

When an external service receives an OIDC ID token from your agent, verify the token using either of the following approaches based on the target service:

  * **Managed cloud platforms (such as Cloud Run, AWS, or Microsoft Azure)** : Use built-in workload identity federation to verify incoming tokens without writing custom verification code.
  * **Custom backend services, API gateways, and on-premises workloads** : Verify tokens programmatically using the public OpenID Connect Discovery and JWKS endpoints.



### Use built-in workload identity federation

If your receiving service runs on a cloud platform that supports built-in IAM authentication or OIDC workload identity federation, you don't need to write custom token verification code:

  * **Cloud Run** : If your receiving service runs on Cloud Run with authenticated ingress (`--no-allow-unauthenticated`), Cloud Run validates incoming Agent Identity tokens at the ingress layer. When the token includes the `cnf` claim, configure the calling agent to target the receiving service's regional mTLS URL (`https://SERVICE_NAME-PROJECT_NUMBER.REGION.mtls.run.app`) so that Cloud Run can validate the client certificate during the mTLS handshake. [Grant the calling agent](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity#grant-access) the Cloud Run Invoker (`roles/run.invoker`) role on the receiving service. For more information, see [Authenticate to MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/ai/authenticate-agents#authenticate-mcp-servers).

If your service allows unauthenticated ingress and verifies tokens in application code, see Verify tokens programmatically.

  * **Amazon Bedrock** : Configure inbound JWT authentication by specifying the Google Cloud Security Token Service discovery URL or issuer URL and your expected audience. For instructions, see [Configure inbound JWT authorizer](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/inbound-jwt-authorizer.html) in the AWS documentation.

  * **Microsoft Entra ID** : Configure a federated identity credential with the **Other issuer** scenario. Specify the Google Cloud Security Token Service issuer URL, the expected audience, and the subject identifier (`sub` claim). For instructions, see [Create a trust relationship between an app and an external identity provider](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust) in the Microsoft Learn documentation.




### Verify tokens programmatically

If your agent sends requests to a custom API, microservice, API gateway, or on-premises workload, your receiving service must verify the incoming OIDC ID token before granting access. Your agent typically passes this token in the `Authorization: Bearer TOKEN` HTTP header.

To verify incoming ID tokens programmatically, complete the following tasks:

  1. Extract and validate the token issuer URL
  2. Discover and cache the public signing keys
  3. Verify the token signature and claims
  4. Optional: Validate certificate binding (`cnf` claim)
  5. Authorize the agent's SPIFFE identity



#### Extract and validate the token issuer URL

When an incoming request arrives, read the unverified JWT payload to extract the `iss` (issuer) claim. This claim contains the URL of the workload identity pool for the agent's [trust domain](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity). This URL serves as the base URL for the discovery document and public signing keys.

Before making any outgoing network requests, verify that the `iss` claim matches the expected Google Cloud Security Token Service workload identity pool URL for your organization or project:

  * **Organization-level trust domains** :
        
        https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN

For example, for an organization with ID `123456789012`, `TRUST_DOMAIN` is `agents.global.org-123456789012.system.id.goog`.

  * **Project-level trust domains** (for projects without an organization):
        
        https://sts.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/TRUST_DOMAIN

For example, for a project with number `9876543210`, `TRUST_DOMAIN` is `agents.global.proj-9876543210.system.id.goog`.


**Caution:** Always validate that the `iss` URL starts with `https://sts.googleapis.com/v1/` and belongs to a trusted Google Cloud organization or project before sending HTTP requests to the discovery endpoint.

#### Discover and cache the public signing keys

After you validate the issuer URL, retrieve and cache the public signing keys from the Google Cloud Security Token Service:

  1. **Query the OpenID Connect Discovery endpoint** : Append `/.well-known/openid-configuration` to the base issuer URL and send an unauthenticated HTTP `GET` request:

Before using any of the request data, make the following replacements: 

     * `ORGANIZATION_ID`: Your Google Cloud organization ID. For a project without an organization, replace `organizations/ORGANIZATION_ID` with `projects/PROJECT_NUMBER`.
     * `TRUST_DOMAIN`: The workload identity pool ID for your agent's trust domain (for example, `agents.global.org-123456789012.system.id.goog`).

HTTP method and URL: 
    
    GET https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN/.well-known/openid-configuration

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    curl -X GET \  
         "https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN/.well-known/openid-configuration"

#### PowerShell (Windows)

Execute the following command: 
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN/.well-known/openid-configuration" | Select-Object -Expand Content

A successful request returns an `HTTP 200 OK` status and a JSON object containing the [OpenID Provider metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfigurationResponse), including the `jwks_uri` field:
    
    {
      "issuer": "https://sts.googleapis.com/v1/organizations/123456789012/locations/global/workloadIdentityPools/agents.global.org-123456789012.system.id.goog",
      "jwks_uri": "https://sts.googleapis.com/v1/organizations/123456789012/locations/global/workloadIdentityPools/agents.global.org-123456789012.system.id.goog/openid/jwks",
      "authorization_endpoint": "https://sts.googleapis.com/v1/organizations/123456789012/locations/global/workloadIdentityPools/agents.global.org-123456789012.system.id.goog/authorize",
      "token_endpoint": "https://sts.googleapis.com/v1/organizations/123456789012/locations/global/workloadIdentityPools/agents.global.org-123456789012.system.id.goog/token",
      "response_types_supported": [
        "id_token"
      ],
      "subject_types_supported": [
        "public"
      ],
      "id_token_signing_alg_values_supported": [
        "RS256"
      ]
    }
    

  2. **Query the JSON Web Key Set (JWKS) endpoint** : Send an unauthenticated HTTP `GET` request to the `jwks_uri` URL returned in the OpenID Provider metadata:

Before using any of the request data, make the following replacements: 

     * `ORGANIZATION_ID`: Your Google Cloud organization ID. For a project without an organization, replace `organizations/ORGANIZATION_ID` with `projects/PROJECT_NUMBER`.
     * `TRUST_DOMAIN`: The workload identity pool ID for your agent's trust domain (for example, `agents.global.org-123456789012.system.id.goog`).

HTTP method and URL: 
    
    GET https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN/openid/jwks

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    curl -X GET \  
         "https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN/openid/jwks"

#### PowerShell (Windows)

Execute the following command: 
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sts.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/workloadIdentityPools/TRUST_DOMAIN/openid/jwks" | Select-Object -Expand Content

A successful request returns an `HTTP 200 OK` status and a JSON object containing an array of public keys formatted according to [RFC 7517](https://datatracker.ietf.org/doc/html/rfc7517#section-4):
    
    {
      "keys": [
        {
          "kty": "RSA",
          "use": "sig",
          "alg": "RS256",
          "kid": "4d1933f8e6c4e0b512c140989f6655c68997...",
          "n": "uQn4zN_1mQ0VpGv82-Wp3w...",
          "e": "AQAB"
        }
      ]
    }
    

  3. **Cache the discovery document and keys** : Responses from both the OpenID Connect Discovery endpoint and the JWKS endpoint include the following HTTP cache header:
         
         Cache-Control: public, max-age=86400, must-revalidate
         

Cache the discovery document and JWKS for up to 24 hours (`86400` seconds) to improve verification performance and avoid rate limiting.

Google Cloud periodically rotates the private and public signing keys for workload identity pools. If your verifier receives an incoming token with a `kid` (key ID) that isn't in its local key cache, fetch a fresh JWKS from the `/openid/jwks` endpoint before rejecting the token.

If you encounter HTTP errors when querying the discovery or JWKS endpoints, see [Troubleshoot Agent Identity authentication issues](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager#oidc-jwks-errors).




#### Verify the token signature and claims

To cryptographically verify the token signature and validate the JWT claims, use a standard OIDC or JWT verification library (such as [Google Tink](https://developers.google.com/tink)) and do the following:

  1. **Signature** : Find the public key in the cached JWKS that matches the `kid` (key ID) in the JWT header. Validate the signature using the algorithm specified in the `alg` field (`RS256`). For forward compatibility, inspect the `alg` and `kty` fields in the JWKS dynamically rather than hardcoding algorithm types.
  2. **Issuer (`iss`)**: Confirm that the `iss` claim matches the trusted Google Cloud workload identity pool issuer URL for your trust domain.
  3. **Audience (`aud`)**: Confirm that the `aud` claim matches your service's configured audience identifier.
  4. **Issued-at time (`iat`) and expiration time (`exp`)**: Verify that the `iat` claim is in the past and that the current time is earlier than the `exp` claim (allowing a small clock-skew tolerance, such as 1 to 2 minutes).



The following example uses Google Tink (`tink.jwt`) to verify an Agent Identity ID token against a JWKS JSON payload:

### Python
    
    
    import tink
    from tink import jwt
    
    # Initialize Tink JWT signature primitives (call once at application startup).
    jwt.register_jwt_signature()
    
    
    def verify_agent_identity_token(
        token: str,
        jwks_json: str,
        expected_issuer: str,
        expected_audience: str,
    ) -> jwt.VerifiedJwt:
        """Verifies an Agent Identity JWT against a JWKS JSON string using Tink.
    
        Args:
            token: The compact serialized JWT string.
            jwks_json: The JWKS JSON string fetched from the STS pool endpoint.
            expected_issuer: The expected token issuer ('iss' claim).
            expected_audience: The expected token audience ('aud' claim).
    
        Returns:
            jwt.VerifiedJwt: The verified JWT claims object.
    
        Raises:
            tink.TinkError: If the JWKS cannot be parsed, the key is not found,
                or token validation (signature, issuer, audience, expiration) fails.
        """
        # 1. Convert the JWKS JSON into a Tink public KeysetHandle.
        keyset_handle = jwt.jwk_set_to_public_keyset_handle(jwks_json)
    
        # 2. Instantiate the Tink JwtPublicKeyVerify primitive.
        jwt_verifier = keyset_handle.primitive(jwt.JwtPublicKeyVerify)
    
        # 3. Configure expected validation rules (issuer, audience, expiration).
        # Google Cloud STS sets 'typ': 'JWT' in the header, so
        # expected_type_header="JWT" is required.
        validator = jwt.new_validator(
            expected_issuer=expected_issuer,
            expected_audience=expected_audience,
            expected_type_header="JWT",
            allow_missing_expiration=False,
        )
    
        # 4. Cryptographically verify the signature and standard OIDC claims.
        return jwt_verifier.verify_and_decode(token, validator)

#### Optional: Validate certificate binding (`cnf` claim)

If your receiving service enforces certificate binding over mTLS, validate the `cnf` (`x5t#S256`) claim against the client certificate presented during the mTLS handshake:

  1. **Terminate mutual TLS (mTLS)** : Configure your server or ingress proxy to request and validate the [agent's X.509 certificate](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-credentials) during the TLS handshake according to [TLS 1.3 (RFC 9846)](https://www.rfc-editor.org/info/rfc9846/).
  2. **Compute the certificate fingerprint (`x5t#S256`)**: Extract the leaf X.509 client certificate from the mTLS connection. Compute the SHA-256 hash over its DER-encoded bytes, and base64url-encode the digest without `=` padding.
  3. **Validate the`cnf` (`x5t#S256`) claim**: Inspect the verified JWT payload for the `cnf` object (`{"cnf": {"x5t#S256": "FINGERPRINT"}}`) and verify that the `x5t#S256` value matches the client certificate fingerprint according to [RFC 8705 Section 6.1](https://www.rfc-editor.org/info/rfc8705/#section-6.1). If the caller didn't present a client certificate over mTLS or if the fingerprints don't match, reject the request with an `HTTP 401 Unauthorized` response.



#### Authorize the agent's SPIFFE identity

After you verify the token's signature and standard claims, inspect the verified `sub` (subject) claim to authorize the request and record the calling agent in your audit logs.

The `sub` claim contains the agent's unique [SPIFFE ID](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity), for example:
    
    
      spiffe://agents.global.org-123456789012.system.id.goog/resources/aiplatform/projects/9876543210/locations/us-central1/reasoningEngines/my-test-agent
    

In your service's authorization logic, compare the verified `sub` claim against an allowlist of trusted agent SPIFFE IDs (or trust domain prefixes) before granting access to protected resources.

## What's next

  * [Troubleshoot Agent Identity authentication issues](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager#oidc-jwks-errors)
  * [Authenticate to Google Cloud using an agent's own identity](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity)
  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2)
  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
