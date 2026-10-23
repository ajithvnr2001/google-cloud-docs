---
url: https://docs.cloud.google.com/run/docs/tutorials/autoscale-vllm-with-gpu-metrics/
title: Autoscale vLLM model serving with GPU metrics \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:41:00.447328+00:00
---

# Autoscale vLLM model serving with GPU metrics  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/autoscale-vllm-with-gpu-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)



Send feedback 

#  Autoscale vLLM model serving with GPU metrics Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to autoscale your Cloud Run services serving LLMs with [vLLM](https://docs.vllm.ai/) based on custom GPU metrics using [Cloud Run External Metrics Autoscaling (CREMA)](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/tree/main).

Although Cloud Run autoscales using CPU utilization and concurrency by default, GPU-intensive inference workloads often require autoscaling based on queue metrics, such as the number of running requests or KV cache utilization. CREMA integrates Kubernetes-based Event Driven Autoscaling (KEDA) with Cloud Run to enable dynamic scaling driven by Prometheus metrics. vLLM exposes the Prometheus metrics and sends them to Cloud Monitoring.

## Objectives

In this tutorial, you will:

  * Download and upload model weights to Cloud Storage
  * Push the vLLM container image to Artifact Registry
  * Deploy the CREMA autoscaler service
  * Configure vLLM service permissions
  * Deploy vLLM service with OpenTelemetry sidecar
  * Check CREMA service logs
  * Run a load test
  * Explore vLLM metrics in Cloud Monitoring



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



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

  6. Enable the Cloud Run, Parameter Manager, Artifact Registry, Cloud Build, Secret Manager, and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,parametermanager.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com,secretmanager.googleapis.com,monitoring.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Set environment variables used throughout this tutorial: 
         
         export PROJECT_ID=PROJECT_ID
         export REGION=us-central1
         export VLLM_SERVICE_NAME=vllm-service
         export MODEL_NAME=gemma-2-2b-it
         export REPO_NAME=vllm-repo
         export BUCKET_NAME=my-vllm-models-${PROJECT_ID}
         export CREMA_SERVICE_NAME=crema-service

Replace PROJECT_ID with your Google Cloud project ID.
  9. Set your project configuration: 
         
         gcloud config set project $PROJECT_ID

  10. If you don't have one already, make an account at [Hugging Face](https://huggingface.co/). Then, create a **read** token on the [Hugging Face](https://huggingface.co/settings/tokens) site. Hugging Face only displays the token once. Save it in a secure location, you won't be able to view it again.
  11. Navigate to the [gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it) model page on Hugging Face and accept the model's terms of agreement.



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Download and upload model weights to Cloud Storage

Download model weights from Hugging Face and transfer them to a Cloud Storage bucket to make them available for model serving:

  1. Install the Hugging Face CLI:
         
         pip install -U "huggingface_hub[cli]"
         

  2. Download the model weights locally using the Hugging Face CLI:
         
         export HF_TOKEN="HF_TOKEN"
         export LOCAL_DIR="/tmp/$MODEL_NAME"
         HF_HOME=/tmp/huggingface python -m huggingface_hub.cli.hf download google/$MODEL_NAME --token $HF_TOKEN --local-dir=$LOCAL_DIR
         

Replace HF_TOKEN with your Hugging Face user access token. The token should begin with `hf_` followed by 35 random alphanumeric characters (for example, `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`).

  3. Create a Cloud Storage bucket and copy the downloaded weights:
         
         gcloud storage buckets create gs://$BUCKET_NAME \
             --project=$PROJECT_ID \
             --location=$REGION \
             --uniform-bucket-level-access
         
         gcloud storage cp -r $LOCAL_DIR gs://$BUCKET_NAME/
         




## Push the vLLM container image to Artifact Registry

Pull your model serving container images and push them to a repository in Artifact Registry:

  1. Create a Docker repository in Artifact Registry:
         
         gcloud artifacts repositories create $REPO_NAME \
             --repository-format=docker \
             --location=$REGION \
             --description="vLLM Docker Images"
         

  2. Authenticate local Docker daemon with the registry:
         
         gcloud auth configure-docker ${REGION}-docker.pkg.dev
         

  3. Pull the vLLM image, tag it, and push it to Artifact Registry:
         
         docker pull docker.io/vllm/vllm-openai:latest
         docker tag docker.io/vllm/vllm-openai:latest ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/vllm-openai:latest
         docker push ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/vllm-openai:latest
         




