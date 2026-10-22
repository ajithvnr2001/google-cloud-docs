---
url: https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets/
title: Event providers and destinations \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:05.238608+00:00
---

# Event providers and destinations  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Event providers and destinations Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview:** While Eventarc is generally available, the following features are subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms): 

  * Sources: Events sent directly from Eventarc, Firebase Authentication, Firebase Realtime Database, Gemini Cloud Assist
  * Source: Third-party events sent directly from third-party providers
  * Target: Google Kubernetes Engine as an event destination
  * Target: Internal HTTP endpoints in a Virtual Private Cloud network as an event destination

Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

Supported events are routed from an event provider (the source) to an event destination (the target).

## Eventarc sources, targets, and event types

Once you have decided upon a source, target, and event type, you can create an Eventarc trigger.

Source (event provider) | Depending on your source, select an appropriate trigger type:

  * Google sources—Filters events sent from Google providers (directly or through Cloud Audit Logs entries)
  * Third-party—Filters events sent from eligible third-party providers

Using the Google Cloud CLI, you can list Eventarc providers and retrieve their details, including supported events. For more information, see [List event providers](https://docs.cloud.google.com/eventarc/docs/list-providers). **Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.  
---|---  
Target (event destination) | Events can be routed to one of the following event destinations:

  * Cloud Run functions ([using the Cloud Run functions interface](https://docs.cloud.google.com/eventarc/standard/docs/functions/create-triggers))
  * Cloud Run
  * Google Kubernetes Engine (GKE), including the public endpoints of private and public services running in a GKE cluster 
  * Internal HTTP endpoints in a Virtual Private Cloud (VPC) network 
  * Workflows

  
Event type | You can route an event by configuring filters for an Eventarc trigger. The trigger configuration varies depending on the supported event type:

  * Cloud Audit Logs events—Triggered when a log is produced through Cloud Audit Logs
  * Direct events—Triggered by an unmediated event such as an update to an object in a Cloud Storage bucket or a message published to a Pub/Sub topic **Note:** If both direct and audit log events are supported for the event that you want to route, we recommend that you create a trigger that filters for the direct event. Direct events offer several advantages over audit log events. For more information, see [Event routes](https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options). 
  * Third-party events—Triggered by the events of a non-Google provider that offers an Eventarc source

  
  
## Eventarc triggers

To create an Eventarc trigger, click the instructions provided for the event you want to route.

Google sourcesThird-partyCloud RunGKEInternal HTTP endpointWorkflowsReset selections

Event provider | Event destination | Event type | Instructions  
---|---|---|---  
Access Approval | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Access Context Manager | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
AI Platform (under Vertex AI) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
AlloyDB for PostgreSQL | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#alloydb-for-postgresql)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route AlloyDB for PostgreSQL events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-alloydb)

  
analyticshub.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
API Gateway | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#api-gateway)

| 

  * [Route API Gateway events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-api-gateway)

  
API Keys | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Apigee | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Apigee API hub | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-api-hub)

| 

  * [Route Apigee API hub events to Cloud Run](https://docs.cloud.google.com/eventarc/docs/run/route-trigger-apigee-api-hub)

  
Apigee Connect | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Apigee Registry | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-registry)

| 

  * [Route Apigee Registry events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-apigee-registry)

  
App Engine | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Artifact Analysis | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Artifact Registry | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Assured Workloads | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Backup for GKE | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#backup-for-gke)

| 

  * [Route Backup for GKE events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-backup-gke)

  
Bare Metal Solution | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Batch | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#batch)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Batch events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-batch)

  
BeyondCorp | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#beyondcorp)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route BeyondCorp events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-beyondcorp)

  
BigQuery | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
BigQuery BI Engine | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
BigQuery Connection API | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
BigQuery Data Transfer | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
BigQuery Migration | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
BigQuery Reservation | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
bigquerydatapolicy.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Binary Authorization | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Certificate Authority | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Certificate Manager | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#certificate-manager)

| 

  * [Route Certificate Manager events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-certificate-manager)

  
Check Point CloudGuard | Cloud Run | 

  * Third-party events (preview)

| 

  * [Route third-party events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#cloud-run_1)

  
Cloud AI Data Labeling | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Asset | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud AutoML (under Vertex AI) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Bigtable Admin | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Billing | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Build | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Data Catalog | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Data Fusion | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-data-fusion)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Data Fusion events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-data-fusion)

  
Cloud Datastore | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Deploy | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-deploy)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Deploy events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-deploy)

  
Cloud Deployment Manager | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Dialogflow | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud DNS | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Error Reporting | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Filestore | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Firebase | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Firestore | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-firestore)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Firestore events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-firestore)

  
Cloud Gaming | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Healthcare | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud IAM | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud IAM Service Account Credentials | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Identity | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Key Management Service (KMS) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Life Sciences | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Logging | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Machine Learning Engine | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Managed Microsoft Active Directory | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Memorystore for Memcached | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-memorystore-for-memcached)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Memorystore for Memcached events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-memorystore-for-memcached)

  
Cloud Monitoring | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud OS Config | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud OS Login | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Profiler | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Pub/Sub | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-pubsub)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Pub/Sub events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-pubsub)

  
Cloud Resource Manager | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Retail | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Run | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Run functions (formerly Cloud Functions) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-functions)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Run functions (formerly Cloud Functions) events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-functions)

  
Cloud Scheduler | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Search | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Service Mesh | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Source Repositories | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Speech-to-Text | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-speech-to-text)

