---
url: https://docs.cloud.google.com/anthos/run/docs/events/quickstart/
title: Migrate Pub/Sub triggers from Events for Cloud Run for Anthos to Eventarc \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:06.533120+00:00
---

# Migrate Pub/Sub triggers from Events for Cloud Run for Anthos to Eventarc  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/run/docs/events/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Migrate Pub/Sub triggers from Events for Cloud Run for Anthos to Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Important:** Events for Cloud Run for Anthos (now known as [Knative serving)](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs) is no longer actively supported. For details, see [Feature deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations). We recommend that you [create an Eventarc trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) so that you can receive events using Eventarc.

You can migrate event triggers so that a Google Kubernetes Engine (GKE) service (including Knative serving services) can receive Pub/Sub events using Eventarc. This guide assumes that you are migrating [existing event triggers](https://docs.cloud.google.com/anthos/run/archive/docs/triggering/migrate-events-anthos-triggers) and that your GKE service is running in a GKE cluster. A migration needs to be run for _each_ cluster.

This migration path avoids the loss of events while minimizing their duplication.

**Note:** If a migration with _no_ duplicated events is required, contact [eventarc@google.com](mailto:eventarc@google.com) for technical assistance and further information.

The migration involves the following:

  1. To allow Eventarc to manage resources in the GKE cluster, enable GKE destinations.
  2. If necessary, enable Workload Identity for the GKE cluster running your target GKE service.
  3. Identify existing event triggers.
  4. Create an Eventarc trigger that points to the same GKE service as the existing trigger.
  5. Confirm that the Eventarc trigger is delivering events as expected.
  6. Delete the original event trigger and clean up after migration.



## Before you begin

This guide assumes that you already have:

  * [A Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * [A Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).



### Set up the command-line environment

To set up the `gcloud` and `kubectl` command-line tools:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Sign in using your account:
         
         gcloud auth login

  3. Set the default settings for the gcloud CLI:
         
         gcloud config set project PROJECT_ID
         gcloud config set run/cluster CLUSTER_NAME
         gcloud config set run/cluster_location CLUSTER_LOCATION
         gcloud config set run/platform gke
         gcloud config set eventarc/location LOCATION

Replace the following:

     * `PROJECT_ID`: your project ID
     * `CLUSTER_NAME`: the name of your cluster
     * `CLUSTER_LOCATION`: any [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where GKE is supported; for example: `us-central1-a`.
     * `LOCATION`: a [location](https://docs.cloud.google.com/eventarc/docs/locations) for the Eventarc trigger; for example: `us-central1`.
  4. Enable the following APIs for the project:
         
         gcloud services enable cloudapis.googleapis.com
         gcloud services enable cloudbuild.googleapis.com
         gcloud services enable cloudresourcemanager.googleapis.com
         gcloud services enable container.googleapis.com
         gcloud services enable containerregistry.googleapis.com
         gcloud services enable eventarc.googleapis.com

  5. Install the `kubectl` command-line tool:
         
         gcloud components install kubectl

  6. Update installed gcloud CLI components:
         
         gcloud components update




## Enable GKE destinations

To allow Eventarc to manage resources in the GKE cluster, enable GKE destinations, and bind the Eventarc service account with the required roles.

  1. Enable GKE destinations for Eventarc:
         
         gcloud eventarc gke-destinations init

  2. At the prompt to bind the required roles, enter `y`.

The following roles are bound:

     * `roles/compute.viewer`
     * `roles/container.developer`
     * `roles/iam.serviceAccountAdmin`



## Enable Workload Identity Federation for GKE on a cluster

If Workload Identity Federation for GKE is already enabled on your cluster, you can skip this step.

Workload Identity Federation for GKE is the recommended way to access Google Cloud services from applications running within GKE due to its improved security properties and manageability. It is also needed to forward GKE events using Eventarc.

To enable Workload Identity Federation for GKE on an existing cluster, refer to [Using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

## Identify existing event triggers

Before migrating any existing event triggers, you must retrieve the trigger details.

  1. List the existing event triggers for the GKE cluster:
         
         gcloud beta events triggers list --namespace EVENTS_NAMESPACE
         

Replace `EVENTS_NAMESPACE` with the namespace of your events broker.

The output is similar to the following:
         
         TRIGGER             EVENT TYPE                                     TARGET
         ✔  trigger-id          google.cloud.pubsub.topic.v1.messagePublished  cloud-run-service-name
         

  2. You will need the topic ID to create the Eventarc trigger. Retrieve the topic ID for the existing event trigger:
         
         gcloud beta events triggers describe TRIGGER_ID \
           --platform gke --namespace EVENTS_NAMESPACE \
           --format="flattened(serialized_source.spec.topic,serialized_trigger.spec.filter.attributes.type,serialized_trigger.spec.subscriber.ref.name,serialized_trigger.spec.subscriber.ref.namespace)"
         

Replace `TRIGGER_ID` with the ID of the existing event trigger or a fully qualified identifier.

The output is similar to the following:
         
         topic:     topic-id
         type:      google.cloud.pubsub.topic.v1.messagePublished
         name:      cloud-run-service-name
         namespace: events
         




## Create an Eventarc trigger to replace the existing trigger

Before creating the Eventarc trigger, set up a user-managed service account and grant it specific roles so that Eventarc can manage events for GKE destinations.

  1. Create a Google Cloud service account (GSA):
         
         TRIGGER_GSA=SERVICE_ACCOUNT_NAME
         gcloud iam service-accounts create $TRIGGER_GSA

Replace `SERVICE_ACCOUNT_NAME` with a name that is between 6 and 30 characters. It can contain lowercase alphanumeric characters and dashes.

  2. Grant the `pubsub.subscriber` and `monitoring.metricWriter` roles to the service account:
         
         PROJECT_ID=$(gcloud config get-value project)
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member "serviceAccount:$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com" \
           --role "roles/pubsub.subscriber"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member "serviceAccount:$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com" \
           --role "roles/monitoring.metricWriter"

  3. Create a new Eventarc trigger based on the existing event trigger's configuration. All the arguments, including the destination service, cluster, and topic ID, should match that of the existing event trigger.
         
         gcloud eventarc triggers create EVENTARC_TRIGGER_NAME \
           --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
           --location LOCATION \
           --destination-gke-service=DESTINATION_SERVICE \
           --destination-gke-cluster=CLUSTER_NAME  \
           --destination-gke-location=CLUSTER_LOCATION  \
           --destination-gke-namespace=EVENTS_NAMESPACE  \
           --destination-gke-path=/ \
           --service-account=$TRIGGER_GSA@$PROJECT_ID.iam.gserviceaccount.com \
           --transport-topic=projects/PROJECT_ID/topics/TOPIC_ID

Replace `EVENTARC_TRIGGER_NAME` with a name for the new Eventarc trigger and TOPIC_ID with the Pub/Sub topic ID that you retrieved previously.

This creates an Eventarc trigger for the Pub/Sub topic ID.

  4. Confirm that the trigger was successfully created:
         
         gcloud eventarc triggers list

The output is similar to the following:
         
         NAME                  TYPE                                           DESTINATION_RUN_SERVICE  DESTINATION_RUN_PATH  ACTIVE
         eventarc-trigger-name google.cloud.pubsub.topic.v1.messagePublished                                                 Yes
         




## Test the migration and verifying the output

**Caution:** Before moving to production, verify and validate that events are being delivered and received as expected by your GKE service.

To test your migration, trigger a test event by publishing to a Pub/Sub topic, and then verify that there is at least one event delivered for each of the existing event triggers and Eventarc triggers, respectively.

For example, the output after triggering a test event would be duplicated, and would be similar to the following:
    
    
      Hello, World! ID: 2896291125947199
      Hello, World! ID: 2896291125947199

You can also use the following scenario for guidance in which the event receiver can display the event data:

  1. Publish a message to the Pub/Sub topic:
         
         gcloud pubsub topics publish TOPIC_ID \
           --message "Hello, World!"
         

  2. Verify the event and its successful delivery. For example, look at the logs of the receiving GKE service:
         
         kubectl logs \
           --selector serving.knative.dev/service=DESTINATION_SERVICE \
           -c user-container \
           -n EVENTS_NAMESPACE \
           --tail=100
         

The output from the two triggers is similar to the following, with differences only in the `Context Attributes` and `Extensions`. The actual message data, with the exception of the `subscription` data, should be identical so that no event receiver changes are required after migrating to Eventarc.

Eventarc event:
         
         ☁️  cloudevents.Event
         Validation: valid
         Context Attributes,
           specversion: 1.0
           type: google.cloud.pubsub.topic.v1.messagePublished
           source: //pubsub.googleapis.com/projects/project-id/topics/topic-name
           id: 2759155988927083
           time: 2021-07-22T17:47:19.964Z
           datacontenttype: application/json
         Data,
           {
             "subscription": "projects/project-id/subscriptions/eventarc-us-central1-eventarc-trigger-name-sub-567",
             **"message": {
               "data": "V29ybGQ=",
               "messageId": "2759155988927083",
               "publishTime": "2021-07-22T17:47:19.964Z"
             }**
           }
         

Knative serving event:
         
         ☁️  cloudevents.Event
         Validation: valid
         Context Attributes,
           specversion: 1.0
           type: google.cloud.pubsub.topic.v1.messagePublished
           source: //pubsub.googleapis.com/projects/project-id/topics/topic-name
           id: 2759155988927083
           time: 2021-07-22T17:47:19.964Z
           dataschema: https://raw.githubusercontent.com/googleapis/google-cloudevents/master/proto/google/events/cloud/pubsub/v1/data.proto
           datacontenttype: application/json
         Extensions,
           knativearrivaltime: 2021-07-22T17:47:20.723302362Z
           knsourcetrigger: link0.09767362059083662
           traceparent: 00-f3cc6d754d361a0e49e83e5973fa3565-b4a20ef4ecffe96b-00
         Data,
           {
             "subscription": "cre-src_events_source-for-trigger-name_5ffa9638-8cab-4010-900a-2edb275d9eaf",
             **"message": {
               "messageId": "2759155988927083",
               "data": "V29ybGQ=",
               "publishTime": "2021-07-22T17:47:19.964Z"
             }**
           }
         




## Clean up after the migration

After testing and verifying the migration of the trigger to Eventarc, you can delete the original event trigger.

  1. Delete the original event trigger:
         
         gcloud beta events triggers delete TRIGGER_NAME \
           --platform gke \
           --namespace EVENTS_NAMESPACE \
           --quiet




You have migrated an existing Knative serving trigger to Eventarc.

## What's next

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)
  * [Learn how to route Cloud Pub/Sub events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-pubsub)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
