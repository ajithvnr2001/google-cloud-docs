---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/deploy-enterprise-gateway/
title: Deploy Google Antigravity Enterprise Gateway \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:17.229948+00:00
---

# Deploy Google Antigravity Enterprise Gateway  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/deploy-enterprise-gateway/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Deploy Google Antigravity Enterprise Gateway Stay organized with collections  Save and categorize content based on your preferences. 

This document shows administrators and security architects how to deploy and configure an enterprise gateway for Google Antigravity.

Enterprise organizations in regulated industries often maintain strict network controls that prevent developer workstations from making direct internet connections to external services or completing interactive browser-based Google sign-in.

Antigravity Enterprise Gateway lets you route Antigravity traffic through an enterprise gateway that your organization operates before forwarding inference requests to Google. This architecture routes model inference requests through your gateway and removes interactive sign-in while preserving your Gemini Enterprise contract billing attribution.

## Overview

When you configure Antigravity Enterprise Gateway, developer workstations communicate with the enterprise gateway instead of connecting directly to Google. Developers authenticate to the gateway with an API key that your gateway issues, so Antigravity doesn't prompt them for individual Google Account sign-in. Your gateway then uses a centralized Google Cloud service account to authenticate and forward Antigravity requests to Google.

**Important:** Antigravity Enterprise Gateway routes inference requests using a centralized Google Cloud service account and is billed on a **pay-as-you-go (PAYG) consumption basis** through the Gemini Enterprise Agent Platform. 

This deployment model **doesn't use your Gemini Enterprise seat-based subscription quotas** (such as included Standard or Plus monthly allowances). You can't use a gateway and sign in with a Google Account at the same time. If you want to use your included subscription quota instead, disable the enterprise gateway and sign in with your Google Account.

Antigravity automatically attaches client attribution headers to identify developer chat prompts and agent workflows. To ensure this model usage is recognized and billed under your organization's existing Gemini Enterprise agreement rather than billed as uncommitted raw API consumption, your gateway must preserve and forward these Antigravity headers to Google:

  * **`User-Agent`** : Antigravity automatically emits an identification header:
        
        User-Agent: antigravity/<var>VERSION</var> (aidev_client; auth_method=gateway)
        

  * **`X-Goog-Api-Client`** : Identifies the Antigravity client runtime and SDK telemetry so Google credits the activity to your licensed enterprise deployment.




## Supported tools and versions

Antigravity Enterprise Gateway supports the following AI developer tools:

Tool | Minimum version | Supported platforms  
---|---|---  
**Antigravity app** | 

  * 2.15.0 or later

| macOS, Windows, and Linux  
**Antigravity CLI (`agy`)** | 

  * 1.2.15 or later

| macOS and Linux  
**Antigravity for IDEs** | 

  * Visual Studio Code and Visual Studio: Antigravity CLI 1.2.15 or later, which the extension downloads and updates automatically. 
  * JetBrains IDEs and Zed (with ACP server): 1.3.0 or later

|  Visual Studio Code, Visual Studio, JetBrains IDEs, and Zed. For more information, see [Antigravity IDE extensions](https://antigravity.google/docs/ide/extensions).   
**Note:** Antigravity on the web doesn't support enterprise gateway routing and requires interactive Google sign-in. To use gateway authentication, use the Antigravity app, CLI, or supported IDE extensions.

## Before you begin

Before you deploy the gateway, verify that you have the following:

  * **Google Cloud project** : A Google Cloud project with access to Gemini Enterprise Agent Platform (formerly Vertex AI) and the Gemini Enterprise Agent Platform API (`aiplatform.googleapis.com`) enabled. Deploying the enterprise gateway doesn't require an invoiced Cloud Billing account. Anyone with access to Gemini Enterprise Agent Platform can use the gateway.
  * **Service account** : A Google Cloud service account in your project that's granted the `roles/aiplatform.user` IAM role. Your gateway uses this service account to authenticate Antigravity requests to Google Cloud.
  * **Data Access audit logs** : To verify billing attribution in Cloud Logging, turn on Data Access audit logs for the Gemini Enterprise Agent Platform API. For more information, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).
  * **Supported client versions** : Developers must use a supported version of each Antigravity tool. For more information, see Supported Antigravity tools.