| 

  * [Route Cloud Speech-to-Text events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-speech-to-text)

  
Cloud SQL | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Storage | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-storage)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Cloud Storage events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-storage)

  
Cloud Tasks | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud TPU | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Trace | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Translation | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Video Intelligence | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Cloud Vision | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Compute Engine | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Contact Center AI | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
contactcenteraiplatform.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Data Pipeline | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Database Migration | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#database-migration)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Database Migration events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-database-migration)

  
Datadog | Cloud Run | 

  * Third-party events (preview)

| 

  * [Route third-party events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#cloud-run_1)

  
Dataflow | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#dataflow)

| 

  * [Route Dataflow events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-dataflow)

  
dataform.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
datalineage.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Dataproc Metastore | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#dataproc-metastore)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Dataproc Metastore events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-dataproc-metastore)

  
Datastream | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#datastream)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Datastream events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-datastream)

  
documentai.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Essential Contacts | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Eventarc | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#eventarc-preview)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Eventarc events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-eventarc)

  
Firebase Alerts | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-alerts)

| 

  * [Route Firebase Alerts events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-firebase-alerts)

  
Firebase Authentication | Cloud Run | 

  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-auth)

| 

  * [Route Firebase Authentication events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-firebase-auth)

  
Firebase Data Connect | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-data-connect)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Firebase Data Connect events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-firebase-data-connect)

  
Firebase Realtime Database | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-realtime-database-preview)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Firebase Realtime Database events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-firebase-realtime-database)

  
Firebase Remote Config | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-remote-config)

| 

  * [Route Firebase Remote Config events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-firebase-remote-config)

  
Firebase Storage | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Firebase Test Lab | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-test-lab)

| 

  * [Route Firebase Test Lab events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-firebase-test-lab)

  
ForgeRock | Cloud Run | 

  * Third-party events (preview)

| 

  * [Route third-party events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#cloud-run_1)

  
GCE Serial Port | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Gemini Cloud Assist | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gemini-cloud-assist-preview)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Gemini Cloud Assist events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-gemini-cloud-assist)

  
GKE Hub | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gke-hub)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route GKE Hub events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-gke-hub)

  
Google Cloud Memorystore for Redis | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-memorystore-for-redis)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Google Cloud Memorystore for Redis events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-memorystore-redis)

  
Google Domains | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Google Kubernetes Engine (GKE) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Google Workspace Admin | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Identity Toolkit | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Identity-Aware Proxy (IAP) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Knowledge Catalog (formerly Cloud Dataplex) | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-dataplex)

| 

  * [Route Knowledge Catalog (formerly Cloud Dataplex) events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-dataplex)

  
