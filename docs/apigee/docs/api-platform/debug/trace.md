---
url: https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace/
title: Using Debug \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:21.032971+00:00
---

# Using Debug  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using Debug Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes how to create and manage debug sessions, and view the request and response data using the Apigee UI and API. 

Use [Offline Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace) to view and analyze debug sessions that were previously downloaded.

## Creating a debug session 

The Debug tool is simple to use. You start a debug session, and then make an API call to Apigee, and then view the request and response data in the UI.

Create a debug session using the Apigee UI or API as described in the following sections.

**Note:** There is a delay of approximately 15 seconds between starting a debug session and its activation across Apigee. This can cause missed API requests in the initial 15-20 seconds of a debug session. **Note:** The Debug tool is available in the Apigee UI. Some debug actions can also be performed using the API. 

### Apigee UI

To create a debug session:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API Proxies** page. 

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the API proxy that you want to debug. This displays the Proxy Editor **Overview** pane. 
  3. Click the **Debug** tab.
  4. Click **Start debug session**. This displays the **Start debug session** pane. 
  5. In the **Start debug session** pane:

     1. Select the **Environment** in which you want to run the debug session. 
     2. (Optional) From the **Filter** drop-down list, select a filter to apply to all transactions in the debug session you are creating. The default is `None (All transactions)`, which includes all transactions in the debug data. 

For information on using filters, see Using filters in a debug session. For information about the built-in filters, see Using predefined filters. 

     3. Click **Start**.



The Apigee UI now displays the **Debug session in progress** pane. 

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/new-debug-session-v2.png)![new debug session](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/new-debug-session-v2.png)

The debug session records requests for 10 minutes or until 15 requests have been captured. You can adjust the 10-minute limit if you create the debug session using the API. The **Ends within** field displays the amount of time remaining in the session. 

You won't see any information displayed in the Debug pane until you send a request to the proxy you are debugging in the selected environment for the debug session. 

After you send the request, it is displayed in the **Transactions** list pane. The **Transactions** list updates every five seconds. 

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/request-in-debug-session-v2.png)![request in transaction list](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/request-in-debug-session-v2.png)

To view or copy transaction output:

  1. In the **Transactions** list, click notes **View transaction output**. The **Transaction output** pane displays. 
  2. Click an individual transaction, or click **All transactions**.
  3. Click content_copy **Copy** to copy the transaction output to the clipboard.
  4. Click **Close**. 

**Note:** During an active debug session, you can start another session in the Apigee UI. See  Starting another debug session in the UI. 

### API

