---
url: https://docs.cloud.google.com/eventarc/standard/docs/gke/big-query-tutorial/
title: Build a BigQuery processing pipeline for Knative serving with Eventarc \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:55.041109+00:00
---

# Build a BigQuery processing pipeline for Knative serving with Eventarc  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/gke/big-query-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Build a BigQuery processing pipeline for Knative serving with Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Eventarc for GKE destinations**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial shows you how to use Eventarc to build a processing pipeline that schedules queries to a public BigQuery dataset, generates charts based on the data, and shares links to the charts through email.

## Objectives

In this tutorial, you will build and deploy three Knative serving services running in a Google Kubernetes Engine (GKE) cluster and that receive events using Eventarc:

  1. **Query runner** —Triggered when Cloud Scheduler jobs publish a message to a Pub/Sub topic; this service uses the BigQuery API to retrieve data from a public COVID-19 dataset, and saves the results in a new BigQuery table. 
  2. **Chart creator** —Triggered when the query runner service publishes a message to a Pub/Sub topic; this service generates charts using the Python plotting library, [Matplotlib](https://matplotlib.org/), and saves the charts to a Cloud Storage bucket.
  3. **Notifier** —Triggered by audit logs when the chart creator service stores a chart in a Cloud Storage bucket; this service uses the email service, [SendGrid](https://sendgrid.com/), to send links of the charts to an email address.



The following diagram shows the high-level architecture:

![BigQuery processing pipeline](https://docs.cloud.google.com/static/eventarc/images/bigquery-pipeline-anthos.svg)

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [BigQuery](https://docs.cloud.google.com/bigquery)
  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Cloud Scheduler](https://docs.cloud.google.com/scheduler)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Eventarc](https://docs.cloud.google.com/eventarc)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  7. Enable the Artifact Registry, Cloud Build, Cloud Logging, Cloud Scheduler, Eventarc, GKE, Pub/Sub, and Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com cloudresourcemanager.googleapis.com cloudscheduler.googleapis.com container.googleapis.com eventarc.googleapis.com pubsub.googleapis.com run.googleapis.com logging.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  13. Enable the Artifact Registry, Cloud Build, Cloud Logging, Cloud Scheduler, Eventarc, GKE, Pub/Sub, and Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com cloudresourcemanager.googleapis.com cloudscheduler.googleapis.com container.googleapis.com eventarc.googleapis.com pubsub.googleapis.com run.googleapis.com logging.googleapis.com

  14. For Cloud Storage, enable audit logging for the `ADMIN_READ`, `DATA_WRITE`, and `DATA_READ` data access types. 

     1. Read the Identity and Access Management (IAM) policy associated with your Google Cloud project, folder, or organization and store it in a temporary file: 
            
            gcloud projects get-iam-policy PROJECT_ID > /tmp/policy.yaml

     2. In a text editor, open `/tmp/policy.yaml`, and add or change _only_ the audit log configuration in the `auditConfigs` section: **Caution:** You must preserve the `bindings:` and `etag:` sections without changes. Changing parts of your policy not related to audit logging might make your Google Cloud project inaccessible.
            
            **  auditConfigs:
              - auditLogConfigs:
                - logType: ADMIN_READ
                - logType: DATA_WRITE
                - logType: DATA_READ
                service: storage.googleapis.com**
              bindings:
              - members:
              [...]
              etag: BwW_bHKTV5U=
              version: 1

     3. Write your new IAM policy: 
            
            gcloud projects set-iam-policy PROJECT_ID /tmp/policy.yaml

If the preceding command reports a conflict with another change, then repeat these steps, starting with reading the IAM policy. For more information, see [Configure Data Access audit logs with the API](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-api). 

  15. Set the defaults used in this tutorial: 
         
         CLUSTER_NAME=events-cluster
         CLUSTER_LOCATION=us-central1
         PROJECT_ID=PROJECT_ID
         gcloud config set project $PROJECT_ID
         gcloud config set run/region $CLUSTER_LOCATION
         gcloud config set run/cluster $CLUSTER_NAME
         gcloud config set run/cluster_location $CLUSTER_LOCATION
         gcloud config set run/platform gke
         gcloud config set eventarc/location $CLUSTER_LOCATION

Replace `PROJECT_ID` with your project ID. 




## Create a SendGrid API key

SendGrid is a cloud-based email provider that lets you send email without having to maintain email servers.

  1. [Sign in to SendGrid](https://sendgrid.com) and go to **Settings > API Keys**.
  2. Click **Create API Key**.
  3. Select the permissions for the key. At a minimum, the key must have **Mail Send** permissions to send email.
  4. Click **Save** to create the key.
  5. SendGrid generates a new key. This is the **only** copy of the key, so make sure that you copy the key and save it for later.



## Create a GKE cluster

Create a cluster with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_cluster) enabled so that it can access Google Cloud services from applications running within GKE. You also need Workload Identity Federation for GKE to forward events using Eventarc.

  1. Create a GKE cluster for Knative serving with the `CloudRun`, `HttpLoadBalancing` and `HorizontalPodAutoscaling` addons enabled:
         
         gcloud beta container clusters create $CLUSTER_NAME \
             --addons=HttpLoadBalancing,HorizontalPodAutoscaling,CloudRun \
             --machine-type=n1-standard-4 \
             --enable-autoscaling --min-nodes=2 --max-nodes=10 \
             --no-issue-client-certificate --num-nodes=2  \
             --logging=SYSTEM,WORKLOAD \
             --monitoring=SYSTEM \
             --scopes=cloud-platform,logging-write,monitoring-write,pubsub \
             --zone us-central1 \
             --release-channel=rapid \
             --workload-pool=$PROJECT_ID.svc.id.goog
         

  2. Wait a few minutes for the cluster creation to complete. During the process, you might see warnings that you can safely ignore. When the cluster has been created, the output is similar to the following:
         
         Creating cluster ...done.
         Created [https://container.googleapis.com/v1beta1/projects/my-project/zones/us-central1/clusters/events-cluster].
         

  3. Create an Artifact Registry standard repository to store your Docker container image:
         
         gcloud artifacts repositories create REPOSITORY \
             --repository-format=docker \
             --location=$CLUSTER_LOCATION

Replace `REPOSITORY` with a unique name for the repository.




## Configure the GKE service account

Configure a GKE service account to act as the default compute service account.

  1. Create an Identity and Access Management (IAM) binding between the service accounts:
         
         PROJECT_NUMBER="$(gcloud projects describe $(gcloud config get-value project) --format='value(projectNumber)')"
         
         gcloud iam service-accounts add-iam-policy-binding \
             --role roles/iam.workloadIdentityUser \
             --member "serviceAccount:$PROJECT_ID.svc.id.goog[default/default]" \
             $PROJECT_NUMBER-compute@developer.gserviceaccount.com

  2. Add the `iam.gke.io/gcp-service-account` annotation to the GKE service account, using the email address of the compute service account:
         
         kubectl annotate serviceaccount \
             --namespace default \
             default \
             iam.gke.io/gcp-service-account=$PROJECT_NUMBER-compute@developer.gserviceaccount.com




## Enable GKE destinations

To allow Eventarc to manage resources in the GKE cluster, enable GKE destinations and bind the Eventarc service account with the required roles.

  1. Enable GKE destinations for Eventarc:
         
         gcloud eventarc gke-destinations init

  2. At the prompt to bind the required roles, enter `y`.

The following roles are bound:

     * `roles/compute.viewer`
     * `roles/container.developer`
     * `roles/iam.serviceAccountAdmin`



## Create a service account and bind access roles

Before creating the Eventarc trigger, set up a user-managed service account and grant it specific roles so that Eventarc can forward Pub/Sub events.

  1. Create a service account called `TRIGGER_GSA`:
         
         TRIGGER_GSA=eventarc-bigquery-triggers
         gcloud iam service-accounts create $TRIGGER_GSA

  2. Grant the `pubsub.subscriber`, `monitoring.metricWriter`, and `eventarc.eventReceiver` roles to the service account:
         
         PROJECT_ID=$(gcloud config get-value project)
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member "serviceAccount:$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com" \
             --role "roles/pubsub.subscriber"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member "serviceAccount:$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com" \
             --role "roles/monitoring.metricWriter"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member "serviceAccount:$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com" \
             --role "roles/eventarc.eventReceiver"




## Create a Cloud Storage bucket

Create a Cloud Storage bucket to save the charts. Make sure that the bucket and the charts are publicly available, and in the same region as your GKE service:
    
    
    export BUCKET="$(gcloud config get-value core/project)-charts"
    gcloud storage buckets create gs://${BUCKET} --location=$(gcloud config get-value run/region)
    gcloud storage buckets update gs://${BUCKET} --uniform-bucket-level-access
    gcloud storage buckets add-iam-policy-binding gs://${BUCKET} --member=allUsers --role=roles/storage.objectViewer

## Clone the repository

Clone the GitHub repository.
    
    
    git clone https://github.com/GoogleCloudPlatform/eventarc-samples
    cd eventarc-samples/processing-pipelines

## Deploy the notifier service

From the `bigquery/notifier/python` directory, deploy a Knative serving service that receives chart creator events and uses SendGrid to email links to the generated charts.

  1. Build and push the container image:
         
         pushd bigquery/notifier/python
         export SERVICE_NAME=notifier
         docker build -t $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1 .
         docker push $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1
         popd

  2. Deploy the container image to Knative serving, passing in an address to send emails to, and the SendGrid API key:
         
         export TO_EMAILS=EMAIL_ADDRESS
         export SENDGRID_API_KEY=YOUR_SENDGRID_API_KEY
         gcloud run deploy ${SERVICE_NAME} \
             --image $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1 \
             --update-env-vars TO_EMAILS=${TO_EMAILS},SENDGRID_API_KEY=${SENDGRID_API_KEY},BUCKET=${BUCKET}

Replace the following:

     * `EMAIL_ADDRESS`: an email address to send the links to the generated charts
     * `YOUR_SENDGRID_API_KEY`: the SendGrid API key you noted previously



When you see the service URL, the deployment is complete.

**Note:** It can take a few minutes before permissions are propagated to the service and before you can create a trigger.

### Create a trigger for the notifier service

The Eventarc trigger for the notifier service deployed on Knative serving filters for Cloud Storage audit logs where the methodName is `storage.objects.create`.

  1. Create the trigger:
         
         gcloud eventarc triggers create trigger-${SERVICE_NAME}-gke \
             --destination-gke-cluster=$CLUSTER_NAME \
             --destination-gke-location=$CLUSTER_LOCATION \
             --destination-gke-namespace=default \
             --destination-gke-service=$SERVICE_NAME \
             --destination-gke-path=/ \
             --event-filters="type=google.cloud.audit.log.v1.written" \
             --event-filters="serviceName=storage.googleapis.com" \
             --event-filters="methodName=storage.objects.create" \
             --service-account=$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com

This creates a trigger called `trigger-notifier-gke`.




## Deploy the chart creator service

From the `bigquery/chart-creator/python` directory, deploy a Knative serving service that receives query runner events, retrieves data from a BigQuery table for a specific country, and then generates a chart, using Matplotlib, from the data. The chart is uploaded to a Cloud Storage bucket.

  1. Build and push the container image:
         
         pushd bigquery/chart-creator/python
         export SERVICE_NAME=chart-creator
         docker build -t $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1 .
         docker push $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1
         popd

  2. Deploy the container image to Knative serving, passing in `BUCKET`:
         
         gcloud run deploy ${SERVICE_NAME} \
             --image $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1 \
             --update-env-vars BUCKET=${BUCKET}




When you see the service URL, the deployment is complete.

### Create a trigger for the chart creator service

The Eventarc trigger for the chart creator service deployed on Knative serving filters for messages published to a Pub/Sub topic.

  1. Create the trigger:
         
         gcloud eventarc triggers create trigger-${SERVICE_NAME}-gke \
             --destination-gke-cluster=$CLUSTER_NAME \
             --destination-gke-location=$CLUSTER_LOCATION \
             --destination-gke-namespace=default \
             --destination-gke-service=$SERVICE_NAME \
             --destination-gke-path=/ \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account=$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com

This creates a trigger called `trigger-chart-creator-gke`.

  2. Set the Pub/Sub topic environment variable.
         
         export TOPIC_QUERY_COMPLETED=$(basename $(gcloud eventarc triggers describe trigger-${SERVICE_NAME}-gke --format='value(transport.pubsub.topic)'))




## Deploy the query runner service

From the `processing-pipelines` directory, deploy a Knative serving service that receives Cloud Scheduler events, retrieves data from a public COVID-19 dataset, and saves the results in a new BigQuery table.

  1. Build and push the container image:
         
         export SERVICE_NAME=query-runner
         docker build -t $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1 -f Dockerfile .
         docker push $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1

  2. Deploy the container image to Knative serving, passing in `PROJECT_ID` and `TOPIC_QUERY_COMPLETED`:
         
         gcloud run deploy ${SERVICE_NAME} \
             --image $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/${SERVICE_NAME}:v1 \
             --update-env-vars PROJECT_ID=$(gcloud config get-value project),TOPIC_ID=${TOPIC_QUERY_COMPLETED}




When you see the service URL, the deployment is complete.

### Create a trigger for the query runner service

The Eventarc trigger for the query runner service deployed on Knative serving filters for messages published to a Pub/Sub topic.

  1. Create the trigger:
         
         gcloud eventarc triggers create trigger-${SERVICE_NAME}-gke \
             --destination-gke-cluster=$CLUSTER_NAME \
             --destination-gke-location=$CLUSTER_LOCATION \
             --destination-gke-namespace=default \
             --destination-gke-service=$SERVICE_NAME \
             --destination-gke-path=/ \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account=$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com

This creates a trigger called `trigger-query-runner-gke`.

  2. Set an environment variable for the Pub/Sub topic.
         
         export TOPIC_QUERY_SCHEDULED=$(gcloud eventarc triggers describe trigger-${SERVICE_NAME}-gke --format='value(transport.pubsub.topic)')




## Schedule the jobs

The processing pipeline is triggered by two Cloud Scheduler jobs.

  1. Create an App Engine app which is required by Cloud Scheduler and specify an appropriate [ location](https://docs.cloud.google.com/appengine/docs/locations) (for example, `europe-west`):
         
         export APP_ENGINE_LOCATION=LOCATION
         gcloud app create --region=${APP_ENGINE_LOCATION}

  2. Create two Cloud Scheduler jobs that publish to a Pub/Sub topic once per day:
         
         gcloud scheduler jobs create pubsub cre-scheduler-uk \
             --schedule="0 16 * * *" \
             --topic=${TOPIC_QUERY_SCHEDULED} \
             --message-body="United Kingdom"
         
         gcloud scheduler jobs create pubsub cre-scheduler-cy \
             --schedule="0 17 * * *" \
             --topic=${TOPIC_QUERY_SCHEDULED} \
             --message-body="Cyprus"

The schedule is specified in [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules). For example, `0 16 * * *` means that the jobs runs at 16:00 (4 PM) UTC every day.




## Run the pipeline

  1. Confirm that all the triggers were successfully created:
         
         gcloud eventarc triggers list

**Note:** It can take up to two minutes for triggers to be fully functional.

The output should be similar to the following:
         
         NAME                       TYPE                                            DESTINATION         ACTIVE  LOCATION
         trigger-chart-creator-gke  google.cloud.pubsub.topic.v1.messagePublished   GKE:chart-creator   Yes     us-central1
         trigger-notifier-gke       google.cloud.audit.log.v1.written               GKE:notifier        Yes     us-central1
         trigger-query-runner-gke   google.cloud.pubsub.topic.v1.messagePublished   GKE:query-runner    Yes     us-central1
         

  2. Retrieve the Cloud Scheduler job IDs:
         
         gcloud scheduler jobs list

The output should be similar to the following:
         
         ID                LOCATION      SCHEDULE (TZ)         TARGET_TYPE  STATE
         cre-scheduler-cy  us-central1   0 17 * * * (Etc/UTC)  Pub/Sub      ENABLED
         cre-scheduler-uk  us-central1   0 16 * * * (Etc/UTC)  Pub/Sub      ENABLED
         

  3. Although the jobs are scheduled to run daily at 4 and 5 PM, you can also run the Cloud Scheduler jobs manually:
         
         gcloud scheduler jobs run cre-scheduler-cy
         gcloud scheduler jobs run cre-scheduler-uk

  4. After a few minutes, confirm that there are two charts in the Cloud Storage bucket:
         
         gcloud storage ls gs://${BUCKET}

The output should be similar to the following:
         
         gs://PROJECT_ID-charts/chart-cyprus.png
         gs://PROJECT_ID-charts/chart-unitedkingdom.png
         




Congratulations! You should also receive two emails with links to the charts.

## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and want to keep it without the changes added in this tutorial, delete the resources created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete tutorial resources

  1. Delete any Knative serving services you deployed in this tutorial:
         
         gcloud run services delete SERVICE_NAME

Where `SERVICE_NAME` is your chosen service name.

You can also delete Knative serving services from the [Google Cloud console](https://console.cloud.google.com/kubernetes/run).

  2. Delete any Eventarc triggers you created in this tutorial:
         
         gcloud eventarc triggers delete TRIGGER_NAME
         

Replace `TRIGGER_NAME` with the name of your trigger.

  3. Remove any Google Cloud CLI default configurations you added during the tutorial setup.
         
         gcloud config unset project
         gcloud config unset run/cluster
         gcloud config unset run/cluster_location
         gcloud config unset run/platform
         gcloud config unset eventarc/location
         gcloud config unset compute/zone

  4. Delete the images from Artifact Registry.
         
         gcloud artifacts docker images delete $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/notifier:v1
         gcloud artifacts docker images delete $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/chart-creator:v1
         gcloud artifacts docker images delete $CLUSTER_LOCATION-docker.pkg.dev/$(gcloud config get-value project)/REPOSITORY/query-runner:v1

  5. Delete the bucket, along with all the objects within the bucket:
         
         gcloud storage rm --recursive gs://${BUCKET}/

  6. Delete the Cloud Scheduler jobs:
         
         gcloud scheduler jobs delete cre-scheduler-cy
         gcloud scheduler jobs delete cre-scheduler-uk




## What's next

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)
  * [Learn more about Knative serving](https://docs.cloud.google.com/anthos/run/docs/architecture-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
