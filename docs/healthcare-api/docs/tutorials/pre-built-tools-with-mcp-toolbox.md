---
url: https://docs.cloud.google.com/healthcare-api/docs/tutorials/pre-built-tools-with-mcp-toolbox/
title: Use the Cloud Healthcare API with MCP and other agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:33.818311+00:00
---

# Use the Cloud Healthcare API with MCP and other agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/tutorials/pre-built-tools-with-mcp-toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Use the Cloud Healthcare API with MCP and other agents Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to use the [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) to connect the Cloud Healthcare API to a variety of Integrated Development Environments (IDEs) and developer tools. It uses the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open protocol for connecting large language models (LLMs) to data sources like healthcare datasets, allowing you to search and interact with healthcare data directly from your existing tools.

This guide demonstrates the connection process for the following IDEs:

  * Cursor
  * Windsurf (formerly Codeium)
  * Visual Studio Code (Copilot)
  * Cline (VS Code extension)
  * Claude desktop
  * Claude code



## Before you begin

  1. In the Google Cloud console, on the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard), select or create a Google Cloud project.

  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  3. [Enable the Cloud Healthcare API in the Google Cloud project](https://console.cloud.google.com/apis/enableflow?apiid=healthcare.googleapis.com&redirect=https://console.cloud.google.com/).

  4. Configure the required roles and permissions to complete this task. You will need the [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/healthcare/docs/access-control) role (`roles/healthcare.fhirResourceReader`) and the Healthcare DICOM Viewer role (`roles/healthcare.dicomViewer`), or equivalent IAM permissions to connect to the project.

  5. Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) for your environment.




## Install the MCP Toolbox

The toolbox acts as an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that sits between your IDE and the Cloud Healthcare API, providing a secure and efficient control plane for your AI tools.

  1. Download the latest version of the MCP Toolbox as a binary. Select the [binary](https://github.com/googleapis/mcp-toolbox/releases) corresponding to your operating system (OS) and CPU architecture. You must use MCP Toolbox version v0.19.1 or later:

### linux/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/linux/amd64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example `v0.19.1`.

### macOS darwin/arm64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/darwin/arm64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example `v0.19.1`.

### macOS darwin/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/darwin/amd64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example `v0.19.1`.

### windows/amd64
         
         curl -O https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/windows/amd64/toolbox
         

Replace `VERSION` with the MCP Toolbox version—for example `v0.19.1`.

  2. Make the binary executable:
         
         chmod +x toolbox
         

  3. Verify the installation:
         
         ./toolbox --version
         




## Set up clients and connections

This section explains how to connect the Cloud Healthcare API to your tools.

### Claude code

  1. Install [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview). 
  2. Create a `.mcp.json` file in your project root, if it doesn't exist. 
  3. Add the configuration, replace the environment variables with your values, and save: 
         
         {
                   "mcpServers": {
                     "healthcare": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-healthcare","--stdio"],
                       "env": {
                         "HEALTHCARE_PROJECT": "PROJECT_ID",
                         "HEALTHCARE_REGION": "REGION",
                         "HEALTHCARE_DATASET": "DATASET_ID"
                       }
                     }
                   }
                 }
                 

  4. Restart Claude Code to load the new settings. When it reopens, the tool provides an indication that the configured MCP server has been detected. 



### Claude desktop

  1. Open [Claude Desktop](https://claude.ai/download) and navigate to **Settings**. 
  2. In the **Developer** tab, click **Edit Config** to open the configuration file. 
  3. Add the configuration, replace the environment variables with your values, and save: 
         
         {
                   "mcpServers": {
                     "healthcare": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-healthcare","--stdio"],
                       "env": {
                         "HEALTHCARE_PROJECT": "PROJECT_ID",
                         "HEALTHCARE_REGION": "REGION",
                         "HEALTHCARE_DATASET": "DATASET_ID"
                       }
                     }
                   }
                 }
                 

  4. Restart Claude Desktop.
  5. The new chat screen displays a hammer (MCP) icon with the new MCP server. 



