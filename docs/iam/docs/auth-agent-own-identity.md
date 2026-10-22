---
url: https://docs.cloud.google.com/iam/docs/auth-agent-own-identity/
title: Authenticate to Google Cloud using an agent's own identity \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:23.906966+00:00
---

# Authenticate to Google Cloud using an agent's own identity  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/auth-agent-own-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Authenticate to Google Cloud using an agent's own identity Stay organized with collections  Save and categorize content based on your preferences. 

Agents can access Google Cloud APIs and other resources using their own identity. Google recommends this method for agents hosted on Google Cloud to interact with other Google Cloud services.

When an agent acts on its own authority, it uses its primary [SPIFFE identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity) to request Google Cloud access tokens.

**Note:** If you want your agent to authenticate to external backends or third-party services using its own identity, see [Authenticate to external services using an agent's own identity](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity-external). If you want your agent to access Google Cloud services on behalf of an end user, see [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2).

## Before you begin

  1. [Verify that you have chosen the correct authentication method](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models).
  2. [Create and deploy an agent](https://docs.cloud.google.com/iam/docs/create-and-deploy-agent) with Agent Identity enabled.
  3. Verify that you have the roles required to complete this task.



### Required roles

To get the permissions that you need to grant an agent access to Google Cloud services, ask your administrator to grant you the following IAM roles on the target resource: 

  * To grant access to an agent: 
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
    * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
  * Recommended roles for the agent identity: 
    * [Agent Context Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentContextEditor) (`roles/aiplatform.agentContextEditor`)
    * [Agent Default Access ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.agentDefaultAccess) (`roles/aiplatform.agentDefaultAccess`)
    * [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
    * [Browser ](https://docs.cloud.google.com/iam/docs/roles-permissions/browser#browser) (`roles/browser`)
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Grant access to agents

To let your agent access a Google Cloud service, you must grant the agent's identity the required roles on the target resource.

In IAM allow policies, agent identities use [_principal identifiers_](https://docs.cloud.google.com/iam/docs/principal-identifiers).

To grant an agent access to a resource, use the Google Cloud console or the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the **IAM** page for the resource that you want to grant access to. 
     * For a project, go to the **IAM** page: 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

     * For other resources, go to the page for that resource and click the **Permissions** or **IAM** tab.
  2. Click person_add **Grant Access**.
  3. In the **New principals** field, enter the principal identifier that matches the level of access you want to grant: 
     * **A single agent** : `principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/ENGINE_ID`
     * **All agents in a project** : `principalSet://agents.global.org-ORGANIZATION_ID.system.id.goog/attribute.platformContainer/aiplatform/projects/PROJECT_NUMBER`
     * **All agents in an organization** : `principalSet://agents.global.org-ORGANIZATION_ID.system.id.goog/*`
  4. In the **Select a role** field, search for and select the role that you want to grant.
  5. Click **Save**.



### Google Cloud CLI

To grant an agent access to a resource, run the following command: 
    
    
    gcloud SERVICE add-iam-policy-binding RESOURCE_NAME \
        --member="PRINCIPAL_IDENTIFIER" \
        --role="ROLE"

Replace the following:

  * SERVICE: The Google Cloud service (for example, `storage` or `bigquery`).
  * RESOURCE_NAME: The name of the resource (for example, the bucket name or dataset ID).
  * PRINCIPAL_IDENTIFIER: The principal identifier that matches the level of access that you want to grant: 
    * **A single agent** : `principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/ENGINE_ID`
    * **All agents in a project** : `principalSet://agents.global.org-ORGANIZATION_ID.system.id.goog/attribute.platformContainer/aiplatform/projects/PROJECT_NUMBER`
    * **All agents in an organization** : `principalSet://agents.global.org-ORGANIZATION_ID.system.id.goog/*`
  * ORGANIZATION_ID: Your Google Cloud organization ID.
  * PROJECT_NUMBER: Your Google Cloud project number.
  * LOCATION: The location of your agent (for example, `us-central1`). (Required only for single agent access.)
  * ENGINE_ID: The ID of your reasoning engine. (Required only for single agent access.)
  * ROLE: The IAM role that you want to grant.



## Reference the agent identity in your code

The Google Cloud client libraries automatically use Agent Identity when your agent is deployed to a supported Google Cloud environment.

The following Python snippet shows how to manually use Agent Identity credentials to call the Cloud Vision API using the Agent Development Kit (ADK).
    
    
    from google.cloud import vision
    from google.auth import default
    from google.adk.tools import tool
    
    @tool
    def analyze_image_from_gcs(gcs_uri: str) -> dict:
        # Application default credentials automatically retrieve the
        # Agent Identity token from the metadata server.
        agent_identity_credentials, project_id = default()
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)(
            credentials=agent_identity_credentials,
            project=project_id
        )
    
        # Prepare the image object with the Cloud Storage URI.
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)()
        image.source.image_uri = gcs_uri
    
        # Perform label detection on the image.
        response = client.label_detection(image=image)
    
        # Check for any errors returned by the API.
        if response.error.message:
            return {"status": "failure", "error_message": response.error.message}
    
        labels = response.label_annotations
        return {"status": "success", "labels": [label.description for label in labels]}
    

## Optional: Opt out of certificate-bound tokens

A default Google-managed Context-Aware Access policy helps secure Agent Identity credentials. Beyond the Agent Gateway, the policy enforces Demonstrating Proof of Possession (DPoP) by authenticating the agent's access token. The policy also requires mutual TLS (mTLS) to access the Agent Gateway. This requirement helps ensure that only the intended, trusted runtime environment, such as a Cloud Run container or a Google Kubernetes Engine (GKE) Pod, can use the certificate-bound tokens. This security baseline makes stolen credentials unreplayable, helping protect against credential theft and account takeover (ATO).

Certificate binding helps protect two types of [agent credentials](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-credentials):

  * **Google Cloud access tokens** : Short-lived OAuth 2.0 access tokens that authenticate requests to Google Cloud APIs and other resources (`*.googleapis.com`).
  * **OpenID Connect (OIDC) ID tokens** : JSON Web Tokens (JWTs) that authenticate requests to [external services](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity-external) and to tools and services hosted on Google Cloud runtimes, such as Cloud Run (`*.mtls.run.app`) or GKE.



### Opt out of binding for all access and ID tokens

Opting out of the default Context-Aware Access policy and certificate-bound tokens across the runtime environment **isn't recommended**. Setting `GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN=false` removes token-binding protection for both Google Cloud access tokens and OIDC ID tokens, making these short-lived tokens vulnerable to theft or replay attacks.

However, you can opt out across the runtime environment in the following rare cases:

  * You have specific token-sharing requirements among agents.
  * You must inject the token directly into the request header.
  * Your agent can't authenticate and returns a [`401 UNAUTHENTICATED` error](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager#401-error).



To opt out across the runtime environment, set the following environment variable when you deploy your agent:
    
    
    config={
      "env_vars": {
        "GOOGLE_API_ENABLE_RUNTIME_BOUND_TOKEN": "false",
      }
    }

### Opt out for individual ID token requests

By default, supported Google Auth client libraries cryptographically bind OIDC ID tokens to the agent's unique X.509 certificate by including the certificate fingerprint in the token's `cnf` (`x5t#S256`) claim.

Some services, such as Cloud Run, enforce certificate binding when the `cnf` claim is present. If your agent calls these services over a non-mTLS endpoint, such as a standard `*.run.app` URL, or if a target endpoint doesn't require certificate binding, you can opt out for individual ID token requests. This setting affects only that request and doesn't disable certificate binding for Google Cloud access tokens.

### Python

In the Python `google-auth` library (`2.61.0` or later on GKE and `2.62.0` or later on Cloud Run), set `bind_id_token=False`:
    
    
    from google.auth.transport.requests import AuthorizedSession
    from google.auth.transport.requests import Request
    from google.oauth2 import id_token
    
    target_audience = "https://TARGET_SERVICE_URL"
    
    # Option 1: Use AuthorizedSession with IDTokenCredentials
    credentials = id_token.fetch_id_token_credentials(
        audience=target_audience,
        bind_id_token=False,
    )
    authed_session = AuthorizedSession(credentials)
    response = authed_session.get(target_audience)
    
    # Option 2: Fetch a raw ID token directly
    token = id_token.fetch_id_token(
        Request(),
        audience=target_audience,
        bind_id_token=False,
    )

Replace `TARGET_SERVICE_URL` with the audience URI or URL of the receiving service that your agent calls.

## Deploy the agent

When you deploy your agent to Google Cloud, ensure that Agent Identity is enabled. If you're deploying to Agent Runtime on Gemini Enterprise Agent Platform , use the `identity_type=AGENT_IDENTITY` flag:
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai import [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html)
    from vertexai.agent_engines import [AdkApp](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.AdkApp.html)
    
    # Initialize the Vertex AI client with v1beta1 API for Agent Identity support
    client = [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).Client(
        project="PROJECT_ID",
        location="LOCATION",
        http_options=dict(api_version="v1beta1")
    )
    
    # Use the proper wrapper class for your Agent Framework (e.g., AdkApp)
    app = AdkApp(agent=agent)
    
    # Deploy the agent with Agent Identity enabled
    remote_app = client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).create(
        agent=app,
        config={
            "identity_type": [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html).[IdentityType](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html).[AGENT_IDENTITY](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html#vertexai__genai_types_IdentityType_AGENT_IDENTITY),
            "requirements": ["google-cloud-aiplatform[agent_engines,adk]"],
        },
    )
    

## What's next

  * [Authenticate to external services using an agent's own identity](https://docs.cloud.google.com/iam/docs/auth-agent-own-identity-external)
  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2)
  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
