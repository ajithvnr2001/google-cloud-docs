---
url: https://docs.cloud.google.com/eventarc/docs/locations/
title: Eventarc locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:27.668498+00:00
---

# Eventarc locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Resources ](https://docs.cloud.google.com/eventarc/docs/resources)



Send feedback 

#  Eventarc locations Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

Eventarc is available in specific regions depending on whether you are using Eventarc Advanced or Eventarc Standard.

  * A region is a specific geographic place, such as São Paulo.

  * A multi-region is a large geographic area, such as the United States, that contains two or more geographic places. (Some sources support _dual-regions_ which are a specific pair of regions, such as Tokyo and Osaka.)




For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Eventarc Advanced

Eventarc Advanced is available in the following regions:

Region name | Region description |   
---|---|---  
`asia-south1` | Mumbai, India |   
`asia-southeast1` | Jurong West, Singapore |   
`australia-southeast1` | Sydney, Australia |   
`europe-north1` | Hamina, Finland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west1` | St. Ghislain, Belgium |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west3` | Frankfurt, Germany |   
`us-central1` | Council Bluffs, Iowa, North America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-east4` | Ashburn, Virginia, North America |   
  
## Eventarc Standard

The location for an Eventarc trigger should be either `global` (applicable to some events only) or one of the supported regions depending on the event type.

For more information, see [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations).

### Cloud Audit Logs events

Triggers for Cloud Audit Logs events are available in single-region locations and you can create a `global` Eventarc trigger; however, triggers are not supported in dual-region and multi-region locations.

When specifying the global location for Cloud Audit Logs triggers, you will receive events from all locations for which the event filters match. For example, by creating a `global` Eventarc trigger, you can receive events from resources in the `EU` and `US` multi-regions.

### Pub/Sub messages

Triggers for Pub/Sub messages are only available in single-region locations and you can't create a `global` Eventarc trigger.

### Direct events

Triggers for events that are sent directly from one of the following Google sources are available in specific locations. For all other sources, see the supported regions.

###  AlloyDB for PostgreSQL 

Eventarc triggers for AlloyDB events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west6`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  API Gateway 

Eventarc triggers for API Gateway events are available only in the following locations:

  * `asia-east1`
  * `asia-northeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `global`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Apigee API hub 

Eventarc triggers for API hub events are available only in the following locations:

  * `europe-west1`
  * `us-central1`



###  Apigee Registry 

Eventarc triggers for Apigee Registry events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Backup for GKE 

Eventarc triggers for Backup for GKE events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Batch 

Eventarc triggers for Batch events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-south1`
  * `asia-southeast1`
  * `europe-central2`
  * `europe-north1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `northamerica-northeast1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  BeyondCorp 

Eventarc triggers for BeyondCorp events are available only in the following locations:

  * `asia-east1`
  * `europe-west1`
  * `global`
  * `us-central1`
  * `us-east1`



###  Certificate Manager 

You must create a `global` Eventarc trigger for Certificate Manager events.

###  Cloud Data Fusion 

