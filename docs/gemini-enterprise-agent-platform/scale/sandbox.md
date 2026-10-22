---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/
title: Sandboxes overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:45.422547+00:00
---

# Sandboxes overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Sandboxes overview Stay organized with collections  Save and categorize content based on your preferences. 

Many agent tasks involve executing untrusted code, running commands, using a web browser, or interacting with external environments in ways that could pose security risks. The Gemini Enterprise Agent Platform provides isolated **sandboxes** to handle these workloads securely.

Sandboxes provide secure, isolated execution environments that are spawned to perform specific tasks on behalf of an agent. By running these operations in a sandbox, you can protect your infrastructure and data from potentially malicious or erroneous actions performed by the agent. Sandboxes mitigate these risks by:

  * **Isolation** : Each sandbox is isolated from other sandboxes and the host system. Actions taken by one agent in a sandbox doesn't affect other agents or users sharing the same runtime resources.
  * **Security** : Operations within the sandbox are restricted, preventing unauthorized access to your resources. All sandbox environments use secure container sandboxing, providing a strong security boundary. Malicious code can't access sensitive data or credentials within the runtime.
  * **Safety** : If an agent executes a harmful command or infinite loop, the impact is contained within the sandbox. For example, poorly written or malicious code could consume all available CPU or memory.



## Sandbox compared to runtime

The agent runtime and a sandbox differ in their purpose and usage:

  * **Agent Runtime** : This is the environment where the agent's core logic, decision-making, and orchestration run. It is a trusted environment that executes your code and manages the agent's lifecycle.
  * **Sandbox** : This is an auxiliary environment spawned _by_ the agent or the platform to execute specific, potentially unsafe tasks. Sandboxes can be short-lived, session-based, or stateful for several days.



For example, if an agent needs to calculate a complex formula by generating and running a custom Python script, it should run that script in a code execution sandbox, not in its own runtime. Additionally, if the agent uses a skill and a shell script, it must run them in an environment provisioned specifically for that session, using the end user's access.

## TTL and Sandbox provisioning speeds

  * **TTL** : Sandbox TTLs vary, ranging from 7 days for a custom container image to 14 days for a code execution sandbox. This allows you to resume state on a sandbox environment several days later for long-horizon tasks and resumable shell environments.
  * **Provisioning** : Creating a new sandbox takes up to 2 minutes to provision resources from a cold start, but after they are provisioned, sandboxes usually spin up in seconds. You can view the underlying architecture in the following open source projects: [AX](https://agentexecutor.io/) and [Substrate](https://github.com/agent-substrate/substrate).



## Features

Sandboxes offer several features such as predefined sandboxes, custom containers, enterprise security controls, and lifecycle management:

  * **[Code execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview)** : Allows the agent to generate and run code in a secure environment. This is useful for complex mathematical calculations, data analysis, and other tasks that require computation.
  * **[Computer use](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use)** : Enables the agent to interact with a web browser to perform tasks such as filling out forms, searching the web, or navigating complex UI workflows.
  * **[Custom containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/custom-containers)** : You can "Bring Your Own Container" to customize the execution environment with specific libraries, tools, or configurations. Use this to give your agent a shell environment containing the commands and tools in your custom image.
  * **[VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/configure-vpc-sc)** : Configure security perimeters to protect sensitive data and prevent unauthorized egress from sandbox environments.
  * **[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/configure-cmek)** : Protect sandbox data at rest with encryption keys managed in Cloud Key Management Service (Cloud KMS).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
