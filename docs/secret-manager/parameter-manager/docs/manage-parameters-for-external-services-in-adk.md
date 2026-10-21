---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/manage-parameters-for-external-services-in-adk/
title: Manage parameters for external services in Agent Development Kit \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:42.490572+00:00
---

# Manage parameters for external services in Agent Development Kit  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/manage-parameters-for-external-services-in-adk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Manage parameters for external services in Agent Development Kit Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manage parameters for external services in Agent Development Kit (ADK).

## Required roles

To get the permissions that you need to configure the integration, ask your administrator to grant you the [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Before you begin

Complete the following prerequisites before you configure the integration.

  1. [Set up an agent with ADK](https://adk.dev/get-started/). This feature requires ADK version `adk-python 1.30` or higher.
  2. Install the ADK extensions package to enable the Parameter Manager integration:
         
         pip install "google-adk[extensions]"
         

  3. Enable the Parameter Manager and Secret Manager APIs:
         
         gcloud services enable parametermanager.googleapis.com secretmanager.googleapis.com
         




## Configure access permissions

To retrieve parameters and resolve secrets at runtime, grant the necessary IAM permissions to your agent identity and parameter resources.

  1. [Create a parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter) and [parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version) in Parameter Manager.

  2. Grant the `Parameter Manager Accessor` role (`roles/parametermanager.parameterAccessor`) to your agent identity. This role allows your agent to render the parameter configuration at runtime.

  3. If your parameter contains embedded secrets, grant the `Secret Manager Secret Accessor` role (`roles/secretmanager.secretAccessor`) to your parameter resource. This cross-service permission allows Parameter Manager to resolve the referenced secrets on behalf of the agent. For more information, see [Grant the Secret Manager Secret Accessor role to the parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter).




## Implementation example

The following code sample demonstrates how to use `ParameterManagerClient` module to retrieve a parameter securely within an ADK agent. The agent retrieves the secrets embedded in parameters internally to prevent exposure of sensitive credentials to the large language model (LLM) context window or conversation history.

**Global parameters**

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    #!/usr/bin/env python
    
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    """
    ADK agent for accessing parameters from global Parameter Manager.
    """
    
    import os
    
    from google.adk import Agent
    from google.adk.integrations.parameter_manager.parameter_client import ParameterManagerClient
    
    # Fetch parameter from global Parameter Manager
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    parameter_id = os.environ.get("ADK_TEST_PARAMETER_ID")
    parameter_version = os.environ.get("ADK_TEST_PARAMETER_VERSION", "latest")
    
    if not project_id or not parameter_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT and ADK_TEST_PARAMETER_ID environment variables must be set.")
    
    resource_name = f"projects/{project_id}/locations/global/parameters/{parameter_id}/versions/{parameter_version}"
    
    print("Fetching parameter from global Parameter Manager...")
    # Initialize Parameter Manager Client
    client = ParameterManagerClient()
    
    # Fetch parameter
    try:
        parameter_payload = client.get_parameter(resource_name)
        print("Successfully fetched parameter.")
    except Exception as e:
        print(f"Error fetching parameter: {e}")
        raise e
    
    # Initialize Agent
    root_agent = Agent(
        model='gemini-2.5-flash',
        name='root_agent',
        description='A helpful assistant for user questions.',
        instruction='Answer user questions to the best of your knowledge',
    )
    
    print("Agent initialized successfully.")
    

**Regional parameters**

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    #!/usr/bin/env python
    
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    """
    ADK agent for accessing parameters from regional Parameter Manager.
    """
    
    import os
    
    from google.adk import Agent
    from google.adk.integrations.parameter_manager.parameter_client import ParameterManagerClient
    
    # Fetch parameter from regional Parameter Manager
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_PROJECT_LOCATION")
    parameter_id = os.environ.get("ADK_TEST_PARAMETER_ID")
    parameter_version = os.environ.get("ADK_TEST_PARAMETER_VERSION", "latest")
    
    if not project_id or not location or not parameter_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_PROJECT_LOCATION, and ADK_TEST_PARAMETER_ID environment variables must be set.")
    
    resource_name = f"projects/{project_id}/locations/{location}/parameters/{parameter_id}/versions/{parameter_version}"
    
    print(f"Fetching parameter from regional Parameter Manager ({location})...")
    # Initialize Parameter Manager Client (Regional)
    client = ParameterManagerClient(location=location)
    
    # Fetch parameter
    try:
        parameter_payload = client.get_parameter(resource_name)
        print("Successfully fetched parameter.")
    except Exception as e:
        print(f"Error fetching parameter: {e}")
        raise e
    
    # Initialize Agent
    root_agent = Agent(
        model='gemini-2.5-flash',
        name='root_agent',
        description='A helpful assistant for user questions.',
        instruction='Answer user questions to the best of your knowledge',
    )
    
    print("Agent initialized successfully.")
    

## Manage regional endpoints

The ADK integration supports diverse infrastructure requirements through both global and regional API endpoints. By default, the client uses the global endpoint (`parametermanager.googleapis.com`). If your architecture requires data residency or regional isolation, you can initialize the client with a specific Google Cloud region (such as `us-central1`). The client then automatically constructs and routes requests to the appropriate regional endpoint (`parametermanager.{location}.rep.googleapis.com`).

## What's next

  * Explore [Agent Development Kit](https://adk.dev/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