Eventarc triggers for Cloud Data Fusion events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`



###  Cloud Deploy 

Eventarc triggers for Cloud Deploy events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `europe-west10`
  * `europe-west12`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Cloud Firestore 

Eventarc triggers for Cloud Firestore must be in the same location as the Cloud Firestore database. In addition to the single-region locations listed in the [Supported regions](https://docs.cloud.google.com/eventarc/docs/locations#regions) section, the following locations are also supported for Cloud Firestore triggers:

  * `eur3`: EUROPE-WEST1 and EUROPE-WEST4
  * `nam5`: US-CENTRAL1 and US-CENTRAL2
  * `nam7`: US-CENTRAL1 and US-EAST4



###  Cloud Run functions (formerly Cloud Functions) 

Eventarc triggers for Cloud Run functions (formerly Cloud Functions) events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Cloud Speech-to-Text 

You must create a `global` Eventarc trigger for Cloud Speech-to-Text events.

###  Cloud Storage 

Triggers for Cloud Storage events are available in single-region, dual-region, and multi-region locations; you can't create a `global` Eventarc trigger.

**Important:** Because Eventarc Standard uses Pub/Sub as its transport layer, Cloud Storage triggers can fail if a Cloud Storage event originates from a region not permitted by your Pub/Sub message storage policy, and if in-transit operations are enforced (`"enforceInTransit": true`). When you create a Cloud Storage trigger in a multi-region location, ensure your message storage policy allows all source regions within that multi-region. For more information, see [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). 

Note that the Cloud Storage bucket must reside in the same Google Cloud project and region as the Eventarc trigger.

In addition to the single-region locations listed in the [Supported regions](https://docs.cloud.google.com/eventarc/docs/locations#regions) section, the following locations are also supported for Cloud Storage triggers:

  * `asia`: Data centers in Asia
  * `asia1`: ASIA-NORTHEAST1 and ASIA-NORTHEAST2
  * `eu`: Data centers within member states of the European Union
  * `eur4`: EUROPE-NORTH1 and EUROPE-WEST4
  * `nam4`: US-CENTRAL1 and US-EAST1
  * `us`: Data centers in the United States



For more information, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

###  Database Migration 

Eventarc triggers for Database Migration events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Dataflow 

Eventarc triggers for Dataflow events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Dataproc Metastore 

Eventarc triggers for Dataproc Metastore events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `europe-central2`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Datastream 

Eventarc triggers for Datastream events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Eventarc 

Triggers for direct Eventarc events are available in the single-region locations and in the `global` region, but are not available in dual-region and multi-region locations.

###  Firebase Alerts 

You must create a `global` Eventarc trigger for Firebase Alerts events.

###  Firebase Data Connect 

Eventarc triggers for Firebase Data Connect events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Firebase Authentication 

You must create a `global` Eventarc trigger for Firebase Authentication events.

###  Firebase Realtime Database 

Eventarc triggers for Firebase Realtime Database events are available only in the following locations:

  * `asia-southeast1`
  * `europe-west1`
  * `us-central1`



For more information, see [Realtime Database locations](https://firebase.google.com/docs/projects/locations#rtdb-locations).

###  Firebase Remote Config 

You must create a `global` Eventarc trigger for Firebase Remote Config events.

###  Firebase Test Lab 

You must create a `global` Eventarc trigger for Firebase Test Lab events.

###  Gemini Cloud Assist 

You must create a `global` Eventarc trigger for Gemini Cloud Assist events.

###  GKE Hub 

Eventarc triggers for GKE Hub events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `global`
  * `me-central1`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Google Cloud Memorystore for Redis 

Eventarc triggers for Google Cloud Memorystore for Redis events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Knowledge Catalog (formerly Cloud Dataplex) 

Eventarc triggers for Knowledge Catalog (formerly Cloud Dataplex) events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-southeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`



###  Network Connectivity 

Eventarc triggers for Network Connectivity events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `global`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Network Management API 

You must create a `global` Eventarc trigger for Network Management API events.

###  Network Services API 

Eventarc triggers for Network Services API events are available only in the following locations:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `global`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



###  Notebooks 

Eventarc triggers for Notebooks events are available only in the following locations:

  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-southeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west4`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-central1`
  * `us-west1`
  * `us-west4`



###  Transcoder API 

Eventarc triggers for Transcoder API events are available only in the following locations:

  * `asia-east1`
  * `asia-south1`
  * `asia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west4`
  * `southamerica-east1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`



###  Vision AI 

You must create a `us-central1` Eventarc trigger for Vision AI events.

###  VM Migration 

You can create triggers for VM Migration events in Eventarc-supported locations or as a `global` trigger.

###  Workflows 

