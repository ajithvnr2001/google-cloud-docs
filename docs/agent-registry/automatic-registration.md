---
url: https://docs.cloud.google.com/agent-registry/automatic-registration/
title: Use automatic registration \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:22.898403+00:00
---

# Use automatic registration  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/automatic-registration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Use automatic registration Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry can register agents hosted on supported Google Cloud runtimes without requiring you to manually call the Agent Registry API. Depending on the runtime, this registration process happens automatically or requires an opt-in configuration step during deployment.

This document explains how to enable discovery for agents on supported runtimes. If you host an agent externally or on an unsupported runtime, see [Use manual registration](https://docs.cloud.google.com/agent-registry/manual-registration).

The metadata and capabilities indexed for an agent during registration depend on whether the agent implements the Agent2Agent (A2A) protocol. For more information, see [Register agents](https://docs.cloud.google.com/agent-registry/register-agents).

## Before you begin

Before you register agents, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup). You need [your project ID](https://support.google.com/googleapi/answer/7014113) to verify registration.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

## Register agents from Agent Runtime

If you develop and deploy agents with [Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime), registration in Agent Registry is automatic.

The [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/) is an open standard that lets agents declare their capabilities and identity. The following example shows how to deploy an [agent implementing the A2A protocol](https://docs.cloud.google.com/agent-registry/register-agents#automatic-registration) to Agent Runtime. For more information, see [Deploy an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent).
    
    
    # Create and deploy the agent
    # This action automatically registers the agent in Agent Registry
    remote_agent = client.agent_engines.create(
        agent=my_a2a_agent, # Your defined A2A object
        config={
            "display_name": "my-support-agent",
            "description": "An agent that handles support tickets.",
            "requirements": ["google-cloud-aiplatform[agent_engines,langchain]"],
        },
    )
    

As you update or delete your agent in Agent Runtime, Agent Registry automatically synchronizes those changes.

## Register built-in Google agents

Built-in Google agents, such as [Google Workspace](https://developers.google.com/workspace/guides/get-started) and [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) agents, are automatically registered in Agent Registry. You don't need to perform any configuration or deployment steps. These agents are ingested and available for [discovery](https://docs.cloud.google.com/agent-registry/concepts#discovery) within your registry.

## Register agents from GKE

You can register agents deployed on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex) by adding the `registry.gke.io/functional-type: "AGENT"` label to your deployments. This label identifies the deployment as an AI agent workload, which instructs the GKE cluster runtime controller to perform an in-cluster introspection scan and register the agent with Agent Registry.

**Note:** GKE also supports the `apphub.cloud.google.com/functional-type: "AGENT"` annotation for backward compatibility. However, we recommend using the `registry.gke.io/functional-type: "AGENT"` label for your GKE deployments. 

To enable automated discovery of the agent's skills, you must also provide the `a2a-protocol.org/agent-card` annotation. The GKE ingestion controller uses this annotation to query the A2A Agent Card.

To enable authenticated communication, also configure [Agent Identity](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity) by adding the `iam.gke.io/spiffe-identity-type: agent-identity` annotation to the Pod specification.

The following example shows a GKE agent deployment manifest using these configurations. For more information, see [Deploy and orchestrate AI agents](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex).
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-agent
      labels:
        # GKE takes this label and registers the agent to Agent Registry
        registry.gke.io/functional-type: "AGENT"
      annotations:
        # A2A protocol metadata annotation for automated Agent Card discovery
        a2a-protocol.org/agent-card: |
          card:
            endpoint: /.well-known/agent-card.json
            protocol: HTTP
            port: 8080
    spec:
      selector:
        matchLabels:
          app: my-agent
      template:
        metadata:
          labels:
            app: my-agent
          annotations:
            # Agent Identity annotation for identity and access management
            iam.gke.io/spiffe-identity-type: agent-identity
        spec:
          containers:
          - name: server
            image: gcr.io/my-project/my-agent:1.0.0
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: my-agent-service
      labels:
        app: my-agent
    spec:
      type: ClusterIP
      ports:
      - port: 8080
        targetPort: 8080
        protocol: TCP
        name: http
      selector:
        app: my-agent
    

When the deployment is applied, the GKE cluster runtime controller automatically introspects the workload container, queries the Agent Card endpoint declared in the annotation, and syncs the agent's metadata and A2A skills directly into the Agent Registry data model.

## Register agents from Cloud Run

You can register agents deployed to [Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features) by specifying the `--functional-type=agent` and `--identity-type=agent-identity` flags during deployment. The `--functional-type=agent` flag identifies the Cloud Run workload as an AI agent rather than a standard containerized application, instructing Cloud Run to register the agent with Agent Registry.

Workloads configured with `--functional-type=agent` must specify the `--identity-type=agent-identity` flag. Deploying with any other identity type results in an error.

You can deploy agents as Cloud Run services or jobs. To learn how to deploy an agent as a service or job in Cloud Run, see [Configure Agent Platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).

During registration, Cloud Run automatically adds the agent's name and type (`AGENT`) to the registry. For more information about deploying A2A agents to Cloud Run, see [Deploy A2A agents to Cloud Run](https://docs.cloud.google.com/run/docs/deploy-a2a-agents).

Automatic registration only discovers resources deployed within the same Google Cloud project. To register agents deployed across different projects, see [manual registration](https://docs.cloud.google.com/agent-registry/manual-registration#cross-project).

## Verify registration

You can verify that Agent Registry successfully registered your agents by listing them:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/concepts#agent-identifier), description, runtime, and location.

  4. Filter the list by the agent's location or its runtime resource:

     * To filter by location, click the **Location** menu, select the locations you want to filter, and click **Apply**.
     * To filter by runtime, click the **Runtime** menu, select the runtimes you want to filter, and click **Apply**.

The page displays a filtered list of the registered agents for your selected conditions.




###  gcloud 

You can filter the list by the agent's metadata. Make sure you have [set up your Google Cloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli) for Agent Registry, and then run:
    
    
    gcloud agent-registry agents list \
      --project=PROJECT_ID \
      --location=REGION \
      --filter="FILTER_EXPRESSION"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.
  * `FILTER_EXPRESSION`: The filter expression for the agents that you want to filter. For example, to filter by display name, you can use `displayName='DISPLAY_NAME'`. To filter by the globally unique [identifier](https://docs.cloud.google.com/agent-registry/concepts#agent-identifier) (URN), you can use `agentId='urn:agent:AGENT_URN'`.



Built-in Google agents use a URN format that depends on where the agent is deployed. For example, you can discover built-in Google Workspace agents by filtering your list for the `googleapis.com` publisher using `--filter="agentId:'urn:agent:googleapis.com:*'"`.

###  Terraform 

Reference your registered agent in other Terraform configurations by using the `google_agent_registry_agent` data source:
    
    
    data "google_agent_registry_agent" "my_agent" {
      location = "REGION"
      filter = "displayName=\"DISPLAY_NAME\""
    }
    
    output "agent_urn" {
      value = data.google_agent_registry_agent.my_agent.urn
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable display name of the agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
