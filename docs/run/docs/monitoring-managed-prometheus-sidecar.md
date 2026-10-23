---
url: https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar/
title: Write Prometheus metrics by using the Prometheus sidecar \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:53:07.969452+00:00
---

# Write Prometheus metrics by using the Prometheus sidecar  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Write Prometheus metrics by using the Prometheus sidecar Stay organized with collections  Save and categorize content based on your preferences. 

The Managed Service for Prometheus sidecar for Cloud Run is the Google-recommended way to get [Prometheus-style monitoring](https://prometheus.io/docs/introduction/overview/) for Cloud Run services. If your Cloud Run service writes [OTLP metrics](https://opentelemetry.io/docs/concepts/signals/metrics/), then you can use the [OpenTelemetry sidecar](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar). But for services that write [Prometheus metrics](https://prometheus.io/docs/concepts/metric_types/), use the Managed Service for Prometheus sidecar described in this document.

This document describes how to do the following:

  * Add the Managed Service for Prometheus sidecar to an existing Cloud Run service.
  * Build a sample app with the sidecar. You can use the sample app to see how the sidecar works if you don't have an existing Cloud Run service.



The sidecar uses [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) on the server side and a distribution of the OpenTelemetry Collector, custom-built for serverless workloads, on the client side. This custom distribution includes some changes to support Cloud Run. The collector performs a start-up scrape after 10 seconds and performs a shut-down scrape, no matter how short-lived the instance is. For maximum reliability, we recommend that Cloud Run services running the sidecar also use the instance-based billing setting; for more information, see [Billing settings (services)](https://docs.cloud.google.com/run/docs/configuring/billing-settings). Some scrape attempts might fail if the CPU allocation is throttled due to a low number of queries per second (QPS). An always-allocated CPU remains available.

The sidecar relies on the Cloud Run multi-container (sidecar) feature to run the collector as a sidecar container alongside your workload container. For more information about sidecars in Cloud Run, see [Deploying multiple containers to a service (sidecars)](https://docs.cloud.google.com/run/docs/deploying#sidecars).

The Managed Service for Prometheus sidecar for Cloud Run introduces a new configuration, `RunMonitoring`, a subset of the Kubernetes [`PodMonitoring`](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#podmonitoring) custom resource. Most users can use the default `RunMonitoring` configuration, but you can also create custom configurations. For more information about the default and custom `RunMonitoring` configurations, see Add the sidecar to a Cloud Run service.

## Before you begin

This section describes the setup necessary to use this document.

### Install and configure the gcloud CLI

Many of the steps described in this document use the Google Cloud CLI. For information about installing the gcloud CLI, see [Managing Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components).

When invoking `gcloud` commands, you must specify the identifier for your Google Cloud project. You can set a default project for the Google Cloud CLI and eliminate the need to enter it with every command. To set your project as the default, enter the following command:
    
    
    gcloud config set project PROJECT_ID
    

You can also set a default region for your Cloud Run service. To set a default region, enter the following command:
    
    
    gcloud config set run/region REGION
    

### Enable APIs

You must enable the following APIs in your Google Cloud project:

  * Cloud Run Admin API: `run.googleapis.com`
  * Artifact Registry API: `artifactregistry.googleapis.com`
  * Cloud Monitoring API: `monitoring.googleapis.com`
  * Cloud Logging API: `logging.googleapis.com`
  * (Optional) If you create a custom `RunMonitoring` config, then you must enable the Secret Manager API: `secretmanager.googleapis.com`
  * (Optional) If you choose to run the sample app by using Cloud Build, then you must also enable the following APIs: 
    * Cloud Build API: `cloudbuild.googleapis.com`.
    * Identity and Access Management API: `iam.googleapis.com`. For more information, see Build and run the sample app.



To see the APIs enabled in your project, run the following command:
    
    
    gcloud services list
    

To enable an API that isn't enabled, run one of following commands:
    
    
    gcloud services enable run.googleapis.com
    gcloud services enable artifactregistry.googleapis.com
    gcloud services enable secretmanager.googleapis.com
    gcloud services enable monitoring.googleapis.com
    gcloud services enable logging.googleapis.com
    gcloud services enable cloudbuild.googleapis.com
    gcloud services enable iam.googleapis.com
    

### Service account for Cloud Run

By default, Cloud Run jobs and services use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), `PROJECT_NUMBER-compute@developer.gserviceaccount.com`. This service account usually has the Identity and Access Management (IAM) roles necessary to write the metrics and logs described in this document:

  * `roles/monitoring.metricWriter`
  * `roles/logging.logWriter`



If you create a custom `RunMonitoring` config, then your service account must also have the following roles:

  * `roles/secretmanager.admin`
  * `roles/secretmanager.secretAccessor`



You can also configure a user-managed service account for Cloud Run. A user-managed service account must also have these roles. For more information about service accounts for Cloud Run, see [Configuring Service Identity](https://docs.cloud.google.com/run/docs/securing/service-identity).

## Configure and add the sidecar to a Cloud Run service

The Managed Service for Prometheus sidecar for Cloud Run introduces a new configuration, `RunMonitoring`, which is a subset of the Kubernetes [`PodMonitoring`](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#podmonitoring) custom resource. The `RunMonitoring` configuration uses existing `PodMonitoring` options to support Cloud Run while eliminating some options that are specific to Kubernetes.

You can use the default `RunMonitoring` configuration, or you can create a custom configuration. The following sections describe both approaches. You don't need to do both. For more information about using default or custom configurations, select the corresponding tab.

###  Default configuration 

### Use the default RunMonitoring configuration

If you don't create a custom `RunMonitoring` configuration, then the sidecar collector synthesizes the following default configuration to scrape metrics from port 8080 at metrics path `/metrics` every 30 seconds:
    
    
    apiVersion: monitoring.googleapis.com/v1beta
    kind: RunMonitoring
    metadata:
      name: run-gmp-sidecar
    spec:
      endpoints:
      - port: 8080
        path: /metrics
        interval: 30s
    

Using the default configuration requires no additional setup beyond adding the sidecar to your Cloud Run service.

### Add the sidecar to a Cloud Run service

To use the sidecar with the default `RunMonitoring` configuration, you need to modify your existing Cloud Run configuration to add the sidecar. To add the sidecar, do the following:

  * Add a container-dependency annotation that specifies the startup and shutdown order of the containers. In the following example, the sidecar container, named "collector", starts after and shuts down before the application container, named "app" in the example.
  * Create a container for the collector, named "collector" in the following example.



For example, add the lines preceded by the `+` (plus) character to your Cloud Run configuration, and then redeploy your service:
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      annotations:
        run.googleapis.com/launch-stage: ALPHA
        run.googleapis.com/cpu-throttling: 'false'
      name: my-cloud-run-service
    spec:
      template:
        metadata:
          annotations:
            run.googleapis.com/execution-environment: gen2
    +       run.googleapis.com/container-dependencies: '{"collector":["app"]}'
        spec:
          containers:
          - image: "REGION-docker.pkg.dev/PROJECT_ID/run-gmp/sample-app"
            name: app
            startupProbe:
              httpGet:
                path: /startup
                port: 8000
            livenessProbe:
              httpGet:
                path: /liveness
                port: 8000
            ports:
            - containerPort: 8000
    +     - image: "us-docker.pkg.dev/cloud-ops-agents-artifacts/cloud-run-gmp-sidecar/cloud-run-gmp-sidecar:1.2.0"
    +       name: collector
    

To redeploy the Cloud Run service with the configuration file `run-service.yaml`, run the following command:
    
    
    gcloud run services replace run-service.yaml --region=REGION
    

**Note:** If you're [using Artifact Registry with VPC Service Controls](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc#ar-vpc), then you must also configure your egress rule to allow egress to the `cloud-ops-agents-artifacts` project. To do so, add `projects/1042947621568` as a resource in your egress rule.

###  Custom configuration 

### Create a custom RunMonitoring configuration

You can create a `RunMonitoring` configuration for a Cloud Run service if the default configuration is not sufficient. For example, you might create a configuration like the following:
    
    
    apiVersion: monitoring.googleapis.com/v1beta
    kind: RunMonitoring
    metadata:
      name: my-custom-cloud-run-job
    spec:
      endpoints:
      - port: 8080
        path: /metrics
        interval: 10s
        metricRelabeling:
        - action: replace
          sourceLabels:
          - __address__
          targetLabel: label_key
          replacement: label_value
      targetLabels:
        metadata:
        - service
        - revision
    

This configuration does the following:

  * Scrapes metrics from the port 8080 and uses the default metrics path `/metrics`.
  * Uses a 10-second scrape interval.
  * Uses relabelling to add the label `label_key` with the value `label_value` to every metric scraped.
  * Adds the `service` and `revision` metadata labels to every metric scraped.



For information on the available configuration options, see RunMonitoring spec: configuration options.

When you use a custom `RunMonitoring` configuration, you must perform the following additional configuration:

  * Enable the Secret Manager API and grant your Cloud Run service account Secret Manager roles. For more information, see Before you begin.
  * Store the custom configuration as a secret.
  * Add the sidecar to a Cloud Run service .



#### Store the configuration by using Secret Manager

To provide a custom `RunMonitoring` configuration, do the following:

  * Create a file that contains the custom configuration.
  * Create a Secret Manager secret that contains the custom configuration.



The following command creates a secret named mysecret from the `custom-config.yaml` file:
    
    
    gcloud secrets create mysecret --data-file=custom-config.yaml
    

To pick up a change to the configuration after you modify the `custom-config.yaml` file, you must delete and recreate the secret, and then redeploy the Cloud Run service.

#### Updating the configuration in Secret Manager

If you want to update the custom `RunMonitoring` configuration at any time, you can add a new version of the existing secret to Secret Manager.

For example, to update mysecret with a new config stored in file `custom-config-updated.yaml`, you can run:
    
    
    gcloud secrets versions add mysecret --data-file=custom-config-updated.yaml
    

The sidecar automatically reloads and applies the changes to its configuration.

### Add the sidecar to a Cloud Run service

After you have created a Secret Manager secret for your `RunMonitoring` configuration, you must modify your Cloud Run configuration to do the following:

  * Add the Managed Service for Prometheus sidecar 
    * Add a container-dependency annotation that specifies the startup and shutdown order of the containers. In the following example, the sidecar container, named "collector", starts after and shuts down before the application container, named "app" in the example.
    * Create a container for the collector, named "collector" in the following example.
  * Add the secret by mounting the secret at the location `/etc/rungmp/config.yaml`: 
    * Add a secrets annotation that points to the secret holding your custom `RunMonitoring` configuration.
    * Create a volume, named "config" in the following example, for the secret that points to the file `config.yaml`.
    * Mount the volume as part of the collector image at the mount path `/etc/rungmp`.



For example, add the lines preceded by the `+` (plus) character to your Cloud Run configuration, and then redeploy your service:
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      annotations:
        run.googleapis.com/launch-stage: ALPHA
        run.googleapis.com/cpu-throttling: 'false'
      name: my-cloud-run-service
    spec:
      template:
        metadata:
          annotations:
            run.googleapis.com/execution-environment: gen2
    +       run.googleapis.com/container-dependencies: '{"collector":["app"]}'
    +       run.googleapis.com/secrets: 'mysecret:projects/PROJECT_ID/secrets/mysecret'
        spec:
          containers:
          - image: "REGION-docker.pkg.dev/PROJECT_ID/run-gmp/sample-app"
            name: app
            startupProbe:
              httpGet:
                path: /startup
                port: 8000
            livenessProbe:
              httpGet:
                path: /liveness
                port: 8000
            ports:
            - containerPort: 8000
    +     - image: "us-docker.pkg.dev/cloud-ops-agents-artifacts/cloud-run-gmp-sidecar/cloud-run-gmp-sidecar:1.2.0"
    +       name: collector
    +       volumeMounts:
    +       - mountPath: /etc/rungmp/
    +         name: config
    +     volumes:
    +     - name: config
    +       secret:
    +         items:
    +         - key: latest
    +           path: config.yaml
    +         secretName: 'mysecret'
    

To redeploy the Cloud Run service with the configuration file `run-service.yaml`, run the following command:
    
    
    gcloud run services replace run-service.yaml --region=REGION
    

### RunMonitoring spec: configuration options

This section describes `RunMonitoring` configuration spec for the Managed Service for Prometheus sidecar. The following shows an example custom configuration:
    
    
    apiVersion: monitoring.googleapis.com/v1beta
    kind: RunMonitoring
    metadata:
      name: my-custom-cloud-run-job
    spec:
      endpoints:
      - port: 8080
        path: /metrics
        interval: 10s
        metricRelabeling:
        - action: replace
          sourceLabels:
          - __address__
          targetLabel: label_key
          replacement: label_value
      targetLabels:
        metadata:
        - service
        - revision
    

##### RunMonitoring

The `RunMonitoring` configuration monitors a Cloud Run service.

Field | Description | Scheme | Required  
---|---|---|---  
`metadata` | Metadata that all persisted resources must have. | `[ metav1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta)` | false  
`spec` | Specification of the Cloud Run deployment selected for target discovery by Prometheus. | `RunMonitoringSpec` | true  
  
##### RunMonitoringSpec

This spec describes how the `RunMonitoring` configuration monitors a Cloud Run service.

Field | Description | Scheme | Required  
---|---|---|---  
`endpoints` | Endpoints to scrape on the selected pods. | `[][ScrapeEndpoint](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#scrapeendpoint)` | true  
`targetLabels` | Labels to add to the Prometheus target for discovered endpoints. The `instance` label is always set to the Cloud Run instance ID. | `RunTargetLabels` | false  
`limits` | Limits to apply at scrape time. | `*[ScrapeLimits](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#scrapelimits)` | false  
  
##### RunTargetLabels

The `RunTargetLabels` configuration lets you include Cloud Run labels from the discovered Prometheus targets.

Field | Description | Scheme | Required  
---|---|---|---  
`metadata` | Cloud Run metadata labels that are set on all scraped targets.  
  
Permitted keys are `instance`, `revision`, `service`, and `configuration`.  
  
If permitted keys are set, then the sidecar adds the corresponding value from the Cloud Run instance as metric labels to every metric: `instanceID`, `revision_name`, `service_name`, and `configuration_name`.  
  
Defaults to all permitted keys being set. | `*[]string` | false  
  
## Build and run a sample app

This section describes how to run the Managed Service for Prometheus sidecar with a sample app. This section is optional. If you already have a Cloud Run service and want to deploy the sidecar with it, then see Add the Managed Service for Prometheus sidecar to a Cloud Run service.

### Clone the `run-gmp-sidecar` repository

To get the sample app and its configuration files, clone the `run-gmp-sidecar` repository by running the following command:
    
    
    git clone https://github.com/GoogleCloudPlatform/run-gmp-sidecar/
    

After cloning the repository, change to the `run-gmp-sidecar` directory:
    
    
    cd run-gmp-sidecar
    

### Build and run the sample app

The sample app requires Docker or a similar container build system for Linux. You can build and run the sample app in either of the following ways:

  * Use Cloud Build to run without local Docker support. If you use Cloud Build, then you must also enable the Cloud Build API.
  * Build and run the sample app manually.



The following sections describe both approaches. You don't need to do both. For more information, select the tab for one of the approaches.

###  Use Cloud Build 

## Use Cloud Build

The `run-gmp-sidecar` repository includes configuration files for Cloud Build. These files bundle together the steps needed to build and deploy the sample app.

You can also manually perform the steps handled by Cloud Build. For more information, see Build and run manually.

### Set up for Cloud Build

These configuration files require a Cloud Build service account and an Artifact Registry repository. The `run-gmp-sidecar` repository also includes a script, `create-sa-and-ar.sh` that does the following:

  * Creates a service account, `run-gmp-sa@PROJECT_ID.iam.gserviceaccount.com`.
  * Grants the following roles to the service account: 
    * `roles/iam.serviceAccountUser`
    * `roles/storage.objectViewer`
    * `roles/logging.logWriter`
    * `roles/artifactregistry.createOnPushWriter`
    * `roles/secretmanager.admin`
    * `roles/secretmanager.secretAccessor`
    * `roles/run.admin`
  * Creates an Artifact Registry repository, `run-gmp`, for your container images.



To create the `run-gmp-sa` service account and `run-gmp` repository, run the following command:
    
    
    ./create-sa-and-ar.sh
    

It takes some time for the permissions to propagate, so we recommend waiting about 30 seconds before proceeding to the next step. Otherwise, you might see authorization errors.

### Submit Cloud Build request

After you've set up the `run-gmp-sa` service account and `run-gmp` repository, you can start a Cloud Build job by submitting the Cloud Build configuration file. You can use the following `gcloud builds submit` command:
    
    
    gcloud builds submit . --config=cloudbuild-simple.yaml --region=REGION
    

This command takes several minutes to run, but it almost immediately indicates you where you can find the Cloud Build build details. The message looks like the following:
    
    
    Logs are available at [
    https://console.cloud.google.com/cloud-build/builds/637860fb-7a14-46f2-861e-09c1dc4cea6b?project=PROJECT_NUMBER].
    

To watch the build progress, navigate to the returned URL in your browser. You can also view the sidecar logs in Cloud Logging.

### Check the service URL

After the Cloud Build job ends, check the Cloud Run service endpoint URL by running the following command:
    
    
    gcloud run services describe my-cloud-run-service --region=REGION --format="value(status.url)"
    

This command returns the service URL, which looks like the following:
    
    
    https://my-cloud-run-service-abcdefghij-ue.a.run.app
    

###  Build and run manually 

## Build and run manually

You can manually perform the steps handled by Cloud Build, described in Use Cloud Build. The following sections describe how to manually perform the same tasks.

### Set variables used by later steps

Several of the later steps use environment variables for common values. Set up these variables by using the following commands:
    
    
    export GCP_PROJECT=PROJECT_ID
    export REGION=REGION
    

### Create a container image repository

Create an Artifact Registry repository for the container image by running the following command:
    
    
    gcloud artifacts repositories create run-gmp \
        --repository-format=docker \
        --location=${REGION}
    

### Build and push the sample app

This example uses Docker on Linux to build the sample app and push it to an Artifact Registry repository. You might need to adapt these commands if you are working in a Windows or macOS environment.

**Note:** If you need `sudo` to execute `docker` commands, then you also need to authenticate by using `sudo` as well. Failure to do so results in the wrong system user being configured, and requests to Cloud Run are not authenticated. 
    
    
    sudo gcloud auth login --no-launch-browser
    sudo gcloud auth configure-docker
    

To build the sample app and push it to Artifact Registry, do the following:

  1. Authenticate your Docker client with the Google Cloud CLI:
         
         gcloud auth configure-docker ${REGION}-docker.pkg.dev
         

  2. Go to the `simple-app` directory in the `run-gmp-sidecar` repository: 
         
         pushd sample-apps/simple-app
         

  3. Build the `simple-app` app by running the following command:
         
         docker build -t ${REGION}-docker.pkg.dev/${GCP_PROJECT}/run-gmp/sample-app .
         

  4. Push the image for the built app by running the following command: 
         
         docker push ${REGION}-docker.pkg.dev/${GCP_PROJECT}/run-gmp/sample-app
         

  5. Return to the `run-gmp-sidecar` directory:
         
         popd
         




### Configure the Cloud Run service

The `run-service-simple.yaml` file in the `run-gmp-sidecar` repository defines a multi-container Cloud Run service that uses the sample app and collector images that you built in previous steps. The `run-service-simple.yaml` file contains the following Service specification:
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      annotations:
        run.googleapis.com/launch-stage: ALPHA
        run.googleapis.com/cpu-throttling: 'false'
      name: my-cloud-run-service
    spec:
      template:
        metadata:
          annotations:
            run.googleapis.com/execution-environment: gen2
            run.googleapis.com/container-dependencies: '{"collector":["app"]}'
        spec:
          containers:
          - image: "%SAMPLE_APP_IMAGE%"
            name: app
            startupProbe:
              httpGet:
                path: /startup
                port: 8000
            livenessProbe:
              httpGet:
                path: /liveness
                port: 8000
            ports:
            - containerPort: 8000
          - image: "us-docker.pkg.dev/cloud-ops-agents-artifacts/cloud-run-gmp-sidecar/cloud-run-gmp-sidecar:1.2.0"
            name: collector
    

This file contains a placeholder value for the images you've built in previous steps, so you must update the placeholders with the actual values for your Google Cloud project.

Replace the `%SAMPLE_APP_IMAGE%` placeholder by running the following command:
    
    
    sed -i s@%SAMPLE_APP_IMAGE%@REGION-docker.pkg.dev/${GCP_PROJECT}/run-gmp/sample-app@g run-service-simple.yaml
    

### Deploy the Cloud Run service

After you've updated the `run-service-simple.yaml` file with your values, you can create and deploy the Cloud Run service by running the following command:
    
    
    gcloud run services replace run-service-simple.yaml --region=REGION
       

This command returns the service URL, which looks like the following:
    
    
    https://my-cloud-run-service-abcdefghij-ue.a.run.app
    

### Allow unauthenticated HTTP access

Before you can make a request to the service URL, you need to change the Cloud Run service policy to accept unauthenticated HTTP access. The `policy.yaml` file in the `run-gmp-sidecar` repository contains the necessary change.

To change the service policy, run the following command:
    
    
    gcloud run services set-iam-policy my-cloud-run-service policy.yaml --region=REGION
    

### Verify that your app is running

To verify that the Cloud Run service has correctly run the sample app, use the `curl` utility to access the service's `metrics` endpoint.

  1. Run the following command to obtain your service URL:
         
         SERVICE_URL=$(gcloud run services describe my-cloud-run-service --region=REGION --format 'value(status.url)')
         

Replace REGION with the Cloud Run region of your service.

  2. Send a request to the service URL by running the following command:
         
         curl $SERVICE_URL
         




If your app was successfully started, you see the following response:
    
    
    User request received!
    

### View app metrics in Metrics Explorer

The sample `app` container writes the following metrics:

  * `foo_metric`: The current time as a floating-point value (gauge).
  * `bar_metric`: The current time as a floating-point value (counter).



To view these metrics in Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

  3. Enter the following query into the editor pane:
         
         foo_metric
         

  4. Click **Add query**.

  5. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

  6. Enter the following query into the second editor pane:
         
         bar_metric
         

  7. Click **Run query**.

  8. To see details about the metrics, in the toggle labeled **Chart Table Both** , select **Both**.




### Clean up

When you are finished experimenting with the sample app, you can use the `clean-up-cloud-run.sh` script in the `run-gmp-sidecar` repository to delete the following resources you might have created for the sample:

  * The Cloud Run service.
  * The Artifact Registry repository.
  * The service account created for Cloud Build.



Deleting these resources ensures that you don't incur costs after running the sample.

To clean up the sample app, run the `clean-up-cloud-run.sh` script:
    
    
    ./clean-up-cloud-run.sh
    

## View self metrics in Metrics Explorer

The Managed Service for Prometheus sidecar reports the following metrics about itself to Cloud Monitoring:

  * `agent_uptime`: The uptime of the sidecar collector (counter).
  * `agent_memory_usage`: The memory being consumed by the sidecar collector (gauge).
  * `agent_api_request_count`: The number of API requests from the sidecar collector (counter).
  * `agent_monitoring_point_count`: The number of metric points written to Cloud Monitoring by the sidecar collector (counter).



To view the sidecar's self metrics in Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

  3. Enter the name of the metric you want to query into the editor pane, for example:
         
         agent_api_request_count
         

  4. Click **Run query**.

  5. To see details about the metrics, in the toggle labeled **Chart Table Both** , select **Both**.




## View self logs in Logs Explorer

The Managed Service for Prometheus sidecar writes logs to Cloud Logging. The sidecar writes logs against the Logging monitored resource type [`cloud_run_revision`](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_could_run_revision).

To view the sidecar's logs in Logs Explorer, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the **Cloud Run Revision** resource type, or enter the following query and click **Run query** :
         
         resource.type="cloud_run_revision"
         




## About the collected metrics

When the metrics emitted by the sidecar are ingested into Cloud Monitoring, the metrics are written against the Cloud Monitoring [`prometheus_target`](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target) monitored resource type. This resource type is used for both application metrics and the sidecar's self metrics.

When writing the metrics, the sidecar sets the resource labels as follows:

  * `project_id`: The ID of the Google Cloud project in which the container is running.
  * `location`: The Google Cloud region in which the container is running.
  * `cluster`: The value `__run__`.
  * `namespace`: The name of the Cloud Run service being run; comes from the `K_SERVICE` environment variable.
  * `job`: Name from the `RunMonitoring` configuration; defaults to `run-gmp-sidecar`.
  * `instance`: The value `faas.ID:PORT` of the local workload from which the container is configured to pull metrics. The faas.ID value is the instance ID of the Cloud Run instance.



The sidecar also adds the following metric labels:

  * `instanceId`: The ID of the Cloud Run instance.
  * `service_name`: The name of the Cloud Run service being run.
  * `revision_name`: The name of the Cloud Run revision being run.
  * `configuration_name`: The name of the Cloud Run configuration being run.



These metric labels are all added by default. If you use a custom `RunMonitoring` configuration, you can omit the `service_name`, `revision_name`, and `configuration_name` labels by using the `targetLabels` option in the `RunMonitoring` spec. You can also use a custom configuration to relabel the values of the `service_name`, `revision_name`, and `configuration_name` labels.

All other labels that appear with ingested metrics come from your metric. If a user-defined label conflicts with one of the system-provided labels, the user-defined label is prefixed with the string `exported_`. For example, a user-specified label `namespace="playground"` conflicts with the system-defined `namespace` label, so the user label appears as `exported_namespace="playground"`.

### Metric type

When the metrics emitted by the sidecar are ingested into Cloud Monitoring, the metrics are written as `prometheus.googleapis.com` metrics, and the type of the Prometheus metric is appended to the end of the name. For example, the sample app emits a Prometheus gauge metric named `foo_metric`. In Cloud Monitoring, the metric is stored as the metric type `prometheus.googleapis.com/foo_metric/gauge`.

When querying the metric with PromQL, you can use the Prometheus name, as illustrated in View app metrics in Metrics Explorer and View self metrics in Metrics Explorer. When using tools like the query builder or Monitoring Query Language (MQL) in Metrics Explorer, the Cloud Monitoring metric type is relevant.

### Billing

Metrics emitted by the sidecar are ingested into Cloud Monitoring with the prefix `prometheus.googleapis.com`. Metrics with this prefix are charged by the number of samples ingested. For more information about billing and Managed Service for Prometheus, see [Billing](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus#gmp-billing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
