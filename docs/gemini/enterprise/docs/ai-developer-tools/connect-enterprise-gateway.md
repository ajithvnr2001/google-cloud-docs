---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/connect-enterprise-gateway/
title: Connect Antigravity to an Enterprise Gateway \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:16.907696+00:00
---

# Connect Antigravity to an Enterprise Gateway  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/connect-enterprise-gateway/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Developer guide ](https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide)



Send feedback 

#  Connect Antigravity to an Enterprise Gateway Stay organized with collections  Save and categorize content based on your preferences. 

This document shows developers using Gemini Enterprise how to connect Google Antigravity to an enterprise gateway from a workstation, container, or developer sandbox.

If your organization enforces strict network controls that block direct internet connections to Google services, Antigravity Enterprise Gateway routes your development requests through an enterprise gateway that your organization operates. This setup lets you use Antigravity without completing interactive browser sign-in. To learn more about Antigravity features, tools, and workflows, see the [Antigravity documentation](https://antigravity.google/docs).

**Note:** Connecting to an enterprise gateway requires an active gateway deployed by your cloud or security team. If you don't have a gateway URL or API key, contact your administrator. For infrastructure setup instructions, refer your platform team to [Deploy Antigravity Enterprise Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/deploy-enterprise-gateway).**Important:** Antigravity Enterprise Gateway routes inference requests using a centralized Google Cloud service account and is billed on a **pay-as-you-go (PAYG) consumption basis** through the Gemini Enterprise Agent Platform. 

This deployment model **doesn't use your Gemini Enterprise seat-based subscription quotas** (such as included Standard or Plus monthly allowances). You can't use a gateway and sign in with a Google Account at the same time. If you want to use your included subscription quota instead, disable the enterprise gateway and sign in with your Google Account.

## Supported tools and versions

Antigravity Enterprise Gateway supports the following AI developer tools:

Tool | Minimum version | Supported platforms  
---|---|---  
**Antigravity app** | 

  * 2.15.0 or later

|  macOS (Apple silicon arm64, Intel x86_64), Windows 10 or 11 (64-bit), Linux (x86_64)   
**Antigravity CLI (`agy`)** | 

  * 1.2.15 or later

| macOS (arm64), Linux (x86_64)  
**Antigravity for IDEs** | 

  * Visual Studio Code and Visual Studio: Antigravity CLI 1.2.15 or later, which the extension downloads and updates automatically. 
  * JetBrains IDEs and Zed (with ACP server): 1.3.0 or later

|  Visual Studio Code, Visual Studio, JetBrains IDEs, and Zed. For more information about IDE extensions, see [Antigravity IDE extensions](https://antigravity.google/docs/ide/extensions).   
**Note:** Antigravity on the web doesn't support enterprise gateway routing and requires interactive Google sign-in. To use gateway authentication, use the Antigravity app, CLI, or supported IDE extensions.

## Choose a configuration method

How you configure Antigravity depends on how your development environment is managed:

  * **Managed corporate workstations** : Your administrator configures Antigravity for you. No manual configuration is required.
  * **Custom environments, containers, and sandboxes** : You configure Antigravity using environment variables. Use this method for remote SSH hosts, development virtual machines, containers, and CI/CD pipelines.



### Managed corporate workstations

If your company manages your computer using a mobile device management (MDM) tool, your administrator deploys an `admin_settings.json` file to your operating system.

When you open the Antigravity app, run the Antigravity CLI, or use Antigravity in supported IDEs (Visual Studio Code, Visual Studio, JetBrains IDEs, and Zed), Antigravity automatically detects these settings and routes requests to the enterprise gateway without displaying individual sign-in prompts. No manual configuration is required.

**Note:** Settings in `admin_settings.json` take precedence over environment variables. If your administrator configured a setting in `admin_settings.json`, you can't override it with an environment variable.

### Custom environments, containers, and sandboxes

If you work in a non-managed environment, such as a remote development virtual machine, a Docker container, an automated CI/CD runner, or a local IDE that isn't managed by MDM, configure Antigravity by setting environment variables or updating your IDE agent configuration.

**Note:** Environment variables set in shell startup files apply to the Antigravity CLI, to Visual Studio Code and Visual Studio (which integrate with the CLI), and to applications started from the same terminal session. Desktop applications and IDEs started from the macOS Dock or Windows Start menu don't read shell profiles. For JetBrains IDEs and Zed, pass environment variables in the IDE's agent server configuration.

The following table describes the environment variables used to configure gateway mode:

Variable | Required | Description  
---|---|---  
`AGY_LLM_GATEWAY_URL` | Yes | The HTTPS URL of your organization's enterprise gateway.  
`AGY_LLM_GATEWAY_API_KEY` | Yes | The API key that your gateway issues. Get this key from your administrator.  
`AGY_LLM_GATEWAY_WIRE_PROTOCOL` | No | The API wire protocol. Set to `genai` (default) for the Gemini API protocol, or `openai` for the OpenAI Chat Completions protocol.  
`AGY_LLM_GATEWAY_CA_CERT` | No | The path to your organization's root CA certificate bundle. If this variable isn't set, Antigravity uses the standard `SSL_CERT_FILE` variable.  
`AGY_LLM_GATEWAY_MODELS` | No | A comma-separated list of allowed models.  
`AGY_LLM_GATEWAY_HEADERS` | No | Custom HTTP headers, in `KEY: VALUE` format, separated by commas or line breaks. Use these headers for cost-center tracking.  
  
#### Configuration examples

The following examples show how to configure Antigravity Enterprise Gateway environment variables for different development environments:

### Interactive shell

The following example shows how to configure gateway environment variables in your shell startup profile (such as `~/.bashrc` or `~/.zshrc`) for interactive terminal sessions and IDE extensions that integrate with the Antigravity CLI (such as Visual Studio Code and Visual Studio):
    
    
    # Configure Antigravity Enterprise Gateway
    export AGY_LLM_GATEWAY_URL="https://gateway.cymbal.com"
    export AGY_LLM_GATEWAY_API_KEY="GATEWAY_API_KEY"
    export AGY_LLM_GATEWAY_WIRE_PROTOCOL="genai"
    export AGY_LLM_GATEWAY_CA_CERT="/etc/ssl/certs/cymbal-root-ca.pem"
    export AGY_LLM_GATEWAY_HEADERS="X-Cost-Center: Platform-Engineering"
    export AGY_LLM_GATEWAY_MODELS="gemini-3.8-flash,gemini-3.7-flash,gemini-3.1-pro-preview"

In this example:

  * `AGY_LLM_GATEWAY_URL`: Sets the HTTPS endpoint of your enterprise gateway (`https://gateway.cymbal.com`).
  * `AGY_LLM_GATEWAY_API_KEY`: Sets the API key (`GATEWAY_API_KEY`) that your gateway requires.
  * `AGY_LLM_GATEWAY_WIRE_PROTOCOL`: Sets the API wire protocol to `genai` (the default) for the Gemini API protocol, or `openai` for the OpenAI Chat Completions protocol.
  * `AGY_LLM_GATEWAY_CA_CERT`: Sets the path to your corporate root CA certificate bundle so that Antigravity trusts your gateway's TLS certificate.
  * `AGY_LLM_GATEWAY_HEADERS`: Adds a custom header that your gateway can use to attribute usage to your team's cost center.
  * `AGY_LLM_GATEWAY_MODELS`: Sets the models that you can select. For more information about available models, see the [list of supported models](https://antigravity.google/docs/models).



To apply the changes, reload your shell profile:
    
    
    source ~/.bashrc

### Docker container

The following example `Dockerfile` configures the gateway connection for containerized development environments and automated CI/CD runners:
    
    
    FROM ubuntu:24.04
    
    # Install prerequisites and Antigravity CLI (v1.2.15 or later)
    RUN apt-get update && apt-get install -y curl ca-certificates
    RUN curl -fsSL https://antigravity.google/cli/install.sh -o /tmp/install.sh \
        && bash /tmp/install.sh \
        && rm -f /tmp/install.sh
    
    # Copy corporate root CA certificate
    COPY certs/cymbal-root-ca.pem /usr/local/share/ca-certificates/cymbal-root-ca.crt
    RUN update-ca-certificates
    
    # Configure gateway connection
    ENV AGY_LLM_GATEWAY_URL="https://gateway.cymbal.com" \
        AGY_LLM_GATEWAY_WIRE_PROTOCOL="genai" \
        AGY_LLM_GATEWAY_CA_CERT="/etc/ssl/certs/cymbal-root-ca.pem" \
        AGY_LLM_GATEWAY_MODELS="gemini-3.8-flash,gemini-3.1-pro-preview"
    
    # Provide API key securely at runtime using container secrets or runtime env
    ENTRYPOINT ["agy"]

In this example:

  * The container image installs the Antigravity CLI and adds the corporate root CA certificate to the system certificate store.
  * Non-sensitive connection settings (`AGY_LLM_GATEWAY_URL`, `AGY_LLM_GATEWAY_WIRE_PROTOCOL`, `AGY_LLM_GATEWAY_CA_CERT`, and `AGY_LLM_GATEWAY_MODELS`) are set as environment variables.
  * The API key (`AGY_LLM_GATEWAY_API_KEY`) isn't stored in the image. Instead, provide it at runtime using container secrets or environment arguments (for example, `docker run -e AGY_LLM_GATEWAY_API_KEY=...`).



### JetBrains IDEs

JetBrains IDEs communicate with Antigravity through the Antigravity Agent Client Protocol (ACP) server. Because desktop IDEs don't read shell startup profiles like `~/.bashrc`, configure gateway settings in the IDE agent configuration:

  1. In `~/.jetbrains/acp.json`, configure the Antigravity agent server with your gateway environment variables:
         
         {
           "agent_servers": {
             "Antigravity": {
               "command": "PATH_TO_ACP_SERVER",
               "env": {
                 "AGY_LLM_GATEWAY_URL": "https://gateway.cymbal.com",
                 "AGY_LLM_GATEWAY_API_KEY": "GATEWAY_API_KEY",
                 "AGY_LLM_GATEWAY_CA_CERT": "/etc/ssl/certs/cymbal-root-ca.pem",
                 "AGY_LLM_GATEWAY_HEADERS": "X-Cost-Center: Platform-Engineering",
                 "AGY_LLM_GATEWAY_MODELS": "gemini-3.8-flash,gemini-3.7-flash,gemini-3.1-pro-preview"
               }
             }
           }
         }

Replace `PATH_TO_ACP_SERVER` with the path to your `agy_acp_server` binary.

  2. In `~/.gemini/antigravity-acp/settings.json` (or `$GEMINI_HOME/antigravity-acp/settings.json` if `GEMINI_HOME` is set), turn on gateway authentication:
         
         {
           "auth": {
             "type": "gateway"
           }
         }

Note: Unlike the Antigravity CLI, setting `AGY_LLM_GATEWAY_URL` alone doesn't turn on gateway routing in the ACP server; setting `"auth": { "type": "gateway" }` is required.

  3. Restart your JetBrains IDE.



### Zed

Zed communicates with Antigravity through the Antigravity Agent Client Protocol (ACP) server. Because desktop IDEs don't read shell startup profiles like `~/.bashrc`, configure gateway settings in Zed's settings file:

  1. In your Zed `settings.json` file, add the Antigravity agent server with your gateway environment variables under `agent_servers`:
         
         {
           "agent_servers": {
             "Antigravity": {
               "command": "PATH_TO_ACP_SERVER",
               "env": {
                 "AGY_LLM_GATEWAY_URL": "https://gateway.cymbal.com",
                 "AGY_LLM_GATEWAY_API_KEY": "GATEWAY_API_KEY",
                 "AGY_LLM_GATEWAY_CA_CERT": "/etc/ssl/certs/cymbal-root-ca.pem",
                 "AGY_LLM_GATEWAY_HEADERS": "X-Cost-Center: Platform-Engineering",
                 "AGY_LLM_GATEWAY_MODELS": "gemini-3.8-flash,gemini-3.7-flash,gemini-3.1-pro-preview"
               }
             }
           }
         }

Replace `PATH_TO_ACP_SERVER` with the path to your `agy_acp_server` binary.

  2. In `~/.gemini/antigravity-acp/settings.json` (or `$GEMINI_HOME/antigravity-acp/settings.json` if `GEMINI_HOME` is set), turn on gateway authentication:
         
         {
           "auth": {
             "type": "gateway"
           }
         }

Note: Unlike the Antigravity CLI, setting `AGY_LLM_GATEWAY_URL` alone doesn't turn on gateway routing in the ACP server; setting `"auth": { "type": "gateway" }` is required.

  3. Restart Zed.



## Verify your connection

After configuring your environment, verify that Antigravity connects to your enterprise gateway:

  1. **Check the Antigravity app** : 
     * In the bottom status bar, verify that the connection status displays **Connected: Enterprise Gateway**.
     * In **Account Settings** , verify that the status displays **Enterprise Gateway Mode Active**.
  2. **Test the Antigravity CLI** : Run a test prompt in your terminal:
         
         agy -p "Explain binary search in Go"
         

The response streams in your terminal without opening a browser window or asking you to sign in with a Google Account.




## Workstation security and local sandboxing

Routing requests through an enterprise gateway doesn't change how Antigravity protects your workstation:

  * **Model requests** : Prompts, context files, and responses route through your organization's enterprise gateway, where your organization can audit them and enforce policies.
  * **Local tool execution** : Terminal commands, file creation, and workspace changes continue to run within Antigravity's local sandbox.
  * **Human-in-the-loop controls** : Antigravity still requires your approval before running potentially destructive terminal commands or changing files on disk.



## Troubleshooting

If you encounter errors when connecting to the gateway, review the following solutions:

Error message | Cause | How to fix  
---|---|---  
`x509: certificate signed by unknown authority` | Your environment doesn't trust the gateway's TLS certificate. | Set `AGY_LLM_GATEWAY_CA_CERT` to the path of your corporate root CA bundle.  
`401 Unauthorized` | The gateway rejected your API key. | Verify that `AGY_LLM_GATEWAY_API_KEY` matches the key provided by your administrator.  
`404 Not Found` | The requested model isn't available on the enterprise gateway, or the model ID is mistyped. | Verify that the model ID in `AGY_LLM_GATEWAY_MODELS` matches a supported model available on your gateway.  
Antigravity prompts for Google sign-in | The gateway URL isn't set in your current shell or IDE configuration. | For terminal sessions and CLI-integrated IDEs, verify that `AGY_LLM_GATEWAY_URL` is set in your current environment. For JetBrains IDEs or Zed, verify that `AGY_LLM_GATEWAY_URL` is passed in the agent `env` block and that `"auth": { "type": "gateway" }` is configured in `~/.gemini/antigravity-acp/settings.json`.  
Error mentioning `AGY_LLM_GATEWAY_URL` in JetBrains or Zed | `auth.type` is set to `gateway` in ACP settings, but the IDE did not pass the variable to the agent server. | Add `AGY_LLM_GATEWAY_URL` to the agent `env` block in `~/.jetbrains/acp.json` (JetBrains) or `settings.json` (Zed), not your shell profile, and restart the IDE.  
`gateway.wireProtocol 'openai' is not supported by the ACP server` | `AGY_LLM_GATEWAY_WIRE_PROTOCOL` or administrator settings specify `openai` wire protocol, which the ACP server does not support. | Set `AGY_LLM_GATEWAY_WIRE_PROTOCOL="genai"` in your environment or ask your administrator to configure `genai` wire protocol for JetBrains and Zed users.  
  
## What's next

  * Learn more about Antigravity features, tools, and workflows: [Antigravity documentation](https://antigravity.google/docs).
  * Explore Gemini Enterprise developer tools capabilities: [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview).
  * Review developer metrics and productivity dashboards: [View AI developer tools metrics](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics).
  * Learn about custom IAM permissions: [Create a custom role to restrict access](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