To create a debug session using the API, issue a `POST` request to the following resource: 
    
    
    https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /apis/**$API** /revisions/**$REV** /debugsessions

Optionally, you can: 

  * Set the length of a debug session (in seconds) by passing the `timeout` property as a query parameter or in the request body. If both are specified, the `timeout` value specified in the request body takes precedence.
  * Filter data in a debug session by passing the `filter` property in the request body.



The following example demonstrates how to create a debug session using the API.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/apis/PROXY/revisions/REV/debugsessions" \
          -X POST \
          -H "Authorization: Bearer $TOKEN"
        

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response:
    
    
    {
          "name":"56382416-c4ed-4242-6381-591bbf2788cf",
          "validity":300,
          "count":10,
          "tracesize":5120,
          "timeout":"600"
        }

Subsequent requests to your API proxy (until the session duration or maximum number of requests is reached) will be evaluated and potentially stored in the debug session data.

For more information, see the [Create debug session API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/create).

#### Setting the length of a debug session using the API

To set the length of a debug session using the API, include the following as a payload in your debug session creation request:
    
    
    {
          "timeout":"debug_session_length_in_seconds"
        }

The following example creates a debug session that is just 42 seconds long:
    
    
    curl https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/apis/PROXY/revisions/REV/debugsessions"
          -X "POST" \
          -H "Authorization: Bearer $TOKEN" \
          -d ' {
            "timeout":"42"
          } '

You can set a session's `timeout` in debug session creation requests only; you cannot change a session's duration after you create the session.

The default value of `timeout` is 300 (5 minutes). The maximum value is 600 seconds (10 minutes).

### Copy the proxy URL

The proxy URL is used to send requests to your API proxy.

To find and copy the proxy URL:

  1. In the **Debug session** pane, **URL** field, click content_copy **Copy**. 
  2. If a **Debug session** is not open: 
     1. In the Google Cloud console, go to the **Apigee > Management > Environments > Environment Groups** page.

[Go to Environment Groups ](https://console.cloud.google.com/apigee/environments/groups)

     2. The URL is the **Hostname** for the respective environment you'd like to run your debug session with. Select it and then copy it. 



To select a different proxy URL:

  1. In the **Debug session** pane, **URL** field, click edit **Edit**. 
  2. Make any desired changes and then click **Update**.
  3. If a **Debug session** is not open: 
     1. Find the proxy URL.
     2. Click more_vert **More** , and then click edit **Edit**. 
     3. Make any desired changes and then click **Update**.



### Starting another debug session in the UI

You can create any number of debug sessions in the UI.

During an active debug session, you _can_ start another session in the Apigee UI. To do this, click close **Close** in the **Debug session** pane: 

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/ui-trace-return-to-start-panel-v2.png)![Close and return to the Start a debug session panel](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/ui-trace-return-to-start-panel-v2.png)

The UI returns to the **Start a debug session** panel, where you can start a new debug session.

### When does a debug session end?

You cannot simply _stop_ an active debug session. You can, however, delete an active session's data, as described in Deleting debug session data.

When you create a debug session, two properties determine when it ends:

  * **timeout:** The length of time for which you collect data during a session. The default length depends on how you started the session (through the UI or API). The maximum value is 600 seconds (or 10 minutes). **Tip:** You cannot configure the timeout when you create a new debug session with the Apigee UI. You _can_ , however, set the timeout when you create a new debug session using the API.
  * **count:** The maximum number of requests that are recorded in a single session _per Message Processor_. Because the number of Message Processors in most clusters is variable, the effects of the count can be unpredictable. Apigee does not recommend customizing this setting.



When either the timeout or the count is reached, the debug session for that Message Processor ends.

The following terms are used to describe the state of a debug session:

  * _active session_ is a debug session that has not yet reached its timeout or exceeded its count. An active session is still recording request data for requests that are not filtered out.
  * _completed session_ is a debug session that has either reached its timeout or exceeded its count; a completed session no longer records data about new requests and its data is deleted within 24 hours of the time at which the session ended.



## How to read a debug session

This section provides an overview of a debug session.

See also:

  * Transaction pane
  * Transaction pane legend
  * Phase details pane



The Debug Tool has two main parts, the transaction pane and the phase details:

  * The transaction pane uses icons to mark each notable step that occurs during an API proxy transaction, including policy execution, conditional steps, and transitions. Hover over any icon to see summary information. The request flow steps appear along the top of the transaction map and response flow steps along the bottom. 
  * The phase details pane lists information about the proxy's internal processing, including variables that were set or read, request and response headers, and much more. Click any icon to see the phase details for that step. 



### Transaction pane

The transaction pane shows the steps in the request and response.

Here's a sample debug tool transaction pane with the main proxy processing segments labeled:

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/debug-session-v2-labeled.png)![Debug diagram showing Begin proxy request to begin target request to begin target
              response to begin proxy response to begin proxy post client flow](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/debug-session-v2-labeled.png)

### Transaction pane legend

The following describes the icons in the transaction pane:

This section describes the icons in the transaction pane: 

  * Policy icons
  * Other icons



### Policy icons

Each type of policy has a unique icon. These icons let you see where policies are executed in the proper order and if they are successful or not. You can click a policy icon to see the results of its execution and if they are expected or not. For example, you can see if the message was transformed properly or if it is being cached. 

Standard policies augment your APIs to control traffic, enhance performance, enforce security, and increase the utility of your APIs, without requiring you to write code or modify backend services. 

Extensible policies let you add custom logic to your API proxies. You can use these policies to add functionality that is not provided by the standard policies. 

See [ Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy) for more information about policies and categories. 

To filter the table: 

  * Select one policy type and/or one policy category.
  * Click the **Name** column header to sort the table by policy name.
  * Type a keyword to search for a policy name.



#### Policy type

Standard Extensible | 

#### Policy category

AI Dialog flow Extension Mediation Security Traffic management  
---|---  
  
Icon | Name | Type | Category  
---|---|---|---  
![LLMTokenQuota policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/icon-quotas.png) | [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) | Extensible | AI  
chat_spark | [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy) | Extensible | AI  
shield_spark | [SanitizeUserPrompt policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy) | Extensible | AI  
shield_spark | [SanitizeModelResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy) | Extensible | AI  
async | [SemanticCacheLookup policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy) | Extensible | AI  
async | [SemanticCachePopulate policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy) | Extensible | AI  
manage_search | [ParseDialogflowRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy) | Extensible | Dialog flow  
chat_add_on | [SetDialogflowResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy) | Extensible | Dialog flow  
stacked_line_chart | [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) | Extensible | Extension  
display_external_input | [ExternalCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy) | Standard | Extension  
flowsheet | [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy) | Extensible | Extension  
automation | [IntegrationCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy) | Extensible | Extension  
![JavaCallout policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/policy_icon_java.png) | [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) | Extensible | Extension  
![JavaScript policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/policy_icon_javascript.png) | [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) | Extensible | Extension  
add_notes | [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) | Extensible | Extension  
chat_paste_go | [PublishMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy) | Standard | Extension  
![PythonScript policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/policy_icon_python.png) | [PythonScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy) | Extensible | Extension  
integration_instructions | [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) | Extensible | Extension  
automation | [SetIntegrationRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-integration-request-policy) | Extensible | Extension  
waterfall_chart | [TraceCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy) | Extensible | Extension  
cloud_done | [AccessEntity policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy) | Extensible | Mediation  
account_tree | [AsseretCondition policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy) | Standard | Mediation  
edit_square | [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) | Extensible | Mediation  
login | [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) | Extensible | Mediation  
![GraphQL policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/policy_icon_graphql.png) | [GraphQL policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy) | Standard | Mediation  
sync_alt | [HTTPModifier policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy) | Standard | Mediation  
sync_alt | [JSONtoXML policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy) | Standard | Mediation  
account_tree | [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) | Extensible | Mediation  
sync_alt | [MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy) | Extensible | Mediation  
cloud_done | [OASValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy) | Standard | Mediation  
report | [RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy) | Standard | Mediation  
sync_alt | [ReadPropertySet policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy) | Standard | Mediation  
cloud_done | [SOAPMessageValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-validation-policy) | Standard | Mediation  
sync_alt | [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) | Standard | Mediation  
cloud_done | [XSLTransform policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) | Extensible | Mediation  
lock | [AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy) | Standard | Security  
security | [BasicAuthentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy) | Extensible | Security  
connect_without_contact | [CORS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy) | Standard | Security  
lock | [DecodeJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/decode-jws-policy) | Extensible | Security  
lock | [DecodeJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/decode-jwt-policy) | Standard | Security  
passkey | [DeleteOAuthV2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/delete-oauth-v2-info) | Extensible | Security  
lock | [GenerateSamlAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy) | Extensible | Security  
lock | [GenerateJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jws-policy) | Extensible | Security  
lock | [GenerateJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy) | Extensible | Security  
passkey | [GetOAuthV2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy) | Extensible | Security  
lock | [HMAC policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/hmac-policy) | Standard | Security  
security | [JSONThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy) | Extensible | Security  
passkey | [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) | Extensible | Security  
security | [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection) | Extensible | Security  
passkey | [RevokeOAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/revoke-oauth-v2-policy) | Extensible | Security  
passkey | [SetOAuthV2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-oauth-v2-info-policy) | Extensible | Security  
lock | [ValidateSamlAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy) | Extensible | Security  
key | [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) | Extensible | Security  
passkey | [VerifyIAM policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-iam-policy) | Extensible | Security  
lock | [VerifyJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jws-policy) | Extensible | Security  
lock | [VerifyJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jwt-policy) | Standard | Security  
security | [XMLThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy) | Extensible | Security  
cached | [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) | Extensible | Traffic management  
cached | [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) | Extensible | Traffic management  
cached | [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy) | Extensible | Traffic management  
![quota policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/icon-quotas2.png) | [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) | Extensible | Traffic management  
repartition | [ResetQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reset-quota-policy) | Extensible | Traffic management  
cached | [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) | Extensible | Traffic management  
emergency_home | [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) | Standard | Traffic management  
  
### Other icons

The following table describes the intent of the other icons you will see in the transaction pane. These icons mark each of the notable processing steps throughout the proxy flow.

To filter the table: 

  * Select one icon type.
  * Click the **Name** column header to sort the table by icon name.
  * Type a keyword to search for an icon name.



#### Icon type

Standard transaction Step status |   
---|---  
  
Icon | Name | Type | Description  
---|---|---|---  
monitor | Client app | Standard transaction |  The client app that sends a request to the ProxyEndpoint of the API proxy.   
circle | Transitional endpoint | Standard transaction |  The circle marks transitional endpoints in the proxy flow. They are there when a request comes in from the client, when the request goes to the target, when the response comes back from the target, and when the response goes back to the client.   
stat_0 | Flow segment | Standard transaction |  The diamond indicates the beginning of a flow segment in the API proxy flow. Flow segments are: ProxyEndpoint request, TargetEndpoint request, TargetEndpoint response, and ProxyEndpoint response. A segment includes the PreFlow, Conditional Flows, and PostFlow.  See [ Conditional flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations) for more information.   
![condition true icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction_icon_condition_true.png) | Conditional flow true | Standard transaction |  A conditional flow that evaluates to true (like an `if` statement that evaluated to `true`). For an introduction to conditional flows, see [ Conditional flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations).  Note that some conditions are Apigee-generated. For example, the following is an expression that Apigee uses to check if an error occurred in the ProxyEndpoint:  `((error.state equals PROXY_REQ_FLOW) or (error.state equals PROXY_RESP_FLOW))`  
![condition false icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction_icon_condition_false.png) | Conditional flow false | Standard transaction |  A conditional flow that evaluates to false. For an introduction to conditional flows, see [ Conditional flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations).  Note that some conditions are Apigee-generated. For example, the following is an expression that Apigee uses to check if an error occurred in the TargetEndpoint:  ` (((error.state equals TARGET_REQ_FLOW) or (error.state equals TARGET_RESP_FLOW)) or ((error.state equals REQ_SENT) or (error.state equals RESP_START))) `  
![flow info icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction_icon_flow_info.png) | Flow info | Standard transaction |  Represents contextual information about the API proxy execution, which varies depending on the point in the flow. This includes details about the proxy configuration, the current execution state (e.g., PreFlow, PostFlow, flow hooks), policy execution details, and variables populated during policy execution, to indicate the specific state of the proxy at that point.   
done_all | Flow execution | Standard transaction |  Marks the beginning or end of a flow's execution, indicating the timeframe of a distinct flow segment, to visually demarcate flow boundaries and indicate the sequence of flow execution.   
commit | Flow processing | Standard transaction |  Indicates active processing within a flow, representing the period during which policies and flow logic are executed.   
bar_chart | Apigee analytics captured data | Standard transaction |  Indicates that Analytics actions have occurred in the background.   
location_on | Backend service | Standard transaction |  Backend service that receives the request. The backend target called by the API proxy.   
![disabled icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction_icon_condition_false.png) | Disabled | Step status |  Appears on a policy icon when a policy is disabled. A policy can be disabled with the public API. See [ API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).   
![error icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction_icon_error.png) | Error | Step status |  Appears on a policy icon when the policy step condition evaluates to false (see [ Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions)), or on the RaiseFault policy icon whenever a RaiseFault policy executes.   
![skipped icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction_icon_skipped.png) | Skipped | Step status |  Appears on a policy icon when the policy was not executed because the step condition evaluated to false. See [ Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions)) for more information.   
  
### Phase details pane

The phase details pane tells you about the state of your proxy at each processing step. 

The phase details pane tells you a lot about the state of your proxy at each processing step. Here are some of the details provided. Click any icon in the debug tool to see details for the selected step, or use the **>** **Next** or **<** **Back** buttons to move from one step to another. 

**Warning:** Debug captures message content. If your message payloads contain sensitive information, then you should enable data masking. For instructions, see [ Masking and hiding data](https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking). 

The following table describes the details provided in the phase details pane. 

**Phase Detail** | **Description**  
---|---  
Variables |  Lists the flow variables that were read and assigned a value by a policy, See also [ Using flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).  **Note:**

  * An equals sign (=) indicates the value that was assigned to the variable. 
  * A crossed-out equals sign (≠) indicates that the variable could not be assigned a value because it is [ read-only](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) or there was an error in policy xecution. 
  * An empty field indicates that the variable value was read. 

  
Request Headers | Lists the HTTP request headers.  
Request Content | Shows the HTTP request body.  
Properties | Properties represent the internal state of the API proxy. These are not shown by default.  
Target Endpoint | Indicates which TargetEndpoint was selected for execution.   
Response Headers | Lists the HTTP response headers.  
Response Content | Shows the HTTP response body.   
  
### Timeline

The timeline indicates how long (in milliseconds) that the processing time took to complete. Comparing the elapsed time segments helps you isolate the policies that are taking the longest to execute that are slowing down your API calls. 

The Epsilon indicates a time-span smaller than a millisecond. 

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/timeline-debug-v2.png)![Timeline in the Debug v2 UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/timeline-debug-v2.png)

### Expanding and collapsing groups

This section describes how to expand and collapse groups in the **Transaction pane**.

Transaction steps, for both request and response, are grouped by how they were configured previously on the **Develop tab** ; by shared flow. For example: pre-proxy, post-proxy, pre-target, and post-target. 

Each grouping clearly displays relevant policies, conditions, shared flows, and flow information. 

Shared flows are grouped and collapsed by default.

The following actions are available in the **Transaction pane** :

Item | Name | Description  
---|---|---  
![expand all slider](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/expand_all_slider.png)  
![collapse all slider](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/collapse_all_slider.png)|  Expand all  
Collapse all | Expand or collapse all groups.  
![expand group icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/expand_group_icon.png)  
![collapse group icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/collapse_group_icon.png) |  Expand  
Collapse | Expand or collapse a group.  
  
See also:

  * [Zoom](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#zoom)
  * [ Selecting view options in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#selecting-view-options-in-the-ui)



### Search

Search allows you to find a word or phrase in the request or response. 

Search allows you to find a word or phrase in the request or response.

Note the following:

  * Search is case-insensitive
  * Search applies to a single transaction; that is, it does not search across all transactions in the entire debug session.
  * Search expands collapsed sections, but does not show information on nodes that are filtered out by [ View Options](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#selecting-view-options-in-the-ui) selections. 



To search:

  1. Type text in the search box. 
  2. Press `Enter`.

The search results are highlighted in the **Transaction pane** and in the **Phase Details** pane. 

  3. Click keyboard_arrow_up **Back** or keyboard_arrow_down **Next** to move to the next or previous step. 

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/search-debug-v2.png)![Search results in the Debug v2 UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/search-debug-v2.png)

### Zoom

Zoom allows you to control the view of the **Transaction pane**. 

Zoom controls the view of the **Transaction pane** as follows:

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/zoom-debug-v2.png)![Debug v2 zoom controls](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/zoom-debug-v2.png)Icon | Description  
---|---  
100% | Current zoom level. Defaults to 100%.  
fit_screen | Fit to screen  
zoom_in | Zoom in  
zoom_out | Zoom out  
youtube_searched_for | Zoom reset  
  
## Debugging with the debug tool

The debug lets you see a lot of internal details about an API proxy. For example:

  * You can see at a glance which policies are executing correctly or failing. 
  * Let's say you noticed through one of the Analytics dashboards that one of your APIs is experiencing an unusual decrease in performance. Now, you can use Debug to help identify where the bottleneck is occurring. Debug gives the time, in milliseconds, that it takes for each processing step to complete. If you find one step is taking too long, you can take corrective action. 
  * You can check headers that are being sent to the backend, view variables set by policies, and so on.
  * By verifying the base path, you can ensure that a policy is routing the message to the correct server.

Note: The debug tool truncates payloads, headers, and flow variables to 10 KB.

## Filtering data in a debug session

When you create a debug session, you can add a filter to that session so that Apigee returns only the data you want. A filter is a conditional statement that Apigee evaluates against request and response messages to determine if its debug data should be included in the debug session. For example, you can filter out all requests with an HTTP response code that is less than 599 or compare values in the request against custom variables.

Note the following: 

  * Requests that are not included in a debug session because they are filtered out do not count towards the [maximum number of transactions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#debug-sessions) in the debug session.
  * Apigee does not support adding filters in the query string.
  * You cannot add a filter to a debug session once the session has started. To add a filter, you must create a debug session.



### Using filters

Use a filter when creating a debug session using the Apigee UI or API, as described in the following sections. 

### Apigee UI

When you create a debug session in the UI, in the **Filters** drop-down list you can choose a predefined filter to apply in the **Start a debug session** panel or choose **Custom Filter** and build your own with the filter syntax.

### API

To create a debug session with a filter using the API, include the following as a payload in your debug session creation request:
    
    
    {
      "filter":"filter_body"
    }

For information on constructing filters, see Filter syntax.

The following example creates a debug session that includes only transactions in which header `A` equals `42` and header `B` equals `43`, or the fault code is `ExpectedEOF`:
    
    
    curl -H "Authorization: Bearer $TOKEN" -X "POST"
      https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/apis/PROXY/revisions/REV/debugsessions
      -d ' {
        "filter":"(request.header.A == '42' && request.header.B == '43') || fault.code == 'jsonparser.ExpectedEOF'"
      } '

You can define a filter in debug session creation requests only; you cannot add a filter to an existing debug session, and you cannot remove a filter from an active debug session.

### Filter syntax 

Filters support the same syntax that is used by Apigee conditions, as described in [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference). This includes:

  * [Grouping](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#structureofconditionalstatements)
  * [Logical AND (`&&`) and OR (`|"`)](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#structureofconditionalstatements)
  * [Path expressions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#pathexpressions)
  * [Operators](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#operators) and [Operands](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#operands)
  * [Literals](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#literals) (`null`, `true`, and `false`)



In addition, filters can access all flow variables that are described in the [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) as well as custom variables. The following examples show just some of the possible flow variables that you can use in filters:
    
    
    # Response codes:
      response.status.code <= 599
      response.status.code >=301 && response.status.code <=420
    
    # Requests/responses:
      request.verb == "GET"
      request.header.A == 'B' || request.queryparam.X == 'Y'
    
    # Query parameters:
      request.queryparam.myparam == 'fish'
      (request.queryparam.param1 == 'X' || request.queryparam.param2 == 'Y') && request.queryparam.param3 == 'Z'
    
    # Faults:
      fault.code != 'messaging.runtime.RouteFailed'
      fault.name == 'IPDeniedAccess'

For information about using custom variables, see [How to use custom attributes in Apigee](https://discuss.google.dev/t/how-to-use-custom-attributes-in-apigee-edge/13234) in the [Apigee Community](https://discuss.google.dev/).

### Predefined UI filters

The Apigee UI provides a set of common filters so that you don't have to write your own custom filters. The predefined filters are as summarized in the following table.

Filter Name | Description  
---|---  
`Response Time Greater Than` | Checks for latency issues where:

  * `target.duration` is the _target latency_ , or the amount of time, in milliseconds, that a request takes to be sent to and received from the target (calculated as the difference between `target.received.end.timestamp` and `target.sent.start.timestamp`)
  * `client.duration` is the _client latency_ , or the amount of time, in milliseconds, that a request takes to be sent to and received from the client (calculated as the difference between `client.received.end.timestamp` and `client.sent.start.timestamp`)

For example:
    
    
    target.duration > 420 && client.duration > 1000

For more information, see `[client](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#client)` and `[target](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#target)` in the [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).  
`Response Code` | Checks if the HTTP response code matches the specified value; for example:
    
    
    response.status.code <= 599

**Tip:** If you are receiving errors, try using `message.status.code` instead of `response.status.code`.  
`Header` | Checks if the specified request header is equal to the specified value; for example:
    
    
    request.header.cache-control.1 == "16544"  
  
`Path` | Checks if the request matches the specified path. You can use wildcard matching in your value; for example:
    
    
    request.path == /myproxy/customer/4*  
  
`Query Param` | Checks if the specified request query parameter is equal to the specified value; for example:
    
    
    request.queryparam.lang == "language:en-us"  
  
`Custom` | Lets you insert your own expressions. You can use any objects in the [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) and the syntax in [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference). In addition, you can use custom variables. For more information about creating custom filters, see Filter syntax.  
  
## Viewing debug sessions

Apigee saves debug session data for **24 hours**. You cannot configure this value; after 24 hours, the data will no longer be available. Before that time, you can view the debug sessions.

**Note** : If you want to save debug session data for future reference, Apigee recommends that you download the debug session. 

To view downloaded debug session data, use the [Offline Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace). 

View recent debug sessions using the Apigee UI or API, as described in the following sections. 

### Apigee UI

To view debug sessions using the Google Cloud console

  1. In the Google Cloud console, go to the **Proxy development > API Proxies** page. 

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click the proxy that you want to debug.
  3. Click the **Debug** tab.
  4. The **Recent debug sessions** displays a list of debug sessions that are available.
  5. Click the link for the session you want to view.




### API

Using the API, you can: 

  * View all debug sessions
  * View all transactions for a debug session
  * View transaction data for a debug session

**Note:** The [Debug session API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions) does not indicate whether a debug session is active.

#### View all debug sessions using the API

To view all recent debug sessions defined for an API proxy revision in an environment, issue a GET request to the following resource: 
    
    
    https://apigee.googleapis.com/v1/organizations/org/environments/env/apis/api/revisions/rev/debugsessions

Optionally, you can specify one of the following query parameters to control the amount of data returned:

  * **pageSize** : Maximum number of debug sessions to list. The page size defaults to 25.
  * **pageToken** : Page token, returned from a previous call, that you can use to retrieve the next page.



The following example demonstrates how to view the debug sessions for revision 1 of the `helloworld` API proxy in the `test` environment.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/myorg/environments/test/apis/helloworld/revisions/1/debugsessions" \
    -X GET \
    -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The response includes a `sessions` object that contains a list of currently active debug sessions, as shown in the following example:
    
    
    {
    "sessions": [
    {
    "id": "a423ac73-0902-4cfa-4242-87a353a84d87",
    "timestamp_ms": 1566330186000
    },
    {
    "id": "f1eccbbe-1fa6-2424-83e4-3d063b47728a",
    "timestamp_ms": 1566330286000
    }
    ]
    }

Only debug sessions that contain at least one transaction are included in the response; debug sessions that do not have any transactions are not included in this list.

For more information, see [List Debug sessions API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list).

#### View all transactions for a debug session using the API

To view a list of transactions for a debug session, issue a GET request to the following resource:
    
    
    https://apigee.googleapis.com/v1/organizations/org/environments/env/apis/api/revisions/rev/debugsessions/debugsession/data

Where debugsession is the ID of a debug session returned when you view debug sessions.

The following example demonstrates how to view the transactions for a debug session for revision 1 of the `helloworld` API in the `test` environment.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/myorg/environments/test/apis/helloworld/revisions/1/debugsessions/a423ac73-0902-4cfa-4242-87a353a84d87/data" \
    -X GET \
    -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The response includes an array of transaction IDs, as shown in the following example:
    
    
    [
    "myorg-test-ver-5qxdb-64",
    "myorg-test-ver-5qxdb-65",
    "myorg-test-ver-5qxdb-66",
    "myorg-test-ver-5qxdb-67",
    "myorg-test-ver-5qxdb-68",
    "myorg-test-ver-5qxdb-69",
    "myorg-test-ver-5qxdb-70",
    "myorg-test-ver-5qxdb-71",
    "myorg-test-ver-5qxdb-72"
    ]
    

For more information, see [List debug session data API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/list).

#### Viewing transaction data for a debug session using the API

To view transaction data for a debug session, issue a GET request to the following resource: 
    
    
    https://apigee.googleapis.com/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/debugsessions/{debugsession}/data/{transactionId}

Where debugsession is the ID of a debug session returned when you view debug sessions and transactionId is the transaction ID returned when you View a list of transactions for a debug session.

You cannot use this API to view an entire sessions' data at one time; to do that, you must use the UI, as described in Downloading debug data.

The transaction data saved during a debug session is formatted in JSON. You can load this data in the [Offline Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace).

The following example demonstrates how to download the transaction data for a debug session for revision 1 of the `helloworld` API in the `test` environment.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/myorg/environments/test/apis/helloworld/revisions/1/debugsessions/a423ac73-0902-4cfa-4242-87a353a84d87/data/myorg-test-ver-5qxdb-64" \
    -X GET \
    -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The response consists of a JSON payload that contains the data for the specified transaction, as described in Download data structure.

Debug data contains all information about the request and response for each part of the flow in a proprietary JSON format. You can save this data and later use it in the [Offline Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace).

If no requests were added to the session before it ended, then the response will look like the following:
    
    
    []

For more information, see [Get debug session data API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/get).

### Selecting view options in the UI

This section describes how to select view options to filter what is shown in the UI.

To choose the view options for the debug session, select or clear options from the **View options** pane. These view options are persisted across debug session for each user. 

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/view-options-v2.png)![view options list](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/view-options-v2.png)Option | Description  
---|---  
Show disabled policies | Show any disabled policies. A policy can be disabled with the public API. See [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).  
Show skipped policies | Show any policies that were skipped. A skipped policy occurs when policy was not executed because the step condition evaluated to false. See [Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions) for more information.   
Show all FlowInfos | Represent transitions within a flow segment.  
Show all flow conditions | Represent the conditions that were evaluated for each flow.  
  
## Share a debug session

You can share a debug session with other users who have access to your organization and the necessary permissions. To do so, just send them the URL displayed in your browser when you are viewing the debug session. The link is only valid for 24 hours after the debug session is created.

## Downloading debug session data

You can download a file of raw debug results for offline viewing. The downloaded file shows the complete details of the debug session including the contents of all headers, variables, and policies.

Debug session data is available to download or view in the UI for 24 hours only. After that point, Apigee deletes the session data.

To view downloaded debug session data, use the [Offline Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace). 

**Note:**

  * You cannot use the Apigee API to view an entire sessions' data at one time; you can only use the API to view individual transaction data, as described in Viewing debug sessions. 
  * Metadata is NOT included when downloading transactions via the Apigee API. It is necessary to manually add metadata in order to upload and view the transaction using [ Offline Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace). 



### Apigee UI

To download the current debug session in the Google Cloud console, click **Download** in the Debug view.

**Note:** A debug session is deleted within 24 hours of the time it is completed, so if you want to view the debug session after that time, you need to download it before then. 

### API

To view the IDs of all transactions for the current debug session using the Apigee API, enter the following command:
    
    
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/apis/PROXY/revisions/REV/debugsessions/SESSION_ID/data

where SESSION_ID is the ID for the debug session you want to download.

See [ List the transaction IDs from a debug session](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/list).

To get the debug data for a transaction using the Apigee API, enter the following command:
    
    
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/apis/PROXY/revisions/REV/debugsessions/SESSION_ID/data/TRANSACTION_ID

### Download data structure

The download structure of the debug session data is different for the Apigee UI and Apigee API.

### Apigee UI

When you download data using the Apigee UI, the data structure:

  * Includes all transactions in the entire session
  * Stores transactions in a `Messages` array
  * Includes metadata about the session (as a `DebugSession` object)



### API

You cannot use the Apigee API to view an entire sessions' data at one time; you can only use the API to view individual transaction data, as described in Viewing debug sessions.

For example:
    
    
    {
    "completed": true,
    "point": [
      ...
    ...
    }

### Download data examples

**Note:** Metadata is NOT included when downloading transactions via the Apigee API. It is necessary to manually add metadata in order to upload and view the transaction using [ Offline Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace). 

The following example highlights a `DebugSession` metadata object in the downloaded data. This object is following by the `Messages` array that contains the transactions in the session.
    
    
    {
    **"DebugSession": {**
    **"Retrieved": "2019-06-08T13:08:13.395Z",**
    **"Organization": "myorg",**
    **"Environment": "prod",**
    **"API": "myproxy",**
    **"Revision": "1",**
    **"SessionId": "a2a271aa-4242-4ac6-97cb-aec8dcb115a9"**
    **},**
      "Messages": [
        {
          "completed": true,
          "point": [
            {
              "id": "Paused"
            },
            {
              "id": "Resumed"
            },
            {
              "id": "StateChange",
              "results": [
                {
                  "ActionResult": "DebugInfo",
                  "properties": {
                    "property": [
                      {
                        "name": "To",
                        "value": "REQ_HEADERS_PARSED"
                      },
                      {
                        "name": "From",
                        "value": "REQ_START"
                      }
                    ]
                  },
                  "timestamp": "8-6-19 13:08:37:718"
                },
                {
                  "ActionResult": "RequestMessage",
                  "headers": [
                    {
                      "name": "accept",
                      "value": "*/*"
                    },
                    {
                      "name": "accept-encoding",
                      "value": "gzip,gzip,deflate,br"
                    },
                    {
                      "name": "content-length",
                      "value": "0"
                    },
                    {
                      "name": "host",
                      "value": "myorg.example.domain.net"
                    },
                    {
                      "name": "user-agent",
                      "value": "Google-Apigee"
                    },
                    {
                      "name": "x-b3-sampled",
                      "value": "0"
                    },
                    {
                      "name": "x-b3-spanid",
                      "value": "d4ee579206759662"
                    },
                    {
                      "name": "x-b3-traceid",
                      "value": "adc1e171777c237dd4ee579206759662"
                    },
                    {
                      "name": "x-forwarded-for",
                      "value": "66.102.8.98"
                    },
                    {
                      "name": "x-forwarded-proto",
                      "value": "https"
                    },
                    {
                      "name": "x-request-id",
                      "value": "54e05cba-4242-4490-4242-60c45c156f90"
                    }
                  ],
                  "uRI": "/myproxy",
                  "verb": "GET"
                }
              ]
            },
            {
              "id": "FlowInfo",
              "results": [
                {
                  "ActionResult": "DebugInfo",
                  "properties": {
                    "property": [
                      {
                        "name": "environment.name",
                        "value": "prod"
                      },
                      {
                        "name": "environment.qualifiedname",
                        "value": "myorg__prod"
                      },
                      {
                        "name": "environment.orgname",
                        "value": "myorg"
                      }
                    ]
                  },
                  "timestamp": "8-6-19 13:08:37:718"
                }
              ]
            },
            {
              "id": "FlowInfo",
              "results": [
                {
                  "ActionResult": "DebugInfo",
                  "properties": {
                    "property": [
                      {
                        "name": "organization.name",
                        "value": "myorg"
                      }
                    ]
                  },
                  "timestamp": "8-6-19 13:08:37:718"
                }
              ]
            },
            {
              "id": "FlowInfo",
              "results": [
                {
                  "ActionResult": "DebugInfo",
                  "properties": {
                    "property": [
                      {
                        "name": "apiproxy.qualifiedname",
                        "value": "myproxy__1"
                      },
                      {
                        "name": "apiproxy.basepath",
                        "value": "/"
                      },
                      {
                        "name": "apiproxy.revision",
                        "value": "1"
                      },
                      {
                        "name": "apiproxy.name",
                        "value": "myproxy"
                      }
                    ]
                  },
                  "timestamp": "8-6-19 13:08:37:718"
                }
              ]
            },
            ...
          ...
        }
      ]
    }