Lacework | Cloud Run | 

  * Third-party events (preview)

| 

  * [Route third-party events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#cloud-run_1)

  
Managed Service for Apache Airflow (formerly Cloud Composer) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Managed Service for Apache Spark (formerly Cloud Dataproc) | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Mesh certificate authority | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
migrationcenter.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Network Connectivity | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-connectivity)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Network Connectivity events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-network-connectivity)

  
Network Management | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-management)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Network Management events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-network-management)

  
Network Security | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Network Services | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-services)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Network Services events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-network-services)

  
Notebooks | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#notebooks)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Notebooks events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-notebooks)

  
OAuth 2.0 | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
On-Demand Scanning | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Pub/Sub Lite | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
publicca.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
reCAPTCHA Enterprise | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Recommendations | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Recommender | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Remote Build Execution | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Resource Settings | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Secret Manager | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
securedlandingzone.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Security Command Center | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Security Token Service API | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Sensitive Data Protection | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Serverless VPC Access | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Service Consumer Management | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Service Directory | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Service Management | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Service Usage | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
timeseriesinsights.googleapis.com | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Transcoder | Cloud Run | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#transcoder)

| 

  * [Route Transcoder events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-transcoder)

  
Transparency and Control Center Audit Logging | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Vision AI | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#vision-ai)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Vision AI events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-vision-ai)

  
VM Migration | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#vm-migration)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route VM Migration events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-vm-migration)

  
VMware Engine | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Web Security Scanner | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Workflow executions | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)

  
Workflows | Cloud Run | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#workflows)

| 

  * [Route audit log events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs)
  * [Route Workflows events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-workflows)

  
Access Approval | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Access Context Manager | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
AI Platform (under Vertex AI) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
AlloyDB for PostgreSQL | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#alloydb-for-postgresql)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route AlloyDB for PostgreSQL events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-alloydb)

  
analyticshub.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
API Gateway | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#api-gateway)

| 

  * [Route API Gateway events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-api-gateway)

  
API Keys | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Apigee | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Apigee API hub | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-api-hub)

| 

  * [Route Apigee API hub events to GKE](https://docs.cloud.google.com/eventarc/docs/gke/route-trigger-apigee-api-hub)

  
Apigee Connect | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Apigee Registry | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-registry)

| 

  * [Route Apigee Registry events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-apigee-registry)

  
App Engine | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Artifact Analysis | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Artifact Registry | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Assured Workloads | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Backup for GKE | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#backup-for-gke)

| 

  * [Route Backup for GKE events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-backup-gke)

  
Bare Metal Solution | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Batch | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#batch)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Batch events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-batch)

  
BeyondCorp | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#beyondcorp)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route BeyondCorp events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-beyondcorp)

  
BigQuery | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
BigQuery BI Engine | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
BigQuery Connection API | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
BigQuery Data Transfer | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
BigQuery Migration | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
BigQuery Reservation | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
bigquerydatapolicy.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Binary Authorization | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Certificate Authority | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Certificate Manager | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#certificate-manager)

| 

  * [Route Certificate Manager events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-certificate-manager)

  
Check Point CloudGuard | GKE | 

  * Third-party events (preview)

| 

  * [Route third-party events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#gke_1)

  
Cloud AI Data Labeling | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Asset | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud AutoML (under Vertex AI) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Bigtable Admin | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Billing | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Build | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Data Catalog | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Data Fusion | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-data-fusion)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Data Fusion events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-data-fusion)

  
Cloud Datastore | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Deploy | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-deploy)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Deploy events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-deploy)

  
Cloud Deployment Manager | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Dialogflow | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud DNS | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Error Reporting | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Filestore | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Firebase | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Firestore | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-firestore)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Firestore events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-firestore)

  
Cloud Gaming | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Healthcare | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud IAM | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud IAM Service Account Credentials | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Identity | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Key Management Service (KMS) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Life Sciences | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Logging | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Machine Learning Engine | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Managed Microsoft Active Directory | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Memorystore for Memcached | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-memorystore-for-memcached)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Memorystore for Memcached events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-memorystore-for-memcached)

  
Cloud Monitoring | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud OS Config | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud OS Login | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Profiler | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Pub/Sub | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-pubsub)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Pub/Sub events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-pubsub)

  
Cloud Resource Manager | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Retail | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Run | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Run functions (formerly Cloud Functions) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-functions)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Run functions (formerly Cloud Functions) events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-functions)

  
Cloud Scheduler | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Search | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Service Mesh | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Source Repositories | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Speech-to-Text | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-speech-to-text)

