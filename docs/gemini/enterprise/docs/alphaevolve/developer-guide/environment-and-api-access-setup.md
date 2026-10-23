---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/environment-and-api-access-setup/
title: Environment and API access setup \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:07.214323+00:00
---

# Environment and API access setup  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/environment-and-api-access-setup/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Environment and API access setup Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the necessary steps to initialize your environment, provision the API, and configure your user settings to begin working with AlphaEvolve.

  1. Prerequisites

     * Google Cloud project and licensing

     * User profiles and IAM requirements

     * Administrative host environment

  2. Setting up AlphaEvolve

     * Environment initialization (cloud admin)

     * Setting up the Discovery Engine hierarchy

     * Testing API access and verification




## Prerequisites

Before configuring your environment, verify that your Google Cloud organization completes the foundational procurement and infrastructure steps.

### Google Cloud project and licensing

  * **Google Cloud project** : Create a dedicated Google Cloud project. For project provisioning, coordinate with your assigned Google Cloud account team.

  * **Gemini Enterprise licenses** : Purchase Gemini Enterprise licenses through your Google Cloud sales representative. Any Gemini Enterprise tier, including a trial license grants access to AlphaEvolve.

  * **License allocation note** : The system requires one Gemini Enterprise license per system user who interacts with the API through service account impersonation. Google Cloud service accounts don't consume Workspace or Cloud Identity licenses.




### User profiles and IAM requirements

The AlphaEvolve lifecycle utilizes the three distinct identities.

Ensure your project complies with the following mandatory access control roles:

Profile | Description | Required roles and permissions  
---|---|---  
**Cloud Administrator** | Manages one-time initial environment configuration, IAM assignment, and enabling the Discovery Engine API and the Gemini API in Vertex AI. | 

  * `roles/resourcemanager.projectCreator` (Organization / Folder level) 
  * `roles/billing.user` (Billing account level)
  * `roles/serviceusage.admin`
  * Workspace or Cloud Identity administrator privileges

  
**System User**  
 _(Researcher / Scientist)_ |  Configures and executes optimization experiments. Interacts with the API strictly through service account impersonation.  | 

  * `roles/iam.serviceAccountTokenCreator` granted on the Service Account resource. 
  * _Optional:_ `roles/iam.serviceAccountUser` if attaching the service account to compute resources (for example, Vertex AI Workbench). 

  
**Service Account** |  Automated identity that interfaces directly with the AlphaEvolve on Cloud API service.  | 

  * `roles/discoveryengine.editor` or `roles/discoveryengine.admin` (Project-scoped)

  
  
### Administrative host environment

An administrative Linux host (such as Google Cloud Shell or a secure bastion host) runs the configuration scripts and test payloads. Verify that your host contains the following foundational utilities:

  * Google Cloud SDK: Required to execute project management commands. Install the [`gcloud` CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) if it is not present on the host.

  * curl: Validates HTTP transport access to the backend API endpoint. For Debian or Ubuntu distributions, install the utility through the package manager:
        
        sudo apt update && sudo apt install -y curl
        




## Set up AlphaEvolve

Setting up AlphaEvolve requires coordination between the cloud administrator and the system user. You must complete the following installation tasks:

### Create a service account

Use the following steps to provision a service account for your optimization experiments. The cloud administrator must execute the following commands from an administrative host:

  1. Set your Google Cloud project ID:

This step declares an environment variable for your target Google Cloud project, ensuring subsequent commands operate in the correct context.
         
         PROJECT_ID="my-gcp-project-id"
         

Alternatively, you can dynamically retrieve your active CLI project ID:
         
         PROJECT_ID=$(gcloud config get project)
         

  2. Choose a service account name:

This step declares an environment variable for the human-readable identifier of the service account, which will be used in the creation command.
         
         SA_NAME="alpha-evolve-client"
         

  3. Create the service account:

This command registers a new service account within the Google Cloud project, defining its unique name, display name, and a brief description of its intended purpose.
         
         gcloud iam service-accounts create "${SA_NAME}" \
           --description="Service Account to call AlphaEvolve on Cloud API service" \
           --display-name="AlphaEvolve Client SA" \
           --project=$PROJECT_ID
         

  4. Extract the service account email string:

