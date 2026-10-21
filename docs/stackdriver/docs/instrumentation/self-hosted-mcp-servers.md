---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/self-hosted-mcp-servers/
title: Instrument a self-hosted MCP server with OpenTelemetry \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:05.047892+00:00
---

# Instrument a self-hosted MCP server with OpenTelemetry  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/self-hosted-mcp-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Instrument a self-hosted MCP server with OpenTelemetry Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines the steps to instrument and deploy a self-hosted Model Context Protocol (MCP) server, enabling the collection of telemetry. The example in this document builds an MCP server by using [FastMCP](https://gofastmcp.com/getting-started/welcome) and deploys the MCP server using Cloud Run. FastMCP [includes OpenTelemetry instrumentation](https://gofastmcp.com/servers/telemetry) that collects telemetry from all MCP operations.

This document describes the following steps:

  1. Prepare your Python project with the `uv` package manager.
  2. Create an MCP server for math operations.
  3. Deploy to Cloud Run.
  4. Authenticate MCP client.
  5. Test the self-hosted MCP server.
  6. View your telemetry data.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Artifact Registry, Cloud Run, Cloud Build, Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,run.googleapis.com,telemetry.googleapis.com,logging.googleapis.com,monitoring.googleapis.com,trace.googleapis.com)

  7. [Set up your Cloud Run development environment](https://docs.cloud.google.com/run/docs/setup) in your Google Cloud project.
  8. Make sure you have the appropriate [permissions to deploy services](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration), and the [Cloud Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) and [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) roles granted to your account.
  9. Grant the [Cloud Run Invoker (`roles/run.invoker`)](https://docs.cloud.google.com/run/docs/securing/managing-access#invoker) role to your account. This role allows the self-hosted MCP server to access the Cloud Run service.

#### Learn how to grant the roles

#### Console

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address used to deploy the Cloud Run service.

     5. In the **Select a role** list, select a role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

#### gcloud

To grant the required IAM roles to your account on your project:
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=PRINCIPAL \
           --role=ROLE
       

Replace:

     * PROJECT_ID: The identifier of the project.
     * PRINCIPAL: An identifier for the principal that you want to grant the role to. Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the formats that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).
     * ROLE: An IAM role.

  10. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, then you must access your deployed service as described in [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).

  11. Install [Uv](https://docs.astral.sh/uv/getting-started/installation/), a Python package and project manager.



## Prepare your Python project

The following steps describe how to [set up your Python project with the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/).

  1. Create a folder named `mcp-on-cloudrun` to store the source code for deployment:
         
         mkdir mcp-on-cloudrun
           cd mcp-on-cloudrun
         

  2. Create a Python project with the `uv` tool to generate a `pyproject.toml` file:
         
         uv init --name "mcp-on-cloudrun" --description "Example of deploying an MCP server on Cloud Run" --bare --python 3.10
         

The `uv init` command creates the following `pyproject.toml` file:
         
         [project]
         name = "mcp-server"
         version = "0.1.0"
         description = "Example of deploying an MCP server on Cloud Run"
         readme = "README.md"
         requires-python = ">=3.10"
         dependencies = []
         

  3. Create the following additional new files:

     * `server.py` for the MCP server source code.
     * `otel_setup.py` to configure OpenTelemetry.
     * `test_server.py` to test the self-hosted server.
     * A Dockerfile for deploying to Cloud Run.
    
    touch server.py otel_setup.py test_server.py Dockerfile
    

Your project directory should contain the following structure:
    
    ├── mcp-on-cloudrun
    │   ├── pyproject.toml
    │   ├── otel_setup.py
    │   ├── server.py
    │   ├── test_server.py
    │   └── Dockerfile
    




## Create an MCP server for math operations

In this section, you set up a math MCP server with [FastMCP](https://gofastmcp.com/getting-started/welcome). FastMCP provides a quick way to build MCP servers and clients with Python.

Follow these steps to create an MCP server for math operations such as addition and subtraction.

  1. Run the following command to add FastMCP and the required OpenTelemetry dependencies in the `pyproject.toml` file:
         
         uv add fastmcp==3.2.0 opentelemetry-api==1.40.0 opentelemetry-sdk==1.40.0 opentelemetry-exporter-otlp-proto-grpc==1.40.0 --no-sync
         

  2. Add the following OpenTelemetry setup code in the `otel_setup.py` file:
         
         import logging
         import google.auth
         import google.auth.transport.requests
         import grpc
         from google.auth.transport.grpc import AuthMetadataPlugin
         from opentelemetry import trace
         from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
             OTLPSpanExporter,
         )
         from opentelemetry.sdk.resources import SERVICE_NAME, Resource
         from opentelemetry.sdk.trace import TracerProvider
         from opentelemetry.sdk.trace.export import BatchSpanProcessor
         
         logger = logging.getLogger(__name__)
         
         
         def setup_opentelemetry(service_name: str) -> None:
             """Sets up OpenTelemetry to send traces to Google Cloud Observability."""
             credentials, project_id = google.auth.default()
             if not project_id:
                 raise Exception("Could not determine Google Cloud project ID.")
         
             resource = Resource.create(
                 attributes={
                     SERVICE_NAME: service_name,
                     "gcp.project_id": project_id,
                 }
             )
         
             # Set up OTLP auth
             request = google.auth.transport.requests.Request()
             auth_metadata_plugin = AuthMetadataPlugin(credentials=credentials, request=request)
             channel_creds = grpc.composite_channel_credentials(
                 grpc.ssl_channel_credentials(),
                 grpc.metadata_call_credentials(auth_metadata_plugin),
             )
         
             # Set up OpenTelemetry Python SDK
             tracer_provider = TracerProvider(resource=resource)
             tracer_provider.add_span_processor(
                 BatchSpanProcessor(
                     OTLPSpanExporter(
                         credentials=channel_creds,
                         endpoint="https://telemetry.googleapis.com:443/v1/traces",
                     )
                 )
             )
             trace.set_tracer_provider(tracer_provider)
             logger.info("OpenTelemetry successfully initialized.")
         
         

  3. Add the following math MCP server source code in the `server.py` file:
         
         from otel_setup import setup_opentelemetry
         setup_opentelemetry("mcp-server")
         
         import asyncio
         import logging
         import os
         
         from fastmcp import FastMCP 
         
         logger = logging.getLogger(__name__)
         logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)
         
         mcp = FastMCP("MCP Server on Cloud Run")
         
         @mcp.tool()
         def add(a: int, b: int) -> int:
             """Use this to add two numbers together.
         
             Args:
                 a: The first number.
                 b: The second number.
         
             Returns:
                 The sum of the two numbers.
             """
             logger.info(f">>> 🛠️ Tool: 'add' called with numbers '{a}' and '{b}'")
             return a + b
         
         @mcp.tool()
         def subtract(a: int, b: int) -> int:
             """Use this to subtract two numbers.
         
             Args:
                 a: The first number.
                 b: The second number.
         
             Returns:
                 The difference of the two numbers.
             """
             logger.info(f">>> 🛠️ Tool: 'subtract' called with numbers '{a}' and '{b}'")
             return a - b
         
         if __name__ == "__main__":
             logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8080)}")
             # Could also use 'sse' transport, host="0.0.0.0" required for Cloud Run.
             asyncio.run(
                 mcp.run_async(
                     transport="streamable-http",
                     host="0.0.0.0",
                     port=os.getenv("PORT", 8080),
                 )
             )
         

  4. Include the following code in the Dockerfile to use the `uv` tool for running the `server.py` file:
         
         # Use the official Python image
         FROM python:3.14-slim
         
         # Install uv
         COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
         
         # Install the project into /app
         COPY . /app
         WORKDIR /app
         
         # Allow statements and log messages to immediately appear in the logs
         ENV PYTHONUNBUFFERED=1
         
         # Install dependencies
         RUN uv sync
         
         EXPOSE $PORT
         
         # Run the FastMCP server
         CMD ["uv", "run", "server.py"]
         




