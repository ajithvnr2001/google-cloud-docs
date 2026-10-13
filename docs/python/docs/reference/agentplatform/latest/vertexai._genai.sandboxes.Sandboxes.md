---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.sandboxes.Sandboxes
title: Class Sandboxes (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:50.334309+00:00
---

# Class Sandboxes (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.sandboxes.Sandboxes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Sandboxes (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    Sandboxes(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `Sandboxes` class.

## Properties 

### snapshots

API documentation for `snapshots` property.

### templates

API documentation for `templates` property.

## Methods 

### create
    
    
    create(
        *,
        name: str,
        poll_interval_seconds: float = 0.1,
        spec: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.SandboxEnvironmentSpec,
                vertexai._genai.types.common.SandboxEnvironmentSpecDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateAgentEngineSandboxConfig,
                vertexai._genai.types.common.CreateAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineSandboxOperation

Creates a new sandbox in the Agent Engine.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to create sandbox for. projects/{project}/locations/{location}/reasoningEngines/{resource_id}  
`poll_interval_seconds` |  `float`   
Optional. The interval in seconds to poll for sandbox creation completion.  
`spec` |  `SandboxEnvironmentSpec`   
Optional. The specification for the sandbox to create.  
`config` |  `CreateAgentEngineSandboxConfigOrDict`   
Optional. The configuration for the sandbox.  
**Returns**  
---  
**Type** | **Description**  
`AgentEngineSandboxOperation` | The operation for creating the sandbox.  
  
### delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSandboxConfig,
                vertexai._genai.types.common.DeleteAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSandboxOperation

Deletes an agent engine sandbox.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID such as projects/{project}/locations/{location}/reasoningEngines/{resource_id}/SandboxEnvironments/{sandbox_id} or a shortened name such as "reasoningEngines/{resource_id}/sandboxEnvironments/{sandbox_id}".  
`config` |  `DeleteAgentEngineSandboxConfigOrDict`   
Optional. The configuration for the sandbox to delete.  
  
### execute_code
    
    
    execute_code(
        *,
        name: str,
        input_data: dict[str, typing.Any],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ExecuteCodeAgentEngineSandboxConfig,
                vertexai._genai.types.common.ExecuteCodeAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.ExecuteSandboxEnvironmentResponse

Executes code in the Agent Engine sandbox.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine sandbox to run code in. projects/{project}/locations/{location}/reasoningEngines/{resource_id}/SandboxEnvironments/{sandbox_id}  
`input_data` |  `dict[str, Any]`   
Required. The input to the code to execute.  
`config` |  `ExecuteCodeAgentEngineSandboxConfigOrDict`   
Optional. The configuration for the sandboxes to run code in.  
**Returns**  
---  
**Type** | **Description**  
`ExecuteSandboxEnvironmentResponse` | The response from executing the code.  
  
### generate_access_token
    
    
    generate_access_token(service_account_email: str, timeout: int = 3600) -> str

Signs a JWT with a Google Cloud service account.

**Parameters**  
---  
**Name** | **Description**  
`service_account_email` |  `str`   
Required. The email of the service account to use for signing.  
`timeout` |  `int`   
Optional. The timeout in seconds for the token. Defaults to 3600.  
**Returns**  
---  
**Type** | **Description**  
`str` | The signed JWT.  
  
### generate_browser_ws_headers
    
    
    generate_browser_ws_headers(
        sandbox_environment: vertexai._genai.types.common.SandboxEnvironment,
        service_account_email: str,
        port: str = "8080",
        timeout: int = 3600,
        psc_endpoint: typing.Optional[str] = None,
    ) -> tuple[str, dict[str, str]]

Generates the websocket upgrade headers for the browser.

**Parameters**  
---  
**Name** | **Description**  
`sandbox_environment` |  `types.SandboxEnvironment`   
Required. The sandbox environment to generate websocket headers for.  
`service_account_email` |  `str`   
Required. The email of the service account to use for signing.  
`port` |  `str`   
Optional. The port to use for the CDP websocket endpoint url fetching. Defaults to "8080". This should be one of the ports specified during template creation.  
`timeout` |  `int`   
Optional. The timeout in seconds for the token. Defaults to 3600.  
`psc_endpoint` |  `str`   
Optional. Host (RFC1918 IP or resolvable internal hostname) of the customer-side PSC endpoint forwarding rule that targets `connection_info.service_attachment`. Needed for VPC-SC sandboxes; see `send_command` for details. When provided, it is used as the websocket host in place of the load balancer address, and is propagated to the internal `send_command` call that fetches the CDP endpoint.  
**Returns**  
---  
**Type** | **Description**  
`tuple[str, dict[str, str]]` | A tuple containing the websocket URL and the headers for websocket upgrade.  
  
### get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSandboxConfig,
                vertexai._genai.types.common.GetAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.SandboxEnvironment

Gets an agent engine sandbox.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. A fully-qualified resource name or ID such as projects/{project}/locations/{location}/reasoningEngines/{resource_id}/SandboxEnvironments/{sandbox_id} or a shortened name such as "reasoningEngines/{resource_id}/sandboxEnvironments/{sandbox_id}".  
`config` |  `GetAgentEngineSandboxConfigOrDict`   
Optional. The configuration for the sandbox to get.  
  
### list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSandboxesConfig,
                vertexai._genai.types.common.ListAgentEngineSandboxesConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.SandboxEnvironment]

Lists Agent Engine sandboxes.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the agent engine to list sandboxes for. projects/{project}/locations/{location}/reasoningEngines/{resource_id}/SandboxEnvironments/{sandbox_id}  
`config` |  `ListAgentEngineSandboxConfig`   
Optional. The configuration for the sandboxes to list.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[SandboxEnvironment]` | An iterable of agent engine sandboxes.  
  
### send_command
    
    
    send_command(
        *,
        http_method: str,
        access_token: str,
        sandbox_environment: vertexai._genai.types.common.SandboxEnvironment,
        port: str = "8080",
        path: typing.Optional[str] = None,
        query_params: typing.Optional[dict[str, object]] = None,
        headers: typing.Optional[dict[str, str]] = None,
        request_dict: typing.Optional[dict[str, object]] = None,
        psc_endpoint: typing.Optional[str] = None
    ) -> google.genai.types.HttpResponse

Sends a command to the sandbox.

**Parameters**  
---  
**Name** | **Description**  
`http_method` |  `str`   
Required. The HTTP method to use for the command.  
`access_token` |  `str`   
Required. The access token to use for authorization.  
`sandbox_environment` |  `types.SandboxEnvironment`   
Required. The sandbox environment to send the command to.  
`port` |  `str`   
Optional. The port to use for the token. Defaults to "8080". This should be one of the ports specified during template creation.  
`path` |  `str`   
Optional. The path to send the command to.  
`query_params` |  `dict[str, object]`   
Optional. The query parameters to include in the command.  
`headers` |  `dict[str, str]`   
Optional. The headers to include in the command.  
`request_dict` |  `dict[str, object]`   
Optional. The request body to include in the command.  
`psc_endpoint` |  `str`   
Optional. Host (RFC1918 IP or resolvable internal hostname) of the customer-side PSC endpoint forwarding rule that targets `connection_info.service_attachment`. Needed for VPC-SC sandboxes (`ingressControlConfig.enablePrivateServiceConnect=true`) where `connection_info.load_balancer_hostname` and `load_balancer_ip` are both unset because ingress goes through PSC in the customer's VPC rather than a Google-managed load balancer. When provided, it is used as the data-plane host in place of the load balancer address.  
**Returns**  
---  
**Type** | **Description**  
`genai_types.HttpResponse` | The response from the sandbox.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