This command queries the list of service accounts based on the display name and extracts the official email address as an environment variable (`SERVICE_ACCOUNT_EMAIL`) to uniquely identify the resource.
         
         SERVICE_ACCOUNT_EMAIL=$(gcloud iam service-accounts list \
           --filter="displayName:AlphaEvolve Client SA" \
           --format='value(email)' \
           --project=$PROJECT_ID)
         
         echo "Newly created Service Account Email: ${SERVICE_ACCOUNT_EMAIL}"
         

**Note:** This email matches the standard layout: `PROJECT_ID.iam.gserviceaccount.com`.
  5. Grant the Discovery Engine role to the service account:

Run the following `gcloud` command to grant the `roles/discoveryengine.admin` role to the service account at the project level:
         
         gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
           --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
           --role="roles/discoveryengine.admin" \
           --project="${PROJECT_ID}"
         

This configuration applies the following technical logic parameters:

     * `--member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}"`: Specifies the principal receiving the administrative role capabilities.

     * `--role="roles/discoveryengine.admin"`: Grants the necessary permissions to create underlying Discovery Engine instances, conversational sessions, and `AlphaEvolveExperiments` child resources.

     * `${SERVICE_ACCOUNT_EMAIL}`: Identifies the resource (the new service account) that the principal is allowed to impersonate.




### Impersonate the service account

After completing the creation steps, use the `gcloud` command-line tool to grant a researcher (`SYSTEM_USER`) the explicit ability to impersonate the newly created service account.

**Note:** For a user identity or calling service to impersonate a service account, the principal must be granted the Service Account token creator role (`roles/iam.serviceAccountTokenCreator`) on the target service account resource itself. If a researcher needs to attach this service account directly to a managed compute instance (such as a Vertex AI Workbench notebook environment), the `Service Account User` role (`roles/iam.serviceAccountUser`) is also required.

  1. Define the impersonating principal: Declare the variable target string. Replace `SYSTEM_USER_EMAIL` with the corporate identity or email address of the researcher performing the optimization runs.
         
         SYSTEM_USER="user:SYSTEM_USER_EMAIL"
         

  2. Grant the token creation role to the principal: Run the following command to map the short-lived credential token minting capability to the specified system user:
         
         gcloud iam service-accounts add-iam-policy-binding \
           "${SERVICE_ACCOUNT_EMAIL}" \
           --member="${SYSTEM_USER}" \
           --role="roles/iam.serviceAccountTokenCreator" \
           --project="${PROJECT_ID}"
         

This authorization binding ensures that:

     * `--member="${SYSTEM_USER}"`: Specifies the human user receiving the credential minting authorization.

     * `--role="roles/iam.serviceAccountTokenCreator"`: Grants permission to mint short-lived OAuth 2.0 access tokens, which drives secure service account impersonation.

     * `"${SERVICE_ACCOUNT_EMAIL}"`: Identifies the target service account resource being bound to the incoming policy.

**Note:** To attach this service account to compute instances (such as a Vertex AI Workbench), repeat the latter command and swap the target role definition parameter for the `Service Account User` role (`roles/iam.serviceAccountUser`).



### Enable the required APIs

The cloud administrator must enable two APIs in the project:

  * The Discovery Engine API (`discoveryengine.googleapis.com`), which serves the AlphaEvolve on Cloud API endpoints.

  * The Vertex AI API (`aiplatform.googleapis.com`), which serves the Gemini API in Vertex AI. AlphaEvolve generates each candidate program with an ensemble of Gemini models, so a system user cannot run an experiment until this API is enabled.




**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,aiplatform.googleapis.com)

Alternatively, enable both APIs with the Google Cloud SDK on the Linux Host:
    
    
    gcloud services enable discoveryengine.googleapis.com \
      aiplatform.googleapis.com --project="${PROJECT_ID}"
    

Confirm that both APIs are enabled:
    
    
    gcloud services list --enabled --project="${PROJECT_ID}" \
      --filter="config.name:(discoveryengine.googleapis.com OR aiplatform.googleapis.com)"
    

## Create Discovery Engine resources and sessions

The configuration process transitions from administrative identity setups to provisioning your core application data layer. In this stage, you build out the nested logical components required by the underlying API to manage, route, and track your code mutation experiments.

### Discovery Engine resource hierarchy