## Deploy the enterprise gateway

You can host your enterprise gateway using any containerized or managed platform, such as Cloud Run, Envoy, LiteLLM, or Apigee.

Your gateway must satisfy three infrastructure requirements:

  1. **Preserve client attribution headers** : Forward incoming client headers unchanged to Google, including `User-Agent`, `X-Goog-Api-Client`, and any custom headers configured in `gateway.customHeaders` (such as `X-Cost-Center`).

Antigravity clients don't send Google Cloud project information in gateway mode. If your gateway forwards requests to a project other than the project containing the gateway's service account, configure your gateway to inject the `X-Goog-User-Project` header with the target project ID for billing and quota attribution.

  2. **Support unbuffered streaming** : Flush Server-Sent Events (SSE) chunks immediately when processing streaming requests (`:streamGenerateContent?alt=sse`). Don't buffer chunks in the gateway layer.

  3. **Acknowledge telemetry endpoints** : Respond with HTTP `200 OK` (`{}`) to background metric calls (`POST /v1beta:*`), or forward them to your security information and event management (SIEM) system.




### Mandatory request paths

Your gateway must route the following inference paths. Paths are relative to your gateway URL. For example, a streaming request to `https://gateway.cymbal.com` uses `https://gateway.cymbal.com/v1beta/models/<var>MODEL_ID</var>:streamGenerateContent?alt=sse`.

  * **Streaming inference** : `POST /v1beta/models/<var>MODEL_ID</var>:streamGenerateContent?alt=sse`
  * **Unary inference** : `POST /v1beta/models/<var>MODEL_ID</var>:generateContent`



Your gateway must also accept the equivalent full Gemini Enterprise Agent Platform paths:

  * **Streaming inference** : `POST /v1beta1/projects/<var>PROJECT_ID</var>/locations/<var>REGION</var>/publishers/google/models/<var>MODEL_ID</var>:streamGenerateContent?alt=sse`
  * **Unary inference** : `POST /v1beta1/projects/<var>PROJECT_ID</var>/locations/<var>REGION</var>/publishers/google/models/<var>MODEL_ID</var>:generateContent`



Request bodies use the standard `generateContent` JSON schema (`contents`, `generationConfig`, `safetySettings`, and `systemInstruction`).

#### Supported wire protocols

Antigravity Enterprise Gateway supports two wire protocols for inference requests:

  * **Gemini protocol (`genai`)**: The default wire protocol. Antigravity sends inference requests formatted in Google's `generateContent` schema to the `POST /v1beta/models/...` endpoints described previously.
  * **OpenAI wire protocol (`openai`)**: When you set `gateway.wireProtocol` to `openai` (or set `AGY_LLM_GATEWAY_WIRE_PROTOCOL=openai`), Antigravity formats inference requests in the OpenAI Chat Completions protocol and sends them to `POST /v1/chat/completions`.

**Note:** The Antigravity ACP server (used by JetBrains IDEs and Zed) supports only the `genai` wire protocol. If `admin_settings.json` configures `"wireProtocol": "openai"`, JetBrains and Zed sessions fail to connect with an error that `gateway.wireProtocol 'openai' is not supported by the ACP server`.

### Authenticate requests to your gateway

Antigravity authenticates to your gateway with an API key that your gateway issues. Antigravity sends the key from `gateway.apiKey` (or the `AGY_LLM_GATEWAY_API_KEY` environment variable) as a bearer token in the `Authorization` header:
    
    
    Authorization: Bearer <var>GATEWAY_API_KEY</var>
    

