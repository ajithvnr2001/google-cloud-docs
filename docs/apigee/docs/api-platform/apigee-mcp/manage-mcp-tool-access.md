---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/manage-mcp-tool-access/
title: Manage MCP tool access with API products \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:51.866429+00:00
---

# Manage MCP tool access with API products  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/manage-mcp-tool-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage MCP tool access with API products Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to use Apigee API products to control access to MCP tools. Whether you use the Apigee MCP Discovery Proxy or proxy traffic to your own MCP server, you can authenticate MCP clients, apply per-tool quotas, and filter tool visibility based on API product configuration.

**Note (Apigee hybrid):** All API product, ParsePayload, OAuthV2, VerifyAPIKey, and Quota policy configuration on this page applies identically to Apigee hybrid. Policies are authored on the Apigee control plane and enforced by the Apigee Message Processor in your cluster.

MCP servers use a single endpoint (for example, `/mcp`) for all tool invocations. Unlike REST APIs where operations are distinguished by URL path and HTTP method, MCP embeds the operation in the JSON-RPC request body. Apigee uses the **ParsePayload** policy to extract these operations so that standard API management policies—authentication, quota enforcement, and tool filtering—can be applied on a per-tool basis.

**Note:** This guide assumes you have an API proxy deployed that routes traffic to your MCP server. You can use the [Apigee MCP Discovery Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart) or [create an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy) with your own MCP server as the backend target.

## Overview

To manage MCP tool access with API products, you complete the following steps:

  1. Add the ParsePayload policy to extract the MCP tool name from the request body.
  2. Configure an API product with MCP tool operations and per-tool quotas.
  3. Register a developer app to obtain client credentials.
  4. Add authentication policies (API key or OAuth 2.0) to verify client credentials against the API product.
  5. Add a Quota policy to enforce per-tool rate limits.
  6. Test tool filtering to confirm that `tools/list` responses are filtered based on the API product configuration.



## Add the ParsePayload policy

The **ParsePayload** policy parses the JSON-RPC request body and extracts the MCP operation, such as `tools/call/get_weather` or `tools/list`. The extracted operation is stored in a flow variable prefixed with the policy name (for example, `parsepayload.ParsePayload-MCP.operation`), which downstream policies use for authentication and quota enforcement.

Add the following ParsePayload policy to the request PreFlow of your MCP proxy:
    
    
    <ParsePayload name="ParsePayload-MCP">
        <DisplayName>Parse MCP Payload</DisplayName>
        <Source>request</Source>
        <PayloadType>JSON-RPC-2.0</PayloadType>
        <Protocol>MCP</Protocol>
    </ParsePayload>

Where:

  * `<Source>`: The message to parse. Defaults to `request`.
  * `<PayloadType>`: The payload format. Must be `JSON-RPC-2.0`.
  * `<Protocol>`: The protocol to use for parsing. Must be `MCP` for MCP servers.



After execution, the policy populates flow variables prefixed with the policy instance name, following the pattern `parsepayload.policyName.suffix`. For a policy named `ParsePayload-MCP`, the following variables are set:

Flow variable | Description | Example value  
---|---|---  
`parsepayload.ParsePayload-MCP.operation` | The derived operation name used for API product matching and quota enforcement. | `tools/call/get_weather`  
`parsepayload.ParsePayload-MCP.json-rpc.request.method` | The JSON-RPC `method` field from the request. | `tools/call`  
`parsepayload.ParsePayload-MCP.json-rpc.request.id` | The JSON-RPC `id` field from the request. | `1`  
`parsepayload.ParsePayload-MCP.json-rpc.request.params.name` | The `params.name` field from the request. | `get_weather`  
**Note:** The ParsePayload policy must be placed _before_ any authentication or quota policies in the request PreFlow, because those policies depend on the extracted operation flow variable for API product matching.

## Configure an API product with MCP tool operations

An API product defines which MCP tools a client application can access and the quota limits for each tool. You configure MCP tool operations using the `payloadOperationGroup` field in the API product definition.

Each entry in `payloadOperationGroup.operationConfigs` specifies:

  * The API proxy that serves the MCP tools (`apiSource`).
  * One or more tool operations (for example, `tools/call/get_stock_price`, `tools/list`).
  * An optional quota for that set of operations.