| 

  * [Route Cloud Speech-to-Text events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-speech-to-text)

  
Cloud SQL | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Storage | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-storage)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Cloud Storage events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-storage)

  
Cloud Tasks | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud TPU | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Trace | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Translation | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Video Intelligence | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Cloud Vision | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Compute Engine | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Contact Center AI | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
contactcenteraiplatform.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Data Pipeline | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Database Migration | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#database-migration)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Database Migration events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-database-migration)

  
Datadog | GKE | 

  * Third-party events (preview)

| 

  * [Route third-party events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#gke_1)

  
Dataflow | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#dataflow)

| 

  * [Route Dataflow events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-dataflow)

  
dataform.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
datalineage.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Dataproc Metastore | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#dataproc-metastore)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Dataproc Metastore events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-dataproc-metastore)

  
Datastream | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#datastream)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Datastream events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-datastream)

  
documentai.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Essential Contacts | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Eventarc | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#eventarc-preview)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Eventarc events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-eventarc)

  
Firebase Alerts | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-alerts)

| 

  * [Route Firebase Alerts events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-firebase-alerts)

  
Firebase Authentication | GKE | 

  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-auth)

| 

  * [Route Firebase Authentication events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-firebase-auth)

  
Firebase Data Connect | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-data-connect)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Firebase Data Connect events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-firebase-data-connect)

  
Firebase Realtime Database | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-realtime-database-preview)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Firebase Realtime Database events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-firebase-realtime-database)

  
Firebase Remote Config | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-remote-config)

| 

  * [Route Firebase Remote Config events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-firebase-remote-config)

  
Firebase Storage | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Firebase Test Lab | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-test-lab)

| 

  * [Route Firebase Test Lab events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-firebase-test-lab)

  
ForgeRock | GKE | 

  * Third-party events (preview)

| 

  * [Route third-party events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#gke_1)

  
GCE Serial Port | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Gemini Cloud Assist | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (Preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gemini-cloud-assist-preview)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Gemini Cloud Assist events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-gemini-cloud-assist)

  
GKE Hub | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gke-hub)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route GKE Hub events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-gke-hub)

  
Google Cloud Memorystore for Redis | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-memorystore-for-redis)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Google Cloud Memorystore for Redis events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-memorystore-redis)

  
Google Domains | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Google Kubernetes Engine (GKE) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Google Workspace Admin | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Identity Toolkit | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Identity-Aware Proxy (IAP) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Knowledge Catalog (formerly Cloud Dataplex) | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-dataplex)

| 

  * [Route Knowledge Catalog (formerly Cloud Dataplex) events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-dataplex)

  
Lacework | GKE | 

  * Third-party events (preview)

| 

  * [Route third-party events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#gke_1)

  
Managed Service for Apache Airflow (formerly Cloud Composer) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Managed Service for Apache Spark (formerly Cloud Dataproc) | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Mesh certificate authority | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
migrationcenter.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Network Connectivity | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-connectivity)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Network Connectivity events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-network-connectivity)

  
Network Management | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-management)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Network Management events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-network-management)

  
Network Security | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Network Services | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-services)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Network Services events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-network-services)

  
Notebooks | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#notebooks)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Notebooks events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-notebooks)

  
OAuth 2.0 | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
On-Demand Scanning | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Pub/Sub Lite | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
publicca.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
reCAPTCHA Enterprise | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Recommendations | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Recommender | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Remote Build Execution | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Resource Settings | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Secret Manager | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
securedlandingzone.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Security Command Center | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Security Token Service API | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Sensitive Data Protection | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Serverless VPC Access | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Service Consumer Management | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Service Directory | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Service Management | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Service Usage | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
timeseriesinsights.googleapis.com | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Transcoder | GKE | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#transcoder)

