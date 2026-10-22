---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/python/
title: Python instrumentation sample \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:39.190658+00:00
---

# Python instrumentation sample  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Python instrumentation sample Stay organized with collections  Save and categorize content based on your preferences. 

You can instrument a Python application to collect trace and metric data with the [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) SDK and an OpenTelemetry collector and to write correlated, structured JSON logs to standard output. To experiment with this instrumentation, you can download and run the sample [Flask](https://flask.palletsprojects.com/en/3.0.x/) application, which generates log, metric, and trace data and exports it to your Google Cloud project. 

## About the instrumentation approach

When you use an OpenTelemetry collector, you instrument your application with the SDK and the SDK's OTLP in-process exporter. This instrumentation is vendor neutral. You also deploy an OpenTelemetry collector that receives telemetry from the in-process exporter and then exports that telemetry to your Google Cloud project. To learn more about collectors, see [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).

We recommend that you use an OpenTelemetry collector to export your telemetry data when your environment supports the use of a collector. For some environments, you must use an in-process exporter that directly sends data to your Google Cloud project. To learn about in-process instrumentation, see [Migrate from the Trace exporter to the OTLP endpoint](https://docs.cloud.google.com/stackdriver/docs/instrumentation/migrate-to-otlp-endpoints).

To learn more about instrumentation, see the following documents:

  * [Observability for application developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/application-developers)
  * [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)



## About manual and zero-code instrumentation

For this language, OpenTelemetry defines _zero-code instrumentation_ as the practice of collecting telemetry from libraries and frameworks without making code changes. However, you do have to install modules and set environment variables.

This document doesn't describe zero-code instrumentation. For information about that topic, see [Python zero-code instrumentation](https://opentelemetry.io/docs/languages/python/automatic/).

For general information, see [OpenTelemetry Instrumentation for Python](https://opentelemetry.io/docs/languages/python/instrumentation/).

## Before you begin

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

  7. Enable the Cloud Logging, Cloud Monitoring, Cloud Trace, and Telemetry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com telemetry.googleapis.com

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

  13. Enable the Cloud Logging, Cloud Monitoring, Cloud Trace, and Telemetry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com telemetry.googleapis.com

  14. To get the permissions that you need to have the sample application write log, metric, and trace data, ask your administrator to grant you the following IAM roles: 

     * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on your project
     * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on your project
     * [Cloud Telemetry Traces Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter) (`roles/telemetry.tracesWriter`) on your project
     * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your quota project

These permissions are sufficient if you run the sample in the Cloud Shell, on Google Cloud resources, or on a local development environment. To learn how to configure a quota project, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project).

**Important** : Production applications typically rely on a service account to provide the credentials required to write log, metric, and trace data. In those scenarios, grant the previous roles to the service account.

To get the permissions that you need to view your log, metric, and trace data, ask your administrator to grant you the following IAM roles on your project: 

     * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
     * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
     * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Instrument your app to collect traces, metrics, and logs

**Note:** This document displays only selected portions of a working application. For example, the sample doesn't display the list of imported packages. However, the full application is available on GitHub. To view the full sample, in the sample's toolbar, select the GitHub logo.

To instrument your app to collect trace and metric data and to write structured JSON logs to standard output, perform the following steps:

  1. Configure OpenTelemetry
  2. Configure structured logging



### Configure OpenTelemetry

This example app is configured to use the OpenTelemetry Python SDK to export traces and metrics by using the [OTLP protocol](https://opentelemetry.io/docs/specs/otlp/). By default, the OpenTelemetry Python SDK uses the [W3C Trace Context](https://www.w3.org/TR/trace-context/) format for [propagating trace context](https://opentelemetry.io/docs/concepts/context-propagation/#propagation), which ensures that spans have the correct parent-child relationship within a trace.

The following code sample illustrates a Python module to set up OpenTelemetry. To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    def setup_opentelemetry() -> None:
        resource = Resource.create(
            attributes={
                # Use the PID as the service.instance.id to avoid duplicate timeseries
                # from different Gunicorn worker processes.
                SERVICE_INSTANCE_ID: f"worker-{os.getpid()}",
            }
        )
        # Set up OpenTelemetry Python SDK
        tracer_provider = TracerProvider(resource=resource)
        tracer_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
        trace.set_tracer_provider(tracer_provider)
    
        logger_provider = LoggerProvider(resource=resource)
        logger_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter()))
        logs.set_logger_provider(logger_provider)
    
        reader = PeriodicExportingMetricReader(OTLPMetricExporter())
        meter_provider = MeterProvider(metric_readers=[reader], resource=resource)
        metrics.set_meter_provider(meter_provider)
    
    

The Flask app relies on [Gunicorn](https://gunicorn.org/) to serve HTTP requests following the recommendations in Flask's [Deploying to Production](https://flask.palletsprojects.com/en/3.0.x/deploying/) guide. Gunicorn starts multiple copies of your app running in independent worker processes to increase throughput. To ensure that metrics from the worker processes don't conflict with each other, we recommend that each worker process sets a unique value for the `service.instance.id` resource attribute. One way to do this is by including the process ID in the `service.instance.id`. For more information, see [Time-series collisions](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#timeseries-collisions).

For more information and configuration options, see [OpenTelemetry Python instrumentation](https://opentelemetry.io/docs/languages/python/exporters/).

### Configure structured logging

To write structured logs that are linked to traces, configure your app to output JSON-formatted logs to standard output with keys containing trace information. The following code sample illustrates how to configure the standard [`logging`](https://docs.python.org/3/library/logging.html) library to output JSON structured logs using the [`python-json-logger`](https://pypi.org/project/python-json-logger/) library and how to use the [`opentelemetry-instrumentation-logging`](https://pypi.org/project/opentelemetry-instrumentation-logging/) package to include trace information.
    
    
    class JsonFormatter(jsonlogger.JsonFormatter):
        def formatTime(self, record: logging.LogRecord, datefmt: Optional[str] = None):
            # Format the timestamp as RFC 3339 with microsecond precision
            isoformat = datetime.fromtimestamp(record.created).isoformat()
            return f"{isoformat}Z"
    
    
    def setup_structured_logging() -> None:
        LoggingInstrumentor().instrument()
    
        log_handler = logging.StreamHandler()
        formatter = JsonFormatter(
            "%(asctime)s %(levelname)s %(message)s %(otelTraceID)s %(otelSpanID)s %(otelTraceSampled)s",
            rename_fields={
                "levelname": "severity",
                "asctime": "timestamp",
                "otelTraceID": "logging.googleapis.com/trace",
                "otelSpanID": "logging.googleapis.com/spanId",
                "otelTraceSampled": "logging.googleapis.com/trace_sampled",
            },
        )
        log_handler.setFormatter(formatter)
        logging.basicConfig(
            level=logging.INFO,
            handlers=[log_handler],
        )
    
    

The previous configuration extracts information about the active span from the log message and then adds that information as attributes to the JSON structured log. These attributes can then be used to correlate a log with a trace:

  * `logging.googleapis.com/trace`: Resource name of the trace associated with the log entry.
  * `logging.googleapis.com/spanId`: The span ID within the trace that is associated with the log entry.
  * `logging.googleapis.com/trace_sampled`: The value of this field must be `true` or `false`.



For more information about these fields, see the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) structure.

## Run a sample app configured to collect telemetry

The instrumentation in the sample app uses vendor-neutral formats, like JSON for log data and OTLP for metric and trace data. The sample app also uses [Flask](https://flask.palletsprojects.com/en/3.0.x/) to serve HTTP requests and the [requests](https://requests.readthedocs.io/en/latest/) library to make HTTP requests. The OpenTelemetry `Collector` sends log and metric data to your project by using Google exporters. It sends your trace data to your project by using the Telemetry API, which uses OTLP.

To generate metrics and traces for the HTTP client and server, the example app installs the [`opentelemetry-instrumentation-flask`](https://pypi.org/project/opentelemetry-instrumentation-flask/) and [`opentelemetry-instrumentation-requests`](https://pypi.org/project/opentelemetry-instrumentation-requests/) instrumentation libraries:
    
    
    logger = logging.getLogger(__name__)
    
    # Initialize OpenTelemetry Python SDK and structured logging
    setup_opentelemetry()
    setup_structured_logging()
    
    app = Flask(__name__)
    
    # Add instrumentation
    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()

The app has two endpoints:

  * The `/multi` endpoint is handled by the `multi` function. The load generator in the app issues requests to the `/multi` endpoint. When this endpoint receives a request, it sends between three and seven requests to the `/single` endpoint on the local server.
        
        @app.route("/multi")
        def multi():
            """Handle an http request by making 3-7 http requests to the /single endpoint."""
            sub_requests = randint(3, 7)
            logger.info("handle /multi request", extra={"subRequests": sub_requests})
            for _ in range(sub_requests):
                requests.get(url_for("single", _external=True))
            return "ok"
        
        

  * The `/single` endpoint is handled by the `single` function. When this endpoint receives a request, it sleeps for a short delay and then responds with a string.
        
        @app.route("/single")
        def single():
            """Handle an http request by sleeping for 100-200 ms, and write the number of seconds slept as the response."""
            duration = uniform(0.1, 0.2)
            logger.info("handle /single request", extra={"duration": duration})
            time.sleep(duration)
            return f"slept {duration} seconds"
        
        




### Download and deploy the app

**Note:** We recommend running the sample app by using Cloud Shell. However, if you want to run the sample app locally on Linux or Mac, then skip the first step in the following instructions.

To run the sample, do the following:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Clone the repository:
         
         git clone https://github.com/GoogleCloudPlatform/opentelemetry-samples
         

  3. Go to the sample directory:
         
         cd opentelemetry-samples/python/instrumentation-quickstart
         

  4. Build and run the sample:
         
         docker compose up --abort-on-container-exit
         

If you aren't running on Cloud Shell, then run the application with the `GOOGLE_APPLICATION_CREDENTIALS` environment variable pointing to a credentials file. [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal) provides a credentials file at `$HOME/.config/gcloud/application_default_credentials.json`.
         
         # Set environment variables
         export GOOGLE_CLOUD_PROJECT="PROJECT_ID"
         export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.config/gcloud/application_default_credentials.json"
         export USERID="$(id -u)"
         
         # Run
         docker compose -f docker-compose.yaml -f docker-compose.creds.yaml up --abort-on-container-exit
         




### View your metrics

The OpenTelemetry instrumentation in the sample app generates Prometheus metrics that you can view by using the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

  * `Prometheus/http_server_duration_milliseconds/histogram` records the duration of server requests and stores the results in a histogram.

  * `Prometheus/http_client_duration_milliseconds/histogram` records the duration of client requests and stores the results in a histogram.


To view the metrics generated by the sample app, do the following: 
  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `http_server` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Prometheus Target**.
     2. In the **Active metric categories** menu, select **Http**.
     3. In the **Active metrics** menu, select a metric. 
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed.   


When the measurements for a metric are cumulative, Metrics Explorer automatically normalizes the measured data by the alignment period, which results in the chart displaying a rate. For more information, see [Kinds, types, and conversions](https://docs.cloud.google.com/monitoring/api/v3/aggregation#ts-conversion).

When integer or double values are measured, such as with the two `counter` metrics, Metrics Explorer automatically sums all time series. To view the data for the `/multi` and `/single` HTTP routes, set the first menu of the **Aggregation** entry to **None**.

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




### View your traces

It might take several minutes before your trace data is available. For example, when trace data is received by your project, Google Cloud Observability might need to create a database to store that data. The creation of the database can take a few minutes and during that period, no trace data is available to view.

To view your trace data, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

  2. In the table section of the page, select a row with the span name `/multi`.
  3. In the Gantt chart on the **Trace details** panel, select the span labeled `/multi`.

A panel opens that displays information about the HTTP request. These details include the method, status code, number of bytes, and the user agent of the caller.

  4. To view the logs associated with this trace, select the **Logs & Events** tab.

The tab shows individual logs. To view the details of the log entry, expand the log entry. You can also click **View Logs** and view the log by using the Logs Explorer.




For more information about using the **Trace Explorer** page, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

### View your logs

From the Logs Explorer, you can inspect your logs, and you can also view associated traces when they exist.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate a log with the description of `handle /multi request`.

To view the details of the log, expand the log entry.

  3. Click ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Traces** on a log entry with the "handle /multi request" message, and then select **View trace details**.

A **Trace details** panel opens and displays the selected trace.

Your log data might be available several minutes before your trace data is available. If you encounter an error when viewing trace data either by searching for a trace by ID or by following the steps in this task, then wait a minute or two and retry the action.




For more information about using the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## What's next

  * [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/)
  * [OTLP specification](https://opentelemetry.io/docs/specs/otlp/)
  * [Structured logging](https://docs.cloud.google.com/logging/docs/structured-logging)
  * [Troubleshooting Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting)
  * [Troubleshoot Cloud Trace](https://docs.cloud.google.com/trace/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
