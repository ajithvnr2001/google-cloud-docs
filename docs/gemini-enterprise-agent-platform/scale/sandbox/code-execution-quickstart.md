---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-quickstart/
title: Code Execution quickstart \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:42.629257+00:00
---

# Code Execution quickstart  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Code Execution quickstart Stay organized with collections  Save and categorize content based on your preferences. 

This page demonstrates how to make direct API calls to Code Execution to run untrusted code in an isolated sandbox environment. Direct API calls are useful when you don't want the agent framework to orchestrate calls for you or if you'd like to integrate Code Execution with other agent frameworks.

In this quickstart, you perform the follow tasks:

  * Create an Agent Platform instance to access Code Execution
  * Create a Code Execution sandbox
  * (Optional) List and get sandboxes
  * Execute code in a sandbox
  * Execute more code using the same sandbox. Notice that the sandbox automatically maintains its state.
  * Clean up



For more information about using Code Execution with Agent Development Kit (ADK), see [Code Execution tool](https://google.github.io/adk-docs/tools/google-cloud/code-exec-agent-engine/).

## Before you begin

Set up your project and environment.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)


**Note:** To enable APIs, you need the `serviceusage.services.enable` permission. If you don't have this permission, ask your administrator to grant you the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) role.

### Get the required roles

To get the permissions that you need to use Vertex AI Agent Engine, ask your administrator to grant you the [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up your environment

This section assumes that you have [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup), or are using a runtime with a Python development environment (such as Colab).

### Install libraries

Install the Agent Platform SDK:
    
    
      pip install google-cloud-agentplatform>=2.0.1

### Authenticate

To authenticate:

### Local shell
    
    
    gcloud init
    gcloud auth application-default login
    

### Colab
    
    
    from google.colab import auth
    
    auth.authenticate_user()
    

## Create an Agent Platform instance

To use Code Execution, first create an Agent Platform instance. You don't need to deploy an agent to use Code Execution. Without deployment, creating an Agent Platform instance should take a few seconds.
    
    
    import agentplatform
    from agentplatform import types
    
    client = agentplatform.Client(project=PROJECT_ID, location=LOCATION)
    
    remote_agent = client.runtimes.create()
    remote_agent_name = remote_agent.api_resource.name
    

Replace the following:

  * PROJECT_ID: Your Google Cloud project ID.

  * LOCATION: The Google Cloud region for your Agent Platform instance. See [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).




## Create a sandbox

Create a sandbox for code execution.
    
    
    operation = client.sandboxes.create(
        spec={"code_execution_environment": {}},
        name=remote_agent_name,
        config=types.CreateRuntimeSandboxConfig(display_name=SANDBOX_DISPLAY_NAME)
    )
    
    sandbox_name = operation.response.name
    

Replace the following:

  * `SANDBOX_DISPLAY_NAME`: the human readable name of the code execution sandbox environment.



You can also configure the sandbox settings like coding language and machine config:
    
    
    operation = client.sandboxes.create(
       spec={
           "code_execution_environment": {
                "code_language": "LANGUAGE_JAVASCRIPT",
                "machine_config": "MACHINE_CONFIG_VCPU4_RAM4GIB"
            }
       },
       name='projects/PROJECT_ID/locations/LOCATION/reasoningEngines/INSTANCE_ID',
       config=types.CreateRuntimeSandboxConfig(
           display_name=sandbox_display_name, ttl="3600s"),
    )
    

Replace the following:

  * PROJECT_ID: Your Google Cloud project ID.

  * LOCATION: The Google Cloud region for your Agent Platform instance. See [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).

  * INSTANCE_ID: The ID for your Agent Platform instance.




Only `LANGUAGE_PYTHON` and `LANGUAGE_JAVASCRIPT` are supported. If `machine_config` is not specified, the default configuration is 2 vCPU and 1.5 GB of RAM. If you specify `MACHINE_CONFIG_VCPU4_RAM4GIB`, the sandbox has 4 vCPU and 4GB of RAM.

## (Optional) List and get sandboxes

List all the sandboxes associated with the specified Agent Engine instance:
    
    
    sandboxes = client.sandboxes.list(name=remote_agent_name)
    
    for sandbox in sandboxes:
        pprint.pprint(sandbox)
    

Here's the sample output:
    
    
    SandboxEnvironment(
      create_time=datetime.datetime(2025, 9, 7, 3, 42, 17, 93656, tzinfo=TzInfo(UTC)),
      display_name='test_sandbox',
      name=SANDBOX_NAME,
      spec=SandboxEnvironmentSpec(
        code_execution_environment=SandboxEnvironmentSpecCodeExecutionEnvironment()
      ),
      state=<State.STATE_RUNNING: 'STATE_RUNNING'>,
      update_time=datetime.datetime(2025, 9, 7, 3, 42, 17, 93656, tzinfo=TzInfo(UTC))
    )
    

To get an existing sandbox:
    
    
    sandbox = client.sandboxes.get(name=sandbox_name)
    
    pprint.pprint(sandbox)
    

Here's the sample output:
    
    
    SandboxEnvironment(
      create_time=datetime.datetime(2025, 9, 7, 3, 42, 17, 93656, tzinfo=TzInfo(UTC)),
      display_name='test_sandbox',
      name=SANDBOX_NAME,
      spec=SandboxEnvironmentSpec(
        code_execution_environment=SandboxEnvironmentSpecCodeExecutionEnvironment()
      ),
      state=<State.STATE_RUNNING: 'STATE_RUNNING'>,
      update_time=datetime.datetime(2025, 9, 7, 3, 42, 17, 93656, tzinfo=TzInfo(UTC))
    )
    

## Execute code in a sandbox

To execute code, call `execute_code`:
    
    
    my_code = """
    with open("input.txt", "r") as input:
       with open("output.txt", "w") as output:
           for line in input:
               print(line)
               output.write(line)
    """
    input_data = {
       "code": my_code,
       "files": [{
           "name": "input.txt",
           "content": b"Hello, world!"
       }]
    }
    
    
    response = client.sandboxes.execute_code(
       name = sandbox_name,
       input_data = input_data
    )
    

Here's the sample output:
    
    
    ExecuteSandboxEnvironmentResponse(
      outputs=[
        Chunk(
          data=b'{
            "msg_err":"",
            "msg_out":"",
          }',
          mime_type='application/json',
        ),
        chunk(
    data=b"hello world!",
            mime_type="text/plain"
            attributes={
              "file_name":"output.txt"
            }
        )
      ]
    )
    

