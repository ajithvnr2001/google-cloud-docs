---
url: https://docs.cloud.google.com/trace/docs/trace-app-latency/
title: Quickstart: View latency of app requests \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:32.102488+00:00
---

# Quickstart: View latency of app requests  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-app-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View latency of app requests

Cloud Trace lets you collect and analyze end-to-end request latency data so that you can identify performance bottlenecks across your applications. In this quickstart, you use the Google Cloud CLI to create a Google Kubernetes Engine (GKE) cluster, deploy a sample application, send an HTTP request to generate a trace, and inspect the resulting latency data in the Google Cloud console.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/traces/explorer?walkthrough_id=cloud_trace_getting_started)

* * *

## Before you begin

  1. Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Google Kubernetes Engine and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudtrace.googleapis.com)

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Google Kubernetes Engine and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudtrace.googleapis.com)




### Required roles

To get the permissions that you need to create a Google Kubernetes Engine cluster and to view trace spans, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a GKE cluster

This guide creates a standard GKE cluster. If you use Autopilot mode for Google Kubernetes Engine or if you enable Workload Identity Federation for GKE, then you must [configure your application to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).

  1. In the toolbar, click _terminal_ **Activate Cloud Shell** , and then perform the following steps in the Cloud Shell.

  2. Create a cluster:
         
         gcloud container clusters create cloud-trace-demo --zone us-central1-c
         

The previous command, which takes several minutes to complete, creates a standard cluster with the name `cloud-trace-demo` in the zone `us-central1-c`.

  3. Configure `kubectl` to automatically refresh its credentials to use the same identity as the Google Cloud CLI:
         
         gcloud container clusters get-credentials cloud-trace-demo --zone us-central1-c
         

  4. Verify access to your cluster:
         
         kubectl get nodes
         

A sample output of this command is:
         
         NAME                                              STATUS   ROLES    AGE   VERSION
         gke-cloud-trace-demo-default-pool-063c0416-113s   Ready    <none>   78s   v1.22.12-gke.2300
         gke-cloud-trace-demo-default-pool-063c0416-1n27   Ready    <none>   79s   v1.22.12-gke.2300
         gke-cloud-trace-demo-default-pool-063c0416-frkd   Ready    <none>   78s   v1.22.12-gke.2300
         




## Download and deploy an application

Download and deploy a Python application, which uses the Flask framework and the OpenTelemetry package. The application is described in the About the app section of this page.

In the Cloud Shell, do the following:

  1. Clone a Python app from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

  2. Run the following command to deploy the sample application:
         
         cd python-docs-samples/trace/cloud-trace-demo-app-opentelemetry && ./setup.sh
         

The script `setup.sh` takes several minutes to complete.

The script configures three services using a prebuilt image and then waits for all resources to be provisioned. The workloads are named `cloud-trace-demo-a`, `cloud-trace-demo-b`, and `cloud-trace-demo-c`.

A sample output of this command is:
         
         deployment.apps/cloud-trace-demo-a is created
         service/cloud-trace-demo-a is created
         deployment.apps/cloud-trace-demo-b is created
         service/cloud-trace-demo-b is created
         deployment.apps/cloud-trace-demo-c is created
         service/cloud-trace-demo-c is created
         
         Wait for load balancer initialization complete......
         Completed.
         




## Create trace data

A _trace_ describes the time it takes an application to complete a single operation.

To create a trace, in the Cloud Shell, run the following command:
    
    
    curl $(kubectl get svc -o=jsonpath='{.items[?(@.metadata.name=="cloud-trace-demo-a")].status.loadBalancer.ingress[0].ip}')
    

The response of the previous command looks like the following:
    
    
    Hello, I am service A
    And I am service B
    Hello, I am service C
    

You can execute the `curl` command multiple times to generate multiple traces.

## View latency data

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

The following screenshot shows the result of running the `curl` command several times. The graph displays aggregated latency data for _spans_ , which describe trace sub-operations.

