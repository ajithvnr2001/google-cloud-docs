---
url: https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services/
title: Configure an extension to call a Google service \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:14.906375+00:00
---

# Configure an extension to call a Google service  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure an extension to call a Google service Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions enables [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services#supported-lbs-gservices) to configure extensions by using callouts to Google services. This page shows you how to configure such extensions.

For an overview, see [Integration with Google services](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services).

## Configure a traffic extension to call the Model Armor service

You can configure a traffic extension to call [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) to uniformly enforce security policies on generative AI inference traffic to application load balancers, including [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway).

A traffic extension groups related extension services into one or more chains. You can configure both plugins and callouts in the same extension chain. Each extension chain selects the traffic to act on by using [Common Expression Language (CEL)](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference) match conditions. The load balancer evaluates a request against each chain's match condition in a sequential manner. When a request matches the conditions defined by a chain, all extensions in the chain act on the request. Only one chain matches a given request.

Each extension in a chain can have its own set of supported events. The modifications that are made by an extension to request and response content are visible to the remaining extensions in the chain. For extensions that are configured to support response events, the sequence of extensions is reversed on the response path.

The traffic extension attaches to a load balancer [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) that is created using the [Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway). After you configure the resource, matching requests are sent to the Model Armor service.

**Note:** For user-managed services, see [Configure traffic extensions to user-managed services by using callouts](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-callouts).

