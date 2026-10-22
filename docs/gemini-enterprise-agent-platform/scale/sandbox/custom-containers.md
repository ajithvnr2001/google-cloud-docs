---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/custom-containers/
title: Custom container sandbox overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:44:46.268528+00:00
---

# Custom container sandbox overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/custom-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Custom container sandbox overview Stay organized with collections  Save and categorize content based on your preferences. 

The standard sandboxes provide a predefined set of libraries, which provide turnkey solutions for specific tasks like code execution and computer use. For agentic workloads that require specific dependencies, libraries, custom tools, or specialized data plane interfaces, you can provide your own container images (also known as bring your own container or BYOC). This feature lets you run custom workloads within the secure confines of a sandbox environment.

## Before you begin

Set up your project, image repository, and permissions.

### Set up your container image

  1. **Build a container image** : Create a Docker image that contains your custom environment. To ensure compatibility with Gemini Enterprise Agent Platform sandboxes, your custom image must meet the following requirements:

     * **OS** : Linux-based (for example, Debian or Ubuntu).
     * **Runner** : Must include a compatible runner or entry point that Gemini Enterprise Agent Platform can use to execute commands.
     * **Security** : Must not require root privileges or access to restricted system resources, as the image will run within a secure, isolated sandbox.
  2. **Add image to Artifact Registry** : Add your image to Google Cloud Artifact Registry where Agent Platform can access it. When you provision your sandbox, provide Artifact Registry image URI.




### Configure permissions

To allow the Agent Sandbox to pull your custom container image from Artifact Registry, grant the **[Artifact Registry Reader](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles)** (`roles/artifactregistry.reader`) role on the repository that contains the image to the Agent Sandbox service agent:

  * **Agent Sandbox service agent** : `service-PROJECT_NUMBER@gcp-sa-vertex-sandbox.iam.gserviceaccount.com`



Replace `PROJECT_NUMBER` with the project number of your project.

For more information about granting roles, see [Grant permissions to a service agent](https://docs.cloud.google.com/iam/docs/create-service-agents).

### Create an Agent Platform instance

If you don't have an Agent Platform instance, create one.
    
    
    import agentplatform
    client = agentplatform.Client(
        project='PROJECT_ID',
        location='LOCATION',
        http_options={
            "api_version": "v1beta1",
        }
    )
    remote_agent = client.runtimes.create()
    remote_agent_name = remote_agent.api_resource.name
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The Google Cloud region for your Agent Platform instance. See [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).



## Create a custom container sandbox

To create a custom container sandbox, you first create a sandbox template (`SandboxEnvironmentTemplate`). After you create a template, Agent Platform creates pre-warmed pools that are associated with the template to provide faster and more reliable startup times.

To create a template, define a `SandboxEnvironmentTemplate` resource, which specifies the configuration for your custom container:

  * **Container image** : The URI of a prebuilt custom image that is hosted in Artifact Registry.
  * **Ports** : Network ports to expose from the container.



### Create the template
    
    
    # Create a custom sandbox template
    templates_client = client.sandboxes.templates
    
    operation = templates_client.create(
        name=remote_agent_name,
        display_name="DISPLAY_NAME",
        config={
            "custom_container_environment": {
                "custom_container_spec": {
                    "image_uri": "IMAGE_LOCATION"
                },
                "resources": {
                    "requests": {
                        "cpu": "1",
                        "memory": "500Mi"
                    },
                    "limits": {
                        "cpu": "1",
                        "memory": "500Mi"
                    }
                },
                "ports": [
                    {
                        "port": PORT_NUMBER,
                        "protocol": "TCP"
                    }
                ]
            },
            "egress_control_config": {
                "internet_access": True
            }
        }
    )
    template_name = operation.response.name
    print(f"Template created: {template_name}")
    

### Create the sandbox

After you define your template, you can provision a new sandbox environment by referencing the template resource name.
    
    
    # Provision a sandbox referencing the template
    create_operation = client.sandboxes.create(
        name=remote_agent_name,
        config={
            "sandbox_environment_template": template_name,
            "display_name": "DISPLAY_NAME"
        }
    )
    sandbox = create_operation.response
    print(f"Sandbox environment provisioned: {sandbox.name}")
    

## What's next

  * Learn how to [manage your sandboxes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/manage-sandboxes).
  * Learn how to [manage sandbox templates](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/manage-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