![Trace explorer window for the quickstart.](https://docs.cloud.google.com/static/trace/images/quickstart-trace-list-example.png)

**Note:** If you don't see any trace data after waiting a few minutes, then there might be a permission problem. To resolve this problem, check to see whether the service account with the extension `@developer.gserviceaccount.com` has the Editor role. If not, then [grant the service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) the [Cloud Trace Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) role, and run the `curl` command.
  2. To view a trace in detail, select a span in the graph or a row in the table.

The trace details dialog opens, as shown in the following screenshot:

![Additional details about each span are shown in the details pane.](https://docs.cloud.google.com/static/trace/images/quickstart-trace-span-details.png)

A Gantt chart displays information about the selected trace. The first row in the Gantt chart is for the trace, and each following row is a span within the trace.

  3. To view information detailed information about a span, in the Gantt chart, select the span.




## About the application

The sample application used in this quickstart is available in a GitHub repository. This repository contains information on how to use the application in environments other than the Cloud Shell. The sample application is written in Python, uses the Flask framework and OpenTelemetry packages, and executes on a GKE cluster.

This guide creates a standard GKE cluster. If you use Autopilot mode for Google Kubernetes Engine or if you enable Workload Identity Federation for GKE, then you must [configure your application to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).

### Instrumentation

The file `app.py` in the [GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/trace/cloud-trace-demo-app-opentelemetry), contains the instrumentation necessary to capture and send trace data to your Google Cloud project:

  * The application imports several OpenTelemetry packages:
        
        from opentelemetry import trace
        from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
        from opentelemetry.instrumentation.flask import FlaskInstrumentor
        from opentelemetry.instrumentation.requests import RequestsInstrumentor
        from opentelemetry.propagate import set_global_textmap
        from opentelemetry.propagators.cloud_trace_propagator import CloudTraceFormatPropagator
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        

  * The application instruments web requests with trace context and automatically traces Flask handlers and requests to other services:
        
        app = flask.Flask(__name__)
        FlaskInstrumentor().instrument_app(app)
        RequestsInstrumentor().instrument()

  * The application configures the Cloud Trace exporter as a trace provider, which propagates trace context in the Cloud Trace format:
        
        def configure_exporter(exporter):
            """Configures OpenTelemetry context propagation to use Cloud Trace context
        
            Args:
                exporter: exporter instance to be configured in the OpenTelemetry tracer provider
            """
            set_global_textmap(CloudTraceFormatPropagator())
            tracer_provider = TracerProvider()
            tracer_provider.add_span_processor(BatchSpanProcessor(exporter))
            trace.set_tracer_provider(tracer_provider)
        
        
        configure_exporter(CloudTraceSpanExporter())
        tracer = trace.get_tracer(__name__)

  * The following code snippet shows how to send requests in Python. OpenTelemetry implicitly propagates the trace context for you with your outgoing requests:
        
        if endpoint is not None and endpoint != "":
            data = {"body": keyword}
            response = requests.get(
                endpoint,
                params=data,
            )
            return keyword + "\n" + response.text
        else:
            return keyword, 200
        
        




### How the application works

For clarity, in this section, `cloud-trace-demo` is omitted from the service names. For example, the service `cloud-trace-demo-c` is referenced as `c`.

This application creates three services named `a`, `b`, and `c`. Service `a` is configured to call service `b`, service `b` is configured to call service `c`. For details on the configuration of the services, see the YAML files in the [GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/trace/cloud-trace-demo-app-opentelemetry).

When you issued a HTTP request to service `a` in this quickstart, you used the following `curl` command:
    
    
    curl $(kubectl get svc -o=jsonpath='{.items[?(@.metadata.name=="cloud-trace-demo-a")].status.loadBalancer.ingress[0].ip}')
    

The `curl` command works as follows:

  1. `kubectl` fetches the IP address of the service named `cloud-trace-demo-a`.
  2. The `curl` command then sends the HTTP request to service `a`.
  3. Service `a` receives the HTTP request and sends a request to service `b`.
  4. Service `b` receives the HTTP request and sends a request to service `c`.
  5. Service `c` receives the HTTP request from service `b` and returns the string `Hello, I am service C` to service `b`.
  6. Service `b` receives the response from service `c`, appends it to the string `And I am service B`, and returns the result to service `a`.
  7. Service `a` receives the response from service `b` and appends it to the string `Hello, I am service A`.
  8. The response from service `a` is printed in the Cloud Shell.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project and you no longer need the project, then [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing project, then do the following:

  1. To delete your cluster, in the Cloud Shell, run the following command:
         
         gcloud container clusters delete cloud-trace-demo --zone us-central1-c




## What's next

  * For information on languages and platforms supported, see [Cloud Trace overview](https://docs.cloud.google.com/trace/docs/overview).
  * For details on how to instrument your applications, see:

    * [Instrument for Cloud Trace](https://docs.cloud.google.com/trace/docs/setup).
    * [OpenTelemetry](https://opentelemetry.io/).
    * [Data model](https://docs.cloud.google.com/trace/docs/reference#data_model).
  * For more information on the **Trace Explorer** window, see [Find and view traces](https://docs.cloud.google.com/trace/docs/finding-traces).

  * To learn more about managing GKE clusters, see [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