![The API product creation UI showing the Payload Operation panel with API Proxy set to mcp-discovery, Protocol set to MCP, and MCP Operation Type options for List and Call with quota configuration.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/mcp-api-product-payload-operation.png)

Use the following API call to create an API product with MCP tool operations:
    
    
    curl -X POST \
      "https://apigee.googleapis.com/v1/organizations/ORG_NAME/apiproducts" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "PRODUCT_NAME",
        "displayName": "PRODUCT_DISPLAY_NAME",
        "approvalType": "auto",
        "payloadOperationGroup": {
          "operationConfigs": [
            {
              "apiSource": "MCP_PROXY_NAME",
              "operations": [
                { "operation": "tools/call/get_stock_price" },
                { "operation": "tools/call/get_company_news" }
              ],
              "quota": {
                "limit": "100",
                "interval": "1",
                "timeUnit": "minute"
              }
            },
            {
              "apiSource": "MCP_PROXY_NAME",
              "operations": [
                { "operation": "tools/list" }
              ],
              "quota": {
                "limit": "300",
                "interval": "1",
                "timeUnit": "minute"
              }
            }
          ]
        }
      }'

Where:

  * `ORG_NAME` is the name of your Apigee organization.
  * `PRODUCT_NAME` is the internal name of the API product.
  * `PRODUCT_DISPLAY_NAME` is the display name of the API product.
  * `MCP_PROXY_NAME` is the name of the API proxy that routes traffic to your MCP server. This can be an Apigee MCP Discovery Proxy or a proxy with your own MCP server as the backend.



### Configure per-tool quotas

You can configure different quotas for individual tools. For example, the following configuration limits `get_stock_price` to 300 calls per minute but restricts `get_company_news` to only 3 calls per minute:
    
    
    {
      "payloadOperationGroup": {
        "operationConfigs": [
          {
            "apiSource": "MCP_PROXY_NAME",
            "operations": [
              { "operation": "tools/call/get_stock_price" }
            ],
            "quota": { "limit": "300", "interval": "1", "timeUnit": "minute" }
          },
          {
            "apiSource": "MCP_PROXY_NAME",
            "operations": [
              { "operation": "tools/call/get_company_news" }
            ],
            "quota": { "limit": "3", "interval": "1", "timeUnit": "minute" }
          },
          {
            "apiSource": "MCP_PROXY_NAME",
            "operations": [
              { "operation": "tools/list" }
            ],
            "quota": { "limit": "300", "interval": "1", "timeUnit": "minute" }
          }
        ]
      }
    }

**Note:** Include `tools/list` as an operation in your API product if you want the client to be able to discover available tools. If `tools/list` is not included, the client will not be able to list tools through this API product.

You can create multiple API products with different tool subsets to offer tiered access. For example, a _Basic_ product might include only `tools/call/get_stock_price`, while a _Premium_ product includes all available tools with higher quotas. Each developer app is associated with one or more API products, so different clients automatically get access to different sets of tools with independent rate limits.

## Register a developer app

To obtain an API key or OAuth credentials for testing, register a developer and create a developer app associated with the API product you created in the previous step.

  1. [Register an app developer](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product) in your Apigee organization.
  2. [Create a developer app](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api) and associate it with your API product.
  3. [Obtain the consumer key (API key)](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/obtaining-developer-keys) from the app credentials. Use this key in the authentication examples that follow.



## Add authentication policies

After adding the ParsePayload policy, add an authentication policy to verify that the client is authorized to use the requested MCP tool. Apigee matches the extracted operation against the operations defined in the client’s API product.

If the requested tool is not listed in the client’s API product, Apigee returns a `401 Unauthorized` error.

**Note:** Place the authentication policy after the ParsePayload policy and before the Quota policy in the request PreFlow. See Complete proxy configuration for the full policy ordering.

### Option 1: API key authentication

Use the **VerifyAPIKey** policy to authenticate clients using an API key. Add this policy to the request PreFlow after the ParsePayload policy:
    
    
    <VerifyAPIKey name="VerifyAPIKey-1">
        <DisplayName>Verify API Key</DisplayName>
        <APIKey ref="request.queryparam.apikey"/>
    </VerifyAPIKey>

The client passes the API key as a query parameter when calling the MCP proxy:
    
    
    curl -X POST "https://RUNTIME_HOSTNAME/mcp?apikey=API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": { "name": "get_stock_price", "arguments": { "ticker": "GOOGL" } },
        "id": 1
      }'