| 

  * [Route Transcoder events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-transcoder)

  
Transparency and Control Center Audit Logging | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

| Vision AI | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#vision-ai)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Vision AI events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-vision-ai)

  
VM Migration | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#vm-migration)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route VM Migration events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-vm-migration)

  
VMware Engine | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Web Security Scanner | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Workflow executions | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)

  
Workflows | GKE | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#workflows)

| 

  * [Route audit log events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-cloud-audit-logs)
  * [Route Workflows events to GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-workflows)

  
All event providers | Internal HTTP endpoint | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/event-types#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/event-types#directly-from-a-google-cloud-source)
  * [Third-party events](https://docs.cloud.google.com/eventarc/docs/event-types#using-third-party-sources)

| 

  * [Route events to an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events)

  
Access Approval | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Access Context Manager | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
AI Platform (under Vertex AI) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
AlloyDB for PostgreSQL | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#alloydb-for-postgresql)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route AlloyDB for PostgreSQL events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-alloydb)

  
analyticshub.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
API Gateway | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#api-gateway)

| 

  * [Route API Gateway events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-api-gateway)

  
API Keys | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Apigee | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Apigee API hub | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-api-hub)

| 

  * [Route Apigee API hub events to Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/route-trigger-apigee-api-hub)

  
Apigee Connect | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Apigee Registry | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-registry)

| 

  * [Route Apigee Registry events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-apigee-registry)

  
App Engine | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Artifact Analysis | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Artifact Registry | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Assured Workloads | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Backup for GKE | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#backup-for-gke)

| 

  * [Route Backup for GKE events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-backup-gke)

  
Bare Metal Solution | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Batch | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#batch)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Batch events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-batch)

  
BeyondCorp | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#beyondcorp)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route BeyondCorp events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-beyondcorp)

  
BigQuery | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
BigQuery BI Engine | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
BigQuery Connection API | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
BigQuery Data Transfer | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
BigQuery Migration | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
BigQuery Reservation | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
bigquerydatapolicy.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Binary Authorization | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Certificate Authority | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Certificate Manager | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#certificate-manager)

| 

  * [Route Certificate Manager events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-certificate-manager)

  
Check Point CloudGuard | Workflows | 

  * Third-party events (preview)

| 

  * [Route third-party events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#workflows_1)

  
Cloud AI Data Labeling | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Asset | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud AutoML (under Vertex AI) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Bigtable Admin | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Billing | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Build | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Data Catalog | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Data Fusion | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-data-fusion)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Data Fusion events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-data-fusion)

  
Cloud Datastore | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Deploy | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-deploy)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Deploy events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-deploy)

  
Cloud Deployment Manager | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Dialogflow | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud DNS | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Error Reporting | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Filestore | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Firebase | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Firestore | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-firestore)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Firestore events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-firestore)

  
Cloud Gaming | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Healthcare | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud IAM | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud IAM Service Account Credentials | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Identity | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Key Management Service (KMS) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Life Sciences | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Logging | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Machine Learning Engine | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Managed Microsoft Active Directory | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Memorystore for Memcached | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-memorystore-for-memcached)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Memorystore for Memcached events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-memorystore-for-memcached)

  
Cloud Monitoring | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud OS Config | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud OS Login | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Profiler | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Pub/Sub | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-pubsub)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Pub/Sub events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-pubsub)

  
Cloud Resource Manager | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Retail | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Run | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Run functions (formerly Cloud Functions) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-functions)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Run functions (formerly Cloud Functions) events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-functions)

  
Cloud Scheduler | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Search | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Service Mesh | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Source Repositories | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Speech-to-Text | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-speech-to-text)

| 

  * [Route Cloud Speech-to-Text events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-speech-to-text)

  
Cloud SQL | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Storage | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-storage)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Cloud Storage events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage)

  
Cloud Tasks | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud TPU | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Trace | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Translation | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Video Intelligence | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Cloud Vision | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Compute Engine | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Contact Center AI | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
contactcenteraiplatform.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Data Pipeline | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Database Migration | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#database-migration)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Database Migration events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-database-migration)

  
Datadog | Workflows | 

  * Third-party events (preview)