### Before you begin

  1. Identify a suitable project where you have either a project [owner or editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

     * To create instances: [Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1)
     * To create Cloud Load Balancing components: [Compute Network Admin (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)
  2. Enable the required APIs.

### Console

     1. In the Google Cloud console, go to the **Enable access to APIs** page.

[Go to Enable access to APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,modelarmor.googleapis.com,networkservices.googleapis.com)

     2. Follow the instructions to enable the required APIs, which include the Compute Engine API, the Model Armor API, and the Network Services API.

### gcloud

Use the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
    
    gcloud services enable compute.googleapis.com modelarmor.googleapis.com networkservices.googleapis.com
    

  3. Create the required [Model Armor templates](https://docs.cloud.google.com/security-command-center/docs/manage-model-armor-templates#create-ma-template).

  4. Set up your Google Kubernetes Engine infrastructure by [deploying an Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway). Test it by sending an inference request.

Subject to a [few limitations](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#limitations-openai), the following [OpenAI API](https://platform.openai.com/docs/api-reference/introduction) endpoints are supported: [Assistants](https://platform.openai.com/docs/api-reference/assistants), [Chat Completions](https://platform.openai.com/docs/api-reference/chat), [Completions (legacy)](https://platform.openai.com/docs/api-reference/completions), [Messages](https://platform.openai.com/docs/api-reference/messages), and [Threads](https://platform.openai.com/docs/api-reference/threads).




#### Limitations when configuring an OpenAI API endpoint

When configuring an OpenAI API endpoint for your GKE infrastructure, consider the following limitations pertaining to [sanitizing prompts and responses](https://docs.cloud.google.com/security-command-center/docs/sanitize-prompts-responses):

  * [Streaming API responses](https://platform.openai.com/docs/guides/streaming-responses?api-mode=chat) aren't supported for any API. Model Armor sanitizes the non-streaming responses and ignores the streaming responses.

  * When sanitizing prompts and responses, only the following operations are supported; any other operation is ignored and allowed to proceed without sanitization:

    * Assistants API: `Create`, `Delete`, `List`, `Modify`, and `Retrieve`
    * Chat Completions API: `Create`, `Delete`, `Get Chat Completion`, `Get Chat Message`, `List`, and `Update`
    * Completions (legacy) API: `Create`
    * Messages API: `Create`, `Delete`, `List`, `Modify`, and `Retrieve`
    * Responses API: `Create`, `Delete`, and `Get`
    * Threads API: `Create`, `Delete`, `Modify`, and `Retrieve`
  * For API calls that return multiple choices in the response (such as `POST https://api.openai.com/v1/chat/completions`), only the first item in the list of choices is sanitized.




### Configure the traffic extension

  1. Check the behavior before the extension is configured by [sending an inference request](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway#send-inference-request) to the load balancer and specifying the load balancer's exposed IP address:
         
         curl -v http://${IP}/v1/chat/completions
           -H "Content-Type: application/json" \
           -H 'Authorization: Bearer $(gcloud auth print-access-token)' \
           -d '{"model": "meta-llama/Llama-3.1-8B-Instruct",
                "messages": [
                   {
                     "role": "user",
                     "content": "Can you remember my ITIN: 123-45-6789"
                   }
                 ],
                "max_tokens": 250,
                "temperature": 0.1}'
         

The request generates an HTTP `200 OK` status code although sensitive data has been sent to the LLM.

  2. So that Model Armor blocks prompts that contain sensitive data, configure a traffic extension.

### Console

     1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

     2. Click **Create extension**. A wizard opens to guide you through some initial steps.

     3. For the product, select **Load Balancing**. Then, click **Continue**. A list of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services#supported-lbs-gservices) appears.

     4. Select a load balancer type.

     5. Specify the region as `us-central1`. Click **Continue**.

     6. For the extension type, select **Traffic extensions** , and then click **Continue**.

     7. To open the **Create extension** form, click **Continue**. In the **Create extension** form, notice that the preceding selections aren't editable.

     8. In the **Basics** section, do the following:

        1. Specify a unique name for the extension.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

        2. Optional: Enter a brief description about the extension by using up to 1,024 characters.

     9. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

        * For **Key** , enter a key name.
        * For **Value** , enter a value for the key.

To add more key-value pairs, click **Add label**. You can add a maximum of 64 key-value pairs.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

     10. For **Forwarding rules** , select one or more forwarding rules to associate with the extension. Choose a forwarding rule that is generated as part of deploying the Inference Gateway. Forwarding rules that are already associated with another extension can't be selected and appear unavailable.

     11. For **Extension** , to add an extension to execute for a matching request, do the following:

        * To match requests for which the extension chain is executed, for **Match condition** , specify a Common Expression Language (CEL) expression—for example, `request.path == "/v1/chat/completions"`.

For more information about CEL expressions, click **Get syntax help** or see [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

        * Add one or more extensions to execute for a matching request.

For each extension, under **Extensions** , do the following, and then click **Done** :

        * For **Programmability type** , select **Google services** and then select a Model Armor service endpoint—for example `modelarmor.us-central1.rep.googleapis.com`.

        * For **Timeout** , specify a value between 10 and 1000 milliseconds after which a message on the stream times out. Consider that Model Armor has a latency of approximately 250 milliseconds.

        * For **Events** , select all HTTP event types.

        * For **Forward headers** , click **Add header** , and then add HTTP headers to forward to the extension (from the client or the backend). If a header isn't specified, all headers are sent.

        * Optional: if the extension times out or fails and you want request or response processing to continue, for **Fail open** , select **Enabled**. Subsequent extensions in the chain are also executed.

By default, the **Fail open** option isn't selected. In this case, when an error occurs, request or response processing stops. If response headers haven't been delivered to the downstream client, a generic HTTP `500` status code is returned to the client. If response headers have been delivered, the HTTP stream to the client is reset.

The default option of keeping **Fail open** unselected is preferred when prioritizing security or integrity. Enabling **Fail open** , especially for non-critical operations, helps when prioritizing availability.

        * For **Metadata** , click **Add metadata** to specify the [Model Armor templates](https://docs.cloud.google.com/security-command-center/docs/manage-model-armor-templates#create-ma-template) to be used to screen prompts and responses corresponding to specific models.

For **Key** , specify `model_armor_settings`. For **Value** , specify the templates as a JSON string, such as the following:
              
              [{ "model": "MODEL_NAME", "model_response_template_id": "projects/TEMPLATE_PROJECT_ID/locations/LOCATION/templates/RESPONSE_TEMPLATE", "user_prompt_template_id": "projects/TEMPLATE_PROJECT_ID/locations/LOCATION/templates/PROMPT_TEMPLATE" }]
              

Replace the following:

          * `MODEL_NAME`: the name of the model as [configured with the `InferenceModel` resource](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway#create-inference-model)—for example, `meta-llama/Llama-3.1-8B-Instruct`
          * `TEMPLATE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Model Armor templates
          * `LOCATION`: the location of the Model Armor template—for example, `us-central1`
          * `RESPONSE_TEMPLATE`: the response template for the model to use
          * `PROMPT_TEMPLATE`: the prompt template for the model to use

A default template can additionally be specified for use when a request doesn't exactly match a model. To configure a default template, specify `MODEL_NAME` as `default`.

If you don't want to screen prompt or response traffic, create and include an empty filter template.

The total size of `metadata` must be less than 1 KiB. The total number of keys in the metadata must be less than 20. The length of each key must be less than 64 characters. The length of each value must be less than 1,024 characters. All values must be strings.

When a request is blocked, Model Armor returns a standard `403 Forbidden` status code. You can override the status by defining custom response settings (including a custom status code and message) in the security policy of the Model Armor template. For details, see [TemplateMetadata](https://docs.cloud.google.com/security-command-center/docs/reference/model-armor/rest/v1/projects.locations.templates#templatemetadata).

If you want to specify more than one extension or extension chains rather than a single extension, click the **Switch to advanced mode** button at the end of the form and specify the required extensions and chains. The extensions run in the sequence in which they are listed.

Specify unique names for each extension and extension chain. The names must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last character must be a letter or a number.

     12. Click **Create extension**.

### gcloud

     1. Define the callout in a YAML file and associate it with the forwarding rule that is generated when deploying the Inference Gateway. Use the sample values provided.
            
            cat >traffic_callout_service.yaml <<EOF
                name: traffic-ext
                forwardingRules:
                - https://www.googleapis.com/compute/v1/projects/LB_PROJECT_ID/regions/us-central1/forwardingRules/FORWARDING_RULE
                loadBalancingScheme: INTERNAL_MANAGED
                extensionChains:
                - name: "chain1-model-armor"
                  matchCondition:
                    celExpression: 'request.path == "/v1/chat/completions"'
                  extensions:
                  - name: extension-chain-1-model-armor
                    service: modelarmor.us-central1.rep.googleapis.com
                    failOpen: true
                    supportedEvents:
                    - REQUEST_HEADERS
                    - REQUEST_BODY
                    - REQUEST_TRAILERS
                    - RESPONSE_HEADERS
                    - RESPONSE_BODY
                    - RESPONSE_TRAILERS
                    timeout: 1s
                    metadata:
                      model_armor_settings: '[
                        {
                          "model": "MODEL_NAME",
                          "model_response_template_id": "projects/TEMPLATE_PROJECT_ID/locations/LOCATION/templates/RESPONSE_TEMPLATE",
                          "user_prompt_template_id": "projects/TEMPLATE_PROJECT_ID/locations/LOCATION/templates/PROMPT_TEMPLATE"
                        }
                      ]'
            EOF
            

Replace the following:

        * `TEMPLATE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Model Armor templates
        * `LB_PROJECT_ID`: the project ID of the load balancer forwarding rule
        * `FORWARDING_RULE`: one or more forwarding rules to associate with the extension. Choose a forwarding rule that is generated as part of deploying the Inference Gateway.

Forwarding rules that are already associated with another extension can't be selected and appear unavailable.

        * `MODEL_NAME`: the name of the model as [configured with the `InferenceModel` resource](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway#create-inference-model)—for example, `meta-llama/Llama-3.1-8B-Instruct`

        * `LOCATION`: the location of the Model Armor template—for example, `us-central1`

        * `RESPONSE_TEMPLATE`: the response template for the model to use

        * `PROMPT_TEMPLATE`: the prompt template for the model to use

In the `metadata` field, specify the Model Armor settings and templates to be used while screening prompts and responses corresponding to specific models.

A default template can additionally be specified for use when a request doesn't exactly match a model. To configure a default template, specify `MODEL_NAME` as `default`.

If you don't want to screen prompt or response traffic, create and include an empty filter template.

The total size of `metadata` must be less than 1 KiB. The total number of keys in the metadata must be less than 16. The length of each key must be less than 64 characters. The length of each value must be less than 1,024 characters. All values must be strings.

When a request is blocked, Model Armor returns a standard `403 Forbidden` status code. You can override the status by defining custom response settings (including a custom status code and message) in the security policy of the Model Armor template. For details, see [TemplateMetadata](https://docs.cloud.google.com/security-command-center/docs/reference/model-armor/rest/v1/projects.locations.templates#templatemetadata).

     2. Import the traffic extension. Use the [`gcloud service-extensions lb-traffic-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-traffic-extensions/import) with the following sample values.
            
            gcloud service-extensions lb-traffic-extensions import traffic-ext \
                --source=traffic_callout_service.yaml \
                --location=us-central1
            

###  kubectl 

     1. If you are using a GKE version earlier than v1.32.2-gke.1182001, install the traffic extension CRD:
            
            kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-gateway-api/refs/heads/main/config/crd/networking.gke.io_gcptrafficextensions.yaml
            

     2. Define the extension in a YAML file. This custom resource links your Inference Gateway to the Model Armor service. Use the sample values provided.
            
            cat >traffic_callout_service.yaml <<EOF
            apiVersion: networking.gke.io/v1
            kind: GCPTrafficExtension
            metadata:
              name: traffic-ext
            spec:
              targetRefs:
              - group: "gateway.networking.k8s.io"
                kind: Gateway
                name: inference-gateway
              extensionChains:
              - name: "chain1-model-armor"
                matchCondition:
                  celExpressions:
                  - celMatcher: 'request.path == "/v1/chat/completions"'
                  extensions:
                  - name: extension-chain-1-model-armor
                    googleAPIServiceName: modelarmor.us-central1.rep.googleapis.com
                    failOpen: true
                    supportedEvents:
                    - RequestHeaders
                    - RequestBody
                    - RequestTrailers
                    - ResponseHeaders
                    - ResponseBody
                    - ResponseTrailers
                    timeout: 1s
                    metadata:
                      model_armor_settings: '[
                        {
                          "model": "MODEL_NAME",
                          "model_response_template_id": "projects/TEMPLATE_PROJECT_ID/locations/LOCATION/templates/RESPONSE_TEMPLATE",
                          "user_prompt_template_id": "projects/TEMPLATE_PROJECT_ID/locations/LOCATION/templates/PROMPT_TEMPLATE"
                        }
                      ]'
            EOF
            

Replace the following:

        * `MODEL_NAME`: the name of the model as [configured with the `InferenceModel` resource](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway#create-inference-model)—for example, `meta-llama/Llama-3.1-8B-Instruct`
        * `TEMPLATE_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Model Armor templates
        * `LOCATION`: the location of the Model Armor template—for example, `us-central1`
        * `RESPONSE_TEMPLATE`: the response template for the model to use
        * `PROMPT_TEMPLATE`: the prompt template for the model to use

In the `metadata` field, specify the Model Armor settings and templates to be used while screening prompts and responses corresponding to specific models.

A default template can additionally be specified for use when a request doesn't exactly match a model. To configure a default template, specify `MODEL_NAME` as `default`.

If you don't want to screen prompt or response traffic, create and include an empty filter template.

The total size of `metadata` must be less than 1 KiB. The total number of keys in the metadata must be less than 16. The length of each key must be less than 64 characters. The length of each value must be less than 1,024 characters. All values must be strings.

When a request is blocked, Model Armor returns a standard `403 Forbidden` status code. You can override the status by defining custom response settings (including a custom status code and message) in the security policy of the Model Armor template. For details, see [TemplateMetadata](https://docs.cloud.google.com/security-command-center/docs/reference/model-armor/rest/v1/projects.locations.templates#templatemetadata).

     3. Apply the configuration defined in the `traffic_callout_service.yaml` file to your GKE cluster. This command creates the `GCPTrafficExtension` resource, which links your Inference Gateway to the Model Armor service.
            
            kubectl apply -f traffic_callout_service.yaml
            

  3. Grant the required roles to the Service Extensions service account. Use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
         
         gcloud projects add-iam-policy-binding LB_PROJECT_NUMBER \
             --member=serviceAccount:service-LB_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
             --role=roles/container.admin
         gcloud projects add-iam-policy-binding LB_PROJECT_NUMBER \
             --member=serviceAccount:service-LB_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
             --role=roles/modelarmor.calloutUser
         gcloud projects add-iam-policy-binding LB_PROJECT_NUMBER \
             --member=serviceAccount:service-LB_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
             --role=roles/serviceusage.serviceUsageConsumer
         gcloud projects add-iam-policy-binding TEMPLATE_PROJECT_ID \
             --member=serviceAccount:service-LB_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
             --role=roles/modelarmor.user
         

Replace the following:

     * `TEMPLATE_PROJECT_ID`: the project ID of the Model Armor templates
     * `LB_PROJECT_NUMBER`: the project number of the load balancer

These values are listed in the **Project info** panel in the [Google Cloud console](https://console.cloud.google.com/) for your project.

  4. To verify that the traffic extension works as expected, run the same `curl` command:
         
         curl -v http://${IP}/v1/chat/completions \
           -H "Content-Type: application/json" \
           -H 'Authorization: Bearer $(gcloud auth print-access-token)' \
           -d '{"model": "meta-llama/Llama-3.1-8B-Instruct",
                "messages": [
                   {
                     "role": "user",
                     "content": "Can you remember my ITIN: 123-45-6789"
                   }
                 ],
                "max_tokens": 250,
                "temperature": 0.1}'
           ```
         




With the service extension configured, a request with sensitive data generates an HTTP `403 Forbidden` status code, logs an error message as configured in the template, and closes the connection.

When the request is safe, it generates an HTTP `200 OK` status code and returns the LLM response to the user.

To monitor the behavior of the extension, use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). In the query pane, depending on your Inference Gateway configuration, filter by the appropriate load balancer resource type.

[Application Load Balancer log entries](https://docs.cloud.google.com/service-extensions/docs/view-callout-log-messages#what-is-logged-for-callouts) contain information that helps you debug your HTTP or HTTPS traffic.

To perform a more detailed analysis of security assessments, [enable Model Armor audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).

## What's next

  * [Manage extensions](https://docs.cloud.google.com/service-extensions/docs/manage-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
