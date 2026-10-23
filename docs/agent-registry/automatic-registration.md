---
url: https://docs.cloud.google.com/agent-registry/automatic-registration/
title: Use automatic registration for agents \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:15.536281+00:00
---

# Use automatic registration for agents  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/automatic-registration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Use automatic registration for agents Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you configure automatic registration for agents on supported Google Cloud runtimes so that developers and orchestrator agents can discover them without manually creating registry resources. Depending on the runtime, registration happens by default or through an opt-in deployment step, and the indexed metadata depends on the implementation protocol.

Automatic registration only discovers supported resources deployed within the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. To register remote agents deployed in other Google Cloud projects, see [Register an agent from another project](https://docs.cloud.google.com/agent-registry/manual-registration#cross-project). For remote agents hosted externally or on unsupported runtimes, see [Use manual registration for agents](https://docs.cloud.google.com/agent-registry/manual-registration).

## Automatically indexed metadata

The metadata and capabilities indexed for an agent during automatic registration depend on whether the agent implements the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/):

  * **Agents implementing the A2A protocol** : Agent Registry queries the agent's `/.well-known/agent-card.json` [Agent Card](https://docs.cloud.google.com/agent-registry/json-schemas#agent-card) to automatically extract its advertised [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) and capabilities in Agent Registry.
  * **Agents not implementing the A2A protocol** : Agent Registry registers the agent, but can't automatically capture metadata such as the endpoint URL where the agent is hosted, the agent identity, and A2A skills. These are agents that expose, for example, standard REST or gRPC endpoints. To associate capabilities with non-A2A agents, use [manual registration](https://docs.cloud.google.com/agent-registry/manual-registration) or [register skills](https://docs.cloud.google.com/agent-registry/register-skills).



## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



## Register agents from Agent Runtime

If you develop and deploy agents with [Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime), registration in Agent Registry is automatic.

The following example shows how to deploy an agent implementing the A2A protocol to Agent Runtime. For more information, see [Deploy an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent).
    
    
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

Built-in Google agents, such as [Google Workspace](https://developers.google.com/workspace/guides/get-started) and [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) agents, are automatically registered in Agent Registry. You don't need to perform any configuration or deployment steps. These agents are ingested and available for [discovery](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#discovery-types) within your registry.

## Register agents from GKE

To register agents deployed on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex), add the required Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to your deployment manifest. The following example shows a GKE manifest that defines a Kubernetes `Deployment` and a Kubernetes `Service` configured for automatic registration:
    
    
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
            image: gcr.io/PROJECT_ID/my-agent:1.0.0
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
    ---
    # Kubernetes Service for in-cluster network routing to the agent pod
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
    

Replace `PROJECT_ID` with your Google Cloud project ID.

To configure and apply the deployment manifest, do the following:

  1. In `metadata.labels` of your `Deployment` manifest, add the `registry.gke.io/functional-type: "AGENT"` label. This label identifies the deployment as an AI agent workload, which instructs the GKE cluster runtime controller to inspect the workload and register the agent with Agent Registry.

**Note:** GKE also supports the `apphub.cloud.google.com/functional-type: "AGENT"` annotation for backward compatibility. However, use the `registry.gke.io/functional-type: "AGENT"` label for your GKE deployments.
  2. In `metadata.annotations` of your `Deployment` manifest, enable automated discovery of the agent's [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) by providing the `a2a-protocol.org/agent-card` annotation. The GKE ingestion controller uses this annotation to query the A2A Agent Card.

  3. In `spec.template.metadata.annotations` of the Pod template, enable authenticated communication by configuring [Agent Identity](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity) with the `iam.gke.io/spiffe-identity-type: agent-identity` annotation.

  4. Apply the deployment manifest to your cluster. For more information, see [Deploy and orchestrate AI agents](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex).

When you apply the deployment, the GKE cluster runtime controller automatically inspects the workload container and queries the Agent Card endpoint declared in the annotation. It then syncs the agent's metadata and A2A skills directly into a read-only `Agent` discovery resource in Agent Registry.




## Register agents from Cloud Run

You can automatically register agents when you deploy them as Cloud Run services or jobs by specifying the [`--functional-type=agent`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy#--functional-type) and [`--identity-type=agent-identity`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy#--identity-type) flags. The `--functional-type=agent` flag identifies the Cloud Run service or job as an AI agent rather than a standard containerized workload, instructing Cloud Run to register the agent with Agent Registry. During registration, Cloud Run automatically adds the agent's name and the `AGENT` type to the registry.

Workloads configured with `--functional-type=agent` must specify the `--identity-type=agent-identity` flag. Deploying with any other identity type results in an error.

To configure automatic registration on a new or existing Cloud Run service or job, see [Configure Gemini Enterprise Agent Platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features#configure-features). To prepare, containerize, and deploy an A2A-compliant agent on Cloud Run, see [Deploy A2A agents to Cloud Run](https://docs.cloud.google.com/run/docs/deploy-a2a-agents).

## Verify registration

You can verify that Agent Registry successfully registered your agents by listing them:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), description, runtime, and location.

  4. Filter the list by the agent's location or its runtime resource:

     * To filter by location, click the **Location** menu, select the locations you want to filter, and click **Apply**.
     * To filter by runtime, click the **Runtime** menu, select the runtimes you want to filter, and click **Apply**.

The page displays a filtered list of the registered agents for your selected conditions.




###  gcloud 

You can filter the list by the agent's metadata. Make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli) for Agent Registry, and then run the [`gcloud agent-registry agents list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/list) command:
    
    
    gcloud agent-registry agents list \
        --project=PROJECT_ID \
        --location=REGION \
        --filter="FILTER_EXPRESSION"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `FILTER_EXPRESSION`: the filter expression for the agents that you want to filter. For example, to filter by display name, you can use `displayName='DISPLAY_NAME'`. To filter by the globally unique [agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) (URN), you can use `agentId='urn:agent:AGENT_URN'`.



Built-in Google agents use an [agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) (URN) format that depends on where the agent is deployed. For example, you can discover built-in Google Workspace agents by filtering your list for the `googleapis.com` publisher using `--filter="agentId:'urn:agent:googleapis.com:*'"`.

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

  * `REGION`: the registry region.
  * `DISPLAY_NAME`: the human-readable display name of the agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
