---
url: https://docs.cloud.google.com/secret-manager/docs/integrate-secret-manager-with-adk/
title: Manage secrets for external services in Agent Development Kit \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:56.201002+00:00
---

# Manage secrets for external services in Agent Development Kit  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/integrate-secret-manager-with-adk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Manage secrets for external services in Agent Development Kit Stay organized with collections  Save and categorize content based on your preferences. 

[Agent Development Kit (ADK)](https://adk.dev/) agents interact with external services outside of Google Cloud. Both [agent identities](https://docs.cloud.google.com/iam/docs/principals-overview#agent-identity) and [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) let you authenticate with Google Cloud services. However, they can't prove identity to external platforms that don't support Google's identity federation.

ADK agents require access to various credentials to interact with external entities such as MCP services, ADK tools, and APIs. Common examples include the following:

  * API keys for payment processing platforms
  * Username and password combinations for legacy on-premises databases
  * Private keys for mutual TLS (mTLS) connections

To support these use cases, ADK provides the `SecretManagerClient` module within the `google.adk.integrations.secret_manager.secret_client` package. This module provides a standard interface for agents to retrieve secrets from Secret Manager at runtime. This document explains how to manage secrets for external services in ADK using Secret Manager. 

## Advantages of using Secret Manager with ADK

Manual secret management can introduce security risks and increase developer toil. Secret Manager can help resolve these issues through the following:

  * If you embed secrets in agent code, you create a significant security risk. This practice can lead to unauthorized access to production systems. Using Secret Manager removes sensitive data from your source code. This helps make your application more secure.
  * If you embed static secrets through environment variables, credential rotation becomes complicated. To apply updates, you must restart deployment containers. Secret Manager retrieves credentials dynamically at runtime, which allows for updates without system downtime.
  * If you write custom `SecretManagerServiceClient` boilerplate code for every tool, you increase developer toil and the risk of errors. The standardized ADK integration provides a clean, reusable approach to retrieve credentials.



## Before you begin

Before you integrate Secret Manager with ADK, complete the following:

  1. [Set up an agent using ADK](https://adk.dev/get-started/). This feature requires [ADK version 1.29 or later](https://github.com/google/adk-python/releases/tag/v1.29.0) for Python.
  2. Grant the [`Secret Manager Secret Accessor`](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor) IAM role to the agent identity. This role allows your agent to retrieve secrets at runtime.
  3. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create-a-secret) and [add a secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version), such as an API key, in Secret Manager.



## How an ADK agent retrieves secrets at runtime

The `secret_client.SecretManagerClient` module retrieves credentials into the Python agent code logic at runtime. The agent orchestration logic sends prompts to the large language model (LLM) to decide which tool to execute, but the system doesn't send the secret to the LLM.

The agent executes the following steps during the runtime phase:

  1. Before an ADK agent invokes a third-party tool, the agent initializes the `SecretManagerClient` module and calls `get_secret()` function.
  2. The ADK agent uses the agent identity to authenticate with Secret Manager.
  3. The `SecretManagerClient` module returns the plaintext secret to the ADK agent.
  4. The ADK agent uses the secret to make an authenticated call to the third-party tool.



## Retrieve secrets within an ADK agent at runtime

The following code sample shows how you can use `SecretManagerClient` module to retrieve a secret securely within an ADK agent. The agent retrieves the secret internally to prevent exposing sensitive credentials to the LLM's context window or conversation history.

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
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
    """
    ADK agent for accessing secrets from global Secret Manager.
    """
    
    import os
    
    from google.adk import Agent
    from google.adk.integrations.secret_manager.secret_client import SecretManagerClient
    
    # Fetch secret from global Secret Manager
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    secret_id = os.environ.get("ADK_TEST_SECRET_ID")
    secret_version = os.environ.get("ADK_TEST_SECRET_VERSION", "latest")
    
    if not project_id or not secret_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT and ADK_TEST_SECRET_ID environment variables must be set.")
    
    resource_name = f"projects/{project_id}/secrets/{secret_id}/versions/{secret_version}"
    
    print("Fetching secret from global Secret Manager...")
    # Initialize Secret Manager Client (Global)
    client = SecretManagerClient()
    
    # Fetch secret
    try:
        secret_payload = client.get_secret(resource_name)
        print("Successfully fetched secret.")
        # The secret_payload can now be used by the agent or its tools as required.
    except Exception as e:
        print(f"Error fetching secret: {e}")
        raise e
    
    # Initialize Agent
    root_agent = Agent(
        model='gemini-2.5-flash',
        name='root_agent',
        description='A helpful assistant for user questions.',
        instruction='Answer user questions to the best of your knowledge',
    )
    
    print("Agent initialized successfully.")
    

## What's next

  * Explore [Agent Development Kit](https://adk.dev/get-started/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