Antigravity doesn't obtain Google Cloud credentials, OAuth tokens, or client certificates on behalf of developers. Your gateway must authenticate every request and reject requests that don't present a valid key.

**Caution:** Don't place your gateway behind an authentication layer that reads the `Authorization` header itself, such as Cloud Run IAM invoker checks or Identity-Aware Proxy. These layers expect a Google-signed identity token in that header and reject the gateway API key before the request reaches your gateway.

Because the API key is stored on developer workstations, combine it with network-level controls:

  * **Keep the gateway private** : Expose the gateway only on your corporate network, for example through an internal Application Load Balancer that workstations reach over Cloud VPN or Cloud Interconnect. Don't give the gateway a public endpoint.
  * **Restrict which devices can connect** : Allow connections only from managed workstations, for example by using firewall rules, a zero-trust network access proxy, or device posture checks.
  * **Protect and rotate keys** : Store keys in Secret Manager, validate them on every request, and rotate them regularly. To attribute usage to individual developers, issue a separate key to each developer.



For more information, see Security considerations.

### Connect your gateway to Gemini Enterprise Agent Platform

Your gateway calls the Gemini Enterprise Agent Platform API by using a Google Cloud service account. You can build the gateway on a managed API gateway such as Apigee, or deploy a gateway such as Envoy or LiteLLM on your own infrastructure.

  1. Enable the required APIs:
         
         gcloud services enable \
           aiplatform.googleapis.com \
           secretmanager.googleapis.com \
           --project=<var>PROJECT_ID</var>
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create a service account for the gateway and grant it the `roles/aiplatform.user` role:
         
         gcloud iam service-accounts create <var>SERVICE_ACCOUNT_NAME</var> \
           --project=<var>PROJECT_ID</var> \
           --display-name="Antigravity Enterprise Gateway"
         
         gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
           --member="serviceAccount:<var>SERVICE_ACCOUNT_NAME</var>@<var>PROJECT_ID</var>.iam.gserviceaccount.com" \
           --role="roles/aiplatform.user"
         

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account, such as `agy-gateway-sa`.

  3. Generate a gateway API key, store it in Secret Manager, and let the service account read it:
         
         openssl rand -base64 32 | tr -d '\n' | gcloud secrets create <var>SECRET_NAME</var> \
           --project=<var>PROJECT_ID</var> \
           --data-file=-
         
         gcloud secrets add-iam-policy-binding <var>SECRET_NAME</var> \
           --project=<var>PROJECT_ID</var> \
           --member="serviceAccount:<var>SERVICE_ACCOUNT_NAME</var>@<var>PROJECT_ID</var>.iam.gserviceaccount.com" \
           --role="roles/secretmanager.secretAccessor"
         

Replace `SECRET_NAME` with a name for the secret, such as `agy-gateway-api-key`. You distribute this key to workstations as `gateway.apiKey` in `admin_settings.json`.

  4. Configure your gateway to do the following:

     * Authenticate to Gemini Enterprise Agent Platform as the service account.
     * Read the API key from Secret Manager and reject requests that don't present it.
     * Allow requests to run for at least 60 minutes so that long streaming responses aren't cut off.



To confirm that the gateway works before you configure workstations, see Test the gateway directly.

## Deploy settings using MDM

To configure developer workstations centrally, deploy the `admin_settings.json` configuration file using your mobile device management (MDM) system, such as Jamf, Microsoft Intune, Ansible, or Google Workspace MDM.

Antigravity reads `admin_settings.json` from the following operating system paths:

  * **macOS** : `/Library/Application Support/Antigravity/admin_settings.json`
  * **Linux** : `/etc/antigravity/admin_settings.json`
  * **Windows** : `%ProgramData%\Antigravity\admin_settings.json`



To deploy the settings file, do the following:

  1. Create an `admin_settings.json` file with your gateway URL, API key, and approved models. For an example, see Configuration example.
  2. In your MDM system, create a package, policy, or script that copies the file to the path for each target operating system. Run it with administrator privileges so that the file is owned by an administrator account, and developers can read but not modify it. For example, your MDM script can run the following commands:

