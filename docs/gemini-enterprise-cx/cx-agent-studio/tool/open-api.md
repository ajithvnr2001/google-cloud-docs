---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api/
title: OpenAPI tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:06.847702+00:00
---

# OpenAPI tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  OpenAPI tools Stay organized with collections  Save and categorize content based on your preferences. 

An agent can connect to an external API using an OpenAPI tool by providing the [OpenAPI](https://www.openapis.org/) schema. The agent will call the API on your behalf.

Limitations:

  * Each OpenAPI tool can only have one operation or function.



Example schema:
    
    
    openapi: 3.0.0
    info:
      title: Simple Pets API
      version: 1.0.0
    servers:
      - url: 'https://api.pet-service-example.com/v1'
    paths:
      /pets/{petId}:
        get:
          summary: Return a pet by ID.
          operationId: getPet
          parameters:
            - in: path
              name: petId
              required: true
              description: Pet id
              schema:
                type: integer
          responses:
            200:
              description: OK
      /pets:
        get:
          summary: List all pets
          operationId: listPets
          parameters:
            - name: petName
              in: query
              required: false
              description: Pet name
              schema:
                type: string
            - name: label
              in: query
              description: Pet label
              style: form
              explode: true
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: X-OWNER
              in: header
              description: Optional pet owner provided in the HTTP header
              required: false
              schema:
                type: string
            - name: X-SESSION
              in: header
              description: session id
              required: true
              schema:
                type: string
              x-ces-session-context: $context.session_id
          responses:
            '200':
              description: An array of pets
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/Pet'
        post:
          summary: Create a new pet
          operationId: createPet
          requestBody:
            description: Pet to add to the store
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Pet'
          responses:
            '201':
              description: Pet created
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Pet'
    components:
      schemas:
        Pet:
          type: object
          required:
            - id
            - name
          properties:
            id:
              type: integer
              format: int64
            name:
              type: string
            owner:
              type: string
            label:
              type: array
              items:
                type: string
    

## Injecting session context variables

You can inject variables from the session context, such as the session ID, into your OpenAPI requests. Use the `x-ces-session-context` extension field within the parameter definition. The value should be the path to the variable within the `context` object. For more information, see [Session context variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#session-context).

For example:
    
    
          parameters:
            - name: X-SESSION
              in: header
              description: session id
              required: true
              schema:
                type: string
              # This extension injects the session ID
              x-ces-session-context: $context.session_id
    

## Security Considerations

When configuring OpenAPI tools, it's important to understand how permissions are handled:

  * **Tool Execution Identity:** Actions performed by the OpenAPI tool are executed using the permissions granted to the CX Agent Studio service account, not the direct permissions of the end-user interacting with the agent.
  * **Transitive Access Risk:** This means if the CX Agent Studio service account has permissions to invoke Cloud Run functions, the tool can potentially call _any_ function accessible by that service account, even if the end-user lacks direct access.



To mitigate potential risks associated with this behavior:

  1. **Use Dedicated Projects:** We strongly recommend deploying agent applications in a dedicated project, separate from other critical resources or sensitive functions. This isolation limits the scope of permissions available to the CX Agent Studio service account.
  2. **Implement VPC Service Controls:** Utilize [VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/vpc-service-controls) to define a service perimeter around your sensitive services. This lets you to control access to services like Cloud Run functions and prevent unwanted calls from the CX Agent Studio service account.
  3. **Follow Least Privilege:** Ensure the CX Agent Studio service account is granted only the minimum necessary Identity and Access Management roles and permissions required for its intended functionality.



## API authentication

The following authentication options are supported when calling an external API:

### Service agent ID token

CX Agent Studio can generate an [ID token](https://docs.cloud.google.com/docs/authentication/token-types#id) using the Customer Engagement Suite [Service agent](https://docs.cloud.google.com/iam/docs/service-agents) (of the format: `service-{PROJECT_NUMBER}@gcp-sa-ces.iam.gserviceaccount.com`). The token is added in the authorization HTTP header when CX Agent Studio calls an external API.

If Cloud Run functions and Cloud Run services are in the same project as the agent, you don't need additional IAM permissions to call them. If they are in different projects, an ID token can be used to access Cloud Run functions and Cloud Run services after you grant the [roles/cloudfunctions.invoker](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker) and [roles/run.invoker](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker) roles to the service agent address.

### Service Account auth

Service accounts can be used to authenticate tool requests to any Google APIs which support it. Provide your service account email address.

If you haven't already, [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).

Because service accounts are principals, they can access resources in your project by [granting it a role](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-identities), just like you would for any other principal. The service account email will be used to [generate an access token](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials) which will be sent in the `Authorization` header of the tool request.

The user who is configuring the tool to use service accounts must have the following permissions:

  * `roles/iam.serviceAccountUser`



In order for Dialogflow CX to generate tokens, the Customer Engagement Suite [Service agent](https://docs.cloud.google.com/iam/docs/service-agents) must have the following permissions:

  * `roles/iam.serviceAccountTokenCreator`



The service account must also have permissions to access the service that is hosting the tool.

**Note:** If you are trying to use service accounts across multiple projects, ensure that your [organization policy supports it](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project). Both the permissions need to be granted in the project which contains the service account.

### OAuth

Provide the OAuth information for the service you are using.

If you are using OAuth for a Google service, you need to [configure OAuth for the service](https://developers.google.com/workspace/marketplace/configure-oauth-consent-screen).

### API key

You can configure API key authentication by providing the key name, request location (header or query string) and API key so that CX Agent Studio passes the API key in the request. Supply your API key using the Secret Manager secret version.

#### Secret Manager Authentication

You can store credentials as **secrets** using [Secret Manager](https://docs.cloud.google.com/secret-manager). Here are the necessary steps to authenticate your tool using secrets:

  1. [Create your secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) if you don't have one already.
  2. Grant [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#customer-engagement-suite-service-account) the [**Secret Manager Secret Accessor**](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) role on the new secret.
  3. Copy your credential into the clipboard.
  4. [Add a new secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) to your secret. Paste your credential as the secret value. 
     * Omit any newline character at the end.
  5. Copy the name of the secret version you just added. The name format is `projects/{project_id}/secrets/{secret_id}/versions/{version_id}`. Use this secret version for the tool configuration.

**Note:** We only support global Secret Manager. Usage of regional secrets is unsupported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
