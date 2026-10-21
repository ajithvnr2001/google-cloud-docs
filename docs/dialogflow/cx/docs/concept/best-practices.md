---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices/
title: Service use best practices \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:51.703660+00:00
---

# Service use best practices  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Service use best practices Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides best practices for using the Dialogflow service. These guidelines are designed for greater efficiency and accuracy as well as optimal response times from the service.

You should also see the [general agent design](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design) guide for all agent types, and the [voice agent design](https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-agent-design) guide specifically for designing voice agents.

## Productionization

Before running your agent in production, be sure to implement the following best practices:

  * Use agent versions
  * Reuse session clients
  * Implement error handling with retries



## Enable audit logs

Enable Data Access [audit logs](https://docs.cloud.google.com/dialogflow/cx/docs/concept/audit-logging) for Dialogflow API in your project. Similar to the [Change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history) feature, audit logs can help you track design-time changes in the Dialogflow CX agents associated with the project.

## Agent versions

You should always use agent versions for your production traffic. See [Versions and environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) for details.

## Create agent backup

Keep an up-to-date [exported](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export) agent backup. This will allow you to quickly recover if you or your team members accidentally delete the agent or the project.

## Client reuse

You can improve the performance of your application by reusing `*Client` client library instances for the duration of your application's execution lifetime.

Most importantly, you can improve the performance of detect intent API calls by reusing a `SessionsClient` client library instance.

Go to the Session API reference

**Select a protocol and version for the Session reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions) |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions)  
RPC |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions) |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Sessions)  
C++ |  [SessionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionsClient.html) |  Not available   
C# |  [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) |  Not available   
Go |  [SessionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient) |  Not available   
Java |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionsClient)  
Node.js |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionsClient.html) |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.sessions.SessionsClient)  
Ruby |  Not available  |  Not available   
  
Close

