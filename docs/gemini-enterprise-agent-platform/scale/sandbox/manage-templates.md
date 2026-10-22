---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/manage-templates/
title: Manage sandbox templates \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:06.366789+00:00
---

# Manage sandbox templates  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/manage-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Manage sandbox templates Stay organized with collections  Save and categorize content based on your preferences. 

Every sandbox is backed by a _sandbox environment template_ , which describes the container image to run. Sandbox templates serve as blueprints for [custom container sandboxes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/custom-containers). This page demonstrates how to manage the lifecycle of sandbox templates using the Agent Platform SDK. You can list existing templates, view their details, or delete them when they are no longer needed.

To modify a template's configuration (such as changing the container image), delete the existing template and create a new one with the updated configuration.

## Before you begin

To manage sandbox templates, you need the following roles on your project:

  * Agent Platform User (`roles/aiplatform.user`)



## Reuse templates across sandboxes

For Computer Use and shell sandboxes, if you don't specify a template, the default template (`DEFAULT_CONTAINER_CATEGORY_COMPUTER_USE` or `DEFAULT_CONTAINER_CATEGORY_SHELL_SANDBOX`) is created for the sandbox.

A new template is created during every `create()` call that doesn't name a template. Deleting the sandbox doesn't delete the template, so you need to delete the templates separately. If you create many sandboxes, we recommend re-using templates to conserve resources.

Create a template:
    
    
    from agentplatform._genai import types
    
    template_op = client.agent_engines.sandboxes.templates.create(
        name=instance_name,
        display_name="shell-sandbox-template",
        config=types.CreateSandboxEnvironmentTemplateConfig(
            default_container_environment=types.SandboxEnvironmentTemplateDefaultContainerEnvironment(
                default_container_category=types.DefaultContainerCategory.DEFAULT_CONTAINER_CATEGORY_SHELL_SANDBOX,
            ),
        ),
    )
    template = template_op.response.name
    

Associate each sandbox with the template by setting `sandbox_environment_template`:
    
    
    operation = client.sandboxes.create(
        name=instance_name,
        spec={"shell_environment": {}},
        config={
            "sandbox_environment_template": template,
            "wait_for_completion": True,
        },
    )
    

## List templates

To list all sandbox templates associated with an Agent Platform instance:
    
    
    import agentplatform
    
    client = agentplatform.Client(project='PROJECT_ID', location='LOCATION')
    instance_name = 'projects/PROJECT_ID/locations/LOCATION/reasoningEngines/INSTANCE_ID'
    
    templates_response = client.sandboxes.templates.list(name=instance_name)
    
    for template in templates_response.sandbox_environment_templates:
        print(template.name)
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The Google Cloud region of your Agent Platform instance. See [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).
  * `INSTANCE_ID`: The Agent Platform instance ID.



## View template details

To view the configuration of a specific sandbox template:
    
    
    template_name = 'projects/PROJECT_ID/locations/LOCATION/reasoningEngines/INSTANCE_ID/SandboxEnvironmentTemplate/TEMPLATE_ID'
    
    template = client.sandboxes.templates.get(name=template_name)
    print(template)
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The Google Cloud region of your Agent Platform instance. See [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).
  * `INSTANCE_ID`: The Agent Platform instance ID that contains your sandbox template.
  * `TEMPLATE_ID`: The sandbox template ID.



## View a sandbox's template

To view the sandbox template associated with a sandbox, run the following:
    
    
    print(sandbox.sandbox_environment_template)
    

## Delete a template

To delete a sandbox template:
    
    
    client.sandboxes.templates.delete(name=template_name)
    print("Template deleted.")
    

**Note:** Deactivating a template is done by deleting it. You cannot delete a template if a warm pool is actively using it (meaning the template is being created) or if sandboxes are being created from it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
