---
url: https://docs.cloud.google.com/pubsub/docs/smts/ai-inference-smt/
title: AI Inference SMT \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:11.501790+00:00
---

# AI Inference SMT  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/ai-inference-smt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  AI Inference SMT Stay organized with collections  Save and categorize content based on your preferences. 

The AI Inference Single Method Transform (SMT) lets you get inferences on Pub/Sub messages from [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/overview) models. You can use your own custom models deployed on Agent Platform endpoints, or use any of the Google and partner models available through Agent Platform. The model's inferences are added to each message, making them available for downstream processing along with the original message data.

Use cases for the AI Inference SMT include the following:

  * Real-time enrichment: Add context, classifications, predictions, sentiments, or embeddings to event data as it flows through Pub/Sub.

  * Simplified AI pipelines: Eliminate the need for intermediary services to get inferences from AI models. Pub/Sub handles calling the AI model and enriching the message with the inference.

  * Reduced latency for AI pipelines: Remove extra network hops in your architecture to achieve lower end-to-end latency.

  * Enhanced flow control: To avoid overloading model endpoints, Pub/Sub optimizes the rate of requests to the AI model. For more information, see Message flow in this document.




The AI Inference SMT supports the following types of model:

  * **Self-deployed models**. Open, partner, and custom models deployed to a shared or dedicated public Agent Platform endpoint.

  * **Model-as-a-Service (MaaS) models**. Models offered as a service through the [Model Garden](https://cloud.google.com/model-garden), such as Gemini and Claude, that don't require you to manage the deployment. For a list of MaaS models that are compatible with the AI Inference SMT, see Compatible MaaS models.




## Required roles and permissions

To get the permissions that you need to create a topic or subscription with SMTs, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a topic or subscription with SMTs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a topic or subscription with SMTs:

  * Create a topic: `pubsub.topics.create` on the project 
  * Create a subscription: `pubsub.subscriptions.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Service account permissions

The AI Inference SMT uses an IAM service account to call the Agent Platform endpoint. By default, it uses the **Cloud Pub/Sub Service Agent** account (`service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`). You can also provide your own service account.

The service account needs the following permissions on the Google Cloud project that contains the Agent Platform endpoint:

  * `aiplatform.endpoints.get`
  * `aiplatform.endpoints.predict`



To give these permissions, grant the [Agent Platform User](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) role to the service account (whether using the **Cloud Pub/Sub Service Agent** service account or a custom service account).

## Message processing

This section describes how the AI Inference SMT processes Pub/Sub messages.

### Input

The Pub/Sub message data must be a request to send to the AI model, as a JSON string. You can also specify additional model parameters to send with each request. The SMT merges these parameters with the message data and sends the merged JSON to the model endpoint.

For example, if you have:

  * **Input message data:** `{"messages": [{"role": "user", "content": "Explain photosynthesis"}]}`
  * **SMT Parameters:** `{"temperature": 0.2}`



The resulting payload sent to the model is:
    
    
    {
      "messages": [
        {
          "role": "user",
          "content": "Explain photosynthesis"
        }
      ],
      "temperature": 0.2
    }
    

If a parameter specified in the SMT configuration has the same name as a field in the message data, the value in the message data takes precedence.

The following table shows which API the SMT calls to get the inference, based on the type of model.

Model deployment | Model type | API  
---|---|---  
Self-deployed | All |  [ `rawPredict`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/rawPredict)  
Model-as-a-Service (MaaS) |  Gemini foundational model Example: `gemini-3.0-pro` |  [ `Chat Completions API`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/examples)  
Other Gemini models Example: `gemini-embeddings` |  [ `rawPredict`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/rawPredict)  
Anthropic, Mistral AI, or AI21 |  [ `rawPredict`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/rawPredict)  
All other MaaS models |  [ `Chat Completions API`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/examples)  
  
To format the message data and model parameters correctly, consult the documentation for your model. For example, for Gemini foundational models, see [Chat Completions API examples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/examples).

If your publisher application can't format messages in the specific JSON structure required by the model (such as the Chat Completions API format), you can chain a [JavaScript UDF](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview) SMT _before_ the AI Inference SMT to pre-process and format the request payload. For an example, see Pre-process payloads with a JavaScript UDF.

### Output

If the call to the model endpoint succeeds, the SMT enriches the original Pub/Sub message with the model response. The enriched message is a JSON string like the following, where `ORIGINAL_MESSAGE` is the original message data and `INFERENCE_RESULT` is the response from the model:
    
    
    {
      "original_message": { ORIGINAL_MESSAGE },
      "model_output": { INFERENCE_RESULT }
    }
    

## Message flow

**Topic SMTs:** When you define an AI Inference SMT on a topic, Pub/Sub handles incoming messages as follows:

  1. A publisher application sends a message to a Pub/Sub topic.

  2. The message is sent to the configured model endpoint for inference. The enriched message, containing the original data and the model's inference, is written to Pub/Sub's internal storage.

  3. Pub/Sub delivers the enriched message to all attached subscriptions.




**Subscription SMTs:** When you define an AI Inference SMT on a subscription, Pub/Sub handles incoming messages as follows:

  1. A publisher application sends a message to a Pub/Sub topic.

  2. Pub/Sub delivers the message to the subscription.

  3. The message is sent to the configured model endpoint for inference.

  4. The subscription sends the enriched message to the subscriber application.

  5. Pub/Sub optimizes the rate of requests to the AI model to maximize throughput, based on your deployment's latency and quota. Note: This capability isn't supported when using the [unary pull API](https://docs.cloud.google.com/pubsub/docs/pull#pull-api).




You can chain an AI Inference SMT with one or more [JavaScript UDF](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview) SMTs. Use this pattern to pre-process a message to fit your model's expected input format, or post-process the model's output before it is delivered to subscribers.

**Best Practice:** We strongly recommend using **Subscription SMTs** rather than Topic SMTs for AI Inference. If the AI model endpoint is throttled, experiences latency spikes, or becomes unavailable, the potential impact on your pipeline is greater with a topic SMT:

  * With a topic SMT, the publish request fails, directly impacting the availability of your publisher application.

  * With a Subscription SMT, Pub/Sub retries the delivery, including executing the SMT, according to the subscription's retry policy. You can also configure a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics) to handle persistent failures without affecting ingestion availability.




## Create an AI Inference SMT

SMTs can be configured on Pub/Sub topics or subscriptions.

  * Topic SMTs are executed before Pub/Sub stores the message, and the results are available to all subscribers.
  * Subscription SMTs are executed before the message is delivered, and the results are only available for that subscription.




### Console

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Create either a topic or a subscription.

     * To create a topic, click **Create topic**. The **Create topic** page opens.

     * To create a subscription:

       1. Click the name of the topic where you want the subscription.

       2. Click **Create subscription**. The **Add subscription to topic** page opens.

  3. Under **Transforms** , click **Add a transform**.

  4. For **Transform type** , select **AI Inference**.

  5. For **Endpoint** , enter the full resource name of your model endpoint:

     * Self-deployed model: `projects/PROJECT/locations/LOCATION/endpoints/ENDPOINT`
     * Model Garden model: `projects/PROJECT/locations/LOCATION/publishers/PUBLISHER/models/MODEL_NAME`
  6. Optional. Select a **Service account** to use when calling the Agent Platform endpoint. For more information, see Service account permissions.

  7. Optional. In the **Parameters** field, enter model parameters as a JSON object. The SMT merges these parameters with each message before calling the model. Example:
         
         {
           "temperature": 0.5,
           "max_tokens": 1000
         }
         

  8. To create the topic or subscription, click **Create**.




###  gcloud 

#### Create a definition file

Create a YAML or JSON file that defines the Inference AI.

###  YAML 
    
    
    - aiInference:
        endpoint: "ENDPOINT_RESOURCE"
        unstructuredInference: {
            parameters:
              MODEL_PARAMETERS
        }
        service_account_email: SERVICE_ACCOUNT
    

###  JSON 
    
    
    {
      "aiInference": {
        "endpoint": "ENDPOINT_RESOURCE",
        "unstructuredInference": {
            "parameters": {
              MODEL_PARAMETERS
            }
        }
        "service_account_email": SERVICE_ACCOUNT
      }
    }
    

Replace the following:

  * ENDPOINT_RESOURCE: The full resource name of the model endpoint. Use the following format:

    * Self-deployed model: `projects/PROJECT/locations/LOCATION/endpoints/ENDPOINT`
    * Model Garden model: `projects/PROJECT/locations/LOCATION/publishers/PUBLISHER/models/MODEL_NAME`
  * MODEL_PARAMETERS: Optional. Model parameters, specified as a JSON object. The SMT merges these parameters with each message before calling the model. Example:
        
        {
          "temperature": 0.5,
          "max_tokens": 1000
        }
        

  * SERVICE_ACCOUNT: Optional. A service account email to use when calling the endpoint. For more information, see Service account permissions.




#### Create a topic or subscription

To create a topic, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command.
    
    
    gcloud pubsub topics create TOPIC_ID \
      --message-transforms-file=TRANSFORMS_FILE
    

Replace the following:

  * TOPIC_ID: The ID or name of the topic you want to create.
  * TRANSFORMS_FILE: The path to the definition file.



To create a subscription, run the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command.
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION_ID \
      --topic=projects/PROJECT_ID/topics/TOPIC_ID \
      --message-transforms-file=TRANSFORMS_FILE
    

Replace the following:

  * SUBSCRIPTION_ID: The ID or name of the subscription to create.

  * PROJECT_ID: The ID of the project that contains the topic.

  * TOPIC_ID: The ID of the topic to subscribe to.

  * TRANSFORMS_FILE: The path to the definition file.




### Validate and test

Optionally, you can validate and test the configured SMT, before you create the topic or subscription. For more information, see the following documents:

  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)
  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)

**Note:** If you test the SMT, Pub/Sub calls your Agent Platform model to perform the test. You are billed for the Agent Platform usage.

## Examples

### Use the AI Inference SMT

The following example shows how to create a subscription with an AI Inference SMT and then use it to send a prompt to Gemini.

###  gcloud 

  1. Using a text editor, create a file named `ai-smt.yaml` and paste in the following text:
         
         - aiInference:
             endpoint: projects/PROJECT_ID/locations/LOCATION/publishers/google/models/gemini-3.8-flash
             unstructuredInference: {
                 parameters: {
                     "max_tokens": 25000
                 }
             }
         

Replace the following:

     * PROJECT_ID: The ID of your Google Cloud project.
     * LOCATION: The location of the endpoint to call. Example: `us-central1`.
  2. Create a new Pub/Sub topic.
         
         gcloud pubsub topics create TOPIC_ID
         

Replace TOPIC_ID with the name of the topic to create. Example: `topic-1`.

  3. Create a subscription that has an AI Inference SMT.
         
         gcloud pubsub subscriptions create TOPIC_ID-sub \
           --ack-deadline=600 \
           --topic TOPIC_ID \
           --message-transforms-file ai-smt.yaml
         

  4. Publish a message to the topic. The message contains a prompt that is formatted for the [Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/examples).
         
         gcloud pubsub topics publish TOPIC_ID --message=$'{
           "model":"google/gemini-3.8-flash","messages":[{
             "role": "user",
             "content": "Explain how AI works in a few words"
             }]
           }'
         

  5. Receive a message from the subscription.
         
         gcloud pubsub subscriptions pull TOPIC_ID-sub
         

If the call to Agent Platform succeeds, the message is enriched with the output from the prompt.




### Pre-process payloads with a JavaScript UDF

If your publisher application emits raw text, logs, or event payloads rather than the structured JSON required by AI models (such as the OpenAI-compatible Chat Completions format), you can chain a [JavaScript UDF](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview) SMT _before_ the AI Inference SMT. The UDF acts as a translation layer, transforming the raw message into the format the model expects.

The following JavaScript UDF example shows how to pre-process a message containing a text prompt into a Chat Completions API request compatible with Gemini 3.8 Flash:
    
    
    /**
     * Pre-processes a message containing a text prompt into a
     * Chat Completions API request compatible with Gemini 3.8 Flash.
     */
    function prepareGeminiRequest(message, metadata) {
      // Assuming the incoming message data is a raw text prompt
      const promptText = message.data;
    
      const chatRequest = {
        "model": "google/gemini-3.8-flash",
        "messages": [
          {
            "role": "user",
            "content": promptText
          }
        ]
      };
    
      // Replace the message data with the stringified JSON request
      message.data = JSON.stringify(chatRequest);
      return message;
    }
    

You can also chain a post-processing JavaScript UDF after the AI Inference SMT to extract specific fields from the model's response before delivering it to subscribers.

## Compatible MaaS models

**Note:** We recommend migrating to the newest available models when possible, especially for Gemini models, because model support and availability are subject to change. For migration guidance, see [Migrate to new models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate).

The following table lists the Model-as-a-Service (MaaS) models that Google has tested with the AI Inference SMT and are known to be compatible. This list is subject to change, as models become deprecated or new MaaS models are added.

Model| API called  
---|---  
`google/gemini-3.8-flash` | Chat Completions API  
`google/gemini-3.7-flash` | Chat Completions API  
`google/gemini-3.6-flash` | Chat Completions API  
`google/gemini-3.5-flash` | Chat Completions API  
`google/gemini-3.5-flash-lite` | Chat Completions API  
`google/gemini-3.1-flash-lite` | Chat Completions API  
`google/gemini-3.1-pro-preview` | Chat Completions API  
`google/gemini-3-flash-preview` | Chat Completions API  
`google/gemini-3.1-flash-image` | Chat Completions API  
`google/gemini-3-pro-image` | Chat Completions API  
`google/gemini-2.5-flash-image` | Chat Completions API  
`google/gemini-2.5-pro` | Chat Completions API  
`google/gemini-2.5-flash-lite` | Chat Completions API  
`google/gemini-2.5-flash` | Chat Completions API  
`google/gemini-2.0-flash-lite-001` | Chat Completions API  
`google/gemini-2.0-flash-001` | Chat Completions API  
`meta/llama-4-maverick-17b-128e-instruct-maas` | Chat Completions API  
`meta/llama-4-scout-17b-16e-instruct-maas` | Chat Completions API  
`meta/llama-3.3-70b-instruct-maas` | Chat Completions API  
`deepseek-ai/deepseek-r1-0528-maas` | Chat Completions API  
`deepseek-ai/deepseek-v3.1-maas` | Chat Completions API  
`qwen/qwen3-235b-a22b-instruct-2507-maas` | Chat Completions API  
`qwen/qwen3-coder-480b-a35b-instruct-maas` | Chat Completions API  
`openai/gpt-oss-20b-maas` | Chat Completions API  
`openai/gpt-oss-120b-maas` | Chat Completions API  
`google/text-multilingual-embedding-002` | `rawPredict`  
`google/text-embedding-005` | `rawPredict`  
`google/text-embedding-large-exp-03-07` | `rawPredict`  
`google/gemini-embedding-001` | `rawPredict`  
`google/multimodalembedding` | `rawPredict`  
`anthropic/claude-sonnet-4-6` | `rawPredict`  
`anthropic/claude-sonnet-4-5` | `rawPredict`  
`anthropic/claude-opus-4-6` | `rawPredict`  
`anthropic/claude-opus-4-5` | `rawPredict`  
`anthropic/claude-haiku-4-5` | `rawPredict`  
`mistralai/mistral-ocr-2505` | `rawPredict`  
`mistralai/mistral-small-2503` | `rawPredict`  
`mistralai/mistral-medium-3` | `rawPredict`  
`mistralai/codestral-2` | `rawPredict`  
  
## Limitations

  * Only one AI Inference SMT is allowed per topic or subscription.

  * Private endpoints are not supported. Self-deployed models must be hosted on public Agent Platform endpoints.

  * The [global endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#global-endpoint) is only supported for Gemini foundation models. For other models, you must use a regional endpoint.

  * Pub/Sub does not validate the input message data. You are responsible for ensuring the data format is correct.

  * The transform sends one inference request per Pub/Sub message. Client-side batching is not performed.

  * Asynchronous batch inferences are not supported.

  * The inference must not take longer than 60 seconds. If it exceeds 60 seconds, the delivery attempt times out and Pub/Sub retries, up to the configured [message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-message-retention) and [retry policy settings](https://docs.cloud.google.com/pubsub/docs/subscription-retry-policy). If the attempt times out, the message is forwarded to the [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics), if one is configured.




### Unsupported models

The AI Inference SMT doesn't support the following MaaS models. Many of these models have self-deployed versions available that you can use instead.

  * `deepseek-ai/deepseek-ocr-maas`
  * `deepseek-ai/deepseek-v3.2-maas`
  * `google/gemini-embedding-2-preview`
  * `google/lyria-002`
  * `google/lyria-3-clip-preview`
  * `google/lyria-3-pro-preview`
  * `google/veo-3.1-fast-generate-001`
  * `google/veo-3.1-generate-001`
  * `intfloat/multilingual-e5-large-instruct-maas`
  * `intfloat/multilingual-e5-small-instruct-maas`
  * `minimaxai/minimax-m2-maas`
  * `moonshotai/kimi-k2-thinking-maas`
  * `qwen/qwen3-next-80b-a3b-instruct-maas`
  * `qwen/qwen3-next-80b-a3b-thinking-maas`
  * `zai-org/glm-4.7-maas`
  * `zai-org/glm-5-maas`



## Regional constraints

The following constraints apply to AI Inference SMTs based on the region of the Agent Platform endpoint.

  * If an AI Inference SMT is defined on a topic, then the endpoint region must be within the regions allowed by the topic's [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

This constraint also applies to subscription SMTs if the **Enforce in-transit regions for Pub/Sub messages** [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services) is in effect.

  * If an AI Inference SMT is defined on an [export subscription](https://docs.cloud.google.com/pubsub/docs/subscription-overview#push_pull), then the endpoint region must be in the region of the associated resource:

    * For a [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription), the region of the destination table.
    * For a [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription), the region of the Cloud Storage bucket.
  * If a publish request is made to a region other than the endpoint region, then Pub/Sub automatically redirects the request to the endpoint region.

  * If you pull from a subscription with an AI Inference SMT, and the pull request is made to a region other than the endpoint region, then Pub/Sub rejects the request. We recommend using a [locational endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) for pull subscriptions. This constraint applies to both streaming pull and unary pull.

  * When a push subscription has an AI Inference SMT, the subscription pushes messages from the endpoint region. If a regional constraint violation occurs, then Pub/Sub stops pushing messages from that subscription.




## Troubleshooting

This section provides troubleshooting tips for the AI Inference SMT.

  * **Topic SMT errors**. If the inference fails when the message is published, the entire publish request fails. The error information is returned to the publisher client.

  * **Subscription SMT errors**. If the inference fails when the message is delivered (for example, due to prolonged model unavailability, sustained quota exhaustion, or invalid argument errors), the original, unmodified message is forwarded to the configured [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics). This ensures no data is lost. The forwarded message includes a `CloudPubSubDeadLetterSourceSMTErrorMessage` attribute containing the details of the SMT failure. We recommend setting up a dead-letter topic when using SMTs on a subscription.

  * **Model inference errors**. If the inference fails and returns an error, check the following:

    * Verify that the configured endpoint is correct.

    * Verify that the Pub/Sub message data contains a valid inference request for your model.

    * Verify that all model parameters are valid.

The inference might fail for other reasons, such as connectivity issues.

  * **Permission or endpoint errors**. If the configured service account loses permission to the endpoint, or the endpoint is deleted, the SMT fails.




## Quotas and limits

  * In addition to [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas), the AI Inference SMT is subject to the quotas and rate limits of the Agent Platform endpoint. Pub/Sub's built-in flow control automatically adjusts the request rate to avoid overloading the endpoint, but the rate can't exceed the model's quota.

  * The final transformed message size, including the original message and the inference output, must be less than the Pub/Sub [message size limit](https://docs.cloud.google.com/pubsub/quotas#resource_limits). If the transformed message exceeds the limit, the transform fails.




## What's next

  * [Learn more about SMTs](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview)
  * [Choose topic or subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/choose-smts)
  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)
  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
