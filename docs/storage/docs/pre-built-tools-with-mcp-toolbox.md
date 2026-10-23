---
url: https://docs.cloud.google.com/storage/docs/pre-built-tools-with-mcp-toolbox/
title: Connect LLMs to Cloud Storage with MCP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:26:50.829824+00:00
---

# Connect LLMs to Cloud Storage with MCP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/pre-built-tools-with-mcp-toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Connect LLMs to Cloud Storage with MCP Stay organized with collections  Save and categorize content based on your preferences. 

You can run a local Model Context Protocol (MCP) server with the [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) to interact with Cloud Storage directly from your IDE and developer tools. This setup lets large language models (LLMs) in clients such as Antigravity, Claude, Cline, Cursor, Visual Studio Code (Copilot), and Windsurf create buckets, manage object data, and inspect Identity and Access Management (IAM) policies.

The open-source MCP Toolbox supports OAuth2 and OIDC authentication, and integrates with OpenTelemetry for observability. Cloud Storage integration requires MCP Toolbox version 1.2.0 or later. To run a standalone local MCP server without the toolbox, use the [Cloud Storage MCP GitHub repository](https://github.com/googleapis/gcloud-mcp/tree/main/packages/storage-mcp).

## Before you begin

  1. In the Google Cloud console, on the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard), select or create a Google Cloud project.

  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  3. [Enable the Cloud Storage API in the Google Cloud project](https://console.cloud.google.com/apis/enableflow?apiid=storage.googleapis.com&redirect=https://console.cloud.google.com/).

  4. Configure the required roles and permissions to complete this task. The user invoking the LLM agents needs the following roles at the bucket or project level:

     * To list buckets, create buckets, and delete empty buckets: **Storage Admin** (`roles/storage.admin`)
     * To list objects, read objects, get object metadata, or bucket metadata: **Storage Object Viewer** (`roles/storage.objectViewer`)
     * To write content to an object or upload an object: **Storage Object Creator** (`roles/storage.objectCreator`)
     * To copy, move, or delete objects: **Storage Object Admin** (`roles/storage.objectAdmin`)
  5. Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) for your environment.




## Connect with Antigravity

You connect Cloud Storage to Antigravity using a custom configuration. In this context, a _custom MCP server_ is a server that you configure manually by editing your configuration file (such as `mcp_config.json`). This manual configuration is used instead of installing the server directly from the built-in MCP Store catalog.

**Note:** You don't need to download the MCP Toolbox binary to use this method.