Eventarc triggers for Workflows events are available only in the following locations:

  * `asia-east1`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-north1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west4`



###  Other direct events 

See the supported regions.

### Supported regions

The supported regions for Eventarc Standard are as follows:

  * Americas
  * Europe
  * Asia-Pacific
  * Middle East
  * Africa
  * Cloud Storage triggers only
  * Cloud Firestore triggers only



#### Americas

The following table lists the regions in North and South America where Eventarc is available.

Region name | Region description | Details  
---|---|---  
`northamerica-northeast1` | Montréal, Québec, North America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast2` | Toronto, Ontario, North America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-south1` | Mexico, North America |   
`southamerica-east1` | Osasco, São Paulo, Brazil, South America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-west1` | Santiago, Chile, South America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1` | Council Bluffs, Iowa, North America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-east1` | Moncks Corner, South Carolina, North America |   
`us-east4` | Ashburn, Virginia, North America |   
`us-east5` | Columbus, Ohio, North America |   
`us-south1` | Dallas, Texas, North America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west1` | The Dalles, Oregon, North America |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west2` | Los Angeles, California, North America |   
`us-west3` | Salt Lake City, Utah, North America |   
`us-west4` | Las Vegas, Nevada, North America |   
`us-west8` | Phoenix, Arizona, North America |   
  
#### Europe

The following table lists the regions in Europe where Eventarc is available.

Region name | Region description | Details  
---|---|---  
`europe-central2` | Warsaw, Poland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north1` | Hamina, Finland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north2` | Stockholm, Sweden |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-southwest1` | Madrid, Spain |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west1` | St. Ghislain, Belgium |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west2` | London, England |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west3` | Frankfurt, Germany |   
`europe-west4` | Eemshaven, Netherlands |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west6` | Zurich, Switzerland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west8` | Milan, Italy |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west9` | Paris, France |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west10` | Berlin, Germany |   
`europe-west12` | Turin, Italy |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
#### Asia Pacific

The following table lists the regions in Asia Pacific where Eventarc is available.

Region name | Region description |   
---|---|---  
`asia-east1` | Changhua County, Taiwan |   
`asia-east2` | Hong Kong |   
`asia-northeast1` | Tokyo, Japan |   
`asia-northeast2` | Osaka, Japan |   
`asia-northeast3` | Seoul, South Korea |   
`asia-south1` | Mumbai, India |   
`asia-south2` | Delhi, India |   
`asia-southeast1` | Jurong West, Singapore |   
`asia-southeast2` | Jakarta, Indonesia |   
`asia-southeast3` | Bangkok, Thailand |   
`australia-southeast1` | Sydney, Australia |   
`australia-southeast2` | Melbourne, Australia |   
  
#### Middle East

The following table lists the regions in the Middle East where Eventarc is available.

Region name | Region description |   
---|---|---  
`me-central1` | Doha, Qatar |   
`me-central2` | Dammam, Kingdom of Saudi Arabia |   
`me-west1` | Tel Aviv, Israel |   
  
#### Africa

The following table lists the regions in Africa where Eventarc is available.

Region name | Region description |   
---|---|---  
`africa-south1` | Johannesburg, South Africa |   
  
#### Cloud Storage triggers only

In addition to the single-region locations listed on this page, the following table lists the other locations supported for Cloud Storage triggers.

**Important:** Because Eventarc Standard uses Pub/Sub as its transport layer, Cloud Storage triggers can fail if a Cloud Storage event originates from a region not permitted by your Pub/Sub message storage policy, and if in-transit operations are enforced (`"enforceInTransit": true`). When you create a Cloud Storage trigger in a multi-region location, ensure your message storage policy allows all source regions within that multi-region. For more information, see [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). 

Region name | Region description |   
---|---|---  
`asia` | Data centers in Asia  
`asia1` | ASIA-NORTHEAST1 and ASIA-NORTHEAST2  
`eu` | Data centers within member states of the European Union  
`eur4` | EUROPE-NORTH1 and EUROPE-WEST4  
`nam4` | US-CENTRAL1 and US-EAST1  
`us` | US Data centers in the United States  
  
#### Cloud Firestore triggers only

In addition to the single-region locations listed on this page, the following table lists the other locations supported for Firestore triggers.

Region name | Region description |   
---|---|---  
`eur3` | EUROPE-WEST1 and EUROPE-WEST4  
`nam5` | US-CENTRAL1 and US-CENTRAL2  
`nam7` | US-CENTRAL1 and US-EAST4  
  
### Listing available locations

You can use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/locations/list) to get a list of available locations for Eventarc Standard:
    
    
    gcloud eventarc locations list
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