If the debug session did not include any requests, then the `Message` array is empty, as the following example shows:
    
    
    {
      "DebugSession": {
        "Retrieved": "2019-06-08T13:08:13.395Z",
        "Organization": "myorg",
        "Environment": "prod",
        "API": "myproxy",
        "Revision": "1",
        "SessionId": "a2a271aa-4242-4ac6-97cb-aec8dcb115a9"
      },
    **"Messages": []**
    }

## Deleting data for a debug session

Delete data for a debug session using the Apigee UI or API, as described in the following sections. 

### Apigee UI

To delete a debug session in the Google Cloud console:

  1. On the **Debug** tab, click the row for the session you want to delete. 
  2. In the **Debug session** pane, click delete **Delete**.



### API

**Caution:** You cannot delete individual transactions or specific debug sessions from the stored debug data. If you issue a deletion request, you delete all debug sessions and all the data associated with those sessions.

To delete all debug session data using the API, issue a DELETE request to the following resource: 
    
    
    https://apigee.googleapis.com/v1/organizations/org/environments/env/apis/api/revisions/rev/debugsessions/debugsession/data

Where debugsession is the ID of a debug session returned when you view debug sessions. 

The following example demonstrates how to delete debug session data for revision 1 of the `helloworld` API in the `test` environment.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/myorg/environments/test/apis/helloworld/revisions/1/debugsessions/a423ac73-0902-4cfa-4242-87a353a84d87/data" \
          -X DELETE \
          -H "Authorization: Bearer $TOKEN"
        

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

If successful, the response body will be empty. 

Debug session data is persisted for 24 hours only. If you do not explicitly delete it before that time, then Apigee deletes it for you.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
