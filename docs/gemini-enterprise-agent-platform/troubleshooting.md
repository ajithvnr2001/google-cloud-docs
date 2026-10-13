---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/
title: Troubleshoot Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:51.430426+00:00
---

# Troubleshoot Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Troubleshoot Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

This page is the starting point for troubleshooting Gemini Enterprise Agent Platform. Use it to diagnose an error, look up a specific error, find the guide for your task, or get support.

## Diagnose an error

Before you look for a specific fix, collect the following information:

### Read the error

Note the status code, such as `400` or `429`, and the exact message text. You can look up both in the error catalog.

You can also identify the specific failure from a machine-readable reason, documentation link, or prefiltered log view if those are present in the error message.

### Find the logs

To search and filter agent error logs, [use the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), set **Resource type** to **Vertex AI Reasoning Engine** , and select the corresponding **Resource container** value (your project number) and **Reasoning engine ID** value.

### Check quotas and service health

Errors that appear intermittently, or that started without a change on your side, are often caused by quota or by an ongoing incident:

  * Compare your usage against [Quotas and system limits](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-quotas).
  * Check [Google Cloud Service Health](https://status.cloud.google.com/) for an ongoing incident in your region.



## Error catalog

Find the error you received in the following table. If your error isn't listed, use the troubleshooting guides for the task you were trying to complete.

Status code or message | Resolution  
---|---  
`ImportError: cannot import name 'reasoning_engines'`, `ImportError: cannot import name 'agent_engines'` | [Outdated version of the Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/runtime-setup#outdated-vertex-sdk-errors)  
`401` `Context-Aware Access requirements are not met`, `401` `Request had invalid authentication credentials` | [401 authorization errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/runtime-setup#401-errors)  
`ValueError: Cannot get the Candidate text` | [Content generation errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-creation#content-generation-errors)  
`failed to start and cannot serve traffic`, on your first custom container (BYOC) deployment in a region | [BYOC first-time creation error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-creation#byoc-first-creation-error)  
`failed to start and cannot serve traffic` or `Request is prohibited by organization's policy`, inside a VPC Service Controls perimeter | [VPC-SC violation errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#vpc-sc-violation-errors)  
`429`, `RESOURCE_EXHAUSTED` | [Resource exhausted or rate limit errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#error-429)  
`429`, `RESOURCE_EXHAUSTED`, `at capacity` | [Region temporarily at capacity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#region-capacity)  
`429`, `RESOURCE_EXHAUSTED`, `max_instances` | [Maximum instances exceed regional limit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#max-instances-limit)  
`500` internal server error from a prebuilt template | [Prebuilt template errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#prebuilt-template-errors)  
`cloudpickle` or `pydantic` version conflicts when serializing your agent | [Serialization errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#serialization-errors)  
`NotFound: 404 Can not copy from "gs://..."` | [Cloud Storage bucket subdirectory isn't created](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#storage-bucket-subdirectory-errors)  
`iam.serviceAccounts.actAs` denied, metadata server unavailable | [Custom service account errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#custom-service-account-errors)  
`400`, `INVALID_ARGUMENT`, `REASONING_ENGINE_SECRET_ACCESS_DENIED`, `referenced by spec.deployment_spec.secret_env` | [Secret Manager access errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment#secret-access-errors)  
`InvalidArgument: 400 Provided filter is not valid` | [Error when filtering the list of agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/managing-deployed-agents#filter-agents-errors)  
`google.api_core.exceptions.Unknown: None`, `Failed to convert project number to project ID`, during startup | [Errors during Agent Runtime startup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway#bootstrap-errors)  
`403 Forbidden` on an outbound request | [403 Forbidden errors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway#confirm-egress-error)  
Certificate verification failures reaching a self-signed or private CA destination  | [Self-signed or private CA destinations fail to connect](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway#self-signed-ca-fail)  
TLS handshake failures from a custom container (BYOC) agent | [Agent deployed with custom container (BYOC) fails to connect](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway#byoc-ca-fail)  
Sandbox creation failures | [Sandbox creation issues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/code-execution#sandbox-creation-issues)  
Code execution times out, file I/O failures in a sandbox | [Code execution issues](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/code-execution#code-execution-issues)  
`RuntimeError: Failed to generate memory`, or no memories returned after a session | [No memories were generated](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/memory-bank#no-memories-generated)  
**Note:** If your error isn't listed in the table, use the troubleshooting guides, and report the error through Get support.

## Troubleshooting guides

If you don't have a specific error message, or your error isn't in the error catalog, see the following table for the corresponding guide for your task:

Task | Guide  
---|---  
Installing the Agent Platform SDK and setting up your environment | [Agent Runtime environment setup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/runtime-setup)  
Creating an agent | [Create an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-creation)  
Deploying an agent to Agent Runtime | [Agent deployment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-deployment)  
Calling an external service from an agent | [Agent Gateway connectivity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway)  
Listing, updating, or deleting a deployed agent | [Manage deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/managing-deployed-agents)  
Running code in a sandbox | [Code Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/code-execution)  
Generating or retrieving memories | [Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/memory-bank)  
Serving a model or hitting a model quota | [Troubleshooting machine learning services](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/troubleshooting)  
  
## Get support

If the guides on this page don't resolve your issue, see [Getting help for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-support) for support packages, community forums, and bug reporting. For billing questions, see [Billing questions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/billing-questions).

If you [file a bug](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-support#file_bugs_or_feature_requests), provide the following information:

  * Status code
  * Error message
  * (Optional) Feedback if the error message is wrong, misleading, or not actionable.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