The hierarchy of Discovery Engine resources begins with a Google Cloud project, and its resources are hosted within a specific location (supported locations for AlphaEvolve are `global`, `us`, and `eu`). Within this foundational structure, a collection acts as a top-level organizational container for related resources. The [engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines) is provisioned inside a collection to host the core AI application, which is also where an assistant resource is configured to manage the generative AI properties and tools for the application. The engine manages individual user interactions captured as [session](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions) objects.

The `AlphaEvolveExperiment` is nested under a session, representing a single run of the evolutionary coding agent used for algorithm discovery and optimization within the context of that specific user interaction.

![Discovery Engine hierarchy](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/alphaevolve/der-hierarchy.png)

### Provision the resources

  1. Set your Google Cloud project ID:

This step declares an environment variable for your target Google Cloud project, ensuring subsequent commands operate in the correct context:
         
         PROJECT_ID="my-gcp-project-id"
         

or
         
         PROJECT_ID=$(gcloud config get project)
         

  2. Define your engine ID:

This step declares an environment variable for the URL-friendly unique identifier of the engine ID.
         
         ENGINE_ID="alpha-evolve-experiment-engine"
         

  3. Create the engine:

This command registers a new Engine within the Google Cloud project, defining its unique name, display name, and SolutionType (`SOLUTION_TYPE_GENERATIVE_CHAT`)
         
         URL="https://discoveryengine.googleapis.com/v1alpha"
         URL="${URL}/projects/${PROJECT_ID}/locations/global"
         URL="${URL}/collections/default_collection/engines"
         URL="${URL}?engineId=${ENGINE_ID}"
         curl -X POST "${URL}" \
           -H "Content-Type: application/json" \
           -H "x-goog-user-project: ${PROJECT_ID}" \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -d '{
             "display_name": "'"${ENGINE_ID}"'",
             "data_store_ids": [],
             "solution_type": "SOLUTION_TYPE_GENERATIVE_CHAT"
           }'
         

**Note:** Creating a new engine is asynchronous and it takes a few minutes to create it.
  4. Define your assistant ID:

This step declares an environment variable for the URL-friendly unique identifier of the assistant ID.

**Note:** Assistant Service only accepts the 'default_assistant' for the unique identifier.
         
         ASSISTANT_ID="default_assistant"
         

  5. Create the assistant:

This command registers a new Assistant within the Google Cloud project, defining its unique name, display name, and a brief description of its intended purpose.
         
         URL="https://discoveryengine.googleapis.com/v1alpha"
         URL="${URL}/projects/${PROJECT_ID}/locations/global"
         URL="${URL}/collections/default_collection/engines"
         URL="${URL}/${ENGINE_ID}/assistants?assistantId=${ASSISTANT_ID}"
         curl -X POST "${URL}" \
           -H "Content-Type: application/json" \
           -H "x-goog-user-project: ${PROJECT_ID}" \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -d '{
             "display_name": "'"${ASSISTANT_ID}"'",
             "description": null,
             "generation_config": null,
             "web_grounding_type": "WEB_GROUNDING_TYPE_UNSPECIFIED",
             "enabled_actions": null,
             "customer_policy": null
           }'
         




## Testing API access

Once your cloud administrator finishes provisioning identities, setting up service account impersonation, and verifying the engine layout, run these final checks. This quick smoke-test verifies your authorization and end-to-end connection before you run active optimization workloads.

### View and delete engines

Use your current access token or the impersonated service account to verify, list, or delete your engines:
    
    
      URL="https://discoveryengine.googleapis.com/v1alpha"
      URL="${URL}/projects/${PROJECT_ID}/locations/global"
      URL="${URL}/collections/default_collection/engines"
      curl -X GET "${URL}" \
        -H "Content-Type: application/json" \
        -H "x-goog-user-project: ${PROJECT_ID}" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"
    
    
    
      URL="https://discoveryengine.googleapis.com/v1alpha"
      URL="${URL}/projects/${PROJECT_ID}/locations/global"
      URL="${URL}/collections/default_collection/engines/${ENGINE_ID}"
      curl -X DELETE "${URL}" \
        -H "Content-Type: application/json" \
        -H "x-goog-user-project: ${PROJECT_ID}" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

Congratulations, you have completed the setup steps! Now you can execute the AlphaEvolve V1 API!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