To configure a custom MCP server, do the following:

  1. Verify that `npx` is installed and properly configured on your system by running `npx --version` in your terminal. If you need to install Node.js, which includes `npx`, see the npm [Downloading and installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) guide.
  2. Open [Antigravity](https://antigravity.google/docs/mcp) and navigate to the MCP store using the **"..."** drop-down at the top of the editor's agent panel.
  3. To open the **mcp_config.json** file, click **MCP Servers** and then click **Manage MCP Servers > View raw config**.
  4. Add the following configuration, replace the placeholder with your project ID, and save: 
         
         {
           "mcpServers": {
             "storage": {
               "command": "npx",
               "args": ["-y","@toolbox-sdk/server","--prebuilt","cloud-storage","--stdio"],
               "env": {
                   "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
               }
             }
           }
         }
         




## Install the MCP Toolbox

The toolbox is an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that runs locally on your machine. The local server manages communication between your IDE and Cloud Storage. This connection provides a secure and efficient environment for your AI tools.

  1. Download the latest version of the MCP Toolbox as a binary. Select the [binary](https://github.com/googleapis/mcp-toolbox/releases) corresponding to your operating system (OS) and CPU architecture. You must use MCP Toolbox version 1.2.0 or later:

### linux/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/linux/amd64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example, `v1.2.0`.

### macOS darwin/arm64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/darwin/arm64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example, `v1.2.0`.

### macOS darwin/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/darwin/amd64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example, `v1.2.0`.

### windows/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/windows/amd64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example, `v1.2.0`.

  2. Make the binary executable:
         
         chmod +x toolbox
         

  3. Verify the installation:
         
         ./toolbox --version
         




To set up the toolbox with a container image or Homebrew, see the [Install Toolbox](https://mcp-toolbox.dev/documentation/introduction/) page.

## Set up clients and connections

This section describes how to connect Cloud Storage to your tools after you install the MCP Toolbox.

### Claude code

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview). 
  2. Create a `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the configuration, replace the placeholders with your values, and save: 
         
         {
                   "mcpServers": {
                     "storage": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-storage","--stdio"],
                       "env": {
                         "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

Replace the following variables with your values: 
     * `./PATH/TO/toolbox`: The path to your `toolbox` binary.
     * `CLOUD_STORAGE_PROJECT`: The environment variable specifying the Google Cloud Project ID.
     * `PROJECT_ID`: Your Google Cloud project ID.
  4. Restart Claude Code to load the new settings. When Claude Code reopens, the application detects the configured MCP server. 



### Claude desktop

  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**. 
  2. In the **Developer** tab, click **Edit Config** to open the configuration file. 
  3. Add the configuration, replace the placeholders with your values, and save: 
         
         {
                   "mcpServers": {
                     "storage": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-storage","--stdio"],
                       "env": {
                         "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

Replace the following variables with your values: 
     * `./PATH/TO/toolbox`: The path to your `toolbox` binary.
     * `CLOUD_STORAGE_PROJECT`: The environment variable specifying the Google Cloud Project ID.
     * `PROJECT_ID`: Your Google Cloud project ID.
  4. Restart Claude Desktop.
  5. The new chat screen displays a hammer (MCP) icon with the new MCP server. 



### Cline

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and click the **MCP Servers** icon. 
  2. Click **Configure MCP Servers** to open the configuration file. 
  3. Add the following configuration, replace the placeholders with your values, and save: 
         
         {
                   "mcpServers": {
                     "storage": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-storage","--stdio"],
                       "env": {
                         "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

Replace the following variables with your values: 
     * `./PATH/TO/toolbox`: The path to your `toolbox` binary.
     * `CLOUD_STORAGE_PROJECT`: The environment variable specifying the Google Cloud Project ID.
     * `PROJECT_ID`: Your Google Cloud project ID.



A green active status appears after the server connects successfully. 

### Cursor

  1. Create the `.cursor` directory in your project root if it doesn't exist. 
  2. Create the `.cursor/mcp.json` file if it doesn't exist and open it. 
  3. Add the following configuration, replace the placeholders with your values, and save: 
         
         {
                   "mcpServers": {
                     "storage": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-storage","--stdio"],
                       "env": {
                         "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

Replace the following variables with your values: 
     * `./PATH/TO/toolbox`: The path to your `toolbox` binary.
     * `CLOUD_STORAGE_PROJECT`: The environment variable specifying the Google Cloud Project ID.
     * `PROJECT_ID`: Your Google Cloud project ID.
  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects. 



### Visual Studio Code (Copilot)

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create a `.vscode` directory in your project root if it does not exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it. 
  3. Add the following configuration, replace the placeholders with your values, and save: 
         
         {
                   "mcpServers": {
                     "storage": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-storage","--stdio"],
                       "env": {
                         "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

Replace the following variables with your values: 
     * `./PATH/TO/toolbox`: The path to your `toolbox` binary.
     * `CLOUD_STORAGE_PROJECT`: The environment variable specifying the Google Cloud Project ID.
     * `PROJECT_ID`: Your Google Cloud project ID.
  4. Reload the VS Code window. The MCP-compatible extension automatically detects the configuration and starts the server. 



### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to the Cascade assistant. 
  2. Click the MCP icon, then click **Configure** to open the configuration file. 
  3. Add the following configuration, replace the placeholders with your values, and save: 
         
         {
                   "mcpServers": {
                     "storage": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-storage","--stdio"],
                       "env": {
                         "CLOUD_STORAGE_PROJECT": "PROJECT_ID"
                       }
                     }
                   }
                 }
                 

Replace the following variables with your values: 
     * `./PATH/TO/toolbox`: The path to your `toolbox` binary.
     * `CLOUD_STORAGE_PROJECT`: The environment variable specifying the Google Cloud Project ID.
     * `PROJECT_ID`: Your Google Cloud project ID.



## Prebuilt tools

After you connect the MCP Toolbox to Cloud Storage, your agent uses the following prebuilt tools:

  * **list_buckets** : Lists Cloud Storage buckets in the configured project.
  * **list_objects** : Lists objects in a bucket with optional prefix and delimiter filtering.
  * **get_bucket_metadata** : Returns metadata for a bucket.
  * **get_bucket_iam_policy** : Returns the IAM policy bindings for a bucket.
  * **get_object_metadata** : Returns metadata for an object.
  * **read_object** : Reads a UTF-8 text object (or byte range). Capped at 8 MiB; binary objects are rejected.
  * **download_object** : Downloads an object to a local path.
  * **create_bucket** : Creates a bucket in the configured project.
  * **delete_bucket** : Deletes an empty bucket.
  * **upload_object** : Uploads a local file to an object.
  * **write_object** : Writes text content directly to an object.
  * **copy_object** : Copies an object to a destination object.
  * **move_object** : Atomically renames an object within the same bucket.
  * **delete_object** : Deletes an object.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