### macOS

In a shell, run the following commands as an administrator:
         
         sudo mkdir -p "/Library/Application Support/Antigravity"
         sudo install -m 644 -o root -g wheel admin_settings.json \
         "/Library/Application Support/Antigravity/admin_settings.json"

### Linux

In a shell, run the following commands as an administrator:
         
         sudo install -D -m 644 -o root -g root admin_settings.json \
         /etc/antigravity/admin_settings.json

### Windows

In PowerShell, run the following commands as an administrator:
         
         $dir = Join-Path $env:ProgramData "Antigravity"
         # Remove any folder that a non-admin created first, so they can't keep ownership.
         if (Test-Path $dir) { Remove-Item -Recurse -Force $dir }
         New-Item -ItemType Directory -Path $dir | Out-Null
         # Administrators own the folder; only admins and SYSTEM can write; users can read.
         icacls $dir /setowner "*S-1-5-32-544"
         icacls $dir /inheritance:r /grant:r "*S-1-5-32-544:(OI)(CI)F" "*S-1-5-18:(OI)(CI)F" "*S-1-5-32-545:(OI)(CI)RX"
         Copy-Item admin_settings.json (Join-Path $dir "admin_settings.json")

These commands make the folder and file readable by all users and writable only by administrators.

  3. Assign the package or policy to the devices or device groups that use Antigravity.

  4. Restart Antigravity on the workstations so that it loads the new settings.

  5. To confirm that workstations connect to the gateway, see Verify client connections.




### Settings precedence

Antigravity reads gateway settings from three sources. When the same setting is defined in more than one source, the source with the higher precedence wins:

  1. **Administrator settings file** (highest): `admin_settings.json` deployed by your MDM system.
  2. **Environment variables** : `AGY_LLM_GATEWAY_*` variables set on the workstation. For more information, see [Connect Antigravity to an Enterprise Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/connect-enterprise-gateway).
  3. **User settings file** (lowest): `~/.antigravity/settings.json` in the developer's home folder.



Settings merge field by field. For example, if `admin_settings.json` sets the gateway URL but not the API key, Antigravity uses the API key from an environment variable. Because the administrator settings file has the highest precedence, developers can't override the values that you set in it.

**Note:** The ACP server used by JetBrains IDEs and Zed reads only the administrator settings file and environment variables; it doesn't read user settings from `~/.antigravity/settings.json`.

### Configuration example

The following example `admin_settings.json` file configures Antigravity to route AI traffic through an enterprise gateway at `https://gateway.cymbal.com`, attaches corporate cost-center headers, and restricts model selection to approved models:
    
    
    {
      "gateway": {
        "enabled": true,
        "url": "https://gateway.cymbal.com",
        "apiKey": "<var>GATEWAY_API_KEY</var>",
        "wireProtocol": "genai",
        "customHeaders": {
          "X-Cost-Center": "Platform-Engineering",
          "X-Corporate-BU": "DevTools"
        }
      },
      "caCertPath": "/etc/ssl/certs/cymbal-root-ca.pem",
      "models": {
        "defaultModelId": "gemini-3.8-flash",
        "list": [
          { "modelId": "gemini-3.8-flash" },
          { "modelId": "gemini-3.7-flash" },
          { "modelId": "gemini-3.1-pro-preview" }
        ]
      }
    }
    

