---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook/
title: Webhooks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:16.338645+00:00
---

# Webhooks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Webhooks Stay organized with collections  Save and categorize content based on your preferences. 

_Webhooks_ are services that host your business logic or call other services. During a session, webhooks allow you to use the data extracted by Dialogflow CX's natural language processing to generate dynamic responses, validate collected data, or trigger actions on the backend. 

A webhook can either be a _standard webhook_ or a _flexible webhook_. With a standard webhook, the request and response fields are defined by Dialogflow CX. With a flexible webhook, you define the request and response fields.

You can also access the HTTP status code of the webhook call using the `$request.webhook_status_code` request parameter.

## Standard webhooks

With standard webhooks, you use Dialogflow CX-defined request and response messages. The request message provides many details about the session. For example, the current active page, recent matched intent, session parameter values, and agent-defined responses are all included.

### Standard webhook request

When a [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) with a webhook is called, Dialogflow CX sends an HTTPS POST webhook request to your webhook service. The body of this request is a `WebhookRequest` JSON object with information about the session.

Some [integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) populate the `WebhookRequest.payload` field with additional information. For example, the [Dialogflow CX Phone Gateway integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway#payload) provides the end-user caller ID.

For details, see the [`WebhookRequest` (V3)](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookRequest) or [`WebhookRequest` (V3Beta1)](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/WebhookRequest) reference documentation.

### Standard webhook response

After your webhook service receives a request, it must send a response that meets these requirements:

  * The response must occur within the timeout configured when creating the webhook resource.
  * The response must be 64 KiB or smaller.



For details, see the [`WebhookResponse` (V3)](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookResponse) or [`WebhookResponse` (V3Beta1)](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/WebhookResponse) reference documentation.

### Standard webhook resource settings

The following table describes webhook resource settings for standard webhooks:

X | Item  
---|---  
Display name | The name shown in the console for the webhook.  
Webhook timeout | When Dialogflow CX sends an HTTP request to your webhook service, this setting controls the timeout in seconds for each individual request attempt, not the overall conversational turn. If an attempt times out or fails with a transient error, Dialogflow CX automatically retries once. This retry can result in a total turnaround time of up to double the configured timeout value before returning an error. If a timeout occurs after retrying, Dialogflow CX invokes a [webhook.error.timeout event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). For details, see Automatic retries.  
Type | Set to **Service directory** if you are using service directory for private network access, otherwise set to **Generic web service**.  
Webhook URL | Provide the URL address for your webhook service.  
Subtype | Set to _Standard_.  
Environment-specific webhook | You can provide environment-specific webhooks.  
Authentication | See the Authentication section.  
Custom CA certificate | This is used to upload [custom CA certificates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca).  
  
## Flexible webhooks

With flexible webhooks, you define the request HTTP method, request URL parameters, and fields of the request and response messages. The request can only provide selected parameter values, and the response can only provide parameter override values. This simplifies the interface between the agent and the webhook, as there is rarely a need to communicate anything other than session parameter values. It also simplifies your webhook implementation because the request and response messages only contain what you need, and you can provide unique webhook messages for various scenarios.

### Flexible webhook request

When you create the webhook resource for your agent, you can specify the following for webhook requests:

  * The HTTP method used for webhook requests sent to your webhook service.
  * Session parameter values that Dialogflow CX should send to your webhook service using the URL.
  * Session parameter values that Dialogflow CX should send to your webhook service through the request JSON body if you choose `POST`, `PUT`, or `PATCH` as the method.



To send session parameter values using the request URL or JSON body, use [parameter references](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#use). You don't need to URL-escape the parameter reference or wrap it in quotations. At runtime, Dialogflow CX URL-escapes the parameter value as needed. A list or composite value is provided as JSON.

When using a parameter reference in the JSON body, you must wrap the reference in quotations, regardless of the parameter's type. If the parameter is actually a numeric scalar, list, or composite value, Dialogflow CX will remove the quotes when sending the request at runtime to preserve the parameter data type. String scalar types will remain quoted. If a numeric scalar, list, or composite value is referenced within a string value (for example: "This is a number: $session.params.size"), the parameter will be treated as a string ("This is a number: 3").

For example, you can provide the `fruit` and `size` session parameter values to the request URL as follows:
    
    
    https://your-webhook-service.com/handler?f=$session.params.fruit&s=$session.params.size
    

And, to the request JSON body as follows:
    
    
    {
      "fruitParameter": "$session.params.fruit",
      "sizeParameter": "$session.params.size"
    }
    

### Flexible webhook response

When creating the webhook resource for your agent, you can specify session parameters that Dialogflow CX should set to specific fields of the webhook response at runtime.

Your response must meet the following limitations:

  * The response must occur within the timeout configured when creating the webhook resource, otherwise the request will time out.
  * The response must be at most 64 KiB in size.



To specify a scalar, list, or composite field, use the following format:
    
    
    $.fully.qualified.path.to.field
    

For example, consider the following JSON response:
    
    
    {
      "routes" : [
        {
          "legs" : [
            {
              "distance" : {
                "text" : "2,064 mi",
                "value" : 3321004
              }
            }
          ]
        }
      ]
    }
    

To specify the "value" field, use the following:
    
    
    $.routes[0].legs[0].distance.value
    

### Flexible webhook resource settings

The following table describes webhook resource settings for flexible webhooks.

X | Item  
---|---  
Display name | The name shown in the console for the webhook.  
Webhook timeout | When Dialogflow CX sends an HTTP request to your webhook service, this setting controls the timeout in seconds for each individual request attempt, not the overall conversational turn. If an attempt times out or fails with a transient error, Dialogflow CX automatically retries once. This retry can result in a total turnaround time of up to double the configured timeout value before returning an error. If a timeout occurs after retrying, Dialogflow CX invokes a [webhook.error.timeout event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). For details, see Automatic retries.  
Type | Set to **Service directory** if you are using service directory for private network access, otherwise set to **Generic web service**.  
Webhook URL | Provide the URL address for your webhook service, which may include references to session parameters.  
Subtype | Set to _Flexible_.  
Method | Set the HTTP method for the webhook request.  
Request body | Provide the request JSON body as described above.  
Response configuration | Provide the session parameters that should be set to response fields as described above.  
Environment-specific webhook | You can provide environment-specific webhooks  
Authentication | See the authentication section.  
Custom CA certificate | This is used to upload [custom CA certificates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca).  
  
### Use a predefined custom template

Dialogflow offers predefined custom templates that you can use to integrate flexible webhooks with Salesforce CRM.

  1. Go to the **Manage** tab, select **Webhooks** , and then click **Create**.
  2. Under **Subtype** , select **Flexible**.
  3. Click **Configure using predefined template**.
  4. In the **Integration type** menu, select **Salesforce**.
  5. In the **API name** menu, select an API name. The template automatically fills out the webhook form based on the API name you choose. 
     1. Manually configure the following fields if applicable, based on your parameters: 
        * Webhook URL
        * Method
        * Request body JSON
        * Response Configuration
     2. The required OAuth fields will be highlighted in the **Authentication** section.
  6. Click **Save**.



## Webhook service requirements

Your webhook service must meet the following requirements:

  * Handle HTTPS requests. HTTP is unsupported. If you host your webhook service on Google Cloud using a [Compute](https://cloud.google.com/products/compute) or [Serverless computing](https://docs.cloud.google.com/serverless) solution, see the documentation for serving with HTTPS. For other hosting options, see [Get an SSL certificate for your domain](https://support.google.com/domains/answer/7630973).
  * Ensure the webhook service URL is publicly accessible, unless it is hosted as a Cloud Run resource or accessed as a Service directory webhook.
  * Handle requests and responses as described in the standard webhook or flexible webhook section.
  * If your agent does not integrate with [Service Directory private network access](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#sd), webhook calls are outside the service perimeter and are blocked when enabling VPC Service Controls. Service Directory supports limited endpoints; for details, refer to [Service Directory](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview).



## Authentication

Secure your webhook service so that only you or your Dialogflow CX agent can make requests. Configure this when creating or editing a webhook resource. Dialogflow CX supports the following authentication mechanisms:

X | Item  
---|---  
Authentication headers | For webhook settings, you can specify optional HTTP header key-value pairs. If supplied, Dialogflow CX adds these HTTP headers to webhook requests. It is common to provide a single pair with a key of `authorization`. The header values support [session parameter references](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#session-ref) and [system function parsing](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions) like in [static response messages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#static). If you use a static credential for the `authorization` header, we recommend you to supply your credential using Secret Manager.  
Basic auth with username and password | For webhook settings, you can specify optional login username and password values. If supplied, Dialogflow CX adds an authorization HTTP header to webhook requests. This header is of the form: `"authorization: Basic <base 64 encoding of the string username:password>"`. We recommend you to supply your username and password using Secret Manager.  
Third-party OAuth | You can specify the Third-party OAuth configuration so that Dialogflow CX exchanges an access token from the OAuth system and adds it in the authorization HTTP header. Only [client credential flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4) is supported. We recommend you to supply your client secret using Secret Manager.  
Service agent access tokens | Discontinued.  
Service account | You can use a service account for authentication. This can be used to access other Google Cloud APIs.  
Service agent ID tokens | You can choose ID token in the Service agent authentication section, which lets you use Service agent ID token for authentication. This lets you access Cloud Run resources.  
Mutual TLS authentication | See the [Mutual TLS authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls) documentation.  
**Note:** If multiple authentication options are enabled, higher priority options take precedence. The priority order is as follows: Authentication headers, Basic auth, Third-party OAuth, Service agent auth.**Note:** We don't recommend using IP ranges to authenticate webhook requests. If you choose to use the request's source IP to enable connectivity into your network perimeter, allow requests from the ranges listed at <https://www.gstatic.com/ipranges/goog.json> and deny connections from the ranges listed at <https://www.gstatic.com/ipranges/cloud.json> (these are Google's addresses that can be used to deploy third-party workloads). Dialogflow cannot guarantee IP ranges for machines that send webhook requests.**Note:** After Aug 15, 2025, exported agents no longer contain raw value credentials for authentication headers, basic auth with username and password, or third-party OAuth.

### Third-party OAuth

Dialogflow CX collects an access token from a third-party OAuth provider and adds it to the authorization HTTP header when making webhook requests.

The following table describes resource settings for third-party OAuth:

X | Item  
---|---  
Client ID | The Client ID to use when requesting an OAuth token.  
Client Secret | The secret to use when requesting an OAuth token. We recommend you to supply your client secret using Secret Manager.  
OAuth Endpoint URL | The URL to use to request an OAuth token.  
OAuth Scopes | A comma-separated list of scopes that the OAuth token can be used for.  
  
Requests sent to the OAuth endpoint URL to receive a token don't include the custom request headers configured for the webhook request. You can pass custom information to the OAuth server as parameters within the OAuth endpoint URL's query string.

**Note:** Third-party OAuth tokens are reused for webhook requests using the same client ID, endpoint URL, and scopes within the same Dialogflow CX agent so long as the request is made on the same Dialogflow CX server and the token has not expired. To achieve high availability, agents are deployed across many individual servers that don't share OAuth token caches. When deploying a solution that uses third-party OAuth tokens, carefully consider implementing an API proxy to help manage the volume of requests that your agent may send to your third-party OAuth provider.

### Service agent ID token

Dialogflow CX can generate an [ID token](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) using the [Dialogflow CX service agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). This token is added to the Authorization HTTP header when Dialogflow CX calls a webhook.

An ID token can be used to access Cloud Run resources after you grant the [Cloud Run Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`roles/run.invoker`) to 
    
    
    service-agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com

If the Cloud Run resources are in the same resource project, you don't need additional Identity and Access Management (IAM) permission to call them. 

The audience used to generate the ID token is the entire webhook URL, excluding any query parameters. If you are using Cloud Run, ensure that this URL is supported by the [Cloud Run audiences](https://docs.cloud.google.com/run/docs/configuring/custom-audiences).

For example, if the webhook URL is:
    
    
    https://myproject.cloudfunctions.net/my-function/method1?query=value
    

the following URL needs to be in custom audiences:
    
    
    https://myproject.cloudfunctions.net/my-function/method1
    

Any webhook can also optionally validate the token using Google client libraries or open-source libraries like the [Google Auth Library for Node.js](https://github.com/googleapis/google-auth-library-nodejs).

If your webhook is hosted on Cloud Run and accessed through a load balancer, add your load balancer's URL as a custom audience to your Cloud Run. For more information about custom audiences, see [Set custom audiences for services](https://docs.cloud.google.com/run/docs/configuring/custom-audiences).

### Service Account

Service accounts can be used to authenticate webhook requests to any Google APIs that support them.

If you haven't already, [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).

Because service accounts are principals, they can access resources in your project by [granting them a role](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-identities), just like any other principal. The service account email is used to [generate an access token](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials) that is sent in the `Authorization` header of the webhook request.

To configure the webhook to use service accounts, you must have the following permissions:

  * `roles/iam.serviceAccountUser`



To generate tokens, the [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent) must have the following permissions:

  * `roles/iam.serviceAccountTokenCreator`



The service account must also have permissions to access the service that hosts the webhook.

**Note:** If you are trying to use service accounts across multiple projects, ensure that your [organization policy supports it](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project). Both permissions must be granted in the project that contains the service account.

### Secret Manager Authentication

If you use authentication headers, basic auth with username and password, or third-party OAuth, you can store the credentials as **secrets** using [Secret Manager](https://docs.cloud.google.com/secret-manager). The following are the necessary steps to authenticate your webhook using secrets:

  1. [Create your secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) if you don't have one.
  2. Grant the [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent) the [**Secret Manager Secret Accessor**](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) role on the new secret.
  3. Copy your credential to the clipboard.
  4. [Add a new secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) to your secret and paste your credential as the secret value: 
     * If you use authentication headers, enter `Bearer <YOUR_CREDENTIAL>`.
     * If you use basic username and password authentication, enter `<YOUR_USERNAME>:<YOUR_PASSWORD>`.
     * Omit any newline character at the end.
  5. Copy the name of the secret version you added. The name format is `projects/<var>PROJECT_ID</var>/secrets/<var>SECRET_ID</var>/versions/<var>VERSION_ID</var>`.
  6. Open the webhook edit screen.
  7. Configure the authentication settings: 
     * If you use authentication headers, create a new **Secret version request header**. Enter "Authorization" in the **Key** field, and paste the secret version name into the **Secret version** field.
     * For basic username and password authentication, click **Secret version** under **Basic Auth** , and paste the secret version name into the **Secret version** field.
     * If you use **Third-party OAuth** , click **Secret version** under **Third-party OAuth** , and paste the secret version name into the **Secret version** field.
  8. Click **Save**.

**Note:** We only support global Secret Manager secrets. We don't support regional secrets.

## HTTPS certificate verification

Dialogflow CX by default uses Google's default trust store to verify HTTPS certificates. If you intend to use certificates not recognized by Google's default trust store for your HTTPS server, such as self-signed certificates or custom root certificates, see [Custom CA certificates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca).

## Environment-specific webhooks

If you use [environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) to isolate production from development, you can configure your webhooks to be environment-specific. You can provide environment-specific URL and authentication settings for each webhook resource.

This configuration lets you safely develop and test your webhook code updates before deploying them to production.

## Create or edit webhook resources

After you have a _webhook service_ running, create a _webhook resource_ in your agent that includes connectivity and authentication information. You can edit webhook resource settings at any time.

To create or edit a webhook resource:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Go to your project.
  3. Select your agent.
  4. Click the **Manage** tab.
  5. Click **Webhooks**.
  6. Click **Create** or select an existing webhook to edit.
  7. Configure the standard webhook resource settings or flexible webhook resource settings.
  8. Click **Save**.



###  API 

For information about creating a webhook resource, see the `create` method for the `Webhook` type. For information about editing a webhook resource (except for environment-specific settings), see the `patch` or `update` method for the `Webhook` type. Go to the Webhook API reference

**Select a protocol and version for the Webhook reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Webhook resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks) |  [Webhook resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.webhooks)  
RPC |  [Webhook interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Webhooks) |  [Webhook interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Webhooks)  
C++ |  [WebhooksClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1WebhooksClient.html) |  Not available   
C# |  [WebhooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClient) |  Not available   
Go |  [WebhooksClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_WebhooksClient) |  Not available   
Java |  [WebhooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhooksClient) |  [WebhooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.WebhooksClient)  
Node.js |  [WebhooksClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.WebhooksClient.html) |  [WebhooksClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.WebhooksClient.html)  
PHP |  Not available  |  Not available   
Python |  [WebhooksClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.webhooks.WebhooksClient) |  [WebhooksClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.webhooks.WebhooksClient)  
Ruby |  Not available  |  Not available   
  
Close

For information about editing the environment-specific settings for a webhook, see the `patch` or `update` method for the `Environment` type. Go to the Environment API reference

**Select a protocol and version for the Environment reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Environment resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments) |  [Environment resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.environments)  
RPC |  [Environment interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#environments) |  [Environment interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#environments)  
C++ |  [EnvironmentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1EnvironmentsClient.html) |  Not available   
C# |  [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClient) |  Not available   
Go |  [EnvironmentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_EnvironmentsClient) |  Not available   
Java |  [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient) |  [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EnvironmentsClient)  
Node.js |  [EnvironmentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.EnvironmentsClient.html) |  [EnvironmentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.EnvironmentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.environments.EnvironmentsClient) |  [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.environments.EnvironmentsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Webhook errors

If your webhook service encounters an error while handling a webhook request, your webhook code should return one of the following HTTP status codes:

  * `400`: Bad Request
  * `401`: Unauthorized
  * `403`: Forbidden
  * `404`: Not found
  * `500`: Server fault
  * `503`: Service unavailable



Dialogflow CX invokes a webhook error or timeout [built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) and continues processing as usual in the following error situations:

  * The response timeout is exceeded.
  * An error status code is received.
  * The response is invalid.
  * The webhook service is unavailable.



If the webhook service call was triggered by a detect intent API call, the `queryResult.webhookStatuses` field in the detect intent response contains the webhook status information.

### Automatic retries

Dialogflow CX automatically retries requests on certain webhook errors to improve robustness. Automatic retries are enabled by default and cannot be disabled.

Dialogflow CX executes a single retry for transient failures, such as request timeouts, dropped network connections, and HTTP status codes in the 5xx range (such as `500 Server fault` or `503 Service unavailable`). Terminal client errors, such as HTTP status code `404 Not found`, fail immediately without a retry.

#### Cumulative latency and timeout budgeting

Because Dialogflow CX retries transient failures once, an unresponsive webhook endpoint can result in a cumulative turnaround time of up to double the configured timeout value before Dialogflow CX returns an error. For example, with the default 5-second timeout setting, an unresponsive endpoint times out after 5 seconds on the initial attempt and times out after another 5 seconds on the retry attempt. This results in a total latency of approximately 10 seconds before Dialogflow CX invokes error handlers, such as a `webhook.error.timeout` event handler or a `sys.no-match-default` event handler.

If your architecture has strict upstream latency limits (such as telephony or interactive voice response (IVR) systems that terminate calls after a 10-second timeout window), budget for both attempts by setting the webhook timeout to half of the allowable window (for example, between 2.5 and 4 seconds).

#### Best practices for retries

To handle retries effectively in your webhook service:

  * Implement idempotency or request deduplication in your webhook service logic to safely process duplicate requests.
  * If your webhook operation takes longer than the configured timeout, return an immediate HTTP status code `200 OK` response with a fallback message, and process the long-running task asynchronously.



## Using Cloud Run

**Caution:** This section describes how to use secure Cloud Run resources for Dialogflow CX webhooks. Keeping your resources secure is recommended. If you choose to authenticate with URL-based username and password, or HTTP headers, you must allow unauthenticated access to your Cloud Run resource.

Dialogflow CX integrates with [Cloud Run](https://docs.cloud.google.com/run/docs), so you can create a secure, serverless webhook. If you create a Cloud Run resource that resides in the same project as your agent, select **Service Agent Auth** , and then select **ID token** in authentication configuration so that your agent can securely call your webhook.

You must manually set up this integration in the following two situations:

  1. The **Dialogflow CX Service Agent** [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) with the following address must exist for your agent project: 
         
         service-agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com

This special service account and the associated key is normally created automatically when you create the first agent for a project. If your agent was created before November 01, 2020, you can trigger creation of this special service account: 
     1. Create a new agent for the project.
     2. Execute the following command: 
            
            gcloud beta services identity create --service=dialogflow.googleapis.com --project=agent-project-id

  2. If your webhook function resides in a different project than the agent, you must provide the **Cloud Run Invoker** or **Cloud Functions Invoker** [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) to the **Dialogflow CX Service Agent** service account in your Cloud Run resource project.



Next, select **Service Agent Auth > ID Token** in the **Auth configuration** section.

## Using containerized webhooks and the Go ezcx framework

To implement a containerized webhook using Go, see the [Go ezcx framework](https://github.com/googleCloudPlatform/ezcx). This framework simplifies many of the steps required to create a webhook.

## Using Cloud Run with internal only traffic

**Note:** The use of Cloud Run outside the VPC Service Controls perimeter of the Dialogflow CX agent project for webhooks is not supported.

You can use Cloud Run resources configured to accept internal traffic from Virtual Private Cloud (VPC) networks in the same project or the same VPC Service Controls perimeter as a webhook, provided the agent is in the same project or the same VPC Service Controls perimeter.

## Using Service Directory for private network access

Dialogflow CX integrates with [Service Directory private network access](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview), so it can connect to webhook targets inside your VPC network. This keeps the traffic within the Google Cloud network and enforces [IAM](https://docs.cloud.google.com/iam/docs/overview) and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To set up a webhook targeting a private network:

  1. Follow [Service Directory private network configuration](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access) to configure your VPC network and Service Directory endpoint.

**Note:** Dialogflow CX caches Service Directory information for 90 seconds. This means that when you update the Service Directory endpoint, the change takes 90 seconds to occur.
  2. The **Dialogflow CX Service Agent** [service account](https://docs.cloud.google.com/IAM/docs/understanding-service-accounts) with the following address must exist for your agent project: 
         
         service-agent-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com

Grant the following roles to the **Dialogflow CX Service Agent** service account in the project where your Service Directory is located:

     * `servicedirectory.viewer`
     * `servicedirectory.pscAuthorizedService`

Additionally, if your Service Directory is in a different project than your Dialogflow CX agent, you also need to grant the `servicedirectory.viewer` role to the Dialogflow CX Service Agent account in the project that hosts your Dialogflow CX agent.

  3. Specify the Service Directory service, the URL, and any optional authentication information when you create the webhook.

###  Console 

![Service Directory Webhook screenshot.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-webhook-sd.png)

###  API 

See the `serviceDirectory` field for the `Webhook` type. Go to the Webhook API reference

**Select a protocol and version for the Webhook reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Webhook resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks) |  [Webhook resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.webhooks)  
RPC |  [Webhook interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Webhooks) |  [Webhook interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Webhooks)  
C++ |  [WebhooksClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1WebhooksClient.html) |  Not available   
C# |  [WebhooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClient) |  Not available   
Go |  [WebhooksClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_WebhooksClient) |  Not available   
Java |  [WebhooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhooksClient) |  [WebhooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.WebhooksClient)  
Node.js |  [WebhooksClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.WebhooksClient.html) |  [WebhooksClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.WebhooksClient.html)  
PHP |  Not available  |  Not available   
Python |  [WebhooksClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.webhooks.WebhooksClient) |  [WebhooksClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.webhooks.WebhooksClient)  
Ruby |  Not available  |  Not available   
  
Close




To troubleshoot issues, you can set up a [private uptime check](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks) to verify that your Service Directory is configured correctly.

## Samples and troubleshooting

For more information, see the [webhook how-to guide](https://docs.cloud.google.com/dialogflow/cx/docs/how/webhook).

[ Previous arrow_back  Fulfillments  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment)

[ Next Generators  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generators)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