## Deploy the CREMA autoscaler service

Configure service account roles and parameter manifests for CREMA before deploying the autoscaler service.

### Create a custom service account

Create a custom service account with [minimum permissions required](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) to use the provisioned resources. This service account acts as the identity for the autoscaler. Run the following command to create the CREMA service account:
    
    
    export CREMA_SA="crema-autoscaler@${PROJECT_ID}.iam.gserviceaccount.com"
    
    gcloud iam service-accounts create crema-autoscaler \
        --description="Service account for Cloud Run CREMA to read metrics and scale workloads" \
        --display-name="CREMA Autoscaler System"
    

### Grant additional permissions to your custom service account

To scale the service, grant the following permissions on the custom service account:

  1. Grant your CREMA service account permission to read from the Parameter Manager:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$CREMA_SA" \
             --role="roles/parametermanager.parameterViewer"
         

  2. Grant your CREMA service account permission to scale the service:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$CREMA_SA" \
             --role="roles/run.developer"
         

  3. Grant your CREMA service account the service account user role:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$CREMA_SA" \
             --role="roles/iam.serviceAccountUser"
         

  4. Grant your CREMA service account permission to view metrics:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$CREMA_SA" \
             --role="roles/monitoring.viewer"
         




### Create and register the CREMA configuration

Define scaling thresholds and rules in a CREMA configuration manifest and register it in Parameter Manager:

  1. Save the following configuration as `my-crema-config.yaml`. This configuration triggers scaling when the number of running requests (`vllm:num_requests_running`) exceeds 2:
         
         apiVersion: crema/v1
         kind: CremaConfig
         spec:
           pollingInterval: 15
           triggerAuthentications:
             - metadata:
                 name: adc-trigger-auth
               spec:
                 podIdentity:
                   provider: gcp
           scaledObjects:
             - spec:
                 scaleTargetRef:
                   name: projects/PROJECT_ID/locations/us-central1/services/vllm-service
                 minReplicaCount: 1
                 maxReplicaCount: 5
                 triggers:
                   - type: prometheus
                     authenticationRef:
                       name: adc-trigger-auth
                     metadata:
                       serverAddress: https://monitoring.googleapis.com/v1/projects/PROJECT_ID/location/global/prometheus
                       metric: vllm:num_requests_running
                       query: sum(vllm:num_requests_running)
                       threshold: '2'
         

  2. Register the configuration file in Parameter Manager:
         
         gcloud parametermanager parameters create crema-config \
             --location=global \
             --parameter-format=YAML
         
         gcloud parametermanager parameters versions create 1 \
             --location=global \
             --parameter=crema-config \
             --payload-data-from-file=my-crema-config.yaml
         




### Deploy the CREMA service

Deploy the CREMA image as an internal background service on Cloud Run:
    
    
    gcloud run deploy $CREMA_SERVICE_NAME \
        --image=us-central1-docker.pkg.dev/cloud-run-oss-images/crema-v1/autoscaler:1.0 \
        --region=$REGION \
        --service-account="$CREMA_SA" \
        --no-allow-unauthenticated \
        --no-cpu-throttling \
        --cpu=1 \
        --memory=1Gi \
        --min-instances=1 \
        --max-instances=1 \
        --ingress=internal \
        --base-image=us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/java25 \
        --set-env-vars="CREMA_CONFIG=projects/$PROJECT_ID/locations/global/parameters/crema-config/versions/1,OUTPUT_SCALER_METRICS=True"
    

## Configure vLLM service permissions

Grant the default Compute Engine service account permissions to export metrics and read model weights from Cloud Storage:

  1. Retrieve your project number:
         
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
         

  2. Grant your service account permission to write metrics:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/monitoring.metricWriter"
         

  3. Grant your service account permission to read model weights from Cloud Storage:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/storage.objectViewer"
         




