---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph/
title: Instrument a LangGraph ReAct agent with OpenTelemetry \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:07.994550+00:00
---

# Instrument a LangGraph ReAct agent with OpenTelemetry  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Instrument a LangGraph ReAct agent with OpenTelemetry Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines the steps to instrument a LangGraph ReAct agent with OpenTelemetry, enabling collecting telemetry from the agent. User prompts and agent responses and choices are included in the telemetry as attributes attached to spans. Agent responses are also included in the log entries that are correlated with spans containing generative AI events. The instructions in this document apply when the agent uses Langchain's ChatVertexAI to call a Gemini model.

Applications that use a LangGraph ReAct agent can also collect multimodal prompts and responses. This document describes how to collect text prompts and responses. If you want to collect multimodal data, then additional configuration is required. For more information, see [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses).

## Instrument your generative AI application to collect telemetry

To instrument your generative AI application to collect log, metric, and trace data, do the following:

  1. Install OpenTelemetry packages
  2. Configure OpenTelemetry to collect and send telemetry
  3. Trace the invocation of the generative AI agent



### Install OpenTelemetry packages

Add the following OpenTelemetry instrumentation and exporter packages:
    
    
    uv add 'opentelemetry-instrumentation-vertexai>=2.0b0' \
      'opentelemetry-instrumentation-sqlite3' \
      'opentelemetry-exporter-otlp-proto-grpc'
    

Log, metric and trace data is sent to Google Cloud by using the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview), which implements the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp). The [`opentelemetry-exporter-otlp-proto-grpc`](https://pypi.org/project/opentelemetry-exporter-otlp-proto-grpc/) library invokes the Telemetry (OTLP) API endpoint.

Your trace data is stored in a format that is generally consistent with the proto files defined by the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp). However, fields might be converted from an OpenTelemetry-specific data type to a JSON data type before storage. To learn more about the storage format, see [Schema for trace data](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/trace-schema).

### Configure OpenTelemetry to collect and send telemetry

Within the initialization code of your LangGraph agent, configure OpenTelemetry to capture and send telemetry to your Google Cloud project:

To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    def setup_opentelemetry() -> None:
        credentials, project_id = google.auth.default()
        resource = Resource.create(
            attributes={
                SERVICE_NAME: "langgraph-sql-agent",
                CLOUD_PROVIDER: "gcp",
                CLOUD_ACCOUNT_ID: project_id,
                # The project to send spans to
                "gcp.project_id": project_id,
                CLOUD_REGION: "us-central1",
                SERVICE_NAMESPACE: "local",
                SERVICE_INSTANCE_ID: "local-instance",
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
    
        logger_provider = LoggerProvider(resource=resource)
        logger_provider.add_log_record_processor(
            BatchLogRecordProcessor(
                OTLPLogExporter(
                    credentials=channel_creds,
                    endpoint="https://telemetry.googleapis.com:443/v1/logs",
                )
            )
        )
        logs.set_logger_provider(logger_provider)
    
        reader = PeriodicExportingMetricReader(
            OTLPMetricExporter(
                credentials=channel_creds,
                endpoint="https://telemetry.googleapis.com:443/v1/metrics",
            )
        )
        meter_provider = MeterProvider(metric_readers=[reader], resource=resource)
        metrics.set_meter_provider(meter_provider)
    
        # Load instrumentors
        SQLite3Instrumentor().instrument()
        GoogleGenAiSdkInstrumentor().instrument()
    
    

### Trace the invocation of the generative AI agent

To trace the execution of the LangGraph agent invocation, create a custom span around the agent invocation:

To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    # Invoke the agent within a span
    with tracer.start_as_current_span("invoke agent"):
        result = agent.invoke({"messages": [prompt]}, config=config)

You might want to include the previous code in key places in your application code.

To learn more about adding custom spans and metrics, see [Add custom traces and metrics to your app](https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/custom-instrumentation).

## Run the sample

This sample is a LangGraph agent instrumented with OpenTelemetry to send traces and logs with generative AI prompts and responses, and metrics to your Google Cloud project.

### LangGraph agent persona

The LangGraph agent is defined as a SQL expert that has full access to an ephemeral SQLite database. The agent is implemented with the [LangGraph prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/agents/agents/#basic-configuration#code) and accesses the database, which is initially empty, using the [SQLDatabaseToolkit](https://python.langchain.com/docs/integrations/tools/sql_database/).

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vertex AI, Service Usage, Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable aiplatform.googleapis.com serviceusage.googleapis.com telemetry.googleapis.com logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Vertex AI, Service Usage, Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable aiplatform.googleapis.com serviceusage.googleapis.com telemetry.googleapis.com logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com

  14. To get the permissions that you need to have the sample application write log, metric, and trace data, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Telemetry Traces Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter) (`roles/telemetry.tracesWriter`)
     * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
     * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
     * [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)

These permissions are sufficient if you run the sample in the Cloud Shell, on Google Cloud resources, or on a local development environment.

**Important** : Production applications typically rely on a service account to provide the credentials required to write log, metric, and trace data. In those scenarios, grant the previous roles to the service account.
  15. Make sure that you specify a quota project. The Vertex AI API (`aiplatform.googleapis.com`) requires that a quota project is specified. For more information, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project). For example, the following command can set a quota project.
         
         gcloud config set billing/quota_project PROJECT_ID




### Run sample

To run the sample, do the following:

  1. In the Cloud Shell, clone the repository:
         
         git clone https://github.com/GoogleCloudPlatform/opentelemetry-samples.git
         

  2. Go to the sample directory:
         
         cd opentelemetry-samples/python/langgraph-sql-agent
         

  3. Configure environment variables:
         
         # Capture GenAI prompts and responses
         export OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true
         # Capture application logs automatically
         export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
         # Set the location to one that supports gemini-3.5-flash
         export GOOGLE_CLOUD_REGION=global
         

If you prefer to use a different model, edit `main.py`. Make sure that your model supports the location you specify. For information about models, see [Google models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models).

  4. Create a virtual environment and run the sample:
         
         uv run main.py
         

The application displays a message similar to the following:
         
         Starting agent using ephemeral SQLite DB.
         

  5. To create a database, enter a value at the **Talk to the SQL agent >>** prompt, and then press **Enter**.

The actions taken by the agent are then displayed on your Cloud Shell.

The following illustrates sample interactions between a user and the application:
         
         Talk to the SQL agent >> Create a new table to hold weather data.
         👤 User: Create a new table to hold weather data.
         🤖 Agent: Okay, I'll create a table to hold weather data. First, I need to decide on the schema for the table. I'll include columns for date, location, temperature, humidity, and precipitation.
         
         CREATE TABLE weather (
           date DATE,
           location VARCHAR(255),
           temperature REAL,
           humidity REAL,
           precipitation REAL
         );
         
         🤖 Agent: I have created the weather table.
         👤 User: Add altitude to the table.
         🤖 Agent
         
         ALTER TABLE weather ADD COLUMN altitude REAL;
         
         

  6. To exit, enter `Ctrl-C`.




The actions performed by generative AI agents aren't deterministic, so you might see a different response for the same prompt.

## View the traces, metrics, and logs

This section describes how can view generative AI events.

### Before you begin

To get the permissions that you need to view your log, metric, and trace data, ask your administrator to grant you the following IAM roles on your project: 

  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### View telemetry

To view the generative AI events, use the **Trace Explorer** page:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

  2. In the toolbar, select **Add filter** , select **Span name** , and then select `invoke agent`.

The Run sample section included an example execution where two prompts are sent to application. The following illustrates the **Trace Explorer** page after filtering the data:

![Display of trace spans.](https://docs.cloud.google.com/static/stackdriver/docs/instrumentation/images/trace-explorer-langgraph.png)

If you've never used Cloud Trace before, then Google Cloud Observability needs to create a database to store your trace data. The creation of the database can take a few minutes and during that period, no trace data is available to view.

  3. To explore your span and log data, in the **Spans** table, select a span.

The **Details** page opens. This page displays the associated trace and its spans. The table on the page displays detailed information for the span you selected. This information includes the following:

     * The **Inputs/Outputs** tab displays events for generative AI agents. To learn more about these events, see [View generative AI events](https://docs.cloud.google.com/trace/docs/finding-traces#view_generative_ai_events).

The following screenshot illustrates a trace, where one span has the name `invoke_agent`. That span invokes Gemini. The Gemini span includes generative AI events:

![Display of generative AI events.](https://docs.cloud.google.com/static/stackdriver/docs/instrumentation/images/trace-explorer-langgraph-ai-events.png)

     * The **Logs & Events** tab lists log entries and events that are associated with the span. If you want to view the log data in the Logs Explorer, then in the toolbar of this tab, select **View logs**.

The log data includes the response of the LangGraph agent. For example, for the sample run, the JSON payload includes the following content:
           
           {
             logName: "projects/my-project/logs/otel_python_inprocess_log_name_temp"
             jsonPayload: {
               message: {
                 role: "model"
                 content: [
                   0: {
                     text: "Okay, I'll create a table to hold weather data. First, I need to decide on the schema for the table. I'll include columns for date, location, temperature, humidity, and precipitation.
           
                     CREATE TABLE weather (
                         date DATE,
                         location VARCHAR(255),
                         temperature REAL,
                         humidity REAL,
                         precipitation REAL
                     );
                     "
                   }
                 ]
               }
             index: 0
             }
           ...
           }
           




The sample is instrumented to send metric data to your Google Cloud project, but it doesn't generate any metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
