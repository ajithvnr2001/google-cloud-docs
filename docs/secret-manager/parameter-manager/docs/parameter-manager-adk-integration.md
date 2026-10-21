---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-manager-adk-integration/
title: Parameter Manager integration with Agent Development Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:42.236826+00:00
---

# Parameter Manager integration with Agent Development Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-manager-adk-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Parameter Manager integration with Agent Development Kit Stay organized with collections  Save and categorize content based on your preferences. 

[Agent Development Kit (ADK) agents](https://adk.dev/) often interact with services outside Google Cloud and require configuration parameters. To support these use cases, ADK provides the `ParameterManagerClient` module within the `google.adk.integrations.parameter_manager` package. This module provides a standard interface for agents to retrieve rendered parameter values from Parameter Manager at runtime.

## Benefits of Parameter Manager integration with ADK

You can use Parameter Manager as the single source of truth for agent instructions and tool configurations. Doing so has several strategic and security advantages.

  * Developer teams can focus on tools and runtimes, which allows domain experts to tune the agent behavior.
  * You can adjust decision logic or system instructions through a managed control plane without a full code redeployment.
  * You can secure secrets and respond to security threats through configuration changes.
  * You can maintain consistent behavior across large-scale deployments through centralized management.
  * The integration minimizes the scope for security attacks by eliminating plaintext secrets from environment variables and application code.
  * The agent references a parameter ID pointer instead of a raw secret value, which prevents credential exposure in the large language model (LLM) conversation history.
  * Agents get secrets from Secret Manager only when necessary. This limits credential exposure to the exact moment of use and prevents persistent unauthorized access.
  * Resolving a secret generates logs in both Parameter Manager and Secret Manager, which provides a clear audit trail for each session.



## Implementation strategies and use cases

When you configure Parameter Manager as the single source of truth for agent instructions and tool configurations, you can implement the following three core strategies:

  * Update agent instructions dynamically
  * Update feature flags and parameters
  * Provide input/output pairs to improve accuracy



### Update instructions dynamically

You can update agent behavior without redeploying application code. Use the `before_agent_callback` function to retrieve and inject system prompts at runtime. This strategy supports the following use cases:

  * Publish a parameter instantly to defend against new prompt-injection attacks.
  * Update a mandatory disclaimer resource (such as a GDPR statement) to apply it to all subsequent agent responses.
  * Update the agent tone automatically to include seasonal messages, such as holiday wishes in December.
  * Store two prompt versions (such as a concise prompt and a detailed prompt) and use a callback to assign them randomly to measure task success without code changes.



### Update feature flags and parameters

Most applications require parameters such as `max_results` or `api_endpoint`. You can store these configurations as a JSON payload in Parameter Manager and retrieve them by using the `ToolContext` variable within the `BaseTool#runAsync` function. Automated format validation prevents tool failures caused due to malformed configurations. This strategy lets you perform the following operational tasks:

  * Lower the query rates or increase retry sleep intervals if a connected external service experiences high latency or instability.
  * Switch between experimental and production API endpoints when you update the Parameter Manager resource version.



### Provide input/output pairs to improve accuracy

Few-shot examples are highly effective tools to increase agent accuracy. You can store the input and output pairs as YAML files in Parameter Manager, reference them using the `ToolContext {few_shot_examples}` variable in your prompt, and load them into the `session.state` variable through the `before_agent_callback` function. This approach improves agent performance over time without a code deployment. Vertex AI Agent Engine supports this pattern, which lets you deploy and scale your optimized few-shot configurations on Google Cloud without a code redeployment. For more information, see [Include few-shot examples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/few-shot-examples).

  * Add specific question and answer pairs (such as definitions of complex medical terms) to give the agent context.
  * Retrieve culturally relevant examples based on the user's detected language, such as `examples-fr` for French or `examples-jp` for Japanese.
  * Provide examples of complex formatting to prevent invalid argument errors.
  * Provide a sample Markdown table to guide the output format, which is more reliable than explicit instructions in the system prompt.



### Use cases

  * **Just-in-time tool authorization** : Static API keys in initialization code are insecure. With this integration, the ADK agent retrieves the Parameter Manager resource that resolves the Secret Manager reference at runtime. This practice ensures that the agent loads secrets into memory on demand.
  * **Secure multi-tenant workflows** : Passing raw user tokens from a frontend is a security risk for multi-tenant agents. To mitigate this risk, you can store Parameter Manager IDs mapping to users. Use the `before_agent_callback` function to detect the `user_id` variable, retrieve the user-specific Parameter Manager resource, and rehydrate the `session.state` variable with the resolved OAuth token. Automatic updates occur if a user rotates their secret in Secret Manager.
  * **Encrypted system tasks** : If a `LongRunningFunctionTool` function must poll a database, you can prevent the primary database password from entering the LLM conversation history. The ADK retrieves the secret from Parameter Manager, performs the background task, and uses `EventActions` function to update its state with a success or failure flag. The ADK agent then returns only a summary to the model.



### Strategy for multi-region deployment

You can maintain shared logic and tools across global deployments while using regional Parameter Manager overrides. If you construct regional JSON configurations, such as `config-us` for USD or `config-emea` for EUR, the session automatically detects the user location. The session then retrieves the correct parameter ID to apply the appropriate local currency and contact information.

## What's next

  * [Manage parameters for external services in ADK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/manage-parameters-for-external-services-in-adk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