This example configuration defines the following settings:

  * `gateway.enabled`: Enables gateway routing mode. When set to `true`, Antigravity sends all inference requests to your gateway instead of sending them directly to Google, and doesn't prompt developers to sign in with a Google Account.
  * `gateway.url`: The HTTPS endpoint of your enterprise gateway (`https://gateway.cymbal.com`).
  * `gateway.apiKey`: The API key (`<var>GATEWAY_API_KEY</var>`) that your gateway requires to authorize requests. Your gateway issues this key, not Google. Antigravity sends it as a bearer token in the `Authorization` header.
  * `gateway.wireProtocol`: The API wire protocol. Supported values are:

    * `genai` (default): Uses the Gemini API protocol (`POST /v1beta/models/...`).
    * `openai`: Uses the OpenAI Chat Completions wire protocol (`POST /v1/chat/completions`).
**Note:** JetBrains IDEs and Zed use the ACP server, which supports only the `genai` wire protocol.
  * `gateway.customHeaders`: Custom HTTP headers (`X-Cost-Center` and `X-Corporate-BU`) that Antigravity adds to each request. Use these headers to attribute usage to teams or cost centers in your gateway logs or SIEM.

  * `caCertPath`: The absolute path to your corporate root certificate authority (CA) bundle. This setting ensures that workstations trust your gateway's internal TLS certificate.

  * `models.defaultModelId`: The model that Antigravity selects by default (such as `gemini-3.8-flash`).

  * `models.list`: The approved models that developers can select in Antigravity. Each entry requires a `modelId` matching a model served by your gateway. For a list of supported Google models, see [Supported models](https://antigravity.google/docs/models).


**Warning:** Antigravity reads the gateway API key as plain text from `admin_settings.json` or the `AGY_LLM_GATEWAY_API_KEY` environment variable. To limit exposure, restrict your gateway to your corporate network, store the key in Secret Manager on the gateway side, and rotate it regularly. To issue per-developer keys instead of a shared key, omit `gateway.apiKey` from `admin_settings.json` and set `AGY_LLM_GATEWAY_API_KEY` on each workstation.

### Security considerations

When you plan your gateway authentication and attribution, consider the following:

  * **Client-supplied headers aren't trusted** : Developers control their own workstations, so they can change headers that are set by environment variables (`AGY_LLM_GATEWAY_HEADERS`) or in the user settings file. Don't rely on these headers for security-critical audit logging or billing attribution.
  * **Pin headers by using MDM** : To prevent developers from overriding attribution or policy headers, define them in `gateway.customHeaders` in `admin_settings.json`. Values in `admin_settings.json` take precedence over environment variables and user settings.
  * **Authenticate at the network or transport layer** : To verify developer identity or enforce strict cost-center attribution, authenticate traffic at the network or transport layer, such as with mutual TLS (mTLS), proxy-level single sign-on (SSO), or network microsegmentation. Don't rely only on the API key or HTTP headers.



## Verify the deployment

Before deploying configuration files to developer workstations, verify that your enterprise gateway routes traffic correctly and that attribution information reaches Cloud Logging.

### Test the gateway directly

Test your enterprise gateway endpoint directly using `curl` before testing on developer workstations. Testing the gateway directly confirms that network routing, TLS certificate validation, authentication, and unbuffered Server-Sent Events (SSE) streaming work independently of Antigravity.

The following example `curl` command sends a streaming request directly to your gateway endpoint:
    
    
    curl -N -X POST "https://gateway.cymbal.com/v1beta/models/<var>MODEL_ID</var>:streamGenerateContent?alt=sse" \
      -H "Authorization: Bearer <var>GATEWAY_API_KEY</var>" \
      -H "Content-Type: application/json" \
      -H "User-Agent: antigravity/1.2.15 (aidev_client; auth_method=gateway)" \
      -d '{"contents": [{"role": "user", "parts": [{"text": "Reply with PONG"}]}]}'
    

In this command:

  * `-N`: Turns off response buffering in `curl` so Server-Sent Events (SSE) stream immediately.
  * `<var>MODEL_ID</var>`: An approved model from your `models.list` (such as `gemini-3.8-flash` or `gemini-3.7-flash`). We recommend testing with a Flash model for initial verification. For a list of available models, see [Supported models](https://antigravity.google/docs/models).
  * `Authorization`: Sends the gateway API key (`<var>GATEWAY_API_KEY</var>`) to authenticate the request with the gateway.
  * `User-Agent`: Sends the client attribution string that Google uses to attribute usage to your Gemini Enterprise agreement.
  * `streamGenerateContent?alt=sse`: Calls the streaming API endpoint for the specified model.



Verify that the gateway streams the response chunks immediately. If you encounter connection errors, certificate warnings, or response buffering delays, see Troubleshooting.

### Verify client connections

Check the client status on a configured workstation:

  * **Antigravity app** : In the bottom status bar, verify that the indicator displays **Connected: Enterprise Gateway**. In **Account Settings** , verify that **Enterprise Gateway Mode Active** is displayed.
  * **Antigravity CLI** : Run a test prompt:
        
        agy -p "Explain binary search in Go"
        

This command sends a test prompt to the gateway. Verify that the response streams in your terminal without displaying an interactive Google sign-in prompt. If the client fails to connect or prompts for Google authentication, see Troubleshooting.




### Verify attribution in Cloud Logging

In the Google Cloud console, verify that attribution headers are received:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

  2. Run the following query:
         
         resource.type="aiplatform.googleapis.com/Endpoint" OR
         protoPayload.serviceName="aiplatform.googleapis.com"
         

  3. Inspect the log entry metadata. Verify that `protoPayload.requestMetadata.callerSuppliedUserAgent` contains `antigravity/<var>VERSION</var> (aidev_client; auth_method=gateway)`.




If no log entries appear, verify that Data Access audit logs are turned on for the Gemini Enterprise Agent Platform API.

## Onboard developers

After you verify the gateway, prepare your developers to use Antigravity:

  * **Managed workstations** : If you deploy `admin_settings.json` using your MDM system, developers don't need to perform any configuration. Antigravity connects to the gateway automatically when started.
  * **Sandboxes and CI/CD pipelines** : For developers working in containerized runners, remote SSH hosts, or non-managed development environments, provide your gateway URL, API key, and root CA path. Direct developers to [Connect Antigravity to an Enterprise Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/connect-enterprise-gateway).



## Troubleshooting

The following table lists common deployment issues and how to resolve them:

Symptom | Cause | Resolution  
---|---|---  
`x509: certificate signed by unknown authority` | The workstation doesn't trust the gateway TLS certificate. | Specify the path to your corporate root CA bundle using `caCertPath` in `admin_settings.json`.  
`401 Unauthorized` or `403 Forbidden` | The API key is invalid or the gateway service account lacks access. | Verify the `gateway.apiKey` value, and verify that the gateway service account has the `roles/aiplatform.user` IAM role on the target project.  
`404 Not Found` | The requested model isn't available on the enterprise gateway, or the model ID is mistyped. | Verify that each model ID configured in `models.list` in `admin_settings.json` matches a model name that your enterprise gateway serves.  
`gateway.wireProtocol 'openai' is not supported by the ACP server` | `admin_settings.json` or an environment variable specifies `openai` wire protocol, which the ACP server does not support. | Set `wireProtocol` to `genai` (or omit it to use the default) for JetBrains IDE and Zed workstations.  
Streaming responses time out | The gateway is buffering HTTP responses. | Configure the gateway to turn off response buffering for Server-Sent Events (`text/event-stream`).  
Antigravity prompts for Google sign-in | Gateway mode isn't turned on, or Antigravity can't find the settings file. | Verify that `admin_settings.json` is deployed to the correct operating system path and contains `"enabled": true` and a `url` in the `gateway` section.  
  
## What's next

  * Learn how developers connect from remote sandboxes: [Connect Antigravity to an Enterprise Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/connect-enterprise-gateway).
  * Learn more about Antigravity features and workflows: [Antigravity documentation](https://antigravity.google/docs).
  * Review developer tools metrics and usage: [View AI developer tools metrics](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics).
  * Configure project security policies: [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