For more information on this, see the [Best Practices with Client Libraries guide](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices#reuse_client_objects_and_sessions).

## API error retries

When calling API methods, you may receive error responses. There are some errors which should be retried, because they are often due to transient issues. There are two types of errors:

  * [Cloud API errors](https://docs.cloud.google.com/apis/design/errors).
  * Errors sent from your [webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors). 



In addition, you should implement an [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) for retries. This allows your system to find an acceptable rate while the API service is under heavy load.

### Cloud API errors

If you are using a Google supplied [client library](https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/overview), Cloud API error retries with exponential backoff are implemented for you.

If you have implemented your own client library using REST or gRPC, you must implement retries for your client. For information on the errors that you should or should not retry, see [API Improvement Proposals: Automatic retry configuration](https://google.aip.dev/194).

### Webhook errors

If your API call triggers a webhook call, your webhook may return an error. Even if you are using a Google supplied client library, webhook errors will not be retried automatically. Your code should retry `503 Service Unavailable` errors received from your webhook. See the [webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors) documentation for information on the types of webhook errors and how to check for them.

## Load testing

It is a best practice to execute load testing for your system before you release code to production. Consider these points before implementing your load tests:

Summary | Details  
---|---  
Ramp up load. | Your load test must ramp up the load applied to the Dialogflow service. The service is not designed to handle abrupt bursts of load, which are rarely experienced with real traffic. It takes time for the service to adjust to load demands, so ramp up the request rate slowly, until your test achieves the desired load.  
API calls are charged. | You will be charged for API calls during a test, and the calls will be limited by project quota.  
Use test doubles. | You may not need to call the API during your load test. If the purpose of your load test is to determine how _your system_ handles load, it is often best to use a [test double](https://en.wikipedia.org/wiki/Test_double) in place of actual calls to the API. Your test double can simulate the behavior of the API under load.  
Use retries. | Your load test must perform retries with a backoff.  
  
## Calling Dialogflow securely from an end-user device

You should never store your private keys used to access the Dialogflow API on an end-user device. This applies to storing keys on the device directly and to hard coding keys in applications. When your client application needs to call the Dialogflow API, it should send requests to a developer-owned proxy service on a secure platform. The proxy service can make the actual, authenticated Dialogflow calls.

For example, you should not create a mobile application that calls Dialogflow directly. Doing so would require you to store private keys on an end-user device. Your mobile application should instead pass requests through a secure proxy service.

**Note:** Some Dialogflow integrations, like Dialogflow Messenger, provide both client code and a proxy service, similar to the description above. The proxy service only responds to requests when the integration is enabled. To improve utility of these integrations, the proxy service may not require authentication. The proxy service API is limited to a small subset of Dialogflow API methods that are required for the integration. In addition, the proxy service never provides Google Cloud or Dialogflow administrative API access without requiring authentication. This limited proxy API reduces the vulnerability for abuse.

## Performance

This section outlines performance information for various operations within Dialogflow. Understanding latency is important for designing responsive agents and setting realistic performance expectations, although these values are not part of the Dialogflow SLA.

When building monitoring and alerting tools, note that Large Language Models (LLMs) and speech processing are typically handled using streaming methods. Responses are sent to the client as soon as possible, often much earlier than the total duration of the method call. For more information, see the [Best practices with large language models (LLMs)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompt-best-practices).

### Performance per operation

The following table provides information about the typical performance of Dialogflow operations:

Action | Notes  
---|---  
Flow actions: state handlers | Fastest operation  
Flows: intent detection (text) | Fastest operation  
Flows: parameter detection (text) | Fast operation  
Speech recognition (streaming) | Data is processed and responses are returned as soon as possible. The total execution time is primarily determined by the length of the input audio. Measuring latency using the total execution time is not recommended.  
Speech synthesis (streaming) | The total execution time is primarily determined by the length of the output audio. Data is processed and responses are returned as quickly as possible.  
Data stores: generative AI disabled | Actual time depends on the size of the data store.  
Data stores: generative AI enabled | Performance depends on the size of the data store, the language model in use, and the length of the prompt output and input, in that order.  
Generative fallback | Performance depends on the language in use and the prompt output and input length, in that order.  
Generators | Performance depends on the language model in use, the complexity of the prompt input and output length, and the number of generators in the turn. Multiple generators in a single turn result in multiple calls to a language model.  
Playbooks execution | Performance depends on the complexity of the playbook, the number of prompts, and the execution time of any tools called. The length of the prompt output and input impacts this performance. Multiple language model prompts may be executed serially, adding up to the total call time.  
Playbooks: tools | Performance depends on the underlying execution of the tool.  
Webhook calls | Performance is directly determined by the execution time of your code in the webhook.  
Import / Export agent | Performance depends on the size of the agent.  
Agent training | Performance depends on the number of flows, intents, and training phrases. Training large agents can take tens of minutes.  
Environment creation | Creating an environment involves training the agent, so the total time will depend on the size and complexity of the agent.  
  
**Key Notes:**

  * **Streaming:** For streaming calls (speech recognition and synthesis), data is processed as it arrives, and responses are returned as soon as possible. This means the initial response is typically much faster than the total time of the call.
  * **Playbooks:** An LLM prompt is constructed based on the playbook instructions, the conversation context and the tool input. Multiple LLM prompts can be executed in a single playbook call. This is why the playbook execution is variable, depending on the amount of prompts issued and the complexity of the calls.



### Important Latency Considerations

  * **No Latency Guarantees:** Dialogflow SLAs do not consider latency, even under Provisioned Throughput.
  * **LLM Latency:** Be aware that LLM processing can introduce significant latency. Factor this into your agent design and user expectations.
  * **Monitoring and Alerting:** When setting up monitoring and alerting, account for the streamed nature of responses from LLMs and speech services. Don't assume full response time is equal to time to first response.



[ Previous arrow_back  Call companion  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion)

[ Next General agent design best practices  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