## Deploy vLLM service with OpenTelemetry sidecar

Deploy your primary vLLM serving container to Cloud Run with model weights mounted from Cloud Storage. Because deploying multi-container services with sidecars on Cloud Run requires a declarative YAML service specification, you configure the primary vLLM engine alongside an OpenTelemetry sidecar collector to scrape and export vLLM metrics:

  1. Save the following multi-container deployment specification as `vllm-service.yaml`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: vllm-service
           labels:
             cloud.googleapis.com/location: us-central1
           annotations:
             run.googleapis.com/scalingMode: manual
             run.googleapis.com/manualInstanceCount: "1"
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/execution-environment: gen2
                 run.googleapis.com/cpu-throttling: "false"
                 run.googleapis.com/gpu-zonal-redundancy-disabled: "true"
                 autoscaling.knative.dev/minScale: "1"
             spec:
               containerConcurrency: 80
               nodeSelector:
                 run.googleapis.com/accelerator: nvidia-l4
               volumes:
                 - name: gcs-volume
                   csi:
                     driver: gcsfuse.run.googleapis.com
                     volumeAttributes:
                       bucketName: my-vllm-models-PROJECT_ID
               containers:
                 # Primary container: vLLM serving engine
                 - name: vllm-container
                   image: us-central1-docker.pkg.dev/PROJECT_ID/vllm-repo/vllm-openai:latest
                   ports:
                     - containerPort: 8080
                   resources:
                     limits:
                       cpu: "4"
                       memory: 16Gi
                       nvidia.com/gpu: "1"
                   args:
                     - "--model"
                     - "/gcs/gemma-2-2b-it"
                     - "--port"
                     - "8080"
                     - "--max-model-len"
                     - "2048"
                     - "--chat-template"
                     - "{% for msg in messages %}{{ msg['content'] }}{% endfor %}"
                   volumeMounts:
                     - name: gcs-volume
                       mountPath: /gcs
                   startupProbe:
                     httpGet:
                       path: /health
                       port: 8080
                     periodSeconds: 10
                     failureThreshold: 24
         
                 # Sidecar container: OpenTelemetry Collector
                 - name: otel-collector
                   image: otel/opentelemetry-collector-contrib:latest
                   resources:
                     limits:
                       cpu: "1"
                       memory: 1Gi
                   args:
                     - |
                       --config=yaml:
                       receivers:
                         prometheus:
                           config:
                             scrape_configs:
                               - job_name: 'vllm'
                                 scrape_interval: 10s
                                 metrics_path: '/metrics'
                                 static_configs:
                                   - targets: ['localhost:8080']
                       processors:
                         resourcedetection:
                           detectors: [gcp]
                           timeout: 2s
                         transform:
                           metric_statements:
                             - context: datapoint
                               statements:
                                 - set(attributes["exported_location"], attributes["location"])
                                 - delete_key(attributes, "location")
                                 - set(attributes["exported_cluster"], attributes["cluster"])
                                 - delete_key(attributes, "cluster")
                                 - set(attributes["exported_namespace"], attributes["namespace"])
                                 - delete_key(attributes, "namespace")
                                 - set(attributes["exported_job"], attributes["job"])
                                 - delete_key(attributes, "job")
                                 - set(attributes["exported_instance"], attributes["instance"])
                                 - delete_key(attributes, "instance")
                       exporters:
                         googlemanagedprometheus:
                       service:
                         pipelines:
                           metrics:
                             receivers: [prometheus]
                             processors: [resourcedetection, transform]
                             exporters: [googlemanagedprometheus]
         

  2. Replace the existing service configuration with the multi-container manifest:
         
         gcloud run services replace vllm-service.yaml
         




## Check CREMA service logs

  1. In the Google Cloud console, navigate to the **Cloud Run** page.
  2. Select your `crema-service`.
  3. Click the **Logs** tab and verify that metric polling cycles are active:
         
         [INFO] [METRIC-PROVIDER] Starting metric collection cycle
         [INFO] [METRIC-PROVIDER] Successfully fetched scaled object metrics ...
         [INFO] [METRIC-PROVIDER] Sending scale request ...
         [INFO] [SCALER] Received ScaleRequest ...
         [INFO] [SCALER] Current instances ...
         [INFO] [SCALER] Recommended instances ...
         