You can also configure the policy to read the API key from a header:
    
    
    <VerifyAPIKey name="VerifyAPIKey-1">
        <DisplayName>Verify API Key</DisplayName>
        <APIKey ref="request.header.x-api-key"/>
    </VerifyAPIKey>

### Option 2: OAuth 2.0 authentication

Use the **OAuthV2** policy with the `VerifyAccessToken` operation to authenticate clients using OAuth 2.0 access tokens. Add this policy to the request PreFlow after the ParsePayload policy:
    
    
    <OAuthV2 name="OAuthV2-VerifyAccessToken">
        <DisplayName>Verify OAuth Access Token</DisplayName>
        <Operation>VerifyAccessToken</Operation>
    </OAuthV2>

The client passes the access token in the `Authorization` header:
    
    
    curl -X POST "https://RUNTIME_HOSTNAME/mcp" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -d '{
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": { "name": "get_stock_price", "arguments": { "ticker": "GOOGL" } },
        "id": 1
      }'

For more information about configuring OAuth 2.0 in Apigee, see [Getting started with OAuth2](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home).

## Add a Quota policy

Add a **Quota** policy to enforce the per-tool rate limits defined in the API product. The policy uses `UseQuotaConfigInAPIProduct` to automatically apply the quota configuration from the matched API product operation.

**Note:** The Quota policy must appear after both the ParsePayload and the authentication policy in the request PreFlow. See Complete proxy configuration for the full policy ordering.

Add the following Quota policy to the request PreFlow after the authentication policy:
    
    
    <Quota name="Quota-PerToolLimit">
        <DisplayName>Per-Tool Quota</DisplayName>
        <UseQuotaConfigInAPIProduct stepName="AUTH_POLICY_STEP_NAME"/>
        <Distributed>true</Distributed>
    </Quota>

Where `AUTH_POLICY_STEP_NAME` is the value of the `name` attribute in the authentication policy XML element (either `VerifyAPIKey-1` or `OAuthV2-VerifyAccessToken` in the examples on this page). This must match the policy `name` attribute, not the `<DisplayName>`.

With this configuration, each tool operation is rate-limited independently according to the quota defined in the API product. For example, if `tools/call/get_stock_price` has a quota of 300 per minute and `tools/call/get_company_news` has a quota of 3 per minute, each limit is enforced separately even though both tools are accessed through the same proxy.

## Complete proxy configuration

The following example shows the complete request PreFlow configuration for an MCP proxy with ParsePayload, API key authentication, and per-tool quota enforcement:
    
    
    <ProxyEndpoint name="default">
        <PreFlow>
            <Request>
                <Step>
                    <Name>ParsePayload-MCP</Name>
                </Step>
                <Step>
                    <Name>VerifyAPIKey-1</Name>
                </Step>
                <Step>
                    <Name>Quota-PerToolLimit</Name>
                </Step>
            </Request>
        </PreFlow>
        <HTTPProxyConnection>
            <BasePath>/mcp</BasePath>
        </HTTPProxyConnection>
        <RouteRule name="default">
            <TargetEndpoint>default</TargetEndpoint>
        </RouteRule>
    </ProxyEndpoint>

## Tool filtering

When a client sends a `tools/list` request through an MCP proxy with API key or OAuth authentication, Apigee automatically filters the response to include only the tools that are registered in the client’s API product.

For example, if a client’s API product includes the operations `tools/call/get_stock_price` and `tools/call/get_company_news`, a `tools/list` response from the MCP server will be filtered to return only `get_stock_price` and `get_company_news`, even if the MCP server exposes additional tools.

This filtering happens by default when the following configuration is in place. No dedicated filtering policy is required:

  * The request PreFlow includes the ParsePayload and an authentication policy (VerifyAPIKey or OAuthV2).
  * The API product includes `tools/list` in the `payloadOperationGroup`.
  * The API product specifies the tool operations (for example, `tools/call/get_stock_price`) that the client is allowed to access.



To test tool filtering, send a `tools/list` request with the client’s API key:
    
    
    curl -X POST "https://RUNTIME_HOSTNAME/mcp?apikey=API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "jsonrpc": "2.0",
        "method": "tools/list",
        "id": 1
      }'