| 

  * [Route third-party events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#workflows_1)

  
Dataflow | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#dataflow)

| 

  * [Route Dataflow events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-dataflow)

  
dataform.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
datalineage.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Dataproc Metastore | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#dataproc-metastore)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Dataproc Metastore events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-dataproc-metastore)

  
Datastream | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#datastream)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Datastream events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-datastream)

  
documentai.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Essential Contacts | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Eventarc | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#eventarc-preview)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Eventarc events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-eventarc)

  
Firebase Alerts | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-alerts)

| 

  * [Route Firebase Alerts events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-firebase-alerts)

  
Firebase Authentication | Workflows | 

  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-auth)

| 

  * [Route Firebase Authentication events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-firebase-auth)

  
Firebase Data Connect | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-data-connect)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Firebase Data Connect events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-firebase-data-connect)

  
Firebase Realtime Database | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-realtime-database-preview)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Firebase Realtime Database events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-firebase-realtime-database)

  
Firebase Remote Config | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-remote-config)

| 

  * [Route Firebase Remote Config events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-firebase-remote-config)

  
Firebase Storage | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Firebase Test Lab | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-test-lab)

| 

  * [Route Firebase Test Lab events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-firebase-test-lab)

  
ForgeRock | Workflows | 

  * Third-party events (preview)

| 

  * [Route third-party events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#workflows_1)

  
GCE Serial Port | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Gemini Cloud Assist | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events (Preview)](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gemini-cloud-assist-preview)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Gemini Cloud Assist events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-gemini-cloud-assist)

  
GKE Hub | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gke-hub)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route GKE Hub events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-gke-hub)

  
Google Cloud Memorystore for Redis | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-memorystore-for-redis)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Google Cloud Memorystore for Redis events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-memorystore-redis)

  
Google Domains | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Google Kubernetes Engine (GKE) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Google Workspace Admin | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Identity Toolkit | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Identity-Aware Proxy (IAP) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Knowledge Catalog (formerly Cloud Dataplex) | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-dataplex)

| 

  * [Route Knowledge Catalog (formerly Cloud Dataplex) events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-dataplex)

  
Lacework | Workflows | 

  * Third-party events (preview)

| 

  * [Route third-party events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty#workflows_1)

  
Managed Service for Apache Airflow (formerly Cloud Composer) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Managed Service for Apache Spark (formerly Cloud Dataproc) | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Mesh certificate authority | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
migrationcenter.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Network Connectivity | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-connectivity)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Network Connectivity events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-network-connectivity)

  
Network Management | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-management)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Network Management events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-network-management)

  
Network Security | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Network Services | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-services)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Network Services events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-network-services)

  
Notebooks | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#notebooks)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Notebooks events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-notebooks)

  
OAuth 2.0 | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
On-Demand Scanning | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Pub/Sub Lite | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
publicca.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
reCAPTCHA Enterprise | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Recommendations | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Recommender | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Remote Build Execution | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Resource Settings | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Secret Manager | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
securedlandingzone.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Security Command Center | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Security Token Service API | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Sensitive Data Protection | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Serverless VPC Access | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Service Consumer Management | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Service Directory | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Service Management | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Service Usage | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
timeseriesinsights.googleapis.com | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Transcoder | Workflows | 

  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#transcoder)

| 

  * [Route Transcoder events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-transcoder)

  
Transparency and Control Center Audit Logging | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Vision AI | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#vision-ai)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Vision AI events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-vision-ai)

  
VM Migration | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#vm-migration)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route VM Migration events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-vm-migration)

  
VMware Engine | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Web Security Scanner | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Workflow executions | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)

  
Workflows | Workflows | 

  * [Audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)
  * [Direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#workflows)

| 

  * [Route audit log events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)
  * [Route Workflows events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-workflows)

  
  
## What's next

  * [Eventarc Standard overview](https://docs.cloud.google.com/eventarc/standard/docs/overview)
  * [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