## Run a load test

To test autoscaling, run a load testing script to send concurrent requests to the vLLM service:

  1. In your working directory, create a file named `load-test.sh` and add the following code:
         
         #!/bin/bash
         
         export SERVICE_URL=$(gcloud run services describe $VLLM_SERVICE_NAME --region $REGION --format='value(status.url)')
         
         echo "Launching 5 parallel heavy requests to trigger autoscaling..."
         
         for i in {1..5}; do
             curl -s -X POST "${SERVICE_URL}/v1/chat/completions" \
                 -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
                 -H "Content-Type: application/json" \
                 -d "{
                     \"model\": \"/gcs/${MODEL_NAME}\",
                     \"messages\": [{\"role\": \"user\", \"content\": \"Write an exceptionally long, detailed, and exhaustive essay about the entire history of the universe from the Big Bang to the modern day.\"}]
                 }" > /dev/null &
         done
         
         echo "All 5 requests dispatched. Waiting for requests to complete..."
         wait
         echo "Done."
         

  2. Make the script executable and run the load test:
         
         chmod +x load-test.sh
         ./load-test.sh
         

  3. Re-check the `crema-service` logs and Cloud Run metrics dashboard to verify that the recommended instance count scales up in response to the queued requests.




## Explore vLLM metrics in Cloud Monitoring

After running the load test, explore how traffic affects the model serving metrics in Cloud Monitoring:

  1. In the Google Cloud console, go to the **[Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)** page in Cloud Monitoring.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Click **Select a metric**.

  3. Expand **Prometheus Target** > **Vllm** and select any of the available metrics ending in `/gauge`. For example, select `prometheus/vllm:num_requests_running/gauge` to view the active request count during the load test.




As described in the [vLLM production metrics documentation](https://docs.vllm.ai/en/stable/design/metrics/#v1-metrics), additional vLLM metrics exported to Cloud Monitoring include:

  * `prometheus/vllm:num_requests_waiting/gauge`: The number of requests waiting in the queue to be processed by the vLLM engine.
  * `prometheus/vllm:num_requests_running/gauge`: The number of requests executing in model batches.
  * `prometheus/vllm:gpu_cache_usage_perc/gauge`: The percentage of GPU KV-cache memory utilized.
  * `prometheus/vllm:num_requests_swapped/gauge`: The number of requests whose KV cache was swapped to host CPU memory due to memory pressure.



Although this tutorial scales based on `vllm:num_requests_running`, you can use any of these vLLM metrics in your CREMA configuration to customize autoscaling rules for your workloads based on queue size, KV-cache utilization, or request swapping.

Unlike standard HTTP request concurrency metrics that treat all requests equally, vLLM's internal metrics account for the dynamic GPU memory footprint of different prompt lengths. Scaling on `vllm:num_requests_running` helps you scale proactively based on genuine GPU load. This maintains an active capacity buffer before the server is forced to queue requests into `vllm:num_requests_waiting`, protecting users from severe Time To First Token (TTFT) latency spikes.

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
         

  4. Delete the CREMA configuration assigned to Parameter Manager:
         
         gcloud parametermanager parameters delete crema-config \
             --location=global \
             --quiet
         

  5. Delete the custom service account created for CREMA:
         
         gcloud iam service-accounts delete $CREMA_SA \
             --quiet
         

  6. Delete the Cloud Storage bucket containing the model:
         
         gcloud storage rm --recursive gs://$BUCKET_NAME
         

  7. Delete other Google Cloud resources created in this tutorial:

     * [Delete the Cloud Run vLLM service](https://docs.cloud.google.com/run/docs/managing/services#delete)
     * [Delete the CREMA service](https://docs.cloud.google.com/run/docs/managing/services#delete)
     * [Delete the Docker repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos) in Artifact Registry



## What's next

  * Learn more about [CREMA autoscaling on Cloud Run](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/tree/main).
  * Read more about deploying [Gemma models on Cloud Run](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
