---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/kafka-autoscaler/
title: Autoscale worker pools with external metrics \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:05:23.820636+00:00
---

# Autoscale worker pools with external metrics  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/kafka-autoscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Autoscale worker pools with external metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to autoscale Cloud Run worker pools using external event-driven metrics. Cloud Run External Metrics Autoscaling (CREMA) enables this functionality by leveraging [Kubernetes-based Event Driven Autoscaling (KEDA)](https://github.com/kedacore/keda) to scale workloads based on external event sources.

For supported scalers and compatibility with Cloud Run, see [Cloud Run External Metrics Autoscaling (CREMA)](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/tree/main?tab=readme-ov-file#compatibility) in the Google Cloud GitHub documentation.

## About the autoscaler service

To autoscale worker pools, deploy the CREMA autoscaler service to Cloud Run. This service performs the following actions:

  1. Polls external event sources, such as [Apache Kafka](https://keda.sh/docs/2.17/scalers/apache-kafka/) topics or [GitHub Runner Scaler](https://keda.sh/docs/2.17/scalers/github-runner/).

  2. Calculates the required instance count based on your [YAML configuration](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/tree/main?tab=readme-ov-file#compatibility).

  3. Updates the worker pool's instance count automatically.




## Before you begin

  1. Make sure you have set up a new project for Cloud Run, as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.

  2. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, Secret Manager, and Parameter Manager APIs:
         
         gcloud services enable artifactregistry.googleapis.com \
             cloudbuild.googleapis.com \
             run.googleapis.com \
             secretmanager.googleapis.com \
             parametermanager.googleapis.com
         

  3. Configure an event-driven or request-based workload, such as GitHub Runners or Apache Kafka. To verify that your workload source is supported, see the [CREMA compatibility list](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/tree/main?tab=readme-ov-file#compatibility) in the Google Cloud GitHub documentation.

  4. Review the [pricing calculator](https://cloud.google.com/products/calculator?_gl=1*2gq39x*_ga*MTkxNjkwODgyMy4xNzY0ODk5NjEy*_ga_4LYFWVHBEB*czE3NjUzMjkwNjQkbzEkZzEkdDE3NjUzMzI4MzQkajEwJGwwJGgw) to estimate costs. You incur charges for your Cloud Run scaling service based on how often you trigger scaling.




## Required roles

To get the permissions that you need to autoscale your worker pool, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to autoscale your worker pool. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Create a custom service account

Create a custom service account with the [minimum permissions required](https://docs.cloud.google.com/iam/docs/using-iam-securely) to use provisioned resources required for your workload. To set up the service account, do the following:
    
    
    gcloud iam service-accounts create CREMA_SERVICE_ACCOUNT \
      --display-name="CREMA Service Account"
    

Replace CREMA_SERVICE_ACCOUNT with a name for your custom service account, for example `crema-service-account`. This command creates a service account that follows the format, `crema-service-account@example-project.iam.gserviceaccount.com`.

## Create the CREMA configuration file

To define your scaling logic, create a YAML configuration file in your root directory. This file instructs the CREMA service on which external sources to monitor, how to authenticate with the resources, and which worker pools to scale.

### YAML example

The following example shows the configuration file to scale a Cloud Run worker pool (`example-workerpool`) using the [GitHub Runner](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners) metrics. It uses a Secret Manager secret named `github_runner_token` to authenticate with GitHub for reading the metrics.
    
    
      apiVersion: crema/v1
      kind: CremaConfig
      metadata:
        name: gh-demo
      spec:
        triggerAuthentications:
          - metadata:
              name: github-trigger-auth
            spec:
              gcpSecretManager:
                secrets:
                  - parameter: personalAccessToken
                    id: github_runner_token
                    version: latest
        scaledObjects:
          - spec:
              scaleTargetRef:
                name: projects/example-project/locations/us-central1/workerpools/example-workerpool
              triggers:
                - type: github-runner
                  name: example-runner
                  metadata:
                    owner: repo-owner
                    runnerScope: repo
                    repos: repo-name
                    targetWorkflowQueueLength: 1
                  authenticationRef:
                    name: github-trigger-auth
              advanced:
                horizontalPodAutoscalerConfig:
                  behavior:
                    scaleDown:
                      stabilizationWindowSeconds: 10
                      policies:
                        - type: Pods
                          value: 100
                          periodSeconds: 10
                    scaleUp:
                      stabilizationWindowSeconds: 10
                      policies:
                        - type: Pods
                          value: 2
                          periodSeconds: 10
            pollingInterval: 10
    

The YAML configuration uses the following high-level parameters:

  * `triggerAuthentications`: determines how CREMA authenticates the external service, such as using a token stored in Secret Manager.

  * `scaledObjects`: defines the mapping between your Cloud Run worker pool and the external metric resource. This parameter includes:

    * `scaleTargetRef`: the Cloud Run services or worker pools to scale.

    * `triggers`: the specific external metric used for scaling. If your external metric source requires authentication, set the `authenticationRef` field to specify one of the `TriggerAuthentications` objects for credentials.

  * `pollingInterval`: controls the interval (in seconds) at which CREMA refreshes its metrics. If you omit this parameter, CREMA doesn't poll automatically, and you must trigger a scaling check manually using a POST request to the service.




For more information on defining basic and advanced configuration metrics, see [Configuration reference](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/blob/main/metric-provider/api/README.md) in the Google Cloud GitHub documentation.

For the complete list of configuration definitions for your compatible scalers, see [Scalers](https://keda.sh/docs/2.17/scalers/) in the KEDA documentation.

## Store your CREMA configuration in Parameter Manager

To store parameter versions for your CREMA autoscaler service, follow these steps:

  1. Create a parameter in the Parameter Manager:
         
         gcloud parametermanager parameters create PARAMETER_ID --location=global  --parameter-format=YAML
         

Replace PARAMETER_ID with the name of your parameter.

  2. Upload your local YAML file as a new parameter version:
         
         gcloud parametermanager parameters versions create PARAMETER_VERSION \
           --location=global \
           --parameter=PARAMETER_ID \
           --payload-data-from-file=LOCAL_YAML_CONFIG_FILE
         

Replace the following:

     * PARAMETER_VERSION: the ID that you want to assign to the parameter version, for example, `1`.
     * LOCAL_YAML_CONFIG_FILE: the path to your YAML configuration file.



For more information, see [Create a parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter).

## Grant additional permissions to your CREMA service account

To scale the worker pool you specified in your YAML configuration, grant the following permissions on the custom service account:

  1. Grant your CREMA service account permission to read from the Parameter Manager:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:CREMA_SERVICE_ACCOUNT_NAME \
           --role="roles/parametermanager.parameterViewer"
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.

     * CREMA_SERVICE_ACCOUNT_NAME: the name of your CREMA service account.

  2. Grant your CREMA service account the `roles/run.developer` role on the worker pool. This allows the CREMA service to modify the instance count of your worker pool in response to changing metrics:
         
         WORKER_POOL_NAME=WORKER_POOL_NAME
         WORKER_POOL_REGION=WORKER_POOL_REGION
         gcloud run worker-pools add-iam-policy-binding $WORKER_POOL_NAME \
           --region=$WORKER_POOL_REGION \
           --member="serviceAccount:CREMA_SERVICE_ACCOUNT_NAME" \
           --role="roles/run.developer"
         

Replace the following:

     * WORKER_POOL_NAME: the name of the worker pool.
     * WORKER_POOL_REGION: the region of your worker pool.
  3. Grant your CREMA service account permission to write metrics:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:CREMA_SERVICE_ACCOUNT_NAME" \
            --role="roles/monitoring.metricWriter"
         

  4. Grant your CREMA service account the service account user role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:CREMA_SERVICE_ACCOUNT_NAME" \
           --role="roles/iam.serviceAccountUser"
         




### Deploy the service to scale your workloads

To deploy the service to scale your worker pool, run the following command with a prebuilt container image:
    
    
    gcloud run deploy SERVICE_NAME\
      --image=us-central1-docker.pkg.dev/cloud-run-oss-images/crema-v1/autoscaler:1.0 \
      --region=SERVICE_REGION \
      --service-account="CREMA_SERVICE_ACCOUNT_NAME" \
      --no-allow-unauthenticated \
      --no-cpu-throttling \
      --base-image=us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/java25 \
      --labels=created-by=crema \
      --set-env-vars="CREMA_CONFIG=projects/PROJECT_ID/locations/PARAMETER_REGION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION,OUTPUT_SCALER_METRICS=True"
    

Replace the following:

  * SERVICE_NAME: the name of your autoscaler service.

  * SERVICE_REGION: the region of your service.

  * CREMA_SERVICE_ACCOUNT_NAME: the name of your CREMA service account.

  * PROJECT_ID: the ID of your Google Cloud project.

  * PARAMETER_REGION, PARAMETER_ID, and PARAMETER_VERSION: values you stored in the Parameter Manager.




You can also deploy your CREMA service using a [custom container image you build](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling?tab=readme-ov-file#optional-build-the-container-image-from-source) from the source code with Cloud Build.

## Test your CREMA service

To verify your autoscaling service is working correctly, [check the **Logs** tab of the Cloud Run service](https://docs.cloud.google.com/run/docs/logging#service-logs).

You should see the following logs in your service's logs each time metrics are refreshed:

Each log message is labeled with the component that emitted it.
    
    
    [INFO] [METRIC-PROVIDER] Starting metric collection cycle
    [INFO] [METRIC-PROVIDER] Successfully fetched scaled object metrics ...
    [INFO] [METRIC-PROVIDER] Sending scale request ...
    [INFO] [SCALER] Received ScaleRequest ...
    [INFO] [SCALER] Current instances ...
    [INFO] [SCALER] Recommended instances ...
    

## What's next

  * Learn how to use [self-hosted GitHub runners on worker pools to execute the workflows defined in your GitHub repository, and scale your worker pool with CREMA](https://docs.cloud.google.com/run/docs/tutorials/github-runner).

  * Learn more about [Cloud Run worker pools](https://docs.cloud.google.com/run/docs/deploy-worker-pools). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
