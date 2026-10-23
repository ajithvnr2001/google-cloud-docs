---
url: https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar/
title: Write OTLP metrics by using an OpenTelemetry Collector sidecar \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:44:17.555248+00:00
---

# Write OTLP metrics by using an OpenTelemetry Collector sidecar  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Write OTLP metrics by using an OpenTelemetry Collector sidecar Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to write, deploy, and call a Cloud Run service that reports custom [OTLP metrics](https://opentelemetry.io/docs/concepts/signals/metrics/) to [Google Cloud Managed Service For Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) by using the Google-Built OpenTelemetry Collector as a sidecar. For information about the Google-built Collector, see [Overview of the Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).

If you have a Cloud Run service that reports [Prometheus metrics](https://prometheus.io/docs/concepts/metric_types/), then use the [Prometheus sidecar for Cloud Run](https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar) instead.

## Objectives

  * Write, build, and deploy a service to Cloud Run with the Google-Built OpenTelemetry Collector as a sidecar.
  * Generate custom metrics and report them to Google Cloud Managed Service For Prometheus.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Google Cloud Managed Service For Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Run](https://cloud.google.com/run)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

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

  6. Enable the Cloud Run, Cloud Monitoring, Artifact Registry, and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,cloudbuild.googleapis.com,monitoring.googleapis.com,artifactregistry.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Update Google Cloud CLI: `gcloud components update`



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

Also note that the Cloud Run service identity needs the **Monitoring Metric Writer** (`roles/monitoring.metricWriter`) role. The [Compute Engine default service account](https://docs.cloud.google.com/run/docs/securing/service-identity#default_service_account) might have this role by default, but you might need to add it if you have changed its permissions or are using a different service account.

## Setting up gcloud defaults

To configure gcloud with defaults for your Cloud Run service:

  1. Set your default project:
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the name of the project you created for this tutorial.

  2. Configure gcloud for your chosen region:
         
         gcloud config set run/region REGION

Replace REGION with the supported Cloud Run region of your choice.




### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables)

  * `asia-east1` (Taiwan) 
  * `asia-northeast1` (Tokyo) 
  * `asia-northeast2` (Osaka) 
  * `asia-south1` (Mumbai, India) 
  * `asia-southeast3 ` (Bangkok) 
  * `europe-north1` (Finland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-north2` (Stockholm) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-southwest1` (Madrid) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west8` (Milan) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west9` (Paris) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-west1` (Tel Aviv) 
  * `northamerica-south1` (Mexico) 
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-east1` (South Carolina) 
  * `us-east4` (Northern Virginia) 
  * `us-east5` (Columbus) 
  * `us-south1` (Dallas) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west1` (Oregon) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



#### Subject to [Tier 2 pricing](https://cloud.google.com/run/pricing#tables)

  * `africa-south1` (Johannesburg) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-southeast1` (Singapore) 
  * `asia-southeast2 ` (Jakarta) 
  * `asia-south2` (Delhi, India) 
  * `australia-southeast1` (Sydney) 
  * `australia-southeast2` (Melbourne) 
  * `europe-central2` (Warsaw, Poland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west10` (Berlin) 
  * `europe-west12` (Turin) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west2` (London, UK) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west6` (Zurich, Switzerland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-central1` (Doha) 
  * `me-central2` (Dammam) 
  * `northamerica-northeast1` (Montreal) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `northamerica-northeast2` (Toronto) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-east1` (Sao Paulo, Brazil) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-west1` (Santiago, Chile) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west2` (Los Angeles) 
  * `us-west3` (Salt Lake City) 
  * `us-west4` (Las Vegas) 



If you already created a Cloud Run service, you can view the region in the Cloud Run dashboard in the [Google Cloud console](https://console.cloud.google.com/run).

OK

## Creating a Artifact Registry image repository

Create an Artifact Registry Docker repository to host the sample service image:
    
    
    gcloud artifacts repositories create run-otel \
        --repository-format=docker \
        --location=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * PROJECT_ID with the name of the project you created for this tutorial.
  * REGION REGION with the supported [Cloud Run region](https://docs.cloud.google.com/run/docs/locations) of your choice.



## Retrieving the code sample

To retrieve the code sample for use:

  1. Clone the sample app repository to your local machine:

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run sample code:

###  Go 
         
         cd golang-samples/run/custom-metrics/




## Reviewing the code

The code for this tutorial consists of the following:

  * A server that handles incoming requests and generates a metric named `sidecar_sample_counter_total`.


    
    
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    	"os/signal"
    	"syscall"
    	"time"
    
    	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
    	"go.opentelemetry.io/otel/metric"
    	sdkmetric "go.opentelemetry.io/otel/sdk/metric"
    	"go.opentelemetry.io/otel/sdk/resource"
    	semconv "go.opentelemetry.io/otel/semconv/v1.24.0"
    )
    
    var counter metric.Int64Counter
    
    func main() {
    	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
    	defer stop()
    
    	shutdownMetrics := setupCounter(ctx)
    
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    		log.Printf("defaulting to port %s", port)
    	}
    
    	http.HandleFunc("/", handler)
    	server := &http.Server{Addr: ":" + port}
    	log.Printf("listening on port %s", port)
    	go func() {
    		if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
    			log.Fatalf("server failed: %v", err)
    		}
    	}()
    
    	<-ctx.Done()
    
    	shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    	defer cancel()
    	if err := server.Shutdown(shutdownCtx); err != nil {
    		log.Printf("server shutdown failed: %v", err)
    	}
    
    	metricsCtx, metricsCancel := context.WithTimeout(context.Background(), 5*time.Second)
    	defer metricsCancel()
    	if err := shutdownMetrics(metricsCtx); err != nil {
    		log.Printf("metrics shutdown failed: %v", err)
    	}
    }
    
    func handler(w http.ResponseWriter, r *http.Request) {
    	counter.Add(context.Background(), 100)
    	fmt.Fprintln(w, "Incremented sidecar_sample_counter_total metric!")
    }
    
    func setupCounter(ctx context.Context) func(context.Context) error {
    	serviceName := os.Getenv("K_SERVICE")
    	if serviceName == "" {
    		serviceName = "sample-cloud-run-app"
    	}
    	r, err := resource.Merge(
    		resource.Default(),
    		resource.NewWithAttributes(
    			resource.Default().SchemaURL(),
    			semconv.ServiceName(serviceName),
    		),
    	)
    	if err != nil {
    		log.Fatalf("Error creating resource: %v", err)
    	}
    
    	exporter, err := otlpmetricgrpc.New(ctx,
    		otlpmetricgrpc.WithInsecure(),
    	)
    	if err != nil {
    		log.Fatalf("Error creating exporter: %s", err)
    	}
    	provider := sdkmetric.NewMeterProvider(
    		sdkmetric.WithReader(sdkmetric.NewPeriodicReader(exporter)),
    		sdkmetric.WithResource(r),
    	)
    
    	meter := provider.Meter("example.com/metrics")
    	counter, err = meter.Int64Counter("sidecar-sample-counter")
    	if err != nil {
    		log.Fatalf("Error creating counter: %s", err)
    	}
    	return provider.Shutdown
    }
    

  * A `Dockerfile` that defines the operating environment for the service.


    
    
    FROM golang:1.25 as builder
    WORKDIR /app
    COPY . .
    RUN CGO_ENABLED=0 GOOS=linux go build -o sample-app
    
    FROM alpine:3
    RUN apk add --no-cache ca-certificates
    COPY --from=builder /app/sample-app /sample-app
    CMD ["/sample-app"]

The sample also includes files under the `collector` subdirectory for building a custom collector:

  * A config file for the collector.
        
        receivers:
          otlp:
            protocols:
              grpc:
              http:
        
        processors:
          batch:
            # batch metrics before sending to reduce API usage
            send_batch_max_size: 200
            send_batch_size: 200
            timeout: 5s
        
          memory_limiter:
            # drop metrics if memory usage gets too high
            check_interval: 1s
            limit_percentage: 65
            spike_limit_percentage: 20
        
          # automatically detect Cloud Run resource metadata                                                                                                                                               
          resourcedetection:
            detectors: [env, gcp]
            timeout: 2s
            override: false
        
          resource:
            attributes:
            # add instance_id as a resource attribute
            - key: service.instance.id
              from_attribute: faas.id
              action: upsert
              # parse service name from K_SERVICE Cloud Run variable                                                                                                                                       
            - key: service.name
              value: ${env:K_SERVICE}
              action: insert
        
        exporters:
          googlemanagedprometheus: # Note: this is intentionally left blank   
        
        extensions:
          health_check:
            endpoint: 0.0.0.0:13133
        service:
          extensions: [health_check]
          pipelines:
            metrics:
              receivers: [otlp]
              processors: [batch, memory_limiter, resourcedetection, resource]
              exporters: [googlemanagedprometheus]

  * A `Dockerfile` that bundles the provided config into an upstream Collector image.
        
        FROM us-docker.pkg.dev/cloud-ops-agents-artifacts/google-cloud-opentelemetry-collector/otelcol-google:0.121.0
        
        COPY collector-config.yaml /etc/otelcol-google/config.yaml




## Shipping the code

Shipping code consists of three steps: building a container image with Cloud Build, uploading the container image to Artifact Registry, and deploying the container image to Cloud Run.

To ship your code:

  1. Build your sample service container and publish on Artifact Registry:
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/run-otel/sample-metrics-app

Upon success, you should see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Artifact Registry and can be re-used if desired.

  2. Build your Collector container and publish on Artifact Registry:
         
         gcloud builds submit collector --tag REGION-docker.pkg.dev/PROJECT_ID/run-otel/otel-collector-metrics

Upon success, you should see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Artifact Registry and can be re-used if desired.

  3. Deploy your application:

### YAML

     1. Create a new file called `service.yaml` with the following:
            
            apiVersion: serving.knative.dev/v1
            kind: Service
            metadata:
              name: SERVICE-NAME
              annotations:
                run.googleapis.com/launch-stage: BETA
            spec:
              template:
                metadata:
                  annotations:
                    run.googleapis.com/container-dependencies: "{app:[collector]}"
                spec:
                  containers:
                  - image: REGION-docker.pkg.dev/PROJECT_ID/run-otel/sample-metrics-app
                    name: app
                    ports:
                    - containerPort: CONTAINER_PORT
                    env:
                    - name: "OTEL_EXPORTER_OTLP_ENDPOINT"
                      value: "http://localhost:4317"
                  - image: REGION-docker.pkg.dev/PROJECT_ID/run-otel/otel-collector-metrics
                    name: collector
                    startupProbe:
                      httpGet:
                        path: /
                        port: 13133
            

     2. Replace the following: 
        * CONTAINER_PORT with the [port your service's ingress container listens on](https://docs.cloud.google.com/run/docs/container-contract#port). By default, this is `8080`.
        * SERVICE-NAME with any name for your service, such as `custom-metrics-sample-service`. 

  4. Create the new service with the following command:
         
         gcloud run services replace service.yaml

This command returns a service URL. Use this URL to try out the sample application in Trying it out.




## Trying it out

Using the URL from the `gcloud run` command in Shipping the code, connect to the service to generate some sample metrics (you can run this command several times to generate more interesting data):
    
    
    curl -H \
    "Authorization: Bearer $(gcloud auth print-identity-token)" \
    SERVICE_URL
    

Replace SERVICE_URL with the URL of your service.

Next, navigate to the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) within the Cloud Monitoring section of the Google Cloud console and select the `sidecar_sample_counter_total` metric.

![Custom metric shown in the Metrics Explorer UI](https://docs.cloud.google.com/static/run/docs/tutorials/images/gmp_custom_metrics_cmui.png)

You can also query the metrics with [PromQL](https://docs.cloud.google.com/monitoring/promql). For example, the query below will filter metrics based on the Cloud Run instance ID:
    
    
    sidecar_sample_counter_total{instance="INSTANCE_ID"}
    

Replace INSTANCE_ID with the ID of any instance for your service (available in the instance logs or from the [metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server)).

This query produces a chart like the one below:

![Custom metric queried by PromQL](https://docs.cloud.google.com/static/run/docs/tutorials/images/gmp_custom_metrics_promql.png)

**Success:** You deployed a Cloud Run service that reports custom OTLP metrics to Google Cloud Managed Service For Prometheus.

## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the Artifact Registry Docker repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos)



## What's next

More examples, including examples for traces and logs, are available on [GitHub](https://github.com/GoogleCloudPlatform/opentelemetry-cloud-run/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
