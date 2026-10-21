---
url: https://docs.cloud.google.com/run/docs/ai/agent-platform-features/
title: Configure Agent Platform features for Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:38.282296+00:00
---

# Configure Agent Platform features for Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai/agent-platform-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure Agent Platform features for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Configure Agent Platform features for Cloud Run**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) features like [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) and [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry) provide built-in capabilities for building, deploying, and managing AI agents, Model Context Protocol (MCP) servers, and tools. By enabling these features for your Cloud Run resources, you can take advantage of system-managed identities and automatic registration to simplify discovery and security for your agentic workloads.

This guide covers how to:

  * Establish required IAM roles
  * Understand functional and identity types
  * Configure features for services and jobs
  * View assigned identities
  * View registered agents and tools in Agent Registry



Cloud Run supports the following Agent Platform features:

  * [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview): assigns a unique, cryptographically verifiable identity to your workload, enabling secure connections to other agents, tools, and Google Cloud APIs.
  * [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry): automatically registers your agents and tools to make them discoverable by other developers and agents in your organization.



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

  12. Enable the Cloud Run Admin API, Identity and Access Management API, Agent Registry API, and App Hub API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,iam.googleapis.com,agentregistry.googleapis.com,apphub.googleapis.com&redirect=https%3A//console.cloud.google.com)

  13. Ensure that you have [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) in your project or organization. 
  14. [Install and initialize](https://docs.cloud.google.com/sdk/docs) the gcloud CLI. 
  15. Update components: 
         
         gcloud components update

  16. Review the Cloud Run [pricing](https://cloud.google.com/run/pricing) page for CPU, memory, and network egress. The entire size of the provisioned disk and the lifetime of the instance that is using it contribute to your cost. 



### Required roles

To get the permissions that you need to configure Agent Platform features, ask your administrator to grant you the following IAM roles on your project: 

  * To deploy and manage Cloud Run resources: [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) 
  * To manage App Hub resources, one of the following: 
    * [App Hub Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.admin) (`roles/apphub.admin`)
    * [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apiregistry#apiregistry.admin) (`roles/apiregistry.admin`)
  * To deploy with a specific identity, one of the following: 
    * [IAM Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
    * [IAM Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use cases

Use Agent Platform features with Cloud Run in the following scenarios:

  * Authenticate your agent to other agents, tools, and Google Cloud APIs using a unique, system-managed identity tied to its lifecycle.
  * Enable automatic discovery of agents and MCP servers within your organization's Agent Registry.
  * Use Identity-Aware Proxy as an authentication policy to secure MCP servers.



## Understand functional and identity types

You configure Agent Platform features by setting functional and identity properties on your Cloud Run resources.

These two properties control how to register and identify a workload:

  * **Functional type** : declares the primary purpose of the workload. Once set, this property cannot be changed or unset. You assign your workload one of the following functional types: 
    * `agent`: designates the workload as an AI agent. Workloads of this type must use the `agent-identity` type.
    * `mcp-server`: designates the workload as a user-managed MCP server. This type can use any supported identity type.
  * **Identity type** : specifies the kind of identity assigned to the workload. Once set, this property cannot be changed or unset. You assign your workload one of the following identity types: 
    * `agent-identity`: assigns a system-managed agent identity designed for agents. When you deploy with `agent-identity`, Agent Platform enables identity certificates by default. To opt out, update your service with the `--no-identity-certificate` flag or set the `run.googleapis.com/identity-certificate-enabled: "false"` annotation. Follow the guide to [authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets) for agents acting on their own authority or on behalf of end users. To understand the core concepts and security benefits of system-managed agent identities, learn more about [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview).
    * `service-account`: uses a standard Google Cloud service account.



### Configuration behavior

The behavior of functional and identity properties depends on the combination you choose:

Functional type | Identity type | Resulting behavior  
---|---|---  
`agent` | `agent-identity` | Workload is registered as an agent in the Agent Registry and assigned a system-managed agent identity.  
`agent` | Other or unspecified | Error. Workloads with `functional-type=agent` must use `identity-type=agent-identity`.  
`mcp-server` | `agent-identity`, `service-account`, or unspecified | Workload is registered as an MCP server (`/mcpServers`) in the Agent Registry. If unspecified, defaults to a service account identity.  
Unspecified | `service-account` | Workload runs as a standard Cloud Run service or job.  
  
## Configure features on services and jobs

You configure Agent Platform features on your Cloud Run services and jobs using the Google Cloud CLI.

### Services

  * To deploy an agent, specify `--functional-type=agent` and `--identity-type=agent-identity`:
        
        gcloud beta run deploy SERVICE_NAME \
            --image=IMAGE_URL \
            --functional-type=agent \
            --identity-type=agent-identity

Replace the following:

    * `SERVICE_NAME`: the name of your Cloud Run service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
  * To update an existing service to use Agent Identity:
        
        gcloud beta run services update SERVICE_NAME \
            --functional-type=agent \
            --identity-type=agent-identity \
            --no-traffic

**Important:** When you update an existing service from a service account to `agent-identity`, Cloud Run assigns a new principal that doesn't inherit permissions from your previous service account. To avoid connection disruptions, use [Policy Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview) to identify required roles and pre-assign them to the `principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/run/projects/PROJECT_NUMBER/locations/REGION/services/SERVICE_NAME` principal before updating, or update the service with `--no-traffic` to assign permissions before migrating traffic.

Replace the following:

    * `SERVICE_NAME`: the name of your Cloud Run service.
    * `ORGANIZATION_ID`: your Google Cloud organization ID.
    * `PROJECT_NUMBER`: your Google Cloud project number.
    * `REGION`: the region where your service is deployed.
  * To deploy a user-managed MCP server, specify `--functional-type=mcp-server`. You can optionally specify an identity type using `--identity-type`:
        
        gcloud beta run deploy SERVICE_NAME \
            --image=IMAGE_URL \
            --functional-type=mcp-server \
            --identity-type=IDENTITY_TYPE

Replace the following:

    * `SERVICE_NAME`: the name of your Cloud Run service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
    * `IDENTITY_TYPE`: Optional. The type of identity assigned to the workload. Specify `agent-identity` or `service-account`. Defaults to `service-account`.



### Jobs

**Note:** Only Cloud Run services can be exposed as MCP servers. Cloud Run jobs cannot be exposed as MCP servers and only support the `agent` functional type. 

  * To create an agent job, specify `--functional-type=agent` and `--identity-type=agent-identity`:
        
        gcloud beta run jobs create JOB_NAME \
          --image=IMAGE_URL \
          --functional-type=agent \
          --identity-type=agent-identity

Replace the following:

    * `JOB_NAME`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the container image.



## View assigned identities

You can view the assigned agent identity from the Google Cloud console or gcloud CLI.

### Services

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select **Services** from the Cloud Run navigation menu, and click your service.

  3. Click the **Revisions** tab and select a revision.

  4. Click the **Security** tab.




The **Identity** field displays the assigned agent identity.

###  gcloud 

To view the agent identity, describe the revision of your service:
    
    
    gcloud beta run revisions describe REVISION_NAME

Replace `REVISION_NAME` with the name of your service revision.

The assigned agent identity is displayed in the output.

### Jobs

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Select **Jobs** from the Cloud Run navigation menu, and click your job.

  3. Click the **Executions** tab and select an execution.

  4. View the execution details.




The **Identity** field displays the assigned agent identity.

###  gcloud 

To view the agent identity for a job execution, describe the execution:
    
    
    gcloud beta run jobs executions describe EXECUTION_NAME

Replace `EXECUTION_NAME` with the name of your job execution.

The assigned agent identity is displayed in the output.

## View an agent or MCP in Agent Registry

When you deploy a Cloud Run resource with `--functional-type=agent` or `--functional-type=mcp-server`, it's [automatically registered](https://docs.cloud.google.com/agent-registry/register-agents#automatic-registration) in your organization's Agent Registry.

  * [Agents](https://docs.cloud.google.com/run/docs/ai/authenticate-agents#view-in-registry) are registered under the agent catalog (`/agents`).
  * [MCP servers](https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers#view-in-registry) are registered under the MCP server catalog (`/mcpServers`).



To view your registered agents and tools in the registry, and to learn how to securely store and discover your agents and tools, explore [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).

## What's next

  * Learn how to [authenticate your agents](https://docs.cloud.google.com/run/docs/ai/authenticate-agents) to APIs and tools.
  * Learn how to [authenticate MCP servers](https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers) for secure connections.
  * Learn how to [host MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers).
  * Use the [Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk) to build and register custom agents in the registry.
  * To build and deploy agents that conform to the A2A specification, see [Deploy A2A agents to Cloud Run](https://docs.cloud.google.com/run/docs/deploy-a2a-agents).
  * See the [troubleshooting guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment) if you encounter issues with agent registration or identity assignment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
