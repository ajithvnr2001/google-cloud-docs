---
url: https://docs.cloud.google.com/run/docs/deploy-a2a-agents/
title: Deploy A2A agents to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:15.883810+00:00
---

# Deploy A2A agents to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/deploy-a2a-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deploy A2A agents to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Agent2Agent (A2A)**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Prepare and configure Agent2Agent (A2A) agents for deployment on Cloud Run.

This guide covers essential steps for deploying A2A agents:

  * Configure your project
  * Establish IAM roles
  * Configure your cloud environment
  * Deploy your agent
  * Debug deployment failures
  * Test and monitor



## Review the A2A specification and sample agents

Before you start developing and deploying your A2A agent, familiarize yourself with the following concepts and resources:

  * Review the official [A2A specification](https://a2aproject.github.io/A2A/latest/specification/) and [agent communication concepts](https://a2aproject.github.io/A2A/latest/topics/key-concepts/) for agent communication.
  * Explore existing [sample agents](https://github.com/a2aproject/a2a-samples).
  * Review the [ADK Cloud Run sample](https://github.com/a2aproject/a2a-samples/tree/main/samples/python/agents/adk_cloud_run).



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. By default, we recommend assigning a secure, system-managed [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) to your agent by passing the `--functional-type=agent` and `--identity-type=agent-identity` flags during deployment. For instructions, see [Configure agent platform features](https://docs.cloud.google.com/run/docs/ai/agent-platform-features). If you must deploy your agent with a standard service account, you can [Create a user-managed service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and pass the `--service-account` flag during deployment. 



#### Grant the service account roles

To grant the required IAM roles to your account on your project:
    
    
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:A2A_SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
             --role="ROLE"
         

Replace:

  * PROJECT_ID: your project ID
  * A2A_SERVICE_ACCOUNT_NAME: the name of your service account
  * ROLE: the role you are adding to the service account



### Required roles

To get the permissions that you need to deploy A2A agents, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on the project
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project
  * [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) on the service account
  * [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) on the service account
  * If you are deploying with AlloyDB for PostgreSQL, grant the following roles: 
    * [AlloyDB for PostgreSQL client ](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.client) (`roles/alloydb.client`) on the service account
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Grant the roles

#### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address that is used to deploy the Cloud Run service.

  5. In the **Select a role** list, select a role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



#### gcloud

To grant the required IAM roles to your account on your project:
    
    
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=PRINCIPAL \
             --role=ROLE
         

Replace:

  * PROJECT_NUMBER with your Google Cloud project number.
  * PROJECT_ID with your Google Cloud project ID.
  * PRINCIPAL with the account you are adding the binding for. This is typically the email address that is used to deploy the Cloud Run service.
  * ROLE with the role you are adding to the deployer account.



## Prepare for Cloud Run deployment

This section describes the configurations required to prepare your A2A agent for deployment to Cloud Run for a Python code sample.

### Prepare A2A agent

  1. Retrieve the code sample by cloning the sample app repository to your local machine:
         
         git clone https://github.com/a2aproject/a2a-samples
         

  2. Change to the directory that contains the sample code:
         
         cd a2a-samples/samples/python/agents/adk_cloud_run
         




### Configure secrets for Cloud Run services

Provide all sensitive credentials, such as API keys and database passwords, to your A2A server using a secure mechanism. Cloud Run supports providing secrets as environment variables or dynamically mounted volumes. For more information, see [Configure secrets in Cloud Run](https://docs.cloud.google.com/run/docs/configuring/secrets).

Agents need access to external services to complete their tasks. Secrets are the secure mechanism for granting that access. When deploying with AlloyDB for PostgreSQL, you need the user and password. Create and manage the database user and password secrets within Secret Manager by running the following commands in the gcloud CLI:
    
    
    gcloud secrets create alloy_db_user --replication-policy="automatic"
    # Create a file user.txt with contents of secret value
    gcloud secrets versions add alloy_db_user --data-file="user.txt"
    
    gcloud secrets create alloy_db_pass --replication-policy="automatic"
    # Create a file pass.txt with contents of secret value
    gcloud secrets versions add alloy_db_pass --data-file="pass.txt"
    

For more information, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).

### Dockerfile for containerization

Cloud Run can deploy services either from already hosted container images or directly from your source code. When deploying from source code, Cloud Run automatically builds a container image if a Dockerfile is present in your project's root directory.

The Dockerfile determines the details of the container image. The following is the Dockerfile from the sample A2A agent you cloned earlier:
    
    
    FROM python:3.13-slim
    COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
    EXPOSE 8080
    WORKDIR /app
    COPY . ./
    RUN uv sync
    ENTRYPOINT ["uv", "run", ".", "--host", "0.0.0.0", "--port", "8080"]
    

#### Deploy from source code without a Dockerfile

For source code repositories without a Dockerfile, Cloud Run offers built-in support for certain popular programming languages, simplifying the containerization process.

  * **Python applications on Cloud Run:** Cloud Run looks for a [`main.py`](https://github.com/a2aproject/a2a-samples/blob/50b7363f11477f400520affef4ac748e5117fee2/samples/python/agents/adk_cloud_run/__main__.py) file to build and deploy Python services. For more information, see the [Deploy a Python service on Cloud Run quickstart](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/python).
  * **Node.js applications on Cloud Run:** Cloud Run looks for an `index.js` file to build and deploy Node.js services. See the [Deploy a Node.js service on Cloud Run quickstart](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/nodejs).



## Deploy the A2A agent to Cloud Run

To assign a system-managed identity to your A2A agent and register it in the Agent Platform, see [Configure agent platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).

Deploy your A2A application with an in-memory `TaskStore` configuration or with AlloyDB for PostgreSQL.

  * An in-memory `TaskStore` configuration stores all its data exclusively within the Cloud Run container instance. This means that all task data is lost when the container instance shuts down, scales down, or restarts.
  * AlloyDB for PostgreSQL provides data persistence, enabling agents to scale horizontally, and ensuring tasks survive container restarts, scale events, and deployments.



An in-memory `TaskStore` configuration is suitable for developing A2A agents in the local environment, and AlloyDB for PostgreSQL is suitable for scaling the A2A agent in production.

The following commands show how to use IAM-based authentication for your Cloud Run service. Using the `--no-allow-unauthenticated` flag at deployment is the recommended approach for configuring authentication for internal Google Cloud clients, such as Gemini Enterprise.

If your A2A server is designed for public access, and needs to handle agent-level authentication, you can specify the `--allow-unauthenticated` flag during deployment. See [Cloud Run public access authentication](https://docs.cloud.google.com/run/docs/authenticating/public) for more details. To allow for public access to your Cloud Run service, you must also provide crucial authentication information in your A2A agent's card using the `securitySchemes` and `security` parameters. For more information, see [A2A Specification: SecurityScheme Object Details](https://a2a-protocol.org/latest/specification/#553-securityscheme-object).

### Deploy with an in-memory `TaskStore` configuration

To deploy your A2A agent with an in-memory `TaskStore` configuration, run the following command in the directory that contains your A2A agent source code:
    
    
    gcloud run deploy sample-a2a-agent \
        --port=8080 \
        --source="." \
        --no-allow-unauthenticated \
        --region=REGION \
        --project=PROJECT_ID \
        --memory=1Gi \
        --functional-type=agent \
        --identity-type=agent-identity \
        --set-env-vars=GOOGLE_GENAI_USE_VERTEXAI=true,GOOGLE_CLOUD_PROJECT="PROJECT_ID",GOOGLE_CLOUD_LOCATION="REGION",APP_URL="https://sample-a2a-agent-PROJECT_NUMBER.REGION.run.app"
    

Replace the following:

  * REGION: the Google Cloud region where you want to deploy your service—for example `europe-west1`.
  * PROJECT_ID: your project ID.
  * PROJECT_NUMBER: your project number.



### Deploy with AlloyDB for PostgreSQL

To persist A2A tasks, use AlloyDB for PostgreSQL. To deploy your A2A agent with AlloyDB for PostgreSQL for _persistent task storage_ , use the following command:
    
    
    gcloud run deploy sample-a2a-agent \
        --port=8080 \
        --source="." \
        --no-allow-unauthenticated \
        --region=REGION \
        --project=PROJECT_ID \
        --memory=1Gi \
        --update-secrets=DB_USER=alloy_db_user:latest,DB_PASS=alloy_db_pass:latest \
        --functional-type=agent \
        --identity-type=agent-identity \
        --set-env-vars=GOOGLE_GENAI_USE_VERTEXAI=true,GOOGLE_CLOUD_PROJECT="PROJECT_ID",GOOGLE_CLOUD_LOCATION="REGION",APP_URL="https://sample-a2a-agent-PROJECT_NUMBER.REGION.run.app",USE_ALLOY_DB="True",DB_INSTANCE="projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME/instances/primary-instance",DB_NAME="postgres"
    

Replace the following:

  * REGION: the Google Cloud region where you want to deploy your service—for example `europe-west1`.
  * PROJECT_ID: your project ID.
  * PROJECT_NUMBER: your project number.
  * CLUSTER_NAME: the name of your AlloyDB for PostgreSQL cluster.



## Debug deployment failures

If you encounter errors or Cloud Run deployment failures, consider the following:

  * **Detailed logs:** For detailed deployment logs, set the `--verbosity=info` flag in your `gcloud run deploy` command.
  * **URL mismatch:** If the `run.app` URL returned by the deploy command differs from the expected deterministic URL, update the `APP_URL` environment variable for your Cloud Run service:

    1. Use the following command to update the `APP_URL` environment variable:
           
           gcloud run services update SERVICE_NAME \
               --project="PROJECT_ID" \
               --region="REGION" \
               --update-env-vars=APP_URL="CLOUD_RUN_SERVICE_URL"
           

Replace the following:

       * SERVICE_NAME: the name of your Cloud Run service.
       * PROJECT_ID: your project ID.
       * REGION: the Google Cloud region where you want to deploy your service. For example `europe-west1`.
       * CLOUD_RUN_SERVICE_URL: the URL of your Cloud Run service.
    2. Verify that the `APP_URL` is updated correctly by describing the service:
           
           gcloud run services describe SERVICE_NAME \
               --project="PROJECT_ID" \
               --region="REGION"
           




### Understand the Cloud Run application URL

On successful deployment, Cloud Run automatically provides a `run.app` URL, which serves as the endpoint to query your active A2A service. The URL is deterministic and predictable if your service name is sufficiently short.

  * **Cloud Run URL format:** `https://TAG---SERVICE_NAME-PROJECT_NUMBER.REGION.run.app`
  * **Example URL:** `https://sample-a2a-agent-1234.europe-west1.run.app`



## Test and monitor A2A agent deployment

After successfully deploying your A2A agent to Cloud Run, thoroughly test its functionality. Establish strong monitoring practices to ensure continuous performance and reliability.

### A2A inspector: Validate agent compliance

Use the [a2a-inspector](https://github.com/a2aproject/a2a-inspector) tool to inspect, debug, and validate your deployed Google A2A agent. This tool ensures that your agent fully complies with the A2A specification and functions correctly.

After a successful connection, the inspector performs the following actions:

  * **Displays the agent card:** Automatically shows your agent's card.
  * **Validates compliance:** Checks that the card meets A2A specifications.
  * **Enables live chat:** Lets you send and receive messages with the agent.
  * **Shows raw data:** Displays raw JSON-RPC 2.0 messages in a console for debugging.



### CLI interaction with a deployed A2A agent

Use the command-line interface (CLI) tools from the [A2A samples repository](https://github.com/a2aproject/a2a-samples) to interact with your deployed service. This CLI supports bearer token-based authentication.

If your service uses IAM-based authentication, export the `gcloud` token for successful interaction:
    
    
    export A2A_CLI_BEARER_TOKEN=$(gcloud auth print-identity-token)
    # From CLI directory
    uv run . --agent CLOUD_RUN_SERVICE_URL
    

Replace CLOUD_RUN_SERVICE_URL with the URL of your deployed Cloud Run service.

> **Note:** Upon successful deployment and invocation, the [agent card](https://a2a-protocol.org/latest/topics/agent-discovery/#the-role-of-the-agent-card) appears, initiating a new task and prompting you for input. Each event in the CLI includes details such as the task ID, status, and timestamp.

### Local testing of deployed A2A services

You can test your deployed Cloud Run service locally. This is particularly useful when implementing IAM-based authentication.

#### Test IAM-based authentication for Cloud Run agents

Clients interacting with your Identity and Access Management (IAM)-secured Cloud Run service must possess the `roles/run.invoker` IAM role.

Locally test your deployed service authentication flow using the `gcloud auth print-identity-token` command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" CLOUD_RUN_SERVICE_URL/.well-known/agent.json
    

Replace `CLOUD_RUN_SERVICE_URL` with the URL of your deployed Cloud Run service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