### Cline

  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and tap the **MCP Servers** icon. 
  2. Tap **Configure MCP Servers** to open the configuration file. 
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
                   "mcpServers": {
                     "healthcare": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-healthcare","--stdio"],
                       "env": {
                         "HEALTHCARE_PROJECT": "PROJECT_ID",
                         "HEALTHCARE_REGION": "REGION",
                         "HEALTHCARE_DATASET": "DATASET_ID"
                       }
                     }
                   }
                 }
                 




A green active status appears after the server connects successfully. 

### Cursor

  1. Create the `.cursor` directory in your project root if it doesn't exist. 
  2. Create the `.cursor/mcp.json` file if it doesn't exist and open it. 
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
                   "mcpServers": {
                     "healthcare": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-healthcare","--stdio"],
                       "env": {
                         "HEALTHCARE_PROJECT": "PROJECT_ID",
                         "HEALTHCARE_REGION": "REGION",
                         "HEALTHCARE_DATASET": "DATASET_ID"
                       }
                     }
                   }
                 }
                 

  4. Open [Cursor](https://www.cursor.com/) and navigate to **Settings > Cursor Settings > MCP**. A green active status appears when the server connects. 



###  Visual Studio Code (Copilot) 

  1. Open [VS Code](https://code.visualstudio.com/docs/copilot/overview) and create a `.vscode` directory in your project root if it does not exist. 
  2. Create the `.vscode/mcp.json` file if it doesn't exist, and open it. 
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
                   "servers": {
                     "healthcare": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-healthcare","--stdio"],
                       "env": {
                         "HEALTHCARE_PROJECT": "PROJECT_ID",
                         "HEALTHCARE_REGION": "REGION",
                         "HEALTHCARE_DATASET": "DATASET_ID"
                       }
                     }
                   }
                 }
                 

  4. Reload the VS Code window. The MCP-compatible extension automatically detects the configuration and starts the server. 



### Windsurf

  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to the Cascade assistant. 
  2. Click the MCP icon, then click **Configure** to open the configuration file. 
  3. Add the following configuration, replace the environment variables with your values, and save: 
         
         {
                   "mcpServers": {
                     "healthcare": {
                       "command": "./PATH/TO/toolbox",
                       "args": ["--prebuilt","cloud-healthcare","--stdio"],
                       "env": {
                         "HEALTHCARE_PROJECT": "PROJECT_ID",
                         "HEALTHCARE_REGION": "REGION",
                         "HEALTHCARE_DATASET": "DATASET_ID"
                       }
                     }
         
                   }
                 }
                 




> **Note:** The `HEALTHCARE_PROJECT` environment variable specifies the default Google Cloud Project ID for the MCP Toolbox to use. All operations, such as searching for patients or looking up DICOM instances, are run within this project.

## Use the tools

Your AI tool is now connected to the Cloud Healthcare API using MCP. Try asking your AI assistant to search for FHIR patients, retrieve records for a given patient, look up a DICOM study, or list the DICOM stores in the dataset.

The following tools are available to the LLM:

  * **get_dataset** : Retrieves a dataset's details.
  * **list_datasets** : Lists health datasets in a project.
  * **list_fhir_stores** : Lists the FHIR stores in the given dataset.
  * **list_dicom_stores** : Lists the DICOM stores in the given dataset.
  * **get_fhir_store** : Gets the configuration of the specified FHIR store.
  * **get_fhir_store_metrics** : Gets metrics associated with the FHIR store.
  * **get_fhir_resource** : Gets the contents of a FHIR resource.
  * **get_fhir_resource_version** : Gets the contents of a version (current or historical) of a FHIR resource.
  * **fhir_patient_everything** : Retrieves a FHIR Patient resource and resources related to that patient.
  * **fhir_patient_search** : Searches for FHIR patient resources in the FHIR store according to criteria specified.
  * **get_dicom_store** : Gets the configuration of the specified DICOM store.
  * **get_dicom_store_metrics** : Gets metrics associated with the DICOM store.
  * **search_dicom_studies** : Returns a list of matching DICOM studies.
  * **search_dicom_series** : Returns a list of matching DICOM series.
  * **search_dicom_instances** : Returns a list of matching DICOM instances.
  * **retrieve_dicom_instance_rendered** : Returns a base64-encoding of a rendered image in JPEG format for a DICOM instance associated with the given study, series, and SOP Instance UID.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