## Deploy to Cloud Run

You can deploy the MCP server as a [container image](https://docs.cloud.google.com/run/docs/deploying) or as [source code](https://docs.cloud.google.com/run/docs/deploying-source-code):

###  Container image 

To deploy an MCP server packaged as a container image, follow these instructions.

  1. Create an Artifact Registry repository to store the container image:
         
         gcloud artifacts repositories create self-hosted-mcp-servers \
         --repository-format=docker \
         --location=us-central1 \
         --description="Repository for self-hosted MCP servers" \
         --project=PROJECT_ID
         

  2. Build the container image and push it to Artifact Registry with Cloud Build:
         
         gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/PROJECT_ID/self-hosted-mcp-servers/mcp-server:latest
         

  3. Deploy the MCP server container image to Cloud Run:
         
         gcloud run deploy mcp-server \
         --image us-central1-docker.pkg.dev/PROJECT_ID/self-hosted-mcp-servers/mcp-server:latest \
         --region=us-central1 \
         --no-allow-unauthenticated
         




###  Source 

You can deploy self-hosted MCP servers to Cloud Run from their sources.

Deploy from source by running the following command:
    
    
    gcloud run deploy mcp-server --no-allow-unauthenticated --region=us-central1 --source .
    

## Authenticate MCP client

If you deployed your service with the `--no-allow-unauthenticated` flag, any MCP client that connects to your self-hosted MCP server must authenticate.

  1. Grant the [Cloud Run Invoker](https://docs.cloud.google.com/run/docs/securing/managing-access#invoker) (`roles/run.invoker`) role to the service account. This Identity and Access Management policy binding makes sure that a strong security mechanism is used to authenticate your local MCP client.

  2. Run the [Cloud Run proxy](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/proxy) to create an authenticated tunnel to the self-hosted MCP server on your local machine:
         
         gcloud run services proxy mcp-server --region=us-central1
         

If the Cloud Run proxy is not yet installed, this command prompts you to download the proxy. Follow the prompts to download and install the proxy.




Cloud Run authenticates all traffic to `http://127.0.0.1:8080` and forwards requests to the self-hosted MCP server.

## Test the self-hosted MCP server

You test and connect to your self-hosted MCP server by using the FastMCP client and accessing the URL `http://127.0.0.1:8080/mcp`.

To test and invoke the add and subtract mechanism, follow these steps:

  1. Before running the test server, run the Cloud Run proxy.

  2. Create a test file called `test_server.py` and add the following code:
         
         from otel_setup import setup_opentelemetry
         setup_opentelemetry("test-server")
         
         import asyncio
         
         from fastmcp import Client
         
         
         async def test_server():
             # Test the MCP server using streamable-http transport.
             # Use "/sse" endpoint if using sse transport.
             async with Client("http://localhost:8080/mcp") as client:
                 # List available tools
                 tools = await client.list_tools()
                 for tool in tools:
                     print(f">>> 🛠️  Tool found: {tool.name}")
                 # Call add tool
                 print(">>> 🪛  Calling add tool for 1 + 2")
                 result = await client.call_tool("add", {"a": 1, "b": 2})
                 print(f"<<< ✅ Result: {result.content[0].text}")
                 # Call subtract tool
                 print(">>> 🪛  Calling subtract tool for 10 - 3")
                 result = await client.call_tool("subtract", {"a": 10, "b": 3})
                 print(f"<<< ✅ Result: {result.content[0].text}")
         
         
         if __name__ == "__main__":
             asyncio.run(test_server())

  3. In a new terminal, run the test server:
         
         uv run test_server.py
         

You should see the following output:
         
         🛠️ Tool found: add
          🛠️ Tool found: subtract
          🪛 Calling add tool for 1 + 2
          ✅ Result: 3
          🪛 Calling subtract tool for 10 - 3
          ✅ Result: 7
         




## View your telemetry data

This section describes how you can view the log, metric, and trace data your self-hosted MCP server generates.

### Before you begin

To get the permissions that you need to view your log, metric, and trace data, ask your administrator to grant you the following IAM roles on your project: 

  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### View telemetry

To learn about how to view your log, metric, and trace data, see the following:

### Log data

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

For more information about using the **Logs Explorer** page, see [View and analyze logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Metric data

In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

For more information about using the **Metrics Explorer** page, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

### Trace data

In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

The following screenshot illustrates the **Details** pane in the ****Trace Explorer**** page, which displays trace spans generated from `tools/call` operations:

![Details pane showing a trace and its associated spans.](https://docs.cloud.google.com/static/stackdriver/docs/instrumentation/images/trace-explorer-self-hosted-mcp.png)

For more information about using the **Trace Explorer** page, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## What's next

  * Learn how to [investigate MCP calls using Cloud Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * Learn more about the options you have to [view, explore, and analyze your telemetry data](https://docs.cloud.google.com/stackdriver/docs/observability/query-and-view-overview).

  * Learn more about [hosting MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers).

  * Learn how to use an [MCP server to deploy code to Cloud Run](https://github.com/GoogleCloudPlatform/cloud-run-mcp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