Note the following:

  * `execute_code` resets the sandbox's time to live (TTL).
  * The output is in raw bytes.
  * Each request or response can contain up to 100MB of files.



## Execute more code in a sandbox

To demonstrate that the sandbox maintains its state, execute more code in the same sandbox:
    
    
    python_code = """
    with open("output2.txt", "w") as output:
        for line in lines:
            output.write(line + "World\n")
    """
    input_data = {"code": python_code}
    
    response = client.sandboxes.execute_code(
        name = sandbox_name,
        input_data = input_data
    )
    
    pprint.pprint(response)
    

Here's the sample output:
    
    
    ExecuteSandboxEnvironmentResponse(
      outputs=[
        Chunk(
          data=b'{
            "msg_err":"",
            "msg_out":"",
          }',
          mime_type='application/json',
        ),
        chunk(
          data=b"hello world!",
            mime_type="text/plain"
            attributes={
              "file_name":"output2.txt"
            }
        )
    
      ]
    )
    

The response includes a file that needs to be decoded. Here's an example of how to decode the output:
    
    
    import base64
    import json
    
    if response.outputs[0].mime_type=="application/json":
        json_output = json.loads(response.outputs[0].data.decode("utf-8"))
        output_file_content = json_output.get("output_files")[0].get("content")
        print(output_file_content.b64decode(output_file_content))
    

Here's the sample output:
    
    
    b'HelloWorld\n'
    

## Clean up

To clean up resources created by this quickstart, delete your sandbox and Agent Platform instance.
    
    
    client.sandboxes.delete(name=sandbox_name)
    remote_agent.delete()
    

## What's next

  * [Code Execution troubleshooting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/code-execution)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