If the API product includes `tools/call/get_stock_price` and `tools/call/get_company_news`, the filtered response looks similar to the following, even if the MCP server exposes additional tools:
    
    
    {
      "jsonrpc": "2.0",
      "result": {
        "tools": [
          {
            "name": "get_stock_price",
            "description": "Get the current stock price for a given ticker symbol.",
            "inputSchema": {
              "type": "object",
              "properties": {
                "ticker": { "type": "string", "description": "Stock ticker symbol" }
              },
              "required": ["ticker"]
            }
          },
          {
            "name": "get_company_news",
            "description": "Get recent news articles for a company.",
            "inputSchema": {
              "type": "object",
              "properties": {
                "company": { "type": "string", "description": "Company name" }
              },
              "required": ["company"]
            }
          }
        ]
      },
      "id": 1
    }

Tools that are not listed in the API product (for example, `delete_account` or `admin_reset`) are automatically removed from the response.

The following debug session shows the `McpToolsFilterExecution` step in the response flow, with the `mcp_flow_info.mcp.allowed.tools` property listing the tools allowed by the API product:

![Debug session showing the McpToolsFilterExecution step with mcp_flow_info.mcp.allowed.tools listing the filtered tools.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/mcp-tools-filter-debug.png)

## Use conditional flows for per-tool logic

Use conditional flows when you need per-tool logic beyond what API product quotas provide, such as applying tool-specific SpikeArrest rates, routing to different backends, or adding request transformations for specific tools. Conditional flows use the `parsepayload.policyName.operation` flow variable to match on the extracted MCP operation.

For a ParsePayload policy named `ParsePayload-MCP`:
    
    
    <Flows>
        <Flow name="ListTools">
            <Condition>(parsepayload.ParsePayload-MCP.operation = "tools/list")</Condition>
            <Request/>
        </Flow>
        <Flow name="GetStockPrice">
            <Condition>(parsepayload.ParsePayload-MCP.operation = "tools/call/get_stock_price")</Condition>
            <Request>
                <Step>
                    <Name>SpikeArrest-StockPrice</Name>
                </Step>
            </Request>
        </Flow>
        <Flow name="GetCompanyNews">
            <Condition>(parsepayload.ParsePayload-MCP.operation = "tools/call/get_company_news")</Condition>
            <Request>
                <Step>
                    <Name>SpikeArrest-CompanyNews</Name>
                </Step>
            </Request>
        </Flow>
    </Flows>

## Debug the proxy configuration

Use the Apigee [Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) tool to verify that the ParsePayload policy is correctly extracting the MCP operation and that authentication and quota policies are working as expected.

![Debug session showing the ParsePayload-MCP step with flow variables including parsepayload.ParsePayload-MCP.operation set to tools/list.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/mcp-parse-payload-debug.png)

In the debug session, check for the following flow variables after the ParsePayload policy step (where `ParsePayload-MCP` is the policy name):

  * `parsepayload.ParsePayload-MCP.operation`: Should contain the full operation name (for example, `tools/call/get_stock_price`).
  * `parsepayload.ParsePayload-MCP.json-rpc.request.method`: Should contain the JSON-RPC method (for example, `tools/call`).



## Limitations

  * The ParsePayload policy supports only `JSON-RPC-2.0` as the payload type.
  * API product tool operations support only `tools/call` and `tools/list` methods. Tool filtering for `tools/list` responses only applies to `tools/call` operations configured in the API product.
  * The ParsePayload policy parses the full request body. Apigee enforces a default request body size limit of 10 MB, configurable up to 30 MB using the `request.payload.parse.limit` property. For details, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).
  * The ParsePayload policy with MCP protocol parses only JSON-RPC request payloads (containing `method` and `params` fields). MCP response payloads are not parsed.
  * Tool filtering for `tools/list` responses requires the ParsePayload and authentication policies in the request PreFlow.



## What's next

  * Learn more about MCP in Apigee in [MCP in Apigee overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview).
  * Get started with MCP proxies in [Get started with Apigee and MCP](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart).
  * Learn about [API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product) and [managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products).
  * Learn about [rate limiting](https://docs.cloud.google.com/apigee/docs/api-platform/develop/rate-limiting) in Apigee.
  * Learn about [API keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys) and [OAuth 2.0](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home) authentication.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
