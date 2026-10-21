---
url: https://docs.cloud.google.com/iam/docs/permissions-change-log-archive/
title: Archived permissions change log \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:10.868233+00:00
---

# Archived permissions change log  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/permissions-change-log-archive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Resources ](https://docs.cloud.google.com/iam/docs/resources)



Send feedback 

#  Archived permissions change log Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an archive of changes to Identity and Access Management (IAM) permissions that occurred before 2022. For more recent changes, see [IAM permissions change log](https://docs.cloud.google.com/iam/docs/permissions-change-log).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloud-iam-permissions-change-log.xml) directly. 

## Cloud IAM changes as of 2021-12-03

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.namespaces.create`  
  
Apigee  |  Now GA  |  The role `roles/apigee.apiAdminV2` (Apigee API Admin) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.apiReaderV2` (Apigee API Reader) is now GA.  
Cloud Build  |  Role Updated  |  The following permissions have been added to the role `roles/cloudbuild.builds.builder` (Cloud Build Service Account): `logging.logEntries.list`  
`logging.privateLogEntries.list`  
`logging.views.access`  
  
Cloud Build  |  Role Updated  |  The following permissions have been added to the role `roles/cloudbuild.serviceAgent` (Cloud Build Service Agent): `logging.logEntries.list`  
`logging.privateLogEntries.list`  
`logging.views.access`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.environmentAndStorageObjectAdmin` (Environment and Storage Object Administrator): `orgpolicy.policy.get`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.worker` (Composer Worker): `logging.logEntries.list`  
`logging.privateLogEntries.list`  
`logging.views.access`  
`orgpolicy.policy.get`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `orgpolicy.policy.get`  
  
Cloud Data Fusion  |  Role Updated  |  The following permissions have been added to the role `roles/datafusion.serviceAgent` (Cloud Data Fusion API Service Agent): `orgpolicy.policy.get`  
  
Data Pipelines  |  Role Updated  |  The following permissions have been added to the role `roles/datapipelines.serviceAgent` (Datapipelines Service Agent): `orgpolicy.policy.get`  
  
Dataprep by Trifacta  |  Role Updated  |  The following permissions have been added to the role `roles/dataprep.serviceAgent` (Dataprep Service Agent): `orgpolicy.policy.get`  
  
Managed Service for Apache Spark  |  Role Updated  |  The following permissions have been added to the role `roles/dataproc.serviceAgent` (Dataproc Service Agent): `orgpolicy.policy.get`  
  
Sensitive Data Protection  |  Role Updated  |  The following permissions have been added to the role `roles/dlp.serviceAgent` (DLP API Service Agent): `orgpolicy.policy.get`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.admin` (Firebase Admin): `orgpolicy.policy.get`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.developAdmin` (Firebase Develop Admin): `orgpolicy.policy.get`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.sdkAdminServiceAgent` (Firebase Admin SDK Administrator Service Agent): `orgpolicy.policy.get`  
  
AI Platform  |  Role Updated  |  The following permissions have been added to the role `roles/ml.serviceAgent` (AI Platform Service Agent): `orgpolicy.policy.get`  
  
Cloud Storage  |  Role Updated  |  The following permissions have been added to the role `roles/storage.admin` (Storage Admin): `orgpolicy.policy.get`  
  
Cloud Storage  |  Role Updated  |  The following permissions have been added to the role `roles/storage.hmacKeyAdmin` (Storage HMAC Key Admin): `orgpolicy.policy.get`  
  
Cloud Storage  |  Role Updated  |  The following permissions have been added to the role `roles/storage.objectAdmin` (Storage Object Admin): `orgpolicy.policy.get`  
  
Cloud Storage  |  Role Updated  |  The following permissions have been added to the role `roles/storage.objectCreator` (Storage Object Creator): `orgpolicy.policy.get`  
  
Visual Inspection AI  |  Role Updated  |  The following permissions have been added to the role `roles/visualinspection.serviceAgent` (Visual Inspection AI Service Agent): `orgpolicy.policy.get`  
  
Certificate Manager  |  Added  |  `certificatemanager.certmapentries.create`  
`certificatemanager.certmapentries.delete`  
`certificatemanager.certmapentries.get`  
`certificatemanager.certmapentries.getIamPolicy`  
`certificatemanager.certmapentries.list`  
`certificatemanager.certmapentries.setIamPolicy`  
`certificatemanager.certmapentries.update`  
`certificatemanager.certmaps.create`  
`certificatemanager.certmaps.delete`  
`certificatemanager.certmaps.get`  
`certificatemanager.certmaps.getIamPolicy`  
`certificatemanager.certmaps.list`  
`certificatemanager.certmaps.setIamPolicy`  
`certificatemanager.certmaps.update`  
`certificatemanager.certmaps.use`  
`certificatemanager.certs.create`  
`certificatemanager.certs.delete`  
`certificatemanager.certs.get`  
`certificatemanager.certs.getIamPolicy`  
`certificatemanager.certs.list`  
`certificatemanager.certs.setIamPolicy`  
`certificatemanager.certs.update`  
`certificatemanager.certs.use`  
`certificatemanager.dnsauthorizations.create`  
`certificatemanager.dnsauthorizations.delete`  
`certificatemanager.dnsauthorizations.get`  
`certificatemanager.dnsauthorizations.getIamPolicy`  
`certificatemanager.dnsauthorizations.list`  
`certificatemanager.dnsauthorizations.setIamPolicy`  
`certificatemanager.dnsauthorizations.update`  
`certificatemanager.dnsauthorizations.use`  
`certificatemanager.locations.get`  
`certificatemanager.locations.list`  
`certificatemanager.operations.cancel`  
`certificatemanager.operations.delete`  
`certificatemanager.operations.get`  
`certificatemanager.operations.list`  
  
Certificate Manager  |  Supported In Custom Roles  |  `certificatemanager.certmapentries.create`  
`certificatemanager.certmapentries.delete`  
`certificatemanager.certmapentries.get`  
`certificatemanager.certmapentries.getIamPolicy`  
`certificatemanager.certmapentries.list`  
`certificatemanager.certmapentries.setIamPolicy`  
`certificatemanager.certmapentries.update`  
`certificatemanager.certmaps.create`  
`certificatemanager.certmaps.delete`  
`certificatemanager.certmaps.get`  
`certificatemanager.certmaps.getIamPolicy`  
`certificatemanager.certmaps.list`  
`certificatemanager.certmaps.setIamPolicy`  
`certificatemanager.certmaps.update`  
`certificatemanager.certmaps.use`  
`certificatemanager.certs.create`  
`certificatemanager.certs.delete`  
`certificatemanager.certs.get`  
`certificatemanager.certs.getIamPolicy`  
`certificatemanager.certs.list`  
`certificatemanager.certs.setIamPolicy`  
`certificatemanager.certs.update`  
`certificatemanager.certs.use`  
`certificatemanager.dnsauthorizations.create`  
`certificatemanager.dnsauthorizations.delete`  
`certificatemanager.dnsauthorizations.get`  
`certificatemanager.dnsauthorizations.getIamPolicy`  
`certificatemanager.dnsauthorizations.list`  
`certificatemanager.dnsauthorizations.setIamPolicy`  
`certificatemanager.dnsauthorizations.update`  
`certificatemanager.dnsauthorizations.use`  
`certificatemanager.locations.get`  
`certificatemanager.locations.list`  
`certificatemanager.operations.cancel`  
`certificatemanager.operations.delete`  
`certificatemanager.operations.get`  
`certificatemanager.operations.list`  
  
Compute Engine  |  Added  |  `compute.commitments.update`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.commitments.update`  
  
Compute Engine  |  Now GA  |  `compute.commitments.update`  
  
Cloud Commerce Consumer Procurement  |  Added  |  `consumerprocurement.orderAttributions.get`  
`consumerprocurement.orderAttributions.list`  
`consumerprocurement.orderAttributions.update`  
  
Cloud Commerce Consumer Procurement  |  Supported In Custom Roles  |  `consumerprocurement.orderAttributions.get`  
`consumerprocurement.orderAttributions.list`  
`consumerprocurement.orderAttributions.update`  
  
Data Connectors  |  Added  |  `dataconnectors.connectors.create`  
`dataconnectors.connectors.delete`  
`dataconnectors.connectors.get`  
`dataconnectors.connectors.getIamPolicy`  
`dataconnectors.connectors.list`  
`dataconnectors.connectors.setIamPolicy`  
`dataconnectors.connectors.update`  
`dataconnectors.connectors.use`  
`dataconnectors.locations.get`  
`dataconnectors.locations.list`  
`dataconnectors.operations.cancel`  
`dataconnectors.operations.delete`  
`dataconnectors.operations.get`  
`dataconnectors.operations.list`  
  
Data Connectors  |  Supported In Custom Roles  |  `dataconnectors.connectors.create`  
`dataconnectors.connectors.delete`  
`dataconnectors.connectors.get`  
`dataconnectors.connectors.getIamPolicy`  
`dataconnectors.connectors.list`  
`dataconnectors.connectors.setIamPolicy`  
`dataconnectors.connectors.update`  
`dataconnectors.connectors.use`  
`dataconnectors.locations.get`  
`dataconnectors.locations.list`  
`dataconnectors.operations.cancel`  
`dataconnectors.operations.delete`  
`dataconnectors.operations.get`  
`dataconnectors.operations.list`  
  
Dataflow  |  Added  |  `dataflow.shuffle.read`  
`dataflow.shuffle.write`  
`dataflow.streamingWorkItems.commitWork`  
`dataflow.streamingWorkItems.getData`  
`dataflow.streamingWorkItems.getWork`  
`dataflow.workItems.lease`  
`dataflow.workItems.sendMessage`  
`dataflow.workItems.update`  
  
Network Services  |  Added  |  `networkservices.serviceBindings.create`  
`networkservices.serviceBindings.delete`  
`networkservices.serviceBindings.get`  
`networkservices.serviceBindings.list`  
`networkservices.serviceBindings.update`  
  
VM Migration  |  Added  |  `vmmigration.datacenterConnectors.update`  
  
VM Migration  |  Supported In Custom Roles  |  `vmmigration.datacenterConnectors.update`  
  
  
## Cloud IAM changes as of 2021-11-12

Service | Change | Description  
---|---|---  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.featurestoreDataViewer` (Vertex AI Feature Store Data Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.featurestoreDataWriter` (Vertex AI Feature Store Data Writer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.featurestoreResourceEditor` (Vertex AI Feature Store Resource Editor): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.featurestoreResourceViewer` (Vertex AI Feature Store Resource Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.clusterRoles.update`  
  
Apigee  |  Now GA  |  The role `roles/apigee.securityAdmin` (Apigee Security Admin) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.securityViewer` (Apigee Security Viewer) is now GA.  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.environmentAdmin` (Apigee Environment Admin): `apigee.environments.update`  
  
Binary Authorization  |  Role Updated  |  The following permissions have been added to the role `roles/binaryauthorization.serviceAgent` (Binary Authorization Service Agent): `cloudasset.feeds.create`  
`cloudasset.feeds.delete`  
`cloudasset.feeds.get`  
`cloudasset.feeds.update`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.loadBalancerAdmin` (Compute Load Balancer Admin): `networksecurity.clientTlsPolicies.get`  
`networksecurity.clientTlsPolicies.list`  
`networksecurity.clientTlsPolicies.use`  
`networksecurity.serverTlsPolicies.get`  
`networksecurity.serverTlsPolicies.list`  
`networksecurity.serverTlsPolicies.use`  
  
Firestore  |  Now GA  |  The role `roles/datastore.keyVisualizerViewer` (Cloud Datastore Key Visualizer Viewer) is now GA.  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.serviceAgent` (Dialogflow Service Agent): `dlp.deidentifyTemplates.get`  
`dlp.deidentifyTemplates.list`  
  
Sensitive Data Protection  |  Role Updated  |  The following permissions have been added to the role `roles/dlp.serviceAgent` (DLP API Service Agent): `dlp.deidentifyTemplates.get`  
`dlp.deidentifyTemplates.list`  
  
Google Earth Engine  |  Role Updated  |  The following permissions have been added to the role `roles/earthengine.appsPublisher` (Earth Engine Apps Publisher): `serviceusage.services.get`  
  
Enterprise Knowledge Graph  |  Role Updated  |  The following permissions have been added to the role `roles/enterpriseknowledgegraph.serviceAgent` (Enterprise Knowledge Graph Service Agent): `bigquery.readsessions.getData`  
  
Firebase App Check  |  Now GA  |  The role `roles/firebaseappcheck.serviceAgent` (Firebase App Check Service Agent) is now GA.  
GKE Multi-Cloud  |  Now GA  |  The role `roles/gkemulticloud.admin` (Anthos Multi-cloud Admin) is now GA.  
GKE Multi-Cloud  |  Now GA  |  The role `roles/gkemulticloud.telemetryWriter` (Anthos Multi-cloud Telemetry Writer) is now GA.  
GKE Multi-Cloud  |  Now GA  |  The role `roles/gkemulticloud.viewer` (Anthos Multi-cloud Viewer) is now GA.  
Dataproc Metastore  |  Role Updated  |  The following permissions have been added to the role `roles/metastore.serviceAgent` (Dataproc Metastore Service Agent): `servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
  
Cloud Monitoring  |  Role Updated  |  The following permissions have been added to the role `roles/monitoring.notificationServiceAgent` (Monitoring Service Agent): `servicedirectory.networks.access`  
`servicedirectory.services.resolve`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.subnetworks.use`  
  
Network Connectivity Center  |  Role Updated  |  The following permissions have been added to the role `roles/networkconnectivity.spokeAdmin` (Spoke Admin): `networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.externalSystemsEditor` (Security Center External Systems Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.findingsBulkMuteEditor` (Security Center Findings Bulk Mute Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.findingsMuteSetter` (Security Center Findings Mute Setter) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.muteConfigsEditor` (Security Center Mute Configurations Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.muteConfigsViewer` (Security Center Mute Configurations Viewer) is now GA.  
Web Security Scanner  |  Role Updated  |  The following permissions have been added to the role `roles/websecurityscanner.serviceAgent` (Cloud Web Security Scanner Service Agent): `cloudasset.assets.listResource`  
  
Gemini Enterprise Agent Platform  |  Added  |  `aiplatform.tensorboardRuns.batchCreate`  
`aiplatform.tensorboardTimeSeries.batchCreate`  
`aiplatform.tensorboardTimeSeries.batchRead`  
  
Apigee  |  Added  |  `apigee.developerbalances.adjust`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.developerbalances.adjust`  
  
Apigee  |  Now GA  |  `apigee.developerbalances.adjust`  
  
Artifact Registry  |  Added  |  `artifactregistry.dockerimages.get`  
`artifactregistry.dockerimages.list`  
  
Artifact Registry  |  Now GA  |  `artifactregistry.dockerimages.get`  
`artifactregistry.dockerimages.list`  
  
Compute Engine  |  Added  |  `compute.disks.createTagBinding`  
`compute.disks.deleteTagBinding`  
`compute.disks.listTagBindings`  
`compute.images.createTagBinding`  
`compute.images.deleteTagBinding`  
`compute.images.listTagBindings`  
`compute.snapshots.createTagBinding`  
`compute.snapshots.deleteTagBinding`  
`compute.snapshots.listTagBindings`  
  
Compute Engine  |  Now GA  |  `compute.disks.createTagBinding`  
`compute.disks.deleteTagBinding`  
`compute.disks.listTagBindings`  
`compute.images.createTagBinding`  
`compute.images.deleteTagBinding`  
`compute.images.listTagBindings`  
`compute.machineImages.create`  
`compute.machineImages.delete`  
`compute.machineImages.get`  
`compute.machineImages.getIamPolicy`  
`compute.machineImages.list`  
`compute.machineImages.setIamPolicy`  
`compute.machineImages.useReadOnly`  
`compute.snapshots.createTagBinding`  
`compute.snapshots.deleteTagBinding`  
`compute.snapshots.listTagBindings`  
  
Firestore  |  Added  |  `datastore.keyVisualizerScans.get`  
`datastore.keyVisualizerScans.list`  
  
Firestore  |  Now GA  |  `datastore.keyVisualizerScans.get`  
`datastore.keyVisualizerScans.list`  
  
Datastream  |  Added  |  `datastream.objects.get`  
`datastream.objects.list`  
`datastream.objects.startBackfillJob`  
`datastream.objects.stopBackfillJob`  
  
Document AI  |  Added  |  `documentai.datasetSchemas.get`  
`documentai.datasetSchemas.update`  
`documentai.datasets.get`  
`documentai.datasets.update`  
`documentai.processorTypes.get`  
  
Firebase App Check  |  Added  |  `firebaseappcheck.recaptchaEnterpriseConfig.get`  
`firebaseappcheck.recaptchaEnterpriseConfig.update`  
  
Firebase App Check  |  Supported In Custom Roles  |  `firebaseappcheck.recaptchaEnterpriseConfig.get`  
`firebaseappcheck.recaptchaEnterpriseConfig.update`  
  
GKE Hub  |  Added  |  `gkehub.fleet.create`  
`gkehub.fleet.delete`  
`gkehub.fleet.get`  
`gkehub.fleet.update`  
  
GKE Hub  |  Now GA  |  `gkehub.fleet.create`  
`gkehub.fleet.delete`  
`gkehub.fleet.get`  
`gkehub.fleet.update`  
  
GKE Multi-Cloud  |  Added  |  `gkemulticloud.awsClusters.generateAccessToken`  
`gkemulticloud.azureClusters.generateAccessToken`  
  
GKE Multi-Cloud  |  Now GA  |  `gkemulticloud.awsClusters.create`  
`gkemulticloud.awsClusters.delete`  
`gkemulticloud.awsClusters.generateAccessToken`  
`gkemulticloud.awsClusters.get`  
`gkemulticloud.awsClusters.getAdminKubeconfig`  
`gkemulticloud.awsClusters.list`  
`gkemulticloud.awsClusters.update`  
`gkemulticloud.awsNodePools.create`  
`gkemulticloud.awsNodePools.delete`  
`gkemulticloud.awsNodePools.get`  
`gkemulticloud.awsNodePools.list`  
`gkemulticloud.awsNodePools.update`  
`gkemulticloud.awsServerConfigs.get`  
`gkemulticloud.azureClients.create`  
`gkemulticloud.azureClients.delete`  
`gkemulticloud.azureClients.get`  
`gkemulticloud.azureClients.list`  
`gkemulticloud.azureClusters.create`  
`gkemulticloud.azureClusters.delete`  
`gkemulticloud.azureClusters.generateAccessToken`  
`gkemulticloud.azureClusters.get`  
`gkemulticloud.azureClusters.getAdminKubeconfig`  
`gkemulticloud.azureClusters.list`  
`gkemulticloud.azureClusters.update`  
`gkemulticloud.azureNodePools.create`  
`gkemulticloud.azureNodePools.delete`  
`gkemulticloud.azureNodePools.get`  
`gkemulticloud.azureNodePools.list`  
`gkemulticloud.azureNodePools.update`  
`gkemulticloud.azureServerConfigs.get`  
`gkemulticloud.operations.cancel`  
`gkemulticloud.operations.delete`  
`gkemulticloud.operations.get`  
`gkemulticloud.operations.list`  
`gkemulticloud.operations.wait`  
  
Identity and Access Management  |  Added  |  `iam.denypolicies.create`  
`iam.denypolicies.delete`  
`iam.denypolicies.get`  
`iam.denypolicies.list`  
`iam.denypolicies.replace`  
`iam.denypolicies.update`  
  
Identity and Access Management  |  Added  |  `iam.googleapis.com/denypolicies.create`  
`iam.googleapis.com/denypolicies.delete`  
`iam.googleapis.com/denypolicies.get`  
`iam.googleapis.com/denypolicies.list`  
`iam.googleapis.com/denypolicies.replace`  
  
Cloud Run  |  Added  |  `run.operations.delete`  
`run.operations.get`  
`run.operations.list`  
  
Cloud Run  |  Now GA  |  `run.operations.delete`  
`run.operations.get`  
`run.operations.list`  
  
Security Command Center  |  Added  |  `securitycenter.findingexternalsystems.update`  
`securitycenter.findings.bulkMuteUpdate`  
`securitycenter.findings.setMute`  
`securitycenter.muteconfigs.create`  
`securitycenter.muteconfigs.delete`  
`securitycenter.muteconfigs.get`  
`securitycenter.muteconfigs.list`  
`securitycenter.muteconfigs.update`  
  
Security Command Center  |  Supported In Custom Roles  |  `securitycenter.findingexternalsystems.update`  
`securitycenter.findings.bulkMuteUpdate`  
`securitycenter.findings.setMute`  
`securitycenter.muteconfigs.create`  
`securitycenter.muteconfigs.delete`  
`securitycenter.muteconfigs.get`  
`securitycenter.muteconfigs.list`  
`securitycenter.muteconfigs.update`  
  
Security Command Center  |  Now GA  |  `securitycenter.findingexternalsystems.update`  
`securitycenter.findings.bulkMuteUpdate`  
`securitycenter.findings.setMute`  
`securitycenter.muteconfigs.create`  
`securitycenter.muteconfigs.delete`  
`securitycenter.muteconfigs.get`  
`securitycenter.muteconfigs.list`  
`securitycenter.muteconfigs.update`  
  
Video Stitcher API  |  Added  |  `videostitcher.cdnKeys.create`  
`videostitcher.cdnKeys.delete`  
`videostitcher.cdnKeys.get`  
`videostitcher.cdnKeys.list`  
`videostitcher.cdnKeys.update`  
`videostitcher.liveAdTagDetails.get`  
`videostitcher.liveAdTagDetails.list`  
`videostitcher.liveSessions.create`  
`videostitcher.liveSessions.get`  
`videostitcher.slates.create`  
`videostitcher.slates.delete`  
`videostitcher.slates.get`  
`videostitcher.slates.list`  
`videostitcher.slates.update`  
`videostitcher.vodAdTagDetails.get`  
`videostitcher.vodAdTagDetails.list`  
`videostitcher.vodSessions.create`  
`videostitcher.vodSessions.get`  
`videostitcher.vodStitchDetails.get`  
`videostitcher.vodStitchDetails.list`  
  
  
## Cloud IAM changes as of 2021-10-22

Service | Change | Description  
---|---|---  
Anthos Support  |  Now GA  |  The role `roles/anthossupport.serviceAgent` (Anthos Support Service Agent) is now GA.  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.serviceAgent` (Cloud Functions Service Agent): `source.repos.get`  
`source.repos.list`  
  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.cryptoKeyDecrypterViaDelegation` (Cloud KMS CryptoKey Decrypter Via Delegation) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.cryptoKeyEncrypterDecrypterViaDelegation` (Cloud KMS CryptoKey Encrypter/Decrypter Via Delegation) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.cryptoKeyEncrypterViaDelegation` (Cloud KMS CryptoKey Encrypter Via Delegation) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.expertRawPKCS1` (Cloud KMS Expert Raw PKCS#1 Key Manager) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.viewer` (Cloud KMS Viewer) is now GA.  
Cloud Data Fusion  |  Role Updated  |  The following permissions have been added to the role `roles/datafusion.serviceAgent` (Cloud Data Fusion API Service Agent): `dataproc.operations.cancel`  
  
Data Pipelines  |  Now GA  |  The role `roles/datapipelines.admin` (Data pipelines Admin) is now GA.  
Data Pipelines  |  Now GA  |  The role `roles/datapipelines.invoker` (Data pipelines Invoker) is now GA.  
Data Pipelines  |  Now GA  |  The role `roles/datapipelines.viewer` (Data pipelines Viewer) is now GA.  
Managed Service for Apache Spark  |  Role Updated  |  The following permissions have been added to the role `roles/dataproc.editor` (Dataproc Editor): `dataproc.operations.cancel`  
  
Managed Service for Apache Spark  |  Role Updated  |  The following permissions have been added to the role `roles/dataproc.serviceAgent` (Dataproc Service Agent): `dataproc.autoscalingPolicies.create`  
`dataproc.autoscalingPolicies.delete`  
`dataproc.autoscalingPolicies.getIamPolicy`  
`dataproc.autoscalingPolicies.update`  
  
Customer Usage Data Processing  |  Now GA  |  The role `roles/dataprocessing.dataSourceManager` (Data Processing Controls Data Source Manager) is now GA.  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.serviceAgent` (Dialogflow Service Agent): `storage.objects.create`  
  
Cloud Domains  |  Now GA  |  The role `roles/domains.admin` (Cloud Domains Admin) is now GA.  
Cloud Domains  |  Now GA  |  The role `roles/domains.viewer` (Cloud Domains Viewer) is now GA.  
Game Servers  |  Role Updated  |  The following permissions have been added to the role `roles/gameservices.serviceAgent` (Game Services Service Agent): `iam.serviceAccounts.actAs`  
  
Managed Service for Microsoft Active Directory  |  Now GA  |  The role `roles/managedidentities.peeringAdmin` (Google Cloud Managed Identities Peering Admin) is now GA.  
Managed Service for Microsoft Active Directory  |  Now GA  |  The role `roles/managedidentities.peeringViewer` (Google Cloud Managed Identities Peering Viewer) is now GA.  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.addresses.createInternal`  
`compute.addresses.deleteInternal`  
`compute.addresses.useInternal`  
  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.securityResponseServiceAgent` (Google Cloud Security Response Service Agent) is now GA.  
Cloud Key Management Service  |  Added  |  `cloudkms.cryptoKeyVersions.manageRawPKCS1Keys`  
`cloudkms.cryptoKeyVersions.useToDecryptViaDelegation`  
`cloudkms.cryptoKeyVersions.useToEncryptViaDelegation`  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `cloudkms.cryptoKeyVersions.manageRawPKCS1Keys`  
`cloudkms.cryptoKeyVersions.useToDecryptViaDelegation`  
`cloudkms.cryptoKeyVersions.useToEncryptViaDelegation`  
  
Cloud Key Management Service  |  Now GA  |  `cloudkms.cryptoKeyVersions.manageRawPKCS1Keys`  
`cloudkms.cryptoKeyVersions.useToDecryptViaDelegation`  
`cloudkms.cryptoKeyVersions.useToEncryptViaDelegation`  
  
Compute Engine  |  Added  |  `compute.reservations.update`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.reservations.update`  
  
Data Pipelines  |  Now GA  |  `datapipelines.pipelines.create`  
`datapipelines.pipelines.delete`  
`datapipelines.pipelines.get`  
`datapipelines.pipelines.list`  
`datapipelines.pipelines.run`  
`datapipelines.pipelines.stop`  
`datapipelines.pipelines.update`  
  
Cloud Domains  |  Supported In Custom Roles  |  `domains.locations.get`  
`domains.locations.list`  
`domains.operations.cancel`  
`domains.operations.get`  
`domains.operations.list`  
  
Cloud Domains  |  Now GA  |  `domains.locations.get`  
`domains.locations.list`  
`domains.operations.cancel`  
`domains.operations.get`  
`domains.operations.list`  
`domains.registrations.configureContact`  
`domains.registrations.configureDns`  
`domains.registrations.configureManagement`  
`domains.registrations.create`  
`domains.registrations.delete`  
`domains.registrations.get`  
`domains.registrations.getIamPolicy`  
`domains.registrations.list`  
`domains.registrations.setIamPolicy`  
`domains.registrations.update`  
  
Firebase Cloud Messaging  |  Added  |  `firebasecloudmessaging.messages.create`  
  
Managed Service for Microsoft Active Directory  |  Now GA  |  `managedidentities.peerings.create`  
`managedidentities.peerings.delete`  
`managedidentities.peerings.get`  
`managedidentities.peerings.getIamPolicy`  
`managedidentities.peerings.list`  
`managedidentities.peerings.setIamPolicy`  
`managedidentities.peerings.update`  
  
Google Cloud Fraud Defense  |  Added  |  `recaptchaenterprise.relatedaccountgroupmemberships.list`  
`recaptchaenterprise.relatedaccountgroups.list`  
  
  
## Cloud IAM changes as of 2021-10-01

Service | Change | Description  
---|---|---  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.serviceAgent` (Vertex AI Service Agent): `compute.machineTypes.get`  
`dataflow.jobs.cancel`  
`dataflow.jobs.create`  
`dataflow.jobs.get`  
`dataflow.jobs.list`  
`dataflow.jobs.snapshot`  
`dataflow.jobs.updateContents`  
`dataflow.messages.list`  
`dataflow.metrics.get`  
`dataflow.snapshots.delete`  
`dataflow.snapshots.get`  
`dataflow.snapshots.list`  
  
Artifact Registry  |  Role Updated  |  The following permissions have been added to the role `roles/artifactregistry.serviceAgent` (Artifact Registry Service Agent): `artifactregistry.repositories.downloadArtifacts`  
  
Cloud TPU  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtpu.serviceAgent` (Cloud TPU V2 API Service Agent): `servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
  
Connectors  |  Now GA  |  The role `roles/connectors.admin` (Connector Admin) is now GA.  
Connectors  |  Now GA  |  The role `roles/connectors.viewer` (Connectors Viewer) is now GA.  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
  
Sensitive Data Protection  |  Role Updated  |  The following permissions have been added to the role `roles/dlp.serviceAgent` (DLP API Service Agent): `datacatalog.categories.fineGrainedGet`  
  
Firebase Mods  |  Role Updated  |  The following permissions have been added to the role `roles/firebasemods.serviceAgent` (Firebase Extensions API Service Agent): `resourcemanager.projects.updateLiens`  
  
GKE Hub  |  Now GA  |  The role `roles/gkehub.editor` (GKE Hub Editor) is now GA.  
Transcoder API  |  Role Updated  |  The following permissions have been added to the role `roles/transcoder.serviceAgent` (Transcoder Service Agent): `transcoder.jobs.delete`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `firebaserules.rulesets.test`  
  
Connectors  |  Added  |  `connectors.connections.create`  
`connectors.connections.delete`  
`connectors.connections.get`  
`connectors.connections.getConnectionSchemaMetadata`  
`connectors.connections.getIamPolicy`  
`connectors.connections.getRuntimeActionSchema`  
`connectors.connections.getRuntimeEntitySchema`  
`connectors.connections.list`  
`connectors.connections.setIamPolicy`  
`connectors.connections.update`  
`connectors.connectors.get`  
`connectors.connectors.list`  
`connectors.locations.get`  
`connectors.locations.list`  
`connectors.operations.cancel`  
`connectors.operations.delete`  
`connectors.operations.get`  
`connectors.operations.list`  
`connectors.providers.get`  
`connectors.providers.list`  
`connectors.runtimeconfig.get`  
`connectors.versions.get`  
`connectors.versions.list`  
  
Connectors  |  Supported In Custom Roles  |  `connectors.connections.create`  
`connectors.connections.delete`  
`connectors.connections.get`  
`connectors.connections.getConnectionSchemaMetadata`  
`connectors.connections.getIamPolicy`  
`connectors.connections.getRuntimeActionSchema`  
`connectors.connections.getRuntimeEntitySchema`  
`connectors.connections.list`  
`connectors.connections.setIamPolicy`  
`connectors.connections.update`  
`connectors.connectors.get`  
`connectors.connectors.list`  
`connectors.locations.get`  
`connectors.locations.list`  
`connectors.operations.cancel`  
`connectors.operations.delete`  
`connectors.operations.get`  
`connectors.operations.list`  
`connectors.providers.get`  
`connectors.providers.list`  
`connectors.runtimeconfig.get`  
`connectors.versions.get`  
`connectors.versions.list`  
  
Connectors  |  Now GA  |  `connectors.connections.create`  
`connectors.connections.delete`  
`connectors.connections.get`  
`connectors.connections.getConnectionSchemaMetadata`  
`connectors.connections.getIamPolicy`  
`connectors.connections.getRuntimeActionSchema`  
`connectors.connections.getRuntimeEntitySchema`  
`connectors.connections.list`  
`connectors.connections.setIamPolicy`  
`connectors.connections.update`  
`connectors.connectors.get`  
`connectors.connectors.list`  
`connectors.locations.get`  
`connectors.locations.list`  
`connectors.operations.cancel`  
`connectors.operations.delete`  
`connectors.operations.get`  
`connectors.operations.list`  
`connectors.providers.get`  
`connectors.providers.list`  
`connectors.runtimeconfig.get`  
`connectors.versions.get`  
`connectors.versions.list`  
  
  
## Cloud IAM changes as of 2021-09-24

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.clusterRoleBindings.create`  
`container.clusterRoleBindings.delete`  
`container.clusterRoleBindings.get`  
`container.clusterRoleBindings.list`  
`container.clusterRoleBindings.update`  
`container.clusterRoles.bind`  
`container.clusterRoles.create`  
`container.clusterRoles.delete`  
`container.clusterRoles.escalate`  
`container.clusterRoles.get`  
`container.clusterRoles.list`  
`container.configMaps.create`  
`container.configMaps.delete`  
`container.configMaps.update`  
`container.daemonSets.create`  
`container.daemonSets.delete`  
`container.daemonSets.get`  
`container.daemonSets.getStatus`  
`container.daemonSets.list`  
`container.daemonSets.update`  
`container.serviceAccounts.create`  
`container.serviceAccounts.delete`  
`container.serviceAccounts.get`  
`container.serviceAccounts.list`  
`container.serviceAccounts.update`  
  
Cloud SQL  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsql.admin` (Cloud SQL Admin): `recommender.cloudsqlIdleInstanceRecommendations.get`  
`recommender.cloudsqlIdleInstanceRecommendations.list`  
`recommender.cloudsqlIdleInstanceRecommendations.update`  
`recommender.cloudsqlInstanceActivityInsights.get`  
`recommender.cloudsqlInstanceActivityInsights.list`  
`recommender.cloudsqlInstanceActivityInsights.update`  
`recommender.cloudsqlInstanceCpuUsageInsights.get`  
`recommender.cloudsqlInstanceCpuUsageInsights.list`  
`recommender.cloudsqlInstanceCpuUsageInsights.update`  
`recommender.cloudsqlInstanceMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceMemoryUsageInsights.list`  
`recommender.cloudsqlInstanceMemoryUsageInsights.update`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.get`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.list`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.update`  
  
Cloud SQL  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsql.editor` (Cloud SQL Editor): `recommender.cloudsqlIdleInstanceRecommendations.get`  
`recommender.cloudsqlIdleInstanceRecommendations.list`  
`recommender.cloudsqlIdleInstanceRecommendations.update`  
`recommender.cloudsqlInstanceActivityInsights.get`  
`recommender.cloudsqlInstanceActivityInsights.list`  
`recommender.cloudsqlInstanceActivityInsights.update`  
`recommender.cloudsqlInstanceCpuUsageInsights.get`  
`recommender.cloudsqlInstanceCpuUsageInsights.list`  
`recommender.cloudsqlInstanceCpuUsageInsights.update`  
`recommender.cloudsqlInstanceMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceMemoryUsageInsights.list`  
`recommender.cloudsqlInstanceMemoryUsageInsights.update`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.get`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.list`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.update`  
  
Cloud SQL  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsql.viewer` (Cloud SQL Viewer): `recommender.cloudsqlIdleInstanceRecommendations.get`  
`recommender.cloudsqlIdleInstanceRecommendations.list`  
`recommender.cloudsqlInstanceActivityInsights.get`  
`recommender.cloudsqlInstanceActivityInsights.list`  
`recommender.cloudsqlInstanceCpuUsageInsights.get`  
`recommender.cloudsqlInstanceCpuUsageInsights.list`  
`recommender.cloudsqlInstanceMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceMemoryUsageInsights.list`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.get`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.list`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
`recommender.cloudsqlIdleInstanceRecommendations.get`  
`recommender.cloudsqlIdleInstanceRecommendations.list`  
`recommender.cloudsqlIdleInstanceRecommendations.update`  
`recommender.cloudsqlInstanceActivityInsights.get`  
`recommender.cloudsqlInstanceActivityInsights.list`  
`recommender.cloudsqlInstanceActivityInsights.update`  
`recommender.cloudsqlInstanceCpuUsageInsights.get`  
`recommender.cloudsqlInstanceCpuUsageInsights.list`  
`recommender.cloudsqlInstanceCpuUsageInsights.update`  
`recommender.cloudsqlInstanceMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceMemoryUsageInsights.list`  
`recommender.cloudsqlInstanceMemoryUsageInsights.update`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.get`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.list`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.update`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.hostServiceAgentUser` (Kubernetes Engine Host Service Agent User): `dns.responsePolicies.create`  
`dns.responsePolicies.delete`  
`dns.responsePolicies.get`  
`dns.responsePolicies.list`  
`dns.responsePolicies.update`  
`dns.responsePolicyRules.create`  
`dns.responsePolicyRules.delete`  
`dns.responsePolicyRules.get`  
`dns.responsePolicyRules.list`  
`dns.responsePolicyRules.update`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Firebase Mods  |  Role Updated  |  The following permissions have been added to the role `roles/firebasemods.serviceAgent` (Firebase Extensions API Service Agent): `iam.serviceAccounts.create`  
`iam.serviceAccounts.get`  
`iam.serviceAccounts.list`  
  
Game Servers  |  Role Updated  |  The following permissions have been added to the role `roles/gameservices.serviceAgent` (Game Services Service Agent): `container.mutatingWebhookConfigurations.create`  
`container.mutatingWebhookConfigurations.delete`  
`container.mutatingWebhookConfigurations.update`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.configWriter` (Logs Configuration Writer): `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Dataproc Metastore  |  Role Updated  |  The following permissions have been added to the role `roles/metastore.serviceAgent` (Dataproc Metastore Service Agent): `compute.addresses.createInternal`  
`compute.addresses.deleteInternal`  
`compute.addresses.get`  
`compute.addresses.use`  
`compute.forwardingRules.create`  
`compute.forwardingRules.delete`  
`compute.forwardingRules.get`  
`compute.forwardingRules.pscCreate`  
`compute.forwardingRules.pscDelete`  
`compute.regionOperations.get`  
`compute.subnetworks.get`  
`compute.subnetworks.use`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.addresses.use`  
`compute.regionSslCertificates.create`  
`compute.regionSslCertificates.delete`  
`compute.regionSslCertificates.get`  
`compute.regionSslCertificates.list`  
  
Recommender  |  Role Added  |  The role `roles/recommender.bigQueryCapacityCommitmentsAdmin` (Bigquery Slot Recommender Admin) has been added with the following permissions: `cloudresourcemanager.googleapis.com/projects.get`  
`cloudresourcemanager.googleapis.com/projects.list`  
`recommender.bigqueryCapacityCommitmentsInsights.get`  
`recommender.bigqueryCapacityCommitmentsInsights.list`  
`recommender.bigqueryCapacityCommitmentsInsights.update`  
`recommender.bigqueryCapacityCommitmentsRecommendations.get`  
`recommender.bigqueryCapacityCommitmentsRecommendations.list`  
`recommender.bigqueryCapacityCommitmentsRecommendations.update`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsInsights.get`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsInsights.list`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsInsights.update`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsRecommendations.get`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsRecommendations.list`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsRecommendations.update`  
`recommender.googleapis.com/locations.get`  
`recommender.googleapis.com/locations.list`  
`recommender.locations.get`  
`recommender.locations.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Recommender  |  Role Added  |  The role `roles/recommender.bigQueryCapacityCommitmentsViewer` (Bigquery Slot Recommender Viewer) has been added with the following permissions: `cloudresourcemanager.googleapis.com/projects.get`  
`cloudresourcemanager.googleapis.com/projects.list`  
`recommender.bigqueryCapacityCommitmentsInsights.get`  
`recommender.bigqueryCapacityCommitmentsInsights.list`  
`recommender.bigqueryCapacityCommitmentsRecommendations.get`  
`recommender.bigqueryCapacityCommitmentsRecommendations.list`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsInsights.get`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsInsights.list`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsRecommendations.get`  
`recommender.googleapis.com/bigqueryCapacityCommitmentsRecommendations.list`  
`recommender.googleapis.com/locations.get`  
`recommender.googleapis.com/locations.list`  
`recommender.locations.get`  
`recommender.locations.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Firestore  |  Added  |  `datastore.databases.getMetadata`  
  
Firestore  |  Now GA  |  `datastore.databases.getMetadata`  
  
Cloud Integrations  |  Added  |  `integrations.securityAuthConfigs.create`  
`integrations.securityAuthConfigs.delete`  
`integrations.securityAuthConfigs.get`  
`integrations.securityAuthConfigs.list`  
`integrations.securityAuthConfigs.update`  
`integrations.securityExecutions.cancel`  
`integrations.securityExecutions.get`  
`integrations.securityExecutions.list`  
`integrations.securityIntegTempVers.create`  
`integrations.securityIntegTempVers.get`  
`integrations.securityIntegTempVers.list`  
`integrations.securityIntegrationVers.create`  
`integrations.securityIntegrationVers.deploy`  
`integrations.securityIntegrationVers.get`  
`integrations.securityIntegrationVers.list`  
`integrations.securityIntegrationVers.update`  
`integrations.securityIntegrations.invoke`  
`integrations.securityIntegrations.list`  
  
Recommender  |  Added  |  `recommender.bigqueryCapacityCommitmentsInsights.get`  
`recommender.bigqueryCapacityCommitmentsInsights.list`  
`recommender.bigqueryCapacityCommitmentsInsights.update`  
`recommender.bigqueryCapacityCommitmentsRecommendations.get`  
`recommender.bigqueryCapacityCommitmentsRecommendations.list`  
`recommender.bigqueryCapacityCommitmentsRecommendations.update`  
`recommender.cloudsqlIdleInstanceRecommendations.get`  
`recommender.cloudsqlIdleInstanceRecommendations.list`  
`recommender.cloudsqlIdleInstanceRecommendations.update`  
`recommender.cloudsqlInstanceActivityInsights.get`  
`recommender.cloudsqlInstanceActivityInsights.list`  
`recommender.cloudsqlInstanceActivityInsights.update`  
`recommender.cloudsqlInstanceCpuUsageInsights.get`  
`recommender.cloudsqlInstanceCpuUsageInsights.list`  
`recommender.cloudsqlInstanceCpuUsageInsights.update`  
`recommender.cloudsqlInstanceMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceMemoryUsageInsights.list`  
`recommender.cloudsqlInstanceMemoryUsageInsights.update`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.get`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.list`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.bigqueryCapacityCommitmentsInsights.get`  
`recommender.bigqueryCapacityCommitmentsInsights.list`  
`recommender.bigqueryCapacityCommitmentsInsights.update`  
`recommender.bigqueryCapacityCommitmentsRecommendations.get`  
`recommender.bigqueryCapacityCommitmentsRecommendations.list`  
`recommender.bigqueryCapacityCommitmentsRecommendations.update`  
`recommender.cloudsqlIdleInstanceRecommendations.get`  
`recommender.cloudsqlIdleInstanceRecommendations.list`  
`recommender.cloudsqlIdleInstanceRecommendations.update`  
`recommender.cloudsqlInstanceActivityInsights.get`  
`recommender.cloudsqlInstanceActivityInsights.list`  
`recommender.cloudsqlInstanceActivityInsights.update`  
`recommender.cloudsqlInstanceCpuUsageInsights.get`  
`recommender.cloudsqlInstanceCpuUsageInsights.list`  
`recommender.cloudsqlInstanceCpuUsageInsights.update`  
`recommender.cloudsqlInstanceMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceMemoryUsageInsights.list`  
`recommender.cloudsqlInstanceMemoryUsageInsights.update`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.get`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.list`  
`recommender.cloudsqlOverprovisionedInstanceRecommendations.update`  
  
  
## Cloud IAM changes as of 2021-09-10

Service | Change | Description  
---|---|---  
BigQuery  |  Added  |  `bigquery.tables.createSnapshot`  
`bigquery.tables.deleteSnapshot`  
`bigquery.tables.restoreSnapshot`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.tables.createSnapshot`  
`bigquery.tables.deleteSnapshot`  
`bigquery.tables.restoreSnapshot`  
  
Firebase  |  Added  |  `firebase.playLinks.get`  
`firebase.playLinks.list`  
`firebase.playLinks.update`  
  
Firebase  |  Supported In Custom Roles  |  `firebase.playLinks.get`  
`firebase.playLinks.list`  
`firebase.playLinks.update`  
  
Firebase  |  Now GA  |  `firebase.playLinks.get`  
`firebase.playLinks.list`  
`firebase.playLinks.update`  
  
  
## Cloud IAM changes as of 2021-08-30

Service | Change | Description  
---|---|---  
Cloud Build  |  Role Updated  |  The following permissions have been added to the role `roles/cloudbuild.serviceAgent` (Cloud Build Service Agent): `binaryauthorization.attestors.create`  
`binaryauthorization.attestors.delete`  
`binaryauthorization.attestors.get`  
`binaryauthorization.attestors.list`  
`binaryauthorization.attestors.update`  
`binaryauthorization.attestors.verifyImageAttested`  
`containeranalysis.notes.attachOccurrence`  
`containeranalysis.notes.create`  
`containeranalysis.notes.delete`  
`containeranalysis.notes.get`  
`containeranalysis.notes.list`  
`containeranalysis.notes.update`  
  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.admin` (Data Catalog Admin): `bigquery.connections.get`  
`bigquery.routines.get`  
  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.viewer` (Data Catalog Viewer): `bigquery.connections.get`  
`bigquery.routines.get`  
  
GKE Hub  |  Now GA  |  The role `roles/gkehub.gatewayReader` (Connect Gateway Reader) is now GA.  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.serviceAgent` (GKE Hub Service Agent): `gkemulticloud.awsClusters.get`  
`gkemulticloud.azureClusters.get`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.sslPolicies.use`  
  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.inventoryViewer` (OS Inventory Viewer) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.vulnerabilityReportViewer` (OS VulnerabilityReport Viewer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.integrationExecutorServiceAgent` (Security Center Integration Executor Service Agent) is now GA.  
Storage Transfer Service  |  Role Updated  |  The following permissions have been added to the role `roles/storagetransfer.viewer` (Storage Transfer Viewer): `storagetransfer.agentpools.get`  
`storagetransfer.agentpools.list`  
  
Cloud OS Config  |  Now GA  |  `osconfig.inventories.get`  
`osconfig.inventories.list`  
`osconfig.vulnerabilityReports.get`  
`osconfig.vulnerabilityReports.list`  
  
  
## Cloud IAM changes as of 2021-08-27

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.thirdPartyObjects.create`  
  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.instancesadmin` (Bare Metal Solution Instances Admin) is now GA.  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.instancesviewer` (Bare Metal Solution Instances Viewer) is now GA.  
Cloud Deploy  |  Role Added  |  The role `roles/clouddeploy.releaser` (Cloud Deploy Releaser) has been added with the following permissions: `clouddeploy.deliveryPipelines.get`  
`clouddeploy.googleapis.com/deliveryPipelines.get`  
`clouddeploy.googleapis.com/locations.get`  
`clouddeploy.googleapis.com/locations.list`  
`clouddeploy.googleapis.com/operations.cancel`  
`clouddeploy.googleapis.com/operations.delete`  
`clouddeploy.googleapis.com/operations.get`  
`clouddeploy.googleapis.com/operations.list`  
`clouddeploy.googleapis.com/releases.create`  
`clouddeploy.googleapis.com/releases.get`  
`clouddeploy.googleapis.com/releases.list`  
`clouddeploy.googleapis.com/rollouts.create`  
`clouddeploy.googleapis.com/rollouts.get`  
`clouddeploy.googleapis.com/rollouts.list`  
`clouddeploy.googleapis.com/targets.get`  
`clouddeploy.locations.get`  
`clouddeploy.locations.list`  
`clouddeploy.operations.cancel`  
`clouddeploy.operations.delete`  
`clouddeploy.operations.get`  
`clouddeploy.operations.list`  
`clouddeploy.releases.create`  
`clouddeploy.releases.get`  
`clouddeploy.releases.list`  
`clouddeploy.rollouts.create`  
`clouddeploy.rollouts.get`  
`clouddeploy.rollouts.list`  
`clouddeploy.targets.get`  
`cloudresourcemanager.googleapis.com/projects.get`  
`cloudresourcemanager.googleapis.com/projects.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Deploy  |  Role Updated  |  The following permissions have been added to the role `roles/clouddeploy.serviceAgent` (Cloud Deploy Service Agent): `cloudbuild.workerpools.use`  
  
Content Warehouse  |  Role Updated  |  The following permissions have been added to the role `roles/contentwarehouse.serviceAgent` (Content Warehouse Service Agent): `cloudfunctions.functions.invoke`  
`pubsub.topics.publish`  
`pubsublite.topics.publish`  
  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.orgdriver` (DLP Organization Data Profiles Driver) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.projectdriver` (DLP Project Data Profiles Driver) is now GA.  
Sensitive Data Protection  |  Role Updated  |  The following permissions have been added to the role `roles/dlp.serviceAgent` (DLP API Service Agent): `cloudasset.assets.analyzeIamPolicy`  
`cloudasset.assets.exportResource`  
  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.gatewayAdmin` (Connect Gateway Admin): `serviceusage.services.get`  
  
Cloud Logging  |  Now GA  |  The role `roles/logging.fieldAccessor` (Log Field Accessor) is now GA.  
Apigee  |  Added  |  `apigee.proxies.update`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.proxies.update`  
  
Apigee  |  Now GA  |  `apigee.proxies.update`  
  
Bare Metal Solution  |  Added  |  `baremetalsolution.instances.create`  
`baremetalsolution.instances.get`  
`baremetalsolution.instances.list`  
  
Bare Metal Solution  |  Supported In Custom Roles  |  `baremetalsolution.instances.create`  
`baremetalsolution.instances.get`  
`baremetalsolution.instances.list`  
  
Bare Metal Solution  |  Now GA  |  `baremetalsolution.instances.create`  
`baremetalsolution.instances.get`  
`baremetalsolution.instances.list`  
  
BigQuery  |  Added  |  `bigquery.jobs.delete`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.jobs.delete`  
  
BigQuery  |  Now GA  |  `bigquery.jobs.delete`  
  
Cloud Deploy  |  Added  |  `clouddeploy.config.get`  
`clouddeploy.deliveryPipelines.create`  
`clouddeploy.deliveryPipelines.delete`  
`clouddeploy.deliveryPipelines.get`  
`clouddeploy.deliveryPipelines.getIamPolicy`  
`clouddeploy.deliveryPipelines.list`  
`clouddeploy.deliveryPipelines.setIamPolicy`  
`clouddeploy.deliveryPipelines.update`  
`clouddeploy.locations.get`  
`clouddeploy.locations.list`  
`clouddeploy.operations.cancel`  
`clouddeploy.operations.delete`  
`clouddeploy.operations.get`  
`clouddeploy.operations.list`  
`clouddeploy.releases.create`  
`clouddeploy.releases.delete`  
`clouddeploy.releases.get`  
`clouddeploy.releases.list`  
`clouddeploy.rollouts.approve`  
`clouddeploy.rollouts.create`  
`clouddeploy.rollouts.get`  
`clouddeploy.rollouts.list`  
`clouddeploy.targets.create`  
`clouddeploy.targets.delete`  
`clouddeploy.targets.get`  
`clouddeploy.targets.getIamPolicy`  
`clouddeploy.targets.list`  
`clouddeploy.targets.setIamPolicy`  
`clouddeploy.targets.update`  
  
Cloud Deploy  |  Supported In Custom Roles  |  `clouddeploy.config.get`  
`clouddeploy.deliveryPipelines.create`  
`clouddeploy.deliveryPipelines.delete`  
`clouddeploy.deliveryPipelines.get`  
`clouddeploy.deliveryPipelines.getIamPolicy`  
`clouddeploy.deliveryPipelines.list`  
`clouddeploy.deliveryPipelines.setIamPolicy`  
`clouddeploy.deliveryPipelines.update`  
`clouddeploy.locations.get`  
`clouddeploy.locations.list`  
`clouddeploy.operations.cancel`  
`clouddeploy.operations.delete`  
`clouddeploy.operations.get`  
`clouddeploy.operations.list`  
`clouddeploy.releases.create`  
`clouddeploy.releases.delete`  
`clouddeploy.releases.get`  
`clouddeploy.releases.list`  
`clouddeploy.rollouts.approve`  
`clouddeploy.rollouts.create`  
`clouddeploy.rollouts.get`  
`clouddeploy.rollouts.list`  
`clouddeploy.targets.create`  
`clouddeploy.targets.delete`  
`clouddeploy.targets.get`  
`clouddeploy.targets.getIamPolicy`  
`clouddeploy.targets.list`  
`clouddeploy.targets.setIamPolicy`  
`clouddeploy.targets.update`  
  
Cloud Run functions  |  Added  |  `cloudfunctions.functions.generateUploadUrl`  
  
Compute Engine  |  Added  |  `compute.forwardingRules.use`  
  
Dialogflow  |  Added  |  `dialogflow.conversations.update`  
  
Dialogflow  |  Now GA  |  `dialogflow.conversations.update`  
  
Cloud Integrations  |  Added  |  `integrations.apigeeIntegrationVers.delete`  
  
Cloud Integrations  |  Now GA  |  `integrations.apigeeIntegrationVers.delete`  
  
Cloud Logging  |  Now GA  |  `logging.fields.access`  
  
Storage Transfer Service  |  Added  |  `storagetransfer.agentpools.create`  
`storagetransfer.agentpools.delete`  
`storagetransfer.agentpools.get`  
`storagetransfer.agentpools.list`  
`storagetransfer.agentpools.update`  
  
Storage Transfer Service  |  Now GA  |  `storagetransfer.agentpools.create`  
`storagetransfer.agentpools.delete`  
`storagetransfer.agentpools.get`  
`storagetransfer.agentpools.list`  
`storagetransfer.agentpools.update`  
  
  
## Cloud IAM changes as of 2021-08-20

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.thirdPartyObjects.create`  
  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.instancesadmin` (Bare Metal Solution Instances Admin) is now GA.  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.instancesviewer` (Bare Metal Solution Instances Viewer) is now GA.  
Cloud Deploy  |  Role Added  |  The role `roles/clouddeploy.releaser` (Cloud Deploy Releaser) has been added with the following permissions: `clouddeploy.deliveryPipelines.get`  
`clouddeploy.googleapis.com/deliveryPipelines.get`  
`clouddeploy.googleapis.com/locations.get`  
`clouddeploy.googleapis.com/locations.list`  
`clouddeploy.googleapis.com/operations.cancel`  
`clouddeploy.googleapis.com/operations.delete`  
`clouddeploy.googleapis.com/operations.get`  
`clouddeploy.googleapis.com/operations.list`  
`clouddeploy.googleapis.com/releases.create`  
`clouddeploy.googleapis.com/releases.get`  
`clouddeploy.googleapis.com/releases.list`  
`clouddeploy.googleapis.com/rollouts.create`  
`clouddeploy.googleapis.com/rollouts.get`  
`clouddeploy.googleapis.com/rollouts.list`  
`clouddeploy.googleapis.com/targets.get`  
`clouddeploy.locations.get`  
`clouddeploy.locations.list`  
`clouddeploy.operations.cancel`  
`clouddeploy.operations.delete`  
`clouddeploy.operations.get`  
`clouddeploy.operations.list`  
`clouddeploy.releases.create`  
`clouddeploy.releases.get`  
`clouddeploy.releases.list`  
`clouddeploy.rollouts.create`  
`clouddeploy.rollouts.get`  
`clouddeploy.rollouts.list`  
`clouddeploy.targets.get`  
`cloudresourcemanager.googleapis.com/projects.get`  
`cloudresourcemanager.googleapis.com/projects.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Deploy  |  Role Updated  |  The following permissions have been added to the role `roles/clouddeploy.serviceAgent` (Cloud Deploy Service Agent): `cloudbuild.workerpools.use`  
  
Content Warehouse  |  Role Updated  |  The following permissions have been added to the role `roles/contentwarehouse.serviceAgent` (Content Warehouse Service Agent): `cloudfunctions.functions.invoke`  
`pubsub.topics.publish`  
`pubsublite.topics.publish`  
  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.orgdriver` (DLP Organization Data Profiles Driver) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.projectdriver` (DLP Project Data Profiles Driver) is now GA.  
Sensitive Data Protection  |  Role Updated  |  The following permissions have been added to the role `roles/dlp.serviceAgent` (DLP API Service Agent): `cloudasset.assets.analyzeIamPolicy`  
`cloudasset.assets.exportResource`  
  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.gatewayAdmin` (Connect Gateway Admin): `serviceusage.services.get`  
  
Cloud Logging  |  Now GA  |  The role `roles/logging.fieldAccessor` (Log Field Accessor) is now GA.  
Apigee  |  Added  |  `apigee.proxies.update`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.proxies.update`  
  
Apigee  |  Now GA  |  `apigee.proxies.update`  
  
Bare Metal Solution  |  Added  |  `baremetalsolution.instances.create`  
`baremetalsolution.instances.get`  
`baremetalsolution.instances.list`  
  
Bare Metal Solution  |  Supported In Custom Roles  |  `baremetalsolution.instances.create`  
`baremetalsolution.instances.get`  
`baremetalsolution.instances.list`  
  
Bare Metal Solution  |  Now GA  |  `baremetalsolution.instances.create`  
`baremetalsolution.instances.get`  
`baremetalsolution.instances.list`  
  
BigQuery  |  Added  |  `bigquery.jobs.delete`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.jobs.delete`  
  
BigQuery  |  Now GA  |  `bigquery.jobs.delete`  
  
Cloud Deploy  |  Added  |  `clouddeploy.config.get`  
`clouddeploy.deliveryPipelines.create`  
`clouddeploy.deliveryPipelines.delete`  
`clouddeploy.deliveryPipelines.get`  
`clouddeploy.deliveryPipelines.getIamPolicy`  
`clouddeploy.deliveryPipelines.list`  
`clouddeploy.deliveryPipelines.setIamPolicy`  
`clouddeploy.deliveryPipelines.update`  
`clouddeploy.locations.get`  
`clouddeploy.locations.list`  
`clouddeploy.operations.cancel`  
`clouddeploy.operations.delete`  
`clouddeploy.operations.get`  
`clouddeploy.operations.list`  
`clouddeploy.releases.create`  
`clouddeploy.releases.delete`  
`clouddeploy.releases.get`  
`clouddeploy.releases.list`  
`clouddeploy.rollouts.approve`  
`clouddeploy.rollouts.create`  
`clouddeploy.rollouts.get`  
`clouddeploy.rollouts.list`  
`clouddeploy.targets.create`  
`clouddeploy.targets.delete`  
`clouddeploy.targets.get`  
`clouddeploy.targets.getIamPolicy`  
`clouddeploy.targets.list`  
`clouddeploy.targets.setIamPolicy`  
`clouddeploy.targets.update`  
  
Cloud Deploy  |  Supported In Custom Roles  |  `clouddeploy.config.get`  
`clouddeploy.deliveryPipelines.create`  
`clouddeploy.deliveryPipelines.delete`  
`clouddeploy.deliveryPipelines.get`  
`clouddeploy.deliveryPipelines.getIamPolicy`  
`clouddeploy.deliveryPipelines.list`  
`clouddeploy.deliveryPipelines.setIamPolicy`  
`clouddeploy.deliveryPipelines.update`  
`clouddeploy.locations.get`  
`clouddeploy.locations.list`  
`clouddeploy.operations.cancel`  
`clouddeploy.operations.delete`  
`clouddeploy.operations.get`  
`clouddeploy.operations.list`  
`clouddeploy.releases.create`  
`clouddeploy.releases.delete`  
`clouddeploy.releases.get`  
`clouddeploy.releases.list`  
`clouddeploy.rollouts.approve`  
`clouddeploy.rollouts.create`  
`clouddeploy.rollouts.get`  
`clouddeploy.rollouts.list`  
`clouddeploy.targets.create`  
`clouddeploy.targets.delete`  
`clouddeploy.targets.get`  
`clouddeploy.targets.getIamPolicy`  
`clouddeploy.targets.list`  
`clouddeploy.targets.setIamPolicy`  
`clouddeploy.targets.update`  
  
Cloud Run functions  |  Added  |  `cloudfunctions.functions.generateUploadUrl`  
  
Compute Engine  |  Added  |  `compute.forwardingRules.use`  
  
Dialogflow  |  Added  |  `dialogflow.conversations.update`  
  
Dialogflow  |  Now GA  |  `dialogflow.conversations.update`  
  
Cloud Integrations  |  Added  |  `integrations.apigeeIntegrationVers.delete`  
  
Cloud Integrations  |  Now GA  |  `integrations.apigeeIntegrationVers.delete`  
  
Cloud Logging  |  Now GA  |  `logging.fields.access`  
  
Storage Transfer Service  |  Added  |  `storagetransfer.agentpools.create`  
`storagetransfer.agentpools.delete`  
`storagetransfer.agentpools.get`  
`storagetransfer.agentpools.list`  
`storagetransfer.agentpools.update`  
  
Storage Transfer Service  |  Now GA  |  `storagetransfer.agentpools.create`  
`storagetransfer.agentpools.delete`  
`storagetransfer.agentpools.get`  
`storagetransfer.agentpools.list`  
`storagetransfer.agentpools.update`  
  
  
## Cloud IAM changes as of 2021-08-13

Service | Change | Description  
---|---|---  
Artifact Registry  |  Now GA  |  The role `roles/artifactregistry.admin` (Artifact Registry Administrator) is now GA.  
Artifact Registry  |  Now GA  |  The role `roles/artifactregistry.reader` (Artifact Registry Reader) is now GA.  
Artifact Registry  |  Now GA  |  The role `roles/artifactregistry.repoAdmin` (Artifact Registry Repository Administrator) is now GA.  
Artifact Registry  |  Now GA  |  The role `roles/artifactregistry.writer` (Artifact Registry Writer) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.integrationsEditor` (Cloud Build Integrations Editor) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.integrationsOwner` (Cloud Build Integrations Owner) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.integrationsViewer` (Cloud Build Integrations Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.update`  
  
Network Connectivity Center  |  Now GA  |  The role `roles/networkconnectivity.hubAdmin` (Hub & Spoke Admin) is now GA.  
Network Connectivity Center  |  Now GA  |  The role `roles/networkconnectivity.hubViewer` (Hub & Spoke Viewer) is now GA.  
Network Connectivity Center  |  Now GA  |  The role `roles/networkconnectivity.spokeAdmin` (Spoke Admin) is now GA.  
Speech-to-Text  |  Now GA  |  The role `roles/speech.admin` (Cloud Speech Administrator) is now GA.  
Speech-to-Text  |  Now GA  |  The role `roles/speech.client` (Cloud Speech Client) is now GA.  
Speech-to-Text  |  Now GA  |  The role `roles/speech.editor` (Cloud Speech Editor) is now GA.  
Artifact Registry  |  Now GA  |  `artifactregistry.aptartifacts.create`  
`artifactregistry.files.get`  
`artifactregistry.files.list`  
`artifactregistry.packages.delete`  
`artifactregistry.packages.get`  
`artifactregistry.packages.list`  
`artifactregistry.repositories.create`  
`artifactregistry.repositories.delete`  
`artifactregistry.repositories.deleteArtifacts`  
`artifactregistry.repositories.downloadArtifacts`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.getIamPolicy`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.setIamPolicy`  
`artifactregistry.repositories.update`  
`artifactregistry.repositories.uploadArtifacts`  
`artifactregistry.tags.create`  
`artifactregistry.tags.delete`  
`artifactregistry.tags.get`  
`artifactregistry.tags.list`  
`artifactregistry.tags.update`  
`artifactregistry.versions.delete`  
`artifactregistry.versions.get`  
`artifactregistry.versions.list`  
`artifactregistry.yumartifacts.create`  
  
Network Connectivity Center  |  Now GA  |  `networkconnectivity.hubs.create`  
`networkconnectivity.hubs.delete`  
`networkconnectivity.hubs.get`  
`networkconnectivity.hubs.getIamPolicy`  
`networkconnectivity.hubs.list`  
`networkconnectivity.hubs.setIamPolicy`  
`networkconnectivity.hubs.update`  
`networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
`networkconnectivity.spokes.create`  
`networkconnectivity.spokes.delete`  
`networkconnectivity.spokes.get`  
`networkconnectivity.spokes.getIamPolicy`  
`networkconnectivity.spokes.list`  
`networkconnectivity.spokes.setIamPolicy`  
`networkconnectivity.spokes.update`  
  
Network Services  |  Added  |  `networkservices.endpointPolicies.create`  
`networkservices.endpointPolicies.delete`  
`networkservices.endpointPolicies.get`  
`networkservices.endpointPolicies.getIamPolicy`  
`networkservices.endpointPolicies.list`  
`networkservices.endpointPolicies.setIamPolicy`  
`networkservices.endpointPolicies.update`  
`networkservices.endpointPolicies.use`  
  
Notebooks  |  Added  |  `notebooks.instances.getHealth`  
  
Notebooks  |  Now GA  |  `notebooks.instances.getHealth`  
  
Speech-to-Text  |  Added  |  `speech.adaptations.execute`  
`speech.customClasses.create`  
`speech.customClasses.delete`  
`speech.customClasses.get`  
`speech.customClasses.list`  
`speech.customClasses.update`  
`speech.phraseSets.create`  
`speech.phraseSets.delete`  
`speech.phraseSets.get`  
`speech.phraseSets.list`  
`speech.phraseSets.update`  
  
Speech-to-Text  |  Supported In Custom Roles  |  `speech.adaptations.execute`  
`speech.customClasses.create`  
`speech.customClasses.delete`  
`speech.customClasses.get`  
`speech.customClasses.list`  
`speech.customClasses.update`  
`speech.phraseSets.create`  
`speech.phraseSets.delete`  
`speech.phraseSets.get`  
`speech.phraseSets.list`  
`speech.phraseSets.update`  
  
Speech-to-Text  |  Now GA  |  `speech.adaptations.execute`  
`speech.customClasses.create`  
`speech.customClasses.delete`  
`speech.customClasses.get`  
`speech.customClasses.list`  
`speech.customClasses.update`  
`speech.phraseSets.create`  
`speech.phraseSets.delete`  
`speech.phraseSets.get`  
`speech.phraseSets.list`  
`speech.phraseSets.update`  
  
  
## Cloud IAM changes as of 2021-08-06

Service | Change | Description  
---|---|---  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.customCodeServiceAgent` (Vertex AI Custom Code Service Agent): `bigquery.readsessions.getData`  
  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.serviceAgent` (Vertex AI Service Agent): `aiplatform.annotationSpecs.create`  
`aiplatform.annotationSpecs.delete`  
`aiplatform.annotationSpecs.get`  
`aiplatform.annotationSpecs.list`  
`aiplatform.annotationSpecs.update`  
`aiplatform.annotations.create`  
`aiplatform.annotations.delete`  
`aiplatform.annotations.get`  
`aiplatform.annotations.list`  
`aiplatform.annotations.update`  
`aiplatform.batchPredictionJobs.cancel`  
`aiplatform.batchPredictionJobs.delete`  
`aiplatform.customJobs.delete`  
`aiplatform.dataItems.create`  
`aiplatform.dataItems.delete`  
`aiplatform.dataItems.get`  
`aiplatform.dataItems.list`  
`aiplatform.dataItems.update`  
`aiplatform.dataLabelingJobs.cancel`  
`aiplatform.dataLabelingJobs.create`  
`aiplatform.dataLabelingJobs.delete`  
`aiplatform.dataLabelingJobs.get`  
`aiplatform.dataLabelingJobs.list`  
`aiplatform.datasets.delete`  
`aiplatform.datasets.export`  
`aiplatform.datasets.list`  
`aiplatform.edgeDeploymentJobs.create`  
`aiplatform.edgeDeploymentJobs.delete`  
`aiplatform.edgeDeploymentJobs.get`  
`aiplatform.edgeDeploymentJobs.list`  
`aiplatform.edgeDeviceDebugInfo.get`  
`aiplatform.edgeDevices.create`  
`aiplatform.edgeDevices.delete`  
`aiplatform.edgeDevices.get`  
`aiplatform.edgeDevices.list`  
`aiplatform.edgeDevices.update`  
`aiplatform.endpoints.create`  
`aiplatform.endpoints.delete`  
`aiplatform.endpoints.deploy`  
`aiplatform.endpoints.get`  
`aiplatform.endpoints.list`  
`aiplatform.endpoints.undeploy`  
`aiplatform.endpoints.update`  
`aiplatform.entityTypes.create`  
`aiplatform.entityTypes.delete`  
`aiplatform.entityTypes.importFeatureValues`  
`aiplatform.entityTypes.list`  
`aiplatform.entityTypes.readFeatureValues`  
`aiplatform.entityTypes.streamingReadFeatureValues`  
`aiplatform.entityTypes.update`  
`aiplatform.entityTypes.writeFeatureValues`  
`aiplatform.features.create`  
`aiplatform.features.delete`  
`aiplatform.features.get`  
`aiplatform.features.list`  
`aiplatform.features.update`  
`aiplatform.featurestores.batchReadFeatureValues`  
`aiplatform.featurestores.create`  
`aiplatform.featurestores.delete`  
`aiplatform.featurestores.importFeatures`  
`aiplatform.featurestores.list`  
`aiplatform.featurestores.readFeatures`  
`aiplatform.featurestores.update`  
`aiplatform.featurestores.writeFeatures`  
`aiplatform.humanInTheLoops.create`  
`aiplatform.humanInTheLoops.delete`  
`aiplatform.humanInTheLoops.get`  
`aiplatform.humanInTheLoops.list`  
`aiplatform.humanInTheLoops.send`  
`aiplatform.humanInTheLoops.update`  
`aiplatform.hyperparameterTuningJobs.cancel`  
`aiplatform.hyperparameterTuningJobs.create`  
`aiplatform.hyperparameterTuningJobs.delete`  
`aiplatform.hyperparameterTuningJobs.get`  
`aiplatform.hyperparameterTuningJobs.list`  
`aiplatform.indexEndpoints.create`  
`aiplatform.indexEndpoints.delete`  
`aiplatform.indexEndpoints.deploy`  
`aiplatform.indexEndpoints.get`  
`aiplatform.indexEndpoints.list`  
`aiplatform.indexEndpoints.undeploy`  
`aiplatform.indexEndpoints.update`  
`aiplatform.indexes.create`  
`aiplatform.indexes.delete`  
`aiplatform.indexes.get`  
`aiplatform.indexes.list`  
`aiplatform.indexes.update`  
`aiplatform.locations.get`  
`aiplatform.locations.list`  
`aiplatform.metadataSchemas.delete`  
`aiplatform.modelDeploymentMonitoringJobs.delete`  
`aiplatform.modelDeploymentMonitoringJobs.get`  
`aiplatform.modelDeploymentMonitoringJobs.list`  
`aiplatform.modelDeploymentMonitoringJobs.pause`  
`aiplatform.modelDeploymentMonitoringJobs.resume`  
`aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`  
`aiplatform.modelEvaluationSlices.get`  
`aiplatform.modelEvaluationSlices.list`  
`aiplatform.modelEvaluations.exportEvaluatedDataItems`  
`aiplatform.modelEvaluations.get`  
`aiplatform.modelEvaluations.list`  
`aiplatform.models.delete`  
`aiplatform.models.export`  
`aiplatform.models.get`  
`aiplatform.models.list`  
`aiplatform.models.update`  
`aiplatform.models.upload`  
`aiplatform.nasJobs.cancel`  
`aiplatform.nasJobs.create`  
`aiplatform.nasJobs.delete`  
`aiplatform.nasJobs.get`  
`aiplatform.nasJobs.list`  
`aiplatform.operations.list`  
`aiplatform.pipelineJobs.cancel`  
`aiplatform.pipelineJobs.create`  
`aiplatform.pipelineJobs.delete`  
`aiplatform.pipelineJobs.get`  
`aiplatform.pipelineJobs.list`  
`aiplatform.specialistPools.create`  
`aiplatform.specialistPools.delete`  
`aiplatform.specialistPools.get`  
`aiplatform.specialistPools.list`  
`aiplatform.specialistPools.update`  
`aiplatform.studies.create`  
`aiplatform.studies.delete`  
`aiplatform.studies.get`  
`aiplatform.studies.list`  
`aiplatform.studies.update`  
`aiplatform.tensorboardExperiments.create`  
`aiplatform.tensorboardExperiments.delete`  
`aiplatform.tensorboardExperiments.get`  
`aiplatform.tensorboardExperiments.list`  
`aiplatform.tensorboardExperiments.update`  
`aiplatform.tensorboardExperiments.write`  
`aiplatform.tensorboardRuns.create`  
`aiplatform.tensorboardRuns.delete`  
`aiplatform.tensorboardRuns.get`  
`aiplatform.tensorboardRuns.list`  
`aiplatform.tensorboardRuns.update`  
`aiplatform.tensorboardRuns.write`  
`aiplatform.tensorboardTimeSeries.create`  
`aiplatform.tensorboardTimeSeries.delete`  
`aiplatform.tensorboardTimeSeries.get`  
`aiplatform.tensorboardTimeSeries.list`  
`aiplatform.tensorboardTimeSeries.read`  
`aiplatform.tensorboardTimeSeries.update`  
`aiplatform.tensorboards.create`  
`aiplatform.tensorboards.delete`  
`aiplatform.tensorboards.get`  
`aiplatform.tensorboards.list`  
`aiplatform.tensorboards.update`  
`aiplatform.trainingPipelines.cancel`  
`aiplatform.trainingPipelines.create`  
`aiplatform.trainingPipelines.delete`  
`aiplatform.trainingPipelines.get`  
`aiplatform.trainingPipelines.list`  
`aiplatform.trials.create`  
`aiplatform.trials.delete`  
`aiplatform.trials.get`  
`aiplatform.trials.list`  
`aiplatform.trials.update`  
  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.entityTypeAdmin` (Dialogflow Entity Type Admin) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.environmentEditor` (Dialogflow Environment editor) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.flowEditor` (Dialogflow Flow editor) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.intentAdmin` (Dialogflow Intent Admin) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.testCaseAdmin` (Dialogflow Test Case Admin) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.webhookAdmin` (Dialogflow Webhook Admin) is now GA.  
Cloud Integrations  |  Role Updated  |  The following permissions have been added to the role `roles/integrations.apigeeIntegrationEditorRole` (Apigee Integration Editor): `integrations.apigeeExecutions.list`  
`integrations.apigeeIntegrationVers.deploy`  
`integrations.apigeeIntegrations.invoke`  
  
Network Connectivity Center  |  Role Updated  |  The following permissions have been added to the role `roles/networkconnectivity.spokeAdmin` (Spoke Admin): `networkconnectivity.hubs.get`  
`networkconnectivity.hubs.getIamPolicy`  
`networkconnectivity.hubs.list`  
  
Transcoder API  |  Now GA  |  The role `roles/transcoder.admin` (Transcoder Admin) is now GA.  
Transcoder API  |  Now GA  |  The role `roles/transcoder.viewer` (Transcoder Viewer) is now GA.  
Compute Engine  |  Added  |  `compute.backendServices.getIamPolicy`  
`compute.backendServices.setIamPolicy`  
`compute.regionBackendServices.getIamPolicy`  
`compute.regionBackendServices.setIamPolicy`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.backendServices.getIamPolicy`  
`compute.backendServices.setIamPolicy`  
  
Cyber Insurance Hub  |  Added  |  `riskmanager.operations.delete`  
`riskmanager.operations.get`  
`riskmanager.operations.list`  
`riskmanager.policies.get`  
`riskmanager.policies.list`  
`riskmanager.reports.create`  
`riskmanager.reports.delete`  
`riskmanager.reports.get`  
`riskmanager.reports.list`  
`riskmanager.reports.review`  
`riskmanager.reports.share`  
`riskmanager.serviceAccount.create`  
`riskmanager.settings.get`  
`riskmanager.settings.update`  
  
Cyber Insurance Hub  |  Supported In Custom Roles  |  `riskmanager.settings.get`  
`riskmanager.settings.update`  
  
Transcoder API  |  Now GA  |  `transcoder.jobTemplates.create`  
`transcoder.jobTemplates.delete`  
`transcoder.jobTemplates.get`  
`transcoder.jobTemplates.list`  
`transcoder.jobs.create`  
`transcoder.jobs.delete`  
`transcoder.jobs.get`  
`transcoder.jobs.list`  
  
  
## Cloud IAM changes as of 2021-07-30

Service | Change | Description  
---|---|---  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.serviceAgent` (Vertex AI Service Agent): `aiplatform.modelDeploymentMonitoringJobs.create`  
`aiplatform.modelDeploymentMonitoringJobs.update`  
  
API Gateway  |  Role Updated  |  The following permissions have been added to the role `roles/apigateway.admin` (ApiGateway Admin): `monitoring.metricDescriptors.list`  
`monitoring.monitoredResourceDescriptors.get`  
`monitoring.timeSeries.list`  
`servicemanagement.services.get`  
`serviceusage.services.list`  
  
API Gateway  |  Role Updated  |  The following permissions have been added to the role `roles/apigateway.viewer` (ApiGateway Viewer): `monitoring.metricDescriptors.list`  
`monitoring.monitoredResourceDescriptors.get`  
`monitoring.timeSeries.list`  
`servicemanagement.services.get`  
`serviceusage.services.list`  
  
Bare Metal Solution  |  Role Updated  |  The following permissions have been added to the role `roles/baremetalsolution.admin` (Admin): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Bare Metal Solution  |  Role Updated  |  The following permissions have been added to the role `roles/baremetalsolution.editor` (Editor): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Bare Metal Solution  |  Role Updated  |  The following permissions have been added to the role `roles/baremetalsolution.viewer` (Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.builds.approver` (Cloud Build Approver) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.cryptoOperator` (Cloud KMS Crypto Operator) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.verifier` (Cloud KMS CryptoKey Verifier) is now GA.  
Customer Experience Insights  |  Role Updated  |  The following permissions have been added to the role `roles/contactcenterinsights.serviceAgent` (Contact Center AI Insights Service Agent): `datalabeling.dataitems.get`  
`datalabeling.dataitems.list`  
`datalabeling.datasets.create`  
`datalabeling.datasets.delete`  
`datalabeling.datasets.export`  
`datalabeling.datasets.get`  
`datalabeling.datasets.import`  
`datalabeling.operations.get`  
`datalabeling.operations.list`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.worker` (Dataflow Worker): `autoscaling.sites.readRecommendations`  
`autoscaling.sites.writeMetrics`  
`autoscaling.sites.writeState`  
  
Managed Service for Apache Spark  |  Role Updated  |  The following permissions have been added to the role `roles/dataproc.hubAgent` (Dataproc Hub Agent): `logging.operations.get`  
`logging.operations.list`  
  
Managed Service for Apache Spark  |  Role Updated  |  The following permissions have been added to the role `roles/dataproc.worker` (Dataproc Worker): `storage.multipartUploads.list`  
  
Enterprise Knowledge Graph  |  Role Updated  |  The following permissions have been added to the role `roles/enterpriseknowledgegraph.serviceAgent` (Enterprise Knowledge Graph Service Agent): `bigquery.jobs.create`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Integrations  |  Now GA  |  The role `roles/integrations.apigeeIntegrationAdminRole` (Apigee Integration Admin) is now GA.  
Cloud Integrations  |  Now GA  |  The role `roles/integrations.apigeeIntegrationDeployerRole` (Apigee Integration Deployer) is now GA.  
Cloud Integrations  |  Now GA  |  The role `roles/integrations.apigeeIntegrationEditorRole` (Apigee Integration Editor) is now GA.  
Cloud Integrations  |  Now GA  |  The role `roles/integrations.apigeeIntegrationInvokerRole` (Apigee Integration Invoker) is now GA.  
Cloud Integrations  |  Now GA  |  The role `roles/integrations.apigeeIntegrationsViewer` (Apigee Integration Viewer) is now GA.  
Cloud Integrations  |  Now GA  |  The role `roles/integrations.apigeeSuspensionResolver` (Apigee Integration Approver) is now GA.  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.viewer` (Logs Viewer): `logging.operations.get`  
`logging.operations.list`  
  
Media Asset  |  Role Updated  |  The following permissions have been added to the role `roles/mediaasset.serviceAgent` (Media Asset Service Agent): `transcoder.jobs.create`  
`transcoder.jobs.delete`  
`transcoder.jobs.get`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.thirdPartyObjects.delete`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.controlServiceAgent` (Security Center Control Service Agent): `binaryauthorization.policy.get`  
`logging.operations.get`  
`logging.operations.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.securityHealthAnalyticsServiceAgent` (Security Health Analytics Service Agent): `binaryauthorization.policy.get`  
`logging.operations.get`  
`logging.operations.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.serviceAgent` (Security Center Service Agent): `binaryauthorization.policy.get`  
`logging.operations.get`  
`logging.operations.list`  
  
Cloud Storage  |  Role Updated  |  The following permissions have been added to the role `roles/storage.legacyBucketWriter` (Storage Legacy Bucket Writer): `storage.multipartUploads.list`  
  
Artifact Registry  |  Added  |  `artifactregistry.aptartifacts.create`  
`artifactregistry.yumartifacts.create`  
  
Cloud Build  |  Added  |  `cloudbuild.builds.approve`  
  
Cloud Build  |  Supported In Custom Roles  |  `cloudbuild.builds.approve`  
  
Cloud Build  |  Now GA  |  `cloudbuild.builds.approve`  
  
Cloud Key Management Service  |  Added  |  `cloudkms.cryptoKeyVersions.useToVerify`  
`cloudkms.keyRings.createTagBinding`  
`cloudkms.keyRings.deleteTagBinding`  
`cloudkms.keyRings.listTagBindings`  
`cloudkms.locations.generateRandomBytes`  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `cloudkms.cryptoKeyVersions.useToVerify`  
`cloudkms.locations.generateRandomBytes`  
  
Cloud Key Management Service  |  Now GA  |  `cloudkms.cryptoKeyVersions.useToVerify`  
`cloudkms.keyRings.createTagBinding`  
`cloudkms.keyRings.deleteTagBinding`  
`cloudkms.keyRings.listTagBindings`  
`cloudkms.locations.generateRandomBytes`  
  
Data Pipelines  |  Added  |  `datapipelines.pipelines.create`  
`datapipelines.pipelines.delete`  
`datapipelines.pipelines.get`  
`datapipelines.pipelines.list`  
`datapipelines.pipelines.run`  
`datapipelines.pipelines.stop`  
`datapipelines.pipelines.update`  
  
Firebase App Check  |  Added  |  `firebaseappcheck.appAttestConfig.get`  
`firebaseappcheck.appAttestConfig.update`  
`firebaseappcheck.safetyNetConfig.get`  
`firebaseappcheck.safetyNetConfig.update`  
  
Firebase App Check  |  Supported In Custom Roles  |  `firebaseappcheck.appAttestConfig.get`  
`firebaseappcheck.appAttestConfig.update`  
`firebaseappcheck.safetyNetConfig.get`  
`firebaseappcheck.safetyNetConfig.update`  
  
Cloud Integrations  |  Now GA  |  `integrations.apigeeAuthConfigs.create`  
`integrations.apigeeAuthConfigs.delete`  
`integrations.apigeeAuthConfigs.get`  
`integrations.apigeeAuthConfigs.list`  
`integrations.apigeeAuthConfigs.update`  
`integrations.apigeeCertificates.get`  
`integrations.apigeeExecutions.list`  
`integrations.apigeeIntegrationVers.create`  
`integrations.apigeeIntegrationVers.deploy`  
`integrations.apigeeIntegrationVers.get`  
`integrations.apigeeIntegrationVers.list`  
`integrations.apigeeIntegrationVers.update`  
`integrations.apigeeIntegrations.invoke`  
`integrations.apigeeIntegrations.list`  
`integrations.apigeeSfdcChannels.create`  
`integrations.apigeeSfdcChannels.delete`  
`integrations.apigeeSfdcChannels.get`  
`integrations.apigeeSfdcChannels.list`  
`integrations.apigeeSfdcChannels.update`  
`integrations.apigeeSfdcInstances.create`  
`integrations.apigeeSfdcInstances.delete`  
`integrations.apigeeSfdcInstances.get`  
`integrations.apigeeSfdcInstances.list`  
`integrations.apigeeSfdcInstances.update`  
`integrations.apigeeSuspensions.list`  
`integrations.apigeeSuspensions.resolve`  
  
Managed Service for Microsoft Active Directory  |  Added  |  `managedidentities.peerings.create`  
`managedidentities.peerings.delete`  
`managedidentities.peerings.get`  
`managedidentities.peerings.getIamPolicy`  
`managedidentities.peerings.list`  
`managedidentities.peerings.setIamPolicy`  
`managedidentities.peerings.update`  
  
Managed Service for Microsoft Active Directory  |  Supported In Custom Roles  |  `managedidentities.peerings.create`  
`managedidentities.peerings.delete`  
`managedidentities.peerings.get`  
`managedidentities.peerings.getIamPolicy`  
`managedidentities.peerings.list`  
`managedidentities.peerings.setIamPolicy`  
`managedidentities.peerings.update`  
  
Recommender  |  Added  |  `recommender.resources.export`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.resources.export`  
  
  
## Cloud IAM changes as of 2021-07-16

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.customResourceDefinitions.update`  
  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.workerPoolEditor` (Cloud Build WorkerPool Editor) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.workerPoolOwner` (Cloud Build WorkerPool Owner) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.workerPoolUser` (Cloud Build WorkerPool User) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.workerPoolViewer` (Cloud Build WorkerPool Viewer) is now GA.  
Cloud TPU  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtpu.serviceAgent` (Cloud TPU V2 API Service Agent): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Compliance Scanning  |  Now GA  |  The role `roles/compliancescanning.ServiceAgent` (Compliance Scanning Service Agent) is now GA.  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkUser` (Compute Network User): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkViewer` (Compute Network Viewer): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgFirewallPolicyAdmin` (Compute Organization Firewall Policy Admin): `compute.regionOperations.get`  
`compute.regionOperations.getIamPolicy`  
`compute.regionOperations.list`  
`compute.regionOperations.setIamPolicy`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgFirewallPolicyUser` (Compute Organization Firewall Policy User): `compute.regionOperations.get`  
`compute.regionOperations.getIamPolicy`  
`compute.regionOperations.list`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Cloud Data Fusion  |  Role Updated  |  The following permissions have been added to the role `roles/datafusion.serviceAgent` (Cloud Data Fusion API Service Agent): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Data Pipelines  |  Now GA  |  The role `roles/datapipelines.serviceAgent` (Datapipelines Service Agent) is now GA.  
GKE Multi-Cloud  |  Role Updated  |  The following permissions have been added to the role `roles/gkemulticloud.serviceAgent` (Anthos Multi-Cloud Service Agent): `gkemulticloud.awsClusters.delete`  
`gkemulticloud.awsNodePools.delete`  
`gkemulticloud.azureClients.delete`  
`gkemulticloud.azureClusters.delete`  
`gkemulticloud.azureNodePools.delete`  
  
Gemini Enterprise Agent Platform  |  Added  |  `aiplatform.artifacts.delete`  
`aiplatform.entityTypes.writeFeatureValues`  
`aiplatform.executions.delete`  
`aiplatform.metadataSchemas.delete`  
`aiplatform.tensorboardExperiments.write`  
  
Cloud Build  |  Added  |  `cloudbuild.workerpools.create`  
`cloudbuild.workerpools.delete`  
`cloudbuild.workerpools.get`  
`cloudbuild.workerpools.list`  
`cloudbuild.workerpools.update`  
`cloudbuild.workerpools.use`  
  
Cloud Build  |  Supported In Custom Roles  |  `cloudbuild.workerpools.create`  
`cloudbuild.workerpools.delete`  
`cloudbuild.workerpools.get`  
`cloudbuild.workerpools.list`  
`cloudbuild.workerpools.update`  
`cloudbuild.workerpools.use`  
  
Cloud Build  |  Now GA  |  `cloudbuild.workerpools.create`  
`cloudbuild.workerpools.delete`  
`cloudbuild.workerpools.get`  
`cloudbuild.workerpools.list`  
`cloudbuild.workerpools.update`  
`cloudbuild.workerpools.use`  
  
GKE Multi-Cloud  |  Added  |  `gkemulticloud.awsNodePools.update`  
`gkemulticloud.azureNodePools.update`  
  
Cloud Monitoring  |  Added  |  `monitoring.metricsScopes.link`  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `monitoring.metricsScopes.link`  
  
Policy Analyzer  |  Added  |  `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query`  
`policyanalyzer.serviceAccountLastAuthenticationActivities.query`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.operations.get`  
`pubsublite.operations.list`  
  
Pub/Sub Lite  |  Now GA  |  `pubsublite.operations.get`  
`pubsublite.operations.list`  
  
  
## Cloud IAM changes as of 2021-07-02

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.mutatingWebhookConfigurations.create`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.mutatingWebhookConfigurations.update`  
`container.validatingWebhookConfigurations.create`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.validatingWebhookConfigurations.update`  
  
Managed Service for Apache Airflow  |  Now GA  |  The role `roles/composer.ServiceAgentV2Ext` (Cloud Composer v2 API Service Agent Extension) is now GA.  
Visual Inspection AI  |  Now GA  |  The role `roles/visualinspection.editor` (Visual Inspection AI Solution Editor) is now GA.  
Visual Inspection AI  |  Now GA  |  The role `roles/visualinspection.usageMetricsReporter` (Visual Inspection AI Usage Metrics Reporter) is now GA.  
Visual Inspection AI  |  Now GA  |  The role `roles/visualinspection.viewer` (Visual Inspection AI Viewer) is now GA.  
Compute Engine  |  Added  |  `compute.instances.sendDiagnosticInterrupt`  
  
Compute Engine  |  Now GA  |  `compute.instances.sendDiagnosticInterrupt`  
  
Visual Inspection AI  |  Added  |  `visualinspection.annotationSets.create`  
`visualinspection.annotationSets.delete`  
`visualinspection.annotationSets.get`  
`visualinspection.annotationSets.list`  
`visualinspection.annotationSets.update`  
`visualinspection.annotationSpecs.create`  
`visualinspection.annotationSpecs.delete`  
`visualinspection.annotationSpecs.get`  
`visualinspection.annotationSpecs.list`  
`visualinspection.annotations.create`  
`visualinspection.annotations.delete`  
`visualinspection.annotations.get`  
`visualinspection.annotations.list`  
`visualinspection.annotations.update`  
`visualinspection.datasets.create`  
`visualinspection.datasets.delete`  
`visualinspection.datasets.export`  
`visualinspection.datasets.get`  
`visualinspection.datasets.import`  
`visualinspection.datasets.list`  
`visualinspection.datasets.update`  
`visualinspection.images.delete`  
`visualinspection.images.get`  
`visualinspection.images.list`  
`visualinspection.images.update`  
`visualinspection.locations.get`  
`visualinspection.locations.list`  
`visualinspection.locations.reportUsageMetrics`  
`visualinspection.modelEvaluations.get`  
`visualinspection.modelEvaluations.list`  
`visualinspection.models.create`  
`visualinspection.models.delete`  
`visualinspection.models.get`  
`visualinspection.models.list`  
`visualinspection.models.update`  
`visualinspection.models.writePrediction`  
`visualinspection.modules.create`  
`visualinspection.modules.delete`  
`visualinspection.modules.get`  
`visualinspection.modules.list`  
`visualinspection.modules.update`  
`visualinspection.operations.get`  
`visualinspection.operations.list`  
`visualinspection.solutionArtifacts.create`  
`visualinspection.solutionArtifacts.delete`  
`visualinspection.solutionArtifacts.get`  
`visualinspection.solutionArtifacts.list`  
`visualinspection.solutionArtifacts.predict`  
`visualinspection.solutionArtifacts.update`  
`visualinspection.solutions.create`  
`visualinspection.solutions.delete`  
`visualinspection.solutions.get`  
`visualinspection.solutions.list`  
  
Visual Inspection AI  |  Supported In Custom Roles  |  `visualinspection.annotationSets.create`  
`visualinspection.annotationSets.delete`  
`visualinspection.annotationSets.get`  
`visualinspection.annotationSets.list`  
`visualinspection.annotationSets.update`  
`visualinspection.annotationSpecs.create`  
`visualinspection.annotationSpecs.delete`  
`visualinspection.annotationSpecs.get`  
`visualinspection.annotationSpecs.list`  
`visualinspection.annotations.create`  
`visualinspection.annotations.delete`  
`visualinspection.annotations.get`  
`visualinspection.annotations.list`  
`visualinspection.annotations.update`  
`visualinspection.datasets.create`  
`visualinspection.datasets.delete`  
`visualinspection.datasets.export`  
`visualinspection.datasets.get`  
`visualinspection.datasets.import`  
`visualinspection.datasets.list`  
`visualinspection.datasets.update`  
`visualinspection.images.delete`  
`visualinspection.images.get`  
`visualinspection.images.list`  
`visualinspection.images.update`  
`visualinspection.locations.get`  
`visualinspection.locations.list`  
`visualinspection.locations.reportUsageMetrics`  
`visualinspection.modelEvaluations.get`  
`visualinspection.modelEvaluations.list`  
`visualinspection.models.create`  
`visualinspection.models.delete`  
`visualinspection.models.get`  
`visualinspection.models.list`  
`visualinspection.models.update`  
`visualinspection.models.writePrediction`  
`visualinspection.modules.create`  
`visualinspection.modules.delete`  
`visualinspection.modules.get`  
`visualinspection.modules.list`  
`visualinspection.modules.update`  
`visualinspection.operations.get`  
`visualinspection.operations.list`  
`visualinspection.solutionArtifacts.create`  
`visualinspection.solutionArtifacts.delete`  
`visualinspection.solutionArtifacts.get`  
`visualinspection.solutionArtifacts.list`  
`visualinspection.solutionArtifacts.predict`  
`visualinspection.solutionArtifacts.update`  
`visualinspection.solutions.create`  
`visualinspection.solutions.delete`  
`visualinspection.solutions.get`  
`visualinspection.solutions.list`  
  
Visual Inspection AI  |  Now GA  |  `visualinspection.annotationSets.create`  
`visualinspection.annotationSets.delete`  
`visualinspection.annotationSets.get`  
`visualinspection.annotationSets.list`  
`visualinspection.annotationSets.update`  
`visualinspection.annotationSpecs.create`  
`visualinspection.annotationSpecs.delete`  
`visualinspection.annotationSpecs.get`  
`visualinspection.annotationSpecs.list`  
`visualinspection.annotations.create`  
`visualinspection.annotations.delete`  
`visualinspection.annotations.get`  
`visualinspection.annotations.list`  
`visualinspection.annotations.update`  
`visualinspection.datasets.create`  
`visualinspection.datasets.delete`  
`visualinspection.datasets.export`  
`visualinspection.datasets.get`  
`visualinspection.datasets.import`  
`visualinspection.datasets.list`  
`visualinspection.datasets.update`  
`visualinspection.images.delete`  
`visualinspection.images.get`  
`visualinspection.images.list`  
`visualinspection.images.update`  
`visualinspection.locations.get`  
`visualinspection.locations.list`  
`visualinspection.locations.reportUsageMetrics`  
`visualinspection.modelEvaluations.get`  
`visualinspection.modelEvaluations.list`  
`visualinspection.models.create`  
`visualinspection.models.delete`  
`visualinspection.models.get`  
`visualinspection.models.list`  
`visualinspection.models.update`  
`visualinspection.models.writePrediction`  
`visualinspection.modules.create`  
`visualinspection.modules.delete`  
`visualinspection.modules.get`  
`visualinspection.modules.list`  
`visualinspection.modules.update`  
`visualinspection.operations.get`  
`visualinspection.operations.list`  
`visualinspection.solutionArtifacts.create`  
`visualinspection.solutionArtifacts.delete`  
`visualinspection.solutionArtifacts.get`  
`visualinspection.solutionArtifacts.list`  
`visualinspection.solutionArtifacts.predict`  
`visualinspection.solutionArtifacts.update`  
`visualinspection.solutions.create`  
`visualinspection.solutions.delete`  
`visualinspection.solutions.get`  
`visualinspection.solutions.list`  
  
  
## Cloud IAM changes as of 2021-06-25

Service | Change | Description  
---|---|---  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.admin` (Admin) is now GA.  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.editor` (Editor) is now GA.  
Bare Metal Solution  |  Now GA  |  The role `roles/baremetalsolution.viewer` (Viewer) is now GA.  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.admin` (Cloud Functions Admin): `recommender.locations.get`  
`recommender.locations.list`  
  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.developer` (Cloud Functions Developer): `recommender.locations.get`  
`recommender.locations.list`  
  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.serviceAgent` (Cloud Functions Service Agent): `recommender.locations.get`  
`recommender.locations.list`  
  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.viewer` (Cloud Functions Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.viewer` (Kubernetes Engine Viewer): `container.deployments.getScale`  
`container.statefulSets.getScale`  
`container.storageStates.getStatus`  
`container.storageVersionMigrations.getStatus`  
`container.volumeSnapshotContents.getStatus`  
  
Container Threat Detection  |  Role Updated  |  The following permissions have been added to the role `roles/containerthreatdetection.serviceAgent` (Container Threat Detection Service Agent): `container.deployments.getScale`  
`container.statefulSets.getScale`  
`container.storageStates.getStatus`  
`container.storageVersionMigrations.getStatus`  
`container.volumeSnapshotContents.getStatus`  
  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.admin` (Data Catalog Admin): `bigquery.connections.updateTag`  
  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.tagEditor` (Data Catalog Tag Editor): `bigquery.connections.updateTag`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.aamAdmin` (AAM Admin): `dialogflow.agents.searchResources`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.aamConversationalArchitect` (AAM Conversational Architect): `dialogflow.agents.searchResources`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.aamDialogDesigner` (AAM Dialog Designer): `dialogflow.agents.searchResources`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.aamLeadDialogDesigner` (AAM Lead Dialog Designer): `dialogflow.agents.searchResources`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.aamViewer` (AAM Viewer): `dialogflow.agents.searchResources`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.reader` (Dialogflow API Reader): `dialogflow.agents.searchResources`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.serviceAgent` (Dialogflow Service Agent): `dialogflow.agents.searchResources`  
  
Eventarc  |  Role Updated  |  The following permissions have been added to the role `roles/eventarc.serviceAgent` (Eventarc Service Agent): `storage.buckets.get`  
`storage.buckets.update`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.admin` (Firebase Admin): `recommender.locations.get`  
`recommender.locations.list`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.developAdmin` (Firebase Develop Admin): `recommender.locations.get`  
`recommender.locations.list`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.developViewer` (Firebase Develop Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.viewer` (Firebase Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
Network Connectivity Center  |  Role Updated  |  The following permissions have been added to the role `roles/networkconnectivity.hubAdmin` (Hub & Spoke Admin): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
  
Network Connectivity Center  |  Role Updated  |  The following permissions have been added to the role `roles/networkconnectivity.hubViewer` (Hub & Spoke Viewer): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
  
Network Connectivity Center  |  Role Updated  |  The following permissions have been added to the role `roles/networkconnectivity.spokeAdmin` (Spoke Admin): `networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
  
Cloud Run  |  Role Updated  |  The following permissions have been added to the role `roles/run.admin` (Cloud Run Admin): `recommender.locations.get`  
`recommender.locations.list`  
  
Cloud Run  |  Role Updated  |  The following permissions have been added to the role `roles/run.developer` (Cloud Run Developer): `recommender.locations.get`  
`recommender.locations.list`  
  
Cloud Run  |  Role Updated  |  The following permissions have been removed from the role `roles/run.serviceAgent` (Cloud Run Service Agent): `pubsub.subscriptions.create`  
`pubsub.subscriptions.delete`  
`pubsub.subscriptions.get`  
`pubsub.subscriptions.list`  
`pubsub.topics.attachSubscription`  
`pubsub.topics.create`  
`pubsub.topics.delete`  
`pubsub.topics.get`  
`pubsub.topics.list`  
`pubsub.topics.publish`  
  
Cloud Run  |  Role Updated  |  The following permissions have been added to the role `roles/run.viewer` (Cloud Run Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.controlServiceAgent` (Security Center Control Service Agent): `container.deployments.getScale`  
`container.statefulSets.getScale`  
`container.storageStates.getStatus`  
`container.storageVersionMigrations.getStatus`  
`container.volumeSnapshotContents.getStatus`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.serviceAgent` (Security Center Service Agent): `container.deployments.getScale`  
`container.statefulSets.getScale`  
`container.storageStates.getStatus`  
`container.storageVersionMigrations.getStatus`  
`container.volumeSnapshotContents.getStatus`  
  
Apigee  |  Added  |  `apigee.runtimeconfigs.get`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.runtimeconfigs.get`  
  
Apigee  |  Now GA  |  `apigee.runtimeconfigs.get`  
  
BigQuery  |  Added  |  `bigquery.connections.updateTag`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.connections.updateTag`  
  
Dialogflow  |  Added  |  `dialogflow.agents.searchResources`  
  
Dialogflow  |  Now GA  |  `dialogflow.agents.searchResources`  
  
Firebase Cloud Messaging Data  |  Added  |  `fcmdata.deliverydata.list`  
  
Firebase Cloud Messaging Data  |  Supported In Custom Roles  |  `fcmdata.deliverydata.list`  
  
Live Stream  |  Added  |  `livestream.channels.create`  
`livestream.channels.delete`  
`livestream.channels.get`  
`livestream.channels.list`  
`livestream.channels.start`  
`livestream.channels.stop`  
`livestream.channels.update`  
`livestream.events.create`  
`livestream.events.delete`  
`livestream.events.get`  
`livestream.events.list`  
`livestream.inputs.create`  
`livestream.inputs.delete`  
`livestream.inputs.get`  
`livestream.inputs.list`  
`livestream.inputs.update`  
`livestream.locations.get`  
`livestream.locations.list`  
`livestream.operations.cancel`  
`livestream.operations.delete`  
`livestream.operations.get`  
`livestream.operations.list`  
  
Live Stream  |  Supported In Custom Roles  |  `livestream.channels.create`  
`livestream.channels.delete`  
`livestream.channels.get`  
`livestream.channels.list`  
`livestream.channels.start`  
`livestream.channels.stop`  
`livestream.channels.update`  
`livestream.events.create`  
`livestream.events.delete`  
`livestream.events.get`  
`livestream.events.list`  
`livestream.inputs.create`  
`livestream.inputs.delete`  
`livestream.inputs.get`  
`livestream.inputs.list`  
`livestream.inputs.update`  
`livestream.locations.get`  
`livestream.locations.list`  
`livestream.operations.cancel`  
`livestream.operations.delete`  
`livestream.operations.get`  
`livestream.operations.list`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.reservations.attachTopic`  
`pubsublite.reservations.create`  
`pubsublite.reservations.delete`  
`pubsublite.reservations.get`  
`pubsublite.reservations.list`  
`pubsublite.reservations.listTopics`  
`pubsublite.reservations.update`  
  
Pub/Sub Lite  |  Now GA  |  `pubsublite.reservations.attachTopic`  
`pubsublite.reservations.create`  
`pubsublite.reservations.delete`  
`pubsublite.reservations.get`  
`pubsublite.reservations.list`  
`pubsublite.reservations.listTopics`  
`pubsublite.reservations.update`  
  
Cloud Storage  |  Added  |  `storage.buckets.createTagBinding`  
`storage.buckets.deleteTagBinding`  
`storage.buckets.listTagBindings`  
  
Cloud Storage  |  Now GA  |  `storage.buckets.createTagBinding`  
`storage.buckets.deleteTagBinding`  
`storage.buckets.listTagBindings`  
  
  
## Cloud IAM changes as of 2021-06-18

Service | Change | Description  
---|---|---  
Assured Workloads  |  Role Updated  |  The following permissions have been added to the role `roles/assuredworkloads.admin` (Assured Workloads Administrator): `resourcemanager.folders.create`  
`resourcemanager.folders.get`  
`resourcemanager.folders.list`  
  
Assured Workloads  |  Role Updated  |  The following permissions have been added to the role `roles/assuredworkloads.editor` (Assured Workloads Editor): `resourcemanager.folders.create`  
`resourcemanager.folders.get`  
`resourcemanager.folders.list`  
  
Assured Workloads  |  Role Updated  |  The following permissions have been added to the role `roles/assuredworkloads.reader` (Assured Workloads Reader): `resourcemanager.folders.get`  
`resourcemanager.folders.list`  
  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.aamLeadDialogDesigner` (AAM Lead Dialog Designer) is now GA.  
Firestore  |  Now GA  |  The role `roles/firestore.serviceAgent` (Firestore Service Agent) is now GA.  
Apigee  |  Added  |  `apigee.developerbalances.get`  
`apigee.developerbalances.update`  
`apigee.developermonetizationconfigs.get`  
`apigee.developermonetizationconfigs.update`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.developerbalances.get`  
`apigee.developerbalances.update`  
`apigee.developermonetizationconfigs.get`  
`apigee.developermonetizationconfigs.update`  
  
Apigee  |  Now GA  |  `apigee.developerbalances.get`  
`apigee.developerbalances.update`  
`apigee.developermonetizationconfigs.get`  
`apigee.developermonetizationconfigs.update`  
  
Dialogflow  |  Added  |  `dialogflow.changelogs.get`  
`dialogflow.changelogs.list`  
  
Dialogflow  |  Now GA  |  `dialogflow.changelogs.get`  
`dialogflow.changelogs.list`  
  
Cloud DNS  |  Added  |  `dns.networks.bindDNSResponsePolicy`  
`dns.responsePolicies.create`  
`dns.responsePolicies.delete`  
`dns.responsePolicies.get`  
`dns.responsePolicies.list`  
`dns.responsePolicies.update`  
`dns.responsePolicyRules.create`  
`dns.responsePolicyRules.delete`  
`dns.responsePolicyRules.get`  
`dns.responsePolicyRules.list`  
`dns.responsePolicyRules.update`  
  
Cloud DNS  |  Supported In Custom Roles  |  `dns.networks.bindDNSResponsePolicy`  
`dns.responsePolicies.create`  
`dns.responsePolicies.delete`  
`dns.responsePolicies.get`  
`dns.responsePolicies.list`  
`dns.responsePolicies.update`  
`dns.responsePolicyRules.create`  
`dns.responsePolicyRules.delete`  
`dns.responsePolicyRules.get`  
`dns.responsePolicyRules.list`  
`dns.responsePolicyRules.update`  
  
GKE Multi-Cloud  |  Added  |  `gkemulticloud.awsServerConfigs.get`  
`gkemulticloud.azureServerConfigs.get`  
  
Managed Service for Microsoft Active Directory  |  Added  |  `managedidentities.sqlintegrations.get`  
`managedidentities.sqlintegrations.list`  
  
Managed Service for Microsoft Active Directory  |  Supported In Custom Roles  |  `managedidentities.sqlintegrations.get`  
`managedidentities.sqlintegrations.list`  
  
Recommender  |  Added  |  `recommender.iamPolicyLateralMovementInsights.get`  
`recommender.iamPolicyLateralMovementInsights.list`  
`recommender.iamPolicyLateralMovementInsights.update`  
`recommender.resourcemanagerProjectUtilizationInsights.get`  
`recommender.resourcemanagerProjectUtilizationInsights.list`  
`recommender.resourcemanagerProjectUtilizationInsights.update`  
`recommender.resourcemanagerProjectUtilizationRecommendations.get`  
`recommender.resourcemanagerProjectUtilizationRecommendations.list`  
`recommender.resourcemanagerProjectUtilizationRecommendations.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.iamPolicyLateralMovementInsights.get`  
`recommender.iamPolicyLateralMovementInsights.list`  
`recommender.iamPolicyLateralMovementInsights.update`  
  
Recommender  |  Now GA  |  `recommender.iamPolicyLateralMovementInsights.get`  
`recommender.iamPolicyLateralMovementInsights.list`  
`recommender.iamPolicyLateralMovementInsights.update`  
  
  
## Cloud IAM changes as of 2021-06-11

Service | Change | Description  
---|---|---  
BigQuery  |  Now GA  |  The role `roles/bigquery.filteredDataViewer` (BigQuery Filtered Data Viewer) is now GA.  
FleetEngine  |  Now GA  |  The role `roles/fleetengine.serviceAgent` (FleetEngine Service Agent) is now GA.  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.serviceAgent` (AI Platform Notebooks Service Agent): `aiplatform.customJobs.cancel`  
`aiplatform.customJobs.create`  
`aiplatform.customJobs.get`  
`aiplatform.customJobs.list`  
  
BigQuery  |  Added  |  `bigquery.rowAccessPolicies.create`  
`bigquery.rowAccessPolicies.delete`  
`bigquery.rowAccessPolicies.getFilteredData`  
`bigquery.rowAccessPolicies.getIamPolicy`  
`bigquery.rowAccessPolicies.list`  
`bigquery.rowAccessPolicies.setIamPolicy`  
`bigquery.rowAccessPolicies.update`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.rowAccessPolicies.create`  
`bigquery.rowAccessPolicies.delete`  
`bigquery.rowAccessPolicies.getFilteredData`  
`bigquery.rowAccessPolicies.getIamPolicy`  
`bigquery.rowAccessPolicies.list`  
`bigquery.rowAccessPolicies.setIamPolicy`  
`bigquery.rowAccessPolicies.update`  
  
BigQuery  |  Now GA  |  `bigquery.rowAccessPolicies.create`  
`bigquery.rowAccessPolicies.delete`  
`bigquery.rowAccessPolicies.getFilteredData`  
`bigquery.rowAccessPolicies.getIamPolicy`  
`bigquery.rowAccessPolicies.list`  
`bigquery.rowAccessPolicies.setIamPolicy`  
`bigquery.rowAccessPolicies.update`  
  
Cloud Run functions  |  Added  |  `cloudfunctions.locations.get`  
  
Cloud Run functions  |  Now GA  |  `cloudfunctions.locations.get`  
  
Customer Experience Insights  |  Added  |  `contactcenterinsights.analyses.create`  
`contactcenterinsights.analyses.delete`  
`contactcenterinsights.analyses.get`  
`contactcenterinsights.analyses.list`  
`contactcenterinsights.conversations.create`  
`contactcenterinsights.conversations.delete`  
`contactcenterinsights.conversations.get`  
`contactcenterinsights.conversations.list`  
`contactcenterinsights.conversations.update`  
`contactcenterinsights.issueModels.create`  
`contactcenterinsights.issueModels.delete`  
`contactcenterinsights.issueModels.deploy`  
`contactcenterinsights.issueModels.get`  
`contactcenterinsights.issueModels.list`  
`contactcenterinsights.issueModels.undeploy`  
`contactcenterinsights.issueModels.update`  
`contactcenterinsights.issues.get`  
`contactcenterinsights.issues.list`  
`contactcenterinsights.issues.update`  
`contactcenterinsights.operations.get`  
`contactcenterinsights.operations.list`  
`contactcenterinsights.phraseMatchers.create`  
`contactcenterinsights.phraseMatchers.delete`  
`contactcenterinsights.phraseMatchers.get`  
`contactcenterinsights.phraseMatchers.list`  
`contactcenterinsights.phraseMatchers.update`  
`contactcenterinsights.settings.get`  
`contactcenterinsights.settings.update`  
  
Cloud Healthcare API  |  Added  |  `healthcare.fhirStores.configureSearch`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.fhirStores.configureSearch`  
  
Cloud Healthcare API  |  Now GA  |  `healthcare.fhirStores.configureSearch`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.subscriptions.seek`  
  
Pub/Sub Lite  |  Now GA  |  `pubsublite.subscriptions.seek`  
  
  
## Cloud IAM changes as of 2021-06-04

Service | Change | Description  
---|---|---  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.runtimeAgent` (Apigee Runtime Agent): `apigee.organizations.get`  
  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.serviceAgent` (Cloud Functions Service Agent): `artifactregistry.files.get`  
`artifactregistry.files.list`  
`artifactregistry.packages.delete`  
`artifactregistry.packages.get`  
`artifactregistry.packages.list`  
`artifactregistry.repositories.create`  
`artifactregistry.repositories.delete`  
`artifactregistry.repositories.deleteArtifacts`  
`artifactregistry.repositories.downloadArtifacts`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.getIamPolicy`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.setIamPolicy`  
`artifactregistry.repositories.update`  
`artifactregistry.repositories.uploadArtifacts`  
`artifactregistry.tags.create`  
`artifactregistry.tags.delete`  
`artifactregistry.tags.get`  
`artifactregistry.tags.list`  
`artifactregistry.tags.update`  
`artifactregistry.versions.delete`  
`artifactregistry.versions.get`  
`artifactregistry.versions.list`  
  
Customer Experience Insights  |  Role Updated  |  The following permissions have been added to the role `roles/contactcenterinsights.serviceAgent` (Contact Center AI Insights Service Agent): `dialogflow.participants.suggest`  
  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.admin` (Data Catalog Admin): `bigquery.routines.updateTag`  
  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.tagEditor` (Data Catalog Tag Editor): `bigquery.routines.updateTag`  
  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.aamAdmin` (AAM Admin) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.aamConversationalArchitect` (AAM Conversational Architect) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.aamDialogDesigner` (AAM Dialog Designer) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.aamViewer` (AAM Viewer) is now GA.  
Sensitive Data Protection  |  Role Updated  |  The following permissions have been added to the role `roles/dlp.admin` (DLP Administrator): `dlp.columnDataProfiles.get`  
`dlp.columnDataProfiles.list`  
`dlp.projectDataProfiles.get`  
`dlp.projectDataProfiles.list`  
`dlp.tableDataProfiles.get`  
`dlp.tableDataProfiles.list`  
  
Enterprise Knowledge Graph  |  Now GA  |  The role `roles/enterpriseknowledgegraph.serviceAgent` (Enterprise Knowledge Graph Service Agent) is now GA.  
Essential Contacts  |  Now GA  |  The role `roles/essentialcontacts.admin` (Essential Contacts Admin) is now GA.  
Essential Contacts  |  Now GA  |  The role `roles/essentialcontacts.viewer` (Essential Contacts Viewer) is now GA.  
Explore Anthos  |  Role Updated  |  The following permissions have been added to the role `roles/exploreanthos.serviceAgent` (Explore Anthos Service Agent): `serviceusage.services.use`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.networkEndpointGroups.get`  
`container.deployments.create`  
`container.deployments.delete`  
`container.deployments.get`  
`container.deployments.getScale`  
`container.deployments.getStatus`  
`container.deployments.list`  
`container.deployments.rollback`  
`container.deployments.update`  
`container.deployments.updateScale`  
`container.deployments.updateStatus`  
  
Google Cloud Fraud Defense  |  Role Updated  |  The following permissions have been added to the role `roles/recaptchaenterprise.admin` (reCAPTCHA Enterprise Admin): `monitoring.timeSeries.list`  
  
Google Cloud Fraud Defense  |  Role Updated  |  The following permissions have been added to the role `roles/recaptchaenterprise.viewer` (reCAPTCHA Enterprise Viewer): `monitoring.timeSeries.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.controlServiceAgent` (Security Center Control Service Agent): `bigquery.datasets.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.securityHealthAnalyticsServiceAgent` (Security Health Analytics Service Agent): `bigquery.datasets.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.serviceAgent` (Security Center Service Agent): `bigquery.datasets.get`  
  
Cloud Storage  |  Role Updated  |  The following permissions have been added to the role `roles/storage.legacyBucketReader` (Storage Legacy Bucket Reader): `storage.multipartUploads.list`  
  
Gemini Enterprise Agent Platform  |  Added  |  `aiplatform.artifacts.create`  
`aiplatform.artifacts.get`  
`aiplatform.artifacts.list`  
`aiplatform.artifacts.update`  
`aiplatform.contexts.addContextArtifactsAndExecutions`  
`aiplatform.contexts.addContextChildren`  
`aiplatform.contexts.create`  
`aiplatform.contexts.delete`  
`aiplatform.contexts.get`  
`aiplatform.contexts.list`  
`aiplatform.contexts.queryContextLineageSubgraph`  
`aiplatform.contexts.update`  
`aiplatform.edgeDeploymentJobs.create`  
`aiplatform.edgeDeploymentJobs.delete`  
`aiplatform.edgeDeploymentJobs.get`  
`aiplatform.edgeDeploymentJobs.list`  
`aiplatform.edgeDeviceDebugInfo.get`  
`aiplatform.edgeDevices.create`  
`aiplatform.edgeDevices.delete`  
`aiplatform.edgeDevices.get`  
`aiplatform.edgeDevices.list`  
`aiplatform.edgeDevices.update`  
`aiplatform.entityTypes.create`  
`aiplatform.entityTypes.delete`  
`aiplatform.entityTypes.exportFeatureValues`  
`aiplatform.entityTypes.get`  
`aiplatform.entityTypes.importFeatureValues`  
`aiplatform.entityTypes.list`  
`aiplatform.entityTypes.readFeatureValues`  
`aiplatform.entityTypes.streamingReadFeatureValues`  
`aiplatform.entityTypes.update`  
`aiplatform.executions.addExecutionEvents`  
`aiplatform.executions.create`  
`aiplatform.executions.get`  
`aiplatform.executions.list`  
`aiplatform.executions.queryExecutionInputsAndOutputs`  
`aiplatform.executions.update`  
`aiplatform.features.create`  
`aiplatform.features.delete`  
`aiplatform.features.get`  
`aiplatform.features.list`  
`aiplatform.features.update`  
`aiplatform.featurestores.batchReadFeatureValues`  
`aiplatform.featurestores.create`  
`aiplatform.featurestores.delete`  
`aiplatform.featurestores.exportFeatures`  
`aiplatform.featurestores.get`  
`aiplatform.featurestores.importFeatures`  
`aiplatform.featurestores.list`  
`aiplatform.featurestores.readFeatures`  
`aiplatform.featurestores.update`  
`aiplatform.featurestores.writeFeatures`  
`aiplatform.humanInTheLoops.create`  
`aiplatform.humanInTheLoops.delete`  
`aiplatform.humanInTheLoops.get`  
`aiplatform.humanInTheLoops.list`  
`aiplatform.humanInTheLoops.send`  
`aiplatform.humanInTheLoops.update`  
`aiplatform.indexEndpoints.create`  
`aiplatform.indexEndpoints.delete`  
`aiplatform.indexEndpoints.deploy`  
`aiplatform.indexEndpoints.get`  
`aiplatform.indexEndpoints.list`  
`aiplatform.indexEndpoints.undeploy`  
`aiplatform.indexEndpoints.update`  
`aiplatform.indexes.create`  
`aiplatform.indexes.delete`  
`aiplatform.indexes.get`  
`aiplatform.indexes.list`  
`aiplatform.indexes.update`  
`aiplatform.metadataSchemas.create`  
`aiplatform.metadataSchemas.get`  
`aiplatform.metadataSchemas.list`  
`aiplatform.metadataStores.create`  
`aiplatform.metadataStores.delete`  
`aiplatform.metadataStores.get`  
`aiplatform.metadataStores.list`  
`aiplatform.modelDeploymentMonitoringJobs.create`  
`aiplatform.modelDeploymentMonitoringJobs.delete`  
`aiplatform.modelDeploymentMonitoringJobs.get`  
`aiplatform.modelDeploymentMonitoringJobs.list`  
`aiplatform.modelDeploymentMonitoringJobs.pause`  
`aiplatform.modelDeploymentMonitoringJobs.resume`  
`aiplatform.modelDeploymentMonitoringJobs.searchStatsAnomalies`  
`aiplatform.modelDeploymentMonitoringJobs.update`  
`aiplatform.models.update`  
`aiplatform.nasJobs.cancel`  
`aiplatform.nasJobs.create`  
`aiplatform.nasJobs.delete`  
`aiplatform.nasJobs.get`  
`aiplatform.nasJobs.list`  
`aiplatform.pipelineJobs.cancel`  
`aiplatform.pipelineJobs.create`  
`aiplatform.pipelineJobs.delete`  
`aiplatform.pipelineJobs.get`  
`aiplatform.pipelineJobs.list`  
`aiplatform.tensorboardExperiments.create`  
`aiplatform.tensorboardExperiments.delete`  
`aiplatform.tensorboardExperiments.get`  
`aiplatform.tensorboardExperiments.list`  
`aiplatform.tensorboardExperiments.update`  
`aiplatform.tensorboardRuns.create`  
`aiplatform.tensorboardRuns.delete`  
`aiplatform.tensorboardRuns.get`  
`aiplatform.tensorboardRuns.list`  
`aiplatform.tensorboardRuns.update`  
`aiplatform.tensorboardRuns.write`  
`aiplatform.tensorboardTimeSeries.create`  
`aiplatform.tensorboardTimeSeries.delete`  
`aiplatform.tensorboardTimeSeries.get`  
`aiplatform.tensorboardTimeSeries.list`  
`aiplatform.tensorboardTimeSeries.read`  
`aiplatform.tensorboardTimeSeries.update`  
`aiplatform.tensorboards.create`  
`aiplatform.tensorboards.delete`  
`aiplatform.tensorboards.get`  
`aiplatform.tensorboards.list`  
`aiplatform.tensorboards.update`  
  
Apigee  |  Added  |  `apigee.archivedeployments.create`  
`apigee.archivedeployments.delete`  
`apigee.archivedeployments.download`  
`apigee.archivedeployments.get`  
`apigee.archivedeployments.list`  
`apigee.archivedeployments.update`  
`apigee.archivedeployments.upload`  
  
Apigee  |  Now GA  |  `apigee.archivedeployments.create`  
`apigee.archivedeployments.delete`  
`apigee.archivedeployments.download`  
`apigee.archivedeployments.get`  
`apigee.archivedeployments.list`  
`apigee.archivedeployments.update`  
`apigee.archivedeployments.upload`  
  
BigQuery  |  Added  |  `bigquery.routines.updateTag`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.routines.updateTag`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.listAccessPolicy`  
`cloudasset.assets.listIamPolicy`  
`cloudasset.assets.listOSInventories`  
`cloudasset.assets.listOrgPolicy`  
`cloudasset.assets.listResource`  
  
Firestore  |  Supported In Custom Roles  |  `datastore.databases.export`  
`datastore.databases.get`  
`datastore.databases.import`  
`datastore.entities.allocateIds`  
`datastore.entities.create`  
`datastore.entities.delete`  
`datastore.entities.get`  
`datastore.entities.list`  
`datastore.entities.update`  
`datastore.indexes.create`  
`datastore.indexes.delete`  
`datastore.indexes.get`  
`datastore.indexes.list`  
`datastore.indexes.update`  
`datastore.locations.get`  
`datastore.locations.list`  
`datastore.namespaces.get`  
`datastore.namespaces.list`  
`datastore.operations.cancel`  
`datastore.operations.delete`  
`datastore.operations.get`  
`datastore.operations.list`  
`datastore.statistics.get`  
`datastore.statistics.list`  
  
Datastream  |  Added  |  `datastream.connectionProfiles.create`  
`datastream.connectionProfiles.delete`  
`datastream.connectionProfiles.destinationTypes`  
`datastream.connectionProfiles.discover`  
`datastream.connectionProfiles.get`  
`datastream.connectionProfiles.getIamPolicy`  
`datastream.connectionProfiles.list`  
`datastream.connectionProfiles.listStaticServiceIps`  
`datastream.connectionProfiles.setIamPolicy`  
`datastream.connectionProfiles.sourceTypes`  
`datastream.connectionProfiles.update`  
`datastream.locations.fetchStaticIps`  
`datastream.locations.get`  
`datastream.locations.list`  
`datastream.operations.cancel`  
`datastream.operations.delete`  
`datastream.operations.get`  
`datastream.operations.list`  
`datastream.privateConnections.create`  
`datastream.privateConnections.delete`  
`datastream.privateConnections.get`  
`datastream.privateConnections.getIamPolicy`  
`datastream.privateConnections.list`  
`datastream.privateConnections.setIamPolicy`  
`datastream.routes.create`  
`datastream.routes.delete`  
`datastream.routes.get`  
`datastream.routes.getIamPolicy`  
`datastream.routes.list`  
`datastream.routes.setIamPolicy`  
`datastream.streams.computeState`  
`datastream.streams.create`  
`datastream.streams.delete`  
`datastream.streams.fetchErrors`  
`datastream.streams.get`  
`datastream.streams.getIamPolicy`  
`datastream.streams.list`  
`datastream.streams.pause`  
`datastream.streams.resume`  
`datastream.streams.setIamPolicy`  
`datastream.streams.start`  
`datastream.streams.update`  
  
Datastream  |  Supported In Custom Roles  |  `datastream.connectionProfiles.create`  
`datastream.connectionProfiles.delete`  
`datastream.connectionProfiles.destinationTypes`  
`datastream.connectionProfiles.discover`  
`datastream.connectionProfiles.get`  
`datastream.connectionProfiles.getIamPolicy`  
`datastream.connectionProfiles.list`  
`datastream.connectionProfiles.listStaticServiceIps`  
`datastream.connectionProfiles.setIamPolicy`  
`datastream.connectionProfiles.sourceTypes`  
`datastream.connectionProfiles.update`  
`datastream.locations.fetchStaticIps`  
`datastream.locations.get`  
`datastream.locations.list`  
`datastream.operations.cancel`  
`datastream.operations.delete`  
`datastream.operations.get`  
`datastream.operations.list`  
`datastream.privateConnections.create`  
`datastream.privateConnections.delete`  
`datastream.privateConnections.get`  
`datastream.privateConnections.getIamPolicy`  
`datastream.privateConnections.list`  
`datastream.privateConnections.setIamPolicy`  
`datastream.routes.create`  
`datastream.routes.delete`  
`datastream.routes.get`  
`datastream.routes.getIamPolicy`  
`datastream.routes.list`  
`datastream.routes.setIamPolicy`  
`datastream.streams.computeState`  
`datastream.streams.create`  
`datastream.streams.delete`  
`datastream.streams.fetchErrors`  
`datastream.streams.get`  
`datastream.streams.getIamPolicy`  
`datastream.streams.list`  
`datastream.streams.pause`  
`datastream.streams.resume`  
`datastream.streams.setIamPolicy`  
`datastream.streams.start`  
`datastream.streams.update`  
  
Essential Contacts  |  Added  |  `essentialcontacts.contacts.send`  
  
Essential Contacts  |  Supported In Custom Roles  |  `essentialcontacts.contacts.send`  
  
Essential Contacts  |  Now GA  |  `essentialcontacts.contacts.create`  
`essentialcontacts.contacts.delete`  
`essentialcontacts.contacts.get`  
`essentialcontacts.contacts.list`  
`essentialcontacts.contacts.send`  
`essentialcontacts.contacts.update`  
  
Cloud Integrations  |  Added  |  `integrations.apigeeAuthConfigs.create`  
`integrations.apigeeAuthConfigs.delete`  
`integrations.apigeeAuthConfigs.get`  
`integrations.apigeeAuthConfigs.list`  
`integrations.apigeeAuthConfigs.update`  
`integrations.apigeeCertificates.get`  
`integrations.apigeeExecutions.list`  
`integrations.apigeeIntegrationVers.create`  
`integrations.apigeeIntegrationVers.deploy`  
`integrations.apigeeIntegrationVers.get`  
`integrations.apigeeIntegrationVers.list`  
`integrations.apigeeIntegrationVers.update`  
`integrations.apigeeIntegrations.invoke`  
`integrations.apigeeIntegrations.list`  
`integrations.apigeeSfdcChannels.create`  
`integrations.apigeeSfdcChannels.delete`  
`integrations.apigeeSfdcChannels.get`  
`integrations.apigeeSfdcChannels.list`  
`integrations.apigeeSfdcChannels.update`  
`integrations.apigeeSfdcInstances.create`  
`integrations.apigeeSfdcInstances.delete`  
`integrations.apigeeSfdcInstances.get`  
`integrations.apigeeSfdcInstances.list`  
`integrations.apigeeSfdcInstances.update`  
`integrations.apigeeSuspensions.list`  
`integrations.apigeeSuspensions.resolve`  
  
Payments Reseller Subscription  |  Added  |  `paymentsresellersubscription.products.list`  
`paymentsresellersubscription.promotions.list`  
`paymentsresellersubscription.subscriptions.cancel`  
`paymentsresellersubscription.subscriptions.extend`  
`paymentsresellersubscription.subscriptions.get`  
`paymentsresellersubscription.subscriptions.provision`  
`paymentsresellersubscription.subscriptions.undoCancel`  
  
Payments Reseller Subscription  |  Supported In Custom Roles  |  `paymentsresellersubscription.products.list`  
`paymentsresellersubscription.promotions.list`  
`paymentsresellersubscription.subscriptions.cancel`  
`paymentsresellersubscription.subscriptions.extend`  
`paymentsresellersubscription.subscriptions.get`  
`paymentsresellersubscription.subscriptions.provision`  
`paymentsresellersubscription.subscriptions.undoCancel`  
  
  
## Cloud IAM changes as of 2021-05-28

Service | Change | Description  
---|---|---  
Cloud Service Mesh  |  Role Updated  |  The following permissions have been added to the role `roles/anthosservicemesh.serviceAgent` (Anthos Service Mesh Service Agent): `container.clusters.get`  
  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.developerAdmin` (Apigee Developer Admin): `apigee.developersubscriptions.create`  
`apigee.developersubscriptions.get`  
`apigee.developersubscriptions.list`  
`apigee.developersubscriptions.update`  
`apigee.rateplans.get`  
`apigee.rateplans.list`  
  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.serviceAgent` (Apigee Service Agent): `iam.serviceAccounts.getAccessToken`  
`iam.serviceAccounts.getOpenIdToken`  
  
Content Warehouse  |  Now GA  |  The role `roles/contentwarehouse.serviceAgent` (Content Warehouse Service Agent) is now GA.  
Resource Settings  |  Now GA  |  The role `roles/resourcesettings.admin` (Resource Settings Administrator) is now GA.  
Resource Settings  |  Now GA  |  The role `roles/resourcesettings.viewer` (Resource Settings Viewer) is now GA.  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.analyzeMove`  
  
Cloud Asset Inventory  |  Now GA  |  `cloudasset.assets.analyzeMove`  
  
Dialogflow  |  Added  |  `dialogflow.securitySettings.create`  
`dialogflow.securitySettings.delete`  
`dialogflow.securitySettings.get`  
`dialogflow.securitySettings.list`  
`dialogflow.securitySettings.update`  
  
Dialogflow  |  Now GA  |  `dialogflow.securitySettings.create`  
`dialogflow.securitySettings.delete`  
`dialogflow.securitySettings.get`  
`dialogflow.securitySettings.list`  
`dialogflow.securitySettings.update`  
  
Cloud DNS  |  Added  |  `dns.resourceRecordSets.get`  
  
Cloud DNS  |  Supported In Custom Roles  |  `dns.resourceRecordSets.get`  
  
Cloud DNS  |  Now GA  |  `dns.resourceRecordSets.get`  
  
Resource Settings  |  Added  |  `resourcesettings.settings.get`  
`resourcesettings.settings.list`  
`resourcesettings.settings.update`  
  
Resource Settings  |  Supported In Custom Roles  |  `resourcesettings.settings.get`  
`resourcesettings.settings.list`  
  
Resource Settings  |  Now GA  |  `resourcesettings.settings.get`  
`resourcesettings.settings.list`  
`resourcesettings.settings.update`  
  
  
## Cloud IAM changes as of 2021-05-14

Service | Change | Description  
---|---|---  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.columnDataProfilesReader` (DLP Column Data Profiles Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.dataProfilesReader` (DLP Data Profiles Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.estimatesAdmin` (DLP Cost Estimation) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.projectDataProfilesReader` (DLP Project Data Profiles Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.tableDataProfilesReader` (DLP Table Data Profiles Reader) is now GA.  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.admin` (Security Center Admin): `resourcemanager.folders.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminEditor` (Security Center Admin Editor): `resourcemanager.folders.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminViewer` (Security Center Admin Viewer): `resourcemanager.folders.get`  
`resourcemanager.projects.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.assetsViewer` (Security Center Assets Viewer): `resourcemanager.folders.get`  
`resourcemanager.projects.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.findingsEditor` (Security Center Findings Editor): `resourcemanager.folders.get`  
`resourcemanager.projects.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.findingsViewer` (Security Center Findings Viewer): `resourcemanager.folders.get`  
`resourcemanager.projects.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.securityHealthAnalyticsServiceAgent` (Security Health Analytics Service Agent): `resourcemanager.folders.get`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.listCloudkmsCryptoKeys`  
  
Google Cloud Support  |  Added  |  `cloudsupport.accounts.purchase`  
  
Google Cloud Support  |  Supported In Custom Roles  |  `cloudsupport.accounts.purchase`  
  
Google Cloud Support  |  Now GA  |  `cloudsupport.accounts.purchase`  
  
Dataflow  |  Now GA  |  `dataflow.jobs.snapshot`  
`dataflow.snapshots.delete`  
`dataflow.snapshots.get`  
`dataflow.snapshots.list`  
  
Sensitive Data Protection  |  Added  |  `dlp.columnDataProfiles.get`  
`dlp.columnDataProfiles.list`  
`dlp.estimates.cancel`  
`dlp.estimates.create`  
`dlp.estimates.delete`  
`dlp.estimates.get`  
`dlp.estimates.list`  
`dlp.projectDataProfiles.get`  
`dlp.projectDataProfiles.list`  
`dlp.tableDataProfiles.get`  
`dlp.tableDataProfiles.list`  
  
Sensitive Data Protection  |  Now GA  |  `dlp.columnDataProfiles.get`  
`dlp.columnDataProfiles.list`  
`dlp.estimates.cancel`  
`dlp.estimates.create`  
`dlp.estimates.delete`  
`dlp.estimates.get`  
`dlp.estimates.list`  
`dlp.projectDataProfiles.get`  
`dlp.projectDataProfiles.list`  
`dlp.tableDataProfiles.get`  
`dlp.tableDataProfiles.list`  
  
Cloud Logging  |  Added  |  `logging.fields.access`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.fields.access`  
  
  
## Cloud IAM changes as of 2021-05-07

Service | Change | Description  
---|---|---  
Cloud Deploy  |  Now GA  |  The role `roles/clouddeploy.serviceAgent` (Cloud Deploy Service Agent) is now GA.  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.admin` (Cloud Functions Admin): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.events.receiveAuditLogWritten`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.setIamPolicy`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
`remotebuildexecution.blobs.get`  
`resourcemanager.projects.list`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.setIamPolicy`  
`run.services.update`  
  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.developer` (Cloud Functions Developer): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
`remotebuildexecution.blobs.get`  
`resourcemanager.projects.list`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.update`  
  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.viewer` (Cloud Functions Viewer): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`remotebuildexecution.blobs.get`  
`resourcemanager.projects.list`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.list`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.admin` (Firebase Admin): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.events.receiveAuditLogWritten`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.setIamPolicy`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
`remotebuildexecution.blobs.get`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.setIamPolicy`  
`run.services.update`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.developAdmin` (Firebase Develop Admin): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.events.receiveAuditLogWritten`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.setIamPolicy`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
`remotebuildexecution.blobs.get`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.setIamPolicy`  
`run.services.update`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.developViewer` (Firebase Develop Viewer): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`remotebuildexecution.blobs.get`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.list`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.viewer` (Firebase Viewer): `cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`remotebuildexecution.blobs.get`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.list`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
  
GKE Multi-Cloud  |  Now GA  |  The role `roles/gkemulticloud.serviceAgent` (Anthos Multi-Cloud Service Agent) is now GA.  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.privateLogViewer` (Private Logs Viewer): `logging.views.access`  
  
Resource Manager  |  Role Updated  |  The following permissions have been added to the role `roles/resourcemanager.tagUser` (Tag User): `resourcemanager.tagKeys.get`  
  
Service Directory  |  Now GA  |  The role `roles/servicedirectory.pscAuthorizedService` (Private Service Connect Authorized Service) is now GA.  
Compute Engine  |  Added  |  `compute.instances.addResourcePolicies`  
`compute.instances.removeResourcePolicies`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.addResourcePolicies`  
`compute.instances.removeResourcePolicies`  
  
Compute Engine  |  Now GA  |  `compute.instances.addResourcePolicies`  
`compute.instances.removeResourcePolicies`  
  
Service Directory  |  Added  |  `servicedirectory.networks.access`  
  
Service Directory  |  Now GA  |  `servicedirectory.networks.access`  
  
Translation Hub  |  Added  |  `translationhub.portals.create`  
`translationhub.portals.delete`  
`translationhub.portals.get`  
`translationhub.portals.list`  
`translationhub.portals.update`  
  
Translation Hub  |  Supported In Custom Roles  |  `translationhub.portals.create`  
`translationhub.portals.delete`  
`translationhub.portals.get`  
`translationhub.portals.list`  
`translationhub.portals.update`  
  
  
## Cloud IAM changes as of 2021-04-30

Service | Change | Description  
---|---|---  
Cloud SQL  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsql.admin` (Cloud SQL Admin): `recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update`  
  
Cloud SQL  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsql.editor` (Cloud SQL Editor): `recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update`  
  
Cloud SQL  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsql.viewer` (Cloud SQL Viewer): `recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update`  
  
Explore Anthos  |  Role Updated  |  The following permissions have been added to the role `roles/exploreanthos.serviceAgent` (Explore Anthos Service Agent): `container.apiServices.create`  
`container.apiServices.delete`  
`container.apiServices.get`  
`container.apiServices.getStatus`  
`container.apiServices.list`  
`container.apiServices.update`  
`container.apiServices.updateStatus`  
`container.auditSinks.create`  
`container.auditSinks.delete`  
`container.auditSinks.get`  
`container.auditSinks.list`  
`container.auditSinks.update`  
`container.backendConfigs.create`  
`container.backendConfigs.delete`  
`container.backendConfigs.get`  
`container.backendConfigs.list`  
`container.backendConfigs.update`  
`container.bindings.create`  
`container.bindings.delete`  
`container.bindings.get`  
`container.bindings.list`  
`container.bindings.update`  
`container.certificateSigningRequests.approve`  
`container.certificateSigningRequests.create`  
`container.certificateSigningRequests.delete`  
`container.certificateSigningRequests.get`  
`container.certificateSigningRequests.getStatus`  
`container.certificateSigningRequests.list`  
`container.certificateSigningRequests.update`  
`container.certificateSigningRequests.updateStatus`  
`container.clusterRoleBindings.create`  
`container.clusterRoleBindings.delete`  
`container.clusterRoleBindings.get`  
`container.clusterRoleBindings.list`  
`container.clusterRoleBindings.update`  
`container.clusterRoles.bind`  
`container.clusterRoles.create`  
`container.clusterRoles.delete`  
`container.clusterRoles.escalate`  
`container.clusterRoles.get`  
`container.clusterRoles.list`  
`container.clusterRoles.update`  
`container.clusters.create`  
`container.clusters.delete`  
`container.clusters.getCredentials`  
`container.clusters.update`  
`container.componentStatuses.get`  
`container.componentStatuses.list`  
`container.configMaps.create`  
`container.configMaps.delete`  
`container.configMaps.get`  
`container.configMaps.list`  
`container.configMaps.update`  
`container.controllerRevisions.create`  
`container.controllerRevisions.delete`  
`container.controllerRevisions.get`  
`container.controllerRevisions.list`  
`container.controllerRevisions.update`  
`container.cronJobs.create`  
`container.cronJobs.delete`  
`container.cronJobs.get`  
`container.cronJobs.getStatus`  
`container.cronJobs.list`  
`container.cronJobs.update`  
`container.cronJobs.updateStatus`  
`container.csiDrivers.create`  
`container.csiDrivers.delete`  
`container.csiDrivers.get`  
`container.csiDrivers.list`  
`container.csiDrivers.update`  
`container.csiNodeInfos.create`  
`container.csiNodeInfos.delete`  
`container.csiNodeInfos.get`  
`container.csiNodeInfos.list`  
`container.csiNodeInfos.update`  
`container.csiNodes.create`  
`container.csiNodes.delete`  
`container.csiNodes.get`  
`container.csiNodes.list`  
`container.csiNodes.update`  
`container.customResourceDefinitions.create`  
`container.customResourceDefinitions.delete`  
`container.customResourceDefinitions.get`  
`container.customResourceDefinitions.getStatus`  
`container.customResourceDefinitions.list`  
`container.customResourceDefinitions.update`  
`container.customResourceDefinitions.updateStatus`  
`container.daemonSets.create`  
`container.daemonSets.delete`  
`container.daemonSets.get`  
`container.daemonSets.getStatus`  
`container.daemonSets.list`  
`container.daemonSets.update`  
`container.daemonSets.updateStatus`  
`container.deployments.create`  
`container.deployments.delete`  
`container.deployments.get`  
`container.deployments.getScale`  
`container.deployments.getStatus`  
`container.deployments.list`  
`container.deployments.rollback`  
`container.deployments.update`  
`container.deployments.updateScale`  
`container.deployments.updateStatus`  
`container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.endpoints.create`  
`container.endpoints.delete`  
`container.endpoints.get`  
`container.endpoints.list`  
`container.endpoints.update`  
`container.events.create`  
`container.events.delete`  
`container.events.get`  
`container.events.list`  
`container.events.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.horizontalPodAutoscalers.create`  
`container.horizontalPodAutoscalers.delete`  
`container.horizontalPodAutoscalers.get`  
`container.horizontalPodAutoscalers.getStatus`  
`container.horizontalPodAutoscalers.list`  
`container.horizontalPodAutoscalers.update`  
`container.horizontalPodAutoscalers.updateStatus`  
`container.hostServiceAgent.use`  
`container.ingresses.create`  
`container.ingresses.delete`  
`container.ingresses.get`  
`container.ingresses.getStatus`  
`container.ingresses.list`  
`container.ingresses.update`  
`container.ingresses.updateStatus`  
`container.initializerConfigurations.create`  
`container.initializerConfigurations.delete`  
`container.initializerConfigurations.get`  
`container.initializerConfigurations.list`  
`container.initializerConfigurations.update`  
`container.jobs.create`  
`container.jobs.delete`  
`container.jobs.get`  
`container.jobs.getStatus`  
`container.jobs.list`  
`container.jobs.update`  
`container.jobs.updateStatus`  
`container.leases.create`  
`container.leases.delete`  
`container.leases.get`  
`container.leases.list`  
`container.leases.update`  
`container.limitRanges.create`  
`container.limitRanges.delete`  
`container.limitRanges.get`  
`container.limitRanges.list`  
`container.limitRanges.update`  
`container.localSubjectAccessReviews.create`  
`container.localSubjectAccessReviews.list`  
`container.managedCertificates.create`  
`container.managedCertificates.delete`  
`container.managedCertificates.get`  
`container.managedCertificates.list`  
`container.managedCertificates.update`  
`container.mutatingWebhookConfigurations.create`  
`container.mutatingWebhookConfigurations.delete`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.mutatingWebhookConfigurations.update`  
`container.namespaces.create`  
`container.namespaces.delete`  
`container.namespaces.finalize`  
`container.namespaces.get`  
`container.namespaces.getStatus`  
`container.namespaces.list`  
`container.namespaces.update`  
`container.namespaces.updateStatus`  
`container.networkPolicies.create`  
`container.networkPolicies.delete`  
`container.networkPolicies.get`  
`container.networkPolicies.list`  
`container.networkPolicies.update`  
`container.nodes.create`  
`container.nodes.delete`  
`container.nodes.get`  
`container.nodes.getStatus`  
`container.nodes.list`  
`container.nodes.proxy`  
`container.nodes.update`  
`container.nodes.updateStatus`  
`container.operations.get`  
`container.operations.list`  
`container.persistentVolumeClaims.create`  
`container.persistentVolumeClaims.delete`  
`container.persistentVolumeClaims.get`  
`container.persistentVolumeClaims.getStatus`  
`container.persistentVolumeClaims.list`  
`container.persistentVolumeClaims.update`  
`container.persistentVolumeClaims.updateStatus`  
`container.persistentVolumes.create`  
`container.persistentVolumes.delete`  
`container.persistentVolumes.get`  
`container.persistentVolumes.getStatus`  
`container.persistentVolumes.list`  
`container.persistentVolumes.update`  
`container.persistentVolumes.updateStatus`  
`container.petSets.create`  
`container.petSets.delete`  
`container.petSets.get`  
`container.petSets.list`  
`container.petSets.update`  
`container.petSets.updateStatus`  
`container.podDisruptionBudgets.create`  
`container.podDisruptionBudgets.delete`  
`container.podDisruptionBudgets.get`  
`container.podDisruptionBudgets.getStatus`  
`container.podDisruptionBudgets.list`  
`container.podDisruptionBudgets.update`  
`container.podDisruptionBudgets.updateStatus`  
`container.podPresets.create`  
`container.podPresets.delete`  
`container.podPresets.get`  
`container.podPresets.list`  
`container.podPresets.update`  
`container.podSecurityPolicies.create`  
`container.podSecurityPolicies.delete`  
`container.podSecurityPolicies.get`  
`container.podSecurityPolicies.list`  
`container.podSecurityPolicies.update`  
`container.podSecurityPolicies.use`  
`container.podTemplates.create`  
`container.podTemplates.delete`  
`container.podTemplates.get`  
`container.podTemplates.list`  
`container.podTemplates.update`  
`container.pods.attach`  
`container.pods.create`  
`container.pods.delete`  
`container.pods.evict`  
`container.pods.exec`  
`container.pods.get`  
`container.pods.getLogs`  
`container.pods.getStatus`  
`container.pods.initialize`  
`container.pods.portForward`  
`container.pods.proxy`  
`container.pods.update`  
`container.pods.updateStatus`  
`container.priorityClasses.create`  
`container.priorityClasses.delete`  
`container.priorityClasses.get`  
`container.priorityClasses.list`  
`container.priorityClasses.update`  
`container.replicaSets.create`  
`container.replicaSets.delete`  
`container.replicaSets.get`  
`container.replicaSets.getScale`  
`container.replicaSets.getStatus`  
`container.replicaSets.list`  
`container.replicaSets.update`  
`container.replicaSets.updateScale`  
`container.replicaSets.updateStatus`  
`container.replicationControllers.create`  
`container.replicationControllers.delete`  
`container.replicationControllers.get`  
`container.replicationControllers.getScale`  
`container.replicationControllers.getStatus`  
`container.replicationControllers.list`  
`container.replicationControllers.update`  
`container.replicationControllers.updateScale`  
`container.replicationControllers.updateStatus`  
`container.resourceQuotas.create`  
`container.resourceQuotas.delete`  
`container.resourceQuotas.get`  
`container.resourceQuotas.getStatus`  
`container.resourceQuotas.list`  
`container.resourceQuotas.update`  
`container.resourceQuotas.updateStatus`  
`container.roleBindings.create`  
`container.roleBindings.delete`  
`container.roleBindings.get`  
`container.roleBindings.list`  
`container.roleBindings.update`  
`container.roles.bind`  
`container.roles.create`  
`container.roles.delete`  
`container.roles.escalate`  
`container.roles.get`  
`container.roles.list`  
`container.roles.update`  
`container.runtimeClasses.create`  
`container.runtimeClasses.delete`  
`container.runtimeClasses.get`  
`container.runtimeClasses.list`  
`container.runtimeClasses.update`  
`container.scheduledJobs.create`  
`container.scheduledJobs.delete`  
`container.scheduledJobs.get`  
`container.scheduledJobs.list`  
`container.scheduledJobs.update`  
`container.scheduledJobs.updateStatus`  
`container.secrets.create`  
`container.secrets.delete`  
`container.secrets.get`  
`container.secrets.list`  
`container.secrets.update`  
`container.selfSubjectAccessReviews.create`  
`container.selfSubjectAccessReviews.list`  
`container.selfSubjectRulesReviews.create`  
`container.serviceAccounts.create`  
`container.serviceAccounts.createToken`  
`container.serviceAccounts.delete`  
`container.serviceAccounts.list`  
`container.services.create`  
`container.services.delete`  
`container.services.get`  
`container.services.getStatus`  
`container.services.list`  
`container.services.proxy`  
`container.services.update`  
`container.services.updateStatus`  
`container.statefulSets.create`  
`container.statefulSets.delete`  
`container.statefulSets.get`  
`container.statefulSets.getScale`  
`container.statefulSets.getStatus`  
`container.statefulSets.list`  
`container.statefulSets.update`  
`container.statefulSets.updateScale`  
`container.statefulSets.updateStatus`  
`container.storageClasses.create`  
`container.storageClasses.delete`  
`container.storageClasses.get`  
`container.storageClasses.list`  
`container.storageClasses.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.subjectAccessReviews.create`  
`container.subjectAccessReviews.list`  
`container.thirdPartyObjects.create`  
`container.thirdPartyObjects.delete`  
`container.thirdPartyObjects.get`  
`container.thirdPartyObjects.list`  
`container.thirdPartyObjects.update`  
`container.thirdPartyResources.create`  
`container.thirdPartyResources.delete`  
`container.thirdPartyResources.get`  
`container.thirdPartyResources.list`  
`container.thirdPartyResources.update`  
`container.tokenReviews.create`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.validatingWebhookConfigurations.create`  
`container.validatingWebhookConfigurations.delete`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.validatingWebhookConfigurations.update`  
`container.volumeAttachments.create`  
`container.volumeAttachments.delete`  
`container.volumeAttachments.get`  
`container.volumeAttachments.getStatus`  
`container.volumeAttachments.list`  
`container.volumeAttachments.update`  
`container.volumeAttachments.updateStatus`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
`gkehub.features.create`  
`gkehub.features.delete`  
`gkehub.features.get`  
`gkehub.features.getIamPolicy`  
`gkehub.features.list`  
`gkehub.features.setIamPolicy`  
`gkehub.features.update`  
`gkehub.locations.get`  
`gkehub.locations.list`  
`gkehub.memberships.create`  
`gkehub.memberships.delete`  
`gkehub.memberships.generateConnectManifest`  
`gkehub.memberships.get`  
`gkehub.memberships.getIamPolicy`  
`gkehub.memberships.list`  
`gkehub.memberships.setIamPolicy`  
`gkehub.memberships.update`  
`gkehub.operations.cancel`  
`gkehub.operations.delete`  
`gkehub.operations.get`  
`gkehub.operations.list`  
`resourcemanager.projects.list`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.globalAddresses.list`  
  
Translation  |  Added  |  `cloudtranslate.generalModels.batchDocPredict`  
`cloudtranslate.generalModels.docPredict`  
`cloudtranslate.glossaries.batchDocPredict`  
`cloudtranslate.glossaries.docPredict`  
  
Translation  |  Supported In Custom Roles  |  `cloudtranslate.generalModels.batchDocPredict`  
`cloudtranslate.glossaries.batchDocPredict`  
  
Compute Engine  |  Now GA  |  `compute.globalForwardingRules.pscSetLabels`  
`compute.globalForwardingRules.pscSetTarget`  
  
  
## Cloud IAM changes as of 2021-04-23

Service | Change | Description  
---|---|---  
Gemini Enterprise Agent Platform  |  Role Updated  |  The following permissions have been added to the role `roles/aiplatform.serviceAgent` (AI Platform Service Agent): `aiplatform.batchPredictionJobs.create`  
`aiplatform.batchPredictionJobs.get`  
`aiplatform.batchPredictionJobs.list`  
  
Anthos Demo  |  Now GA  |  The role `roles/anthosdemo.serviceAgent` (Anthos Demo Service Agent) is now GA.  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.serviceAgent` (Apigee Service Agent): `cloudtrace.traces.patch`  
  
Binary Authorization  |  Role Updated  |  The following permissions have been added to the role `roles/binaryauthorization.policyAdmin` (Binary Authorization Policy Administrator): `binaryauthorization.continuousValidationConfig.get`  
`binaryauthorization.continuousValidationConfig.getIamPolicy`  
`binaryauthorization.continuousValidationConfig.setIamPolicy`  
`binaryauthorization.continuousValidationConfig.update`  
  
Binary Authorization  |  Role Updated  |  The following permissions have been added to the role `roles/binaryauthorization.policyEditor` (Binary Authorization Policy Editor): `binaryauthorization.continuousValidationConfig.get`  
`binaryauthorization.continuousValidationConfig.update`  
  
Binary Authorization  |  Role Updated  |  The following permissions have been added to the role `roles/binaryauthorization.policyViewer` (Binary Authorization Policy Viewer): `binaryauthorization.continuousValidationConfig.get`  
  
Google Security Operations Service Management  |  Now GA  |  The role `roles/chroniclesm.admin` (Chronicle Service Admin) is now GA.  
Google Security Operations Service Management  |  Now GA  |  The role `roles/chroniclesm.viewer` (Chronicle Service Viewer) is now GA.  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.serviceAgent` (Cloud Functions Service Agent): `eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
`run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.update`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `compute.instances.updateSecurity`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.packetMirroringAdmin` (Compute packet mirroring admin): `compute.instances.updateSecurity`  
  
Customer Experience Insights  |  Role Updated  |  The following permissions have been added to the role `roles/contactcenterinsights.serviceAgent` (Contact Center AI Insights Service Agent): `dialogflow.operations.get`  
`dialogflow.sessions.detectIntent`  
`pubsub.topics.get`  
`pubsub.topics.publish`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `file.backups.create`  
`file.backups.delete`  
`file.backups.get`  
`file.backups.list`  
`file.backups.update`  
`file.instances.create`  
`file.instances.delete`  
`file.instances.get`  
`file.instances.list`  
`file.instances.restore`  
`file.instances.update`  
`file.locations.get`  
`file.locations.list`  
`file.operations.cancel`  
`file.operations.delete`  
`file.operations.get`  
`file.operations.list`  
`file.snapshots.create`  
`file.snapshots.delete`  
`file.snapshots.get`  
`file.snapshots.list`  
`file.snapshots.update`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.worker` (Dataflow Worker): `storage.buckets.get`  
  
Google Earth Engine  |  Role Added  |  The role `roles/earthengine.appsPublisher` (Earth Engine Apps Publisher) has been added with the following permissions: `cloudresourcemanager.googleapis.com/projects.get`  
`iam.googleapis.com/serviceAccounts.create`  
`iam.googleapis.com/serviceAccounts.disable`  
`iam.googleapis.com/serviceAccounts.enable`  
`iam.googleapis.com/serviceAccounts.get`  
`iam.googleapis.com/serviceAccounts.getIamPolicy`  
`iam.googleapis.com/serviceAccounts.setIamPolicy`  
`iam.serviceAccounts.create`  
`iam.serviceAccounts.disable`  
`iam.serviceAccounts.enable`  
`iam.serviceAccounts.get`  
`iam.serviceAccounts.getIamPolicy`  
`iam.serviceAccounts.setIamPolicy`  
`resourcemanager.projects.get`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `logging.buckets.copyLogEntries`  
`logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
`privateca.caPools.create`  
`privateca.caPools.delete`  
`privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.caPools.update`  
`privateca.certificateTemplates.create`  
`privateca.certificateTemplates.delete`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.update`  
`privateca.certificateTemplates.use`  
`privateca.certificates.createForSelf`  
`pubsublite.topics.computeTimeCursor`  
`redis.instances.rescheduleMaintenance`  
`vmmigration.cloneJobs.create`  
`vmmigration.cloneJobs.get`  
`vmmigration.cloneJobs.list`  
`vmmigration.cloneJobs.update`  
`vmmigration.cutoverJobs.create`  
`vmmigration.cutoverJobs.get`  
`vmmigration.cutoverJobs.list`  
`vmmigration.cutoverJobs.update`  
`vmmigration.datacenterConnectors.create`  
`vmmigration.datacenterConnectors.delete`  
`vmmigration.datacenterConnectors.get`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.create`  
`vmmigration.migratingVms.delete`  
`vmmigration.migratingVms.get`  
`vmmigration.migratingVms.list`  
`vmmigration.migratingVms.update`  
`vmmigration.utilizationReports.create`  
`vmmigration.utilizationReports.delete`  
`vmmigration.utilizationReports.get`  
`vmmigration.utilizationReports.list`  
  
Explore Anthos  |  Role Updated  |  The following permissions have been added to the role `roles/exploreanthos.serviceAgent` (Explore Anthos Service Agent): `container.clusters.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityAdmin` (Security Admin): `logging.operations.list`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.caPools.setIamPolicy`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.setIamPolicy`  
`vmmigration.cloneJobs.list`  
`vmmigration.cutoverJobs.list`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.list`  
`vmmigration.utilizationReports.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityReviewer` (Security Reviewer): `logging.operations.list`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`vmmigration.cloneJobs.list`  
`vmmigration.cutoverJobs.list`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.list`  
`vmmigration.utilizationReports.list`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.admin` (Logging Admin): `logging.buckets.copyLogEntries`  
`logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.configWriter` (Logs Configuration Writer): `logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
  
Media Asset  |  Role Updated  |  The following permissions have been added to the role `roles/mediaasset.serviceAgent` (Media Asset Service Agent): `pubsub.topics.get`  
`pubsub.topics.publish`  
  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.regionBackendServices.create`  
`compute.regionBackendServices.delete`  
`compute.regionBackendServices.get`  
`compute.regionBackendServices.list`  
`compute.regionBackendServices.setSecurityPolicy`  
`compute.regionBackendServices.update`  
`compute.regionBackendServices.use`  
`compute.regionHealthChecks.create`  
`compute.regionHealthChecks.delete`  
`compute.regionHealthChecks.get`  
`compute.regionHealthChecks.list`  
`compute.regionHealthChecks.update`  
`compute.regionHealthChecks.use`  
`compute.regionHealthChecks.useReadOnly`  
`compute.regionTargetHttpProxies.create`  
`compute.regionTargetHttpProxies.delete`  
`compute.regionTargetHttpProxies.get`  
`compute.regionTargetHttpProxies.list`  
`compute.regionTargetHttpProxies.setUrlMap`  
`compute.regionTargetHttpProxies.use`  
`compute.regionTargetHttpsProxies.create`  
`compute.regionTargetHttpsProxies.delete`  
`compute.regionTargetHttpsProxies.get`  
`compute.regionTargetHttpsProxies.list`  
`compute.regionTargetHttpsProxies.setSslCertificates`  
`compute.regionTargetHttpsProxies.setUrlMap`  
`compute.regionTargetHttpsProxies.use`  
`compute.regionUrlMaps.create`  
`compute.regionUrlMaps.delete`  
`compute.regionUrlMaps.get`  
`compute.regionUrlMaps.invalidateCache`  
`compute.regionUrlMaps.list`  
`compute.regionUrlMaps.update`  
`compute.regionUrlMaps.use`  
`compute.regionUrlMaps.validate`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `logging.buckets.copyLogEntries`  
`logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
`privateca.caPools.create`  
`privateca.caPools.delete`  
`privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.caPools.setIamPolicy`  
`privateca.caPools.update`  
`privateca.certificateTemplates.create`  
`privateca.certificateTemplates.delete`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.setIamPolicy`  
`privateca.certificateTemplates.update`  
`privateca.certificateTemplates.use`  
`privateca.certificates.createForSelf`  
`pubsublite.topics.computeTimeCursor`  
`redis.instances.rescheduleMaintenance`  
`vmmigration.cloneJobs.create`  
`vmmigration.cloneJobs.get`  
`vmmigration.cloneJobs.list`  
`vmmigration.cloneJobs.update`  
`vmmigration.cutoverJobs.create`  
`vmmigration.cutoverJobs.get`  
`vmmigration.cutoverJobs.list`  
`vmmigration.cutoverJobs.update`  
`vmmigration.datacenterConnectors.create`  
`vmmigration.datacenterConnectors.delete`  
`vmmigration.datacenterConnectors.get`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.create`  
`vmmigration.migratingVms.delete`  
`vmmigration.migratingVms.get`  
`vmmigration.migratingVms.list`  
`vmmigration.migratingVms.update`  
`vmmigration.utilizationReports.create`  
`vmmigration.utilizationReports.delete`  
`vmmigration.utilizationReports.get`  
`vmmigration.utilizationReports.list`  
  
Certificate Authority Service  |  Role Added  |  The role `roles/privateca.templateUser` (CA Service Certificate Template User) has been added with the following permissions: `privateca.certificateTemplates.get`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.use`  
`privateca.googleapis.com/certificateTemplates.get`  
`privateca.googleapis.com/certificateTemplates.list`  
`privateca.googleapis.com/certificateTemplates.use`  
  
Certificate Authority Service  |  Role Added  |  The role `roles/privateca.workloadCertificateRequester` (CA Service Workload Certificate Requester) has been added with the following permissions: `privateca.certificates.createForSelf`  
`privateca.googleapis.com/certificates.createForSelf`  
  
Certificate Authority Service  |  Now GA  |  The role `roles/privateca.admin` (CA Service Admin) is now GA.  
Certificate Authority Service  |  Now GA  |  The role `roles/privateca.auditor` (CA Service Auditor) is now GA.  
Certificate Authority Service  |  Now GA  |  The role `roles/privateca.caManager` (CA Service Operation Manager) is now GA.  
Certificate Authority Service  |  Now GA  |  The role `roles/privateca.certificateManager` (CA Service Certificate Manager) is now GA.  
Certificate Authority Service  |  Now GA  |  The role `roles/privateca.certificateRequester` (CA Service Certificate Requester) is now GA.  
Certificate Authority Service  |  Role Updated  |  The following permissions have been added to the role `roles/privateca.admin` (CA Service Admin): `privateca.caPools.create`  
`privateca.caPools.delete`  
`privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.caPools.setIamPolicy`  
`privateca.caPools.update`  
`privateca.certificateTemplates.create`  
`privateca.certificateTemplates.delete`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.setIamPolicy`  
`privateca.certificateTemplates.update`  
`privateca.certificateTemplates.use`  
`privateca.certificates.createForSelf`  
  
Certificate Authority Service  |  Role Updated  |  The following permissions have been added to the role `roles/privateca.auditor` (CA Service Auditor): `privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
  
Certificate Authority Service  |  Role Updated  |  The following permissions have been added to the role `roles/privateca.caManager` (CA Service Operation Manager): `privateca.caPools.create`  
`privateca.caPools.delete`  
`privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.caPools.update`  
`privateca.certificateTemplates.create`  
`privateca.certificateTemplates.delete`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.update`  
  
Certificate Authority Service  |  Role Updated  |  The following permissions have been added to the role `roles/privateca.certificateManager` (CA Service Certificate Manager): `privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
  
Pub/Sub  |  Role Updated  |  The following permissions have been added to the role `roles/pubsub.viewer` (Pub/Sub Viewer): `pubsub.schemas.validate`  
  
Pub/Sub Lite  |  Role Updated  |  The following permissions have been added to the role `roles/pubsublite.admin` (Pub/Sub Lite Admin): `pubsublite.topics.computeTimeCursor`  
  
Pub/Sub Lite  |  Role Updated  |  The following permissions have been added to the role `roles/pubsublite.editor` (Pub/Sub Lite Editor): `pubsublite.topics.computeTimeCursor`  
  
Pub/Sub Lite  |  Role Updated  |  The following permissions have been added to the role `roles/pubsublite.subscriber` (Pub/Sub Lite Subscriber): `pubsublite.topics.computeTimeCursor`  
  
Recommender  |  Now GA  |  The role `roles/recommender.cloudAssetInsightsAdmin` (Cloud Asset Insights Admin) is now GA.  
Recommender  |  Now GA  |  The role `roles/recommender.cloudAssetInsightsViewer` (Cloud Asset Insights Viewer) is now GA.  
Memorystore for Redis  |  Role Updated  |  The following permissions have been added to the role `roles/redis.admin` (Cloud Memorystore Redis Admin): `redis.instances.rescheduleMaintenance`  
  
Cloud Run  |  Now GA  |  The role `roles/run.admin` (Cloud Run Admin) is now GA.  
Cloud Run  |  Now GA  |  The role `roles/run.developer` (Cloud Run Developer) is now GA.  
Cloud Run  |  Now GA  |  The role `roles/run.invoker` (Cloud Run Invoker) is now GA.  
Cloud Run  |  Now GA  |  The role `roles/run.viewer` (Cloud Run Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `logging.buckets.copyLogEntries`  
`logging.operations.get`  
`logging.operations.list`  
`privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.use`  
`pubsub.schemas.validate`  
`pubsublite.topics.computeTimeCursor`  
`vmmigration.cloneJobs.get`  
`vmmigration.cloneJobs.list`  
`vmmigration.cutoverJobs.get`  
`vmmigration.cutoverJobs.list`  
`vmmigration.datacenterConnectors.get`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.get`  
`vmmigration.migratingVms.list`  
`vmmigration.utilizationReports.get`  
`vmmigration.utilizationReports.list`  
  
VM Migration  |  Role Updated  |  The following permissions have been added to the role `roles/vmmigration.admin` (VM Migration Administrator): `vmmigration.cloneJobs.create`  
`vmmigration.cloneJobs.get`  
`vmmigration.cloneJobs.list`  
`vmmigration.cloneJobs.update`  
`vmmigration.cutoverJobs.create`  
`vmmigration.cutoverJobs.get`  
`vmmigration.cutoverJobs.list`  
`vmmigration.cutoverJobs.update`  
`vmmigration.datacenterConnectors.create`  
`vmmigration.datacenterConnectors.delete`  
`vmmigration.datacenterConnectors.get`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.create`  
`vmmigration.migratingVms.delete`  
`vmmigration.migratingVms.get`  
`vmmigration.migratingVms.list`  
`vmmigration.migratingVms.update`  
`vmmigration.utilizationReports.create`  
`vmmigration.utilizationReports.delete`  
`vmmigration.utilizationReports.get`  
`vmmigration.utilizationReports.list`  
  
VM Migration  |  Role Updated  |  The following permissions have been added to the role `roles/vmmigration.viewer` (VM Migration Viewer): `vmmigration.cloneJobs.get`  
`vmmigration.cloneJobs.list`  
`vmmigration.cutoverJobs.get`  
`vmmigration.cutoverJobs.list`  
`vmmigration.datacenterConnectors.get`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.migratingVms.get`  
`vmmigration.migratingVms.list`  
`vmmigration.utilizationReports.get`  
`vmmigration.utilizationReports.list`  
  
Google Cloud VMware Engine  |  Role Updated  |  The following permissions have been added to the role `roles/vmwareengine.vmwareengineAdmin` (VMware Engine Service Admin): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Google Cloud VMware Engine  |  Role Updated  |  The following permissions have been added to the role `roles/vmwareengine.vmwareengineViewer` (VMware Engine Service Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Billing  |  Added  |  `billing.accounts.getPricing`  
  
Cloud Billing  |  Supported In Custom Roles  |  `billing.accounts.getPricing`  
  
Cloud Billing  |  Now GA  |  `billing.accounts.getPricing`  
  
Google Security Operations Service Management  |  Added  |  `chroniclesm.gcpAssociations.create`  
`chroniclesm.gcpAssociations.delete`  
`chroniclesm.gcpAssociations.get`  
`chroniclesm.gcpSettings.get`  
`chroniclesm.gcpSettings.update`  
  
Google Security Operations Service Management  |  Now GA  |  `chroniclesm.gcpAssociations.create`  
`chroniclesm.gcpAssociations.delete`  
`chroniclesm.gcpAssociations.get`  
`chroniclesm.gcpSettings.get`  
`chroniclesm.gcpSettings.update`  
  
Commerce Offer Catalog  |  Added  |  `commerceoffercatalog.offers.get`  
  
Commerce Offer Catalog  |  Supported In Custom Roles  |  `commerceoffercatalog.offers.get`  
  
Commerce Price Management  |  Added  |  `commerceprice.privateoffers.create`  
`commerceprice.privateoffers.delete`  
`commerceprice.privateoffers.get`  
`commerceprice.privateoffers.list`  
`commerceprice.privateoffers.publish`  
`commerceprice.privateoffers.update`  
  
Commerce Price Management  |  Supported In Custom Roles  |  `commerceprice.privateoffers.create`  
`commerceprice.privateoffers.delete`  
`commerceprice.privateoffers.get`  
`commerceprice.privateoffers.list`  
`commerceprice.privateoffers.publish`  
`commerceprice.privateoffers.update`  
  
Compute Engine  |  Added  |  `compute.forwardingRules.pscCreate`  
`compute.forwardingRules.pscDelete`  
`compute.forwardingRules.pscSetLabels`  
`compute.forwardingRules.pscSetTarget`  
`compute.forwardingRules.pscUpdate`  
`compute.globalForwardingRules.pscSetLabels`  
`compute.globalForwardingRules.pscSetTarget`  
`compute.instances.updateSecurity`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.forwardingRules.pscCreate`  
`compute.forwardingRules.pscDelete`  
`compute.forwardingRules.pscSetLabels`  
`compute.forwardingRules.pscSetTarget`  
`compute.forwardingRules.pscUpdate`  
`compute.globalForwardingRules.pscSetLabels`  
`compute.globalForwardingRules.pscSetTarget`  
`compute.instances.updateSecurity`  
  
Compute Engine  |  Now GA  |  `compute.forwardingRules.pscCreate`  
`compute.forwardingRules.pscDelete`  
`compute.forwardingRules.pscSetLabels`  
`compute.forwardingRules.pscSetTarget`  
`compute.forwardingRules.pscUpdate`  
`compute.instances.updateSecurity`  
  
Cloud Data Fusion  |  Added  |  `datafusion.namespaces.create`  
`datafusion.namespaces.delete`  
`datafusion.namespaces.execute`  
`datafusion.namespaces.get`  
`datafusion.namespaces.getIamPolicy`  
`datafusion.namespaces.list`  
`datafusion.namespaces.setIamPolicy`  
`datafusion.namespaces.update`  
  
Firebase App Check  |  Added  |  `firebaseappcheck.debugTokens.get`  
`firebaseappcheck.debugTokens.update`  
`firebaseappcheck.deviceCheckConfig.get`  
`firebaseappcheck.deviceCheckConfig.update`  
`firebaseappcheck.recaptchaConfig.get`  
`firebaseappcheck.recaptchaConfig.update`  
`firebaseappcheck.services.get`  
`firebaseappcheck.services.update`  
  
Firebase App Check  |  Supported In Custom Roles  |  `firebaseappcheck.debugTokens.get`  
`firebaseappcheck.debugTokens.update`  
`firebaseappcheck.deviceCheckConfig.get`  
`firebaseappcheck.deviceCheckConfig.update`  
`firebaseappcheck.recaptchaConfig.get`  
`firebaseappcheck.recaptchaConfig.update`  
`firebaseappcheck.services.get`  
`firebaseappcheck.services.update`  
  
GKE Multi-Cloud  |  Added  |  `gkemulticloud.awsClusters.create`  
`gkemulticloud.awsClusters.delete`  
`gkemulticloud.awsClusters.get`  
`gkemulticloud.awsClusters.getAdminKubeconfig`  
`gkemulticloud.awsClusters.list`  
`gkemulticloud.awsClusters.update`  
`gkemulticloud.awsNodePools.create`  
`gkemulticloud.awsNodePools.delete`  
`gkemulticloud.awsNodePools.get`  
`gkemulticloud.awsNodePools.list`  
`gkemulticloud.azureClients.create`  
`gkemulticloud.azureClients.delete`  
`gkemulticloud.azureClients.get`  
`gkemulticloud.azureClients.list`  
`gkemulticloud.azureClusters.create`  
`gkemulticloud.azureClusters.delete`  
`gkemulticloud.azureClusters.get`  
`gkemulticloud.azureClusters.getAdminKubeconfig`  
`gkemulticloud.azureClusters.list`  
`gkemulticloud.azureClusters.update`  
`gkemulticloud.azureNodePools.create`  
`gkemulticloud.azureNodePools.delete`  
`gkemulticloud.azureNodePools.get`  
`gkemulticloud.azureNodePools.list`  
`gkemulticloud.operations.cancel`  
`gkemulticloud.operations.delete`  
`gkemulticloud.operations.get`  
`gkemulticloud.operations.list`  
`gkemulticloud.operations.wait`  
  
Cloud Logging  |  Added  |  `logging.buckets.copyLogEntries`  
`logging.operations.cancel`  
`logging.operations.get`  
`logging.operations.list`  
  
Dataproc Metastore  |  Added  |  `metastore.backups.create`  
`metastore.backups.delete`  
`metastore.backups.get`  
`metastore.backups.list`  
`metastore.backups.use`  
  
Dataproc Metastore  |  Now GA  |  `metastore.backups.create`  
`metastore.backups.delete`  
`metastore.backups.get`  
`metastore.backups.list`  
`metastore.backups.use`  
  
Network Connectivity Center  |  Added  |  `networkconnectivity.hubs.create`  
`networkconnectivity.hubs.delete`  
`networkconnectivity.hubs.get`  
`networkconnectivity.hubs.getIamPolicy`  
`networkconnectivity.hubs.list`  
`networkconnectivity.hubs.setIamPolicy`  
`networkconnectivity.hubs.update`  
`networkconnectivity.locations.get`  
`networkconnectivity.locations.list`  
`networkconnectivity.operations.cancel`  
`networkconnectivity.operations.delete`  
`networkconnectivity.operations.get`  
`networkconnectivity.operations.list`  
`networkconnectivity.spokes.create`  
`networkconnectivity.spokes.delete`  
`networkconnectivity.spokes.get`  
`networkconnectivity.spokes.getIamPolicy`  
`networkconnectivity.spokes.list`  
`networkconnectivity.spokes.setIamPolicy`  
`networkconnectivity.spokes.update`  
  
Notebooks  |  Added  |  `notebooks.runtimes.create`  
`notebooks.runtimes.delete`  
`notebooks.runtimes.get`  
`notebooks.runtimes.getIamPolicy`  
`notebooks.runtimes.list`  
`notebooks.runtimes.reset`  
`notebooks.runtimes.setIamPolicy`  
`notebooks.runtimes.start`  
`notebooks.runtimes.stop`  
`notebooks.runtimes.switch`  
  
Notebooks  |  Now GA  |  `notebooks.runtimes.create`  
`notebooks.runtimes.delete`  
`notebooks.runtimes.get`  
`notebooks.runtimes.getIamPolicy`  
`notebooks.runtimes.list`  
`notebooks.runtimes.reset`  
`notebooks.runtimes.setIamPolicy`  
`notebooks.runtimes.start`  
`notebooks.runtimes.stop`  
`notebooks.runtimes.switch`  
  
Cloud Monitoring  |  Added  |  `opsconfigmonitoring.resourceMetadata.list`  
  
Cloud OS Config  |  Added  |  `osconfig.instanceOSPoliciesCompliances.get`  
`osconfig.instanceOSPoliciesCompliances.list`  
`osconfig.inventories.get`  
`osconfig.inventories.list`  
`osconfig.osPolicyAssignments.create`  
`osconfig.osPolicyAssignments.delete`  
`osconfig.osPolicyAssignments.get`  
`osconfig.osPolicyAssignments.list`  
`osconfig.osPolicyAssignments.update`  
`osconfig.vulnerabilityReports.get`  
`osconfig.vulnerabilityReports.list`  
  
Cloud OS Config  |  Supported In Custom Roles  |  `osconfig.instanceOSPoliciesCompliances.get`  
`osconfig.instanceOSPoliciesCompliances.list`  
`osconfig.inventories.get`  
`osconfig.inventories.list`  
`osconfig.osPolicyAssignments.create`  
`osconfig.osPolicyAssignments.delete`  
`osconfig.osPolicyAssignments.get`  
`osconfig.osPolicyAssignments.list`  
`osconfig.osPolicyAssignments.update`  
`osconfig.vulnerabilityReports.get`  
`osconfig.vulnerabilityReports.list`  
  
Certificate Authority Service  |  Added  |  `privateca.caPools.create`  
`privateca.caPools.delete`  
`privateca.caPools.get`  
`privateca.caPools.getIamPolicy`  
`privateca.caPools.list`  
`privateca.caPools.setIamPolicy`  
`privateca.caPools.update`  
`privateca.certificateTemplates.create`  
`privateca.certificateTemplates.delete`  
`privateca.certificateTemplates.get`  
`privateca.certificateTemplates.getIamPolicy`  
`privateca.certificateTemplates.list`  
`privateca.certificateTemplates.setIamPolicy`  
`privateca.certificateTemplates.update`  
`privateca.certificateTemplates.use`  
`privateca.certificates.createForSelf`  
  
Certificate Authority Service  |  Now GA  |  `privateca.certificateAuthorities.create`  
`privateca.certificateAuthorities.delete`  
`privateca.certificateAuthorities.get`  
`privateca.certificateAuthorities.getIamPolicy`  
`privateca.certificateAuthorities.list`  
`privateca.certificateAuthorities.setIamPolicy`  
`privateca.certificateAuthorities.update`  
`privateca.certificateRevocationLists.create`  
`privateca.certificateRevocationLists.get`  
`privateca.certificateRevocationLists.getIamPolicy`  
`privateca.certificateRevocationLists.list`  
`privateca.certificateRevocationLists.setIamPolicy`  
`privateca.certificateRevocationLists.update`  
`privateca.certificates.create`  
`privateca.certificates.get`  
`privateca.certificates.getIamPolicy`  
`privateca.certificates.list`  
`privateca.certificates.setIamPolicy`  
`privateca.certificates.update`  
`privateca.locations.get`  
`privateca.locations.list`  
`privateca.operations.cancel`  
`privateca.operations.delete`  
`privateca.operations.get`  
`privateca.operations.list`  
`privateca.reusableConfigs.create`  
`privateca.reusableConfigs.delete`  
`privateca.reusableConfigs.get`  
`privateca.reusableConfigs.getIamPolicy`  
`privateca.reusableConfigs.list`  
`privateca.reusableConfigs.setIamPolicy`  
`privateca.reusableConfigs.update`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.topics.computeTimeCursor`  
  
Recommender  |  Added  |  `recommender.cloudAssetInsights.get`  
`recommender.cloudAssetInsights.list`  
`recommender.cloudAssetInsights.update`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.cloudAssetInsights.get`  
`recommender.cloudAssetInsights.list`  
`recommender.cloudAssetInsights.update`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update`  
  
Recommender  |  Now GA  |  `recommender.cloudAssetInsights.get`  
`recommender.cloudAssetInsights.list`  
`recommender.cloudAssetInsights.update`  
  
Memorystore for Redis  |  Added  |  `redis.instances.rescheduleMaintenance`  
  
Resource Manager  |  Added  |  `resourcemanager.hierarchyNodes.createTagBinding`  
`resourcemanager.hierarchyNodes.deleteTagBinding`  
`resourcemanager.hierarchyNodes.listTagBindings`  
  
Cloud Run  |  Now GA  |  `run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.setIamPolicy`  
`run.services.update`  
  
Security Command Center  |  Added  |  `securitycenter.userinterfacemetadata.get`  
  
Security Command Center  |  Supported In Custom Roles  |  `securitycenter.userinterfacemetadata.get`  
  
Cloud Storage  |  Added  |  `storage.multipartUploads.abort`  
`storage.multipartUploads.create`  
`storage.multipartUploads.list`  
`storage.multipartUploads.listParts`  
  
Cloud Storage  |  Now GA  |  `storage.multipartUploads.abort`  
`storage.multipartUploads.create`  
`storage.multipartUploads.list`  
`storage.multipartUploads.listParts`  
  
VM Migration  |  Added  |  `vmmigration.cloneJobs.create`  
`vmmigration.cloneJobs.get`  
`vmmigration.cloneJobs.list`  
`vmmigration.cloneJobs.update`  
`vmmigration.cutoverJobs.create`  
`vmmigration.cutoverJobs.get`  
`vmmigration.cutoverJobs.list`  
`vmmigration.cutoverJobs.update`  
`vmmigration.datacenterConnectors.create`  
`vmmigration.datacenterConnectors.delete`  
`vmmigration.datacenterConnectors.get`  
`vmmigration.datacenterConnectors.list`  
`vmmigration.groups.create`  
`vmmigration.groups.delete`  
`vmmigration.groups.get`  
`vmmigration.groups.list`  
`vmmigration.groups.update`  
`vmmigration.locations.get`  
`vmmigration.locations.list`  
`vmmigration.migratingVms.create`  
`vmmigration.migratingVms.delete`  
`vmmigration.migratingVms.get`  
`vmmigration.migratingVms.list`  
`vmmigration.migratingVms.update`  
`vmmigration.operations.cancel`  
`vmmigration.operations.delete`  
`vmmigration.operations.get`  
`vmmigration.operations.list`  
`vmmigration.sources.create`  
`vmmigration.sources.delete`  
`vmmigration.sources.get`  
`vmmigration.sources.list`  
`vmmigration.sources.update`  
`vmmigration.targets.create`  
`vmmigration.targets.delete`  
`vmmigration.targets.get`  
`vmmigration.targets.list`  
`vmmigration.targets.update`  
`vmmigration.utilizationReports.create`  
`vmmigration.utilizationReports.delete`  
`vmmigration.utilizationReports.get`  
`vmmigration.utilizationReports.list`  
  
  
## Cloud IAM changes as of 2021-04-09

Service | Change | Description  
---|---|---  
Apigee  |  Now GA  |  The role `roles/apigee.monetizationAdmin` (Apigee Monetization Admin) is now GA.  
Cloud Billing  |  Role Updated  |  The following permissions have been added to the role `roles/billing.costsManager` (Billing Account Costs Manager): `billing.resourceAssociations.list`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `artifactregistry.repositories.create`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.update`  
  
Compute Engine  |  Now GA  |  The role `roles/compute.publicIpAdmin` (Compute Public IP Admin) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.consoleSimulatorUser` (Dialogflow Console Simulator User) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.consoleSmartMessagingAllowlistEditor` (Dialogflow Console Smart Messaging Allowlist Editor) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been removed from the role `roles/editor` (Editor): `iam.googleapis.com/workloadIdentityPoolProviders.create`  
`iam.googleapis.com/workloadIdentityPoolProviders.delete`  
`iam.googleapis.com/workloadIdentityPoolProviders.undelete`  
`iam.googleapis.com/workloadIdentityPoolProviders.update`  
`iam.googleapis.com/workloadIdentityPools.create`  
`iam.googleapis.com/workloadIdentityPools.delete`  
`iam.googleapis.com/workloadIdentityPools.undelete`  
`iam.googleapis.com/workloadIdentityPools.update`  
`iam.workloadIdentityPoolProviders.create`  
`iam.workloadIdentityPoolProviders.delete`  
`iam.workloadIdentityPoolProviders.undelete`  
`iam.workloadIdentityPoolProviders.update`  
`iam.workloadIdentityPools.create`  
`iam.workloadIdentityPools.delete`  
`iam.workloadIdentityPools.undelete`  
`iam.workloadIdentityPools.update`  
  
Explore Anthos  |  Now GA  |  The role `roles/exploreanthos.serviceAgent` (Explore Anthos Service Agent) is now GA.  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityAdmin` (Security Admin): `cloudasset.assets.searchAllResources`  
`policysimulator.replays.create`  
`policysimulator.replays.get`  
`policysimulator.replays.run`  
  
Dataproc Metastore  |  Now GA  |  The role `roles/metastore.admin` (Dataproc Metastore Admin) is now GA.  
Dataproc Metastore  |  Now GA  |  The role `roles/metastore.editor` (Dataproc Metastore Editor) is now GA.  
Dataproc Metastore  |  Now GA  |  The role `roles/metastore.metadataOperator` (Dataproc Metastore Metadata Operator) is now GA.  
Dataproc Metastore  |  Now GA  |  The role `roles/metastore.user` (Dataproc Metastore Viewer) is now GA.  
Multi-Cluster Ingress  |  Role Updated  |  The following permissions have been added to the role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent): `compute.subnetworks.list`  
`container.thirdPartyObjects.create`  
  
Service Usage  |  Now GA  |  The role `roles/serviceusage.apiKeysAdmin` (API Keys Admin) is now GA.  
Service Usage  |  Now GA  |  The role `roles/serviceusage.apiKeysViewer` (API Keys Viewer) is now GA.  
Service Usage  |  Now GA  |  The role `roles/serviceusage.serviceUsageAdmin` (Service Usage Admin) is now GA.  
Service Usage  |  Now GA  |  The role `roles/serviceusage.serviceUsageConsumer` (Service Usage Consumer) is now GA.  
Service Usage  |  Now GA  |  The role `roles/serviceusage.serviceUsageViewer` (Service Usage Viewer) is now GA.  
Workflows  |  Now GA  |  The role `roles/workflows.admin` (Workflows Admin) is now GA.  
Workflows  |  Now GA  |  The role `roles/workflows.editor` (Workflows Editor) is now GA.  
Workflows  |  Now GA  |  The role `roles/workflows.invoker` (Workflows Invoker) is now GA.  
Workflows  |  Now GA  |  The role `roles/workflows.viewer` (Workflows Viewer) is now GA.  
Apigee  |  Added  |  `apigee.developersubscriptions.create`  
`apigee.developersubscriptions.get`  
`apigee.developersubscriptions.list`  
`apigee.developersubscriptions.update`  
`apigee.rateplans.create`  
`apigee.rateplans.delete`  
`apigee.rateplans.get`  
`apigee.rateplans.list`  
`apigee.rateplans.update`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.developersubscriptions.create`  
`apigee.developersubscriptions.get`  
`apigee.developersubscriptions.list`  
`apigee.developersubscriptions.update`  
  
Apigee  |  Now GA  |  `apigee.developersubscriptions.create`  
`apigee.developersubscriptions.get`  
`apigee.developersubscriptions.list`  
`apigee.developersubscriptions.update`  
`apigee.rateplans.create`  
`apigee.rateplans.delete`  
`apigee.rateplans.get`  
`apigee.rateplans.list`  
`apigee.rateplans.update`  
  
Cloud Key Management Service  |  Added  |  `cloudkms.locations.get`  
`cloudkms.locations.list`  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `cloudkms.locations.get`  
`cloudkms.locations.list`  
  
Cloud Key Management Service  |  Now GA  |  `cloudkms.locations.get`  
`cloudkms.locations.list`  
  
Compute Engine  |  Added  |  `compute.organizations.setFirewallPolicy`  
  
Compute Engine  |  Now GA  |  `compute.globalPublicDelegatedPrefixes.create`  
`compute.globalPublicDelegatedPrefixes.delete`  
`compute.globalPublicDelegatedPrefixes.get`  
`compute.globalPublicDelegatedPrefixes.list`  
`compute.globalPublicDelegatedPrefixes.update`  
`compute.globalPublicDelegatedPrefixes.updatePolicy`  
`compute.globalPublicDelegatedPrefixes.use`  
`compute.organizations.listAssociations`  
`compute.organizations.setFirewallPolicy`  
`compute.publicAdvertisedPrefixes.create`  
`compute.publicAdvertisedPrefixes.delete`  
`compute.publicAdvertisedPrefixes.get`  
`compute.publicAdvertisedPrefixes.list`  
`compute.publicAdvertisedPrefixes.update`  
`compute.publicAdvertisedPrefixes.updatePolicy`  
`compute.publicAdvertisedPrefixes.use`  
`compute.publicDelegatedPrefixes.create`  
`compute.publicDelegatedPrefixes.delete`  
`compute.publicDelegatedPrefixes.get`  
`compute.publicDelegatedPrefixes.list`  
`compute.publicDelegatedPrefixes.update`  
`compute.publicDelegatedPrefixes.updatePolicy`  
`compute.publicDelegatedPrefixes.use`  
  
Dialogflow  |  Added  |  `dialogflow.answerrecords.delete`  
`dialogflow.answerrecords.get`  
`dialogflow.answerrecords.list`  
`dialogflow.answerrecords.update`  
`dialogflow.callMatchers.create`  
`dialogflow.callMatchers.delete`  
`dialogflow.callMatchers.list`  
`dialogflow.conversationDatasets.create`  
`dialogflow.conversationDatasets.delete`  
`dialogflow.conversationDatasets.get`  
`dialogflow.conversationDatasets.import`  
`dialogflow.conversationDatasets.list`  
`dialogflow.conversationModels.create`  
`dialogflow.conversationModels.delete`  
`dialogflow.conversationModels.deploy`  
`dialogflow.conversationModels.get`  
`dialogflow.conversationModels.list`  
`dialogflow.conversationModels.undeploy`  
`dialogflow.conversationProfiles.create`  
`dialogflow.conversationProfiles.delete`  
`dialogflow.conversationProfiles.get`  
`dialogflow.conversationProfiles.list`  
`dialogflow.conversationProfiles.update`  
`dialogflow.conversations.addPhoneNumber`  
`dialogflow.conversations.complete`  
`dialogflow.conversations.create`  
`dialogflow.conversations.get`  
`dialogflow.conversations.list`  
`dialogflow.messages.list`  
`dialogflow.modelEvaluations.get`  
`dialogflow.modelEvaluations.list`  
`dialogflow.participants.analyzeContent`  
`dialogflow.participants.create`  
`dialogflow.participants.get`  
`dialogflow.participants.list`  
`dialogflow.participants.suggest`  
`dialogflow.participants.update`  
`dialogflow.phoneNumberOrders.cancel`  
`dialogflow.phoneNumberOrders.create`  
`dialogflow.phoneNumberOrders.get`  
`dialogflow.phoneNumberOrders.list`  
`dialogflow.phoneNumberOrders.update`  
`dialogflow.phoneNumbers.delete`  
`dialogflow.phoneNumbers.list`  
`dialogflow.phoneNumbers.undelete`  
`dialogflow.phoneNumbers.update`  
`dialogflow.smartMessagingEntries.create`  
`dialogflow.smartMessagingEntries.delete`  
`dialogflow.smartMessagingEntries.get`  
`dialogflow.smartMessagingEntries.list`  
  
Dialogflow  |  Supported In Custom Roles  |  `dialogflow.answerrecords.delete`  
`dialogflow.answerrecords.get`  
`dialogflow.answerrecords.list`  
`dialogflow.answerrecords.update`  
`dialogflow.callMatchers.create`  
`dialogflow.callMatchers.delete`  
`dialogflow.callMatchers.list`  
`dialogflow.conversationDatasets.create`  
`dialogflow.conversationDatasets.delete`  
`dialogflow.conversationDatasets.get`  
`dialogflow.conversationDatasets.import`  
`dialogflow.conversationDatasets.list`  
`dialogflow.conversationModels.create`  
`dialogflow.conversationModels.delete`  
`dialogflow.conversationModels.deploy`  
`dialogflow.conversationModels.get`  
`dialogflow.conversationModels.list`  
`dialogflow.conversationModels.undeploy`  
`dialogflow.conversations.addPhoneNumber`  
`dialogflow.messages.list`  
`dialogflow.modelEvaluations.get`  
`dialogflow.modelEvaluations.list`  
`dialogflow.participants.suggest`  
`dialogflow.phoneNumberOrders.cancel`  
`dialogflow.phoneNumberOrders.create`  
`dialogflow.phoneNumberOrders.get`  
`dialogflow.phoneNumberOrders.list`  
`dialogflow.phoneNumberOrders.update`  
`dialogflow.phoneNumbers.delete`  
`dialogflow.phoneNumbers.list`  
`dialogflow.phoneNumbers.undelete`  
`dialogflow.phoneNumbers.update`  
`dialogflow.smartMessagingEntries.create`  
`dialogflow.smartMessagingEntries.delete`  
`dialogflow.smartMessagingEntries.get`  
`dialogflow.smartMessagingEntries.list`  
  
Dialogflow  |  Now GA  |  `dialogflow.answerrecords.delete`  
`dialogflow.answerrecords.get`  
`dialogflow.answerrecords.list`  
`dialogflow.answerrecords.update`  
`dialogflow.callMatchers.create`  
`dialogflow.callMatchers.delete`  
`dialogflow.callMatchers.list`  
`dialogflow.conversationDatasets.create`  
`dialogflow.conversationDatasets.delete`  
`dialogflow.conversationDatasets.get`  
`dialogflow.conversationDatasets.import`  
`dialogflow.conversationDatasets.list`  
`dialogflow.conversationModels.create`  
`dialogflow.conversationModels.delete`  
`dialogflow.conversationModels.deploy`  
`dialogflow.conversationModels.get`  
`dialogflow.conversationModels.list`  
`dialogflow.conversationModels.undeploy`  
`dialogflow.conversationProfiles.create`  
`dialogflow.conversationProfiles.delete`  
`dialogflow.conversationProfiles.get`  
`dialogflow.conversationProfiles.list`  
`dialogflow.conversationProfiles.update`  
`dialogflow.conversations.addPhoneNumber`  
`dialogflow.conversations.complete`  
`dialogflow.conversations.create`  
`dialogflow.conversations.get`  
`dialogflow.conversations.list`  
`dialogflow.messages.list`  
`dialogflow.modelEvaluations.get`  
`dialogflow.modelEvaluations.list`  
`dialogflow.participants.analyzeContent`  
`dialogflow.participants.create`  
`dialogflow.participants.get`  
`dialogflow.participants.list`  
`dialogflow.participants.suggest`  
`dialogflow.participants.update`  
`dialogflow.phoneNumberOrders.cancel`  
`dialogflow.phoneNumberOrders.create`  
`dialogflow.phoneNumberOrders.get`  
`dialogflow.phoneNumberOrders.list`  
`dialogflow.phoneNumberOrders.update`  
`dialogflow.phoneNumbers.delete`  
`dialogflow.phoneNumbers.list`  
`dialogflow.phoneNumbers.undelete`  
`dialogflow.phoneNumbers.update`  
`dialogflow.smartMessagingEntries.create`  
`dialogflow.smartMessagingEntries.delete`  
`dialogflow.smartMessagingEntries.get`  
`dialogflow.smartMessagingEntries.list`  
  
Cloud Logging  |  Added  |  `logging.queries.listShared`  
`logging.queries.share`  
`logging.queries.updateShared`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.queries.listShared`  
`logging.queries.share`  
`logging.queries.updateShared`  
  
Cloud Logging  |  Now GA  |  `logging.queries.listShared`  
`logging.queries.share`  
`logging.queries.updateShared`  
  
Managed Service for Microsoft Active Directory  |  Added  |  `managedidentities.domains.updateLDAPSSettings`  
  
Managed Service for Microsoft Active Directory  |  Supported In Custom Roles  |  `managedidentities.domains.updateLDAPSSettings`  
  
Managed Service for Microsoft Active Directory  |  Now GA  |  `managedidentities.domains.updateLDAPSSettings`  
  
Dataproc Metastore  |  Added  |  `metastore.services.restore`  
  
Dataproc Metastore  |  Now GA  |  `metastore.imports.create`  
`metastore.imports.get`  
`metastore.imports.list`  
`metastore.imports.update`  
`metastore.locations.get`  
`metastore.locations.list`  
`metastore.operations.cancel`  
`metastore.operations.delete`  
`metastore.operations.get`  
`metastore.operations.list`  
`metastore.services.create`  
`metastore.services.delete`  
`metastore.services.export`  
`metastore.services.get`  
`metastore.services.getIamPolicy`  
`metastore.services.list`  
`metastore.services.restore`  
`metastore.services.setIamPolicy`  
`metastore.services.update`  
  
Notebooks  |  Added  |  `notebooks.instances.updateShieldInstanceConfig`  
  
Notebooks  |  Now GA  |  `notebooks.instances.updateShieldInstanceConfig`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.topics.computeHeadCursor`  
  
Pub/Sub Lite  |  Now GA  |  `pubsublite.topics.computeHeadCursor`  
  
Service Usage  |  Supported In Custom Roles  |  `serviceusage.services.disable`  
`serviceusage.services.enable`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Service Usage  |  Now GA  |  `serviceusage.services.disable`  
`serviceusage.services.enable`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Workflows  |  Now GA  |  `workflows.executions.cancel`  
`workflows.executions.create`  
`workflows.executions.get`  
`workflows.executions.list`  
`workflows.locations.get`  
`workflows.locations.list`  
`workflows.operations.cancel`  
`workflows.operations.get`  
`workflows.operations.list`  
`workflows.workflows.create`  
`workflows.workflows.delete`  
`workflows.workflows.get`  
`workflows.workflows.getIamPolicy`  
`workflows.workflows.list`  
`workflows.workflows.setIamPolicy`  
`workflows.workflows.update`  
  
  
## Cloud IAM changes as of 2021-03-05

Service | Change | Description  
---|---|---  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.serviceAgent` (Apigee Service Agent): `apigee.appkeys.delete`  
  
Assured Workloads  |  Role Updated  |  The following permissions have been added to the role `roles/assuredworkloads.serviceAgent` (Assured Workloads Service Agent): `cloudasset.assets.exportResource`  
`cloudasset.feeds.create`  
`cloudasset.feeds.delete`  
`cloudasset.feeds.get`  
`cloudasset.feeds.update`  
`serviceusage.services.use`  
  
Customer Experience Insights  |  Role Updated  |  The following permissions have been added to the role `roles/contactcenterinsights.serviceAgent` (Contact Center AI Insights Service Agent): `dialogflow.documents.create`  
`dialogflow.documents.delete`  
`dialogflow.documents.get`  
`dialogflow.documents.list`  
  
Database Migration Service  |  Now GA  |  The role `roles/datamigration.admin` (Database Migration Admin) is now GA.  
Early Access Center  |  Now GA  |  The role `roles/earlyaccesscenter.admin` (Early Access Center Administrator) is now GA.  
Early Access Center  |  Now GA  |  The role `roles/earlyaccesscenter.viewer` (Early Access Center Viewer) is now GA.  
Game Servers  |  Role Updated  |  The following permissions have been added to the role `roles/gameservices.serviceAgent` (Game Services Service Agent): `container.clusterRoleBindings.create`  
`container.clusterRoleBindings.update`  
`container.clusterRoles.bind`  
`container.clusterRoles.create`  
`container.clusterRoles.escalate`  
`container.clusterRoles.update`  
`container.roleBindings.create`  
`container.roles.bind`  
`container.roles.create`  
`container.roles.escalate`  
  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.serviceAgent` (GKE Hub Service Agent): `container.clusterRoleBindings.list`  
`container.clusterRoles.list`  
  
Network Management API  |  Role Updated  |  The following permissions have been added to the role `roles/networkmanagement.serviceAgent` (GCP Network Management Service Agent): `cloudsql.instances.get`  
`cloudsql.instances.list`  
`compute.addresses.get`  
`compute.addresses.list`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.globalAddresses.get`  
`compute.globalAddresses.list`  
`compute.globalNetworkEndpointGroups.get`  
`compute.globalNetworkEndpointGroups.list`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.list`  
`compute.networks.getEffectiveFirewalls`  
`compute.networks.listPeeringRoutes`  
`compute.regionHealthChecks.get`  
`compute.regionHealthChecks.list`  
`compute.regionNetworkEndpointGroups.get`  
`compute.regionNetworkEndpointGroups.list`  
`compute.targetGrpcProxies.get`  
`compute.targetGrpcProxies.list`  
  
Gemini Enterprise Agent Platform  |  Added  |  `aiplatform.studies.create`  
`aiplatform.studies.delete`  
`aiplatform.studies.get`  
`aiplatform.studies.list`  
`aiplatform.studies.update`  
`aiplatform.trials.create`  
`aiplatform.trials.delete`  
`aiplatform.trials.get`  
`aiplatform.trials.list`  
`aiplatform.trials.update`  
  
Database Migration Service  |  Supported In Custom Roles  |  `datamigration.connectionprofiles.create`  
`datamigration.connectionprofiles.delete`  
`datamigration.connectionprofiles.get`  
`datamigration.connectionprofiles.getIamPolicy`  
`datamigration.connectionprofiles.list`  
`datamigration.connectionprofiles.setIamPolicy`  
`datamigration.connectionprofiles.update`  
`datamigration.locations.get`  
`datamigration.locations.list`  
`datamigration.migrationjobs.create`  
`datamigration.migrationjobs.delete`  
`datamigration.migrationjobs.generateSshScript`  
`datamigration.migrationjobs.get`  
`datamigration.migrationjobs.getIamPolicy`  
`datamigration.migrationjobs.list`  
`datamigration.migrationjobs.promote`  
`datamigration.migrationjobs.restart`  
`datamigration.migrationjobs.resume`  
`datamigration.migrationjobs.setIamPolicy`  
`datamigration.migrationjobs.start`  
`datamigration.migrationjobs.stop`  
`datamigration.migrationjobs.update`  
`datamigration.migrationjobs.verify`  
`datamigration.operations.cancel`  
`datamigration.operations.delete`  
`datamigration.operations.get`  
`datamigration.operations.list`  
  
Database Migration Service  |  Now GA  |  `datamigration.connectionprofiles.create`  
`datamigration.connectionprofiles.delete`  
`datamigration.connectionprofiles.get`  
`datamigration.connectionprofiles.getIamPolicy`  
`datamigration.connectionprofiles.list`  
`datamigration.connectionprofiles.setIamPolicy`  
`datamigration.connectionprofiles.update`  
`datamigration.locations.get`  
`datamigration.locations.list`  
`datamigration.migrationjobs.create`  
`datamigration.migrationjobs.delete`  
`datamigration.migrationjobs.generateSshScript`  
`datamigration.migrationjobs.get`  
`datamigration.migrationjobs.getIamPolicy`  
`datamigration.migrationjobs.list`  
`datamigration.migrationjobs.promote`  
`datamigration.migrationjobs.restart`  
`datamigration.migrationjobs.resume`  
`datamigration.migrationjobs.setIamPolicy`  
`datamigration.migrationjobs.start`  
`datamigration.migrationjobs.stop`  
`datamigration.migrationjobs.update`  
`datamigration.migrationjobs.verify`  
`datamigration.operations.cancel`  
`datamigration.operations.delete`  
`datamigration.operations.get`  
`datamigration.operations.list`  
  
Early Access Center  |  Now GA  |  `earlyaccesscenter.campaigns.enroll`  
`earlyaccesscenter.campaigns.get`  
`earlyaccesscenter.campaigns.list`  
`earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
  
Notebooks  |  Added  |  `notebooks.executions.create`  
`notebooks.executions.delete`  
`notebooks.executions.get`  
`notebooks.executions.getIamPolicy`  
`notebooks.executions.list`  
`notebooks.executions.setIamPolicy`  
`notebooks.schedules.create`  
`notebooks.schedules.delete`  
`notebooks.schedules.get`  
`notebooks.schedules.getIamPolicy`  
`notebooks.schedules.list`  
`notebooks.schedules.setIamPolicy`  
  
Notebooks  |  Now GA  |  `notebooks.executions.create`  
`notebooks.executions.delete`  
`notebooks.executions.get`  
`notebooks.executions.getIamPolicy`  
`notebooks.executions.list`  
`notebooks.executions.setIamPolicy`  
`notebooks.schedules.create`  
`notebooks.schedules.delete`  
`notebooks.schedules.get`  
`notebooks.schedules.getIamPolicy`  
`notebooks.schedules.list`  
`notebooks.schedules.setIamPolicy`  
  
  
## Cloud IAM changes as of 2021-02-26

Service | Change | Description  
---|---|---  
Cloud Run functions  |  Role Updated  |  The following permissions have been added to the role `roles/cloudfunctions.serviceAgent` (Cloud Functions Service Agent): `iam.serviceAccounts.actAs`  
  
Cloud TPU  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtpu.serviceAgent` (Cloud TPU V2 API Service Agent): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkViewer` (Compute Network Viewer): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Cloud Data Fusion  |  Role Updated  |  The following permissions have been added to the role `roles/datafusion.serviceAgent` (Cloud Data Fusion API Service Agent): `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Document AI  |  Role Updated  |  The following permissions have been added to the role `roles/documentai.admin` (Cloud DocumentAI Administrator.): `documentai.processorVersions.processBatch`  
`documentai.processorVersions.processOnline`  
`documentai.processorVersions.update`  
  
Document AI  |  Role Updated  |  The following permissions have been added to the role `roles/documentai.apiUser` (Cloud DocumentAI API User): `documentai.processorVersions.processBatch`  
`documentai.processorVersions.processOnline`  
  
Document AI  |  Role Updated  |  The following permissions have been added to the role `roles/documentai.editor` (Cloud DocumentAI Editor): `documentai.processorVersions.processBatch`  
`documentai.processorVersions.processOnline`  
`documentai.processorVersions.update`  
  
Document AI  |  Role Updated  |  The following permissions have been added to the role `roles/documentai.viewer` (Cloud DocumentAI Viewer): `documentai.processorVersions.processBatch`  
`documentai.processorVersions.processOnline`  
  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.attributeDefinitionEditor` (Healthcare Attribute Definition Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.attributeDefinitionReader` (Healthcare Attribute Definition Reader) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentArtifactAdmin` (Healthcare Consent Artifact Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentArtifactEditor` (Healthcare Consent Artifact Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentArtifactReader` (Healthcare Consent Artifact Reader) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentEditor` (Healthcare Consent Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentReader` (Healthcare Consent Reader) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentStoreAdmin` (Healthcare Consent Store Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.consentStoreViewer` (Healthcare Consent Store Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.userDataMappingEditor` (Healthcare User Data Mapping Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.userDataMappingReader` (Healthcare User Data Mapping Reader) is now GA.  
Service Networking  |  Role Updated  |  The following permissions have been added to the role `roles/servicenetworking.serviceAgent` (Service Networking Service Agent): `compute.networks.listPeeringRoutes`  
  
Cloud Billing  |  Supported In Custom Roles  |  `billing.accounts.create`  
`billing.accounts.get`  
`billing.accounts.getIamPolicy`  
`billing.accounts.getPaymentInfo`  
`billing.accounts.list`  
`billing.accounts.move`  
`billing.accounts.removeFromOrganization`  
`billing.accounts.setIamPolicy`  
`billing.accounts.update`  
`billing.accounts.updatePaymentInfo`  
`billing.resourceAssociations.create`  
`billing.resourceAssociations.delete`  
`billing.resourceAssociations.list`  
  
Compute Engine  |  Added  |  `compute.serviceAttachments.create`  
`compute.serviceAttachments.delete`  
`compute.serviceAttachments.get`  
`compute.serviceAttachments.list`  
`compute.serviceAttachments.update`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.serviceAttachments.create`  
`compute.serviceAttachments.delete`  
`compute.serviceAttachments.get`  
`compute.serviceAttachments.list`  
`compute.serviceAttachments.update`  
  
Document AI  |  Added  |  `documentai.evaluations.create`  
`documentai.evaluations.get`  
`documentai.evaluations.list`  
`documentai.processorVersions.processBatch`  
`documentai.processorVersions.processOnline`  
`documentai.processorVersions.update`  
  
Cloud Healthcare API  |  Now GA  |  `healthcare.attributeDefinitions.create`  
`healthcare.attributeDefinitions.delete`  
`healthcare.attributeDefinitions.get`  
`healthcare.attributeDefinitions.list`  
`healthcare.attributeDefinitions.update`  
`healthcare.consentArtifacts.create`  
`healthcare.consentArtifacts.delete`  
`healthcare.consentArtifacts.get`  
`healthcare.consentArtifacts.list`  
`healthcare.consentStores.checkDataAccess`  
`healthcare.consentStores.create`  
`healthcare.consentStores.delete`  
`healthcare.consentStores.evaluateUserConsents`  
`healthcare.consentStores.get`  
`healthcare.consentStores.getIamPolicy`  
`healthcare.consentStores.list`  
`healthcare.consentStores.queryAccessibleData`  
`healthcare.consentStores.setIamPolicy`  
`healthcare.consentStores.update`  
`healthcare.consents.activate`  
`healthcare.consents.create`  
`healthcare.consents.delete`  
`healthcare.consents.get`  
`healthcare.consents.list`  
`healthcare.consents.reject`  
`healthcare.consents.revoke`  
`healthcare.consents.update`  
`healthcare.userDataMappings.archive`  
`healthcare.userDataMappings.create`  
`healthcare.userDataMappings.delete`  
`healthcare.userDataMappings.get`  
`healthcare.userDataMappings.list`  
`healthcare.userDataMappings.update`  
  
Resource Manager  |  Supported In Custom Roles  |  `resourcemanager.projects.createBillingAssignment`  
`resourcemanager.projects.deleteBillingAssignment`  
  
  
## Cloud IAM changes as of 2021-02-19

Service | Change | Description  
---|---|---  
Access Context Manager  |  Role Updated  |  The following permissions have been added to the role `roles/accesscontextmanager.policyAdmin` (Access Context Manager Admin): `cloudasset.assets.searchAllResources`  
  
Access Context Manager  |  Role Updated  |  The following permissions have been added to the role `roles/accesscontextmanager.policyEditor` (Access Context Manager Editor): `cloudasset.assets.searchAllResources`  
  
Cloud Asset Inventory  |  Role Updated  |  The following permissions have been added to the role `roles/cloudasset.owner` (Cloud Asset Owner): `recommender.locations.get`  
`recommender.locations.list`  
  
Cloud Asset Inventory  |  Role Updated  |  The following permissions have been added to the role `roles/cloudasset.viewer` (Cloud Asset Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.hostServiceAgentUser` (Kubernetes Engine Host Service Agent User): `dns.networks.bindPrivateDNSPolicy`  
`dns.networks.bindPrivateDNSZone`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `iam.serviceAccounts.get`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.admin` (Error Reporting Admin): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.user` (Error Reporting User): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.viewer` (Error Reporting Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Media Asset  |  Now GA  |  The role `roles/mediaasset.serviceAgent` (Media Asset Service Agent) is now GA.  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.controlServiceAgent` (Security Center Control Service Agent): `recommender.locations.get`  
`recommender.locations.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.securityHealthAnalyticsServiceAgent` (Security Health Analytics Service Agent): `recommender.locations.get`  
`recommender.locations.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.serviceAgent` (Security Center Service Agent): `recommender.locations.get`  
`recommender.locations.list`  
  
Service Networking  |  Role Updated  |  The following permissions have been added to the role `roles/servicenetworking.serviceAgent` (Service Networking Service Agent): `compute.globalAddresses.list`  
  
Compute Engine  |  Now GA  |  `compute.globalForwardingRules.pscCreate`  
`compute.globalForwardingRules.pscDelete`  
`compute.globalForwardingRules.pscUpdate`  
`compute.nodeGroups.update`  
  
Firebase  |  Added  |  `firebase.clients.list`  
`firebase.clients.update`  
  
Firebase  |  Supported In Custom Roles  |  `firebase.clients.list`  
`firebase.clients.update`  
  
Firebase  |  Now GA  |  `firebase.clients.list`  
`firebase.clients.update`  
  
Policy Simulator  |  Added  |  `policysimulator.replayResults.list`  
`policysimulator.replays.create`  
`policysimulator.replays.get`  
`policysimulator.replays.list`  
`policysimulator.replays.run`  
  
Policy Simulator  |  Supported In Custom Roles  |  `policysimulator.replayResults.list`  
`policysimulator.replays.create`  
`policysimulator.replays.get`  
`policysimulator.replays.list`  
`policysimulator.replays.run`  
  
Pub/Sub  |  Added  |  `pubsub.schemas.attach`  
`pubsub.schemas.create`  
`pubsub.schemas.delete`  
`pubsub.schemas.get`  
`pubsub.schemas.getIamPolicy`  
`pubsub.schemas.list`  
`pubsub.schemas.setIamPolicy`  
`pubsub.schemas.validate`  
  
Recommender  |  Added  |  `recommender.loggingProductSuggestionContainerInsights.get`  
`recommender.loggingProductSuggestionContainerInsights.list`  
`recommender.loggingProductSuggestionContainerInsights.update`  
`recommender.loggingProductSuggestionContainerRecommendations.get`  
`recommender.loggingProductSuggestionContainerRecommendations.list`  
`recommender.loggingProductSuggestionContainerRecommendations.update`  
`recommender.monitoringProductSuggestionComputeInsights.get`  
`recommender.monitoringProductSuggestionComputeInsights.list`  
`recommender.monitoringProductSuggestionComputeInsights.update`  
`recommender.monitoringProductSuggestionComputeRecommendations.get`  
`recommender.monitoringProductSuggestionComputeRecommendations.list`  
`recommender.monitoringProductSuggestionComputeRecommendations.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.loggingProductSuggestionContainerInsights.get`  
`recommender.loggingProductSuggestionContainerInsights.list`  
`recommender.loggingProductSuggestionContainerInsights.update`  
`recommender.loggingProductSuggestionContainerRecommendations.get`  
`recommender.loggingProductSuggestionContainerRecommendations.list`  
`recommender.loggingProductSuggestionContainerRecommendations.update`  
`recommender.monitoringProductSuggestionComputeInsights.get`  
`recommender.monitoringProductSuggestionComputeInsights.list`  
`recommender.monitoringProductSuggestionComputeInsights.update`  
`recommender.monitoringProductSuggestionComputeRecommendations.get`  
`recommender.monitoringProductSuggestionComputeRecommendations.list`  
`recommender.monitoringProductSuggestionComputeRecommendations.update`  
  
Resource Manager  |  Added  |  `resourcemanager.resourceTagBindings.create`  
`resourcemanager.resourceTagBindings.delete`  
`resourcemanager.resourceTagBindings.list`  
`resourcemanager.tagKeys.create`  
`resourcemanager.tagKeys.delete`  
`resourcemanager.tagKeys.get`  
`resourcemanager.tagKeys.getIamPolicy`  
`resourcemanager.tagKeys.list`  
`resourcemanager.tagKeys.setIamPolicy`  
`resourcemanager.tagKeys.update`  
`resourcemanager.tagValueBindings.create`  
`resourcemanager.tagValueBindings.delete`  
`resourcemanager.tagValues.create`  
`resourcemanager.tagValues.delete`  
`resourcemanager.tagValues.get`  
`resourcemanager.tagValues.getIamPolicy`  
`resourcemanager.tagValues.list`  
`resourcemanager.tagValues.setIamPolicy`  
`resourcemanager.tagValues.update`  
  
Resource Manager  |  Supported In Custom Roles  |  `resourcemanager.resourceTagBindings.create`  
`resourcemanager.resourceTagBindings.delete`  
`resourcemanager.resourceTagBindings.list`  
`resourcemanager.tagKeys.create`  
`resourcemanager.tagKeys.delete`  
`resourcemanager.tagKeys.get`  
`resourcemanager.tagKeys.getIamPolicy`  
`resourcemanager.tagKeys.list`  
`resourcemanager.tagKeys.setIamPolicy`  
`resourcemanager.tagKeys.update`  
`resourcemanager.tagValueBindings.create`  
`resourcemanager.tagValueBindings.delete`  
`resourcemanager.tagValues.create`  
`resourcemanager.tagValues.delete`  
`resourcemanager.tagValues.get`  
`resourcemanager.tagValues.getIamPolicy`  
`resourcemanager.tagValues.list`  
`resourcemanager.tagValues.setIamPolicy`  
`resourcemanager.tagValues.update`  
  
  
## Cloud IAM changes as of 2021-01-29

Service | Change | Description  
---|---|---  
Anthos Audit API  |  Now GA  |  The role `roles/anthosaudit.serviceAgent` (Anthos Audit Service Agent) is now GA.  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.developerAdmin` (Apigee Developer Admin): `apigee.apps.get`  
`apigee.apps.list`  
  
Cloud Billing  |  Now GA  |  The role `roles/billing.costsManager` (Billing Account Costs Manager) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.attestorsAdmin` (Binary Authorization Attestor Admin) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.attestorsEditor` (Binary Authorization Attestor Editor) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.attestorsVerifier` (Binary Authorization Attestor Image Verifier) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.attestorsViewer` (Binary Authorization Attestor Viewer) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.policyAdmin` (Binary Authorization Policy Administrator) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.policyEditor` (Binary Authorization Policy Editor) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.policyViewer` (Binary Authorization Policy Viewer) is now GA.  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkViewer` (Compute Network Viewer): `compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
  
Cloud Data Fusion  |  Role Updated  |  The following permissions have been added to the role `roles/datafusion.serviceAgent` (Cloud Data Fusion API Service Agent): `compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.serviceAgent` (GKE Hub Service Agent): `container.customResourceDefinitions.list`  
  
Google Workspace add-ons  |  Now GA  |  The role `roles/gsuiteaddons.developer` (Google Workspace Add-ons Developer) is now GA.  
Google Workspace add-ons  |  Now GA  |  The role `roles/gsuiteaddons.reader` (Google Workspace Add-ons Reader) is now GA.  
Google Workspace add-ons  |  Now GA  |  The role `roles/gsuiteaddons.tester` (Google Workspace Add-ons Tester) is now GA.  
Knative serving  |  Now GA  |  The role `roles/kuberun.eventsControlPlaneServiceAgent` (KubeRun Events Control Plane Service Agent) is now GA.  
Knative serving  |  Now GA  |  The role `roles/kuberun.eventsDataPlaneServiceAgent` (KubeRun Events Data Plane Service Agent) is now GA.  
Memorystore for Memcached  |  Now GA  |  The role `roles/memcache.admin` (Cloud Memorystore Memcached Admin) is now GA.  
Memorystore for Memcached  |  Now GA  |  The role `roles/memcache.editor` (Cloud Memorystore Memcached Editor) is now GA.  
Memorystore for Memcached  |  Now GA  |  The role `roles/memcache.viewer` (Cloud Memorystore Memcached Viewer) is now GA.  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.serviceAgent` (AI Platform Notebooks Service Agent): `ml.jobs.create`  
`ml.jobs.get`  
`ml.jobs.list`  
  
AI Commerce Search API  |  Now GA  |  The role `roles/retail.admin` (Retail Admin) is now GA.  
AI Commerce Search API  |  Now GA  |  The role `roles/retail.editor` (Retail Editor) is now GA.  
AI Commerce Search API  |  Now GA  |  The role `roles/retail.viewer` (Retail Viewer) is now GA.  
Secured Landing Zone  |  Role Updated  |  The following permissions have been added to the role `roles/securedlandingzone.serviceAgent` (Secured Landing Zone Service Agent): `cloudasset.assets.exportOrgPolicy`  
`serviceusage.services.use`  
  
Binary Authorization  |  Now GA  |  `binaryauthorization.attestors.create`  
`binaryauthorization.attestors.delete`  
`binaryauthorization.attestors.get`  
`binaryauthorization.attestors.getIamPolicy`  
`binaryauthorization.attestors.list`  
`binaryauthorization.attestors.setIamPolicy`  
`binaryauthorization.attestors.update`  
`binaryauthorization.attestors.verifyImageAttested`  
`binaryauthorization.policy.get`  
`binaryauthorization.policy.getIamPolicy`  
`binaryauthorization.policy.setIamPolicy`  
`binaryauthorization.policy.update`  
  
Compute Engine  |  Added  |  `compute.commitments.updateReservations`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.commitments.updateReservations`  
  
Compute Engine  |  Now GA  |  `compute.commitments.updateReservations`  
  
Firebase Storage  |  Added  |  `firebasestorage.buckets.addFirebase`  
`firebasestorage.buckets.get`  
`firebasestorage.buckets.list`  
`firebasestorage.buckets.removeFirebase`  
  
Firebase Storage  |  Supported In Custom Roles  |  `firebasestorage.buckets.addFirebase`  
`firebasestorage.buckets.get`  
`firebasestorage.buckets.list`  
`firebasestorage.buckets.removeFirebase`  
  
Google Workspace add-ons  |  Added  |  `gsuiteaddons.authorizations.get`  
`gsuiteaddons.deployments.create`  
`gsuiteaddons.deployments.delete`  
`gsuiteaddons.deployments.execute`  
`gsuiteaddons.deployments.get`  
`gsuiteaddons.deployments.install`  
`gsuiteaddons.deployments.installStatus`  
`gsuiteaddons.deployments.list`  
`gsuiteaddons.deployments.uninstall`  
`gsuiteaddons.deployments.update`  
  
Google Workspace add-ons  |  Supported In Custom Roles  |  `gsuiteaddons.authorizations.get`  
`gsuiteaddons.deployments.create`  
`gsuiteaddons.deployments.delete`  
`gsuiteaddons.deployments.execute`  
`gsuiteaddons.deployments.get`  
`gsuiteaddons.deployments.install`  
`gsuiteaddons.deployments.installStatus`  
`gsuiteaddons.deployments.list`  
`gsuiteaddons.deployments.uninstall`  
`gsuiteaddons.deployments.update`  
  
Google Workspace add-ons  |  Now GA  |  `gsuiteaddons.authorizations.get`  
`gsuiteaddons.deployments.create`  
`gsuiteaddons.deployments.delete`  
`gsuiteaddons.deployments.execute`  
`gsuiteaddons.deployments.get`  
`gsuiteaddons.deployments.install`  
`gsuiteaddons.deployments.installStatus`  
`gsuiteaddons.deployments.list`  
`gsuiteaddons.deployments.uninstall`  
`gsuiteaddons.deployments.update`  
  
Memorystore for Memcached  |  Added  |  `memcache.instances.applySoftwareUpdate`  
  
Memorystore for Memcached  |  Supported In Custom Roles  |  `memcache.instances.applySoftwareUpdate`  
  
Memorystore for Memcached  |  Now GA  |  `memcache.instances.applyParameters`  
`memcache.instances.create`  
`memcache.instances.delete`  
`memcache.instances.get`  
`memcache.instances.list`  
`memcache.instances.update`  
`memcache.instances.updateParameters`  
`memcache.locations.get`  
`memcache.locations.list`  
`memcache.operations.cancel`  
`memcache.operations.delete`  
`memcache.operations.get`  
`memcache.operations.list`  
  
On-Demand Scanning API  |  Added  |  `ondemandscanning.operations.cancel`  
`ondemandscanning.operations.delete`  
`ondemandscanning.operations.get`  
`ondemandscanning.operations.list`  
`ondemandscanning.operations.wait`  
`ondemandscanning.scans.analyzePackages`  
`ondemandscanning.scans.listVulnerabilities`  
`ondemandscanning.scans.scan`  
  
On-Demand Scanning API  |  Supported In Custom Roles  |  `ondemandscanning.operations.cancel`  
`ondemandscanning.operations.delete`  
`ondemandscanning.operations.get`  
`ondemandscanning.operations.list`  
`ondemandscanning.operations.wait`  
`ondemandscanning.scans.analyzePackages`  
`ondemandscanning.scans.listVulnerabilities`  
`ondemandscanning.scans.scan`  
  
Google Cloud Fraud Defense  |  Added  |  `recaptchaenterprise.projectmetadata.get`  
  
AI Commerce Search API  |  Now GA  |  `retail.catalogs.list`  
`retail.catalogs.update`  
`retail.operations.get`  
`retail.operations.list`  
`retail.placements.predict`  
`retail.products.create`  
`retail.products.delete`  
`retail.products.export`  
`retail.products.get`  
`retail.products.import`  
`retail.products.list`  
`retail.products.update`  
`retail.userEvents.create`  
`retail.userEvents.import`  
`retail.userEvents.purge`  
`retail.userEvents.rejoin`  
  
Storage Transfer Service  |  Added  |  `storagetransfer.jobs.run`  
  
Storage Transfer Service  |  Supported In Custom Roles  |  `storagetransfer.jobs.run`  
  
Storage Transfer Service  |  Now GA  |  `storagetransfer.jobs.run`  
  
  
## Cloud IAM changes as of 2021-01-08

Service | Change | Description  
---|---|---  
Apigee  |  Now GA  |  The role `roles/apigee.apiAdmin` (Apigee API Admin) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.apiReader` (Apigee API Reader) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.environmentAdmin` (Apigee Environment Admin) is now GA.  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.admin` (Error Reporting Admin): `stackdriver.projects.get`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.user` (Error Reporting User): `stackdriver.projects.get`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.viewer` (Error Reporting Viewer): `stackdriver.projects.get`  
  
Pub/Sub  |  Role Updated  |  The following permissions have been added to the role `roles/pubsub.serviceAgent` (Cloud Pub/Sub Service Agent): `iam.serviceAccounts.get`  
`iam.serviceAccounts.getAccessToken`  
`iam.serviceAccounts.implicitDelegation`  
`iam.serviceAccounts.list`  
`iam.serviceAccounts.signBlob`  
`iam.serviceAccounts.signJwt`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
AI Commerce Search API  |  Role Updated  |  The following permissions have been added to the role `roles/retail.admin` (Retail Admin): `automlrecommendations.apiKeys.create`  
`automlrecommendations.apiKeys.delete`  
`automlrecommendations.catalogItems.create`  
`automlrecommendations.catalogItems.delete`  
`automlrecommendations.catalogItems.get`  
`automlrecommendations.catalogItems.list`  
`automlrecommendations.catalogItems.update`  
`automlrecommendations.catalogs.getStats`  
`automlrecommendations.catalogs.list`  
`automlrecommendations.catalogs.update`  
`automlrecommendations.eventStores.getStats`  
`automlrecommendations.events.create`  
`automlrecommendations.events.list`  
`automlrecommendations.events.purge`  
`automlrecommendations.events.rejoin`  
`automlrecommendations.placements.create`  
`automlrecommendations.placements.delete`  
`automlrecommendations.placements.getStats`  
`automlrecommendations.placements.list`  
`automlrecommendations.recommendations.create`  
`automlrecommendations.recommendations.delete`  
`automlrecommendations.recommendations.list`  
`automlrecommendations.recommendations.pause`  
`automlrecommendations.recommendations.resume`  
`automlrecommendations.recommendations.update`  
  
AI Commerce Search API  |  Role Updated  |  The following permissions have been added to the role `roles/retail.editor` (Retail Editor): `automlrecommendations.apiKeys.create`  
`automlrecommendations.apiKeys.delete`  
`automlrecommendations.catalogItems.create`  
`automlrecommendations.catalogItems.delete`  
`automlrecommendations.catalogItems.get`  
`automlrecommendations.catalogItems.list`  
`automlrecommendations.catalogItems.update`  
`automlrecommendations.catalogs.getStats`  
`automlrecommendations.catalogs.list`  
`automlrecommendations.catalogs.update`  
`automlrecommendations.eventStores.getStats`  
`automlrecommendations.events.create`  
`automlrecommendations.events.list`  
`automlrecommendations.placements.create`  
`automlrecommendations.placements.delete`  
`automlrecommendations.placements.getStats`  
`automlrecommendations.placements.list`  
`automlrecommendations.recommendations.create`  
`automlrecommendations.recommendations.delete`  
`automlrecommendations.recommendations.list`  
`automlrecommendations.recommendations.pause`  
`automlrecommendations.recommendations.resume`  
`automlrecommendations.recommendations.update`  
  
AI Commerce Search API  |  Role Updated  |  The following permissions have been added to the role `roles/retail.viewer` (Retail Viewer): `automlrecommendations.catalogItems.get`  
`automlrecommendations.catalogItems.list`  
`automlrecommendations.catalogs.getStats`  
`automlrecommendations.catalogs.list`  
`automlrecommendations.eventStores.getStats`  
`automlrecommendations.events.list`  
`automlrecommendations.placements.getStats`  
`automlrecommendations.placements.list`  
`automlrecommendations.recommendations.list`  
  
Cloud Autoscaling  |  Added  |  `autoscaling.sites.getIamPolicy`  
`autoscaling.sites.readRecommendations`  
`autoscaling.sites.setIamPolicy`  
`autoscaling.sites.writeMetrics`  
`autoscaling.sites.writeState`  
  
Cloud Autoscaling  |  Supported In Custom Roles  |  `autoscaling.sites.getIamPolicy`  
`autoscaling.sites.readRecommendations`  
`autoscaling.sites.setIamPolicy`  
`autoscaling.sites.writeMetrics`  
`autoscaling.sites.writeState`  
  
Binary Authorization  |  Added  |  `binaryauthorization.continuousValidationConfig.get`  
`binaryauthorization.continuousValidationConfig.getIamPolicy`  
`binaryauthorization.continuousValidationConfig.setIamPolicy`  
`binaryauthorization.continuousValidationConfig.update`  
  
Binary Authorization  |  Supported In Custom Roles  |  `binaryauthorization.continuousValidationConfig.get`  
`binaryauthorization.continuousValidationConfig.getIamPolicy`  
`binaryauthorization.continuousValidationConfig.setIamPolicy`  
`binaryauthorization.continuousValidationConfig.update`  
  
Compute Engine  |  Added  |  `compute.globalForwardingRules.pscCreate`  
`compute.globalForwardingRules.pscDelete`  
`compute.globalForwardingRules.pscGet`  
`compute.globalForwardingRules.pscUpdate`  
  
Customer Usage Data Processing  |  Added  |  `dataprocessing.datasources.get`  
`dataprocessing.datasources.list`  
`dataprocessing.datasources.update`  
`dataprocessing.groupcontrols.get`  
  
Customer Usage Data Processing  |  Supported In Custom Roles  |  `dataprocessing.datasources.get`  
`dataprocessing.datasources.list`  
`dataprocessing.datasources.update`  
`dataprocessing.groupcontrols.get`  
  
Customer Usage Data Processing  |  Now GA  |  `dataprocessing.datasources.get`  
`dataprocessing.datasources.list`  
`dataprocessing.datasources.update`  
`dataprocessing.groupcontrols.get`  
  
Google Earth Engine  |  Added  |  `earthengine.assets.create`  
`earthengine.assets.delete`  
`earthengine.assets.get`  
`earthengine.assets.getIamPolicy`  
`earthengine.assets.list`  
`earthengine.assets.setIamPolicy`  
`earthengine.assets.update`  
`earthengine.computations.create`  
`earthengine.exports.create`  
`earthengine.filmstripthumbnails.create`  
`earthengine.filmstripthumbnails.get`  
`earthengine.imports.create`  
`earthengine.maps.create`  
`earthengine.maps.get`  
`earthengine.operations.delete`  
`earthengine.operations.get`  
`earthengine.operations.list`  
`earthengine.operations.update`  
`earthengine.tables.create`  
`earthengine.tables.get`  
`earthengine.thumbnails.create`  
`earthengine.thumbnails.get`  
`earthengine.videothumbnails.create`  
`earthengine.videothumbnails.get`  
  
  
## Cloud IAM changes as of 2020-12-18

Service | Change | Description  
---|---|---  
GKE Identity Service  |  Now GA  |  The role `roles/anthosidentityservice.serviceAgent` (Anthos Identity Service Agent) is now GA.  
API Gateway  |  Now GA  |  The role `roles/apigateway.admin` (ApiGateway Admin) is now GA.  
API Gateway  |  Now GA  |  The role `roles/apigateway.viewer` (ApiGateway Viewer) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.portalAdmin` (Apigee Portal Admin) is now GA.  
AutoML  |  Role Updated  |  The following permissions have been added to the role `roles/automl.serviceAgent` (AutoML Service Agent): `bigquery.tables.update`  
  
Service Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/cloudprivatecatalogproducer.orgAdmin` (Catalog Org Admin): `cloudprivatecatalog.targets.get`  
`cloudprivatecatalogproducer.associations.create`  
`cloudprivatecatalogproducer.associations.delete`  
`cloudprivatecatalogproducer.associations.get`  
`cloudprivatecatalogproducer.associations.list`  
`cloudprivatecatalogproducer.catalogAssociations.create`  
`cloudprivatecatalogproducer.catalogAssociations.delete`  
`cloudprivatecatalogproducer.catalogAssociations.get`  
`cloudprivatecatalogproducer.catalogAssociations.list`  
`cloudprivatecatalogproducer.catalogs.create`  
`cloudprivatecatalogproducer.catalogs.delete`  
`cloudprivatecatalogproducer.catalogs.get`  
`cloudprivatecatalogproducer.catalogs.getIamPolicy`  
`cloudprivatecatalogproducer.catalogs.list`  
`cloudprivatecatalogproducer.catalogs.setIamPolicy`  
`cloudprivatecatalogproducer.catalogs.undelete`  
`cloudprivatecatalogproducer.catalogs.update`  
`cloudprivatecatalogproducer.producerCatalogs.attachProduct`  
`cloudprivatecatalogproducer.producerCatalogs.create`  
`cloudprivatecatalogproducer.producerCatalogs.delete`  
`cloudprivatecatalogproducer.producerCatalogs.detachProduct`  
`cloudprivatecatalogproducer.producerCatalogs.get`  
`cloudprivatecatalogproducer.producerCatalogs.getIamPolicy`  
`cloudprivatecatalogproducer.producerCatalogs.list`  
`cloudprivatecatalogproducer.producerCatalogs.setIamPolicy`  
`cloudprivatecatalogproducer.producerCatalogs.update`  
`cloudprivatecatalogproducer.products.create`  
`cloudprivatecatalogproducer.products.delete`  
`cloudprivatecatalogproducer.products.get`  
`cloudprivatecatalogproducer.products.getIamPolicy`  
`cloudprivatecatalogproducer.products.list`  
`cloudprivatecatalogproducer.products.setIamPolicy`  
`cloudprivatecatalogproducer.products.update`  
`cloudprivatecatalogproducer.targets.associate`  
`cloudprivatecatalogproducer.targets.unassociate`  
  
Compute Engine  |  Now GA  |  The role `roles/compute.orgFirewallPolicyAdmin` (Compute Organization Firewall Policy Admin) is now GA.  
Compute Engine  |  Now GA  |  The role `roles/compute.orgFirewallPolicyUser` (Compute Organization Firewall Policy User) is now GA.  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `dns.dnsKeys.get`  
`dns.dnsKeys.list`  
`dns.managedZoneOperations.get`  
`dns.managedZoneOperations.list`  
`dns.managedZones.delete`  
`dns.networks.bindPrivateDNSPolicy`  
`dns.networks.targetWithPeeringZone`  
`dns.policies.create`  
`dns.policies.delete`  
`dns.policies.get`  
`dns.policies.list`  
`dns.policies.update`  
`dns.projects.get`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.admin` (Error Reporting Admin): `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.user` (Error Reporting User): `logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Error Reporting  |  Role Updated  |  The following permissions have been added to the role `roles/errorreporting.viewer` (Error Reporting Viewer): `logging.notificationRules.get`  
`logging.notificationRules.list`  
  
API Gateway  |  Now GA  |  `apigateway.apiconfigs.create`  
`apigateway.apiconfigs.delete`  
`apigateway.apiconfigs.get`  
`apigateway.apiconfigs.getIamPolicy`  
`apigateway.apiconfigs.list`  
`apigateway.apiconfigs.setIamPolicy`  
`apigateway.apiconfigs.update`  
`apigateway.apis.create`  
`apigateway.apis.delete`  
`apigateway.apis.get`  
`apigateway.apis.getIamPolicy`  
`apigateway.apis.list`  
`apigateway.apis.setIamPolicy`  
`apigateway.apis.update`  
`apigateway.gateways.create`  
`apigateway.gateways.delete`  
`apigateway.gateways.get`  
`apigateway.gateways.getIamPolicy`  
`apigateway.gateways.list`  
`apigateway.gateways.setIamPolicy`  
`apigateway.gateways.update`  
`apigateway.locations.get`  
`apigateway.locations.list`  
`apigateway.operations.cancel`  
`apigateway.operations.delete`  
`apigateway.operations.get`  
`apigateway.operations.list`  
  
Apigee  |  Added  |  `apigee.portals.create`  
`apigee.portals.delete`  
`apigee.portals.get`  
`apigee.portals.list`  
`apigee.portals.update`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.portals.create`  
`apigee.portals.delete`  
`apigee.portals.get`  
`apigee.portals.list`  
`apigee.portals.update`  
  
Apigee  |  Now GA  |  `apigee.portals.create`  
`apigee.portals.delete`  
`apigee.portals.get`  
`apigee.portals.list`  
`apigee.portals.update`  
  
Filestore  |  Supported In Custom Roles  |  `file.operations.cancel`  
  
Cloud Logging  |  Added  |  `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Cloud Logging  |  Now GA  |  `logging.notificationRules.create`  
`logging.notificationRules.delete`  
`logging.notificationRules.get`  
`logging.notificationRules.list`  
`logging.notificationRules.update`  
  
Recommender  |  Added  |  `recommender.computeAddressIdleResourceInsights.get`  
`recommender.computeAddressIdleResourceInsights.list`  
`recommender.computeAddressIdleResourceInsights.update`  
`recommender.computeAddressIdleResourceRecommendations.get`  
`recommender.computeAddressIdleResourceRecommendations.list`  
`recommender.computeAddressIdleResourceRecommendations.update`  
`recommender.computeImageIdleResourceInsights.get`  
`recommender.computeImageIdleResourceInsights.list`  
`recommender.computeImageIdleResourceInsights.update`  
`recommender.computeImageIdleResourceRecommendations.get`  
`recommender.computeImageIdleResourceRecommendations.list`  
`recommender.computeImageIdleResourceRecommendations.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.computeAddressIdleResourceInsights.get`  
`recommender.computeAddressIdleResourceInsights.list`  
`recommender.computeAddressIdleResourceInsights.update`  
`recommender.computeAddressIdleResourceRecommendations.get`  
`recommender.computeAddressIdleResourceRecommendations.list`  
`recommender.computeAddressIdleResourceRecommendations.update`  
`recommender.computeImageIdleResourceInsights.get`  
`recommender.computeImageIdleResourceInsights.list`  
`recommender.computeImageIdleResourceInsights.update`  
`recommender.computeImageIdleResourceRecommendations.get`  
`recommender.computeImageIdleResourceRecommendations.list`  
`recommender.computeImageIdleResourceRecommendations.update`  
  
Recommender  |  Now GA  |  `recommender.computeAddressIdleResourceInsights.get`  
`recommender.computeAddressIdleResourceInsights.list`  
`recommender.computeAddressIdleResourceInsights.update`  
`recommender.computeAddressIdleResourceRecommendations.get`  
`recommender.computeAddressIdleResourceRecommendations.list`  
`recommender.computeAddressIdleResourceRecommendations.update`  
`recommender.computeImageIdleResourceInsights.get`  
`recommender.computeImageIdleResourceInsights.list`  
`recommender.computeImageIdleResourceInsights.update`  
`recommender.computeImageIdleResourceRecommendations.get`  
`recommender.computeImageIdleResourceRecommendations.list`  
`recommender.computeImageIdleResourceRecommendations.update`  
  
AI Commerce Search API  |  Added  |  `retail.catalogs.list`  
`retail.catalogs.update`  
`retail.operations.get`  
`retail.operations.list`  
`retail.placements.predict`  
`retail.products.create`  
`retail.products.delete`  
`retail.products.export`  
`retail.products.get`  
`retail.products.import`  
`retail.products.list`  
`retail.products.update`  
`retail.userEvents.create`  
`retail.userEvents.import`  
`retail.userEvents.purge`  
`retail.userEvents.rejoin`  
  
AI Commerce Search API  |  Supported In Custom Roles  |  `retail.catalogs.list`  
`retail.catalogs.update`  
`retail.operations.get`  
`retail.operations.list`  
`retail.placements.predict`  
`retail.products.create`  
`retail.products.delete`  
`retail.products.export`  
`retail.products.get`  
`retail.products.import`  
`retail.products.list`  
`retail.products.update`  
`retail.userEvents.create`  
`retail.userEvents.import`  
`retail.userEvents.purge`  
`retail.userEvents.rejoin`  
  
  
## Cloud IAM changes as of 2020-12-11

Service | Change | Description  
---|---|---  
Cloud TPU  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtpu.serviceAgent` (Cloud TPU V2 API Service Agent): `compute.firewallPolicies.get`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.use`  
  
Managed Service for Apache Airflow  |  Now GA  |  The role `roles/composer.sharedVpcAgent` (Composer Shared VPC Agent) is now GA.  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.serviceAgent` (Cloud Composer API Service Agent): `compute.firewallPolicies.get`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.use`  
`container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.worker` (Composer Worker): `container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Compute Engine  |  Now GA  |  The role `roles/compute.orgSecurityPolicyAdmin` (Compute Organization Security Policy Admin) is now GA.  
Compute Engine  |  Now GA  |  The role `roles/compute.orgSecurityPolicyUser` (Compute Organization Security Policy User) is now GA.  
Compute Engine  |  Now GA  |  The role `roles/compute.orgSecurityResourceAdmin` (Compute Organization Resource Admin) is now GA.  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.admin` (Compute Admin): `compute.firewallPolicies.cloneRules`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `compute.firewallPolicies.get`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.use`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityPolicyAdmin` (Compute Organization Security Policy Admin): `compute.firewallPolicies.cloneRules`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.securityAdmin` (Compute Security Admin): `compute.firewallPolicies.addAssociation`  
`compute.firewallPolicies.cloneRules`  
`compute.firewallPolicies.copyRules`  
`compute.firewallPolicies.create`  
`compute.firewallPolicies.delete`  
`compute.firewallPolicies.get`  
`compute.firewallPolicies.getIamPolicy`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.move`  
`compute.firewallPolicies.removeAssociation`  
`compute.firewallPolicies.setIamPolicy`  
`compute.firewallPolicies.update`  
`compute.firewallPolicies.use`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.serviceAgent` (Compute Engine Service Agent): `cloudnotifications.activities.list`  
`compute.instanceGroupManagers.get`  
`monitoring.alertPolicies.get`  
`monitoring.alertPolicies.list`  
`monitoring.dashboards.get`  
`monitoring.dashboards.list`  
`monitoring.groups.get`  
`monitoring.groups.list`  
`monitoring.metricDescriptors.get`  
`monitoring.metricDescriptors.list`  
`monitoring.monitoredResourceDescriptors.get`  
`monitoring.monitoredResourceDescriptors.list`  
`monitoring.notificationChannelDescriptors.get`  
`monitoring.notificationChannelDescriptors.list`  
`monitoring.notificationChannels.get`  
`monitoring.notificationChannels.list`  
`monitoring.publicWidgets.get`  
`monitoring.publicWidgets.list`  
`monitoring.services.get`  
`monitoring.services.list`  
`monitoring.slos.get`  
`monitoring.slos.list`  
`monitoring.timeSeries.list`  
`monitoring.uptimeCheckConfigs.get`  
`monitoring.uptimeCheckConfigs.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`stackdriver.projects.get`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.admin` (Kubernetes Engine Admin): `container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.developer` (Kubernetes Engine Developer): `container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.serviceAgent` (Kubernetes Engine Service Agent): `compute.firewallPolicies.addAssociation`  
`compute.firewallPolicies.cloneRules`  
`compute.firewallPolicies.copyRules`  
`compute.firewallPolicies.create`  
`compute.firewallPolicies.delete`  
`compute.firewallPolicies.get`  
`compute.firewallPolicies.getIamPolicy`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.move`  
`compute.firewallPolicies.removeAssociation`  
`compute.firewallPolicies.setIamPolicy`  
`compute.firewallPolicies.update`  
`compute.firewallPolicies.use`  
`container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Google Kubernetes Engine  |  Role Updated  |  The following permissions have been added to the role `roles/container.viewer` (Kubernetes Engine Viewer): `container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.storageStates.get`  
`container.storageStates.list`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.list`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.list`  
  
Container Threat Detection  |  Role Updated  |  The following permissions have been added to the role `roles/containerthreatdetection.serviceAgent` (Container Threat Detection Service Agent): `container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.roleBindings.create`  
`container.roleBindings.delete`  
`container.roleBindings.update`  
`container.storageStates.get`  
`container.storageStates.list`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.list`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.list`  
  
Dataflow  |  Role Updated  |  The following permissions have been added to the role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent): `compute.firewallPolicies.get`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.use`  
  
Managed Service for Apache Spark  |  Now GA  |  The role `roles/dataproc.hubAgent` (Dataproc Hub Agent) is now GA.  
Early Access Center  |  Role Updated  |  The following permissions have been added to the role `roles/earlyaccesscenter.admin` (Early Access Center Administrator): `earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
  
Early Access Center  |  Role Updated  |  The following permissions have been added to the role `roles/earlyaccesscenter.viewer` (Early Access Center Viewer): `earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `compute.firewallPolicies.cloneRules`  
`container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
`earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
`metastore.services.export`  
  
Game Servers  |  Role Updated  |  The following permissions have been added to the role `roles/gameservices.serviceAgent` (Game Services Service Agent): `container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityAdmin` (Security Admin): `container.endpointSlices.list`  
`container.frontendConfigs.list`  
`container.storageStates.list`  
`container.storageVersionMigrations.list`  
`container.updateInfos.list`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.list`  
`earlyaccesscenter.customerAllowlists.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityReviewer` (Security Reviewer): `container.endpointSlices.list`  
`container.frontendConfigs.list`  
`container.storageStates.list`  
`container.storageVersionMigrations.list`  
`container.updateInfos.list`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.list`  
`earlyaccesscenter.customerAllowlists.list`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.viewer` (Logs Viewer): `logging.views.get`  
`logging.views.list`  
  
Dataproc Metastore  |  Role Added  |  The role `roles/metastore.metadataOperator` (Dataproc Metastore Metadata Operator) has been added with the following permissions: `metastore.imports.create`  
`metastore.imports.delete`  
`metastore.imports.get`  
`metastore.imports.list`  
`metastore.imports.update`  
`metastore.locations.get`  
`metastore.locations.list`  
`metastore.operations.get`  
`metastore.operations.list`  
`metastore.services.export`  
`metastore.services.get`  
`metastore.services.getIamPolicy`  
`metastore.services.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.legacyAdmin` (Notebooks Legacy Admin): `compute.firewallPolicies.cloneRules`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `compute.firewallPolicies.cloneRules`  
`container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
`earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
`metastore.services.export`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.controlServiceAgent` (Security Center Control Service Agent): `container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.storageStates.get`  
`container.storageStates.list`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.list`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.list`  
`logging.views.get`  
`logging.views.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.securityHealthAnalyticsServiceAgent` (Security Health Analytics Service Agent): `logging.views.get`  
`logging.views.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.serviceAgent` (Security Center Service Agent): `container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.storageStates.get`  
`container.storageStates.list`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.list`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.list`  
`logging.views.get`  
`logging.views.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
`metastore.services.export`  
  
Apigee  |  Added  |  `apigee.organizations.delete`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.organizations.delete`  
  
Apigee  |  Now GA  |  `apigee.organizations.delete`  
  
Compute Engine  |  Added  |  `compute.firewallPolicies.addAssociation`  
`compute.firewallPolicies.cloneRules`  
`compute.firewallPolicies.copyRules`  
`compute.firewallPolicies.create`  
`compute.firewallPolicies.delete`  
`compute.firewallPolicies.get`  
`compute.firewallPolicies.getIamPolicy`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.move`  
`compute.firewallPolicies.removeAssociation`  
`compute.firewallPolicies.setIamPolicy`  
`compute.firewallPolicies.update`  
`compute.firewallPolicies.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.firewallPolicies.addAssociation`  
`compute.firewallPolicies.copyRules`  
`compute.firewallPolicies.create`  
`compute.firewallPolicies.delete`  
`compute.firewallPolicies.get`  
`compute.firewallPolicies.getIamPolicy`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.move`  
`compute.firewallPolicies.removeAssociation`  
`compute.firewallPolicies.setIamPolicy`  
`compute.firewallPolicies.update`  
`compute.firewallPolicies.use`  
  
Compute Engine  |  Now GA  |  `compute.firewallPolicies.addAssociation`  
`compute.firewallPolicies.copyRules`  
`compute.firewallPolicies.create`  
`compute.firewallPolicies.delete`  
`compute.firewallPolicies.get`  
`compute.firewallPolicies.getIamPolicy`  
`compute.firewallPolicies.list`  
`compute.firewallPolicies.move`  
`compute.firewallPolicies.removeAssociation`  
`compute.firewallPolicies.setIamPolicy`  
`compute.firewallPolicies.update`  
`compute.firewallPolicies.use`  
  
Google Kubernetes Engine  |  Added  |  `container.apiServices.getStatus`  
`container.auditSinks.create`  
`container.auditSinks.delete`  
`container.auditSinks.get`  
`container.auditSinks.list`  
`container.auditSinks.update`  
`container.certificateSigningRequests.getStatus`  
`container.clusterRoles.escalate`  
`container.csiNodeInfos.create`  
`container.csiNodeInfos.delete`  
`container.csiNodeInfos.get`  
`container.csiNodeInfos.list`  
`container.csiNodeInfos.update`  
`container.customResourceDefinitions.getStatus`  
`container.endpointSlices.create`  
`container.endpointSlices.delete`  
`container.endpointSlices.get`  
`container.endpointSlices.list`  
`container.endpointSlices.update`  
`container.frontendConfigs.create`  
`container.frontendConfigs.delete`  
`container.frontendConfigs.get`  
`container.frontendConfigs.list`  
`container.frontendConfigs.update`  
`container.leases.create`  
`container.leases.delete`  
`container.leases.get`  
`container.leases.list`  
`container.leases.update`  
`container.managedCertificates.create`  
`container.managedCertificates.delete`  
`container.managedCertificates.get`  
`container.managedCertificates.list`  
`container.managedCertificates.update`  
`container.mutatingWebhookConfigurations.create`  
`container.mutatingWebhookConfigurations.delete`  
`container.mutatingWebhookConfigurations.get`  
`container.mutatingWebhookConfigurations.list`  
`container.mutatingWebhookConfigurations.update`  
`container.namespaces.finalize`  
`container.priorityClasses.create`  
`container.priorityClasses.delete`  
`container.priorityClasses.get`  
`container.priorityClasses.list`  
`container.priorityClasses.update`  
`container.roles.escalate`  
`container.selfSubjectRulesReviews.create`  
`container.serviceAccounts.createToken`  
`container.storageStates.create`  
`container.storageStates.delete`  
`container.storageStates.get`  
`container.storageStates.getStatus`  
`container.storageStates.list`  
`container.storageStates.update`  
`container.storageStates.updateStatus`  
`container.storageVersionMigrations.create`  
`container.storageVersionMigrations.delete`  
`container.storageVersionMigrations.get`  
`container.storageVersionMigrations.getStatus`  
`container.storageVersionMigrations.list`  
`container.storageVersionMigrations.update`  
`container.storageVersionMigrations.updateStatus`  
`container.updateInfos.create`  
`container.updateInfos.delete`  
`container.updateInfos.get`  
`container.updateInfos.list`  
`container.updateInfos.update`  
`container.validatingWebhookConfigurations.create`  
`container.validatingWebhookConfigurations.delete`  
`container.validatingWebhookConfigurations.get`  
`container.validatingWebhookConfigurations.list`  
`container.validatingWebhookConfigurations.update`  
`container.volumeAttachments.create`  
`container.volumeAttachments.delete`  
`container.volumeAttachments.get`  
`container.volumeAttachments.getStatus`  
`container.volumeAttachments.list`  
`container.volumeAttachments.update`  
`container.volumeAttachments.updateStatus`  
`container.volumeSnapshotClasses.create`  
`container.volumeSnapshotClasses.delete`  
`container.volumeSnapshotClasses.get`  
`container.volumeSnapshotClasses.list`  
`container.volumeSnapshotClasses.update`  
`container.volumeSnapshotContents.create`  
`container.volumeSnapshotContents.delete`  
`container.volumeSnapshotContents.get`  
`container.volumeSnapshotContents.getStatus`  
`container.volumeSnapshotContents.list`  
`container.volumeSnapshotContents.update`  
`container.volumeSnapshotContents.updateStatus`  
`container.volumeSnapshots.create`  
`container.volumeSnapshots.delete`  
`container.volumeSnapshots.get`  
`container.volumeSnapshots.getStatus`  
`container.volumeSnapshots.list`  
`container.volumeSnapshots.update`  
`container.volumeSnapshots.updateStatus`  
  
Managed Service for Apache Spark  |  Added  |  `dataproc.clusters.start`  
`dataproc.clusters.stop`  
  
Managed Service for Apache Spark  |  Now GA  |  `dataproc.clusters.start`  
`dataproc.clusters.stop`  
  
Early Access Center  |  Added  |  `earlyaccesscenter.customerAllowlists.get`  
`earlyaccesscenter.customerAllowlists.list`  
  
Cloud Logging  |  Added  |  `logging.views.create`  
`logging.views.delete`  
`logging.views.get`  
`logging.views.list`  
`logging.views.listLogs`  
`logging.views.listResourceKeys`  
`logging.views.listResourceValues`  
`logging.views.update`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.views.create`  
`logging.views.delete`  
`logging.views.get`  
`logging.views.list`  
`logging.views.listLogs`  
`logging.views.listResourceKeys`  
`logging.views.listResourceValues`  
`logging.views.update`  
  
Cloud Logging  |  Now GA  |  `logging.views.create`  
`logging.views.delete`  
`logging.views.get`  
`logging.views.list`  
`logging.views.listLogs`  
`logging.views.listResourceKeys`  
`logging.views.listResourceValues`  
`logging.views.update`  
  
Dataproc Metastore  |  Added  |  `metastore.imports.create`  
`metastore.imports.get`  
`metastore.imports.list`  
`metastore.imports.update`  
`metastore.locations.get`  
`metastore.locations.list`  
`metastore.operations.cancel`  
`metastore.operations.delete`  
`metastore.operations.get`  
`metastore.operations.list`  
`metastore.services.create`  
`metastore.services.delete`  
`metastore.services.export`  
`metastore.services.get`  
`metastore.services.getIamPolicy`  
`metastore.services.list`  
`metastore.services.setIamPolicy`  
`metastore.services.update`  
  
Dataproc Metastore  |  Supported In Custom Roles  |  `metastore.imports.create`  
`metastore.imports.get`  
`metastore.imports.list`  
`metastore.imports.update`  
`metastore.locations.get`  
`metastore.locations.list`  
`metastore.operations.cancel`  
`metastore.operations.delete`  
`metastore.operations.get`  
`metastore.operations.list`  
`metastore.services.create`  
`metastore.services.delete`  
`metastore.services.get`  
`metastore.services.getIamPolicy`  
`metastore.services.list`  
`metastore.services.setIamPolicy`  
`metastore.services.update`  
  
  
## Cloud IAM changes as of 2020-11-20

Service | Change | Description  
---|---|---  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.analyticsEditor` (Apigee Analytics Editor): `apigee.envgroupattachments.get`  
`apigee.envgroupattachments.list`  
`apigee.envgroups.get`  
`apigee.envgroups.list`  
`apigee.environments.list`  
  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.analyticsViewer` (Apigee Analytics Viewer): `apigee.envgroupattachments.get`  
`apigee.envgroupattachments.list`  
`apigee.envgroups.get`  
`apigee.envgroups.list`  
`apigee.environments.get`  
`apigee.environments.list`  
  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.apiCreator` (Apigee API Creator): `apigee.proxyrevisions.deploy`  
`apigee.proxyrevisions.undeploy`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been removed from the role `roles/logging.privateLogViewer` (Private Logs Viewer): `logging.views.access`  
  
Dell EMC Cloud OneFS  |  Added  |  `cloudonefs.isiloncloud.com/clusters.create`  
`cloudonefs.isiloncloud.com/clusters.delete`  
`cloudonefs.isiloncloud.com/clusters.get`  
`cloudonefs.isiloncloud.com/clusters.list`  
`cloudonefs.isiloncloud.com/clusters.update`  
`cloudonefs.isiloncloud.com/clusters.updateAdvancedSettings`  
`cloudonefs.isiloncloud.com/fileshares.create`  
`cloudonefs.isiloncloud.com/fileshares.delete`  
`cloudonefs.isiloncloud.com/fileshares.get`  
`cloudonefs.isiloncloud.com/fileshares.list`  
`cloudonefs.isiloncloud.com/fileshares.update`  
  
Service Catalog  |  Added  |  `cloudprivatecatalogproducer.catalogAssociations.create`  
`cloudprivatecatalogproducer.catalogAssociations.delete`  
`cloudprivatecatalogproducer.catalogAssociations.get`  
`cloudprivatecatalogproducer.catalogAssociations.list`  
`cloudprivatecatalogproducer.producerCatalogs.attachProduct`  
`cloudprivatecatalogproducer.producerCatalogs.create`  
`cloudprivatecatalogproducer.producerCatalogs.delete`  
`cloudprivatecatalogproducer.producerCatalogs.detachProduct`  
`cloudprivatecatalogproducer.producerCatalogs.get`  
`cloudprivatecatalogproducer.producerCatalogs.getIamPolicy`  
`cloudprivatecatalogproducer.producerCatalogs.list`  
`cloudprivatecatalogproducer.producerCatalogs.setIamPolicy`  
`cloudprivatecatalogproducer.producerCatalogs.update`  
`cloudprivatecatalogproducer.products.create`  
`cloudprivatecatalogproducer.products.delete`  
`cloudprivatecatalogproducer.products.get`  
`cloudprivatecatalogproducer.products.getIamPolicy`  
`cloudprivatecatalogproducer.products.list`  
`cloudprivatecatalogproducer.products.setIamPolicy`  
`cloudprivatecatalogproducer.products.update`  
`cloudprivatecatalogproducer.settings.get`  
`cloudprivatecatalogproducer.settings.update`  
  
  
## Cloud IAM changes as of 2020-11-06

Service | Change | Description  
---|---|---  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.conversationManager` (Dialogflow Conversation Manager) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.integrationManager` (Dialogflow Integration Manager) is now GA.  
Service Management  |  Now GA  |  The role `roles/servicemanagement.reporter` (Service Reporter) is now GA.  
Compute Engine  |  Added  |  `compute.globalForwardingRules.update`  
`compute.globalNetworkEndpointGroups.attachNetworkEndpoints`  
`compute.globalNetworkEndpointGroups.create`  
`compute.globalNetworkEndpointGroups.delete`  
`compute.globalNetworkEndpointGroups.detachNetworkEndpoints`  
`compute.globalNetworkEndpointGroups.get`  
`compute.globalNetworkEndpointGroups.list`  
`compute.globalNetworkEndpointGroups.use`  
`compute.regionHealthChecks.create`  
`compute.regionHealthChecks.delete`  
`compute.regionHealthChecks.get`  
`compute.regionHealthChecks.list`  
`compute.regionHealthChecks.update`  
`compute.regionHealthChecks.use`  
`compute.regionHealthChecks.useReadOnly`  
`compute.regionNetworkEndpointGroups.create`  
`compute.regionNetworkEndpointGroups.delete`  
`compute.regionNetworkEndpointGroups.get`  
`compute.regionNetworkEndpointGroups.list`  
`compute.regionNetworkEndpointGroups.use`  
`compute.regionSslCertificates.create`  
`compute.regionSslCertificates.delete`  
`compute.regionSslCertificates.get`  
`compute.regionSslCertificates.list`  
`compute.regionTargetHttpProxies.create`  
`compute.regionTargetHttpProxies.delete`  
`compute.regionTargetHttpProxies.get`  
`compute.regionTargetHttpProxies.list`  
`compute.regionTargetHttpProxies.setUrlMap`  
`compute.regionTargetHttpProxies.use`  
`compute.regionTargetHttpsProxies.create`  
`compute.regionTargetHttpsProxies.delete`  
`compute.regionTargetHttpsProxies.get`  
`compute.regionTargetHttpsProxies.list`  
`compute.regionTargetHttpsProxies.setSslCertificates`  
`compute.regionTargetHttpsProxies.setUrlMap`  
`compute.regionTargetHttpsProxies.use`  
`compute.regionUrlMaps.create`  
`compute.regionUrlMaps.delete`  
`compute.regionUrlMaps.get`  
`compute.regionUrlMaps.invalidateCache`  
`compute.regionUrlMaps.list`  
`compute.regionUrlMaps.update`  
`compute.regionUrlMaps.use`  
`compute.regionUrlMaps.validate`  
`compute.targetGrpcProxies.create`  
`compute.targetGrpcProxies.delete`  
`compute.targetGrpcProxies.get`  
`compute.targetGrpcProxies.list`  
`compute.targetGrpcProxies.update`  
`compute.targetGrpcProxies.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.globalForwardingRules.update`  
`compute.globalNetworkEndpointGroups.attachNetworkEndpoints`  
`compute.globalNetworkEndpointGroups.create`  
`compute.globalNetworkEndpointGroups.delete`  
`compute.globalNetworkEndpointGroups.detachNetworkEndpoints`  
`compute.globalNetworkEndpointGroups.get`  
`compute.globalNetworkEndpointGroups.list`  
`compute.globalNetworkEndpointGroups.use`  
`compute.regionHealthChecks.create`  
`compute.regionHealthChecks.delete`  
`compute.regionHealthChecks.get`  
`compute.regionHealthChecks.list`  
`compute.regionHealthChecks.update`  
`compute.regionHealthChecks.use`  
`compute.regionHealthChecks.useReadOnly`  
`compute.regionNetworkEndpointGroups.create`  
`compute.regionNetworkEndpointGroups.delete`  
`compute.regionNetworkEndpointGroups.get`  
`compute.regionNetworkEndpointGroups.list`  
`compute.regionNetworkEndpointGroups.use`  
`compute.regionSslCertificates.create`  
`compute.regionSslCertificates.delete`  
`compute.regionSslCertificates.get`  
`compute.regionSslCertificates.list`  
`compute.regionTargetHttpProxies.create`  
`compute.regionTargetHttpProxies.delete`  
`compute.regionTargetHttpProxies.get`  
`compute.regionTargetHttpProxies.list`  
`compute.regionTargetHttpProxies.setUrlMap`  
`compute.regionTargetHttpProxies.use`  
`compute.regionTargetHttpsProxies.create`  
`compute.regionTargetHttpsProxies.delete`  
`compute.regionTargetHttpsProxies.get`  
`compute.regionTargetHttpsProxies.list`  
`compute.regionTargetHttpsProxies.setSslCertificates`  
`compute.regionTargetHttpsProxies.setUrlMap`  
`compute.regionTargetHttpsProxies.use`  
`compute.regionUrlMaps.create`  
`compute.regionUrlMaps.delete`  
`compute.regionUrlMaps.get`  
`compute.regionUrlMaps.invalidateCache`  
`compute.regionUrlMaps.list`  
`compute.regionUrlMaps.update`  
`compute.regionUrlMaps.use`  
`compute.regionUrlMaps.validate`  
`compute.targetGrpcProxies.create`  
`compute.targetGrpcProxies.delete`  
`compute.targetGrpcProxies.get`  
`compute.targetGrpcProxies.list`  
`compute.targetGrpcProxies.update`  
`compute.targetGrpcProxies.use`  
  
Compute Engine  |  Now GA  |  `compute.globalForwardingRules.update`  
`compute.globalNetworkEndpointGroups.attachNetworkEndpoints`  
`compute.globalNetworkEndpointGroups.create`  
`compute.globalNetworkEndpointGroups.delete`  
`compute.globalNetworkEndpointGroups.detachNetworkEndpoints`  
`compute.globalNetworkEndpointGroups.get`  
`compute.globalNetworkEndpointGroups.list`  
`compute.globalNetworkEndpointGroups.use`  
`compute.regionHealthChecks.create`  
`compute.regionHealthChecks.delete`  
`compute.regionHealthChecks.get`  
`compute.regionHealthChecks.list`  
`compute.regionHealthChecks.update`  
`compute.regionHealthChecks.use`  
`compute.regionHealthChecks.useReadOnly`  
`compute.regionNetworkEndpointGroups.create`  
`compute.regionNetworkEndpointGroups.delete`  
`compute.regionNetworkEndpointGroups.get`  
`compute.regionNetworkEndpointGroups.list`  
`compute.regionNetworkEndpointGroups.use`  
`compute.regionSslCertificates.create`  
`compute.regionSslCertificates.delete`  
`compute.regionSslCertificates.get`  
`compute.regionSslCertificates.list`  
`compute.regionTargetHttpProxies.create`  
`compute.regionTargetHttpProxies.delete`  
`compute.regionTargetHttpProxies.get`  
`compute.regionTargetHttpProxies.list`  
`compute.regionTargetHttpProxies.setUrlMap`  
`compute.regionTargetHttpProxies.use`  
`compute.regionTargetHttpsProxies.create`  
`compute.regionTargetHttpsProxies.delete`  
`compute.regionTargetHttpsProxies.get`  
`compute.regionTargetHttpsProxies.list`  
`compute.regionTargetHttpsProxies.setSslCertificates`  
`compute.regionTargetHttpsProxies.setUrlMap`  
`compute.regionTargetHttpsProxies.use`  
`compute.regionUrlMaps.create`  
`compute.regionUrlMaps.delete`  
`compute.regionUrlMaps.get`  
`compute.regionUrlMaps.invalidateCache`  
`compute.regionUrlMaps.list`  
`compute.regionUrlMaps.update`  
`compute.regionUrlMaps.use`  
`compute.regionUrlMaps.validate`  
`compute.targetGrpcProxies.create`  
`compute.targetGrpcProxies.delete`  
`compute.targetGrpcProxies.get`  
`compute.targetGrpcProxies.list`  
`compute.targetGrpcProxies.update`  
`compute.targetGrpcProxies.use`  
  
Document AI  |  Added  |  `documentai.humanReviewConfigs.get`  
`documentai.humanReviewConfigs.review`  
`documentai.humanReviewConfigs.update`  
`documentai.labelerPools.create`  
`documentai.labelerPools.delete`  
`documentai.labelerPools.get`  
`documentai.labelerPools.list`  
`documentai.labelerPools.update`  
`documentai.locations.get`  
`documentai.locations.list`  
`documentai.operations.getLegacy`  
`documentai.processorTypes.list`  
`documentai.processorVersions.create`  
`documentai.processorVersions.delete`  
`documentai.processorVersions.get`  
`documentai.processorVersions.list`  
`documentai.processors.create`  
`documentai.processors.delete`  
`documentai.processors.fetchHumanReviewDetails`  
`documentai.processors.get`  
`documentai.processors.list`  
`documentai.processors.processBatch`  
`documentai.processors.processOnline`  
`documentai.processors.update`  
  
Cloud Logging  |  Added  |  `logging.logEntries.download`  
  
Cloud Logging  |  Now GA  |  `logging.logEntries.download`  
  
  
## Cloud IAM changes as of 2020-10-30

Service | Change | Description  
---|---|---  
Compute Engine  |  Added  |  `compute.forwardingRules.update`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.forwardingRules.update`  
  
Compute Engine  |  Now GA  |  `compute.forwardingRules.update`  
  
Early Access Center  |  Added  |  `earlyaccesscenter.campaigns.enroll`  
`earlyaccesscenter.campaigns.get`  
`earlyaccesscenter.campaigns.list`  
`earlyaccesscenter.customerWhitelists.get`  
`earlyaccesscenter.customerWhitelists.list`  
  
Early Access Center  |  Supported In Custom Roles  |  `earlyaccesscenter.campaigns.enroll`  
`earlyaccesscenter.campaigns.get`  
`earlyaccesscenter.campaigns.list`  
`earlyaccesscenter.customerWhitelists.get`  
`earlyaccesscenter.customerWhitelists.list`  
  
GKE Hub  |  Added  |  `gkehub.operations.delete`  
  
GKE Hub  |  Now GA  |  `gkehub.operations.delete`  
  
Cloud Logging  |  Added  |  `logging.locations.get`  
`logging.locations.list`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.locations.get`  
`logging.locations.list`  
  
Cloud Logging  |  Now GA  |  `logging.locations.get`  
`logging.locations.list`  
  
Notebooks  |  Added  |  `notebooks.instances.use`  
  
Notebooks  |  Now GA  |  `notebooks.instances.use`  
  
  
## Cloud IAM changes as of 2020-10-23

Service | Change | Description  
---|---|---  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.serviceAgent` (Dialogflow Service Agent): `cloudfunctions.functions.invoke`  
  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.serviceAgent` (GKE Hub Service Agent): `container.clusterRoles.bind`  
  
Pub/Sub Lite  |  Now GA  |  The role `roles/pubsublite.admin` (Pub/Sub Lite Admin) is now GA.  
Pub/Sub Lite  |  Now GA  |  The role `roles/pubsublite.editor` (Pub/Sub Lite Editor) is now GA.  
Pub/Sub Lite  |  Now GA  |  The role `roles/pubsublite.publisher` (Pub/Sub Lite Publisher) is now GA.  
Pub/Sub Lite  |  Now GA  |  The role `roles/pubsublite.subscriber` (Pub/Sub Lite Subscriber) is now GA.  
Pub/Sub Lite  |  Now GA  |  The role `roles/pubsublite.viewer` (Pub/Sub Lite Viewer) is now GA.  
Service Networking  |  Role Updated  |  The following permissions have been added to the role `roles/servicenetworking.serviceAgent` (Service Networking Service Agent): `compute.networks.updatePeering`  
  
Compute Engine  |  Added  |  `compute.instances.useReadOnly`  
`compute.machineImages.create`  
`compute.machineImages.delete`  
`compute.machineImages.get`  
`compute.machineImages.getIamPolicy`  
`compute.machineImages.list`  
`compute.machineImages.setIamPolicy`  
`compute.machineImages.useReadOnly`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.useReadOnly`  
`compute.machineImages.create`  
`compute.machineImages.delete`  
`compute.machineImages.get`  
`compute.machineImages.getIamPolicy`  
`compute.machineImages.list`  
`compute.machineImages.setIamPolicy`  
`compute.machineImages.useReadOnly`  
  
Compute Engine  |  Now GA  |  `compute.instances.useReadOnly`  
  
Database Migration Service  |  Added  |  `datamigration.connectionprofiles.create`  
`datamigration.connectionprofiles.delete`  
`datamigration.connectionprofiles.get`  
`datamigration.connectionprofiles.getIamPolicy`  
`datamigration.connectionprofiles.list`  
`datamigration.connectionprofiles.setIamPolicy`  
`datamigration.connectionprofiles.update`  
`datamigration.locations.get`  
`datamigration.locations.list`  
`datamigration.migrationjobs.create`  
`datamigration.migrationjobs.delete`  
`datamigration.migrationjobs.generateSshScript`  
`datamigration.migrationjobs.get`  
`datamigration.migrationjobs.getIamPolicy`  
`datamigration.migrationjobs.list`  
`datamigration.migrationjobs.promote`  
`datamigration.migrationjobs.restart`  
`datamigration.migrationjobs.resume`  
`datamigration.migrationjobs.setIamPolicy`  
`datamigration.migrationjobs.start`  
`datamigration.migrationjobs.stop`  
`datamigration.migrationjobs.update`  
`datamigration.migrationjobs.verify`  
`datamigration.operations.cancel`  
`datamigration.operations.delete`  
`datamigration.operations.get`  
`datamigration.operations.list`  
  
Cloud Healthcare API  |  Added  |  `healthcare.nlpservice.analyzeEntities`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.locations.get`  
`healthcare.locations.list`  
`healthcare.nlpservice.analyzeEntities`  
  
Pub/Sub Lite  |  Now GA  |  `pubsublite.subscriptions.create`  
`pubsublite.subscriptions.delete`  
`pubsublite.subscriptions.get`  
`pubsublite.subscriptions.getCursor`  
`pubsublite.subscriptions.list`  
`pubsublite.subscriptions.setCursor`  
`pubsublite.subscriptions.subscribe`  
`pubsublite.subscriptions.update`  
`pubsublite.topics.computeMessageStats`  
`pubsublite.topics.create`  
`pubsublite.topics.delete`  
`pubsublite.topics.get`  
`pubsublite.topics.getPartitions`  
`pubsublite.topics.list`  
`pubsublite.topics.listSubscriptions`  
`pubsublite.topics.publish`  
`pubsublite.topics.subscribe`  
`pubsublite.topics.update`  
  
Cloud Service Mesh  |  Added  |  `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
Cloud Service Mesh  |  Supported In Custom Roles  |  `trafficdirector.networks.getConfigs`  
`trafficdirector.networks.reportMetrics`  
  
  
## Cloud IAM changes as of 2020-10-09

Service | Change | Description  
---|---|---  
Access Context Manager  |  Now GA  |  The role `roles/accesscontextmanager.gcpAccessAdmin` (Cloud Access Binding Admin) is now GA.  
Access Context Manager  |  Now GA  |  The role `roles/accesscontextmanager.gcpAccessReader` (Cloud Access Binding Reader) is now GA.  
Assured Workloads  |  Now GA  |  The role `roles/assuredworkloads.admin` (Assured Workloads Administrator) is now GA.  
Assured Workloads  |  Now GA  |  The role `roles/assuredworkloads.editor` (Assured Workloads Editor) is now GA.  
Assured Workloads  |  Now GA  |  The role `roles/assuredworkloads.reader` (Assured Workloads Reader) is now GA.  
BigQuery  |  Now GA  |  The role `roles/bigquery.connectionAdmin` (BigQuery Connection Admin) is now GA.  
BigQuery  |  Now GA  |  The role `roles/bigquery.connectionUser` (BigQuery Connection User) is now GA.  
Cloud Scheduler  |  Now GA  |  The role `roles/cloudscheduler.admin` (Cloud Scheduler Admin) is now GA.  
Cloud Scheduler  |  Now GA  |  The role `roles/cloudscheduler.jobRunner` (Cloud Scheduler Job Runner) is now GA.  
Cloud Scheduler  |  Now GA  |  The role `roles/cloudscheduler.viewer` (Cloud Scheduler Viewer) is now GA.  
Google Cloud Support  |  Role Updated  |  The following permissions have been added to the role `roles/cloudsupport.admin` (Support Account Administrator): `resourcemanager.organizations.get`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `notebooks.instances.updateConfig`  
  
Game Servers  |  Role Updated  |  The following permissions have been removed from the role `roles/gameservices.serviceAgent` (Game Services Service Agent): `gkehub.gateway.get`  
`gkehub.gateway.getIamPolicy`  
  
GKE Hub  |  Role Updated  |  The following permissions have been removed from the role `roles/gkehub.viewer` (GKE Hub Viewer): `gkehub.gateway.get`  
`gkehub.gateway.getIamPolicy`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.admin` (Notebooks Admin): `notebooks.instances.updateConfig`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.legacyAdmin` (Notebooks Legacy Admin): `notebooks.instances.updateConfig`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.serviceAgent` (AI Platform Notebooks Service Agent): `notebooks.instances.updateConfig`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `notebooks.instances.updateConfig`  
  
Service Directory  |  Now GA  |  The role `roles/servicedirectory.admin` (Service Directory Admin) is now GA.  
Service Directory  |  Now GA  |  The role `roles/servicedirectory.editor` (Service Directory Editor) is now GA.  
Service Directory  |  Now GA  |  The role `roles/servicedirectory.viewer` (Service Directory Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `pubsublite.subscriptions.subscribe`  
  
Access Context Manager  |  Added  |  `accesscontextmanager.gcpUserAccessBindings.create`  
`accesscontextmanager.gcpUserAccessBindings.delete`  
`accesscontextmanager.gcpUserAccessBindings.get`  
`accesscontextmanager.gcpUserAccessBindings.list`  
`accesscontextmanager.gcpUserAccessBindings.update`  
  
Access Context Manager  |  Supported In Custom Roles  |  `accesscontextmanager.gcpUserAccessBindings.create`  
`accesscontextmanager.gcpUserAccessBindings.delete`  
`accesscontextmanager.gcpUserAccessBindings.get`  
`accesscontextmanager.gcpUserAccessBindings.list`  
`accesscontextmanager.gcpUserAccessBindings.update`  
  
Access Context Manager  |  Now GA  |  `accesscontextmanager.gcpUserAccessBindings.create`  
`accesscontextmanager.gcpUserAccessBindings.delete`  
`accesscontextmanager.gcpUserAccessBindings.get`  
`accesscontextmanager.gcpUserAccessBindings.list`  
`accesscontextmanager.gcpUserAccessBindings.update`  
  
Assured Workloads  |  Supported In Custom Roles  |  `assuredworkloads.workload.create`  
`assuredworkloads.workload.delete`  
`assuredworkloads.workload.get`  
`assuredworkloads.workload.list`  
  
Assured Workloads  |  Now GA  |  `assuredworkloads.operations.get`  
`assuredworkloads.operations.list`  
`assuredworkloads.workload.create`  
`assuredworkloads.workload.delete`  
`assuredworkloads.workload.get`  
`assuredworkloads.workload.list`  
`assuredworkloads.workload.update`  
  
BigQuery  |  Now GA  |  `bigquery.connections.create`  
`bigquery.connections.delete`  
`bigquery.connections.get`  
`bigquery.connections.getIamPolicy`  
`bigquery.connections.list`  
`bigquery.connections.setIamPolicy`  
`bigquery.connections.update`  
`bigquery.connections.use`  
  
Cloud Scheduler  |  Supported In Custom Roles  |  `cloudscheduler.jobs.create`  
`cloudscheduler.jobs.delete`  
`cloudscheduler.jobs.enable`  
`cloudscheduler.jobs.fullView`  
`cloudscheduler.jobs.get`  
`cloudscheduler.jobs.list`  
`cloudscheduler.jobs.pause`  
`cloudscheduler.jobs.run`  
`cloudscheduler.jobs.update`  
`cloudscheduler.locations.get`  
`cloudscheduler.locations.list`  
  
Cloud Scheduler  |  Now GA  |  `cloudscheduler.jobs.create`  
`cloudscheduler.jobs.delete`  
`cloudscheduler.jobs.enable`  
`cloudscheduler.jobs.fullView`  
`cloudscheduler.jobs.get`  
`cloudscheduler.jobs.list`  
`cloudscheduler.jobs.pause`  
`cloudscheduler.jobs.run`  
`cloudscheduler.jobs.update`  
  
Essential Contacts  |  Added  |  `essentialcontacts.contacts.create`  
`essentialcontacts.contacts.delete`  
`essentialcontacts.contacts.get`  
`essentialcontacts.contacts.list`  
`essentialcontacts.contacts.update`  
  
Essential Contacts  |  Supported In Custom Roles  |  `essentialcontacts.contacts.create`  
`essentialcontacts.contacts.delete`  
`essentialcontacts.contacts.get`  
`essentialcontacts.contacts.list`  
`essentialcontacts.contacts.update`  
  
Eventarc  |  Added  |  `eventarc.events.receiveAuditLogWritten`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.setIamPolicy`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
  
Eventarc  |  Supported In Custom Roles  |  `eventarc.events.receiveAuditLogWritten`  
`eventarc.locations.get`  
`eventarc.locations.list`  
`eventarc.operations.cancel`  
`eventarc.operations.delete`  
`eventarc.operations.get`  
`eventarc.operations.list`  
`eventarc.triggers.create`  
`eventarc.triggers.delete`  
`eventarc.triggers.get`  
`eventarc.triggers.getIamPolicy`  
`eventarc.triggers.list`  
`eventarc.triggers.setIamPolicy`  
`eventarc.triggers.undelete`  
`eventarc.triggers.update`  
  
Cloud Healthcare API  |  Added  |  `healthcare.attributeDefinitions.create`  
`healthcare.attributeDefinitions.delete`  
`healthcare.attributeDefinitions.get`  
`healthcare.attributeDefinitions.list`  
`healthcare.attributeDefinitions.update`  
`healthcare.consentArtifacts.create`  
`healthcare.consentArtifacts.delete`  
`healthcare.consentArtifacts.get`  
`healthcare.consentArtifacts.list`  
`healthcare.consentStores.checkDataAccess`  
`healthcare.consentStores.create`  
`healthcare.consentStores.delete`  
`healthcare.consentStores.evaluateUserConsents`  
`healthcare.consentStores.get`  
`healthcare.consentStores.getIamPolicy`  
`healthcare.consentStores.list`  
`healthcare.consentStores.queryAccessibleData`  
`healthcare.consentStores.setIamPolicy`  
`healthcare.consentStores.update`  
`healthcare.consents.activate`  
`healthcare.consents.create`  
`healthcare.consents.delete`  
`healthcare.consents.get`  
`healthcare.consents.list`  
`healthcare.consents.reject`  
`healthcare.consents.revoke`  
`healthcare.consents.update`  
`healthcare.userDataMappings.archive`  
`healthcare.userDataMappings.create`  
`healthcare.userDataMappings.delete`  
`healthcare.userDataMappings.get`  
`healthcare.userDataMappings.list`  
`healthcare.userDataMappings.update`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.attributeDefinitions.create`  
`healthcare.attributeDefinitions.delete`  
`healthcare.attributeDefinitions.get`  
`healthcare.attributeDefinitions.list`  
`healthcare.attributeDefinitions.update`  
`healthcare.consentArtifacts.create`  
`healthcare.consentArtifacts.delete`  
`healthcare.consentArtifacts.get`  
`healthcare.consentArtifacts.list`  
`healthcare.consentStores.checkDataAccess`  
`healthcare.consentStores.create`  
`healthcare.consentStores.delete`  
`healthcare.consentStores.evaluateUserConsents`  
`healthcare.consentStores.get`  
`healthcare.consentStores.getIamPolicy`  
`healthcare.consentStores.list`  
`healthcare.consentStores.queryAccessibleData`  
`healthcare.consentStores.setIamPolicy`  
`healthcare.consentStores.update`  
`healthcare.consents.activate`  
`healthcare.consents.create`  
`healthcare.consents.delete`  
`healthcare.consents.get`  
`healthcare.consents.list`  
`healthcare.consents.reject`  
`healthcare.consents.revoke`  
`healthcare.consents.update`  
`healthcare.userDataMappings.archive`  
`healthcare.userDataMappings.create`  
`healthcare.userDataMappings.delete`  
`healthcare.userDataMappings.get`  
`healthcare.userDataMappings.list`  
`healthcare.userDataMappings.update`  
  
Notebooks  |  Added  |  `notebooks.instances.updateConfig`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.topics.computeMessageStats`  
  
Pub/Sub Lite  |  Supported In Custom Roles  |  `pubsublite.topics.computeMessageStats`  
  
Memorystore for Redis  |  Added  |  `redis.instances.getAuthString`  
`redis.instances.updateAuth`  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `redis.instances.getAuthString`  
`redis.instances.updateAuth`  
  
Service Directory  |  Now GA  |  `servicedirectory.endpoints.create`  
`servicedirectory.endpoints.delete`  
`servicedirectory.endpoints.get`  
`servicedirectory.endpoints.getIamPolicy`  
`servicedirectory.endpoints.list`  
`servicedirectory.endpoints.setIamPolicy`  
`servicedirectory.endpoints.update`  
`servicedirectory.locations.get`  
`servicedirectory.locations.list`  
`servicedirectory.namespaces.associatePrivateZone`  
`servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.namespaces.get`  
`servicedirectory.namespaces.getIamPolicy`  
`servicedirectory.namespaces.list`  
`servicedirectory.namespaces.setIamPolicy`  
`servicedirectory.namespaces.update`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
`servicedirectory.services.get`  
`servicedirectory.services.getIamPolicy`  
`servicedirectory.services.list`  
`servicedirectory.services.resolve`  
`servicedirectory.services.setIamPolicy`  
`servicedirectory.services.update`  
  
  
## Cloud IAM changes as of 2020-10-02

Service | Change | Description  
---|---|---  
Cloud Asset Inventory  |  Role Updated  |  The following permissions have been added to the role `roles/cloudasset.serviceAgent` (Cloud Asset Service Agent): `bigquery.tables.update`  
  
Talent Solution  |  Role Updated  |  The following permissions have been added to the role `roles/cloudjobdiscovery.jobsEditor` (Job Editor): `cloudjobdiscovery.tenants.create`  
`cloudjobdiscovery.tenants.delete`  
`cloudjobdiscovery.tenants.get`  
`cloudjobdiscovery.tenants.update`  
  
Talent Solution  |  Role Updated  |  The following permissions have been added to the role `roles/cloudjobdiscovery.jobsViewer` (Job Viewer): `cloudjobdiscovery.tenants.get`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `aiplatform.endpoints.explain`  
`aiplatform.endpoints.predict`  
  
Gemini Enterprise Agent Platform  |  Added  |  `aiplatform.annotationSpecs.create`  
`aiplatform.annotationSpecs.delete`  
`aiplatform.annotationSpecs.get`  
`aiplatform.annotationSpecs.list`  
`aiplatform.annotationSpecs.update`  
`aiplatform.annotations.create`  
`aiplatform.annotations.delete`  
`aiplatform.annotations.get`  
`aiplatform.annotations.list`  
`aiplatform.annotations.update`  
`aiplatform.batchPredictionJobs.cancel`  
`aiplatform.batchPredictionJobs.create`  
`aiplatform.batchPredictionJobs.delete`  
`aiplatform.batchPredictionJobs.get`  
`aiplatform.batchPredictionJobs.list`  
`aiplatform.customJobs.cancel`  
`aiplatform.customJobs.create`  
`aiplatform.customJobs.delete`  
`aiplatform.customJobs.get`  
`aiplatform.customJobs.list`  
`aiplatform.dataItems.create`  
`aiplatform.dataItems.delete`  
`aiplatform.dataItems.get`  
`aiplatform.dataItems.list`  
`aiplatform.dataItems.update`  
`aiplatform.dataLabelingJobs.cancel`  
`aiplatform.dataLabelingJobs.create`  
`aiplatform.dataLabelingJobs.delete`  
`aiplatform.dataLabelingJobs.get`  
`aiplatform.dataLabelingJobs.list`  
`aiplatform.datasets.create`  
`aiplatform.datasets.delete`  
`aiplatform.datasets.export`  
`aiplatform.datasets.get`  
`aiplatform.datasets.import`  
`aiplatform.datasets.list`  
`aiplatform.datasets.update`  
`aiplatform.endpoints.create`  
`aiplatform.endpoints.delete`  
`aiplatform.endpoints.deploy`  
`aiplatform.endpoints.explain`  
`aiplatform.endpoints.get`  
`aiplatform.endpoints.list`  
`aiplatform.endpoints.predict`  
`aiplatform.endpoints.undeploy`  
`aiplatform.endpoints.update`  
`aiplatform.hyperparameterTuningJobs.cancel`  
`aiplatform.hyperparameterTuningJobs.create`  
`aiplatform.hyperparameterTuningJobs.delete`  
`aiplatform.hyperparameterTuningJobs.get`  
`aiplatform.hyperparameterTuningJobs.list`  
`aiplatform.locations.get`  
`aiplatform.locations.list`  
`aiplatform.migratableResources.migrate`  
`aiplatform.migratableResources.search`  
`aiplatform.modelEvaluationSlices.get`  
`aiplatform.modelEvaluationSlices.list`  
`aiplatform.modelEvaluations.exportEvaluatedDataItems`  
`aiplatform.modelEvaluations.get`  
`aiplatform.modelEvaluations.list`  
`aiplatform.models.delete`  
`aiplatform.models.export`  
`aiplatform.models.get`  
`aiplatform.models.list`  
`aiplatform.models.upload`  
`aiplatform.operations.list`  
`aiplatform.specialistPools.create`  
`aiplatform.specialistPools.delete`  
`aiplatform.specialistPools.get`  
`aiplatform.specialistPools.list`  
`aiplatform.specialistPools.update`  
`aiplatform.trainingPipelines.cancel`  
`aiplatform.trainingPipelines.create`  
`aiplatform.trainingPipelines.delete`  
`aiplatform.trainingPipelines.get`  
`aiplatform.trainingPipelines.list`  
  
Gemini Enterprise Agent Platform  |  Supported In Custom Roles  |  `aiplatform.annotationSpecs.create`  
`aiplatform.annotationSpecs.delete`  
`aiplatform.annotationSpecs.get`  
`aiplatform.annotationSpecs.list`  
`aiplatform.annotationSpecs.update`  
`aiplatform.annotations.create`  
`aiplatform.annotations.delete`  
`aiplatform.annotations.get`  
`aiplatform.annotations.list`  
`aiplatform.annotations.update`  
`aiplatform.batchPredictionJobs.cancel`  
`aiplatform.batchPredictionJobs.create`  
`aiplatform.batchPredictionJobs.delete`  
`aiplatform.batchPredictionJobs.get`  
`aiplatform.batchPredictionJobs.list`  
`aiplatform.customJobs.cancel`  
`aiplatform.customJobs.create`  
`aiplatform.customJobs.delete`  
`aiplatform.customJobs.get`  
`aiplatform.customJobs.list`  
`aiplatform.dataItems.create`  
`aiplatform.dataItems.delete`  
`aiplatform.dataItems.get`  
`aiplatform.dataItems.list`  
`aiplatform.dataItems.update`  
`aiplatform.dataLabelingJobs.cancel`  
`aiplatform.dataLabelingJobs.create`  
`aiplatform.dataLabelingJobs.delete`  
`aiplatform.dataLabelingJobs.get`  
`aiplatform.dataLabelingJobs.list`  
`aiplatform.datasets.create`  
`aiplatform.datasets.delete`  
`aiplatform.datasets.export`  
`aiplatform.datasets.get`  
`aiplatform.datasets.import`  
`aiplatform.datasets.list`  
`aiplatform.datasets.update`  
`aiplatform.endpoints.create`  
`aiplatform.endpoints.delete`  
`aiplatform.endpoints.deploy`  
`aiplatform.endpoints.explain`  
`aiplatform.endpoints.get`  
`aiplatform.endpoints.list`  
`aiplatform.endpoints.predict`  
`aiplatform.endpoints.undeploy`  
`aiplatform.endpoints.update`  
`aiplatform.hyperparameterTuningJobs.cancel`  
`aiplatform.hyperparameterTuningJobs.create`  
`aiplatform.hyperparameterTuningJobs.delete`  
`aiplatform.hyperparameterTuningJobs.get`  
`aiplatform.hyperparameterTuningJobs.list`  
`aiplatform.locations.get`  
`aiplatform.locations.list`  
`aiplatform.migratableResources.migrate`  
`aiplatform.migratableResources.search`  
`aiplatform.modelEvaluationSlices.get`  
`aiplatform.modelEvaluationSlices.list`  
`aiplatform.modelEvaluations.exportEvaluatedDataItems`  
`aiplatform.modelEvaluations.get`  
`aiplatform.modelEvaluations.list`  
`aiplatform.models.delete`  
`aiplatform.models.export`  
`aiplatform.models.get`  
`aiplatform.models.list`  
`aiplatform.models.upload`  
`aiplatform.operations.list`  
`aiplatform.specialistPools.create`  
`aiplatform.specialistPools.delete`  
`aiplatform.specialistPools.get`  
`aiplatform.specialistPools.list`  
`aiplatform.specialistPools.update`  
`aiplatform.trainingPipelines.cancel`  
`aiplatform.trainingPipelines.create`  
`aiplatform.trainingPipelines.delete`  
`aiplatform.trainingPipelines.get`  
`aiplatform.trainingPipelines.list`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.models.create`  
`bigquery.models.delete`  
`bigquery.models.getData`  
`bigquery.models.getMetadata`  
`bigquery.models.list`  
`bigquery.models.updateData`  
`bigquery.models.updateMetadata`  
  
BigQuery  |  Now GA  |  `bigquery.models.create`  
`bigquery.models.delete`  
`bigquery.models.export`  
`bigquery.models.getData`  
`bigquery.models.getMetadata`  
`bigquery.models.list`  
`bigquery.models.updateData`  
`bigquery.models.updateMetadata`  
  
  
## Cloud IAM changes as of 2020-09-25

Service | Change | Description  
---|---|---  
Anthos  |  Now GA  |  The role `roles/anthos.serviceAgent` (Anthos Service Agent) is now GA.  
Config Management  |  Now GA  |  The role `roles/anthosconfigmanagement.serviceAgent` (Anthos Config Management Service Agent) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.serviceAgent` (Apigee Service Agent) is now GA.  
App Engine flexible environment  |  Now GA  |  The role `roles/appengineflex.serviceAgent` (App Engine flexible environment Service Agent) is now GA.  
Artifact Registry  |  Now GA  |  The role `roles/artifactregistry.serviceAgent` (Artifact Registry Service Agent) is now GA.  
AutoML  |  Now GA  |  The role `roles/automl.serviceAgent` (AutoML Service Agent) is now GA.  
Recommendations  |  Now GA  |  The role `roles/automlrecommendations.serviceAgent` (Recommendations AI Service Agent) is now GA.  
BigQuery Connection API  |  Now GA  |  The role `roles/bigqueryconnection.serviceAgent` (BigQuery Connection Service Agent) is now GA.  
BigQuery Data Transfer Service  |  Now GA  |  The role `roles/bigquerydatatransfer.serviceAgent` (BigQuery Data Transfer Service Agent) is now GA.  
Binary Authorization  |  Now GA  |  The role `roles/binaryauthorization.serviceAgent` (Binary Authorization Service Agent) is now GA.  
Cloud Asset Inventory  |  Now GA  |  The role `roles/cloudasset.serviceAgent` (Cloud Asset Service Agent) is now GA.  
Cloud Build  |  Now GA  |  The role `roles/cloudbuild.serviceAgent` (Cloud Build Service Agent) is now GA.  
Cloud Run functions  |  Now GA  |  The role `roles/cloudfunctions.serviceAgent` (Cloud Functions Service Agent) is now GA.  
Cloud IoT  |  Now GA  |  The role `roles/cloudiot.serviceAgent` (Cloud IoT Core Service Agent) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.serviceAgent` (Cloud KMS Service Agent) is now GA.  
Cloud Scheduler  |  Now GA  |  The role `roles/cloudscheduler.serviceAgent` (Cloud Scheduler Service Agent) is now GA.  
Cloud SQL  |  Now GA  |  The role `roles/cloudsql.serviceAgent` (Cloud SQL Service Agent) is now GA.  
Cloud Tasks  |  Now GA  |  The role `roles/cloudtasks.serviceAgent` (Cloud Tasks Service Agent) is now GA.  
Cloud Tasks  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtasks.admin` (Cloud Tasks Admin): `monitoring.timeSeries.list`  
  
Cloud Tasks  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtasks.viewer` (Cloud Tasks Viewer): `monitoring.timeSeries.list`  
  
Cloud TPU  |  Now GA  |  The role `roles/cloudtpu.serviceAgent` (Cloud TPU V2 API Service Agent) is now GA.  
Managed Service for Apache Airflow  |  Now GA  |  The role `roles/composer.serviceAgent` (Cloud Composer API Service Agent) is now GA.  
Compute Engine  |  Now GA  |  The role `roles/compute.serviceAgent` (Compute Engine Service Agent) is now GA.  
Google Kubernetes Engine  |  Now GA  |  The role `roles/container.serviceAgent` (Kubernetes Engine Service Agent) is now GA.  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.ServiceAgent` (Container Analysis Service Agent) is now GA.  
Container Registry  |  Now GA  |  The role `roles/containerregistry.ServiceAgent` (Container Registry Service Agent) is now GA.  
Container Scanning  |  Now GA  |  The role `roles/containerscanning.ServiceAgent` (Container Scanner Service Agent) is now GA.  
Container Threat Detection  |  Now GA  |  The role `roles/containerthreatdetection.serviceAgent` (Container Threat Detection Service Agent) is now GA.  
Dataflow  |  Now GA  |  The role `roles/dataflow.serviceAgent` (Cloud Dataflow Service Agent) is now GA.  
Cloud Data Fusion  |  Now GA  |  The role `roles/datafusion.serviceAgent` (Cloud Data Fusion API Service Agent) is now GA.  
AI Platform Data Labeling Service  |  Now GA  |  The role `roles/datalabeling.serviceAgent` (DataLabeling Service Agent) is now GA.  
Dataprep by Trifacta  |  Now GA  |  The role `roles/dataprep.serviceAgent` (Dataprep Service Agent) is now GA.  
Managed Service for Apache Spark  |  Now GA  |  The role `roles/dataproc.serviceAgent` (Dataproc Service Agent) is now GA.  
Data Studio  |  Now GA  |  The role `roles/datastudio.serviceAgent` (Data Studio Service Agent) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.serviceAgent` (Dialogflow Service Agent) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.serviceAgent` (DLP API Service Agent) is now GA.  
Document AI  |  Now GA  |  The role `roles/documentaicore.serviceAgent` (DocumentAI Core Service Agent) is now GA.  
Cloud Endpoints  |  Now GA  |  The role `roles/endpoints.serviceAgent` (Cloud Endpoints Service Agent) is now GA.  
Cloud Endpoints Portal  |  Now GA  |  The role `roles/endpointsportal.serviceAgent` (Endpoints Portal Service Agent) is now GA.  
Filestore  |  Now GA  |  The role `roles/file.serviceAgent` (Cloud Filestore Service Agent) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.appDistributionSdkServiceAgent` (Firebase App Distribution Admin SDK Service Agent) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.managementServiceAgent` (Firebase Service Management Service Agent) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.sdkAdminServiceAgent` (Firebase Admin SDK Administrator Service Agent) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.sdkProvisioningServiceAgent` (Firebase SDK Provisioning Service Agent) is now GA.  
Firebase Mods  |  Now GA  |  The role `roles/firebasemods.serviceAgent` (Firebase Extensions API Service Agent) is now GA.  
Firebase Storage  |  Now GA  |  The role `roles/firebasestorage.serviceAgent` (Cloud Storage for Firebase Service Agent) is now GA.  
Firewall Insights  |  Now GA  |  The role `roles/firewallinsights.serviceAgent` (Cloud Firewall Insights Service Agent) is now GA.  
Game Servers  |  Now GA  |  The role `roles/gameservices.serviceAgent` (Game Services Service Agent) is now GA.  
Cloud Life Sciences  |  Now GA  |  The role `roles/genomics.serviceAgent` (Genomics Service Agent) is now GA.  
GKE Hub  |  Now GA  |  The role `roles/gkehub.serviceAgent` (GKE Hub Service Agent) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.serviceAgent` (Healthcare Service Agent) is now GA.  
Cloud Life Sciences  |  Now GA  |  The role `roles/lifesciences.serviceAgent` (Cloud Life Sciences Service Agent) is now GA.  
Managed Service for Microsoft Active Directory  |  Now GA  |  The role `roles/managedidentities.serviceAgent` (Cloud Managed Identities Service Agent) is now GA.  
Memorystore for Memcached  |  Now GA  |  The role `roles/memcache.serviceAgent` (Cloud Memorystore Memcached Service Agent) is now GA.  
Cloud Service Mesh  |  Now GA  |  The role `roles/meshconfig.serviceAgent` (Mesh Config Service Agent) is now GA.  
Cloud Service Mesh  |  Now GA  |  The role `roles/meshdataplane.serviceAgent` (Mesh Data Plane Service Agent) is now GA.  
AI Platform  |  Now GA  |  The role `roles/ml.serviceAgent` (Cloud ML Service Agent) is now GA.  
Cloud Monitoring  |  Now GA  |  The role `roles/monitoring.notificationServiceAgent` (Monitoring Notification Service Agent) is now GA.  
Multi-Cluster Ingress  |  Now GA  |  The role `roles/multiclusteringress.serviceAgent` (Multi Cluster Ingress Service Agent) is now GA.  
Multi-Cluster Metering  |  Now GA  |  The role `roles/multiclustermetering.serviceAgent` (Multi-cluster metering Service Agent) is now GA.  
Network Management API  |  Now GA  |  The role `roles/networkmanagement.serviceAgent` (GCP Network Management Service Agent) is now GA.  
Notebooks  |  Now GA  |  The role `roles/notebooks.serviceAgent` (AI Platform Notebooks Service Agent) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.serviceAgent` (Cloud OS Config Service Agent) is now GA.  
Pub/Sub  |  Now GA  |  The role `roles/pubsub.serviceAgent` (Cloud Pub/Sub Service Agent) is now GA.  
Memorystore for Redis  |  Now GA  |  The role `roles/redis.serviceAgent` (Cloud Memorystore Redis Service Agent) is now GA.  
Remote Build Execution  |  Now GA  |  The role `roles/remotebuildexecution.serviceAgent` (Remote Build Execution Service Agent) is now GA.  
Cloud Run  |  Now GA  |  The role `roles/run.serviceAgent` (Cloud Run Service Agent) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.automationServiceAgent` (Security Center Automation Service Agent) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.controlServiceAgent` (Security Center Control Service Agent) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.notificationServiceAgent` (Security Center Notification Service Agent) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.securityHealthAnalyticsServiceAgent` (Security Health Analytics Service Agent) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.serviceAgent` (Security Center Service Agent) is now GA.  
Cloud Run  |  Now GA  |  The role `roles/serverless.serviceAgent` (Cloud Run Service Agent) is now GA.  
Service Networking  |  Now GA  |  The role `roles/servicenetworking.serviceAgent` (Service Networking Service Agent) is now GA.  
Cloud Source Repositories  |  Now GA  |  The role `roles/sourcerepo.serviceAgent` (Cloud Source Repositories Service Agent) is now GA.  
Cloud TPU  |  Now GA  |  The role `roles/tpu.serviceAgent` (Cloud TPU API Service Agent) is now GA.  
Serverless VPC Access  |  Now GA  |  The role `roles/vpcaccess.serviceAgent` (Serverless VPC Access Service Agent) is now GA.  
Web Security Scanner  |  Now GA  |  The role `roles/websecurityscanner.serviceAgent` (Cloud Web Security Scanner Service Agent) is now GA.  
Workflows  |  Now GA  |  The role `roles/workflows.serviceAgent` (Cloud Workflows Service Agent) is now GA.  
BigQuery  |  Added  |  `bigquery.capacityCommitments.update`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.capacityCommitments.update`  
  
BigQuery  |  Now GA  |  `bigquery.capacityCommitments.update`  
  
Cloud Domains  |  Added  |  `domains.locations.get`  
`domains.locations.list`  
`domains.operations.cancel`  
`domains.operations.get`  
`domains.operations.list`  
`domains.registrations.configureContact`  
`domains.registrations.configureDns`  
`domains.registrations.configureManagement`  
`domains.registrations.create`  
`domains.registrations.delete`  
`domains.registrations.get`  
`domains.registrations.getIamPolicy`  
`domains.registrations.list`  
`domains.registrations.setIamPolicy`  
`domains.registrations.update`  
  
Transcoder API  |  Added  |  `transcoder.jobTemplates.create`  
`transcoder.jobTemplates.delete`  
`transcoder.jobTemplates.get`  
`transcoder.jobTemplates.list`  
`transcoder.jobs.create`  
`transcoder.jobs.delete`  
`transcoder.jobs.get`  
`transcoder.jobs.list`  
  
Transcoder API  |  Supported In Custom Roles  |  `transcoder.jobTemplates.create`  
`transcoder.jobTemplates.delete`  
`transcoder.jobTemplates.get`  
`transcoder.jobTemplates.list`  
`transcoder.jobs.create`  
`transcoder.jobs.delete`  
`transcoder.jobs.get`  
`transcoder.jobs.list`  
  
  
## Cloud IAM changes as of 2020-09-18

Service | Change | Description  
---|---|---  
BigQuery  |  Now GA  |  The role `roles/bigquery.resourceAdmin` (BigQuery Resource Admin) is now GA.  
BigQuery  |  Now GA  |  The role `roles/bigquery.resourceEditor` (BigQuery Resource Editor) is now GA.  
BigQuery  |  Now GA  |  The role `roles/bigquery.resourceViewer` (BigQuery Resource Viewer) is now GA.  
Recommender  |  Role Updated  |  The following permissions have been added to the role `roles/recommender.firewallAdmin` (Firewall Recommender Admin): `recommender.locations.get`  
`recommender.locations.list`  
  
Recommender  |  Role Updated  |  The following permissions have been added to the role `roles/recommender.firewallViewer` (Firewall Recommender Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
Recommender  |  Role Updated  |  The following permissions have been added to the role `roles/recommender.projectCudAdmin` (Project Usage Commitment Recommender Admin): `recommender.locations.get`  
`recommender.locations.list`  
  
Recommender  |  Role Updated  |  The following permissions have been added to the role `roles/recommender.projectCudViewer` (Project Usage Commitment Recommender Viewer): `recommender.locations.get`  
`recommender.locations.list`  
  
API Gateway  |  Supported In Custom Roles  |  `apigateway.apiconfigs.create`  
`apigateway.apiconfigs.delete`  
`apigateway.apiconfigs.get`  
`apigateway.apiconfigs.getIamPolicy`  
`apigateway.apiconfigs.list`  
`apigateway.apiconfigs.setIamPolicy`  
`apigateway.apiconfigs.update`  
`apigateway.apis.create`  
`apigateway.apis.delete`  
`apigateway.apis.get`  
`apigateway.apis.getIamPolicy`  
`apigateway.apis.list`  
`apigateway.apis.setIamPolicy`  
`apigateway.apis.update`  
`apigateway.gateways.create`  
`apigateway.gateways.delete`  
`apigateway.gateways.get`  
`apigateway.gateways.getIamPolicy`  
`apigateway.gateways.list`  
`apigateway.gateways.setIamPolicy`  
`apigateway.gateways.update`  
`apigateway.locations.get`  
`apigateway.locations.list`  
`apigateway.operations.cancel`  
`apigateway.operations.delete`  
`apigateway.operations.get`  
`apigateway.operations.list`  
  
BigQuery  |  Now GA  |  `bigquery.bireservations.get`  
`bigquery.bireservations.update`  
`bigquery.capacityCommitments.create`  
`bigquery.capacityCommitments.delete`  
`bigquery.capacityCommitments.get`  
`bigquery.capacityCommitments.list`  
`bigquery.reservationAssignments.create`  
`bigquery.reservationAssignments.delete`  
`bigquery.reservationAssignments.list`  
`bigquery.reservationAssignments.search`  
`bigquery.reservations.create`  
`bigquery.reservations.delete`  
`bigquery.reservations.get`  
`bigquery.reservations.list`  
`bigquery.reservations.update`  
  
Identity and Access Management  |  Added  |  `iam.workloadIdentityPoolProviders.create`  
`iam.workloadIdentityPoolProviders.delete`  
`iam.workloadIdentityPoolProviders.get`  
`iam.workloadIdentityPoolProviders.list`  
`iam.workloadIdentityPoolProviders.undelete`  
`iam.workloadIdentityPoolProviders.update`  
`iam.workloadIdentityPools.create`  
`iam.workloadIdentityPools.delete`  
`iam.workloadIdentityPools.get`  
`iam.workloadIdentityPools.list`  
`iam.workloadIdentityPools.undelete`  
`iam.workloadIdentityPools.update`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `iam.workloadIdentityPoolProviders.create`  
`iam.workloadIdentityPoolProviders.delete`  
`iam.workloadIdentityPoolProviders.get`  
`iam.workloadIdentityPoolProviders.list`  
`iam.workloadIdentityPoolProviders.undelete`  
`iam.workloadIdentityPoolProviders.update`  
`iam.workloadIdentityPools.create`  
`iam.workloadIdentityPools.delete`  
`iam.workloadIdentityPools.get`  
`iam.workloadIdentityPools.list`  
`iam.workloadIdentityPools.undelete`  
`iam.workloadIdentityPools.update`  
  
  
## Cloud IAM changes as of 2020-09-11

Service | Change | Description  
---|---|---  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.privateLogViewer` (Private Logs Viewer): `logging.queries.create`  
`logging.queries.delete`  
`logging.queries.get`  
`logging.queries.list`  
`logging.queries.update`  
  
Security Command Center  |  Added  |  `securitycenter.findings.setWorkflowState`  
  
Security Command Center  |  Supported In Custom Roles  |  `securitycenter.findings.setWorkflowState`  
  
  
## Cloud IAM changes as of 2020-09-04

Service | Change | Description  
---|---|---  
Apigee  |  Now GA  |  The role `roles/apigee.portalAdmin` (Apigee Portal Admin) is now GA.  
Cloud Profiler  |  Now GA  |  The role `roles/cloudprofiler.agent` (Cloud Profiler Agent) is now GA.  
Cloud Profiler  |  Now GA  |  The role `roles/cloudprofiler.user` (Cloud Profiler User) is now GA.  
Cloud SQL  |  Now GA  |  The role `roles/cloudsql.instanceUser` (Cloud SQL Instance User) is now GA.  
Notebooks  |  Now GA  |  The role `roles/notebooks.admin` (Notebooks Admin) is now GA.  
Notebooks  |  Now GA  |  The role `roles/notebooks.legacyAdmin` (Notebooks Legacy Admin) is now GA.  
Notebooks  |  Now GA  |  The role `roles/notebooks.legacyViewer` (Notebooks Legacy Viewer) is now GA.  
Notebooks  |  Now GA  |  The role `roles/notebooks.runner` (Notebooks Runner) is now GA.  
Notebooks  |  Now GA  |  The role `roles/notebooks.viewer` (Notebooks Viewer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.settingsAdmin` (Security Center Settings Admin) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.settingsEditor` (Security Center Settings Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.settingsViewer` (Security Center Settings Viewer) is now GA.  
BigQuery  |  Added  |  `bigquery.models.export`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.models.export`  
  
Cloud Profiler  |  Now GA  |  `cloudprofiler.profiles.create`  
`cloudprofiler.profiles.list`  
`cloudprofiler.profiles.update`  
  
Cloud SQL  |  Added  |  `cloudsql.instances.login`  
  
Cloud SQL  |  Supported In Custom Roles  |  `cloudsql.instances.login`  
  
Cloud SQL  |  Now GA  |  `cloudsql.instances.login`  
  
NetApp Cloud Volumes Service  |  Available In Custom Roles  |  `cloudvolumesgcp-api.netapp.com/activeDirectories.create`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.delete`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.get`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.list`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.update`  
`cloudvolumesgcp-api.netapp.com/ipRanges.list`  
`cloudvolumesgcp-api.netapp.com/jobs.get`  
`cloudvolumesgcp-api.netapp.com/jobs.list`  
`cloudvolumesgcp-api.netapp.com/regions.list`  
`cloudvolumesgcp-api.netapp.com/serviceLevels.list`  
`cloudvolumesgcp-api.netapp.com/snapshots.create`  
`cloudvolumesgcp-api.netapp.com/snapshots.delete`  
`cloudvolumesgcp-api.netapp.com/snapshots.get`  
`cloudvolumesgcp-api.netapp.com/snapshots.list`  
`cloudvolumesgcp-api.netapp.com/snapshots.update`  
`cloudvolumesgcp-api.netapp.com/volumes.create`  
`cloudvolumesgcp-api.netapp.com/volumes.delete`  
`cloudvolumesgcp-api.netapp.com/volumes.get`  
`cloudvolumesgcp-api.netapp.com/volumes.list`  
`cloudvolumesgcp-api.netapp.com/volumes.update`  
  
Notebooks  |  Now GA  |  `notebooks.environments.create`  
`notebooks.environments.delete`  
`notebooks.environments.get`  
`notebooks.environments.getIamPolicy`  
`notebooks.environments.list`  
`notebooks.environments.setIamPolicy`  
`notebooks.instances.checkUpgradability`  
`notebooks.instances.create`  
`notebooks.instances.delete`  
`notebooks.instances.get`  
`notebooks.instances.getIamPolicy`  
`notebooks.instances.list`  
`notebooks.instances.reset`  
`notebooks.instances.setAccelerator`  
`notebooks.instances.setIamPolicy`  
`notebooks.instances.setLabels`  
`notebooks.instances.setMachineType`  
`notebooks.instances.start`  
`notebooks.instances.stop`  
`notebooks.instances.update`  
`notebooks.instances.upgrade`  
`notebooks.locations.get`  
`notebooks.locations.list`  
`notebooks.operations.cancel`  
`notebooks.operations.delete`  
`notebooks.operations.get`  
`notebooks.operations.list`  
  
Security Command Center  |  Added  |  `securitycenter.containerthreatdetectionsettings.calculate`  
`securitycenter.containerthreatdetectionsettings.get`  
`securitycenter.containerthreatdetectionsettings.update`  
`securitycenter.eventthreatdetectionsettings.calculate`  
`securitycenter.eventthreatdetectionsettings.get`  
`securitycenter.eventthreatdetectionsettings.update`  
`securitycenter.securitycentersettings.get`  
`securitycenter.securitycentersettings.update`  
`securitycenter.securityhealthanalyticssettings.calculate`  
`securitycenter.securityhealthanalyticssettings.get`  
`securitycenter.securityhealthanalyticssettings.update`  
`securitycenter.subscription.get`  
`securitycenter.websecurityscannersettings.calculate`  
`securitycenter.websecurityscannersettings.get`  
`securitycenter.websecurityscannersettings.update`  
  
Security Command Center  |  Supported In Custom Roles  |  `securitycenter.containerthreatdetectionsettings.calculate`  
`securitycenter.containerthreatdetectionsettings.get`  
`securitycenter.containerthreatdetectionsettings.update`  
`securitycenter.eventthreatdetectionsettings.calculate`  
`securitycenter.eventthreatdetectionsettings.get`  
`securitycenter.eventthreatdetectionsettings.update`  
`securitycenter.securitycentersettings.get`  
`securitycenter.securitycentersettings.update`  
`securitycenter.securityhealthanalyticssettings.calculate`  
`securitycenter.securityhealthanalyticssettings.get`  
`securitycenter.securityhealthanalyticssettings.update`  
`securitycenter.subscription.get`  
`securitycenter.websecurityscannersettings.calculate`  
`securitycenter.websecurityscannersettings.get`  
`securitycenter.websecurityscannersettings.update`  
  
  
## Cloud IAM changes as of 2020-08-28

Service | Change | Description  
---|---|---  
App Engine  |  Now GA  |  The role `roles/appengine.appCreator` (App Engine Creator) is now GA.  
Cloud Run functions  |  Now GA  |  The role `roles/cloudfunctions.admin` (Cloud Functions Admin) is now GA.  
Cloud Run functions  |  Now GA  |  The role `roles/cloudfunctions.developer` (Cloud Functions Developer) is now GA.  
Cloud Run functions  |  Now GA  |  The role `roles/cloudfunctions.invoker` (Cloud Functions Invoker) is now GA.  
Cloud Run functions  |  Now GA  |  The role `roles/cloudfunctions.viewer` (Cloud Functions Viewer) is now GA.  
Assured Workloads  |  Added  |  `assuredworkloads.operations.get`  
`assuredworkloads.operations.list`  
`assuredworkloads.workload.create`  
`assuredworkloads.workload.delete`  
`assuredworkloads.workload.get`  
`assuredworkloads.workload.list`  
`assuredworkloads.workload.update`  
  
Assured Workloads  |  Supported In Custom Roles  |  `assuredworkloads.operations.get`  
`assuredworkloads.operations.list`  
  
Recommendations  |  Added  |  `automlrecommendations.catalogs.update`  
  
Recommendations  |  Supported In Custom Roles  |  `automlrecommendations.catalogs.list`  
`automlrecommendations.catalogs.update`  
`automlrecommendations.recommendations.list`  
  
Cloud Asset Inventory  |  Now GA  |  `cloudasset.assets.analyzeIamPolicy`  
  
Cloud Run functions  |  Supported In Custom Roles  |  `cloudfunctions.functions.call`  
`cloudfunctions.functions.create`  
`cloudfunctions.functions.delete`  
`cloudfunctions.functions.get`  
`cloudfunctions.functions.list`  
`cloudfunctions.functions.sourceCodeGet`  
`cloudfunctions.functions.sourceCodeSet`  
`cloudfunctions.functions.update`  
`cloudfunctions.locations.list`  
`cloudfunctions.operations.get`  
`cloudfunctions.operations.list`  
  
Cloud Run functions  |  Now GA  |  `cloudfunctions.functions.call`  
`cloudfunctions.functions.create`  
`cloudfunctions.functions.delete`  
`cloudfunctions.functions.get`  
`cloudfunctions.functions.getIamPolicy`  
`cloudfunctions.functions.invoke`  
`cloudfunctions.functions.list`  
`cloudfunctions.functions.setIamPolicy`  
`cloudfunctions.functions.sourceCodeGet`  
`cloudfunctions.functions.sourceCodeSet`  
`cloudfunctions.functions.update`  
`cloudfunctions.locations.list`  
`cloudfunctions.operations.get`  
`cloudfunctions.operations.list`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.hl7V2Stores.import`  
  
Cloud Logging  |  Added  |  `logging.queries.create`  
`logging.queries.delete`  
`logging.queries.get`  
`logging.queries.list`  
`logging.queries.update`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.queries.create`  
`logging.queries.delete`  
`logging.queries.get`  
`logging.queries.list`  
`logging.queries.update`  
  
Cloud Logging  |  Now GA  |  `logging.queries.create`  
`logging.queries.delete`  
`logging.queries.get`  
`logging.queries.list`  
`logging.queries.update`  
  
Workflows  |  Added  |  `workflows.executions.cancel`  
`workflows.executions.create`  
`workflows.executions.get`  
`workflows.executions.list`  
`workflows.locations.get`  
`workflows.locations.list`  
`workflows.operations.cancel`  
`workflows.operations.get`  
`workflows.operations.list`  
`workflows.workflows.create`  
`workflows.workflows.delete`  
`workflows.workflows.get`  
`workflows.workflows.getIamPolicy`  
`workflows.workflows.list`  
`workflows.workflows.setIamPolicy`  
`workflows.workflows.update`  
  
Workflows  |  Supported In Custom Roles  |  `workflows.executions.cancel`  
`workflows.executions.create`  
`workflows.executions.get`  
`workflows.executions.list`  
`workflows.locations.get`  
`workflows.locations.list`  
`workflows.operations.cancel`  
`workflows.operations.get`  
`workflows.operations.list`  
`workflows.workflows.create`  
`workflows.workflows.delete`  
`workflows.workflows.get`  
`workflows.workflows.getIamPolicy`  
`workflows.workflows.list`  
`workflows.workflows.setIamPolicy`  
`workflows.workflows.update`  
  
  
## Cloud IAM changes as of 2020-08-21

Service | Change | Description  
---|---|---  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.admin` (Dialogflow API Admin): `dialogflow.environments.lookupHistory`  
`dialogflow.versions.load`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.consoleAgentEditor` (Dialogflow Console Agent Editor): `dialogflow.environments.lookupHistory`  
`dialogflow.versions.load`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `dialogflow.environments.lookupHistory`  
`dialogflow.versions.load`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `dialogflow.environments.lookupHistory`  
`dialogflow.versions.load`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `dialogflow.environments.lookupHistory`  
  
Apigee  |  Added  |  `apigee.caches.delete`  
`apigee.caches.list`  
`apigee.canaryevaluations.create`  
`apigee.canaryevaluations.get`  
`apigee.datacollectors.create`  
`apigee.datacollectors.delete`  
`apigee.datacollectors.get`  
`apigee.datacollectors.list`  
`apigee.datacollectors.update`  
`apigee.datastores.create`  
`apigee.datastores.delete`  
`apigee.datastores.get`  
`apigee.datastores.list`  
`apigee.datastores.update`  
`apigee.envgroupattachments.create`  
`apigee.envgroupattachments.delete`  
`apigee.envgroupattachments.get`  
`apigee.envgroupattachments.list`  
`apigee.envgroups.create`  
`apigee.envgroups.delete`  
`apigee.envgroups.get`  
`apigee.envgroups.list`  
`apigee.envgroups.update`  
`apigee.exports.create`  
`apigee.exports.get`  
`apigee.exports.list`  
`apigee.hostqueries.create`  
`apigee.hostqueries.get`  
`apigee.hostqueries.list`  
`apigee.hoststats.get`  
`apigee.ingressconfigs.get`  
`apigee.instanceattachments.create`  
`apigee.instanceattachments.delete`  
`apigee.instanceattachments.get`  
`apigee.instanceattachments.list`  
`apigee.instances.create`  
`apigee.instances.delete`  
`apigee.instances.get`  
`apigee.instances.list`  
`apigee.instances.reportStatus`  
`apigee.operations.get`  
`apigee.operations.list`  
`apigee.projects.update`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.datastores.create`  
`apigee.datastores.delete`  
`apigee.datastores.get`  
`apigee.datastores.list`  
`apigee.datastores.update`  
`apigee.exports.create`  
`apigee.exports.get`  
`apigee.exports.list`  
  
Apigee  |  Now GA  |  `apigee.caches.delete`  
`apigee.caches.list`  
`apigee.canaryevaluations.create`  
`apigee.canaryevaluations.get`  
`apigee.datacollectors.create`  
`apigee.datacollectors.delete`  
`apigee.datacollectors.get`  
`apigee.datacollectors.list`  
`apigee.datacollectors.update`  
`apigee.datastores.create`  
`apigee.datastores.delete`  
`apigee.datastores.get`  
`apigee.datastores.list`  
`apigee.datastores.update`  
`apigee.envgroupattachments.create`  
`apigee.envgroupattachments.delete`  
`apigee.envgroupattachments.get`  
`apigee.envgroupattachments.list`  
`apigee.envgroups.create`  
`apigee.envgroups.delete`  
`apigee.envgroups.get`  
`apigee.envgroups.list`  
`apigee.envgroups.update`  
`apigee.exports.create`  
`apigee.exports.get`  
`apigee.exports.list`  
`apigee.hostqueries.create`  
`apigee.hostqueries.get`  
`apigee.hostqueries.list`  
`apigee.hoststats.get`  
`apigee.ingressconfigs.get`  
`apigee.instanceattachments.create`  
`apigee.instanceattachments.delete`  
`apigee.instanceattachments.get`  
`apigee.instanceattachments.list`  
`apigee.instances.create`  
`apigee.instances.delete`  
`apigee.instances.get`  
`apigee.instances.list`  
`apigee.instances.reportStatus`  
`apigee.operations.get`  
`apigee.operations.list`  
`apigee.projects.update`  
  
Compute Engine  |  Now GA  |  `compute.images.update`  
  
Dialogflow  |  Added  |  `dialogflow.agents.list`  
`dialogflow.agents.validate`  
`dialogflow.environments.create`  
`dialogflow.environments.delete`  
`dialogflow.environments.get`  
`dialogflow.environments.getHistory`  
`dialogflow.environments.list`  
`dialogflow.environments.lookupHistory`  
`dialogflow.environments.update`  
`dialogflow.flows.create`  
`dialogflow.flows.delete`  
`dialogflow.flows.get`  
`dialogflow.flows.list`  
`dialogflow.flows.train`  
`dialogflow.flows.update`  
`dialogflow.flows.validate`  
`dialogflow.pages.create`  
`dialogflow.pages.delete`  
`dialogflow.pages.get`  
`dialogflow.pages.list`  
`dialogflow.pages.update`  
`dialogflow.transitionRouteGroups.create`  
`dialogflow.transitionRouteGroups.delete`  
`dialogflow.transitionRouteGroups.get`  
`dialogflow.transitionRouteGroups.list`  
`dialogflow.transitionRouteGroups.update`  
`dialogflow.versions.create`  
`dialogflow.versions.delete`  
`dialogflow.versions.get`  
`dialogflow.versions.list`  
`dialogflow.versions.load`  
`dialogflow.versions.update`  
`dialogflow.webhooks.create`  
`dialogflow.webhooks.delete`  
`dialogflow.webhooks.get`  
`dialogflow.webhooks.list`  
`dialogflow.webhooks.update`  
  
Dialogflow  |  Supported In Custom Roles  |  `dialogflow.environments.create`  
`dialogflow.environments.delete`  
`dialogflow.environments.get`  
`dialogflow.environments.getHistory`  
`dialogflow.environments.list`  
`dialogflow.environments.update`  
`dialogflow.versions.create`  
`dialogflow.versions.delete`  
`dialogflow.versions.get`  
`dialogflow.versions.list`  
`dialogflow.versions.update`  
  
Dialogflow  |  Now GA  |  `dialogflow.agents.list`  
`dialogflow.agents.validate`  
`dialogflow.environments.create`  
`dialogflow.environments.delete`  
`dialogflow.environments.get`  
`dialogflow.environments.getHistory`  
`dialogflow.environments.list`  
`dialogflow.environments.update`  
`dialogflow.flows.create`  
`dialogflow.flows.delete`  
`dialogflow.flows.get`  
`dialogflow.flows.list`  
`dialogflow.flows.train`  
`dialogflow.flows.update`  
`dialogflow.flows.validate`  
`dialogflow.pages.create`  
`dialogflow.pages.delete`  
`dialogflow.pages.get`  
`dialogflow.pages.list`  
`dialogflow.pages.update`  
`dialogflow.transitionRouteGroups.create`  
`dialogflow.transitionRouteGroups.delete`  
`dialogflow.transitionRouteGroups.get`  
`dialogflow.transitionRouteGroups.list`  
`dialogflow.transitionRouteGroups.update`  
`dialogflow.versions.create`  
`dialogflow.versions.delete`  
`dialogflow.versions.get`  
`dialogflow.versions.list`  
`dialogflow.versions.update`  
`dialogflow.webhooks.create`  
`dialogflow.webhooks.delete`  
`dialogflow.webhooks.get`  
`dialogflow.webhooks.list`  
`dialogflow.webhooks.update`  
  
Cloud Healthcare API  |  Added  |  `healthcare.annotationStores.create`  
`healthcare.annotationStores.delete`  
`healthcare.annotationStores.evaluate`  
`healthcare.annotationStores.export`  
`healthcare.annotationStores.get`  
`healthcare.annotationStores.getIamPolicy`  
`healthcare.annotationStores.import`  
`healthcare.annotationStores.list`  
`healthcare.annotationStores.setIamPolicy`  
`healthcare.annotationStores.update`  
`healthcare.annotations.create`  
`healthcare.annotations.delete`  
`healthcare.annotations.get`  
`healthcare.annotations.list`  
`healthcare.annotations.update`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.annotationStores.create`  
`healthcare.annotationStores.delete`  
`healthcare.annotationStores.evaluate`  
`healthcare.annotationStores.export`  
`healthcare.annotationStores.get`  
`healthcare.annotationStores.getIamPolicy`  
`healthcare.annotationStores.import`  
`healthcare.annotationStores.list`  
`healthcare.annotationStores.setIamPolicy`  
`healthcare.annotationStores.update`  
`healthcare.annotations.create`  
`healthcare.annotations.delete`  
`healthcare.annotations.get`  
`healthcare.annotations.list`  
`healthcare.annotations.update`  
  
  
## Cloud IAM changes as of 2020-08-14

Service | Change | Description  
---|---|---  
Service Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/cloudprivatecatalog.consumer` (Catalog Consumer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Service Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/cloudprivatecatalogproducer.admin` (Catalog Admin): `cloudprivatecatalog.targets.get`  
`cloudprivatecatalogproducer.targets.associate`  
`cloudprivatecatalogproducer.targets.unassociate`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Service Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/cloudprivatecatalogproducer.manager` (Catalog Manager): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Dialogflow  |  Added  |  `dialogflow.fulfillments.get`  
`dialogflow.fulfillments.update`  
  
Dialogflow  |  Now GA  |  `dialogflow.fulfillments.get`  
`dialogflow.fulfillments.update`  
  
  
## Cloud IAM changes as of 2020-08-07

Service | Change | Description  
---|---|---  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.worker` (Composer Worker): `artifactregistry.packages.delete`  
`artifactregistry.repositories.create`  
`artifactregistry.repositories.delete`  
`artifactregistry.repositories.deleteArtifacts`  
`artifactregistry.repositories.getIamPolicy`  
`artifactregistry.repositories.setIamPolicy`  
`artifactregistry.repositories.update`  
`artifactregistry.tags.delete`  
`artifactregistry.versions.delete`  
  
GKE Hub  |  Role Updated  |  The following permissions have been added to the role `roles/gkehub.viewer` (GKE Hub Viewer): `gkehub.features.getIamPolicy`  
`gkehub.gateway.get`  
`gkehub.gateway.getIamPolicy`  
  
Cloud Logging  |  Now GA  |  The role `roles/logging.bucketWriter` (Logs Bucket Writer) is now GA.  
Cloud Logging  |  Now GA  |  The role `roles/logging.viewAccessor` (Logs View Accessor) is now GA.  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.privateLogViewer` (Private Logs Viewer): `logging.views.access`  
  
Compute Engine  |  Now GA  |  `compute.instances.getScreenshot`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `iam.serviceAccounts.disable`  
`iam.serviceAccounts.enable`  
`iam.serviceAccounts.undelete`  
  
Identity and Access Management  |  Now GA  |  `iam.serviceAccounts.disable`  
`iam.serviceAccounts.enable`  
`iam.serviceAccounts.undelete`  
  
Cloud Logging  |  Added  |  `logging.buckets.create`  
`logging.buckets.delete`  
`logging.buckets.undelete`  
`logging.buckets.write`  
`logging.views.access`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.buckets.create`  
`logging.buckets.delete`  
`logging.buckets.undelete`  
`logging.buckets.write`  
`logging.views.access`  
  
Cloud Logging  |  Now GA  |  `logging.buckets.create`  
`logging.buckets.delete`  
`logging.buckets.undelete`  
`logging.buckets.write`  
`logging.views.access`  
  
OAuthConfig  |  Added  |  `oauthconfig.clientpolicy.get`  
`oauthconfig.testusers.get`  
`oauthconfig.testusers.update`  
`oauthconfig.verification.get`  
`oauthconfig.verification.submit`  
`oauthconfig.verification.update`  
  
OAuthConfig  |  Supported In Custom Roles  |  `oauthconfig.clientpolicy.get`  
`oauthconfig.testusers.get`  
`oauthconfig.testusers.update`  
`oauthconfig.verification.get`  
`oauthconfig.verification.submit`  
`oauthconfig.verification.update`  
  
OAuthPolicyMetadata  |  Added  |  `oauthpolicymetadata.brandpolicy.createOrUpdate`  
`oauthpolicymetadata.brandpolicy.get`  
`oauthpolicymetadata.brandpolicy.submitVerification`  
`oauthpolicymetadata.clientpolicy.get`  
  
OAuthPolicyMetadata  |  Supported In Custom Roles  |  `oauthpolicymetadata.brandpolicy.createOrUpdate`  
`oauthpolicymetadata.brandpolicy.get`  
`oauthpolicymetadata.brandpolicy.submitVerification`  
`oauthpolicymetadata.clientpolicy.get`  
  
OAuthTestApp  |  Added  |  `oauthtestapp.userwhitelist.read`  
`oauthtestapp.userwhitelist.write`  
  
OAuthTestApp  |  Supported In Custom Roles  |  `oauthtestapp.userwhitelist.read`  
`oauthtestapp.userwhitelist.write`  
  
Certificate Authority Service  |  Added  |  `privateca.certificateAuthorities.create`  
`privateca.certificateAuthorities.delete`  
`privateca.certificateAuthorities.get`  
`privateca.certificateAuthorities.getIamPolicy`  
`privateca.certificateAuthorities.list`  
`privateca.certificateAuthorities.setIamPolicy`  
`privateca.certificateAuthorities.update`  
`privateca.certificateRevocationLists.create`  
`privateca.certificateRevocationLists.get`  
`privateca.certificateRevocationLists.getIamPolicy`  
`privateca.certificateRevocationLists.list`  
`privateca.certificateRevocationLists.setIamPolicy`  
`privateca.certificateRevocationLists.update`  
`privateca.certificates.create`  
`privateca.certificates.get`  
`privateca.certificates.getIamPolicy`  
`privateca.certificates.list`  
`privateca.certificates.setIamPolicy`  
`privateca.certificates.update`  
`privateca.locations.get`  
`privateca.locations.list`  
`privateca.operations.cancel`  
`privateca.operations.delete`  
`privateca.operations.get`  
`privateca.operations.list`  
`privateca.reusableConfigs.create`  
`privateca.reusableConfigs.delete`  
`privateca.reusableConfigs.get`  
`privateca.reusableConfigs.getIamPolicy`  
`privateca.reusableConfigs.list`  
`privateca.reusableConfigs.setIamPolicy`  
`privateca.reusableConfigs.update`  
  
Certificate Authority Service  |  Supported In Custom Roles  |  `privateca.certificateAuthorities.create`  
`privateca.certificateAuthorities.delete`  
`privateca.certificateAuthorities.get`  
`privateca.certificateAuthorities.getIamPolicy`  
`privateca.certificateAuthorities.list`  
`privateca.certificateAuthorities.setIamPolicy`  
`privateca.certificateAuthorities.update`  
`privateca.certificateRevocationLists.create`  
`privateca.certificateRevocationLists.get`  
`privateca.certificateRevocationLists.getIamPolicy`  
`privateca.certificateRevocationLists.list`  
`privateca.certificateRevocationLists.setIamPolicy`  
`privateca.certificateRevocationLists.update`  
`privateca.certificates.create`  
`privateca.certificates.get`  
`privateca.certificates.getIamPolicy`  
`privateca.certificates.list`  
`privateca.certificates.setIamPolicy`  
`privateca.certificates.update`  
`privateca.locations.get`  
`privateca.locations.list`  
`privateca.operations.cancel`  
`privateca.operations.delete`  
`privateca.operations.get`  
`privateca.operations.list`  
`privateca.reusableConfigs.create`  
`privateca.reusableConfigs.delete`  
`privateca.reusableConfigs.get`  
`privateca.reusableConfigs.getIamPolicy`  
`privateca.reusableConfigs.list`  
`privateca.reusableConfigs.setIamPolicy`  
`privateca.reusableConfigs.update`  
  
Recommender  |  Added  |  `recommender.commitmentUtilizationInsights.get`  
`recommender.commitmentUtilizationInsights.list`  
`recommender.commitmentUtilizationInsights.update`  
`recommender.usageCommitmentRecommendations.get`  
`recommender.usageCommitmentRecommendations.list`  
`recommender.usageCommitmentRecommendations.update`  
  
  
## Cloud IAM changes as of 2020-07-31

Service | Change | Description  
---|---|---  
Apigee  |  Now GA  |  The role `roles/apigee.admin` (Apigee Organization Admin) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.analyticsAgent` (Apigee Analytics Agent) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.analyticsEditor` (Apigee Analytics Editor) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.analyticsViewer` (Apigee Analytics Viewer) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.apiCreator` (Apigee API Creator) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.deployer` (Apigee Deployer) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.developerAdmin` (Apigee Developer Admin) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.readOnlyAdmin` (Apigee Read-only Admin) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.runtimeAgent` (Apigee Runtime Agent) is now GA.  
Apigee  |  Now GA  |  The role `roles/apigee.synchronizerManager` (Apigee Synchronizer Manager) is now GA.  
Apigee Connect  |  Now GA  |  The role `roles/apigeeconnect.Admin` (Apigee Connect Admin) is now GA.  
Apigee Connect  |  Now GA  |  The role `roles/apigeeconnect.Agent` (Apigee Connect Agent) is now GA.  
Game Servers  |  Now GA  |  The role `roles/gameservices.admin` (Game Services API Admin) is now GA.  
Game Servers  |  Now GA  |  The role `roles/gameservices.viewer` (Game Services API Viewer) is now GA.  
Identity and Access Management  |  Role Updated  |  The following permissions have been removed from the role `roles/iam.securityAdmin` (Security Admin): `container.secrets.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been removed from the role `roles/iam.securityReviewer` (Security Reviewer): `container.secrets.list`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.admin` (Notebooks Admin): `compute.acceleratorTypes.get`  
`compute.addresses.get`  
`compute.addresses.list`  
`compute.autoscalers.get`  
`compute.autoscalers.list`  
`compute.backendBuckets.get`  
`compute.backendBuckets.list`  
`compute.backendServices.get`  
`compute.backendServices.list`  
`compute.commitments.get`  
`compute.commitments.list`  
`compute.diskTypes.get`  
`compute.disks.get`  
`compute.disks.getIamPolicy`  
`compute.disks.list`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.firewalls.get`  
`compute.firewalls.list`  
`compute.forwardingRules.get`  
`compute.forwardingRules.list`  
`compute.globalAddresses.get`  
`compute.globalAddresses.list`  
`compute.globalForwardingRules.get`  
`compute.globalForwardingRules.list`  
`compute.globalOperations.get`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.list`  
`compute.globalPublicDelegatedPrefixes.get`  
`compute.globalPublicDelegatedPrefixes.list`  
`compute.healthChecks.get`  
`compute.healthChecks.list`  
`compute.httpHealthChecks.get`  
`compute.httpHealthChecks.list`  
`compute.httpsHealthChecks.get`  
`compute.httpsHealthChecks.list`  
`compute.images.get`  
`compute.images.getFromFamily`  
`compute.images.getIamPolicy`  
`compute.images.list`  
`compute.instanceGroupManagers.get`  
`compute.instanceGroupManagers.list`  
`compute.instanceGroups.get`  
`compute.instanceGroups.list`  
`compute.instanceTemplates.get`  
`compute.instanceTemplates.getIamPolicy`  
`compute.instanceTemplates.list`  
`compute.instances.get`  
`compute.instances.getEffectiveFirewalls`  
`compute.instances.getGuestAttributes`  
`compute.instances.getIamPolicy`  
`compute.instances.getScreenshot`  
`compute.instances.getSerialPortOutput`  
`compute.instances.getShieldedInstanceIdentity`  
`compute.instances.getShieldedVmIdentity`  
`compute.instances.list`  
`compute.instances.listReferrers`  
`compute.interconnectAttachments.get`  
`compute.interconnectAttachments.list`  
`compute.interconnectLocations.get`  
`compute.interconnectLocations.list`  
`compute.interconnects.get`  
`compute.interconnects.list`  
`compute.licenseCodes.get`  
`compute.licenseCodes.getIamPolicy`  
`compute.licenseCodes.list`  
`compute.licenses.get`  
`compute.licenses.getIamPolicy`  
`compute.licenses.list`  
`compute.machineTypes.get`  
`compute.maintenancePolicies.get`  
`compute.maintenancePolicies.getIamPolicy`  
`compute.maintenancePolicies.list`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.getIamPolicy`  
`compute.networkEndpointGroups.list`  
`compute.networks.get`  
`compute.networks.getEffectiveFirewalls`  
`compute.networks.list`  
`compute.networks.listPeeringRoutes`  
`compute.nodeGroups.get`  
`compute.nodeGroups.getIamPolicy`  
`compute.nodeGroups.list`  
`compute.nodeTemplates.get`  
`compute.nodeTemplates.getIamPolicy`  
`compute.nodeTemplates.list`  
`compute.nodeTypes.get`  
`compute.nodeTypes.list`  
`compute.organizations.listAssociations`  
`compute.projects.get`  
`compute.publicAdvertisedPrefixes.get`  
`compute.publicAdvertisedPrefixes.list`  
`compute.publicDelegatedPrefixes.get`  
`compute.publicDelegatedPrefixes.list`  
`compute.regionBackendServices.get`  
`compute.regionBackendServices.list`  
`compute.regionHealthCheckServices.get`  
`compute.regionHealthCheckServices.list`  
`compute.regionNotificationEndpoints.get`  
`compute.regionNotificationEndpoints.list`  
`compute.regionOperations.get`  
`compute.regionOperations.getIamPolicy`  
`compute.regionOperations.list`  
`compute.regions.get`  
`compute.regions.list`  
`compute.reservations.get`  
`compute.reservations.list`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.routers.get`  
`compute.routers.list`  
`compute.routes.get`  
`compute.routes.list`  
`compute.securityPolicies.get`  
`compute.securityPolicies.getIamPolicy`  
`compute.securityPolicies.list`  
`compute.snapshots.get`  
`compute.snapshots.getIamPolicy`  
`compute.snapshots.list`  
`compute.sslCertificates.get`  
`compute.sslCertificates.list`  
`compute.sslPolicies.get`  
`compute.sslPolicies.list`  
`compute.sslPolicies.listAvailableFeatures`  
`compute.subnetworks.get`  
`compute.subnetworks.getIamPolicy`  
`compute.targetHttpProxies.get`  
`compute.targetHttpProxies.list`  
`compute.targetHttpsProxies.get`  
`compute.targetHttpsProxies.list`  
`compute.targetInstances.get`  
`compute.targetInstances.list`  
`compute.targetPools.get`  
`compute.targetPools.list`  
`compute.targetSslProxies.get`  
`compute.targetSslProxies.list`  
`compute.targetTcpProxies.get`  
`compute.targetTcpProxies.list`  
`compute.targetVpnGateways.get`  
`compute.targetVpnGateways.list`  
`compute.urlMaps.get`  
`compute.urlMaps.list`  
`compute.urlMaps.validate`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnTunnels.get`  
`compute.vpnTunnels.list`  
`compute.zoneOperations.get`  
`compute.zoneOperations.getIamPolicy`  
`compute.zoneOperations.list`  
`compute.zones.get`  
`compute.zones.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.runner` (Notebooks Runner): `compute.acceleratorTypes.get`  
`compute.addresses.get`  
`compute.addresses.list`  
`compute.autoscalers.get`  
`compute.autoscalers.list`  
`compute.backendBuckets.get`  
`compute.backendBuckets.list`  
`compute.backendServices.get`  
`compute.backendServices.list`  
`compute.commitments.get`  
`compute.commitments.list`  
`compute.diskTypes.get`  
`compute.disks.get`  
`compute.disks.getIamPolicy`  
`compute.disks.list`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.firewalls.get`  
`compute.firewalls.list`  
`compute.forwardingRules.get`  
`compute.forwardingRules.list`  
`compute.globalAddresses.get`  
`compute.globalAddresses.list`  
`compute.globalForwardingRules.get`  
`compute.globalForwardingRules.list`  
`compute.globalOperations.get`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.list`  
`compute.globalPublicDelegatedPrefixes.get`  
`compute.globalPublicDelegatedPrefixes.list`  
`compute.healthChecks.get`  
`compute.healthChecks.list`  
`compute.httpHealthChecks.get`  
`compute.httpHealthChecks.list`  
`compute.httpsHealthChecks.get`  
`compute.httpsHealthChecks.list`  
`compute.images.get`  
`compute.images.getFromFamily`  
`compute.images.getIamPolicy`  
`compute.images.list`  
`compute.instanceGroupManagers.get`  
`compute.instanceGroupManagers.list`  
`compute.instanceGroups.get`  
`compute.instanceGroups.list`  
`compute.instanceTemplates.get`  
`compute.instanceTemplates.getIamPolicy`  
`compute.instanceTemplates.list`  
`compute.instances.get`  
`compute.instances.getEffectiveFirewalls`  
`compute.instances.getGuestAttributes`  
`compute.instances.getIamPolicy`  
`compute.instances.getScreenshot`  
`compute.instances.getSerialPortOutput`  
`compute.instances.getShieldedInstanceIdentity`  
`compute.instances.getShieldedVmIdentity`  
`compute.instances.list`  
`compute.instances.listReferrers`  
`compute.interconnectAttachments.get`  
`compute.interconnectAttachments.list`  
`compute.interconnectLocations.get`  
`compute.interconnectLocations.list`  
`compute.interconnects.get`  
`compute.interconnects.list`  
`compute.licenseCodes.get`  
`compute.licenseCodes.getIamPolicy`  
`compute.licenseCodes.list`  
`compute.licenses.get`  
`compute.licenses.getIamPolicy`  
`compute.licenses.list`  
`compute.machineTypes.get`  
`compute.maintenancePolicies.get`  
`compute.maintenancePolicies.getIamPolicy`  
`compute.maintenancePolicies.list`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.getIamPolicy`  
`compute.networkEndpointGroups.list`  
`compute.networks.get`  
`compute.networks.getEffectiveFirewalls`  
`compute.networks.list`  
`compute.networks.listPeeringRoutes`  
`compute.nodeGroups.get`  
`compute.nodeGroups.getIamPolicy`  
`compute.nodeGroups.list`  
`compute.nodeTemplates.get`  
`compute.nodeTemplates.getIamPolicy`  
`compute.nodeTemplates.list`  
`compute.nodeTypes.get`  
`compute.nodeTypes.list`  
`compute.organizations.listAssociations`  
`compute.projects.get`  
`compute.publicAdvertisedPrefixes.get`  
`compute.publicAdvertisedPrefixes.list`  
`compute.publicDelegatedPrefixes.get`  
`compute.publicDelegatedPrefixes.list`  
`compute.regionBackendServices.get`  
`compute.regionBackendServices.list`  
`compute.regionHealthCheckServices.get`  
`compute.regionHealthCheckServices.list`  
`compute.regionNotificationEndpoints.get`  
`compute.regionNotificationEndpoints.list`  
`compute.regionOperations.get`  
`compute.regionOperations.getIamPolicy`  
`compute.regionOperations.list`  
`compute.regions.get`  
`compute.regions.list`  
`compute.reservations.get`  
`compute.reservations.list`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.routers.get`  
`compute.routers.list`  
`compute.routes.get`  
`compute.routes.list`  
`compute.securityPolicies.get`  
`compute.securityPolicies.getIamPolicy`  
`compute.securityPolicies.list`  
`compute.snapshots.get`  
`compute.snapshots.getIamPolicy`  
`compute.snapshots.list`  
`compute.sslCertificates.get`  
`compute.sslCertificates.list`  
`compute.sslPolicies.get`  
`compute.sslPolicies.list`  
`compute.sslPolicies.listAvailableFeatures`  
`compute.subnetworks.get`  
`compute.subnetworks.getIamPolicy`  
`compute.targetHttpProxies.get`  
`compute.targetHttpProxies.list`  
`compute.targetHttpsProxies.get`  
`compute.targetHttpsProxies.list`  
`compute.targetInstances.get`  
`compute.targetInstances.list`  
`compute.targetPools.get`  
`compute.targetPools.list`  
`compute.targetSslProxies.get`  
`compute.targetSslProxies.list`  
`compute.targetTcpProxies.get`  
`compute.targetTcpProxies.list`  
`compute.targetVpnGateways.get`  
`compute.targetVpnGateways.list`  
`compute.urlMaps.get`  
`compute.urlMaps.list`  
`compute.urlMaps.validate`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnTunnels.get`  
`compute.vpnTunnels.list`  
`compute.zoneOperations.get`  
`compute.zoneOperations.getIamPolicy`  
`compute.zoneOperations.list`  
`compute.zones.get`  
`compute.zones.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.viewer` (Notebooks Viewer): `compute.acceleratorTypes.get`  
`compute.addresses.get`  
`compute.addresses.list`  
`compute.autoscalers.get`  
`compute.autoscalers.list`  
`compute.backendBuckets.get`  
`compute.backendBuckets.list`  
`compute.backendServices.get`  
`compute.backendServices.list`  
`compute.commitments.get`  
`compute.commitments.list`  
`compute.diskTypes.get`  
`compute.disks.get`  
`compute.disks.getIamPolicy`  
`compute.disks.list`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.firewalls.get`  
`compute.firewalls.list`  
`compute.forwardingRules.get`  
`compute.forwardingRules.list`  
`compute.globalAddresses.get`  
`compute.globalAddresses.list`  
`compute.globalForwardingRules.get`  
`compute.globalForwardingRules.list`  
`compute.globalOperations.get`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.list`  
`compute.globalPublicDelegatedPrefixes.get`  
`compute.globalPublicDelegatedPrefixes.list`  
`compute.healthChecks.get`  
`compute.healthChecks.list`  
`compute.httpHealthChecks.get`  
`compute.httpHealthChecks.list`  
`compute.httpsHealthChecks.get`  
`compute.httpsHealthChecks.list`  
`compute.images.get`  
`compute.images.getFromFamily`  
`compute.images.getIamPolicy`  
`compute.images.list`  
`compute.instanceGroupManagers.get`  
`compute.instanceGroupManagers.list`  
`compute.instanceGroups.get`  
`compute.instanceGroups.list`  
`compute.instanceTemplates.get`  
`compute.instanceTemplates.getIamPolicy`  
`compute.instanceTemplates.list`  
`compute.instances.get`  
`compute.instances.getEffectiveFirewalls`  
`compute.instances.getGuestAttributes`  
`compute.instances.getIamPolicy`  
`compute.instances.getScreenshot`  
`compute.instances.getSerialPortOutput`  
`compute.instances.getShieldedInstanceIdentity`  
`compute.instances.getShieldedVmIdentity`  
`compute.instances.list`  
`compute.instances.listReferrers`  
`compute.interconnectAttachments.get`  
`compute.interconnectAttachments.list`  
`compute.interconnectLocations.get`  
`compute.interconnectLocations.list`  
`compute.interconnects.get`  
`compute.interconnects.list`  
`compute.licenseCodes.get`  
`compute.licenseCodes.getIamPolicy`  
`compute.licenseCodes.list`  
`compute.licenses.get`  
`compute.licenses.getIamPolicy`  
`compute.licenses.list`  
`compute.machineTypes.get`  
`compute.maintenancePolicies.get`  
`compute.maintenancePolicies.getIamPolicy`  
`compute.maintenancePolicies.list`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.getIamPolicy`  
`compute.networkEndpointGroups.list`  
`compute.networks.get`  
`compute.networks.getEffectiveFirewalls`  
`compute.networks.list`  
`compute.networks.listPeeringRoutes`  
`compute.nodeGroups.get`  
`compute.nodeGroups.getIamPolicy`  
`compute.nodeGroups.list`  
`compute.nodeTemplates.get`  
`compute.nodeTemplates.getIamPolicy`  
`compute.nodeTemplates.list`  
`compute.nodeTypes.get`  
`compute.nodeTypes.list`  
`compute.organizations.listAssociations`  
`compute.projects.get`  
`compute.publicAdvertisedPrefixes.get`  
`compute.publicAdvertisedPrefixes.list`  
`compute.publicDelegatedPrefixes.get`  
`compute.publicDelegatedPrefixes.list`  
`compute.regionBackendServices.get`  
`compute.regionBackendServices.list`  
`compute.regionHealthCheckServices.get`  
`compute.regionHealthCheckServices.list`  
`compute.regionNotificationEndpoints.get`  
`compute.regionNotificationEndpoints.list`  
`compute.regionOperations.get`  
`compute.regionOperations.getIamPolicy`  
`compute.regionOperations.list`  
`compute.regions.get`  
`compute.regions.list`  
`compute.reservations.get`  
`compute.reservations.list`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.routers.get`  
`compute.routers.list`  
`compute.routes.get`  
`compute.routes.list`  
`compute.securityPolicies.get`  
`compute.securityPolicies.getIamPolicy`  
`compute.securityPolicies.list`  
`compute.snapshots.get`  
`compute.snapshots.getIamPolicy`  
`compute.snapshots.list`  
`compute.sslCertificates.get`  
`compute.sslCertificates.list`  
`compute.sslPolicies.get`  
`compute.sslPolicies.list`  
`compute.sslPolicies.listAvailableFeatures`  
`compute.subnetworks.get`  
`compute.subnetworks.getIamPolicy`  
`compute.targetHttpProxies.get`  
`compute.targetHttpProxies.list`  
`compute.targetHttpsProxies.get`  
`compute.targetHttpsProxies.list`  
`compute.targetInstances.get`  
`compute.targetInstances.list`  
`compute.targetPools.get`  
`compute.targetPools.list`  
`compute.targetSslProxies.get`  
`compute.targetSslProxies.list`  
`compute.targetTcpProxies.get`  
`compute.targetTcpProxies.list`  
`compute.targetVpnGateways.get`  
`compute.targetVpnGateways.list`  
`compute.urlMaps.get`  
`compute.urlMaps.list`  
`compute.urlMaps.validate`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnTunnels.get`  
`compute.vpnTunnels.list`  
`compute.zoneOperations.get`  
`compute.zoneOperations.getIamPolicy`  
`compute.zoneOperations.list`  
`compute.zones.get`  
`compute.zones.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Apigee  |  Now GA  |  `apigee.apiproductattributes.createOrUpdateAll`  
`apigee.apiproductattributes.delete`  
`apigee.apiproductattributes.get`  
`apigee.apiproductattributes.list`  
`apigee.apiproductattributes.update`  
`apigee.apiproducts.create`  
`apigee.apiproducts.delete`  
`apigee.apiproducts.get`  
`apigee.apiproducts.list`  
`apigee.apiproducts.update`  
`apigee.appkeys.create`  
`apigee.appkeys.delete`  
`apigee.appkeys.get`  
`apigee.appkeys.manage`  
`apigee.apps.get`  
`apigee.apps.list`  
`apigee.deployments.create`  
`apigee.deployments.delete`  
`apigee.deployments.get`  
`apigee.deployments.list`  
`apigee.deployments.update`  
`apigee.developerappattributes.createOrUpdateAll`  
`apigee.developerappattributes.delete`  
`apigee.developerappattributes.get`  
`apigee.developerappattributes.list`  
`apigee.developerappattributes.update`  
`apigee.developerapps.create`  
`apigee.developerapps.delete`  
`apigee.developerapps.get`  
`apigee.developerapps.list`  
`apigee.developerapps.manage`  
`apigee.developerattributes.createOrUpdateAll`  
`apigee.developerattributes.delete`  
`apigee.developerattributes.get`  
`apigee.developerattributes.list`  
`apigee.developerattributes.update`  
`apigee.developers.create`  
`apigee.developers.delete`  
`apigee.developers.get`  
`apigee.developers.list`  
`apigee.developers.update`  
`apigee.environments.create`  
`apigee.environments.delete`  
`apigee.environments.get`  
`apigee.environments.getDataLocation`  
`apigee.environments.getIamPolicy`  
`apigee.environments.getStats`  
`apigee.environments.list`  
`apigee.environments.manageRuntime`  
`apigee.environments.setIamPolicy`  
`apigee.environments.update`  
`apigee.flowhooks.attachSharedFlow`  
`apigee.flowhooks.detachSharedFlow`  
`apigee.flowhooks.getSharedFlow`  
`apigee.flowhooks.list`  
`apigee.keystorealiases.create`  
`apigee.keystorealiases.delete`  
`apigee.keystorealiases.exportCertificate`  
`apigee.keystorealiases.generateCSR`  
`apigee.keystorealiases.get`  
`apigee.keystorealiases.list`  
`apigee.keystorealiases.update`  
`apigee.keystores.create`  
`apigee.keystores.delete`  
`apigee.keystores.export`  
`apigee.keystores.get`  
`apigee.keystores.list`  
`apigee.keyvaluemaps.create`  
`apigee.keyvaluemaps.delete`  
`apigee.keyvaluemaps.list`  
`apigee.maskconfigs.get`  
`apigee.maskconfigs.update`  
`apigee.organizations.create`  
`apigee.organizations.get`  
`apigee.organizations.list`  
`apigee.organizations.update`  
`apigee.proxies.create`  
`apigee.proxies.delete`  
`apigee.proxies.get`  
`apigee.proxies.list`  
`apigee.proxyrevisions.delete`  
`apigee.proxyrevisions.deploy`  
`apigee.proxyrevisions.get`  
`apigee.proxyrevisions.list`  
`apigee.proxyrevisions.undeploy`  
`apigee.proxyrevisions.update`  
`apigee.queries.create`  
`apigee.queries.get`  
`apigee.queries.list`  
`apigee.references.create`  
`apigee.references.delete`  
`apigee.references.get`  
`apigee.references.list`  
`apigee.references.update`  
`apigee.reports.create`  
`apigee.reports.delete`  
`apigee.reports.get`  
`apigee.reports.list`  
`apigee.reports.update`  
`apigee.resourcefiles.create`  
`apigee.resourcefiles.delete`  
`apigee.resourcefiles.get`  
`apigee.resourcefiles.list`  
`apigee.resourcefiles.update`  
`apigee.sharedflowrevisions.delete`  
`apigee.sharedflowrevisions.deploy`  
`apigee.sharedflowrevisions.get`  
`apigee.sharedflowrevisions.list`  
`apigee.sharedflowrevisions.undeploy`  
`apigee.sharedflowrevisions.update`  
`apigee.sharedflows.create`  
`apigee.sharedflows.delete`  
`apigee.sharedflows.get`  
`apigee.sharedflows.list`  
`apigee.targetservers.create`  
`apigee.targetservers.delete`  
`apigee.targetservers.get`  
`apigee.targetservers.list`  
`apigee.targetservers.update`  
`apigee.tracesessions.create`  
`apigee.tracesessions.delete`  
`apigee.tracesessions.get`  
`apigee.tracesessions.list`  
  
Apigee Connect  |  Now GA  |  `apigeeconnect.connections.list`  
`apigeeconnect.endpoints.connect`  
  
Recommendations  |  Added  |  `automlrecommendations.events.rejoin`  
`automlrecommendations.placements.create`  
`automlrecommendations.placements.delete`  
`automlrecommendations.recommendations.create`  
`automlrecommendations.recommendations.delete`  
`automlrecommendations.recommendations.pause`  
`automlrecommendations.recommendations.resume`  
`automlrecommendations.recommendations.update`  
  
Recommendations  |  Supported In Custom Roles  |  `automlrecommendations.events.rejoin`  
`automlrecommendations.placements.create`  
`automlrecommendations.placements.delete`  
`automlrecommendations.placements.list`  
`automlrecommendations.recommendations.create`  
`automlrecommendations.recommendations.delete`  
`automlrecommendations.recommendations.pause`  
`automlrecommendations.recommendations.resume`  
`automlrecommendations.recommendations.update`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.tables.setCategory`  
  
Game Servers  |  Now GA  |  `gameservices.gameServerClusters.create`  
`gameservices.gameServerClusters.delete`  
`gameservices.gameServerClusters.get`  
`gameservices.gameServerClusters.list`  
`gameservices.gameServerClusters.update`  
`gameservices.gameServerConfigs.create`  
`gameservices.gameServerConfigs.delete`  
`gameservices.gameServerConfigs.get`  
`gameservices.gameServerConfigs.list`  
`gameservices.gameServerDeployments.create`  
`gameservices.gameServerDeployments.delete`  
`gameservices.gameServerDeployments.get`  
`gameservices.gameServerDeployments.list`  
`gameservices.gameServerDeployments.rollout`  
`gameservices.gameServerDeployments.update`  
`gameservices.locations.get`  
`gameservices.locations.list`  
`gameservices.operations.cancel`  
`gameservices.operations.delete`  
`gameservices.operations.get`  
`gameservices.operations.list`  
`gameservices.realms.create`  
`gameservices.realms.delete`  
`gameservices.realms.get`  
`gameservices.realms.list`  
`gameservices.realms.update`  
  
Cloud Healthcare API  |  Added  |  `healthcare.hl7V2Stores.import`  
`healthcare.locations.get`  
`healthcare.locations.list`  
  
Identity and Access Management  |  Added  |  `iam.serviceAccounts.disable`  
`iam.serviceAccounts.enable`  
`iam.serviceAccounts.undelete`  
  
Identity and Access Management  |  Available In Custom Roles  |  `iam.serviceAccounts.undelete`  
  
Notebooks  |  Added  |  `notebooks.instances.checkUpgradability`  
`notebooks.instances.reset`  
`notebooks.instances.setAccelerator`  
`notebooks.instances.setLabels`  
`notebooks.instances.setMachineType`  
`notebooks.instances.start`  
`notebooks.instances.stop`  
`notebooks.instances.upgrade`  
  
  
## Cloud IAM changes as of 2020-07-24

Service | Change | Description  
---|---|---  
Identity and Access Management  |  Role Updated  |  The following permissions have been removed from the role `roles/iam.securityAdmin` (Security Admin): `container.secrets.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been removed from the role `roles/iam.securityReviewer` (Security Reviewer): `container.secrets.list`  
  
  
## Cloud IAM changes as of 2020-07-17

Service | Change | Description  
---|---|---  
GKE Hub  |  Now GA  |  The role `roles/gkehub.gatewayAdmin` (Connect Gateway Admin) is now GA.  
Secret Manager  |  Now GA  |  The role `roles/secretmanager.secretVersionAdder` (Secret Manager Secret Version Adder) is now GA.  
Secret Manager  |  Now GA  |  The role `roles/secretmanager.secretVersionManager` (Secret Manager Secret Version Manager) is now GA.  
Bigtable  |  Added  |  `bigtable.backups.create`  
`bigtable.backups.delete`  
`bigtable.backups.get`  
`bigtable.backups.getIamPolicy`  
`bigtable.backups.list`  
`bigtable.backups.restore`  
`bigtable.backups.setIamPolicy`  
`bigtable.backups.update`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.backups.create`  
`bigtable.backups.delete`  
`bigtable.backups.get`  
`bigtable.backups.getIamPolicy`  
`bigtable.backups.list`  
`bigtable.backups.restore`  
`bigtable.backups.setIamPolicy`  
`bigtable.backups.update`  
  
Bigtable  |  Now GA  |  `bigtable.backups.create`  
`bigtable.backups.delete`  
`bigtable.backups.get`  
`bigtable.backups.getIamPolicy`  
`bigtable.backups.list`  
`bigtable.backups.restore`  
`bigtable.backups.setIamPolicy`  
`bigtable.backups.update`  
  
Cloud Commerce Consumer Procurement  |  Added  |  `consumerprocurement.accounts.create`  
`consumerprocurement.accounts.delete`  
`consumerprocurement.accounts.get`  
`consumerprocurement.accounts.list`  
`consumerprocurement.entitlements.get`  
`consumerprocurement.entitlements.list`  
`consumerprocurement.freeTrials.create`  
`consumerprocurement.freeTrials.get`  
`consumerprocurement.freeTrials.list`  
`consumerprocurement.orders.cancel`  
`consumerprocurement.orders.get`  
`consumerprocurement.orders.list`  
`consumerprocurement.orders.modify`  
`consumerprocurement.orders.place`  
  
Cloud Commerce Consumer Procurement  |  Supported In Custom Roles  |  `consumerprocurement.accounts.create`  
`consumerprocurement.accounts.delete`  
`consumerprocurement.accounts.get`  
`consumerprocurement.accounts.list`  
`consumerprocurement.entitlements.get`  
`consumerprocurement.entitlements.list`  
`consumerprocurement.freeTrials.create`  
`consumerprocurement.freeTrials.get`  
`consumerprocurement.freeTrials.list`  
`consumerprocurement.orders.cancel`  
`consumerprocurement.orders.get`  
`consumerprocurement.orders.list`  
`consumerprocurement.orders.modify`  
`consumerprocurement.orders.place`  
  
GKE Hub  |  Added  |  `gkehub.gateway.delete`  
`gkehub.gateway.get`  
`gkehub.gateway.getIamPolicy`  
`gkehub.gateway.patch`  
`gkehub.gateway.post`  
`gkehub.gateway.put`  
`gkehub.gateway.setIamPolicy`  
  
GKE Hub  |  Now GA  |  `gkehub.gateway.delete`  
`gkehub.gateway.get`  
`gkehub.gateway.getIamPolicy`  
`gkehub.gateway.patch`  
`gkehub.gateway.post`  
`gkehub.gateway.put`  
`gkehub.gateway.setIamPolicy`  
  
  
## Cloud IAM changes as of 2020-07-10

Service | Change | Description  
---|---|---  
Cloud Monitoring  |  Now GA  |  The role `roles/monitoring.servicesEditor` (Monitoring Services Editor) is now GA.  
Cloud Monitoring  |  Now GA  |  The role `roles/monitoring.servicesViewer` (Monitoring Services Viewer) is now GA.  
NetApp Cloud Volumes Service  |  Added  |  `cloudvolumesgcp-api.netapp.com/activeDirectories.create`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.delete`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.get`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.list`  
`cloudvolumesgcp-api.netapp.com/activeDirectories.update`  
`cloudvolumesgcp-api.netapp.com/ipRanges.list`  
`cloudvolumesgcp-api.netapp.com/jobs.get`  
`cloudvolumesgcp-api.netapp.com/jobs.list`  
`cloudvolumesgcp-api.netapp.com/regions.list`  
`cloudvolumesgcp-api.netapp.com/serviceLevels.list`  
`cloudvolumesgcp-api.netapp.com/snapshots.create`  
`cloudvolumesgcp-api.netapp.com/snapshots.delete`  
`cloudvolumesgcp-api.netapp.com/snapshots.get`  
`cloudvolumesgcp-api.netapp.com/snapshots.list`  
`cloudvolumesgcp-api.netapp.com/snapshots.update`  
`cloudvolumesgcp-api.netapp.com/volumes.create`  
`cloudvolumesgcp-api.netapp.com/volumes.delete`  
`cloudvolumesgcp-api.netapp.com/volumes.get`  
`cloudvolumesgcp-api.netapp.com/volumes.list`  
`cloudvolumesgcp-api.netapp.com/volumes.update`  
  
Cloud Monitoring  |  Added  |  `monitoring.services.create`  
`monitoring.services.delete`  
`monitoring.services.get`  
`monitoring.services.list`  
`monitoring.services.update`  
`monitoring.slos.create`  
`monitoring.slos.delete`  
`monitoring.slos.get`  
`monitoring.slos.list`  
`monitoring.slos.update`  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `monitoring.services.create`  
`monitoring.services.delete`  
`monitoring.services.get`  
`monitoring.services.list`  
`monitoring.services.update`  
`monitoring.slos.create`  
`monitoring.slos.delete`  
`monitoring.slos.get`  
`monitoring.slos.list`  
`monitoring.slos.update`  
  
Cloud Monitoring  |  Now GA  |  `monitoring.services.create`  
`monitoring.services.delete`  
`monitoring.services.get`  
`monitoring.services.list`  
`monitoring.services.update`  
`monitoring.slos.create`  
`monitoring.slos.delete`  
`monitoring.slos.get`  
`monitoring.slos.list`  
`monitoring.slos.update`  
  
Network Security  |  Added  |  `networksecurity.authorizationPolicies.create`  
`networksecurity.authorizationPolicies.delete`  
`networksecurity.authorizationPolicies.get`  
`networksecurity.authorizationPolicies.getIamPolicy`  
`networksecurity.authorizationPolicies.list`  
`networksecurity.authorizationPolicies.setIamPolicy`  
`networksecurity.authorizationPolicies.update`  
`networksecurity.authorizationPolicies.use`  
`networksecurity.clientTlsPolicies.create`  
`networksecurity.clientTlsPolicies.delete`  
`networksecurity.clientTlsPolicies.get`  
`networksecurity.clientTlsPolicies.getIamPolicy`  
`networksecurity.clientTlsPolicies.list`  
`networksecurity.clientTlsPolicies.setIamPolicy`  
`networksecurity.clientTlsPolicies.update`  
`networksecurity.clientTlsPolicies.use`  
`networksecurity.locations.get`  
`networksecurity.locations.list`  
`networksecurity.operations.cancel`  
`networksecurity.operations.delete`  
`networksecurity.operations.get`  
`networksecurity.operations.list`  
`networksecurity.serverTlsPolicies.create`  
`networksecurity.serverTlsPolicies.delete`  
`networksecurity.serverTlsPolicies.get`  
`networksecurity.serverTlsPolicies.getIamPolicy`  
`networksecurity.serverTlsPolicies.list`  
`networksecurity.serverTlsPolicies.setIamPolicy`  
`networksecurity.serverTlsPolicies.update`  
`networksecurity.serverTlsPolicies.use`  
  
Network Security  |  Supported In Custom Roles  |  `networksecurity.authorizationPolicies.create`  
`networksecurity.authorizationPolicies.delete`  
`networksecurity.authorizationPolicies.get`  
`networksecurity.authorizationPolicies.getIamPolicy`  
`networksecurity.authorizationPolicies.list`  
`networksecurity.authorizationPolicies.setIamPolicy`  
`networksecurity.authorizationPolicies.update`  
`networksecurity.authorizationPolicies.use`  
`networksecurity.clientTlsPolicies.create`  
`networksecurity.clientTlsPolicies.delete`  
`networksecurity.clientTlsPolicies.get`  
`networksecurity.clientTlsPolicies.getIamPolicy`  
`networksecurity.clientTlsPolicies.list`  
`networksecurity.clientTlsPolicies.setIamPolicy`  
`networksecurity.clientTlsPolicies.update`  
`networksecurity.clientTlsPolicies.use`  
`networksecurity.locations.get`  
`networksecurity.locations.list`  
`networksecurity.operations.cancel`  
`networksecurity.operations.delete`  
`networksecurity.operations.get`  
`networksecurity.operations.list`  
`networksecurity.serverTlsPolicies.create`  
`networksecurity.serverTlsPolicies.delete`  
`networksecurity.serverTlsPolicies.get`  
`networksecurity.serverTlsPolicies.getIamPolicy`  
`networksecurity.serverTlsPolicies.list`  
`networksecurity.serverTlsPolicies.setIamPolicy`  
`networksecurity.serverTlsPolicies.update`  
`networksecurity.serverTlsPolicies.use`  
  
Network Services  |  Added  |  `networkservices.endpointConfigSelectors.create`  
`networkservices.endpointConfigSelectors.delete`  
`networkservices.endpointConfigSelectors.get`  
`networkservices.endpointConfigSelectors.getIamPolicy`  
`networkservices.endpointConfigSelectors.list`  
`networkservices.endpointConfigSelectors.setIamPolicy`  
`networkservices.endpointConfigSelectors.update`  
`networkservices.endpointConfigSelectors.use`  
`networkservices.httpFilters.create`  
`networkservices.httpFilters.delete`  
`networkservices.httpFilters.get`  
`networkservices.httpFilters.getIamPolicy`  
`networkservices.httpFilters.list`  
`networkservices.httpFilters.setIamPolicy`  
`networkservices.httpFilters.update`  
`networkservices.httpFilters.use`  
`networkservices.locations.get`  
`networkservices.locations.list`  
`networkservices.operations.cancel`  
`networkservices.operations.delete`  
`networkservices.operations.get`  
`networkservices.operations.list`  
  
Network Services  |  Supported In Custom Roles  |  `networkservices.endpointConfigSelectors.create`  
`networkservices.endpointConfigSelectors.delete`  
`networkservices.endpointConfigSelectors.get`  
`networkservices.endpointConfigSelectors.getIamPolicy`  
`networkservices.endpointConfigSelectors.list`  
`networkservices.endpointConfigSelectors.setIamPolicy`  
`networkservices.endpointConfigSelectors.update`  
`networkservices.endpointConfigSelectors.use`  
`networkservices.httpFilters.create`  
`networkservices.httpFilters.delete`  
`networkservices.httpFilters.get`  
`networkservices.httpFilters.getIamPolicy`  
`networkservices.httpFilters.list`  
`networkservices.httpFilters.setIamPolicy`  
`networkservices.httpFilters.update`  
`networkservices.httpFilters.use`  
`networkservices.locations.get`  
`networkservices.locations.list`  
`networkservices.operations.cancel`  
`networkservices.operations.delete`  
`networkservices.operations.get`  
`networkservices.operations.list`  
  
Pub/Sub  |  Added  |  `pubsub.topics.detachSubscription`  
  
Pub/Sub  |  Now GA  |  `pubsub.topics.detachSubscription`  
  
Google Cloud Fraud Defense  |  Added  |  `recaptchaenterprise.metrics.get`  
  
Google Cloud Fraud Defense  |  Supported In Custom Roles  |  `recaptchaenterprise.metrics.get`  
  
Recommender  |  Added  |  `recommender.computeDiskIdleResourceInsights.get`  
`recommender.computeDiskIdleResourceInsights.list`  
`recommender.computeDiskIdleResourceInsights.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.computeDiskIdleResourceInsights.get`  
`recommender.computeDiskIdleResourceInsights.list`  
`recommender.computeDiskIdleResourceInsights.update`  
  
Recommender  |  Now GA  |  `recommender.computeDiskIdleResourceInsights.get`  
`recommender.computeDiskIdleResourceInsights.list`  
`recommender.computeDiskIdleResourceInsights.update`  
  
  
## Cloud IAM changes as of 2020-06-26

Service | Change | Description  
---|---|---  
Apigee  |  Role Updated  |  The following permissions have been added to the role `roles/apigee.analyticsViewer` (Apigee Analytics Viewer): `apigee.queries.get`  
`apigee.queries.list`  
`apigee.reports.get`  
`apigee.reports.list`  
  
Cloud Billing  |  Role Updated  |  The following permissions have been added to the role `roles/billing.admin` (Billing Account Administrator): `dataprocessing.groupcontrols.list`  
  
Cloud Billing  |  Role Updated  |  The following permissions have been added to the role `roles/billing.viewer` (Billing Account Viewer): `dataprocessing.groupcontrols.list`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.worker` (Composer Worker): `monitoring.timeSeries.list`  
  
Managed Service for Apache Spark  |  Role Updated  |  The following permissions have been added to the role `roles/dataproc.viewer` (Dataproc Viewer): `compute.zones.list`  
  
Customer Usage Data Processing  |  Role Updated  |  The following permissions have been added to the role `roles/dataprocessing.admin` (Data Processing Controls Resource Admin): `billing.accounts.get`  
`billing.accounts.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `containeranalysis.notes.getIamPolicy`  
`containeranalysis.occurrences.getIamPolicy`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `containeranalysis.notes.getIamPolicy`  
`containeranalysis.occurrences.getIamPolicy`  
  
Serverless VPC Access  |  Now GA  |  The role `roles/vpcaccess.user` (Serverless VPC Access User) is now GA.  
Serverless VPC Access  |  Now GA  |  The role `roles/vpcaccess.viewer` (Serverless VPC Access Viewer) is now GA.  
Compute Engine  |  Added  |  `compute.images.update`  
`compute.instances.getEffectiveFirewalls`  
`compute.networks.getEffectiveFirewalls`  
`compute.organizations.listAssociations`  
`compute.organizations.setSecurityPolicy`  
`compute.securityPolicies.addAssociation`  
`compute.securityPolicies.copyRules`  
`compute.securityPolicies.move`  
`compute.securityPolicies.removeAssociation`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.getEffectiveFirewalls`  
`compute.networks.getEffectiveFirewalls`  
`compute.organizations.listAssociations`  
`compute.organizations.setSecurityPolicy`  
`compute.securityPolicies.addAssociation`  
`compute.securityPolicies.copyRules`  
`compute.securityPolicies.move`  
`compute.securityPolicies.removeAssociation`  
  
Artifact Analysis  |  Added  |  `containeranalysis.notes.attachOccurrence`  
`containeranalysis.notes.create`  
`containeranalysis.notes.delete`  
`containeranalysis.notes.get`  
`containeranalysis.notes.getIamPolicy`  
`containeranalysis.notes.list`  
`containeranalysis.notes.listOccurrences`  
`containeranalysis.notes.setIamPolicy`  
`containeranalysis.notes.update`  
`containeranalysis.occurrences.create`  
`containeranalysis.occurrences.delete`  
`containeranalysis.occurrences.get`  
`containeranalysis.occurrences.getIamPolicy`  
`containeranalysis.occurrences.list`  
`containeranalysis.occurrences.setIamPolicy`  
`containeranalysis.occurrences.update`  
  
Artifact Analysis  |  Supported In Custom Roles  |  `containeranalysis.notes.attachOccurrence`  
`containeranalysis.notes.create`  
`containeranalysis.notes.delete`  
`containeranalysis.notes.get`  
`containeranalysis.notes.getIamPolicy`  
`containeranalysis.notes.list`  
`containeranalysis.notes.listOccurrences`  
`containeranalysis.notes.setIamPolicy`  
`containeranalysis.notes.update`  
`containeranalysis.occurrences.create`  
`containeranalysis.occurrences.delete`  
`containeranalysis.occurrences.get`  
`containeranalysis.occurrences.getIamPolicy`  
`containeranalysis.occurrences.list`  
`containeranalysis.occurrences.setIamPolicy`  
`containeranalysis.occurrences.update`  
  
Recommender  |  Added  |  `recommender.iamServiceAccountInsights.get`  
`recommender.iamServiceAccountInsights.list`  
`recommender.iamServiceAccountInsights.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.iamServiceAccountInsights.get`  
`recommender.iamServiceAccountInsights.list`  
`recommender.iamServiceAccountInsights.update`  
  
Recommender  |  Now GA  |  `recommender.iamServiceAccountInsights.get`  
`recommender.iamServiceAccountInsights.list`  
`recommender.iamServiceAccountInsights.update`  
  
Spanner  |  Added  |  `spanner.databases.beginPartitionedDmlTransaction`  
`spanner.databases.partitionQuery`  
`spanner.databases.partitionRead`  
  
Spanner  |  Supported In Custom Roles  |  `spanner.databases.beginPartitionedDmlTransaction`  
`spanner.databases.partitionQuery`  
`spanner.databases.partitionRead`  
  
Spanner  |  Now GA  |  `spanner.databases.beginPartitionedDmlTransaction`  
`spanner.databases.partitionQuery`  
`spanner.databases.partitionRead`  
  
  
## Cloud IAM changes as of 2020-06-19

Service | Change | Description  
---|---|---  
Actions  |  Role Updated  |  The following permissions have been added to the role `roles/actions.Admin` (Actions Admin): `serviceusage.services.use`  
  
Actions  |  Role Updated  |  The following permissions have been added to the role `roles/actions.Viewer` (Actions Viewer): `serviceusage.services.use`  
  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.admin` (Container Analysis Admin) is now GA.  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.notes.attacher` (Container Analysis Notes Attacher) is now GA.  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.notes.editor` (Container Analysis Notes Editor) is now GA.  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.notes.viewer` (Container Analysis Notes Viewer) is now GA.  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.occurrences.editor` (Container Analysis Occurrences Editor) is now GA.  
Artifact Analysis  |  Now GA  |  The role `roles/containeranalysis.occurrences.viewer` (Container Analysis Occurrences Viewer) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.assignmentAdmin` (Assignment Admin) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.assignmentEditor` (Assignment Editor) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.assignmentViewer` (Assignment Viewer) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.osConfigAdmin` (OsConfig Admin) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.osConfigEditor` (OsConfig Editor) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.osConfigViewer` (OsConfig Viewer) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.patchDeploymentAdmin` (PatchDeployment Admin) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.patchDeploymentViewer` (PatchDeployment Viewer) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.patchJobExecutor` (Patch Job Executor) is now GA.  
Cloud OS Config  |  Now GA  |  The role `roles/osconfig.patchJobViewer` (Patch Job Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been removed from the role `roles/viewer` (Viewer): `apigee.appkeys.create`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.connections.create`  
`bigquery.connections.delete`  
`bigquery.connections.get`  
`bigquery.connections.getIamPolicy`  
`bigquery.connections.list`  
`bigquery.connections.setIamPolicy`  
`bigquery.connections.update`  
`bigquery.connections.use`  
  
Compute Engine  |  Added  |  `compute.instances.update`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.update`  
  
Compute Engine  |  Now GA  |  `compute.instances.update`  
  
Filestore  |  Added  |  `file.backups.create`  
`file.backups.delete`  
`file.backups.get`  
`file.backups.list`  
`file.backups.update`  
  
GKE Hub  |  Added  |  `gkehub.features.create`  
`gkehub.features.delete`  
`gkehub.features.get`  
`gkehub.features.getIamPolicy`  
`gkehub.features.list`  
`gkehub.features.setIamPolicy`  
`gkehub.features.update`  
  
GKE Hub  |  Now GA  |  `gkehub.features.create`  
`gkehub.features.delete`  
`gkehub.features.get`  
`gkehub.features.getIamPolicy`  
`gkehub.features.list`  
`gkehub.features.setIamPolicy`  
`gkehub.features.update`  
  
Cloud OS Config  |  Now GA  |  `osconfig.patchDeployments.create`  
`osconfig.patchDeployments.delete`  
`osconfig.patchDeployments.execute`  
`osconfig.patchDeployments.get`  
`osconfig.patchDeployments.list`  
`osconfig.patchDeployments.update`  
`osconfig.patchJobs.exec`  
`osconfig.patchJobs.get`  
`osconfig.patchJobs.list`  
  
Pub/Sub Lite  |  Added  |  `pubsublite.subscriptions.create`  
`pubsublite.subscriptions.delete`  
`pubsublite.subscriptions.get`  
`pubsublite.subscriptions.getCursor`  
`pubsublite.subscriptions.list`  
`pubsublite.subscriptions.setCursor`  
`pubsublite.subscriptions.subscribe`  
`pubsublite.subscriptions.update`  
`pubsublite.topics.create`  
`pubsublite.topics.delete`  
`pubsublite.topics.get`  
`pubsublite.topics.getPartitions`  
`pubsublite.topics.list`  
`pubsublite.topics.listSubscriptions`  
`pubsublite.topics.publish`  
`pubsublite.topics.subscribe`  
`pubsublite.topics.update`  
  
Pub/Sub Lite  |  Supported In Custom Roles  |  `pubsublite.subscriptions.create`  
`pubsublite.subscriptions.delete`  
`pubsublite.subscriptions.get`  
`pubsublite.subscriptions.getCursor`  
`pubsublite.subscriptions.list`  
`pubsublite.subscriptions.setCursor`  
`pubsublite.subscriptions.subscribe`  
`pubsublite.subscriptions.update`  
`pubsublite.topics.create`  
`pubsublite.topics.delete`  
`pubsublite.topics.get`  
`pubsublite.topics.getPartitions`  
`pubsublite.topics.list`  
`pubsublite.topics.listSubscriptions`  
`pubsublite.topics.publish`  
`pubsublite.topics.subscribe`  
`pubsublite.topics.update`  
  
Google Cloud VMware Engine  |  Now GA  |  The role `roles/vmwareengine.vmwareengineAdmin` (VMWare Engine Service Admin) is now GA.  
Google Cloud VMware Engine  |  Now GA  |  The role `roles/vmwareengine.vmwareengineViewer` (VMWare Engine Service Viewer) is now GA.  
Google Cloud VMware Engine  |  Added  |  `vmwareengine.googleapis.com/services.use`  
`vmwareengine.googleapis.com/services.view`  
`vmwareengine.services.use`  
`vmwareengine.services.view`  
  
Google Cloud VMware Engine  |  Supported In Custom Roles  |  `vmwareengine.googleapis.com/services.use`  
`vmwareengine.googleapis.com/services.view`  
`vmwareengine.services.use`  
`vmwareengine.services.view`  
  
Google Cloud VMware Engine  |  Now GA  |  `vmwareengine.googleapis.com/services.use`  
`vmwareengine.googleapis.com/services.view`  
`vmwareengine.services.use`  
`vmwareengine.services.view`  
  
  
## Cloud IAM changes as of 2020-06-12

Service | Change | Description  
---|---|---  
Customer Usage Data Processing  |  Now GA  |  The role `roles/dataprocessing.admin` (Data Processing Controls Resource Admin) is now GA.  
Customer Usage Data Processing  |  Now GA  |  The role `roles/dataprocessing.iamAccessHistoryExporter` (Data Processing IAM Access History Exporter) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.inspectFindingsReader` (DLP Inspect Findings Reader) is now GA.  
GKE Hub  |  Now GA  |  The role `roles/gkehub.admin` (GKE Hub Admin) is now GA.  
GKE Hub  |  Now GA  |  The role `roles/gkehub.connect` (GKE Hub Connection Agent) is now GA.  
GKE Hub  |  Now GA  |  The role `roles/gkehub.viewer` (GKE Hub Viewer) is now GA.  
Cloud Life Sciences  |  Role Updated  |  The following permissions have been added to the role `roles/lifesciences.viewer` (Cloud Life Sciences Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Monitoring  |  Now GA  |  The role `roles/monitoring.dashboardEditor` (Monitoring Dashboard Configuration Editor) is now GA.  
Cloud Monitoring  |  Now GA  |  The role `roles/monitoring.dashboardViewer` (Monitoring Dashboard Configuration Viewer) is now GA.  
Apigee Connect  |  Added  |  `apigeeconnect.connections.list`  
`apigeeconnect.endpoints.connect`  
  
Apigee Connect  |  Supported In Custom Roles  |  `apigeeconnect.connections.list`  
`apigeeconnect.endpoints.connect`  
  
API Keys  |  Added  |  `apikeys.keys.create`  
`apikeys.keys.delete`  
`apikeys.keys.get`  
`apikeys.keys.list`  
`apikeys.keys.lookup`  
`apikeys.keys.update`  
  
Recommendations  |  Supported In Custom Roles  |  `automlrecommendations.events.create`  
  
BigQuery  |  Added  |  `bigquery.tables.getIamPolicy`  
`bigquery.tables.setIamPolicy`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.tables.getIamPolicy`  
`bigquery.tables.setIamPolicy`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.exportCloudkmsImportJobs`  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `cloudasset.assets.exportCloudkmsImportJobs`  
  
Cloud Asset Inventory  |  Now GA  |  `cloudasset.assets.searchAllIamPolicies`  
`cloudasset.assets.searchAllResources`  
  
Compute Engine  |  Added  |  `compute.globalPublicDelegatedPrefixes.create`  
`compute.globalPublicDelegatedPrefixes.delete`  
`compute.globalPublicDelegatedPrefixes.get`  
`compute.globalPublicDelegatedPrefixes.list`  
`compute.globalPublicDelegatedPrefixes.update`  
`compute.globalPublicDelegatedPrefixes.updatePolicy`  
`compute.globalPublicDelegatedPrefixes.use`  
`compute.publicAdvertisedPrefixes.create`  
`compute.publicAdvertisedPrefixes.delete`  
`compute.publicAdvertisedPrefixes.get`  
`compute.publicAdvertisedPrefixes.list`  
`compute.publicAdvertisedPrefixes.update`  
`compute.publicAdvertisedPrefixes.updatePolicy`  
`compute.publicAdvertisedPrefixes.use`  
`compute.publicDelegatedPrefixes.create`  
`compute.publicDelegatedPrefixes.delete`  
`compute.publicDelegatedPrefixes.get`  
`compute.publicDelegatedPrefixes.list`  
`compute.publicDelegatedPrefixes.update`  
`compute.publicDelegatedPrefixes.updatePolicy`  
`compute.publicDelegatedPrefixes.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.globalPublicDelegatedPrefixes.create`  
`compute.globalPublicDelegatedPrefixes.delete`  
`compute.globalPublicDelegatedPrefixes.get`  
`compute.globalPublicDelegatedPrefixes.list`  
`compute.globalPublicDelegatedPrefixes.update`  
`compute.globalPublicDelegatedPrefixes.updatePolicy`  
`compute.globalPublicDelegatedPrefixes.use`  
`compute.publicAdvertisedPrefixes.create`  
`compute.publicAdvertisedPrefixes.delete`  
`compute.publicAdvertisedPrefixes.get`  
`compute.publicAdvertisedPrefixes.list`  
`compute.publicAdvertisedPrefixes.update`  
`compute.publicAdvertisedPrefixes.updatePolicy`  
`compute.publicAdvertisedPrefixes.use`  
`compute.publicDelegatedPrefixes.create`  
`compute.publicDelegatedPrefixes.delete`  
`compute.publicDelegatedPrefixes.get`  
`compute.publicDelegatedPrefixes.list`  
`compute.publicDelegatedPrefixes.update`  
`compute.publicDelegatedPrefixes.updatePolicy`  
`compute.publicDelegatedPrefixes.use`  
  
Cloud Data Fusion  |  Added  |  `datafusion.instances.runtime`  
  
Customer Usage Data Processing  |  Now GA  |  `dataprocessing.featurecontrols.list`  
`dataprocessing.featurecontrols.update`  
`dataprocessing.groupcontrols.list`  
`dataprocessing.groupcontrols.update`  
  
Sensitive Data Protection  |  Added  |  `dlp.inspectFindings.list`  
`dlp.jobTriggers.hybridInspect`  
`dlp.jobs.hybridInspect`  
  
Sensitive Data Protection  |  Now GA  |  `dlp.inspectFindings.list`  
`dlp.jobTriggers.hybridInspect`  
`dlp.jobs.hybridInspect`  
  
GKE Hub  |  Now GA  |  `gkehub.endpoints.connect`  
`gkehub.locations.get`  
`gkehub.locations.list`  
`gkehub.memberships.create`  
`gkehub.memberships.delete`  
`gkehub.memberships.generateConnectManifest`  
`gkehub.memberships.get`  
`gkehub.memberships.getIamPolicy`  
`gkehub.memberships.list`  
`gkehub.memberships.setIamPolicy`  
`gkehub.memberships.update`  
`gkehub.operations.cancel`  
`gkehub.operations.get`  
`gkehub.operations.list`  
  
Cloud Healthcare API  |  Added  |  `healthcare.fhirResources.translateConceptMap`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.fhirResources.translateConceptMap`  
  
Cloud Healthcare API  |  Now GA  |  `healthcare.fhirResources.translateConceptMap`  
  
Recommender  |  Added  |  `recommender.computeDiskIdleResourceRecommendations.get`  
`recommender.computeDiskIdleResourceRecommendations.list`  
`recommender.computeDiskIdleResourceRecommendations.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.computeDiskIdleResourceRecommendations.get`  
`recommender.computeDiskIdleResourceRecommendations.list`  
`recommender.computeDiskIdleResourceRecommendations.update`  
  
Recommender  |  Now GA  |  `recommender.computeDiskIdleResourceRecommendations.get`  
`recommender.computeDiskIdleResourceRecommendations.list`  
`recommender.computeDiskIdleResourceRecommendations.update`  
  
  
## Cloud IAM changes as of 2020-05-22

Service | Change | Description  
---|---|---  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `apigee.appkeys.create`  
  
  
## Cloud IAM changes as of 2020-03-27

Service | Change | Description  
---|---|---  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.admin` (Notebooks Admin): `compute.acceleratorTypes.list`  
`compute.diskTypes.list`  
`compute.machineTypes.list`  
`compute.subnetworks.list`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.runner` (Notebooks Runner): `compute.acceleratorTypes.list`  
`compute.diskTypes.list`  
`compute.machineTypes.list`  
`compute.subnetworks.list`  
`notebooks.environments.get`  
`notebooks.environments.getIamPolicy`  
`notebooks.environments.list`  
`notebooks.instances.get`  
`notebooks.instances.getIamPolicy`  
`notebooks.instances.list`  
`notebooks.locations.get`  
`notebooks.locations.list`  
`notebooks.operations.get`  
`notebooks.operations.list`  
  
Notebooks  |  Role Updated  |  The following permissions have been added to the role `roles/notebooks.viewer` (Notebooks Viewer): `compute.acceleratorTypes.list`  
`compute.diskTypes.list`  
`compute.machineTypes.list`  
`compute.subnetworks.list`  
  
  
## Cloud IAM changes as of 2020-03-20

Service | Change | Description  
---|---|---  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.admin` (Data Catalog Admin) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.entryGroupCreator` (DataCatalog EntryGroup Creator) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.entryGroupOwner` (DataCatalog entryGroup Owner) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.entryOwner` (DataCatalog entry Owner) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.entryViewer` (DataCatalog Entry Viewer) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.tagEditor` (Data Catalog Tag Editor) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.tagTemplateCreator` (Data Catalog TagTemplate Creator) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.tagTemplateOwner` (Data Catalog TagTemplate Owner) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.tagTemplateUser` (Data Catalog TagTemplate User) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.tagTemplateViewer` (Data Catalog TagTemplate Viewer) is now GA.  
Data Catalog  |  Now GA  |  The role `roles/datacatalog.viewer` (Data Catalog Viewer) is now GA.  
Bigtable  |  Added  |  `bigtable.keyvisualizer.get`  
`bigtable.keyvisualizer.list`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.keyvisualizer.get`  
`bigtable.keyvisualizer.list`  
  
Bigtable  |  Now GA  |  `bigtable.keyvisualizer.get`  
`bigtable.keyvisualizer.list`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.analyzeIamPolicy`  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `cloudasset.assets.analyzeIamPolicy`  
  
Data Catalog  |  Supported In Custom Roles  |  `datacatalog.entries.list`  
`datacatalog.entries.updateTag`  
`datacatalog.entryGroups.update`  
  
Data Catalog  |  Now GA  |  `datacatalog.entries.create`  
`datacatalog.entries.delete`  
`datacatalog.entries.get`  
`datacatalog.entries.getIamPolicy`  
`datacatalog.entries.list`  
`datacatalog.entries.setIamPolicy`  
`datacatalog.entries.update`  
`datacatalog.entries.updateTag`  
`datacatalog.entryGroups.create`  
`datacatalog.entryGroups.delete`  
`datacatalog.entryGroups.get`  
`datacatalog.entryGroups.getIamPolicy`  
`datacatalog.entryGroups.list`  
`datacatalog.entryGroups.setIamPolicy`  
`datacatalog.entryGroups.update`  
`datacatalog.tagTemplates.create`  
`datacatalog.tagTemplates.delete`  
`datacatalog.tagTemplates.get`  
`datacatalog.tagTemplates.getIamPolicy`  
`datacatalog.tagTemplates.getTag`  
`datacatalog.tagTemplates.setIamPolicy`  
`datacatalog.tagTemplates.update`  
`datacatalog.tagTemplates.use`  
  
Customer Usage Data Processing  |  Added  |  `dataprocessing.groupcontrols.list`  
`dataprocessing.groupcontrols.update`  
  
Customer Usage Data Processing  |  Supported In Custom Roles  |  `dataprocessing.featurecontrols.list`  
`dataprocessing.featurecontrols.update`  
`dataprocessing.groupcontrols.list`  
`dataprocessing.groupcontrols.update`  
  
Memorystore for Memcached  |  Added  |  `memcache.instances.applyParameters`  
`memcache.instances.create`  
`memcache.instances.delete`  
`memcache.instances.get`  
`memcache.instances.list`  
`memcache.instances.update`  
`memcache.instances.updateParameters`  
`memcache.locations.get`  
`memcache.locations.list`  
`memcache.operations.cancel`  
`memcache.operations.delete`  
`memcache.operations.get`  
`memcache.operations.list`  
  
Memorystore for Memcached  |  Supported In Custom Roles  |  `memcache.instances.applyParameters`  
`memcache.instances.create`  
`memcache.instances.delete`  
`memcache.instances.get`  
`memcache.instances.list`  
`memcache.instances.update`  
`memcache.instances.updateParameters`  
`memcache.locations.get`  
`memcache.locations.list`  
`memcache.operations.cancel`  
`memcache.operations.delete`  
`memcache.operations.get`  
`memcache.operations.list`  
  
Cloud OS Config  |  Added  |  `osconfig.guestPolicies.create`  
`osconfig.guestPolicies.delete`  
`osconfig.guestPolicies.get`  
`osconfig.guestPolicies.list`  
`osconfig.guestPolicies.update`  
`osconfig.patchDeployments.create`  
`osconfig.patchDeployments.delete`  
`osconfig.patchDeployments.execute`  
`osconfig.patchDeployments.get`  
`osconfig.patchDeployments.list`  
`osconfig.patchDeployments.update`  
`osconfig.patchJobs.exec`  
`osconfig.patchJobs.get`  
`osconfig.patchJobs.list`  
  
Cloud OS Config  |  Supported In Custom Roles  |  `osconfig.guestPolicies.create`  
`osconfig.guestPolicies.delete`  
`osconfig.guestPolicies.get`  
`osconfig.guestPolicies.list`  
`osconfig.guestPolicies.update`  
`osconfig.patchDeployments.create`  
`osconfig.patchDeployments.delete`  
`osconfig.patchDeployments.execute`  
`osconfig.patchDeployments.get`  
`osconfig.patchDeployments.list`  
`osconfig.patchDeployments.update`  
`osconfig.patchJobs.exec`  
`osconfig.patchJobs.get`  
`osconfig.patchJobs.list`  
  
  
## Cloud IAM changes as of 2020-03-13

Service | Change | Description  
---|---|---  
Access Context Manager  |  Now GA  |  The role `roles/accesscontextmanager.vpcScTroubleshooterViewer` (VPC Service Controls Troubleshooter Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.annotationEditor` (Healthcare Annotation Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.annotationReader` (Healthcare Annotation Reader) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.annotationStoreAdmin` (Healthcare Annotation Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.annotationStoreViewer` (Healthcare Annotation Store Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.datasetAdmin` (Healthcare Dataset Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.datasetViewer` (Healthcare Dataset Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.dicomEditor` (Healthcare DICOM Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.dicomStoreAdmin` (Healthcare DICOM Store Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.dicomStoreViewer` (Healthcare DICOM Store Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.dicomViewer` (Healthcare DICOM Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.fhirResourceEditor` (Healthcare FHIR Resource Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.fhirResourceReader` (Healthcare FHIR Resource Reader) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.fhirStoreAdmin` (Healthcare FHIR Store Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.fhirStoreViewer` (Healthcare FHIR Store Viewer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.hl7V2Consumer` (Healthcare HL7v2 Message Consumer) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.hl7V2Editor` (Healthcare HL7v2 Message Editor) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.hl7V2Ingest` (Healthcare HL7v2 Message Ingest) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.hl7V2StoreAdmin` (Healthcare HL7v2 Store Administrator) is now GA.  
Cloud Healthcare API  |  Now GA  |  The role `roles/healthcare.hl7V2StoreViewer` (Healthcare HL7v2 Store Viewer) is now GA.  
Identity Platform  |  Role Updated  |  The following permissions have been added to the role `roles/identityplatform.admin` (Identity Platform Admin): `firebaseauth.configs.create`  
`firebaseauth.configs.get`  
`firebaseauth.configs.getHashConfig`  
`firebaseauth.configs.update`  
`firebaseauth.users.create`  
`firebaseauth.users.createSession`  
`firebaseauth.users.delete`  
`firebaseauth.users.get`  
`firebaseauth.users.sendEmail`  
`firebaseauth.users.update`  
  
Identity Platform  |  Role Updated  |  The following permissions have been added to the role `roles/identityplatform.viewer` (Identity Platform Viewer): `firebaseauth.configs.get`  
`firebaseauth.users.get`  
  
AI Platform  |  Role Updated  |  The following permissions have been added to the role `roles/ml.developer` (ML Engine Developer): `ml.studies.create`  
`ml.studies.delete`  
`ml.studies.get`  
`ml.studies.getIamPolicy`  
`ml.studies.list`  
`ml.studies.setIamPolicy`  
`ml.trials.create`  
`ml.trials.delete`  
`ml.trials.get`  
`ml.trials.list`  
`ml.trials.update`  
  
AI Platform  |  Role Updated  |  The following permissions have been added to the role `roles/ml.viewer` (ML Engine Viewer): `ml.studies.get`  
`ml.studies.getIamPolicy`  
`ml.studies.list`  
`ml.trials.get`  
`ml.trials.list`  
  
Notebooks  |  Role Added  |  The role `roles/notebooks.runner` (Notebooks Runner) has been added with the following permissions: `notebooks.instances.create`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Recommender  |  Now GA  |  The role `roles/recommender.firewallAdmin` (Firewall Recommender Admin) is now GA.  
Recommender  |  Now GA  |  The role `roles/recommender.firewallViewer` (Firewall Recommender Viewer) is now GA.  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.searchAllIamPolicies`  
`cloudasset.assets.searchAllResources`  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `cloudasset.assets.searchAllIamPolicies`  
`cloudasset.assets.searchAllResources`  
  
Compute Engine  |  Added  |  `compute.instances.getScreenshot`  
`compute.networks.access`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.getScreenshot`  
`compute.networks.access`  
  
Compute Engine  |  Now GA  |  `compute.networks.access`  
  
Dataflow  |  Added  |  `dataflow.jobs.snapshot`  
`dataflow.snapshots.delete`  
`dataflow.snapshots.get`  
`dataflow.snapshots.list`  
  
Dataflow  |  Supported In Custom Roles  |  `dataflow.jobs.snapshot`  
`dataflow.snapshots.delete`  
`dataflow.snapshots.get`  
`dataflow.snapshots.list`  
  
Cloud Healthcare API  |  Added  |  `healthcare.dicomStores.deidentify`  
`healthcare.fhirStores.deidentify`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.dicomStores.deidentify`  
`healthcare.fhirStores.deidentify`  
`healthcare.operations.cancel`  
  
Cloud Healthcare API  |  Now GA  |  `healthcare.datasets.create`  
`healthcare.datasets.deidentify`  
`healthcare.datasets.delete`  
`healthcare.datasets.get`  
`healthcare.datasets.getIamPolicy`  
`healthcare.datasets.list`  
`healthcare.datasets.setIamPolicy`  
`healthcare.datasets.update`  
`healthcare.dicomStores.create`  
`healthcare.dicomStores.deidentify`  
`healthcare.dicomStores.delete`  
`healthcare.dicomStores.dicomWebDelete`  
`healthcare.dicomStores.dicomWebRead`  
`healthcare.dicomStores.dicomWebWrite`  
`healthcare.dicomStores.export`  
`healthcare.dicomStores.get`  
`healthcare.dicomStores.getIamPolicy`  
`healthcare.dicomStores.import`  
`healthcare.dicomStores.list`  
`healthcare.dicomStores.setIamPolicy`  
`healthcare.dicomStores.update`  
`healthcare.fhirResources.create`  
`healthcare.fhirResources.delete`  
`healthcare.fhirResources.get`  
`healthcare.fhirResources.patch`  
`healthcare.fhirResources.purge`  
`healthcare.fhirResources.update`  
`healthcare.fhirStores.create`  
`healthcare.fhirStores.deidentify`  
`healthcare.fhirStores.delete`  
`healthcare.fhirStores.executeBundle`  
`healthcare.fhirStores.export`  
`healthcare.fhirStores.get`  
`healthcare.fhirStores.getIamPolicy`  
`healthcare.fhirStores.import`  
`healthcare.fhirStores.list`  
`healthcare.fhirStores.searchResources`  
`healthcare.fhirStores.setIamPolicy`  
`healthcare.fhirStores.update`  
`healthcare.hl7V2Messages.create`  
`healthcare.hl7V2Messages.delete`  
`healthcare.hl7V2Messages.get`  
`healthcare.hl7V2Messages.ingest`  
`healthcare.hl7V2Messages.list`  
`healthcare.hl7V2Messages.update`  
`healthcare.hl7V2Stores.create`  
`healthcare.hl7V2Stores.delete`  
`healthcare.hl7V2Stores.get`  
`healthcare.hl7V2Stores.getIamPolicy`  
`healthcare.hl7V2Stores.list`  
`healthcare.hl7V2Stores.setIamPolicy`  
`healthcare.hl7V2Stores.update`  
`healthcare.operations.cancel`  
`healthcare.operations.get`  
`healthcare.operations.list`  
  
AI Platform  |  Added  |  `ml.studies.create`  
`ml.studies.delete`  
`ml.studies.get`  
`ml.studies.getIamPolicy`  
`ml.studies.list`  
`ml.studies.setIamPolicy`  
`ml.trials.create`  
`ml.trials.delete`  
`ml.trials.get`  
`ml.trials.list`  
`ml.trials.update`  
  
AI Platform  |  Now GA  |  `ml.studies.create`  
`ml.studies.delete`  
`ml.studies.get`  
`ml.studies.getIamPolicy`  
`ml.studies.list`  
`ml.studies.setIamPolicy`  
`ml.trials.create`  
`ml.trials.delete`  
`ml.trials.get`  
`ml.trials.list`  
`ml.trials.update`  
  
Recommender  |  Added  |  `recommender.computeFirewallInsights.get`  
`recommender.computeFirewallInsights.list`  
`recommender.computeFirewallInsights.update`  
`recommender.computeInstanceIdleResourceRecommendations.get`  
`recommender.computeInstanceIdleResourceRecommendations.list`  
`recommender.computeInstanceIdleResourceRecommendations.update`  
`recommender.iamPolicyInsights.get`  
`recommender.iamPolicyInsights.list`  
`recommender.iamPolicyInsights.update`  
  
Recommender  |  Supported In Custom Roles  |  `recommender.computeFirewallInsights.get`  
`recommender.computeFirewallInsights.list`  
`recommender.computeFirewallInsights.update`  
`recommender.computeInstanceIdleResourceRecommendations.get`  
`recommender.computeInstanceIdleResourceRecommendations.list`  
`recommender.computeInstanceIdleResourceRecommendations.update`  
`recommender.iamPolicyInsights.get`  
`recommender.iamPolicyInsights.list`  
`recommender.iamPolicyInsights.update`  
  
Recommender  |  Now GA  |  `recommender.computeFirewallInsights.get`  
`recommender.computeFirewallInsights.list`  
`recommender.computeFirewallInsights.update`  
`recommender.computeInstanceIdleResourceRecommendations.get`  
`recommender.computeInstanceIdleResourceRecommendations.list`  
`recommender.computeInstanceIdleResourceRecommendations.update`  
`recommender.iamPolicyInsights.get`  
`recommender.iamPolicyInsights.list`  
`recommender.iamPolicyInsights.update`  
  
  
## Cloud IAM changes as of 2020-03-06

Service | Change | Description  
---|---|---  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `compute.acceleratorTypes.get`  
`compute.acceleratorTypes.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkViewer` (Compute Network Viewer): `compute.acceleratorTypes.get`  
`compute.acceleratorTypes.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `bigquery.bireservations.update`  
`bigquery.reservationAssignments.create`  
`bigquery.reservationAssignments.delete`  
`bigquery.reservations.create`  
`bigquery.reservations.delete`  
`bigquery.reservations.update`  
`identityplatform.workloadPoolProviders.create`  
`identityplatform.workloadPoolProviders.delete`  
`identityplatform.workloadPoolProviders.get`  
`identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPoolProviders.undelete`  
`identityplatform.workloadPoolProviders.update`  
`identityplatform.workloadPools.create`  
`identityplatform.workloadPools.delete`  
`identityplatform.workloadPools.get`  
`identityplatform.workloadPools.list`  
`identityplatform.workloadPools.undelete`  
`identityplatform.workloadPools.update`  
`servicedirectory.locations.get`  
`servicedirectory.locations.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityAdmin` (Security Admin): `identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPools.list`  
`servicedirectory.locations.list`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityReviewer` (Security Reviewer): `identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPools.list`  
`servicedirectory.locations.list`  
  
Identity Platform  |  Role Added  |  The role `roles/identityplatform.admin` (Identity Platform Admin) has been added with the following permissions: `identityplatform.workloadPoolProviders.create`  
`identityplatform.workloadPoolProviders.delete`  
`identityplatform.workloadPoolProviders.get`  
`identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPoolProviders.undelete`  
`identityplatform.workloadPoolProviders.update`  
`identityplatform.workloadPools.create`  
`identityplatform.workloadPools.delete`  
`identityplatform.workloadPools.get`  
`identityplatform.workloadPools.list`  
`identityplatform.workloadPools.undelete`  
`identityplatform.workloadPools.update`  
  
Identity Platform  |  Role Added  |  The role `roles/identityplatform.viewer` (Identity Platform Viewer) has been added with the following permissions: `identityplatform.workloadPoolProviders.get`  
`identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPools.get`  
`identityplatform.workloadPools.list`  
  
Network Management API  |  Now GA  |  The role `roles/networkmanagement.admin` (Network Management Admin) is now GA.  
Network Management API  |  Now GA  |  The role `roles/networkmanagement.viewer` (Network Management Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `identityplatform.workloadPoolProviders.create`  
`identityplatform.workloadPoolProviders.delete`  
`identityplatform.workloadPoolProviders.get`  
`identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPoolProviders.undelete`  
`identityplatform.workloadPoolProviders.update`  
`identityplatform.workloadPools.create`  
`identityplatform.workloadPools.delete`  
`identityplatform.workloadPools.get`  
`identityplatform.workloadPools.list`  
`identityplatform.workloadPools.undelete`  
`identityplatform.workloadPools.update`  
`servicedirectory.locations.get`  
`servicedirectory.locations.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `identityplatform.workloadPoolProviders.get`  
`identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPools.get`  
`identityplatform.workloadPools.list`  
`servicedirectory.locations.get`  
`servicedirectory.locations.list`  
  
BigQuery  |  Added  |  `bigquery.bireservations.get`  
`bigquery.bireservations.update`  
`bigquery.capacityCommitments.create`  
`bigquery.capacityCommitments.delete`  
`bigquery.capacityCommitments.get`  
`bigquery.capacityCommitments.list`  
`bigquery.reservationAssignments.create`  
`bigquery.reservationAssignments.delete`  
`bigquery.reservationAssignments.list`  
`bigquery.reservationAssignments.search`  
`bigquery.reservations.create`  
`bigquery.reservations.delete`  
`bigquery.reservations.get`  
`bigquery.reservations.list`  
`bigquery.reservations.update`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.bireservations.get`  
`bigquery.bireservations.update`  
`bigquery.capacityCommitments.create`  
`bigquery.capacityCommitments.delete`  
`bigquery.capacityCommitments.get`  
`bigquery.capacityCommitments.list`  
`bigquery.reservationAssignments.create`  
`bigquery.reservationAssignments.delete`  
`bigquery.reservationAssignments.list`  
`bigquery.reservationAssignments.search`  
`bigquery.reservations.create`  
`bigquery.reservations.delete`  
`bigquery.reservations.get`  
`bigquery.reservations.list`  
`bigquery.reservations.update`  
  
Identity Platform  |  Added  |  `identityplatform.workloadPoolProviders.create`  
`identityplatform.workloadPoolProviders.delete`  
`identityplatform.workloadPoolProviders.get`  
`identityplatform.workloadPoolProviders.list`  
`identityplatform.workloadPoolProviders.undelete`  
`identityplatform.workloadPoolProviders.update`  
`identityplatform.workloadPools.create`  
`identityplatform.workloadPools.delete`  
`identityplatform.workloadPools.get`  
`identityplatform.workloadPools.list`  
`identityplatform.workloadPools.undelete`  
`identityplatform.workloadPools.update`  
  
Network Management API  |  Now GA  |  `networkmanagement.connectivitytests.create`  
`networkmanagement.connectivitytests.delete`  
`networkmanagement.connectivitytests.get`  
`networkmanagement.connectivitytests.getIamPolicy`  
`networkmanagement.connectivitytests.list`  
`networkmanagement.connectivitytests.rerun`  
`networkmanagement.connectivitytests.setIamPolicy`  
`networkmanagement.connectivitytests.update`  
`networkmanagement.locations.get`  
`networkmanagement.locations.list`  
`networkmanagement.operations.get`  
`networkmanagement.operations.list`  
  
Memorystore for Redis  |  Added  |  `redis.instances.failover`  
`redis.instances.upgrade`  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `redis.instances.failover`  
`redis.instances.upgrade`  
  
Service Directory  |  Added  |  `servicedirectory.endpoints.create`  
`servicedirectory.endpoints.delete`  
`servicedirectory.endpoints.get`  
`servicedirectory.endpoints.getIamPolicy`  
`servicedirectory.endpoints.list`  
`servicedirectory.endpoints.setIamPolicy`  
`servicedirectory.endpoints.update`  
`servicedirectory.locations.get`  
`servicedirectory.locations.list`  
`servicedirectory.namespaces.associatePrivateZone`  
`servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.namespaces.get`  
`servicedirectory.namespaces.getIamPolicy`  
`servicedirectory.namespaces.list`  
`servicedirectory.namespaces.setIamPolicy`  
`servicedirectory.namespaces.update`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
`servicedirectory.services.get`  
`servicedirectory.services.getIamPolicy`  
`servicedirectory.services.list`  
`servicedirectory.services.resolve`  
`servicedirectory.services.setIamPolicy`  
`servicedirectory.services.update`  
  
Service Directory  |  Supported In Custom Roles  |  `servicedirectory.endpoints.create`  
`servicedirectory.endpoints.delete`  
`servicedirectory.endpoints.get`  
`servicedirectory.endpoints.getIamPolicy`  
`servicedirectory.endpoints.list`  
`servicedirectory.endpoints.setIamPolicy`  
`servicedirectory.endpoints.update`  
`servicedirectory.namespaces.associatePrivateZone`  
`servicedirectory.namespaces.create`  
`servicedirectory.namespaces.delete`  
`servicedirectory.namespaces.get`  
`servicedirectory.namespaces.getIamPolicy`  
`servicedirectory.namespaces.list`  
`servicedirectory.namespaces.setIamPolicy`  
`servicedirectory.namespaces.update`  
`servicedirectory.services.create`  
`servicedirectory.services.delete`  
`servicedirectory.services.get`  
`servicedirectory.services.getIamPolicy`  
`servicedirectory.services.list`  
`servicedirectory.services.resolve`  
`servicedirectory.services.setIamPolicy`  
`servicedirectory.services.update`  
  
  
## Cloud IAM changes as of 2020-02-27

Service | Change | Description  
---|---|---  
BigQuery  |  Now GA  |  The role `roles/bigquery.readSessionUser` (BigQuery Read Session User) is now GA.  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.entryGroupCreator` (DataCatalog EntryGroup Creator): `datacatalog.entryGroups.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `dlp.jobs.create`  
`dlp.jobs.get`  
`dlp.jobs.list`  
  
Secret Manager  |  Role Updated  |  The following permissions have been added to the role `roles/secretmanager.secretAccessor` (Secret Manager Secret Accessor): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminEditor` (Security Center Admin Editor): `securitycenter.organizationsettings.get`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminViewer` (Security Center Admin Viewer): `securitycenter.organizationsettings.get`  
  
Spanner  |  Now GA  |  The role `roles/spanner.backupAdmin` (Cloud Spanner Backup Admin) is now GA.  
Spanner  |  Now GA  |  The role `roles/spanner.backupWriter` (Cloud Spanner Backup Writer) is now GA.  
Spanner  |  Now GA  |  The role `roles/spanner.restoreAdmin` (Cloud Spanner Restore Admin) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `dlp.jobs.get`  
`dlp.jobs.list`  
  
BigQuery  |  Added  |  `bigquery.readsessions.getData`  
`bigquery.readsessions.update`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.readsessions.getData`  
`bigquery.readsessions.update`  
  
BigQuery  |  Now GA  |  `bigquery.readsessions.create`  
`bigquery.readsessions.getData`  
`bigquery.readsessions.update`  
  
Data Catalog  |  Added  |  `datacatalog.entryGroups.list`  
  
Data Catalog  |  Supported In Custom Roles  |  `datacatalog.entryGroups.list`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.fhirStores.executeBundle`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `iam.serviceAccounts.getOpenIdToken`  
  
Spanner  |  Added  |  `spanner.backupOperations.cancel`  
`spanner.backupOperations.get`  
`spanner.backupOperations.list`  
`spanner.backups.create`  
`spanner.backups.delete`  
`spanner.backups.get`  
`spanner.backups.getIamPolicy`  
`spanner.backups.list`  
`spanner.backups.restoreDatabase`  
`spanner.backups.setIamPolicy`  
`spanner.backups.update`  
`spanner.databases.createBackup`  
  
Spanner  |  Supported In Custom Roles  |  `spanner.backupOperations.cancel`  
`spanner.backupOperations.get`  
`spanner.backupOperations.list`  
`spanner.backups.create`  
`spanner.backups.delete`  
`spanner.backups.get`  
`spanner.backups.getIamPolicy`  
`spanner.backups.list`  
`spanner.backups.restoreDatabase`  
`spanner.backups.setIamPolicy`  
`spanner.backups.update`  
`spanner.databases.createBackup`  
  
Spanner  |  Now GA  |  `spanner.backupOperations.cancel`  
`spanner.backupOperations.get`  
`spanner.backupOperations.list`  
`spanner.backups.create`  
`spanner.backups.delete`  
`spanner.backups.get`  
`spanner.backups.getIamPolicy`  
`spanner.backups.list`  
`spanner.backups.restoreDatabase`  
`spanner.backups.setIamPolicy`  
`spanner.backups.update`  
`spanner.databases.createBackup`  
  
  
## Cloud IAM changes as of 2020-02-21

Service | Change | Description  
---|---|---  
Access Context Manager  |  Added  |  `accesscontextmanager.accessLevels.replaceAll`  
`accesscontextmanager.servicePerimeters.commit`  
`accesscontextmanager.servicePerimeters.replaceAll`  
  
Access Context Manager  |  Now GA  |  `accesscontextmanager.accessLevels.replaceAll`  
`accesscontextmanager.servicePerimeters.commit`  
`accesscontextmanager.servicePerimeters.replaceAll`  
  
Compute Engine  |  Added  |  `compute.regionHealthCheckServices.create`  
`compute.regionHealthCheckServices.delete`  
`compute.regionHealthCheckServices.get`  
`compute.regionHealthCheckServices.list`  
`compute.regionHealthCheckServices.update`  
`compute.regionHealthCheckServices.use`  
`compute.regionNotificationEndpoints.create`  
`compute.regionNotificationEndpoints.delete`  
`compute.regionNotificationEndpoints.get`  
`compute.regionNotificationEndpoints.list`  
`compute.regionNotificationEndpoints.update`  
`compute.regionNotificationEndpoints.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.regionHealthCheckServices.create`  
`compute.regionHealthCheckServices.delete`  
`compute.regionHealthCheckServices.get`  
`compute.regionHealthCheckServices.list`  
`compute.regionHealthCheckServices.update`  
`compute.regionHealthCheckServices.use`  
`compute.regionNotificationEndpoints.create`  
`compute.regionNotificationEndpoints.delete`  
`compute.regionNotificationEndpoints.get`  
`compute.regionNotificationEndpoints.list`  
`compute.regionNotificationEndpoints.update`  
`compute.regionNotificationEndpoints.use`  
  
  
## Cloud IAM changes as of 2020-02-14

Service | Change | Description  
---|---|---  
Google Cloud Support  |  Now GA  |  The role `roles/cloudsupport.techSupportEditor` (Tech Support Editor) is now GA.  
Google Cloud Support  |  Now GA  |  The role `roles/cloudsupport.techSupportViewer` (Tech Support Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `healthcare.fhirStores.executeBundle`  
  
Cloud Healthcare API  |  Role Updated  |  The following permissions have been added to the role `roles/healthcare.fhirResourceEditor` (Healthcare FHIR Resource Editor): `healthcare.fhirStores.executeBundle`  
  
Cloud Healthcare API  |  Role Updated  |  The following permissions have been added to the role `roles/healthcare.fhirResourceReader` (Healthcare FHIR Resource Reader): `healthcare.fhirStores.executeBundle`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.privateLogViewer` (Private Logs Viewer): `logging.buckets.get`  
`logging.buckets.list`  
  
Cloud Logging  |  Role Updated  |  The following permissions have been added to the role `roles/logging.viewer` (Logs Viewer): `logging.buckets.get`  
`logging.buckets.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `healthcare.fhirStores.executeBundle`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.admin` (Security Center Admin): `appengine.applications.get`  
`cloudsecurityscanner.crawledurls.list`  
`cloudsecurityscanner.results.get`  
`cloudsecurityscanner.results.list`  
`cloudsecurityscanner.scanruns.get`  
`cloudsecurityscanner.scanruns.getSummary`  
`cloudsecurityscanner.scanruns.list`  
`cloudsecurityscanner.scanruns.stop`  
`cloudsecurityscanner.scans.create`  
`cloudsecurityscanner.scans.delete`  
`cloudsecurityscanner.scans.get`  
`cloudsecurityscanner.scans.list`  
`cloudsecurityscanner.scans.run`  
`cloudsecurityscanner.scans.update`  
`compute.addresses.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminEditor` (Security Center Admin Editor): `appengine.applications.get`  
`cloudsecurityscanner.crawledurls.list`  
`cloudsecurityscanner.results.get`  
`cloudsecurityscanner.results.list`  
`cloudsecurityscanner.scanruns.get`  
`cloudsecurityscanner.scanruns.getSummary`  
`cloudsecurityscanner.scanruns.list`  
`cloudsecurityscanner.scanruns.stop`  
`cloudsecurityscanner.scans.create`  
`cloudsecurityscanner.scans.delete`  
`cloudsecurityscanner.scans.get`  
`cloudsecurityscanner.scans.list`  
`cloudsecurityscanner.scans.run`  
`cloudsecurityscanner.scans.update`  
`compute.addresses.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminViewer` (Security Center Admin Viewer): `cloudsecurityscanner.crawledurls.list`  
`cloudsecurityscanner.results.get`  
`cloudsecurityscanner.results.list`  
`cloudsecurityscanner.scanruns.get`  
`cloudsecurityscanner.scanruns.getSummary`  
`cloudsecurityscanner.scanruns.list`  
`cloudsecurityscanner.scans.get`  
`cloudsecurityscanner.scans.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `healthcare.fhirStores.executeBundle`  
  
Google Cloud Support  |  Added  |  `cloudsupport.properties.get`  
`cloudsupport.techCases.create`  
`cloudsupport.techCases.escalate`  
`cloudsupport.techCases.get`  
`cloudsupport.techCases.list`  
`cloudsupport.techCases.update`  
  
Google Cloud Support  |  Supported In Custom Roles  |  `cloudsupport.properties.get`  
`cloudsupport.techCases.create`  
`cloudsupport.techCases.escalate`  
`cloudsupport.techCases.get`  
`cloudsupport.techCases.list`  
`cloudsupport.techCases.update`  
  
Google Cloud Support  |  Now GA  |  `cloudsupport.techCases.create`  
`cloudsupport.techCases.escalate`  
`cloudsupport.techCases.get`  
`cloudsupport.techCases.list`  
`cloudsupport.techCases.update`  
  
Cloud Healthcare API  |  Added  |  `healthcare.fhirStores.executeBundle`  
  
Cloud Logging  |  Added  |  `logging.buckets.get`  
`logging.buckets.list`  
`logging.buckets.update`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.buckets.get`  
`logging.buckets.list`  
`logging.buckets.update`  
  
Cloud Logging  |  Now GA  |  `logging.buckets.get`  
`logging.buckets.list`  
`logging.buckets.update`  
  
  
## Cloud IAM changes as of 2020-02-07

Service | Change | Description  
---|---|---  
Secret Manager  |  Now GA  |  The role `roles/secretmanager.admin` (Secret Manager Admin) is now GA.  
Secret Manager  |  Now GA  |  The role `roles/secretmanager.secretAccessor` (Secret Manager Secret Accessor) is now GA.  
Secret Manager  |  Now GA  |  The role `roles/secretmanager.viewer` (Secret Manager Viewer) is now GA.  
Cloud Healthcare API  |  Supported In Custom Roles  |  `healthcare.datasets.create`  
`healthcare.datasets.deidentify`  
`healthcare.datasets.delete`  
`healthcare.datasets.get`  
`healthcare.datasets.getIamPolicy`  
`healthcare.datasets.list`  
`healthcare.datasets.setIamPolicy`  
`healthcare.datasets.update`  
`healthcare.dicomStores.create`  
`healthcare.dicomStores.delete`  
`healthcare.dicomStores.dicomWebDelete`  
`healthcare.dicomStores.dicomWebRead`  
`healthcare.dicomStores.dicomWebWrite`  
`healthcare.dicomStores.export`  
`healthcare.dicomStores.get`  
`healthcare.dicomStores.getIamPolicy`  
`healthcare.dicomStores.import`  
`healthcare.dicomStores.list`  
`healthcare.dicomStores.setIamPolicy`  
`healthcare.dicomStores.update`  
`healthcare.fhirResources.create`  
`healthcare.fhirResources.delete`  
`healthcare.fhirResources.get`  
`healthcare.fhirResources.patch`  
`healthcare.fhirResources.purge`  
`healthcare.fhirResources.update`  
`healthcare.fhirStores.create`  
`healthcare.fhirStores.delete`  
`healthcare.fhirStores.export`  
`healthcare.fhirStores.get`  
`healthcare.fhirStores.getIamPolicy`  
`healthcare.fhirStores.import`  
`healthcare.fhirStores.list`  
`healthcare.fhirStores.searchResources`  
`healthcare.fhirStores.setIamPolicy`  
`healthcare.fhirStores.update`  
`healthcare.hl7V2Messages.create`  
`healthcare.hl7V2Messages.delete`  
`healthcare.hl7V2Messages.get`  
`healthcare.hl7V2Messages.ingest`  
`healthcare.hl7V2Messages.list`  
`healthcare.hl7V2Messages.update`  
`healthcare.hl7V2Stores.create`  
`healthcare.hl7V2Stores.delete`  
`healthcare.hl7V2Stores.get`  
`healthcare.hl7V2Stores.getIamPolicy`  
`healthcare.hl7V2Stores.list`  
`healthcare.hl7V2Stores.setIamPolicy`  
`healthcare.hl7V2Stores.update`  
`healthcare.operations.get`  
`healthcare.operations.list`  
  
Google Cloud Fraud Defense  |  Added  |  `recaptchaenterprise.assessments.annotate`  
`recaptchaenterprise.assessments.create`  
`recaptchaenterprise.keys.create`  
`recaptchaenterprise.keys.delete`  
`recaptchaenterprise.keys.get`  
`recaptchaenterprise.keys.list`  
`recaptchaenterprise.keys.update`  
  
Google Cloud Fraud Defense  |  Supported In Custom Roles  |  `recaptchaenterprise.assessments.annotate`  
`recaptchaenterprise.assessments.create`  
`recaptchaenterprise.keys.create`  
`recaptchaenterprise.keys.delete`  
`recaptchaenterprise.keys.get`  
`recaptchaenterprise.keys.list`  
`recaptchaenterprise.keys.update`  
  
Secret Manager  |  Supported In Custom Roles  |  `secretmanager.locations.get`  
`secretmanager.locations.list`  
`secretmanager.secrets.create`  
`secretmanager.secrets.delete`  
`secretmanager.secrets.get`  
`secretmanager.secrets.getIamPolicy`  
`secretmanager.secrets.list`  
`secretmanager.secrets.setIamPolicy`  
`secretmanager.secrets.update`  
`secretmanager.versions.access`  
`secretmanager.versions.add`  
`secretmanager.versions.destroy`  
`secretmanager.versions.disable`  
`secretmanager.versions.enable`  
`secretmanager.versions.get`  
`secretmanager.versions.list`  
  
Secret Manager  |  Now GA  |  `secretmanager.locations.get`  
`secretmanager.locations.list`  
`secretmanager.secrets.create`  
`secretmanager.secrets.delete`  
`secretmanager.secrets.get`  
`secretmanager.secrets.getIamPolicy`  
`secretmanager.secrets.list`  
`secretmanager.secrets.setIamPolicy`  
`secretmanager.secrets.update`  
`secretmanager.versions.access`  
`secretmanager.versions.add`  
`secretmanager.versions.destroy`  
`secretmanager.versions.disable`  
`secretmanager.versions.enable`  
`secretmanager.versions.get`  
`secretmanager.versions.list`  
  
  
## Cloud IAM changes as of 2020-01-31

Service | Change | Description  
---|---|---  
Cloud Build  |  Role Updated  |  The following permissions have been added to the role `roles/cloudbuild.builds.builder` (Cloud Build Service Account): `artifactregistry.files.get`  
`artifactregistry.files.list`  
`artifactregistry.packages.get`  
`artifactregistry.packages.list`  
`artifactregistry.repositories.downloadArtifacts`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.uploadArtifacts`  
`artifactregistry.tags.create`  
`artifactregistry.tags.get`  
`artifactregistry.tags.list`  
`artifactregistry.tags.update`  
`artifactregistry.versions.get`  
`artifactregistry.versions.list`  
  
Managed Service for Apache Airflow  |  Role Updated  |  The following permissions have been added to the role `roles/composer.worker` (Composer Worker): `artifactregistry.files.get`  
`artifactregistry.files.list`  
`artifactregistry.packages.get`  
`artifactregistry.packages.list`  
`artifactregistry.repositories.downloadArtifacts`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.uploadArtifacts`  
`artifactregistry.tags.create`  
`artifactregistry.tags.get`  
`artifactregistry.tags.list`  
`artifactregistry.tags.update`  
`artifactregistry.versions.get`  
`artifactregistry.versions.list`  
  
Game Servers  |  Added  |  `gameservices.gameServerClusters.create`  
`gameservices.gameServerClusters.delete`  
`gameservices.gameServerClusters.get`  
`gameservices.gameServerClusters.list`  
`gameservices.gameServerClusters.update`  
`gameservices.gameServerConfigs.create`  
`gameservices.gameServerConfigs.delete`  
`gameservices.gameServerConfigs.get`  
`gameservices.gameServerConfigs.list`  
`gameservices.gameServerDeployments.create`  
`gameservices.gameServerDeployments.delete`  
`gameservices.gameServerDeployments.get`  
`gameservices.gameServerDeployments.list`  
`gameservices.gameServerDeployments.rollout`  
`gameservices.gameServerDeployments.update`  
`gameservices.locations.get`  
`gameservices.locations.list`  
`gameservices.operations.cancel`  
`gameservices.operations.delete`  
`gameservices.operations.get`  
`gameservices.operations.list`  
`gameservices.realms.create`  
`gameservices.realms.delete`  
`gameservices.realms.get`  
`gameservices.realms.list`  
`gameservices.realms.update`  
  
Game Servers  |  Supported In Custom Roles  |  `gameservices.gameServerClusters.create`  
`gameservices.gameServerClusters.delete`  
`gameservices.gameServerClusters.get`  
`gameservices.gameServerClusters.list`  
`gameservices.gameServerClusters.update`  
`gameservices.gameServerConfigs.create`  
`gameservices.gameServerConfigs.delete`  
`gameservices.gameServerConfigs.get`  
`gameservices.gameServerConfigs.list`  
`gameservices.gameServerDeployments.create`  
`gameservices.gameServerDeployments.delete`  
`gameservices.gameServerDeployments.get`  
`gameservices.gameServerDeployments.list`  
`gameservices.gameServerDeployments.rollout`  
`gameservices.gameServerDeployments.update`  
`gameservices.locations.get`  
`gameservices.locations.list`  
`gameservices.operations.cancel`  
`gameservices.operations.delete`  
`gameservices.operations.get`  
`gameservices.operations.list`  
`gameservices.realms.create`  
`gameservices.realms.delete`  
`gameservices.realms.get`  
`gameservices.realms.list`  
`gameservices.realms.update`  
  
Cloud Monitoring  |  Added  |  `opsconfigmonitoring.resourceMetadata.write`  
  
  
## Cloud IAM changes as of 2020-01-24

Service | Change | Description  
---|---|---  
Cloud Scheduler  |  Role Updated  |  The following permissions have been added to the role `roles/cloudscheduler.admin` (Cloud Scheduler Admin): `serviceusage.services.list`  
  
Cloud Scheduler  |  Role Updated  |  The following permissions have been added to the role `roles/cloudscheduler.jobRunner` (Cloud Scheduler Job Runner): `serviceusage.services.list`  
  
Cloud Scheduler  |  Role Updated  |  The following permissions have been added to the role `roles/cloudscheduler.viewer` (Cloud Scheduler Viewer): `serviceusage.services.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkAdmin` (Compute Network Admin): `compute.machineTypes.get`  
`compute.machineTypes.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkViewer` (Compute Network Viewer): `compute.machineTypes.get`  
`compute.machineTypes.list`  
  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.notificationConfigEditor` (Security Center Notification Configurations Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.notificationConfigViewer` (Security Center Notification Configurations Viewer) is now GA.  
Artifact Registry  |  Added  |  `artifactregistry.files.get`  
`artifactregistry.files.list`  
`artifactregistry.packages.delete`  
`artifactregistry.packages.get`  
`artifactregistry.packages.list`  
`artifactregistry.repositories.create`  
`artifactregistry.repositories.delete`  
`artifactregistry.repositories.deleteArtifacts`  
`artifactregistry.repositories.downloadArtifacts`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.getIamPolicy`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.setIamPolicy`  
`artifactregistry.repositories.update`  
`artifactregistry.repositories.uploadArtifacts`  
`artifactregistry.tags.create`  
`artifactregistry.tags.delete`  
`artifactregistry.tags.get`  
`artifactregistry.tags.list`  
`artifactregistry.tags.update`  
`artifactregistry.versions.delete`  
`artifactregistry.versions.get`  
`artifactregistry.versions.list`  
  
Artifact Registry  |  Supported In Custom Roles  |  `artifactregistry.files.get`  
`artifactregistry.files.list`  
`artifactregistry.packages.delete`  
`artifactregistry.packages.get`  
`artifactregistry.packages.list`  
`artifactregistry.repositories.create`  
`artifactregistry.repositories.delete`  
`artifactregistry.repositories.deleteArtifacts`  
`artifactregistry.repositories.downloadArtifacts`  
`artifactregistry.repositories.get`  
`artifactregistry.repositories.getIamPolicy`  
`artifactregistry.repositories.list`  
`artifactregistry.repositories.setIamPolicy`  
`artifactregistry.repositories.update`  
`artifactregistry.repositories.uploadArtifacts`  
`artifactregistry.tags.create`  
`artifactregistry.tags.delete`  
`artifactregistry.tags.get`  
`artifactregistry.tags.list`  
`artifactregistry.tags.update`  
`artifactregistry.versions.delete`  
`artifactregistry.versions.get`  
`artifactregistry.versions.list`  
  
Identity and Access Management  |  Added  |  `iam.serviceAccounts.getOpenIdToken`  
  
Security Command Center  |  Added  |  `securitycenter.notificationconfig.create`  
`securitycenter.notificationconfig.delete`  
`securitycenter.notificationconfig.get`  
`securitycenter.notificationconfig.list`  
`securitycenter.notificationconfig.update`  
  
Security Command Center  |  Supported In Custom Roles  |  `securitycenter.notificationconfig.create`  
`securitycenter.notificationconfig.delete`  
`securitycenter.notificationconfig.get`  
`securitycenter.notificationconfig.list`  
`securitycenter.notificationconfig.update`  
  
Security Command Center  |  Now GA  |  `securitycenter.notificationconfig.create`  
`securitycenter.notificationconfig.delete`  
`securitycenter.notificationconfig.get`  
`securitycenter.notificationconfig.list`  
`securitycenter.notificationconfig.update`  
  
  
## Cloud IAM changes as of 2020-01-10

Service | Change | Description  
---|---|---  
Cloud Asset Inventory  |  Now GA  |  The role `roles/cloudasset.owner` (Cloud Asset Owner) is now GA.  
Migrate to Virtual Machines  |  Role Updated  |  The following permissions have been added to the role `roles/cloudmigration.inframanager` (Velostrata Manager): `compute.globalOperations.get`  
  
Spanner  |  Role Updated  |  The following permissions have been added to the role `roles/spanner.databaseReader` (Cloud Spanner Database Reader): `spanner.instances.get`  
  
Spanner  |  Role Updated  |  The following permissions have been added to the role `roles/spanner.databaseUser` (Cloud Spanner Database User): `spanner.instances.get`  
  
Cloud Asset Inventory  |  Now GA  |  `cloudasset.feeds.create`  
`cloudasset.feeds.delete`  
`cloudasset.feeds.get`  
`cloudasset.feeds.list`  
`cloudasset.feeds.update`  
  
Compute Engine  |  Added  |  `compute.networks.listPeeringRoutes`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.networks.listPeeringRoutes`  
  
Compute Engine  |  Now GA  |  `compute.networks.listPeeringRoutes`  
  
Network Management API  |  Added  |  `networkmanagement.connectivitytests.create`  
`networkmanagement.connectivitytests.delete`  
`networkmanagement.connectivitytests.get`  
`networkmanagement.connectivitytests.getIamPolicy`  
`networkmanagement.connectivitytests.list`  
`networkmanagement.connectivitytests.rerun`  
`networkmanagement.connectivitytests.setIamPolicy`  
`networkmanagement.connectivitytests.update`  
`networkmanagement.locations.get`  
`networkmanagement.locations.list`  
`networkmanagement.operations.get`  
`networkmanagement.operations.list`  
  
Network Management API  |  Supported In Custom Roles  |  `networkmanagement.connectivitytests.create`  
`networkmanagement.connectivitytests.delete`  
`networkmanagement.connectivitytests.get`  
`networkmanagement.connectivitytests.getIamPolicy`  
`networkmanagement.connectivitytests.list`  
`networkmanagement.connectivitytests.rerun`  
`networkmanagement.connectivitytests.setIamPolicy`  
`networkmanagement.connectivitytests.update`  
`networkmanagement.locations.get`  
`networkmanagement.locations.list`  
`networkmanagement.operations.get`  
`networkmanagement.operations.list`  
  
  
## Cloud IAM change as of 2019-12-20

Service | Change | Description  
---|---|---  
Migrate to Virtual Machines  |  Role Updated  |  The following permissions have been added to the role `roles/cloudmigration.inframanager` (Velostrata Manager): `compute.disks.createSnapshot`  
`compute.snapshots.create`  
`compute.snapshots.delete`  
`compute.snapshots.get`  
`compute.snapshots.setLabels`  
`compute.snapshots.useReadOnly`  
  
Cloud Scheduler  |  Role Updated  |  The following permissions have been added to the role `roles/cloudscheduler.admin` (Cloud Scheduler Admin): `appengine.applications.get`  
`serviceusage.services.get`  
  
Cloud Scheduler  |  Role Updated  |  The following permissions have been added to the role `roles/cloudscheduler.jobRunner` (Cloud Scheduler Job Runner): `appengine.applications.get`  
`serviceusage.services.get`  
  
Cloud Scheduler  |  Role Updated  |  The following permissions have been added to the role `roles/cloudscheduler.viewer` (Cloud Scheduler Viewer): `appengine.applications.get`  
`serviceusage.services.get`  
  
Compute Engine  |  Now GA  |  The role `roles/compute.packetMirroringAdmin` (Compute packet mirroring admin) is now GA.  
Compute Engine  |  Now GA  |  The role `roles/compute.packetMirroringUser` (Compute packet mirroring user) is now GA.  
Cloud DNS  |  Now GA  |  The role `roles/dns.peer` (DNS Peer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been removed from the role `roles/editor` (Editor): `datacatalog.taxonomies.create`  
  
Recommender  |  Now GA  |  The role `roles/recommender.computeAdmin` (Compute Recommender Admin) is now GA.  
Recommender  |  Now GA  |  The role `roles/recommender.computeViewer` (Compute Recommender Viewer) is now GA.  
Recommender  |  Now GA  |  The role `roles/recommender.iamAdmin` (IAM Recommender Admin) is now GA.  
Recommender  |  Now GA  |  The role `roles/recommender.iamViewer` (IAM Recommender Viewer) is now GA.  
Remote Build Execution  |  Role Added  |  The role `roles/remotebuildexecution.reservationAdmin` (Remote Build Execution Reservation Admin) has been added with the following permissions: `remotebuildexecution.actions.create`  
`remotebuildexecution.actions.delete`  
`remotebuildexecution.actions.get`  
  
Bigtable  |  Added  |  `bigtable.tables.getIamPolicy`  
`bigtable.tables.setIamPolicy`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.tables.getIamPolicy`  
`bigtable.tables.setIamPolicy`  
  
Bigtable  |  Now GA  |  `bigtable.tables.getIamPolicy`  
`bigtable.tables.setIamPolicy`  
  
Compute Engine  |  Added  |  `compute.nodeGroups.update`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.nodeGroups.update`  
  
Compute Engine  |  Now GA  |  `compute.networks.mirror`  
`compute.packetMirrorings.update`  
`compute.subnetworks.mirror`  
  
Data Catalog  |  Added  |  `datacatalog.entries.list`  
`datacatalog.entries.updateTag`  
`datacatalog.entryGroups.update`  
  
Managed Service for Apache Spark  |  Added  |  `dataproc.autoscalingPolicies.create`  
`dataproc.autoscalingPolicies.delete`  
`dataproc.autoscalingPolicies.get`  
`dataproc.autoscalingPolicies.getIamPolicy`  
`dataproc.autoscalingPolicies.list`  
`dataproc.autoscalingPolicies.setIamPolicy`  
`dataproc.autoscalingPolicies.update`  
`dataproc.autoscalingPolicies.use`  
  
Managed Service for Apache Spark  |  Now GA  |  `dataproc.autoscalingPolicies.create`  
`dataproc.autoscalingPolicies.delete`  
`dataproc.autoscalingPolicies.get`  
`dataproc.autoscalingPolicies.getIamPolicy`  
`dataproc.autoscalingPolicies.list`  
`dataproc.autoscalingPolicies.setIamPolicy`  
`dataproc.autoscalingPolicies.update`  
`dataproc.autoscalingPolicies.use`  
  
Cloud DNS  |  Now GA  |  `dns.networks.targetWithPeeringZone`  
  
Cloud Logging  |  Added  |  `logging.cmekSettings.get`  
`logging.cmekSettings.update`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.cmekSettings.get`  
`logging.cmekSettings.update`  
  
Cloud Logging  |  Now GA  |  `logging.cmekSettings.get`  
`logging.cmekSettings.update`  
  
Recommender  |  Now GA  |  `recommender.computeInstanceGroupManagerMachineTypeRecommendations.get`  
`recommender.computeInstanceGroupManagerMachineTypeRecommendations.list`  
`recommender.computeInstanceGroupManagerMachineTypeRecommendations.update`  
`recommender.computeInstanceMachineTypeRecommendations.get`  
`recommender.computeInstanceMachineTypeRecommendations.list`  
`recommender.computeInstanceMachineTypeRecommendations.update`  
`recommender.iamPolicyRecommendations.get`  
`recommender.iamPolicyRecommendations.list`  
`recommender.iamPolicyRecommendations.update`  
`recommender.locations.get`  
`recommender.locations.list`  
  
  
## Cloud IAM changes as of 2019-11-22

Service | Change | Description  
---|---|---  
Data Catalog  |  Role Updated  |  The following permissions have been removed from the role `roles/datacatalog.admin` (Data Catalog Admin): `datacatalog.categories.fineGrainedGet`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `remotebuildexecution.actions.delete`  
  
Identity Toolkit  |  Now GA  |  The role `roles/identitytoolkit.admin` (Identity Toolkit Admin) is now GA.  
Identity Toolkit  |  Now GA  |  The role `roles/identitytoolkit.viewer` (Identity Toolkit Viewer) is now GA.  
Apigee  |  Added  |  `apigee.apiproductattributes.createOrUpdateAll`  
`apigee.apiproductattributes.delete`  
`apigee.apiproductattributes.get`  
`apigee.apiproductattributes.list`  
`apigee.apiproductattributes.update`  
`apigee.apiproducts.create`  
`apigee.apiproducts.delete`  
`apigee.apiproducts.get`  
`apigee.apiproducts.list`  
`apigee.apiproducts.update`  
`apigee.appkeys.create`  
`apigee.appkeys.delete`  
`apigee.appkeys.get`  
`apigee.appkeys.manage`  
`apigee.apps.get`  
`apigee.apps.list`  
`apigee.deployments.create`  
`apigee.deployments.delete`  
`apigee.deployments.get`  
`apigee.deployments.list`  
`apigee.deployments.update`  
`apigee.developerappattributes.createOrUpdateAll`  
`apigee.developerappattributes.delete`  
`apigee.developerappattributes.get`  
`apigee.developerappattributes.list`  
`apigee.developerappattributes.update`  
`apigee.developerapps.create`  
`apigee.developerapps.delete`  
`apigee.developerapps.get`  
`apigee.developerapps.list`  
`apigee.developerapps.manage`  
`apigee.developerattributes.createOrUpdateAll`  
`apigee.developerattributes.delete`  
`apigee.developerattributes.get`  
`apigee.developerattributes.list`  
`apigee.developerattributes.update`  
`apigee.developers.create`  
`apigee.developers.delete`  
`apigee.developers.get`  
`apigee.developers.list`  
`apigee.developers.update`  
`apigee.environments.create`  
`apigee.environments.delete`  
`apigee.environments.get`  
`apigee.environments.getDataLocation`  
`apigee.environments.getIamPolicy`  
`apigee.environments.getStats`  
`apigee.environments.list`  
`apigee.environments.manageRuntime`  
`apigee.environments.setIamPolicy`  
`apigee.environments.update`  
`apigee.flowhooks.attachSharedFlow`  
`apigee.flowhooks.detachSharedFlow`  
`apigee.flowhooks.getSharedFlow`  
`apigee.flowhooks.list`  
`apigee.keystorealiases.create`  
`apigee.keystorealiases.delete`  
`apigee.keystorealiases.exportCertificate`  
`apigee.keystorealiases.generateCSR`  
`apigee.keystorealiases.get`  
`apigee.keystorealiases.list`  
`apigee.keystorealiases.update`  
`apigee.keystores.create`  
`apigee.keystores.delete`  
`apigee.keystores.export`  
`apigee.keystores.get`  
`apigee.keystores.list`  
`apigee.keyvaluemaps.create`  
`apigee.keyvaluemaps.delete`  
`apigee.keyvaluemaps.list`  
`apigee.maskconfigs.get`  
`apigee.maskconfigs.update`  
`apigee.organizations.create`  
`apigee.organizations.get`  
`apigee.organizations.list`  
`apigee.organizations.update`  
`apigee.proxies.create`  
`apigee.proxies.delete`  
`apigee.proxies.get`  
`apigee.proxies.list`  
`apigee.proxyrevisions.delete`  
`apigee.proxyrevisions.deploy`  
`apigee.proxyrevisions.get`  
`apigee.proxyrevisions.list`  
`apigee.proxyrevisions.undeploy`  
`apigee.proxyrevisions.update`  
`apigee.queries.create`  
`apigee.queries.get`  
`apigee.queries.list`  
`apigee.references.create`  
`apigee.references.delete`  
`apigee.references.get`  
`apigee.references.list`  
`apigee.references.update`  
`apigee.reports.create`  
`apigee.reports.delete`  
`apigee.reports.get`  
`apigee.reports.list`  
`apigee.reports.update`  
`apigee.resourcefiles.create`  
`apigee.resourcefiles.delete`  
`apigee.resourcefiles.get`  
`apigee.resourcefiles.list`  
`apigee.resourcefiles.update`  
`apigee.sharedflowrevisions.delete`  
`apigee.sharedflowrevisions.deploy`  
`apigee.sharedflowrevisions.get`  
`apigee.sharedflowrevisions.list`  
`apigee.sharedflowrevisions.undeploy`  
`apigee.sharedflowrevisions.update`  
`apigee.sharedflows.create`  
`apigee.sharedflows.delete`  
`apigee.sharedflows.get`  
`apigee.sharedflows.list`  
`apigee.targetservers.create`  
`apigee.targetservers.delete`  
`apigee.targetservers.get`  
`apigee.targetservers.list`  
`apigee.targetservers.update`  
`apigee.tracesessions.create`  
`apigee.tracesessions.delete`  
`apigee.tracesessions.get`  
`apigee.tracesessions.list`  
  
Apigee  |  Supported In Custom Roles  |  `apigee.apiproductattributes.createOrUpdateAll`  
`apigee.apiproductattributes.delete`  
`apigee.apiproductattributes.get`  
`apigee.apiproductattributes.list`  
`apigee.apiproductattributes.update`  
`apigee.apiproducts.create`  
`apigee.apiproducts.delete`  
`apigee.apiproducts.get`  
`apigee.apiproducts.list`  
`apigee.apiproducts.update`  
`apigee.appkeys.create`  
`apigee.appkeys.delete`  
`apigee.appkeys.get`  
`apigee.appkeys.manage`  
`apigee.apps.get`  
`apigee.apps.list`  
`apigee.deployments.create`  
`apigee.deployments.delete`  
`apigee.deployments.get`  
`apigee.deployments.list`  
`apigee.deployments.update`  
`apigee.developerappattributes.createOrUpdateAll`  
`apigee.developerappattributes.delete`  
`apigee.developerappattributes.get`  
`apigee.developerappattributes.list`  
`apigee.developerappattributes.update`  
`apigee.developerapps.create`  
`apigee.developerapps.delete`  
`apigee.developerapps.get`  
`apigee.developerapps.list`  
`apigee.developerapps.manage`  
`apigee.developerattributes.createOrUpdateAll`  
`apigee.developerattributes.delete`  
`apigee.developerattributes.get`  
`apigee.developerattributes.list`  
`apigee.developerattributes.update`  
`apigee.developers.create`  
`apigee.developers.delete`  
`apigee.developers.get`  
`apigee.developers.list`  
`apigee.developers.update`  
`apigee.environments.create`  
`apigee.environments.delete`  
`apigee.environments.get`  
`apigee.environments.getDataLocation`  
`apigee.environments.getIamPolicy`  
`apigee.environments.getStats`  
`apigee.environments.list`  
`apigee.environments.manageRuntime`  
`apigee.environments.setIamPolicy`  
`apigee.environments.update`  
`apigee.flowhooks.attachSharedFlow`  
`apigee.flowhooks.detachSharedFlow`  
`apigee.flowhooks.getSharedFlow`  
`apigee.flowhooks.list`  
`apigee.keystorealiases.create`  
`apigee.keystorealiases.delete`  
`apigee.keystorealiases.exportCertificate`  
`apigee.keystorealiases.generateCSR`  
`apigee.keystorealiases.get`  
`apigee.keystorealiases.list`  
`apigee.keystorealiases.update`  
`apigee.keystores.create`  
`apigee.keystores.delete`  
`apigee.keystores.export`  
`apigee.keystores.get`  
`apigee.keystores.list`  
`apigee.keyvaluemaps.create`  
`apigee.keyvaluemaps.delete`  
`apigee.keyvaluemaps.list`  
`apigee.maskconfigs.get`  
`apigee.maskconfigs.update`  
`apigee.organizations.create`  
`apigee.organizations.get`  
`apigee.organizations.list`  
`apigee.organizations.update`  
`apigee.proxies.create`  
`apigee.proxies.delete`  
`apigee.proxies.get`  
`apigee.proxies.list`  
`apigee.proxyrevisions.delete`  
`apigee.proxyrevisions.deploy`  
`apigee.proxyrevisions.get`  
`apigee.proxyrevisions.list`  
`apigee.proxyrevisions.undeploy`  
`apigee.proxyrevisions.update`  
`apigee.queries.create`  
`apigee.queries.get`  
`apigee.queries.list`  
`apigee.references.create`  
`apigee.references.delete`  
`apigee.references.get`  
`apigee.references.list`  
`apigee.references.update`  
`apigee.reports.create`  
`apigee.reports.delete`  
`apigee.reports.get`  
`apigee.reports.list`  
`apigee.reports.update`  
`apigee.resourcefiles.create`  
`apigee.resourcefiles.delete`  
`apigee.resourcefiles.get`  
`apigee.resourcefiles.list`  
`apigee.resourcefiles.update`  
`apigee.sharedflowrevisions.delete`  
`apigee.sharedflowrevisions.deploy`  
`apigee.sharedflowrevisions.get`  
`apigee.sharedflowrevisions.list`  
`apigee.sharedflowrevisions.undeploy`  
`apigee.sharedflowrevisions.update`  
`apigee.sharedflows.create`  
`apigee.sharedflows.delete`  
`apigee.sharedflows.get`  
`apigee.sharedflows.list`  
`apigee.targetservers.create`  
`apigee.targetservers.delete`  
`apigee.targetservers.get`  
`apigee.targetservers.list`  
`apigee.targetservers.update`  
`apigee.tracesessions.create`  
`apigee.tracesessions.delete`  
`apigee.tracesessions.get`  
`apigee.tracesessions.list`  
  
BigQuery  |  Added  |  `bigquery.tables.setCategory`  
  
Compute Engine  |  Added  |  `compute.networks.mirror`  
`compute.packetMirrorings.update`  
`compute.subnetworks.mirror`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.networks.mirror`  
`compute.packetMirrorings.update`  
`compute.subnetworks.mirror`  
  
Remote Build Execution  |  Added  |  `remotebuildexecution.actions.delete`  
  
Remote Build Execution  |  Supported In Custom Roles  |  `remotebuildexecution.actions.delete`  
  
  
## Cloud IAM changes as of 2019-11-14

Service | Change | Description  
---|---|---  
Access Approval  |  Added  |  `accessapproval.settings.delete`  
  
Notebooks  |  Added  |  `notebooks.environments.create`  
`notebooks.environments.delete`  
`notebooks.environments.get`  
`notebooks.environments.getIamPolicy`  
`notebooks.environments.list`  
`notebooks.environments.setIamPolicy`  
`notebooks.instances.create`  
`notebooks.instances.delete`  
`notebooks.instances.get`  
`notebooks.instances.getIamPolicy`  
`notebooks.instances.list`  
`notebooks.instances.setIamPolicy`  
`notebooks.instances.update`  
`notebooks.locations.get`  
`notebooks.locations.list`  
`notebooks.operations.cancel`  
`notebooks.operations.delete`  
`notebooks.operations.get`  
`notebooks.operations.list`  
  
Notebooks  |  Supported In Custom Roles  |  `notebooks.environments.create`  
`notebooks.environments.delete`  
`notebooks.environments.get`  
`notebooks.environments.getIamPolicy`  
`notebooks.environments.list`  
`notebooks.environments.setIamPolicy`  
`notebooks.instances.create`  
`notebooks.instances.delete`  
`notebooks.instances.get`  
`notebooks.instances.getIamPolicy`  
`notebooks.instances.list`  
`notebooks.instances.setIamPolicy`  
`notebooks.instances.update`  
`notebooks.locations.get`  
`notebooks.locations.list`  
`notebooks.operations.cancel`  
`notebooks.operations.delete`  
`notebooks.operations.get`  
`notebooks.operations.list`  
  
  
## Cloud IAM changes as of 2019-11-01

Service | Change | Description  
---|---|---  
Hangouts Chat  |  Now GA  |  The role `roles/chat.owner` (Chat Bots Owner) is now GA.  
Hangouts Chat  |  Now GA  |  The role `roles/chat.reader` (Chat Bots Viewer) is now GA.  
Hangouts Chat  |  Now GA  |  `chat.bots.get`  
`chat.bots.update`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.exportAppengineApplications`  
`cloudasset.assets.exportAppengineServices`  
`cloudasset.assets.exportAppengineVersions`  
`cloudasset.assets.exportBigqueryDatasets`  
`cloudasset.assets.exportBigqueryTables`  
`cloudasset.assets.exportBigtableCluster`  
`cloudasset.assets.exportBigtableInstance`  
`cloudasset.assets.exportBigtableTable`  
`cloudasset.assets.exportCloudbillingBillingAccounts`  
`cloudasset.assets.exportCloudkmsCryptoKeyVersions`  
`cloudasset.assets.exportCloudkmsCryptoKeys`  
`cloudasset.assets.exportCloudkmsKeyRings`  
`cloudasset.assets.exportCloudresourcemanagerFolders`  
`cloudasset.assets.exportCloudresourcemanagerOrganizations`  
`cloudasset.assets.exportCloudresourcemanagerProjects`  
`cloudasset.assets.exportComputeAddress`  
`cloudasset.assets.exportComputeAutoscalers`  
`cloudasset.assets.exportComputeBackendBuckets`  
`cloudasset.assets.exportComputeBackendServices`  
`cloudasset.assets.exportComputeDisks`  
`cloudasset.assets.exportComputeFirewalls`  
`cloudasset.assets.exportComputeForwardingRules`  
`cloudasset.assets.exportComputeGlobalAddress`  
`cloudasset.assets.exportComputeGlobalForwardingRules`  
`cloudasset.assets.exportComputeHealthChecks`  
`cloudasset.assets.exportComputeHttpHealthChecks`  
`cloudasset.assets.exportComputeHttpsHealthChecks`  
`cloudasset.assets.exportComputeImages`  
`cloudasset.assets.exportComputeInstanceGroupManagers`  
`cloudasset.assets.exportComputeInstanceGroups`  
`cloudasset.assets.exportComputeInstanceTemplates`  
`cloudasset.assets.exportComputeInstances`  
`cloudasset.assets.exportComputeInterconnect`  
`cloudasset.assets.exportComputeInterconnectAttachment`  
`cloudasset.assets.exportComputeLicenses`  
`cloudasset.assets.exportComputeNetworks`  
`cloudasset.assets.exportComputeProjects`  
`cloudasset.assets.exportComputeRegionAutoscaler`  
`cloudasset.assets.exportComputeRegionBackendServices`  
`cloudasset.assets.exportComputeRegionDisk`  
`cloudasset.assets.exportComputeRegionInstanceGroup`  
`cloudasset.assets.exportComputeRegionInstanceGroupManager`  
`cloudasset.assets.exportComputeRouters`  
`cloudasset.assets.exportComputeRoutes`  
`cloudasset.assets.exportComputeSecurityPolicy`  
`cloudasset.assets.exportComputeSnapshots`  
`cloudasset.assets.exportComputeSslCertificates`  
`cloudasset.assets.exportComputeSubnetworks`  
`cloudasset.assets.exportComputeTargetHttpProxies`  
`cloudasset.assets.exportComputeTargetHttpsProxies`  
`cloudasset.assets.exportComputeTargetInstances`  
`cloudasset.assets.exportComputeTargetPools`  
`cloudasset.assets.exportComputeTargetSslProxies`  
`cloudasset.assets.exportComputeTargetTcpProxies`  
`cloudasset.assets.exportComputeTargetVpnGateways`  
`cloudasset.assets.exportComputeUrlMaps`  
`cloudasset.assets.exportComputeVpnTunnels`  
`cloudasset.assets.exportContainerClusterrole`  
`cloudasset.assets.exportContainerClusterrolebinding`  
`cloudasset.assets.exportContainerClusters`  
`cloudasset.assets.exportContainerNamespace`  
`cloudasset.assets.exportContainerNode`  
`cloudasset.assets.exportContainerNodepool`  
`cloudasset.assets.exportContainerPod`  
`cloudasset.assets.exportContainerRole`  
`cloudasset.assets.exportContainerRolebinding`  
`cloudasset.assets.exportContainerregistryImage`  
`cloudasset.assets.exportDatafusionInstance`  
`cloudasset.assets.exportDataprocClusters`  
`cloudasset.assets.exportDataprocJobs`  
`cloudasset.assets.exportDnsManagedZones`  
`cloudasset.assets.exportDnsPolicies`  
`cloudasset.assets.exportIamRoles`  
`cloudasset.assets.exportIamServiceAccountKeys`  
`cloudasset.assets.exportIamServiceAccounts`  
`cloudasset.assets.exportManagedidentitiesDomain`  
`cloudasset.assets.exportPubsubSubscriptions`  
`cloudasset.assets.exportPubsubTopics`  
`cloudasset.assets.exportServicemanagementServices`  
`cloudasset.assets.exportSpannerDatabases`  
`cloudasset.assets.exportSpannerInstances`  
`cloudasset.assets.exportSqladminInstances`  
`cloudasset.assets.exportStorageBuckets`  
  
Data Catalog  |  Added  |  `datacatalog.categories.fineGrainedGet`  
`datacatalog.categories.getIamPolicy`  
`datacatalog.categories.setIamPolicy`  
`datacatalog.taxonomies.create`  
`datacatalog.taxonomies.delete`  
`datacatalog.taxonomies.get`  
`datacatalog.taxonomies.getIamPolicy`  
`datacatalog.taxonomies.list`  
`datacatalog.taxonomies.setIamPolicy`  
`datacatalog.taxonomies.update`  
  
Identity-Aware Proxy  |  Added  |  `iap.projects.getSettings`  
`iap.projects.updateSettings`  
  
NetApp Cloud Volumes Service  |  Added  |  `netappcloudvolumes.jobs.get`  
`netappcloudvolumes.jobs.list`  
  
Redis Enterprise Cloud  |  Added  |  `redisenterprisecloud.databases.create`  
`redisenterprisecloud.databases.delete`  
`redisenterprisecloud.databases.get`  
`redisenterprisecloud.databases.list`  
`redisenterprisecloud.databases.update`  
`redisenterprisecloud.subscriptions.create`  
`redisenterprisecloud.subscriptions.delete`  
`redisenterprisecloud.subscriptions.get`  
`redisenterprisecloud.subscriptions.list`  
`redisenterprisecloud.subscriptions.update`  
  
  
## Cloud IAM changes as of 2019-10-25

Service | Change | Description  
---|---|---  
Identity-Aware Proxy  |  Now GA  |  The role `roles/iap.tunnelResourceAccessor` (IAP-secured Tunnel User) is now GA.  
Managed Service for Microsoft Active Directory  |  Now GA  |  The role `roles/managedidentities.admin` (Google Cloud Managed Identities Admin) is now GA.  
Managed Service for Microsoft Active Directory  |  Now GA  |  The role `roles/managedidentities.domainAdmin` (Google Cloud Managed Identities Domain Admin) is now GA.  
Managed Service for Microsoft Active Directory  |  Now GA  |  The role `roles/managedidentities.viewer` (Google Cloud Managed Identities Viewer) is now GA.  
Actions  |  Added  |  `actions.agentVersions.get`  
  
Actions  |  Supported In Custom Roles  |  `actions.agentVersions.get`  
  
Actions  |  Now GA  |  `actions.agentVersions.get`  
  
Dialogflow  |  Added  |  `dialogflow.documents.create`  
`dialogflow.documents.delete`  
`dialogflow.documents.get`  
`dialogflow.documents.list`  
`dialogflow.knowledgeBases.create`  
`dialogflow.knowledgeBases.delete`  
`dialogflow.knowledgeBases.get`  
`dialogflow.knowledgeBases.list`  
  
Dialogflow  |  Now GA  |  `dialogflow.documents.create`  
`dialogflow.documents.delete`  
`dialogflow.documents.get`  
`dialogflow.documents.list`  
`dialogflow.knowledgeBases.create`  
`dialogflow.knowledgeBases.delete`  
`dialogflow.knowledgeBases.get`  
`dialogflow.knowledgeBases.list`  
  
Identity-Aware Proxy  |  Now GA  |  `iap.tunnel.getIamPolicy`  
`iap.tunnel.setIamPolicy`  
`iap.tunnelInstances.accessViaIAP`  
`iap.tunnelInstances.getIamPolicy`  
`iap.tunnelInstances.setIamPolicy`  
`iap.tunnelZones.getIamPolicy`  
`iap.tunnelZones.setIamPolicy`  
  
Managed Service for Microsoft Active Directory  |  Now GA  |  `managedidentities.domains.attachTrust`  
`managedidentities.domains.create`  
`managedidentities.domains.delete`  
`managedidentities.domains.detachTrust`  
`managedidentities.domains.get`  
`managedidentities.domains.getIamPolicy`  
`managedidentities.domains.list`  
`managedidentities.domains.reconfigureTrust`  
`managedidentities.domains.resetpassword`  
`managedidentities.domains.setIamPolicy`  
`managedidentities.domains.update`  
`managedidentities.domains.validateTrust`  
`managedidentities.locations.get`  
`managedidentities.locations.list`  
`managedidentities.operations.cancel`  
`managedidentities.operations.delete`  
`managedidentities.operations.get`  
`managedidentities.operations.list`  
  
  
## Cloud IAM changes as of 2019-10-18

Service | Change | Description  
---|---|---  
Identity-Aware Proxy  |  Now GA  |  The role `roles/iap.settingsAdmin` (IAP Settings Admin) is now GA.  
Identity-Aware Proxy  |  Added  |  `iap.web.getSettings`  
`iap.web.updateSettings`  
`iap.webServiceVersions.getSettings`  
`iap.webServiceVersions.updateSettings`  
`iap.webServices.getSettings`  
`iap.webServices.updateSettings`  
`iap.webTypes.getSettings`  
`iap.webTypes.updateSettings`  
  
  
## Cloud IAM changes as of 2019-10-11

Service | Change | Description  
---|---|---  
Firebase Security Rules  |  Now GA  |  The role `roles/firebaserules.admin` (Firebase Rules Admin) is now GA.  
Firebase Security Rules  |  Now GA  |  The role `roles/firebaserules.viewer` (Firebase Rules Viewer) is now GA.  
BigQuery  |  Supported In Custom Roles  |  `bigquery.transfers.get`  
`bigquery.transfers.update`  
  
Google Kubernetes Engine  |  Added  |  `container.csiDrivers.create`  
`container.csiDrivers.delete`  
`container.csiDrivers.get`  
`container.csiDrivers.list`  
`container.csiDrivers.update`  
`container.csiNodes.create`  
`container.csiNodes.delete`  
`container.csiNodes.get`  
`container.csiNodes.list`  
`container.csiNodes.update`  
`container.runtimeClasses.create`  
`container.runtimeClasses.delete`  
`container.runtimeClasses.get`  
`container.runtimeClasses.list`  
`container.runtimeClasses.update`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.csiDrivers.create`  
`container.csiDrivers.delete`  
`container.csiDrivers.get`  
`container.csiDrivers.list`  
`container.csiDrivers.update`  
`container.csiNodes.create`  
`container.csiNodes.delete`  
`container.csiNodes.get`  
`container.csiNodes.list`  
`container.csiNodes.update`  
`container.runtimeClasses.create`  
`container.runtimeClasses.delete`  
`container.runtimeClasses.get`  
`container.runtimeClasses.list`  
`container.runtimeClasses.update`  
  
Google Kubernetes Engine  |  Now GA  |  `container.csiDrivers.create`  
`container.csiDrivers.delete`  
`container.csiDrivers.get`  
`container.csiDrivers.list`  
`container.csiDrivers.update`  
`container.csiNodes.create`  
`container.csiNodes.delete`  
`container.csiNodes.get`  
`container.csiNodes.list`  
`container.csiNodes.update`  
`container.runtimeClasses.create`  
`container.runtimeClasses.delete`  
`container.runtimeClasses.get`  
`container.runtimeClasses.list`  
`container.runtimeClasses.update`  
  
Firebase Security Rules  |  Now GA  |  `firebaserules.releases.create`  
`firebaserules.releases.delete`  
`firebaserules.releases.get`  
`firebaserules.releases.getExecutable`  
`firebaserules.releases.list`  
`firebaserules.releases.update`  
`firebaserules.rulesets.create`  
`firebaserules.rulesets.delete`  
`firebaserules.rulesets.get`  
`firebaserules.rulesets.list`  
`firebaserules.rulesets.test`  
  
  
## Cloud IAM changes as of 2019-10-04

Service | Change | Description  
---|---|---  
Actions  |  Added  |  `actions.agent.claimContentProvider`  
`actions.agent.get`  
`actions.agent.update`  
`actions.agentVersions.create`  
`actions.agentVersions.delete`  
`actions.agentVersions.deploy`  
`actions.agentVersions.list`  
  
Actions  |  Supported In Custom Roles  |  `actions.agent.claimContentProvider`  
`actions.agent.get`  
`actions.agent.update`  
`actions.agentVersions.create`  
`actions.agentVersions.delete`  
`actions.agentVersions.deploy`  
`actions.agentVersions.list`  
  
Actions  |  Now GA  |  `actions.agent.claimContentProvider`  
`actions.agent.get`  
`actions.agent.update`  
`actions.agentVersions.create`  
`actions.agentVersions.delete`  
`actions.agentVersions.deploy`  
`actions.agentVersions.list`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `iam.serviceAccounts.actAs`  
`iam.serviceAccounts.getAccessToken`  
`iam.serviceAccounts.implicitDelegation`  
  
  
## Cloud IAM changes as of 2019-09-27

Service | Change | Description  
---|---|---  
Hangouts Chat  |  Added  |  `chat.bots.get`  
`chat.bots.update`  
  
Hangouts Chat  |  Supported In Custom Roles  |  `chat.bots.get`  
`chat.bots.update`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.exportAccessLevel`  
`cloudasset.assets.exportAccessPolicy`  
`cloudasset.assets.exportAllAccessPolicy`  
`cloudasset.assets.exportOrgPolicy`  
`cloudasset.assets.exportServicePerimeter`  
`cloudasset.feeds.create`  
`cloudasset.feeds.delete`  
`cloudasset.feeds.get`  
`cloudasset.feeds.list`  
`cloudasset.feeds.update`  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `cloudasset.assets.exportAccessPolicy`  
`cloudasset.assets.exportOrgPolicy`  
`cloudasset.feeds.create`  
`cloudasset.feeds.delete`  
`cloudasset.feeds.get`  
`cloudasset.feeds.list`  
`cloudasset.feeds.update`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `iam.serviceAccountKeys.create`  
`iam.serviceAccountKeys.delete`  
`iam.serviceAccountKeys.get`  
`iam.serviceAccountKeys.list`  
`iam.serviceAccounts.create`  
`iam.serviceAccounts.delete`  
`iam.serviceAccounts.get`  
`iam.serviceAccounts.getIamPolicy`  
`iam.serviceAccounts.list`  
`iam.serviceAccounts.setIamPolicy`  
`iam.serviceAccounts.signBlob`  
`iam.serviceAccounts.signJwt`  
`iam.serviceAccounts.update`  
  
VM Migration  |  Added  |  `vmmigration.deployments.create`  
`vmmigration.deployments.get`  
`vmmigration.deployments.list`  
  
VM Migration  |  Supported In Custom Roles  |  `vmmigration.deployments.create`  
`vmmigration.deployments.get`  
`vmmigration.deployments.list`  
  
  
## Cloud IAM changes as of 2019-09-20

Service | Change | Description  
---|---|---  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.importer` (Cloud KMS Importer) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.publicKeyViewer` (Cloud KMS CryptoKey Public Key Viewer) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.signer` (Cloud KMS CryptoKey Signer) is now GA.  
Cloud Key Management Service  |  Now GA  |  The role `roles/cloudkms.signerVerifier` (Cloud KMS CryptoKey Signer/Verifier) is now GA.  
Cloud Key Management Service  |  Added  |  `cloudkms.importJobs.create`  
`cloudkms.importJobs.get`  
`cloudkms.importJobs.getIamPolicy`  
`cloudkms.importJobs.list`  
`cloudkms.importJobs.setIamPolicy`  
`cloudkms.importJobs.useToImport`  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `cloudkms.importJobs.create`  
`cloudkms.importJobs.get`  
`cloudkms.importJobs.getIamPolicy`  
`cloudkms.importJobs.list`  
`cloudkms.importJobs.setIamPolicy`  
`cloudkms.importJobs.useToImport`  
  
Cloud Key Management Service  |  Now GA  |  `cloudkms.cryptoKeyVersions.useToSign`  
`cloudkms.cryptoKeyVersions.viewPublicKey`  
`cloudkms.importJobs.create`  
`cloudkms.importJobs.get`  
`cloudkms.importJobs.getIamPolicy`  
`cloudkms.importJobs.list`  
`cloudkms.importJobs.setIamPolicy`  
`cloudkms.importJobs.useToImport`  
  
  
## Cloud IAM changes as of 2019-09-13

Service | Change | Description  
---|---|---  
Firebase Remote Config  |  Now GA  |  The role `roles/cloudconfig.admin` (Firebase Remote Config Admin) is now GA.  
Firebase Remote Config  |  Now GA  |  The role `roles/cloudconfig.viewer` (Firebase Remote Config Viewer) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.admin` (Firebase Admin) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.analyticsAdmin` (Firebase Analytics Admin) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.analyticsViewer` (Firebase Analytics Viewer) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.developAdmin` (Firebase Develop Admin) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.developViewer` (Firebase Develop Viewer) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.growthAdmin` (Firebase Grow Admin) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.growthViewer` (Firebase Grow Viewer) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.qualityAdmin` (Firebase Quality Admin) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.qualityViewer` (Firebase Quality Viewer) is now GA.  
Firebase  |  Now GA  |  The role `roles/firebase.viewer` (Firebase Viewer) is now GA.  
Firebase Authentication  |  Now GA  |  The role `roles/firebaseauth.admin` (Firebase Authentication Admin) is now GA.  
Firebase Authentication  |  Now GA  |  The role `roles/firebaseauth.viewer` (Firebase Authentication Viewer) is now GA.  
Firebase Crashlytics  |  Now GA  |  The role `roles/firebasecrashlytics.admin` (Firebase Crashlytics Admin) is now GA.  
Firebase Crashlytics  |  Now GA  |  The role `roles/firebasecrashlytics.viewer` (Firebase Crashlytics Viewer) is now GA.  
Firebase Realtime Database  |  Now GA  |  The role `roles/firebasedatabase.admin` (Firebase Realtime Database Admin) is now GA.  
Firebase Realtime Database  |  Now GA  |  The role `roles/firebasedatabase.viewer` (Firebase Realtime Database Viewer) is now GA.  
Firebase Dynamic Links  |  Now GA  |  The role `roles/firebasedynamiclinks.admin` (Firebase Dynamic Links Admin) is now GA.  
Firebase Dynamic Links  |  Now GA  |  The role `roles/firebasedynamiclinks.viewer` (Firebase Dynamic Links Viewer) is now GA.  
Firebase Hosting  |  Now GA  |  The role `roles/firebasehosting.admin` (Firebase Hosting Admin) is now GA.  
Firebase Hosting  |  Now GA  |  The role `roles/firebasehosting.viewer` (Firebase Hosting Viewer) is now GA.  
Firebase Cloud Messaging  |  Now GA  |  The role `roles/firebasenotifications.admin` (Firebase Cloud Messaging Admin) is now GA.  
Firebase Cloud Messaging  |  Now GA  |  The role `roles/firebasenotifications.viewer` (Firebase Cloud Messaging Viewer) is now GA.  
Firebase Performance Monitoring  |  Now GA  |  The role `roles/firebaseperformance.admin` (Firebase Performance Reporting Admin) is now GA.  
Firebase Performance Monitoring  |  Now GA  |  The role `roles/firebaseperformance.viewer` (Firebase Performance Reporting Viewer) is now GA.  
Firebase Predictions  |  Now GA  |  The role `roles/firebasepredictions.admin` (Firebase Predictions Admin) is now GA.  
Firebase Predictions  |  Now GA  |  The role `roles/firebasepredictions.viewer` (Firebase Predictions Viewer) is now GA.  
Firebase Remote Config  |  Now GA  |  `cloudconfig.configs.get`  
`cloudconfig.configs.update`  
  
Cloud DNS  |  Now GA  |  `dns.networks.bindPrivateDNSPolicy`  
`dns.policies.create`  
`dns.policies.delete`  
`dns.policies.get`  
`dns.policies.getIamPolicy`  
`dns.policies.list`  
`dns.policies.setIamPolicy`  
`dns.policies.update`  
  
Firebase  |  Now GA  |  `firebase.billingPlans.get`  
`firebase.billingPlans.update`  
`firebase.clients.create`  
`firebase.clients.delete`  
`firebase.clients.get`  
`firebase.links.create`  
`firebase.links.delete`  
`firebase.links.list`  
`firebase.links.update`  
`firebase.projects.delete`  
`firebase.projects.get`  
`firebase.projects.update`  
  
Firebase Authentication  |  Now GA  |  `firebaseauth.configs.create`  
`firebaseauth.configs.get`  
`firebaseauth.configs.getHashConfig`  
`firebaseauth.configs.update`  
`firebaseauth.users.create`  
`firebaseauth.users.createSession`  
`firebaseauth.users.delete`  
`firebaseauth.users.get`  
`firebaseauth.users.sendEmail`  
`firebaseauth.users.update`  
  
Firebase Crashlytics  |  Now GA  |  `firebasecrashlytics.config.get`  
`firebasecrashlytics.config.update`  
`firebasecrashlytics.data.get`  
`firebasecrashlytics.issues.get`  
`firebasecrashlytics.issues.list`  
`firebasecrashlytics.issues.update`  
`firebasecrashlytics.sessions.get`  
  
Firebase Realtime Database  |  Now GA  |  `firebasedatabase.instances.create`  
`firebasedatabase.instances.get`  
`firebasedatabase.instances.list`  
`firebasedatabase.instances.update`  
  
Firebase Dynamic Links  |  Now GA  |  `firebasedynamiclinks.destinations.list`  
`firebasedynamiclinks.destinations.update`  
`firebasedynamiclinks.domains.create`  
`firebasedynamiclinks.domains.delete`  
`firebasedynamiclinks.domains.get`  
`firebasedynamiclinks.domains.list`  
`firebasedynamiclinks.domains.update`  
`firebasedynamiclinks.links.create`  
`firebasedynamiclinks.links.get`  
`firebasedynamiclinks.links.list`  
`firebasedynamiclinks.links.update`  
`firebasedynamiclinks.stats.get`  
  
Firebase Hosting  |  Now GA  |  `firebasehosting.sites.create`  
`firebasehosting.sites.delete`  
`firebasehosting.sites.get`  
`firebasehosting.sites.list`  
`firebasehosting.sites.update`  
  
Firebase Cloud Messaging  |  Now GA  |  `firebasenotifications.messages.create`  
`firebasenotifications.messages.delete`  
`firebasenotifications.messages.get`  
`firebasenotifications.messages.list`  
`firebasenotifications.messages.update`  
  
Firebase Performance Monitoring  |  Now GA  |  `firebaseperformance.config.create`  
`firebaseperformance.config.delete`  
`firebaseperformance.config.update`  
`firebaseperformance.data.get`  
  
Firebase Predictions  |  Now GA  |  `firebasepredictions.predictions.create`  
`firebasepredictions.predictions.delete`  
`firebasepredictions.predictions.list`  
`firebasepredictions.predictions.update`  
  
NetApp Cloud Volumes Service  |  Added  |  `netappcloudvolumes.activeDirectories.create`  
`netappcloudvolumes.activeDirectories.delete`  
`netappcloudvolumes.activeDirectories.get`  
`netappcloudvolumes.activeDirectories.list`  
`netappcloudvolumes.activeDirectories.update`  
`netappcloudvolumes.ipRanges.list`  
`netappcloudvolumes.regions.list`  
`netappcloudvolumes.serviceLevels.list`  
`netappcloudvolumes.snapshots.create`  
`netappcloudvolumes.snapshots.delete`  
`netappcloudvolumes.snapshots.get`  
`netappcloudvolumes.snapshots.list`  
`netappcloudvolumes.snapshots.update`  
`netappcloudvolumes.volumes.create`  
`netappcloudvolumes.volumes.delete`  
`netappcloudvolumes.volumes.get`  
`netappcloudvolumes.volumes.list`  
`netappcloudvolumes.volumes.update`  
  
Event Threat Detection  |  Supported In Custom Roles  |  `threatdetection.detectorSettings.clear`  
`threatdetection.detectorSettings.get`  
`threatdetection.detectorSettings.update`  
`threatdetection.sinkSettings.get`  
`threatdetection.sinkSettings.update`  
`threatdetection.sourceSettings.get`  
`threatdetection.sourceSettings.update`  
  
  
## Cloud IAM changes as of 2019-09-06

Service | Change | Description  
---|---|---  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `dataprocessing.iamaccesshistory.exportData`  
  
Serverless VPC Access  |  Now GA  |  The role `roles/vpaccess.user` (Serverless VPC Access User) is now GA.  
Serverless VPC Access  |  Now GA  |  The role `roles/vpaccess.viewer` (Serverless VPC Access Viewer) is now GA.  
Serverless VPC Access  |  Now GA  |  The role `roles/vpcaccess.admin` (Serverless VPC Access Admin) is now GA.  
Compute Engine  |  Added  |  `compute.externalVpnGateways.create`  
`compute.externalVpnGateways.delete`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.externalVpnGateways.setLabels`  
`compute.externalVpnGateways.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.externalVpnGateways.create`  
`compute.externalVpnGateways.delete`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.externalVpnGateways.setLabels`  
`compute.externalVpnGateways.use`  
  
Compute Engine  |  Now GA  |  `compute.externalVpnGateways.create`  
`compute.externalVpnGateways.delete`  
`compute.externalVpnGateways.get`  
`compute.externalVpnGateways.list`  
`compute.externalVpnGateways.setLabels`  
`compute.externalVpnGateways.use`  
  
Serverless VPC Access  |  Now GA  |  `vpcaccess.connectors.create`  
`vpcaccess.connectors.delete`  
`vpcaccess.connectors.get`  
`vpcaccess.connectors.list`  
`vpcaccess.connectors.use`  
`vpcaccess.locations.list`  
`vpcaccess.operations.get`  
`vpcaccess.operations.list`  
  
  
## Cloud IAM changes as of 2019-08-30

Service | Change | Description  
---|---|---  
Firebase Test Lab  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtestservice.testAdmin` (Firebase Test Lab Admin): `firebase.clients.get`  
`firebase.projects.get`  
  
Firebase Test Lab  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtestservice.testViewer` (Firebase Test Lab Viewer): `firebase.clients.get`  
`firebase.projects.get`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityPolicyAdmin` (Compute Organization Security Policy Admin): `compute.globalOperations.get`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.list`  
`compute.globalOperations.setIamPolicy`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityPolicyUser` (Compute Organization Security Policy User): `compute.globalOperations.get`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.list`  
`compute.globalOperations.setIamPolicy`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityResourceAdmin` (Compute Organization Resource Admin): `compute.globalOperations.get`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.list`  
`compute.globalOperations.setIamPolicy`  
  
  
## Cloud IAM changes as of 2019-08-23

Service | Change | Description  
---|---|---  
Translation  |  Now GA  |  The role `roles/cloudtranslate.admin` (Cloud Translation API Admin) is now GA.  
Translation  |  Now GA  |  The role `roles/cloudtranslate.editor` (Cloud Translation API Editor) is now GA.  
Translation  |  Now GA  |  The role `roles/cloudtranslate.user` (Cloud Translation API User) is now GA.  
Translation  |  Now GA  |  The role `roles/cloudtranslate.viewer` (Cloud Translation API Viewer) is now GA.  
Cloud Healthcare API  |  Role Updated  |  The following permissions have been added to the role `roles/healthcare.dicomEditor` (Healthcare DICOM Editor): `healthcare.dicomStores.dicomWebDelete`  
  
Translation  |  Now GA  |  `cloudtranslate.generalModels.batchPredict`  
`cloudtranslate.generalModels.get`  
`cloudtranslate.generalModels.predict`  
`cloudtranslate.glossaries.batchPredict`  
`cloudtranslate.glossaries.create`  
`cloudtranslate.glossaries.delete`  
`cloudtranslate.glossaries.get`  
`cloudtranslate.glossaries.list`  
`cloudtranslate.glossaries.predict`  
`cloudtranslate.languageDetectionModels.predict`  
`cloudtranslate.locations.get`  
`cloudtranslate.locations.list`  
`cloudtranslate.operations.cancel`  
`cloudtranslate.operations.delete`  
`cloudtranslate.operations.get`  
`cloudtranslate.operations.list`  
`cloudtranslate.operations.wait`  
  
  
## Cloud IAM changes as of 2019-08-16

Service | Change | Description  
---|---|---  
Translation  |  Supported In Custom Roles  |  `cloudtranslate.locations.get`  
`cloudtranslate.locations.list`  
  
Compute Engine  |  Now GA  |  `compute.networks.updatePeering`  
  
Data Catalog  |  Added  |  `datacatalog.entries.create`  
`datacatalog.entries.delete`  
`datacatalog.entries.get`  
`datacatalog.entries.getIamPolicy`  
`datacatalog.entries.setIamPolicy`  
`datacatalog.entries.update`  
`datacatalog.entryGroups.create`  
`datacatalog.entryGroups.delete`  
`datacatalog.entryGroups.get`  
`datacatalog.entryGroups.getIamPolicy`  
`datacatalog.entryGroups.setIamPolicy`  
  
Data Catalog  |  Supported In Custom Roles  |  `datacatalog.entries.create`  
`datacatalog.entries.delete`  
`datacatalog.entries.get`  
`datacatalog.entries.getIamPolicy`  
`datacatalog.entries.setIamPolicy`  
`datacatalog.entries.update`  
`datacatalog.entryGroups.create`  
`datacatalog.entryGroups.delete`  
`datacatalog.entryGroups.get`  
`datacatalog.entryGroups.getIamPolicy`  
`datacatalog.entryGroups.setIamPolicy`  
  
  
## Cloud IAM changes as of 2019-08-09

Service | Change | Description  
---|---|---  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityPolicyAdmin` (Compute Organization Security Policy Admin): `compute.projects.get`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityPolicyUser` (Compute Organization Security Policy User): `compute.projects.get`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.orgSecurityResourceAdmin` (Compute organization resource Admin): `compute.projects.get`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`serviceusage.quotas.get`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
Cloud Storage  |  Now GA  |  The role `roles/storage.hmacKeyAdmin` (Storage HMAC Key Admin) is now GA.  
Cloud Storage  |  Added  |  `storage.hmacKeys.create`  
`storage.hmacKeys.delete`  
`storage.hmacKeys.get`  
`storage.hmacKeys.list`  
`storage.hmacKeys.update`  
  
Cloud Storage  |  Supported In Custom Roles  |  `storage.hmacKeys.create`  
`storage.hmacKeys.delete`  
`storage.hmacKeys.get`  
`storage.hmacKeys.list`  
`storage.hmacKeys.update`  
  
Cloud Storage  |  Now GA  |  `storage.hmacKeys.create`  
`storage.hmacKeys.delete`  
`storage.hmacKeys.get`  
`storage.hmacKeys.list`  
`storage.hmacKeys.update`  
  
  
## Cloud IAM changes as of 2019-06-28

Service | Change | Description  
---|---|---  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `pubsub.snapshots.seek`  
  
Firebase Crashlytics  |  Added  |  `firebasecrashlytics.config.get`  
`firebasecrashlytics.config.update`  
`firebasecrashlytics.data.get`  
`firebasecrashlytics.issues.get`  
`firebasecrashlytics.issues.list`  
`firebasecrashlytics.issues.update`  
`firebasecrashlytics.sessions.get`  
  
Firebase Crashlytics  |  Supported In Custom Roles  |  `firebasecrashlytics.config.get`  
`firebasecrashlytics.config.update`  
`firebasecrashlytics.data.get`  
`firebasecrashlytics.issues.get`  
`firebasecrashlytics.issues.list`  
`firebasecrashlytics.issues.update`  
`firebasecrashlytics.sessions.get`  
  
Memorystore for Redis  |  Added  |  `redis.instances.export`  
`redis.instances.import`  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `redis.instances.export`  
`redis.instances.import`  
  
  
## Cloud IAM changes as of 2019-06-21

Service | Change | Description  
---|---|---  
Migrate to Virtual Machines  |  Role Updated  |  The following permissions have been added to the role `roles/cloudmigration.inframanager` (Velostrata Manager): `compute.instances.updateShieldedInstanceConfig`  
  
Translation  |  Role Updated  |  The following permissions have been added to the role `roles/cloudtranslate.viewer` (Cloud Translation API Viewer): `cloudtranslate.operations.wait`  
  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkUser` (Compute Network User): `compute.vpnGateways.use`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.admin` (Firebase Admin): `cloudmessaging.messages.create`  
  
Firebase  |  Role Updated  |  The following permissions have been added to the role `roles/firebase.growthAdmin` (Firebase Grow Admin): `cloudmessaging.messages.create`  
  
Resource Manager  |  Role Updated  |  The following permissions have been added to the role `roles/resourcemanager.projectMover` (Project Mover): `resourcemanager.projects.move`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminEditor` (Security Center Admin Editor): `securitycenter.assets.group`  
`securitycenter.assets.list`  
`securitycenter.assets.listAssetPropertyNames`  
  
BigQuery  |  Added  |  `bigquery.connections.create`  
`bigquery.connections.delete`  
`bigquery.connections.get`  
`bigquery.connections.getIamPolicy`  
`bigquery.connections.list`  
`bigquery.connections.setIamPolicy`  
`bigquery.connections.update`  
`bigquery.connections.use`  
`bigquery.routines.create`  
`bigquery.routines.delete`  
`bigquery.routines.get`  
`bigquery.routines.list`  
`bigquery.routines.update`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.routines.create`  
`bigquery.routines.delete`  
`bigquery.routines.get`  
`bigquery.routines.list`  
`bigquery.routines.update`  
  
Translation  |  Supported In Custom Roles  |  `cloudtranslate.generalModels.batchPredict`  
`cloudtranslate.generalModels.get`  
`cloudtranslate.generalModels.predict`  
`cloudtranslate.glossaries.batchPredict`  
`cloudtranslate.glossaries.create`  
`cloudtranslate.glossaries.delete`  
`cloudtranslate.glossaries.get`  
`cloudtranslate.glossaries.list`  
`cloudtranslate.glossaries.predict`  
`cloudtranslate.languageDetectionModels.predict`  
`cloudtranslate.operations.cancel`  
`cloudtranslate.operations.delete`  
`cloudtranslate.operations.get`  
`cloudtranslate.operations.list`  
`cloudtranslate.operations.wait`  
  
Managed Service for Apache Airflow  |  Added  |  `composer.imageversions.list`  
  
Managed Service for Apache Airflow  |  Supported In Custom Roles  |  `composer.imageversions.list`  
  
Managed Service for Apache Airflow  |  Now GA  |  `composer.imageversions.list`  
  
Compute Engine  |  Added  |  `compute.vpnGateways.create`  
`compute.vpnGateways.delete`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnGateways.setLabels`  
`compute.vpnGateways.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.vpnGateways.create`  
`compute.vpnGateways.delete`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnGateways.setLabels`  
`compute.vpnGateways.use`  
  
Compute Engine  |  Now GA  |  `compute.vpnGateways.create`  
`compute.vpnGateways.delete`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnGateways.setLabels`  
`compute.vpnGateways.use`  
  
  
## Cloud IAM changes as of 2019-06-14

Service | Change | Description  
---|---|---  
Identity and Access Management  |  Now GA  |  The role `roles/iam.workloadIdentityUser` (Workload Identity User) is now GA.  
Cloud Run functions  |  Added  |  `cloudfunctions.functions.getIamPolicy`  
`cloudfunctions.functions.invoke`  
`cloudfunctions.functions.setIamPolicy`  
  
Cloud Run functions  |  Supported In Custom Roles  |  `cloudfunctions.functions.getIamPolicy`  
`cloudfunctions.functions.invoke`  
`cloudfunctions.functions.setIamPolicy`  
  
Compute Engine  |  Now GA  |  `compute.disks.addResourcePolicies`  
`compute.disks.removeResourcePolicies`  
`compute.resourcePolicies.create`  
`compute.resourcePolicies.delete`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.resourcePolicies.use`  
  
  
## Cloud IAM changes as of 2019-05-31

Service | Change | Description  
---|---|---  
Data Catalog  |  Role Updated  |  The following permissions have been added to the role `roles/datacatalog.admin` (Data Catalog Admin): `bigquery.datasets.updateTag`  
`bigquery.models.updateTag`  
`bigquery.tables.updateTag`  
`pubsub.topics.updateTag`  
  
Migrate to Virtual Machines  |  Added  |  `cloudmigration.velostrataendpoints.connect`  
  
Identity and Access Management  |  Available In Custom Roles  |  `iam.serviceAccounts.actAs`  
`iam.serviceAccounts.getAccessToken`  
`iam.serviceAccounts.implicitDelegation`  
`iam.serviceAccounts.signBlob`  
`iam.serviceAccounts.signJwt`  
  
  
## Cloud IAM changes as of 2019-05-24

Service | Change | Description  
---|---|---  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `managedidentities.domains.validateTrust`  
  
Recommendations  |  Supported In Custom Roles  |  `automlrecommendations.apiKeys.create`  
`automlrecommendations.apiKeys.delete`  
`automlrecommendations.apiKeys.list`  
`automlrecommendations.catalogItems.create`  
`automlrecommendations.catalogItems.delete`  
`automlrecommendations.catalogItems.get`  
`automlrecommendations.catalogItems.list`  
`automlrecommendations.catalogItems.update`  
`automlrecommendations.events.list`  
`automlrecommendations.events.purge`  
  
BigQuery  |  Added  |  `bigquery.datasets.updateTag`  
`bigquery.models.updateTag`  
`bigquery.tables.updateTag`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.datasets.updateTag`  
`bigquery.models.updateTag`  
`bigquery.tables.updateTag`  
  
Data Catalog  |  Added  |  `datacatalog.tagTemplates.create`  
`datacatalog.tagTemplates.delete`  
`datacatalog.tagTemplates.get`  
`datacatalog.tagTemplates.getIamPolicy`  
`datacatalog.tagTemplates.getTag`  
`datacatalog.tagTemplates.setIamPolicy`  
`datacatalog.tagTemplates.update`  
`datacatalog.tagTemplates.use`  
  
Data Catalog  |  Supported In Custom Roles  |  `datacatalog.tagTemplates.create`  
`datacatalog.tagTemplates.delete`  
`datacatalog.tagTemplates.get`  
`datacatalog.tagTemplates.getIamPolicy`  
`datacatalog.tagTemplates.getTag`  
`datacatalog.tagTemplates.setIamPolicy`  
`datacatalog.tagTemplates.update`  
`datacatalog.tagTemplates.use`  
  
Filestore  |  Added  |  `file.snapshots.update`  
  
Filestore  |  Supported In Custom Roles  |  `file.snapshots.update`  
  
Pub/Sub  |  Added  |  `pubsub.topics.updateTag`  
  
Pub/Sub  |  Supported In Custom Roles  |  `pubsub.topics.updateTag`  
  
  
## IAM changes as of 2019-05-17

Service | Change | Description  
---|---|---  
Dialogflow  |  Added  |  `dialogflow.agents.create`  
`dialogflow.agents.delete`  
  
Dialogflow  |  Supported In Custom Roles  |  `dialogflow.agents.create`  
`dialogflow.agents.delete`  
  
Dialogflow  |  Now GA  |  `dialogflow.agents.create`  
`dialogflow.agents.delete`  
  
  
## Cloud IAM changes as of 2019-05-10

Service | Change | Description  
---|---|---  
Identity and Access Management  |  Now GA  |  The role `roles/iam.securityAdmin` (Security Admin) is now GA.  
Cloud IoT  |  Added  |  `cloudiot.devices.bindGateway`  
`cloudiot.devices.sendCommand`  
`cloudiot.devices.unbindGateway`  
  
Cloud IoT  |  Supported In Custom Roles  |  `cloudiot.devices.bindGateway`  
`cloudiot.devices.sendCommand`  
`cloudiot.devices.unbindGateway`  
  
Cloud IoT  |  Now GA  |  `cloudiot.devices.bindGateway`  
`cloudiot.devices.sendCommand`  
`cloudiot.devices.unbindGateway`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.healthChecks.create`  
`compute.healthChecks.delete`  
`compute.healthChecks.get`  
`compute.healthChecks.list`  
`compute.healthChecks.update`  
`compute.healthChecks.use`  
`compute.healthChecks.useReadOnly`  
`compute.instanceGroups.use`  
  
Cloud Healthcare API  |  Added  |  `healthcare.fhirResources.purge`  
  
Managed Service for Microsoft Active Directory  |  Added  |  `managedidentities.domains.attachTrust`  
`managedidentities.domains.create`  
`managedidentities.domains.delete`  
`managedidentities.domains.detachTrust`  
`managedidentities.domains.get`  
`managedidentities.domains.getIamPolicy`  
`managedidentities.domains.list`  
`managedidentities.domains.reconfigureTrust`  
`managedidentities.domains.resetpassword`  
`managedidentities.domains.setIamPolicy`  
`managedidentities.domains.update`  
`managedidentities.domains.validateTrust`  
`managedidentities.locations.get`  
`managedidentities.locations.list`  
`managedidentities.operations.cancel`  
`managedidentities.operations.delete`  
`managedidentities.operations.get`  
`managedidentities.operations.list`  
  
Managed Service for Microsoft Active Directory  |  Supported In Custom Roles  |  `managedidentities.domains.attachTrust`  
`managedidentities.domains.create`  
`managedidentities.domains.delete`  
`managedidentities.domains.detachTrust`  
`managedidentities.domains.get`  
`managedidentities.domains.getIamPolicy`  
`managedidentities.domains.list`  
`managedidentities.domains.reconfigureTrust`  
`managedidentities.domains.resetpassword`  
`managedidentities.domains.setIamPolicy`  
`managedidentities.domains.update`  
`managedidentities.domains.validateTrust`  
`managedidentities.locations.get`  
`managedidentities.locations.list`  
`managedidentities.operations.cancel`  
`managedidentities.operations.delete`  
`managedidentities.operations.get`  
`managedidentities.operations.list`  
  
  
## Cloud IAM changes as of 2019-05-03

Service | Change | Description  
---|---|---  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.admin` (Security Center Admin) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.adminEditor` (Security Center Admin Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.adminViewer` (Security Center Admin Viewer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.assetsDiscoveryRunner` (Security Center Assets Discovery Runner) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.assetSecurityMarksWriter` (Security Center Asset Security Marks Writer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.assetsViewer` (Security Center Assets Viewer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.findingSecurityMarksWriter` (Security Center Finding Security Marks Writer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.findingsEditor` (Security Center Findings Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.findingsStateSetter` (Security Center Findings State Setter) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.findingsViewer` (Security Center Findings Viewer) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.sourcesAdmin` (Security Center Sources Admin) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.sourcesEditor` (Security Center Sources Editor) is now GA.  
Security Command Center  |  Now GA  |  The role `roles/securitycenter.sourcesViewer` (Security Center Sources Viewer) is now GA.  
Recommendations  |  Added  |  `automlrecommendations.apiKeys.create`  
`automlrecommendations.apiKeys.delete`  
`automlrecommendations.apiKeys.get`  
`automlrecommendations.apiKeys.list`  
`automlrecommendations.catalogItems.create`  
`automlrecommendations.catalogItems.delete`  
`automlrecommendations.catalogItems.get`  
`automlrecommendations.catalogItems.list`  
`automlrecommendations.catalogItems.update`  
`automlrecommendations.catalogs.get`  
`automlrecommendations.catalogs.getStats`  
`automlrecommendations.catalogs.list`  
`automlrecommendations.eventStores.get`  
`automlrecommendations.eventStores.getStats`  
`automlrecommendations.eventStores.list`  
`automlrecommendations.events.create`  
`automlrecommendations.events.delete`  
`automlrecommendations.events.get`  
`automlrecommendations.events.list`  
`automlrecommendations.events.purge`  
`automlrecommendations.events.update`  
`automlrecommendations.placements.get`  
`automlrecommendations.placements.getStats`  
`automlrecommendations.placements.list`  
`automlrecommendations.recommendations.get`  
`automlrecommendations.recommendations.list`  
  
BigQuery  |  Added  |  `bigquery.models.create`  
`bigquery.models.delete`  
`bigquery.models.getData`  
`bigquery.models.getMetadata`  
`bigquery.models.list`  
`bigquery.models.updateData`  
`bigquery.models.updateMetadata`  
  
Firebase Cloud Messaging  |  Added  |  `cloudmessaging.messages.create`  
  
Firebase Cloud Messaging  |  Supported In Custom Roles  |  `cloudmessaging.messages.create`  
  
Firebase Cloud Messaging  |  Now GA  |  `cloudmessaging.messages.create`  
  
Security Command Center  |  Now GA  |  `securitycenter.assets.group`  
`securitycenter.assets.list`  
`securitycenter.assets.listAssetPropertyNames`  
`securitycenter.assets.runDiscovery`  
`securitycenter.assetsecuritymarks.update`  
`securitycenter.findings.group`  
`securitycenter.findings.list`  
`securitycenter.findings.listFindingPropertyNames`  
`securitycenter.findings.setState`  
`securitycenter.findings.update`  
`securitycenter.findingsecuritymarks.update`  
`securitycenter.organizationsettings.get`  
`securitycenter.organizationsettings.update`  
`securitycenter.sources.get`  
`securitycenter.sources.getIamPolicy`  
`securitycenter.sources.list`  
`securitycenter.sources.setIamPolicy`  
`securitycenter.sources.update`  
  
  
## Cloud IAM changes as of 2019-04-19

Service | Change | Description  
---|---|---  
Basic Role  |  Role Updated  |  The following permissions have been removed from the role `roles/editor` (Editor): `firebasedynamiclinks.domains.delete`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.admin` (Security Center Admin): `securitycenter.findings.setState`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.adminEditor` (Security Center Admin Editor): `securitycenter.findings.setState`  
  
Security Command Center  |  Role Updated  |  The following permissions have been added to the role `roles/securitycenter.findingsEditor` (Security Center Findings Editor): `securitycenter.findings.setState`  
  
Access Approval  |  Added  |  `accessapproval.requests.approve`  
`accessapproval.requests.dismiss`  
`accessapproval.requests.get`  
`accessapproval.requests.list`  
`accessapproval.settings.get`  
`accessapproval.settings.update`  
  
Access Approval  |  Supported In Custom Roles  |  `accessapproval.requests.approve`  
`accessapproval.requests.dismiss`  
`accessapproval.requests.get`  
`accessapproval.requests.list`  
`accessapproval.settings.get`  
`accessapproval.settings.update`  
  
Bigtable  |  Added  |  `bigtable.locations.list`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.locations.list`  
  
Bigtable  |  Now GA  |  `bigtable.locations.list`  
  
Cloud Scheduler  |  Added  |  `cloudscheduler.locations.get`  
`cloudscheduler.locations.list`  
  
Compute Engine  |  Added  |  `compute.networkEndpointGroups.attachNetworkEndpoints`  
`compute.networkEndpointGroups.create`  
`compute.networkEndpointGroups.delete`  
`compute.networkEndpointGroups.detachNetworkEndpoints`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.getIamPolicy`  
`compute.networkEndpointGroups.list`  
`compute.networkEndpointGroups.setIamPolicy`  
`compute.networkEndpointGroups.use`  
`compute.reservations.create`  
`compute.reservations.delete`  
`compute.reservations.get`  
`compute.reservations.list`  
`compute.reservations.resize`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.networkEndpointGroups.attachNetworkEndpoints`  
`compute.networkEndpointGroups.create`  
`compute.networkEndpointGroups.delete`  
`compute.networkEndpointGroups.detachNetworkEndpoints`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.getIamPolicy`  
`compute.networkEndpointGroups.list`  
`compute.networkEndpointGroups.setIamPolicy`  
`compute.networkEndpointGroups.use`  
`compute.reservations.create`  
`compute.reservations.delete`  
`compute.reservations.get`  
`compute.reservations.list`  
`compute.reservations.resize`  
  
Compute Engine  |  Now GA  |  `compute.networkEndpointGroups.attachNetworkEndpoints`  
`compute.networkEndpointGroups.create`  
`compute.networkEndpointGroups.delete`  
`compute.networkEndpointGroups.detachNetworkEndpoints`  
`compute.networkEndpointGroups.get`  
`compute.networkEndpointGroups.getIamPolicy`  
`compute.networkEndpointGroups.list`  
`compute.networkEndpointGroups.setIamPolicy`  
`compute.networkEndpointGroups.use`  
  
Remote Build Execution  |  Added  |  `remotebuildexecution.actions.create`  
`remotebuildexecution.actions.get`  
`remotebuildexecution.actions.set`  
`remotebuildexecution.actions.update`  
`remotebuildexecution.blobs.create`  
`remotebuildexecution.blobs.get`  
`remotebuildexecution.botsessions.create`  
`remotebuildexecution.botsessions.update`  
`remotebuildexecution.instances.create`  
`remotebuildexecution.instances.delete`  
`remotebuildexecution.instances.get`  
`remotebuildexecution.instances.list`  
`remotebuildexecution.logstreams.create`  
`remotebuildexecution.logstreams.get`  
`remotebuildexecution.logstreams.update`  
`remotebuildexecution.workerpools.create`  
`remotebuildexecution.workerpools.delete`  
`remotebuildexecution.workerpools.get`  
`remotebuildexecution.workerpools.list`  
`remotebuildexecution.workerpools.update`  
  
Remote Build Execution  |  Supported In Custom Roles  |  `remotebuildexecution.actions.create`  
`remotebuildexecution.actions.get`  
`remotebuildexecution.actions.set`  
`remotebuildexecution.actions.update`  
`remotebuildexecution.blobs.create`  
`remotebuildexecution.blobs.get`  
`remotebuildexecution.botsessions.create`  
`remotebuildexecution.botsessions.update`  
`remotebuildexecution.instances.create`  
`remotebuildexecution.instances.delete`  
`remotebuildexecution.instances.get`  
`remotebuildexecution.instances.list`  
`remotebuildexecution.logstreams.create`  
`remotebuildexecution.logstreams.get`  
`remotebuildexecution.logstreams.update`  
`remotebuildexecution.workerpools.create`  
`remotebuildexecution.workerpools.delete`  
`remotebuildexecution.workerpools.get`  
`remotebuildexecution.workerpools.list`  
`remotebuildexecution.workerpools.update`  
  
Serverless VPC Access  |  Added  |  `vpcaccess.connectors.create`  
`vpcaccess.connectors.delete`  
`vpcaccess.connectors.get`  
`vpcaccess.connectors.list`  
`vpcaccess.connectors.use`  
`vpcaccess.locations.list`  
`vpcaccess.operations.get`  
`vpcaccess.operations.list`  
  
  
## Cloud IAM changes as of 2019-03-29

Service | Change | Description  
---|---|---  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.networkUser` (Compute Network User): `servicenetworking.services.get`  
  
Cloud Monitoring  |  Role Updated  |  The following permissions have been added to the role `roles/monitoring.admin` (Monitoring Admin): `serviceusage.services.enable`  
  
Cloud Monitoring  |  Role Updated  |  The following permissions have been added to the role `roles/monitoring.editor` (Monitoring Editor): `serviceusage.services.enable`  
  
Cloud Monitoring  |  Role Updated  |  The following permissions have been added to the role `roles/stackdriver.accounts.editor` (Stackdriver Accounts Editor): `serviceusage.services.enable`  
  
Cloud SQL  |  Added  |  `cloudsql.instances.addServerCa`  
`cloudsql.instances.listServerCas`  
`cloudsql.instances.rotateServerCa`  
  
Cloud SQL  |  Supported In Custom Roles  |  `cloudsql.instances.addServerCa`  
`cloudsql.instances.listServerCas`  
`cloudsql.instances.rotateServerCa`  
  
Cloud SQL  |  Now GA  |  `cloudsql.instances.addServerCa`  
`cloudsql.instances.listServerCas`  
`cloudsql.instances.rotateServerCa`  
  
Translation  |  Added  |  `cloudtranslate.generalModels.batchPredict`  
`cloudtranslate.generalModels.get`  
`cloudtranslate.generalModels.getIamPolicy`  
`cloudtranslate.generalModels.predict`  
`cloudtranslate.generalModels.setIamPolicy`  
`cloudtranslate.glossaries.batchPredict`  
`cloudtranslate.glossaries.create`  
`cloudtranslate.glossaries.delete`  
`cloudtranslate.glossaries.get`  
`cloudtranslate.glossaries.getIamPolicy`  
`cloudtranslate.glossaries.list`  
`cloudtranslate.glossaries.predict`  
`cloudtranslate.glossaries.setIamPolicy`  
`cloudtranslate.languageDetectionModels.getIamPolicy`  
`cloudtranslate.languageDetectionModels.predict`  
`cloudtranslate.languageDetectionModels.setIamPolicy`  
`cloudtranslate.locations.get`  
`cloudtranslate.locations.getIamPolicy`  
`cloudtranslate.locations.list`  
`cloudtranslate.locations.setIamPolicy`  
`cloudtranslate.operations.cancel`  
`cloudtranslate.operations.delete`  
`cloudtranslate.operations.get`  
`cloudtranslate.operations.getIamPolicy`  
`cloudtranslate.operations.list`  
`cloudtranslate.operations.setIamPolicy`  
`cloudtranslate.operations.wait`  
  
Cloud DNS  |  Added  |  `dns.networks.targetWithPeeringZone`  
  
Cloud DNS  |  Supported In Custom Roles  |  `dns.networks.targetWithPeeringZone`  
  
Event Threat Detection  |  Added  |  `threatdetection.detectorSettings.clear`  
`threatdetection.detectorSettings.get`  
`threatdetection.detectorSettings.update`  
`threatdetection.sinkSettings.get`  
`threatdetection.sinkSettings.update`  
`threatdetection.sourceSettings.get`  
`threatdetection.sourceSettings.update`  
  
  
## Cloud IAM changes as of 2019-03-22

Service | Change | Description  
---|---|---  
Talent Solution  |  Now GA  |  The role `roles/cloudjobdiscovery.admin` (Admin) is now GA.  
Talent Solution  |  Now GA  |  The role `roles/cloudjobdiscovery.jobsEditor` (Job Editor) is now GA.  
Talent Solution  |  Now GA  |  The role `roles/cloudjobdiscovery.jobsViewer` (Job Viewer) is now GA.  
Talent Solution  |  Now GA  |  The role `roles/cloudjobdiscovery.profilesEditor` (Profile Editor) is now GA.  
Talent Solution  |  Now GA  |  The role `roles/cloudjobdiscovery.profilesViewer` (Profile Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `file.instances.restore`  
`healthcare.datasets.deidentify`  
  
Filestore  |  Role Updated  |  The following permissions have been added to the role `roles/file.editor` (Cloud Filestore Editor): `file.instances.restore`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `file.instances.restore`  
`healthcare.datasets.deidentify`  
  
Talent Solution  |  Now GA  |  `cloudjobdiscovery.companies.create`  
`cloudjobdiscovery.companies.delete`  
`cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.companies.update`  
`cloudjobdiscovery.events.create`  
`cloudjobdiscovery.jobs.create`  
`cloudjobdiscovery.jobs.delete`  
`cloudjobdiscovery.jobs.get`  
`cloudjobdiscovery.jobs.search`  
`cloudjobdiscovery.jobs.update`  
`cloudjobdiscovery.profiles.create`  
`cloudjobdiscovery.profiles.delete`  
`cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
`cloudjobdiscovery.profiles.update`  
`cloudjobdiscovery.tenants.create`  
`cloudjobdiscovery.tenants.delete`  
`cloudjobdiscovery.tenants.get`  
`cloudjobdiscovery.tenants.update`  
`cloudjobdiscovery.tools.access`  
  
Compute Engine  |  Added  |  `compute.instances.getShieldedInstanceIdentity`  
`compute.instances.getShieldedVmIdentity`  
`compute.instances.setShieldedInstanceIntegrityPolicy`  
`compute.instances.updateShieldedInstanceConfig`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.getShieldedInstanceIdentity`  
`compute.instances.getShieldedVmIdentity`  
`compute.instances.setShieldedInstanceIntegrityPolicy`  
`compute.instances.updateShieldedInstanceConfig`  
  
Compute Engine  |  Now GA  |  `compute.instances.getShieldedInstanceIdentity`  
`compute.instances.getShieldedVmIdentity`  
`compute.instances.setShieldedInstanceIntegrityPolicy`  
`compute.instances.updateShieldedInstanceConfig`  
  
Filestore  |  Added  |  `file.instances.restore`  
  
Firebase Authentication  |  Added  |  `firebaseauth.configs.getHashConfig`  
  
Firebase Authentication  |  Supported In Custom Roles  |  `firebaseauth.configs.getHashConfig`  
  
Cloud Healthcare API  |  Added  |  `healthcare.datasets.create`  
`healthcare.datasets.deidentify`  
`healthcare.datasets.delete`  
`healthcare.datasets.get`  
`healthcare.datasets.getIamPolicy`  
`healthcare.datasets.list`  
`healthcare.datasets.setIamPolicy`  
`healthcare.datasets.update`  
`healthcare.dicomStores.create`  
`healthcare.dicomStores.delete`  
`healthcare.dicomStores.dicomWebDelete`  
`healthcare.dicomStores.dicomWebRead`  
`healthcare.dicomStores.dicomWebWrite`  
`healthcare.dicomStores.export`  
`healthcare.dicomStores.get`  
`healthcare.dicomStores.getIamPolicy`  
`healthcare.dicomStores.import`  
`healthcare.dicomStores.list`  
`healthcare.dicomStores.setIamPolicy`  
`healthcare.dicomStores.update`  
`healthcare.fhirResources.create`  
`healthcare.fhirResources.delete`  
`healthcare.fhirResources.get`  
`healthcare.fhirResources.patch`  
`healthcare.fhirResources.update`  
`healthcare.fhirSecurityLabels.getIamPolicy`  
`healthcare.fhirSecurityLabels.setIamPolicy`  
`healthcare.fhirStores.create`  
`healthcare.fhirStores.delete`  
`healthcare.fhirStores.export`  
`healthcare.fhirStores.get`  
`healthcare.fhirStores.getIamPolicy`  
`healthcare.fhirStores.import`  
`healthcare.fhirStores.list`  
`healthcare.fhirStores.searchResources`  
`healthcare.fhirStores.setIamPolicy`  
`healthcare.fhirStores.update`  
`healthcare.hl7V2Messages.create`  
`healthcare.hl7V2Messages.delete`  
`healthcare.hl7V2Messages.get`  
`healthcare.hl7V2Messages.ingest`  
`healthcare.hl7V2Messages.list`  
`healthcare.hl7V2Messages.update`  
`healthcare.hl7V2Stores.create`  
`healthcare.hl7V2Stores.delete`  
`healthcare.hl7V2Stores.get`  
`healthcare.hl7V2Stores.getIamPolicy`  
`healthcare.hl7V2Stores.list`  
`healthcare.hl7V2Stores.setIamPolicy`  
`healthcare.hl7V2Stores.update`  
`healthcare.operations.cancel`  
`healthcare.operations.get`  
`healthcare.operations.list`  
  
  
## Cloud IAM changes as of 2019-03-15

Service | Change | Description  
---|---|---  
Talent Solution  |  Role Updated  |  The following permissions have been added to the role `roles/cloudjobdiscovery.profilesEditor` (Profile Editor): `cloudjobdiscovery.tenants.create`  
`cloudjobdiscovery.tenants.delete`  
`cloudjobdiscovery.tenants.get`  
`cloudjobdiscovery.tenants.update`  
  
Talent Solution  |  Role Updated  |  The following permissions have been removed from the role `roles/cloudjobdiscovery.profilesEditor` (Profile Editor): `cloudjobdiscovery.companies.create`  
`cloudjobdiscovery.companies.delete`  
`cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.companies.update`  
  
Talent Solution  |  Role Updated  |  The following permissions have been added to the role `roles/cloudjobdiscovery.profilesViewer` (Profile Viewer): `cloudjobdiscovery.tenants.get`  
  
Talent Solution  |  Role Updated  |  The following permissions have been removed from the role `roles/cloudjobdiscovery.profilesViewer` (Profile Viewer): `cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `cloudjobdiscovery.tenants.create`  
`cloudjobdiscovery.tenants.delete`  
`cloudjobdiscovery.tenants.get`  
`cloudjobdiscovery.tenants.update`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `cloudjobdiscovery.tenants.create`  
`cloudjobdiscovery.tenants.delete`  
`cloudjobdiscovery.tenants.get`  
`cloudjobdiscovery.tenants.update`  
  
Storage Transfer Service  |  Now GA  |  The role `roles/storagetransfer.admin` (Storage Transfer Admin) is now GA.  
Storage Transfer Service  |  Now GA  |  The role `roles/storagetransfer.user` (Storage Transfer User) is now GA.  
Storage Transfer Service  |  Now GA  |  The role `roles/storagetransfer.viewer` (Storage Transfer Viewer) is now GA.  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `cloudjobdiscovery.tenants.get`  
  
Talent Solution  |  Added  |  `cloudjobdiscovery.tenants.create`  
`cloudjobdiscovery.tenants.delete`  
`cloudjobdiscovery.tenants.get`  
`cloudjobdiscovery.tenants.update`  
  
Cloud DNS  |  Now GA  |  `dns.networks.bindPrivateDNSZone`  
  
Cloud Run  |  Added  |  `run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.invoke`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.setIamPolicy`  
`run.services.update`  
  
Cloud Run  |  Not Supported In Custom Roles  |  `run.routes.invoke`  
  
Cloud Run  |  Supported In Custom Roles  |  `run.configurations.get`  
`run.configurations.list`  
`run.locations.list`  
`run.revisions.delete`  
`run.revisions.get`  
`run.revisions.list`  
`run.routes.get`  
`run.routes.list`  
`run.services.create`  
`run.services.delete`  
`run.services.get`  
`run.services.getIamPolicy`  
`run.services.list`  
`run.services.setIamPolicy`  
`run.services.update`  
  
Storage Transfer Service  |  Added  |  `storagetransfer.jobs.create`  
`storagetransfer.jobs.delete`  
`storagetransfer.jobs.get`  
`storagetransfer.jobs.list`  
`storagetransfer.jobs.update`  
`storagetransfer.operations.cancel`  
`storagetransfer.operations.get`  
`storagetransfer.operations.list`  
`storagetransfer.operations.pause`  
`storagetransfer.operations.resume`  
`storagetransfer.projects.getServiceAccount`  
  
Storage Transfer Service  |  Supported In Custom Roles  |  `storagetransfer.jobs.create`  
`storagetransfer.jobs.delete`  
`storagetransfer.jobs.get`  
`storagetransfer.jobs.list`  
`storagetransfer.jobs.update`  
`storagetransfer.operations.cancel`  
`storagetransfer.operations.get`  
`storagetransfer.operations.list`  
`storagetransfer.operations.pause`  
`storagetransfer.operations.resume`  
`storagetransfer.projects.getServiceAccount`  
  
Storage Transfer Service  |  Now GA  |  `storagetransfer.jobs.create`  
`storagetransfer.jobs.delete`  
`storagetransfer.jobs.get`  
`storagetransfer.jobs.list`  
`storagetransfer.jobs.update`  
`storagetransfer.operations.cancel`  
`storagetransfer.operations.get`  
`storagetransfer.operations.list`  
`storagetransfer.operations.pause`  
`storagetransfer.operations.resume`  
`storagetransfer.projects.getServiceAccount`  
  
  
## Cloud IAM changes as of 2019-03-07

Service | Change | Description  
---|---|---  
BigQuery  |  Role Added  |  The role `roles/bigquery.connectionAdmin` (BigQuery Connection Admin) has been added with the following permissions: `bigquery.connections.create`  
`bigquery.connections.delete`  
`bigquery.connections.get`  
`bigquery.connections.getIamPolicy`  
`bigquery.connections.list`  
`bigquery.connections.setIamPolicy`  
`bigquery.connections.update`  
`bigquery.connections.use`  
  
BigQuery  |  Role Added  |  The role `roles/bigquery.connectionUser` (BigQuery Connection User) has been added with the following permissions: `bigquery.connections.get`  
`bigquery.connections.getIamPolicy`  
`bigquery.connections.list`  
`bigquery.connections.use`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.admin` (Dialogflow API Admin): `dialogflow.agents.update`  
  
Dialogflow  |  Role Updated  |  The following permissions have been added to the role `roles/dialogflow.consoleAgentEditor` (Dialogflow Console Agent Editor): `dialogflow.agents.update`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `dialogflow.agents.update`  
`file.snapshots.create`  
`file.snapshots.delete`  
`file.snapshots.get`  
`file.snapshots.list`  
  
Filestore  |  Role Updated  |  The following permissions have been added to the role `roles/file.editor` (Cloud Filestore Editor): `file.snapshots.create`  
`file.snapshots.delete`  
`file.snapshots.get`  
`file.snapshots.list`  
  
Filestore  |  Role Updated  |  The following permissions have been added to the role `roles/file.viewer` (Cloud Filestore Viewer): `file.snapshots.get`  
`file.snapshots.list`  
  
Identity and Access Management  |  Now GA  |  The role `roles/iam.serviceAccountCreator` (Create Service Accounts) is now GA.  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.securityReviewer` (Security Reviewer): `file.snapshots.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `dialogflow.agents.update`  
`file.snapshots.create`  
`file.snapshots.delete`  
`file.snapshots.get`  
`file.snapshots.list`  
  
Service Usage  |  Role Updated  |  The following permissions have been added to the role `roles/serviceusage.apiKeysAdmin` (API Keys Admin): `serviceusage.operations.get`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `file.snapshots.get`  
`file.snapshots.list`  
  
AI Platform Data Labeling Service  |  Added  |  `datalabeling.annotateddatasets.delete`  
`datalabeling.annotateddatasets.get`  
`datalabeling.annotateddatasets.label`  
`datalabeling.annotateddatasets.list`  
`datalabeling.annotationspecsets.create`  
`datalabeling.annotationspecsets.delete`  
`datalabeling.annotationspecsets.get`  
`datalabeling.annotationspecsets.list`  
`datalabeling.dataitems.get`  
`datalabeling.dataitems.list`  
`datalabeling.datasets.create`  
`datalabeling.datasets.delete`  
`datalabeling.datasets.export`  
`datalabeling.datasets.get`  
`datalabeling.datasets.import`  
`datalabeling.datasets.list`  
`datalabeling.examples.get`  
`datalabeling.examples.list`  
`datalabeling.instructions.create`  
`datalabeling.instructions.delete`  
`datalabeling.instructions.get`  
`datalabeling.instructions.list`  
`datalabeling.operations.cancel`  
`datalabeling.operations.get`  
`datalabeling.operations.list`  
  
AI Platform Data Labeling Service  |  Supported In Custom Roles  |  `datalabeling.annotateddatasets.delete`  
`datalabeling.annotateddatasets.get`  
`datalabeling.annotateddatasets.label`  
`datalabeling.annotateddatasets.list`  
`datalabeling.annotationspecsets.create`  
`datalabeling.annotationspecsets.delete`  
`datalabeling.annotationspecsets.get`  
`datalabeling.annotationspecsets.list`  
`datalabeling.dataitems.get`  
`datalabeling.dataitems.list`  
`datalabeling.datasets.create`  
`datalabeling.datasets.delete`  
`datalabeling.datasets.export`  
`datalabeling.datasets.get`  
`datalabeling.datasets.import`  
`datalabeling.datasets.list`  
`datalabeling.examples.get`  
`datalabeling.examples.list`  
`datalabeling.instructions.create`  
`datalabeling.instructions.delete`  
`datalabeling.instructions.get`  
`datalabeling.instructions.list`  
`datalabeling.operations.cancel`  
`datalabeling.operations.get`  
`datalabeling.operations.list`  
  
Dialogflow  |  Added  |  `dialogflow.agents.update`  
  
Filestore  |  Added  |  `file.snapshots.create`  
`file.snapshots.delete`  
`file.snapshots.get`  
`file.snapshots.list`  
  
  
## Cloud IAM changes as of 2019-03-01

Service | Change | Description  
---|---|---  
Compute Engine  |  Role Updated  |  The following permissions have been added to the role `roles/compute.instanceAdmin.v1` (Compute Instance Admin (v1)): `compute.resourcePolicies.create`  
`compute.resourcePolicies.delete`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.resourcePolicies.use`  
  
Managed Service for Apache Spark  |  Role Added  |  The role `roles/dataproc.admin` (Dataproc Administrator) has been added with the following permissions: `compute.machineTypes.get`  
`compute.machineTypes.list`  
`compute.networks.get`  
`compute.networks.list`  
`compute.projects.get`  
`compute.regions.get`  
`compute.regions.list`  
`compute.zones.get`  
`compute.zones.list`  
`dataproc.autoscalingPolicies.create`  
`dataproc.autoscalingPolicies.delete`  
`dataproc.autoscalingPolicies.get`  
`dataproc.autoscalingPolicies.getIamPolicy`  
`dataproc.autoscalingPolicies.list`  
`dataproc.autoscalingPolicies.setIamPolicy`  
`dataproc.autoscalingPolicies.update`  
`dataproc.autoscalingPolicies.use`  
`dataproc.clusters.create`  
`dataproc.clusters.delete`  
`dataproc.clusters.get`  
`dataproc.clusters.getIamPolicy`  
`dataproc.clusters.list`  
`dataproc.clusters.setIamPolicy`  
`dataproc.clusters.update`  
`dataproc.clusters.use`  
`dataproc.jobs.cancel`  
`dataproc.jobs.create`  
`dataproc.jobs.delete`  
`dataproc.jobs.get`  
`dataproc.jobs.getIamPolicy`  
`dataproc.jobs.list`  
`dataproc.jobs.setIamPolicy`  
`dataproc.jobs.update`  
`dataproc.operations.cancel`  
`dataproc.operations.delete`  
`dataproc.operations.get`  
`dataproc.operations.getIamPolicy`  
`dataproc.operations.list`  
`dataproc.operations.setIamPolicy`  
`dataproc.workflowTemplates.create`  
`dataproc.workflowTemplates.delete`  
`dataproc.workflowTemplates.get`  
`dataproc.workflowTemplates.getIamPolicy`  
`dataproc.workflowTemplates.instantiate`  
`dataproc.workflowTemplates.instantiateInline`  
`dataproc.workflowTemplates.list`  
`dataproc.workflowTemplates.setIamPolicy`  
`dataproc.workflowTemplates.update`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `dataproc.clusters.getIamPolicy`  
`dataproc.jobs.getIamPolicy`  
`dataproc.operations.getIamPolicy`  
  
Identity and Access Management  |  Role Updated  |  The following permissions have been added to the role `roles/iam.serviceAccountDeleter` (Delete Service Accounts): `iam.serviceAccounts.get`  
`iam.serviceAccounts.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `dataproc.clusters.getIamPolicy`  
`dataproc.jobs.getIamPolicy`  
`dataproc.operations.getIamPolicy`  
  
AutoML  |  Added  |  `automl.columnSpecs.get`  
`automl.columnSpecs.list`  
`automl.columnSpecs.update`  
`automl.datasets.update`  
`automl.models.export`  
`automl.tableSpecs.get`  
`automl.tableSpecs.list`  
`automl.tableSpecs.update`  
  
AutoML  |  Supported In Custom Roles  |  `automl.columnSpecs.list`  
`automl.columnSpecs.update`  
`automl.datasets.update`  
`automl.models.deploy`  
`automl.models.export`  
`automl.models.undeploy`  
`automl.tableSpecs.get`  
`automl.tableSpecs.list`  
`automl.tableSpecs.update`  
  
Compute Engine  |  Added  |  `compute.disks.addResourcePolicies`  
`compute.disks.removeResourcePolicies`  
`compute.resourcePolicies.create`  
`compute.resourcePolicies.delete`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.resourcePolicies.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.disks.addResourcePolicies`  
`compute.disks.removeResourcePolicies`  
`compute.resourcePolicies.create`  
`compute.resourcePolicies.delete`  
`compute.resourcePolicies.get`  
`compute.resourcePolicies.list`  
`compute.resourcePolicies.use`  
  
  
## Cloud IAM changes as of 2019-02-15

Service | Change | Description  
---|---|---  
Access Context Manager  |  Now GA  |  The role `roles/accesscontextmanager.policyAdmin` (Access Context Manager Admin) is now GA.  
Access Context Manager  |  Now GA  |  The role `roles/accesscontextmanager.policyEditor` (Access Context Manager Editor) is now GA.  
Access Context Manager  |  Now GA  |  The role `roles/accesscontextmanager.policyReader` (Access Context Manager Reader) is now GA.  
Talent Solution  |  Role Added  |  The role `roles/cloudjobdiscovery.profilesEditor` (Profile Editor) has been added with the following permissions: `cloudjobdiscovery.companies.create`  
`cloudjobdiscovery.companies.delete`  
`cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.companies.update`  
`cloudjobdiscovery.events.create`  
`cloudjobdiscovery.events.delete`  
`cloudjobdiscovery.events.get`  
`cloudjobdiscovery.events.list`  
`cloudjobdiscovery.events.update`  
`cloudjobdiscovery.profiles.create`  
`cloudjobdiscovery.profiles.delete`  
`cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
`cloudjobdiscovery.profiles.update`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Talent Solution  |  Role Added  |  The role `roles/cloudjobdiscovery.profilesViewer` (Profile Viewer) has been added with the following permissions: `cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.events.get`  
`cloudjobdiscovery.events.list`  
`cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/editor` (Editor): `cloudjobdiscovery.profiles.create`  
`cloudjobdiscovery.profiles.delete`  
`cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
`cloudjobdiscovery.profiles.update`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/owner` (Owner): `cloudjobdiscovery.profiles.create`  
`cloudjobdiscovery.profiles.delete`  
`cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
`cloudjobdiscovery.profiles.update`  
  
Basic Role  |  Role Updated  |  The following permissions have been added to the role `roles/viewer` (Viewer): `cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
  
Cloud Monitoring  |  Role Updated  |  The following permissions have been added to the role `roles/stackdriver.accounts.editor` (Stackdriver Account Editor): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Cloud Monitoring  |  Role Updated  |  The following permissions have been added to the role `roles/stackdriver.accounts.viewer` (Stackdriver Account Viewer): `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
  
Access Context Manager  |  Supported In Custom Roles  |  `accesscontextmanager.accessLevels.create`  
`accesscontextmanager.accessLevels.delete`  
`accesscontextmanager.accessLevels.get`  
`accesscontextmanager.accessLevels.list`  
`accesscontextmanager.accessLevels.update`  
`accesscontextmanager.accessPolicies.create`  
`accesscontextmanager.accessPolicies.delete`  
`accesscontextmanager.accessPolicies.get`  
`accesscontextmanager.accessPolicies.getIamPolicy`  
`accesscontextmanager.accessPolicies.list`  
`accesscontextmanager.accessPolicies.setIamPolicy`  
`accesscontextmanager.accessPolicies.update`  
`accesscontextmanager.accessZones.create`  
`accesscontextmanager.accessZones.delete`  
`accesscontextmanager.accessZones.get`  
`accesscontextmanager.accessZones.list`  
`accesscontextmanager.accessZones.update`  
`accesscontextmanager.policies.create`  
`accesscontextmanager.policies.delete`  
`accesscontextmanager.policies.get`  
`accesscontextmanager.policies.getIamPolicy`  
`accesscontextmanager.policies.list`  
`accesscontextmanager.policies.setIamPolicy`  
`accesscontextmanager.policies.update`  
`accesscontextmanager.servicePerimeters.create`  
`accesscontextmanager.servicePerimeters.delete`  
`accesscontextmanager.servicePerimeters.get`  
`accesscontextmanager.servicePerimeters.list`  
`accesscontextmanager.servicePerimeters.update`  
  
Access Context Manager  |  Now GA  |  `accesscontextmanager.accessLevels.create`  
`accesscontextmanager.accessLevels.delete`  
`accesscontextmanager.accessLevels.get`  
`accesscontextmanager.accessLevels.list`  
`accesscontextmanager.accessLevels.update`  
`accesscontextmanager.accessPolicies.create`  
`accesscontextmanager.accessPolicies.delete`  
`accesscontextmanager.accessPolicies.get`  
`accesscontextmanager.accessPolicies.getIamPolicy`  
`accesscontextmanager.accessPolicies.list`  
`accesscontextmanager.accessPolicies.setIamPolicy`  
`accesscontextmanager.accessPolicies.update`  
`accesscontextmanager.accessZones.create`  
`accesscontextmanager.accessZones.delete`  
`accesscontextmanager.accessZones.get`  
`accesscontextmanager.accessZones.list`  
`accesscontextmanager.accessZones.update`  
`accesscontextmanager.policies.create`  
`accesscontextmanager.policies.delete`  
`accesscontextmanager.policies.get`  
`accesscontextmanager.policies.getIamPolicy`  
`accesscontextmanager.policies.list`  
`accesscontextmanager.policies.setIamPolicy`  
`accesscontextmanager.policies.update`  
`accesscontextmanager.servicePerimeters.create`  
`accesscontextmanager.servicePerimeters.delete`  
`accesscontextmanager.servicePerimeters.get`  
`accesscontextmanager.servicePerimeters.list`  
`accesscontextmanager.servicePerimeters.update`  
  
Talent Solution  |  Added  |  `cloudjobdiscovery.profiles.create`  
`cloudjobdiscovery.profiles.delete`  
`cloudjobdiscovery.profiles.get`  
`cloudjobdiscovery.profiles.search`  
`cloudjobdiscovery.profiles.update`  
  
  
## Cloud IAM changes as of 2019-02-08

Service | Change | Description  
---|---|---  
Security Command Center  |  Supported In Custom Roles  |  `securitycenter.assets.group`  
`securitycenter.assets.list`  
`securitycenter.assets.listAssetPropertyNames`  
`securitycenter.assets.runDiscovery`  
`securitycenter.assetsecuritymarks.update`  
`securitycenter.findings.group`  
`securitycenter.findings.list`  
`securitycenter.findings.listFindingPropertyNames`  
`securitycenter.findings.setState`  
`securitycenter.findings.update`  
`securitycenter.findingsecuritymarks.update`  
`securitycenter.organizationsettings.get`  
`securitycenter.organizationsettings.update`  
`securitycenter.sources.get`  
`securitycenter.sources.getIamPolicy`  
`securitycenter.sources.list`  
`securitycenter.sources.setIamPolicy`  
`securitycenter.sources.update`  
  
  
## Cloud IAM changes as of 2019-02-01

Service | Change | Description  
---|---|---  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.admin` (Dialogflow API Admin) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.client` (Dialogflow API Client) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.consoleAgentEditor` (Dialogflow Console Agent Editor) is now GA.  
Dialogflow  |  Now GA  |  The role `roles/dialogflow.reader` (Dialogflow API Reader) is now GA.  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.exportIamPolicy`  
`cloudasset.assets.exportResource`  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `cloudasset.assets.exportIamPolicy`  
`cloudasset.assets.exportResource`  
  
Cloud Asset Inventory  |  Now GA  |  `cloudasset.assets.exportIamPolicy`  
`cloudasset.assets.exportResource`  
  
Dialogflow  |  Supported In Custom Roles  |  `dialogflow.agents.search`  
`dialogflow.agents.train`  
  
Dialogflow  |  Now GA  |  `dialogflow.agents.export`  
`dialogflow.agents.get`  
`dialogflow.agents.import`  
`dialogflow.agents.restore`  
`dialogflow.agents.search`  
`dialogflow.agents.train`  
`dialogflow.contexts.create`  
`dialogflow.contexts.delete`  
`dialogflow.contexts.get`  
`dialogflow.contexts.list`  
`dialogflow.contexts.update`  
`dialogflow.entityTypes.create`  
`dialogflow.entityTypes.createEntity`  
`dialogflow.entityTypes.delete`  
`dialogflow.entityTypes.deleteEntity`  
`dialogflow.entityTypes.get`  
`dialogflow.entityTypes.list`  
`dialogflow.entityTypes.update`  
`dialogflow.entityTypes.updateEntity`  
`dialogflow.intents.create`  
`dialogflow.intents.delete`  
`dialogflow.intents.get`  
`dialogflow.intents.list`  
`dialogflow.intents.update`  
`dialogflow.operations.get`  
`dialogflow.sessionEntityTypes.create`  
`dialogflow.sessionEntityTypes.delete`  
`dialogflow.sessionEntityTypes.get`  
`dialogflow.sessionEntityTypes.list`  
`dialogflow.sessionEntityTypes.update`  
`dialogflow.sessions.detectIntent`  
`dialogflow.sessions.streamingDetectIntent`  
  
  
## Cloud IAM changes as of 2019-01-25

Service | Change | Description  
---|---|---  
Compute Engine  |  Added  |  `compute.instances.updateDisplayDevice`  
  
  
## Cloud IAM changes as of 2019-01-11

Service | Change | Description  
---|---|---  
Identity-Aware Proxy  |  Now GA  |  The role `roles/iap.admin` (IAP Policy Admin) is now GA.  
Identity-Aware Proxy  |  Supported In Custom Roles  |  `iap.web.getIamPolicy`  
`iap.web.setIamPolicy`  
`iap.webServiceVersions.accessViaIAP`  
`iap.webServiceVersions.getIamPolicy`  
`iap.webServiceVersions.setIamPolicy`  
`iap.webServices.getIamPolicy`  
`iap.webServices.setIamPolicy`  
`iap.webTypes.getIamPolicy`  
`iap.webTypes.setIamPolicy`  
  
  
## Cloud IAM changes as of 2018-12-21

Service | Change | Description  
---|---|---  
Cloud DNS  |  Added  |  `dns.networks.bindPrivateDNSZone`  
  
Cloud DNS  |  Supported In Custom Roles  |  `dns.networks.bindPrivateDNSZone`  
  
  
## Cloud IAM changes as of 2018-12-14

Service | Change | Description  
---|---|---  
Firebase Authentication  |  Added  |  `firebaseauth.configs.create`  
  
Firebase Authentication  |  Supported In Custom Roles  |  `firebaseauth.configs.create`  
  
  
## Cloud IAM changes as of 2018-12-07

Service | Change | Description  
---|---|---  
BigQuery  |  Added  |  `bigquery.readsessions.create`  
  
BigQuery  |  Supported In Custom Roles  |  `bigquery.readsessions.create`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.backendConfigs.create`  
`container.backendConfigs.delete`  
`container.backendConfigs.get`  
`container.backendConfigs.list`  
`container.backendConfigs.update`  
`container.tokenReviews.create`  
  
Google Kubernetes Engine  |  Now GA  |  `container.backendConfigs.create`  
`container.backendConfigs.delete`  
`container.backendConfigs.get`  
`container.backendConfigs.list`  
`container.backendConfigs.update`  
`container.tokenReviews.create`  
  
  
## Cloud IAM changes as of 2018-11-30

Service | Change | Description  
---|---|---  
Cloud Asset Inventory  |  Now GA  |  The role `roles/cloudasset.viewer` (Cloud Asset Viewer) is now GA.  
Cloud Asset Inventory  |  Now GA  |  `cloudasset.assets.exportAll`  
  
Compute Engine  |  Added  |  `compute.licenseCodes.getIamPolicy`  
`compute.licenseCodes.setIamPolicy`  
`compute.nodeGroups.getIamPolicy`  
`compute.nodeGroups.setIamPolicy`  
`compute.nodeTemplates.getIamPolicy`  
`compute.nodeTemplates.setIamPolicy`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.disks.getIamPolicy`  
`compute.disks.setIamPolicy`  
`compute.images.getIamPolicy`  
`compute.instances.getIamPolicy`  
`compute.instances.setIamPolicy`  
`compute.licenseCodes.getIamPolicy`  
`compute.licenseCodes.setIamPolicy`  
`compute.licenses.getIamPolicy`  
`compute.licenses.setIamPolicy`  
`compute.nodeGroups.getIamPolicy`  
`compute.nodeGroups.setIamPolicy`  
`compute.nodeTemplates.getIamPolicy`  
`compute.nodeTemplates.setIamPolicy`  
`compute.snapshots.getIamPolicy`  
`compute.snapshots.setIamPolicy`  
`compute.subnetworks.getIamPolicy`  
`compute.subnetworks.setIamPolicy`  
  
Compute Engine  |  Now GA  |  `compute.licenseCodes.getIamPolicy`  
`compute.licenseCodes.setIamPolicy`  
`compute.nodeGroups.getIamPolicy`  
`compute.nodeGroups.setIamPolicy`  
`compute.nodeTemplates.getIamPolicy`  
`compute.nodeTemplates.setIamPolicy`  
`compute.subnetworks.getIamPolicy`  
`compute.subnetworks.setIamPolicy`  
  
  
## Cloud IAM changes as of 2018-11-16

Service | Change | Description  
---|---|---  
AutoML  |  Added  |  `automl.locations.getIamPolicy`  
`automl.locations.setIamPolicy`  
  
AutoML  |  Supported In Custom Roles  |  `automl.locations.getIamPolicy`  
`automl.locations.setIamPolicy`  
  
Talent Solution  |  Added  |  `cloudjobdiscovery.events.create`  
`cloudjobdiscovery.events.delete`  
`cloudjobdiscovery.events.get`  
`cloudjobdiscovery.events.list`  
`cloudjobdiscovery.events.update`  
  
Compute Engine  |  Added  |  `compute.instanceTemplates.getIamPolicy`  
`compute.instanceTemplates.setIamPolicy`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instanceTemplates.getIamPolicy`  
`compute.instanceTemplates.setIamPolicy`  
  
Compute Engine  |  Now GA  |  `compute.instanceTemplates.getIamPolicy`  
`compute.instanceTemplates.setIamPolicy`  
  
Google Kubernetes Engine  |  Added  |  `container.backendConfigs.create`  
`container.backendConfigs.delete`  
`container.backendConfigs.get`  
`container.backendConfigs.list`  
`container.backendConfigs.update`  
`container.tokenReviews.create`  
  
  
## Cloud IAM changes as of 2018-11-09

Service | Change | Description  
---|---|---  
Google Analytics  |  Added  |  `firebaseanalytics.resources.googleAnalyticsEdit`  
`firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`  
  
Google Analytics  |  Supported In Custom Roles  |  `firebaseanalytics.resources.googleAnalyticsEdit`  
`firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`  
  
  
## Cloud IAM changes as of 2018-11-02

Service | Change | Description  
---|---|---  
Compute Engine  |  Now GA  |  `compute.globalAddresses.createInternal`  
`compute.globalAddresses.deleteInternal`  
  
Filestore  |  Supported In Custom Roles  |  `file.instances.create`  
`file.instances.delete`  
`file.instances.get`  
`file.instances.list`  
`file.instances.update`  
`file.locations.get`  
`file.locations.list`  
`file.operations.get`  
`file.operations.list`  
  
Cloud Monitoring  |  Added  |  `stackdriver.resourceMetadata.write`  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `stackdriver.resourceMetadata.write`  
  
  
## Cloud IAM changes as of 2018-10-26

Service | Change | Description  
---|---|---  
BigQuery  |  Now GA  |  The role `roles/bigquery.metadataViewer` (BigQuery Metadata Viewer) is now GA.  
Identity and Access Management  |  Now GA  |  The role `roles/iam.serviceAccountDeleter` (Delete Service Accounts) is now GA.  
Firebase Realtime Database  |  Added  |  `firebasedatabase.instances.create`  
`firebasedatabase.instances.list`  
  
Firebase Realtime Database  |  Supported In Custom Roles  |  `firebasedatabase.instances.create`  
`firebasedatabase.instances.list`  
  
Firebase Extensions  |  Added  |  `firebaseextensions.configs.create`  
`firebaseextensions.configs.delete`  
`firebaseextensions.configs.list`  
`firebaseextensions.configs.update`  
  
Firebase Extensions  |  Supported In Custom Roles  |  `firebaseextensions.configs.create`  
`firebaseextensions.configs.delete`  
`firebaseextensions.configs.list`  
`firebaseextensions.configs.update`  
  
  
## Cloud IAM changes as of 2018-10-19

Service | Change | Description  
---|---|---  
Google Cloud Support  |  Now GA  |  The role `roles/cloudsupport.admin` (Support Account Administrator) is now GA.  
Google Cloud Support  |  Now GA  |  The role `roles/cloudsupport.viewer` (Support Account Viewer) is now GA.  
Firebase Remote Config  |  Added  |  `cloudconfig.configs.get`  
`cloudconfig.configs.update`  
  
Firebase Remote Config  |  Supported In Custom Roles  |  `cloudconfig.configs.get`  
`cloudconfig.configs.update`  
  
Google Cloud Support  |  Supported In Custom Roles  |  `cloudsupport.accounts.create`  
`cloudsupport.accounts.delete`  
`cloudsupport.accounts.get`  
`cloudsupport.accounts.getIamPolicy`  
`cloudsupport.accounts.getUserRoles`  
`cloudsupport.accounts.list`  
`cloudsupport.accounts.setIamPolicy`  
`cloudsupport.accounts.update`  
`cloudsupport.accounts.updateUserRoles`  
`cloudsupport.operations.get`  
  
Google Cloud Support  |  Now GA  |  `cloudsupport.accounts.create`  
`cloudsupport.accounts.delete`  
`cloudsupport.accounts.get`  
`cloudsupport.accounts.getIamPolicy`  
`cloudsupport.accounts.getUserRoles`  
`cloudsupport.accounts.list`  
`cloudsupport.accounts.setIamPolicy`  
`cloudsupport.accounts.update`  
`cloudsupport.accounts.updateUserRoles`  
`cloudsupport.operations.get`  
  
Compute Engine  |  Added  |  `compute.networks.updatePeering`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.networks.updatePeering`  
  
Firebase Crashlytics  |  Added  |  `firebasecrash.issues.update`  
`firebasecrash.reports.get`  
  
Firebase Crashlytics  |  Supported In Custom Roles  |  `firebasecrash.issues.update`  
`firebasecrash.reports.get`  
  
Firebase Dynamic Links  |  Added  |  `firebasedynamiclinks.destinations.list`  
`firebasedynamiclinks.destinations.update`  
`firebasedynamiclinks.domains.create`  
`firebasedynamiclinks.domains.delete`  
`firebasedynamiclinks.domains.get`  
`firebasedynamiclinks.domains.list`  
`firebasedynamiclinks.domains.update`  
`firebasedynamiclinks.links.create`  
`firebasedynamiclinks.links.get`  
`firebasedynamiclinks.links.list`  
`firebasedynamiclinks.links.update`  
`firebasedynamiclinks.stats.get`  
  
Firebase Dynamic Links  |  Supported In Custom Roles  |  `firebasedynamiclinks.destinations.list`  
`firebasedynamiclinks.destinations.update`  
`firebasedynamiclinks.domains.create`  
`firebasedynamiclinks.domains.delete`  
`firebasedynamiclinks.domains.get`  
`firebasedynamiclinks.domains.list`  
`firebasedynamiclinks.domains.update`  
`firebasedynamiclinks.links.create`  
`firebasedynamiclinks.links.get`  
`firebasedynamiclinks.links.list`  
`firebasedynamiclinks.links.update`  
`firebasedynamiclinks.stats.get`  
  
Firebase In-App Messaging  |  Added  |  `firebaseinappmessaging.campaigns.create`  
`firebaseinappmessaging.campaigns.delete`  
`firebaseinappmessaging.campaigns.get`  
`firebaseinappmessaging.campaigns.list`  
`firebaseinappmessaging.campaigns.update`  
  
Firebase In-App Messaging  |  Supported In Custom Roles  |  `firebaseinappmessaging.campaigns.create`  
`firebaseinappmessaging.campaigns.delete`  
`firebaseinappmessaging.campaigns.get`  
`firebaseinappmessaging.campaigns.list`  
`firebaseinappmessaging.campaigns.update`  
  
Firebase Cloud Messaging  |  Added  |  `firebasenotifications.messages.create`  
`firebasenotifications.messages.delete`  
`firebasenotifications.messages.get`  
`firebasenotifications.messages.list`  
`firebasenotifications.messages.update`  
  
Firebase Cloud Messaging  |  Supported In Custom Roles  |  `firebasenotifications.messages.create`  
`firebasenotifications.messages.delete`  
`firebasenotifications.messages.get`  
`firebasenotifications.messages.list`  
`firebasenotifications.messages.update`  
  
Firebase Performance Monitoring  |  Added  |  `firebaseperformance.config.create`  
`firebaseperformance.config.delete`  
`firebaseperformance.config.update`  
`firebaseperformance.data.get`  
  
Firebase Performance Monitoring  |  Supported In Custom Roles  |  `firebaseperformance.config.create`  
`firebaseperformance.config.delete`  
`firebaseperformance.config.update`  
`firebaseperformance.data.get`  
  
Firebase Predictions  |  Added  |  `firebasepredictions.predictions.create`  
`firebasepredictions.predictions.delete`  
`firebasepredictions.predictions.list`  
`firebasepredictions.predictions.update`  
  
Firebase Predictions  |  Supported In Custom Roles  |  `firebasepredictions.predictions.create`  
`firebasepredictions.predictions.delete`  
`firebasepredictions.predictions.list`  
`firebasepredictions.predictions.update`  
  
Security Command Center  |  Added  |  `securitycenter.assets.get`  
`securitycenter.assets.getFieldNames`  
`securitycenter.assets.group`  
`securitycenter.assets.list`  
`securitycenter.assets.listAssetPropertyNames`  
`securitycenter.assets.runDiscovery`  
`securitycenter.assets.triggerDiscovery`  
`securitycenter.assets.update`  
`securitycenter.assetsecuritymarks.update`  
`securitycenter.configs.get`  
`securitycenter.configs.getIamPolicy`  
`securitycenter.configs.setIamPolicy`  
`securitycenter.configs.update`  
`securitycenter.findings.group`  
`securitycenter.findings.list`  
`securitycenter.findings.listFindingPropertyNames`  
`securitycenter.findings.setState`  
`securitycenter.findings.update`  
`securitycenter.findingsecuritymarks.update`  
`securitycenter.organizationsettings.get`  
`securitycenter.organizationsettings.update`  
`securitycenter.scans.get`  
`securitycenter.scans.list`  
`securitycenter.sources.get`  
`securitycenter.sources.getIamPolicy`  
`securitycenter.sources.list`  
`securitycenter.sources.setIamPolicy`  
`securitycenter.sources.update`  
  
Service Consumer Management  |  Added  |  `serviceconsumermanagement.tenancyu.addResource`  
`serviceconsumermanagement.tenancyu.create`  
`serviceconsumermanagement.tenancyu.delete`  
`serviceconsumermanagement.tenancyu.list`  
`serviceconsumermanagement.tenancyu.removeResource`  
  
Service Consumer Management  |  Supported In Custom Roles  |  `serviceconsumermanagement.tenancyu.addResource`  
`serviceconsumermanagement.tenancyu.create`  
`serviceconsumermanagement.tenancyu.delete`  
`serviceconsumermanagement.tenancyu.list`  
`serviceconsumermanagement.tenancyu.removeResource`  
  
  
## Cloud IAM changes as of 2018-10-12

Service | Change | Description  
---|---|---  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.admin` (DLP Administrator) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.analyzeRiskTemplatesEditor` (DLP Analyze Risk Templates Editor) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.analyzeRiskTemplatesReader` (DLP Analyze Risk Templates Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.deidentifyTemplatesEditor` (DLP De-identify Templates Editor) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.deidentifyTemplatesReader` (DLP De-identify Templates Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.inspectTemplatesEditor` (DLP Inspect Templates Editor) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.inspectTemplatesReader` (DLP Inspect Templates Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.jobsEditor` (DLP Jobs Editor) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.jobsReader` (DLP Jobs Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.jobTriggersEditor` (DLP Job Triggers Editor) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.jobTriggersReader` (DLP Job Triggers Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.reader` (DLP Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.storedInfoTypesEditor` (DLP Stored InfoTypes Editor) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.storedInfoTypesReader` (DLP Stored InfoTypes Reader) is now GA.  
Sensitive Data Protection  |  Now GA  |  The role `roles/dlp.user` (DLP User) is now GA.  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.certificateSigningRequests.approve`  
`container.clusterRoles.bind`  
`container.deployments.rollback`  
`container.nodes.proxy`  
`container.pods.attach`  
`container.pods.evict`  
`container.pods.exec`  
`container.pods.getLogs`  
`container.pods.portForward`  
`container.pods.proxy`  
`container.roles.bind`  
`container.services.proxy`  
`container.thirdPartyObjects.create`  
`container.thirdPartyObjects.delete`  
`container.thirdPartyObjects.get`  
`container.thirdPartyObjects.list`  
`container.thirdPartyObjects.update`  
  
Sensitive Data Protection  |  Supported In Custom Roles  |  `dlp.analyzeRiskTemplates.create`  
`dlp.analyzeRiskTemplates.delete`  
`dlp.analyzeRiskTemplates.get`  
`dlp.analyzeRiskTemplates.list`  
`dlp.analyzeRiskTemplates.update`  
`dlp.deidentifyTemplates.create`  
`dlp.deidentifyTemplates.delete`  
`dlp.deidentifyTemplates.get`  
`dlp.deidentifyTemplates.list`  
`dlp.deidentifyTemplates.update`  
`dlp.inspectTemplates.create`  
`dlp.inspectTemplates.delete`  
`dlp.inspectTemplates.get`  
`dlp.inspectTemplates.list`  
`dlp.inspectTemplates.update`  
`dlp.jobTriggers.create`  
`dlp.jobTriggers.delete`  
`dlp.jobTriggers.get`  
`dlp.jobTriggers.list`  
`dlp.jobTriggers.update`  
`dlp.jobs.cancel`  
`dlp.jobs.create`  
`dlp.jobs.delete`  
`dlp.jobs.get`  
`dlp.jobs.list`  
`dlp.kms.encrypt`  
  
Sensitive Data Protection  |  Now GA  |  `dlp.analyzeRiskTemplates.create`  
`dlp.analyzeRiskTemplates.delete`  
`dlp.analyzeRiskTemplates.get`  
`dlp.analyzeRiskTemplates.list`  
`dlp.analyzeRiskTemplates.update`  
`dlp.deidentifyTemplates.create`  
`dlp.deidentifyTemplates.delete`  
`dlp.deidentifyTemplates.get`  
`dlp.deidentifyTemplates.list`  
`dlp.deidentifyTemplates.update`  
`dlp.inspectTemplates.create`  
`dlp.inspectTemplates.delete`  
`dlp.inspectTemplates.get`  
`dlp.inspectTemplates.list`  
`dlp.inspectTemplates.update`  
`dlp.jobTriggers.create`  
`dlp.jobTriggers.delete`  
`dlp.jobTriggers.get`  
`dlp.jobTriggers.list`  
`dlp.jobTriggers.update`  
`dlp.jobs.cancel`  
`dlp.jobs.create`  
`dlp.jobs.delete`  
`dlp.jobs.get`  
`dlp.jobs.list`  
`dlp.kms.encrypt`  
`dlp.storedInfoTypes.create`  
`dlp.storedInfoTypes.delete`  
`dlp.storedInfoTypes.get`  
`dlp.storedInfoTypes.list`  
`dlp.storedInfoTypes.update`  
  
Cloud DNS  |  Supported In Custom Roles  |  `dns.dnsKeys.get`  
`dns.dnsKeys.list`  
`dns.managedZoneOperations.get`  
`dns.managedZoneOperations.list`  
`dns.managedZones.update`  
  
Firebase  |  Added  |  `firebase.billingPlans.get`  
`firebase.billingPlans.update`  
`firebase.clients.create`  
`firebase.clients.delete`  
`firebase.clients.get`  
`firebase.links.create`  
`firebase.links.delete`  
`firebase.links.list`  
`firebase.links.update`  
`firebase.projects.delete`  
`firebase.projects.get`  
`firebase.projects.update`  
  
Firebase  |  Supported In Custom Roles  |  `firebase.billingPlans.get`  
`firebase.billingPlans.update`  
`firebase.clients.create`  
`firebase.clients.delete`  
`firebase.clients.get`  
`firebase.links.create`  
`firebase.links.delete`  
`firebase.links.list`  
`firebase.links.update`  
`firebase.projects.delete`  
`firebase.projects.get`  
`firebase.projects.update`  
  
Firebase A/B Testing  |  Added  |  `firebaseabt.experimentresults.get`  
`firebaseabt.experiments.create`  
`firebaseabt.experiments.delete`  
`firebaseabt.experiments.get`  
`firebaseabt.experiments.list`  
`firebaseabt.experiments.update`  
`firebaseabt.projectmetadata.get`  
  
Firebase A/B Testing  |  Supported In Custom Roles  |  `firebaseabt.experimentresults.get`  
`firebaseabt.experiments.create`  
`firebaseabt.experiments.delete`  
`firebaseabt.experiments.get`  
`firebaseabt.experiments.list`  
`firebaseabt.experiments.update`  
`firebaseabt.projectmetadata.get`  
  
Firebase Authentication  |  Added  |  `firebaseauth.configs.get`  
`firebaseauth.configs.update`  
`firebaseauth.users.create`  
`firebaseauth.users.createSession`  
`firebaseauth.users.delete`  
`firebaseauth.users.get`  
`firebaseauth.users.sendEmail`  
`firebaseauth.users.update`  
  
Firebase Authentication  |  Supported In Custom Roles  |  `firebaseauth.configs.get`  
`firebaseauth.configs.update`  
`firebaseauth.users.create`  
`firebaseauth.users.createSession`  
`firebaseauth.users.delete`  
`firebaseauth.users.get`  
`firebaseauth.users.sendEmail`  
`firebaseauth.users.update`  
  
Firebase Realtime Database  |  Added  |  `firebasedatabase.instances.get`  
`firebasedatabase.instances.update`  
  
Firebase Realtime Database  |  Supported In Custom Roles  |  `firebasedatabase.instances.get`  
`firebasedatabase.instances.update`  
  
Firebase Hosting  |  Added  |  `firebasehosting.sites.create`  
`firebasehosting.sites.delete`  
`firebasehosting.sites.get`  
`firebasehosting.sites.list`  
`firebasehosting.sites.update`  
  
Firebase Hosting  |  Supported In Custom Roles  |  `firebasehosting.sites.create`  
`firebasehosting.sites.delete`  
`firebasehosting.sites.get`  
`firebasehosting.sites.list`  
`firebasehosting.sites.update`  
  
ML Kit for Firebase  |  Added  |  `firebaseml.compressionjobs.create`  
`firebaseml.compressionjobs.delete`  
`firebaseml.compressionjobs.get`  
`firebaseml.compressionjobs.list`  
`firebaseml.compressionjobs.start`  
`firebaseml.compressionjobs.update`  
`firebaseml.models.create`  
`firebaseml.models.delete`  
`firebaseml.models.get`  
`firebaseml.models.list`  
`firebaseml.modelversions.create`  
`firebaseml.modelversions.get`  
`firebaseml.modelversions.list`  
`firebaseml.modelversions.update`  
  
ML Kit for Firebase  |  Supported In Custom Roles  |  `firebaseml.compressionjobs.create`  
`firebaseml.compressionjobs.delete`  
`firebaseml.compressionjobs.get`  
`firebaseml.compressionjobs.list`  
`firebaseml.compressionjobs.start`  
`firebaseml.compressionjobs.update`  
`firebaseml.models.create`  
`firebaseml.models.delete`  
`firebaseml.models.get`  
`firebaseml.models.list`  
`firebaseml.modelversions.create`  
`firebaseml.modelversions.get`  
`firebaseml.modelversions.list`  
`firebaseml.modelversions.update`  
  
Firebase Security Rules  |  Added  |  `firebaserules.releases.create`  
`firebaserules.releases.delete`  
`firebaserules.releases.get`  
`firebaserules.releases.getExecutable`  
`firebaserules.releases.list`  
`firebaserules.releases.update`  
`firebaserules.rulesets.create`  
`firebaserules.rulesets.delete`  
`firebaserules.rulesets.get`  
`firebaserules.rulesets.list`  
`firebaserules.rulesets.test`  
  
Firebase Security Rules  |  Supported In Custom Roles  |  `firebaserules.releases.create`  
`firebaserules.releases.delete`  
`firebaserules.releases.get`  
`firebaserules.releases.getExecutable`  
`firebaserules.releases.list`  
`firebaserules.releases.update`  
`firebaserules.rulesets.create`  
`firebaserules.rulesets.delete`  
`firebaserules.rulesets.get`  
`firebaserules.rulesets.list`  
`firebaserules.rulesets.test`  
  
  
## Cloud IAM changes as of 2018-10-05

Service | Change | Description  
---|---|---  
Compute Engine  |  Added  |  `compute.instances.resume`  
`compute.instances.suspend`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.resume`  
`compute.instances.suspend`  
  
Compute Engine  |  Now GA  |  `compute.instances.resume`  
`compute.instances.suspend`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.apiServices.updateStatus`  
`container.certificateSigningRequests.updateStatus`  
`container.cronJobs.getStatus`  
`container.cronJobs.updateStatus`  
`container.customResourceDefinitions.updateStatus`  
`container.daemonSets.getStatus`  
`container.daemonSets.updateStatus`  
`container.deployments.getScale`  
`container.deployments.getStatus`  
`container.deployments.updateScale`  
`container.deployments.updateStatus`  
`container.horizontalPodAutoscalers.getStatus`  
`container.horizontalPodAutoscalers.updateStatus`  
`container.ingresses.getStatus`  
`container.ingresses.updateStatus`  
`container.jobs.getStatus`  
`container.jobs.updateStatus`  
`container.namespaces.getStatus`  
`container.namespaces.updateStatus`  
`container.nodes.getStatus`  
`container.nodes.updateStatus`  
`container.persistentVolumeClaims.getStatus`  
`container.persistentVolumeClaims.updateStatus`  
`container.persistentVolumes.getStatus`  
`container.persistentVolumes.updateStatus`  
`container.podDisruptionBudgets.getStatus`  
`container.podDisruptionBudgets.updateStatus`  
`container.pods.getStatus`  
`container.pods.updateStatus`  
`container.replicaSets.getScale`  
`container.replicaSets.getStatus`  
`container.replicaSets.updateScale`  
`container.replicaSets.updateStatus`  
`container.replicationControllers.getScale`  
`container.replicationControllers.getStatus`  
`container.replicationControllers.updateScale`  
`container.replicationControllers.updateStatus`  
`container.resourceQuotas.getStatus`  
`container.resourceQuotas.updateStatus`  
`container.services.getStatus`  
`container.services.updateStatus`  
`container.statefulSets.getScale`  
`container.statefulSets.getStatus`  
`container.statefulSets.updateScale`  
`container.statefulSets.updateStatus`  
  
Google Kubernetes Engine  |  Now GA  |  `container.cronJobs.getStatus`  
`container.daemonSets.getStatus`  
`container.deployments.getStatus`  
`container.horizontalPodAutoscalers.getStatus`  
`container.ingresses.getStatus`  
`container.jobs.getStatus`  
`container.namespaces.getStatus`  
`container.nodes.getStatus`  
`container.persistentVolumeClaims.getStatus`  
`container.persistentVolumes.getStatus`  
`container.podDisruptionBudgets.getStatus`  
`container.pods.getStatus`  
`container.replicaSets.getScale`  
`container.replicaSets.getStatus`  
`container.replicaSets.updateScale`  
`container.replicationControllers.getScale`  
`container.replicationControllers.getStatus`  
`container.replicationControllers.updateScale`  
`container.resourceQuotas.getStatus`  
`container.services.getStatus`  
`container.statefulSets.getStatus`  
  
  
## Cloud IAM changes as of 2018-09-21

Service | Change | Description  
---|---|---  
AutoML  |  Added  |  `automl.datasets.getIamPolicy`  
`automl.datasets.setIamPolicy`  
`automl.models.getIamPolicy`  
`automl.models.setIamPolicy`  
  
AutoML  |  Supported In Custom Roles  |  `automl.datasets.getIamPolicy`  
`automl.datasets.setIamPolicy`  
`automl.models.getIamPolicy`  
`automl.models.setIamPolicy`  
  
Cloud Asset Inventory  |  Added  |  `cloudasset.assets.exportAll`  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `cloudasset.assets.exportAll`  
  
Compute Engine  |  Added  |  `compute.licenses.delete`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.apiServices.create`  
`container.apiServices.delete`  
`container.apiServices.get`  
`container.apiServices.list`  
`container.apiServices.update`  
`container.bindings.create`  
`container.certificateSigningRequests.create`  
`container.certificateSigningRequests.delete`  
`container.certificateSigningRequests.get`  
`container.certificateSigningRequests.list`  
`container.certificateSigningRequests.update`  
`container.clusterRoleBindings.create`  
`container.clusterRoleBindings.delete`  
`container.clusterRoleBindings.get`  
`container.clusterRoleBindings.list`  
`container.clusterRoleBindings.update`  
`container.clusterRoles.create`  
`container.clusterRoles.delete`  
`container.clusterRoles.get`  
`container.clusterRoles.list`  
`container.clusterRoles.update`  
`container.componentStatuses.get`  
`container.componentStatuses.list`  
`container.configMaps.create`  
`container.configMaps.delete`  
`container.configMaps.get`  
`container.configMaps.list`  
`container.configMaps.update`  
`container.controllerRevisions.create`  
`container.controllerRevisions.delete`  
`container.controllerRevisions.get`  
`container.controllerRevisions.list`  
`container.controllerRevisions.update`  
`container.cronJobs.create`  
`container.cronJobs.delete`  
`container.cronJobs.get`  
`container.cronJobs.list`  
`container.cronJobs.update`  
`container.customResourceDefinitions.create`  
`container.customResourceDefinitions.delete`  
`container.customResourceDefinitions.get`  
`container.customResourceDefinitions.list`  
`container.customResourceDefinitions.update`  
`container.daemonSets.create`  
`container.daemonSets.delete`  
`container.daemonSets.get`  
`container.daemonSets.list`  
`container.daemonSets.update`  
`container.deployments.create`  
`container.deployments.delete`  
`container.deployments.get`  
`container.deployments.list`  
`container.deployments.update`  
`container.endpoints.create`  
`container.endpoints.delete`  
`container.endpoints.get`  
`container.endpoints.list`  
`container.endpoints.update`  
`container.events.create`  
`container.events.delete`  
`container.events.get`  
`container.events.list`  
`container.events.update`  
`container.horizontalPodAutoscalers.create`  
`container.horizontalPodAutoscalers.delete`  
`container.horizontalPodAutoscalers.get`  
`container.horizontalPodAutoscalers.list`  
`container.horizontalPodAutoscalers.update`  
`container.ingresses.create`  
`container.ingresses.delete`  
`container.ingresses.get`  
`container.ingresses.list`  
`container.ingresses.update`  
`container.jobs.create`  
`container.jobs.delete`  
`container.jobs.get`  
`container.jobs.list`  
`container.jobs.update`  
`container.limitRanges.create`  
`container.limitRanges.delete`  
`container.limitRanges.get`  
`container.limitRanges.list`  
`container.limitRanges.update`  
`container.localSubjectAccessReviews.create`  
`container.namespaces.create`  
`container.namespaces.delete`  
`container.namespaces.get`  
`container.namespaces.list`  
`container.namespaces.update`  
`container.networkPolicies.create`  
`container.networkPolicies.delete`  
`container.networkPolicies.get`  
`container.networkPolicies.list`  
`container.networkPolicies.update`  
`container.nodes.create`  
`container.nodes.delete`  
`container.nodes.get`  
`container.nodes.list`  
`container.nodes.update`  
`container.persistentVolumeClaims.create`  
`container.persistentVolumeClaims.delete`  
`container.persistentVolumeClaims.get`  
`container.persistentVolumeClaims.list`  
`container.persistentVolumeClaims.update`  
`container.persistentVolumes.create`  
`container.persistentVolumes.delete`  
`container.persistentVolumes.get`  
`container.persistentVolumes.list`  
`container.persistentVolumes.update`  
`container.podDisruptionBudgets.create`  
`container.podDisruptionBudgets.delete`  
`container.podDisruptionBudgets.get`  
`container.podDisruptionBudgets.list`  
`container.podDisruptionBudgets.update`  
`container.podSecurityPolicies.create`  
`container.podSecurityPolicies.delete`  
`container.podSecurityPolicies.get`  
`container.podSecurityPolicies.list`  
`container.podSecurityPolicies.update`  
`container.podTemplates.create`  
`container.podTemplates.delete`  
`container.podTemplates.get`  
`container.podTemplates.list`  
`container.podTemplates.update`  
`container.pods.create`  
`container.pods.delete`  
`container.pods.get`  
`container.pods.list`  
`container.pods.update`  
`container.replicaSets.create`  
`container.replicaSets.delete`  
`container.replicaSets.get`  
`container.replicaSets.list`  
`container.replicaSets.update`  
`container.replicationControllers.create`  
`container.replicationControllers.delete`  
`container.replicationControllers.get`  
`container.replicationControllers.list`  
`container.replicationControllers.update`  
`container.resourceQuotas.create`  
`container.resourceQuotas.delete`  
`container.resourceQuotas.get`  
`container.resourceQuotas.list`  
`container.resourceQuotas.update`  
`container.roleBindings.create`  
`container.roleBindings.delete`  
`container.roleBindings.get`  
`container.roleBindings.list`  
`container.roleBindings.update`  
`container.roles.create`  
`container.roles.delete`  
`container.roles.get`  
`container.roles.list`  
`container.roles.update`  
`container.secrets.create`  
`container.secrets.delete`  
`container.secrets.get`  
`container.secrets.list`  
`container.secrets.update`  
`container.selfSubjectAccessReviews.create`  
`container.serviceAccounts.create`  
`container.serviceAccounts.delete`  
`container.serviceAccounts.get`  
`container.serviceAccounts.list`  
`container.serviceAccounts.update`  
`container.services.create`  
`container.services.delete`  
`container.services.get`  
`container.services.list`  
`container.services.update`  
`container.statefulSets.create`  
`container.statefulSets.delete`  
`container.statefulSets.get`  
`container.statefulSets.list`  
`container.statefulSets.update`  
`container.storageClasses.create`  
`container.storageClasses.delete`  
`container.storageClasses.get`  
`container.storageClasses.list`  
`container.storageClasses.update`  
`container.subjectAccessReviews.create`  
  
  
## Cloud IAM changes as of 2018-09-07

Service | Change | Description  
---|---|---  
Memorystore for Redis  |  Supported In Custom Roles  |  `redis.operations.cancel`  
`redis.operations.delete`  
  
  
## Cloud IAM changes as of 2018-08-31

Service | Change | Description  
---|---|---  
Google Kubernetes Engine  |  Added  |  `container.cronJobs.getStatus`  
`container.daemonSets.getStatus`  
`container.deployments.getStatus`  
`container.horizontalPodAutoscalers.getStatus`  
`container.ingresses.getStatus`  
`container.jobs.getStatus`  
`container.namespaces.getStatus`  
`container.nodes.getStatus`  
`container.persistentVolumeClaims.getStatus`  
`container.persistentVolumes.getStatus`  
`container.podDisruptionBudgets.getStatus`  
`container.pods.getStatus`  
`container.replicaSets.getScale`  
`container.replicaSets.getStatus`  
`container.replicaSets.updateScale`  
`container.replicationControllers.getScale`  
`container.replicationControllers.getStatus`  
`container.replicationControllers.updateScale`  
`container.resourceQuotas.getStatus`  
`container.services.getStatus`  
`container.statefulSets.getStatus`  
  
Sensitive Data Protection  |  Added  |  `dlp.storedInfoTypes.create`  
`dlp.storedInfoTypes.delete`  
`dlp.storedInfoTypes.get`  
`dlp.storedInfoTypes.list`  
`dlp.storedInfoTypes.update`  
  
Sensitive Data Protection  |  Supported In Custom Roles  |  `dlp.storedInfoTypes.create`  
`dlp.storedInfoTypes.delete`  
`dlp.storedInfoTypes.get`  
`dlp.storedInfoTypes.list`  
`dlp.storedInfoTypes.update`  
  
Cloud Source Repositories  |  Added  |  `source.repos.getProjectConfig`  
`source.repos.updateProjectConfig`  
`source.repos.updateRepoConfig`  
  
Cloud Source Repositories  |  Supported In Custom Roles  |  `source.repos.getProjectConfig`  
`source.repos.updateProjectConfig`  
`source.repos.updateRepoConfig`  
  
Cloud Source Repositories  |  Now GA  |  `source.repos.getProjectConfig`  
`source.repos.updateProjectConfig`  
`source.repos.updateRepoConfig`  
  
  
## Cloud IAM changes as of 2018-08-10

Service | Change | Description  
---|---|---  
Binary Authorization  |  Added  |  `binaryauthorization.attestors.verifyImageAttested`  
  
Binary Authorization  |  Supported In Custom Roles  |  `binaryauthorization.attestors.verifyImageAttested`  
  
Compute Engine  |  Added  |  `compute.globalAddresses.createInternal`  
`compute.globalAddresses.deleteInternal`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.globalAddresses.createInternal`  
`compute.globalAddresses.deleteInternal`  
  
Filestore  |  Added  |  `file.instances.create`  
`file.instances.delete`  
`file.instances.get`  
`file.instances.list`  
`file.instances.update`  
`file.locations.get`  
`file.locations.list`  
`file.operations.cancel`  
`file.operations.delete`  
`file.operations.get`  
`file.operations.list`  
  
  
## Cloud IAM changes as of 2018-08-03

Service | Change | Description  
---|---|---  
Android Management  |  Supported In Custom Roles  |  `androidmanagement.enterprises.manage`  
  
Android Management  |  Now GA  |  `androidmanagement.enterprises.manage`  
  
Cloud Billing  |  Supported In Custom Roles  |  `billing.resourceCosts.get`  
  
Binary Authorization  |  Added  |  `binaryauthorization.policy.get`  
`binaryauthorization.policy.getIamPolicy`  
`binaryauthorization.policy.setIamPolicy`  
`binaryauthorization.policy.update`  
  
Managed Service for Apache Airflow  |  Now GA  |  `composer.environments.create`  
`composer.environments.delete`  
`composer.environments.get`  
`composer.environments.list`  
`composer.environments.update`  
`composer.operations.delete`  
`composer.operations.get`  
`composer.operations.list`  
  
Compute Engine  |  Now GA  |  `compute.nodeGroups.addNodes`  
`compute.nodeGroups.create`  
`compute.nodeGroups.delete`  
`compute.nodeGroups.deleteNodes`  
`compute.nodeGroups.get`  
`compute.nodeGroups.list`  
`compute.nodeGroups.setNodeTemplate`  
`compute.nodeTemplates.create`  
`compute.nodeTemplates.delete`  
`compute.nodeTemplates.get`  
`compute.nodeTemplates.list`  
`compute.nodeTypes.get`  
`compute.nodeTypes.list`  
  
Google Kubernetes Engine  |  Now GA  |  `container.hostServiceAgent.use`  
  
Memorystore for Redis  |  Added  |  `redis.operations.cancel`  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `redis.instances.create`  
`redis.instances.delete`  
`redis.instances.get`  
`redis.instances.list`  
`redis.instances.update`  
`redis.locations.get`  
`redis.locations.list`  
`redis.operations.get`  
`redis.operations.list`  
  
Subscribe with Google  |  Added  |  `subscribewithgoogledeveloper.tools.get`  
  
Subscribe with Google  |  Supported In Custom Roles  |  `subscribewithgoogledeveloper.tools.get`  
  
  
## Cloud IAM changes as of 2018-07-20

Service | Change | Description  
---|---|---  
Access Context Manager  |  Added  |  `accesscontextmanager.accessLevels.create`  
`accesscontextmanager.accessLevels.delete`  
`accesscontextmanager.accessLevels.get`  
`accesscontextmanager.accessLevels.list`  
`accesscontextmanager.accessLevels.update`  
`accesscontextmanager.accessPolicies.create`  
`accesscontextmanager.accessPolicies.delete`  
`accesscontextmanager.accessPolicies.get`  
`accesscontextmanager.accessPolicies.getIamPolicy`  
`accesscontextmanager.accessPolicies.list`  
`accesscontextmanager.accessPolicies.setIamPolicy`  
`accesscontextmanager.accessPolicies.update`  
`accesscontextmanager.accessZones.create`  
`accesscontextmanager.accessZones.delete`  
`accesscontextmanager.accessZones.get`  
`accesscontextmanager.accessZones.list`  
`accesscontextmanager.accessZones.update`  
`accesscontextmanager.policies.create`  
`accesscontextmanager.policies.delete`  
`accesscontextmanager.policies.get`  
`accesscontextmanager.policies.getIamPolicy`  
`accesscontextmanager.policies.list`  
`accesscontextmanager.policies.setIamPolicy`  
`accesscontextmanager.policies.update`  
`accesscontextmanager.servicePerimeters.create`  
`accesscontextmanager.servicePerimeters.delete`  
`accesscontextmanager.servicePerimeters.get`  
`accesscontextmanager.servicePerimeters.list`  
`accesscontextmanager.servicePerimeters.update`  
  
AutoML  |  Added  |  `automl.annotationSpecs.create`  
`automl.annotationSpecs.delete`  
`automl.annotationSpecs.get`  
`automl.annotationSpecs.list`  
`automl.annotationSpecs.update`  
`automl.annotations.approve`  
`automl.annotations.create`  
`automl.annotations.list`  
`automl.annotations.manipulate`  
`automl.annotations.reject`  
`automl.datasets.create`  
`automl.datasets.delete`  
`automl.datasets.export`  
`automl.datasets.get`  
`automl.datasets.import`  
`automl.datasets.list`  
`automl.examples.delete`  
`automl.examples.get`  
`automl.examples.list`  
`automl.humanAnnotationTasks.create`  
`automl.humanAnnotationTasks.delete`  
`automl.humanAnnotationTasks.get`  
`automl.humanAnnotationTasks.list`  
`automl.locations.get`  
`automl.locations.list`  
`automl.modelEvaluations.create`  
`automl.modelEvaluations.get`  
`automl.modelEvaluations.list`  
`automl.models.create`  
`automl.models.delete`  
`automl.models.deploy`  
`automl.models.get`  
`automl.models.list`  
`automl.models.predict`  
`automl.models.undeploy`  
`automl.operations.cancel`  
`automl.operations.delete`  
`automl.operations.get`  
`automl.operations.list`  
  
AutoML  |  Supported In Custom Roles  |  `automl.annotationSpecs.create`  
`automl.annotationSpecs.delete`  
`automl.annotationSpecs.get`  
`automl.annotationSpecs.list`  
`automl.annotationSpecs.update`  
`automl.annotations.approve`  
`automl.annotations.create`  
`automl.annotations.list`  
`automl.annotations.manipulate`  
`automl.annotations.reject`  
`automl.datasets.create`  
`automl.datasets.delete`  
`automl.datasets.export`  
`automl.datasets.get`  
`automl.datasets.import`  
`automl.datasets.list`  
`automl.examples.delete`  
`automl.examples.get`  
`automl.examples.list`  
`automl.humanAnnotationTasks.create`  
`automl.humanAnnotationTasks.get`  
`automl.humanAnnotationTasks.list`  
`automl.locations.get`  
`automl.locations.list`  
`automl.modelEvaluations.get`  
`automl.modelEvaluations.list`  
`automl.models.create`  
`automl.models.delete`  
`automl.models.get`  
`automl.models.list`  
`automl.models.predict`  
`automl.operations.cancel`  
`automl.operations.delete`  
`automl.operations.get`  
`automl.operations.list`  
  
Binary Authorization  |  Added  |  `binaryauthorization.attestors.create`  
`binaryauthorization.attestors.delete`  
`binaryauthorization.attestors.get`  
`binaryauthorization.attestors.getIamPolicy`  
`binaryauthorization.attestors.list`  
`binaryauthorization.attestors.setIamPolicy`  
`binaryauthorization.attestors.update`  
  
Binary Authorization  |  Supported In Custom Roles  |  `binaryauthorization.attestors.create`  
`binaryauthorization.attestors.delete`  
`binaryauthorization.attestors.get`  
`binaryauthorization.attestors.getIamPolicy`  
`binaryauthorization.attestors.list`  
`binaryauthorization.attestors.setIamPolicy`  
`binaryauthorization.attestors.update`  
  
Cloud DNS  |  Supported In Custom Roles  |  `dns.changes.create`  
`dns.changes.get`  
`dns.changes.list`  
`dns.managedZones.create`  
`dns.managedZones.delete`  
`dns.managedZones.get`  
`dns.managedZones.list`  
`dns.projects.get`  
`dns.resourceRecordSets.create`  
`dns.resourceRecordSets.delete`  
`dns.resourceRecordSets.list`  
`dns.resourceRecordSets.update`  
  
  
## Cloud IAM changes as of 2018-07-13

Service | Change | Description  
---|---|---  
BigQuery  |  Added  |  `bigquery.datasets.getIamPolicy`  
`bigquery.datasets.setIamPolicy`  
  
Firestore  |  Added  |  `datastore.locations.get`  
`datastore.locations.list`  
  
  
## Cloud IAM changes as of 2018-07-06

Service | Change | Description  
---|---|---  
Managed Service for Apache Airflow  |  Supported In Custom Roles  |  `composer.environments.create`  
`composer.environments.delete`  
`composer.environments.get`  
`composer.environments.list`  
`composer.environments.update`  
`composer.operations.delete`  
`composer.operations.get`  
`composer.operations.list`  
  
Cloud Endpoints  |  Added  |  `endpoints.portals.attachCustomDomain`  
`endpoints.portals.detachCustomDomain`  
`endpoints.portals.listCustomDomains`  
`endpoints.portals.update`  
  
Cloud Endpoints  |  Supported In Custom Roles  |  `endpoints.portals.attachCustomDomain`  
`endpoints.portals.detachCustomDomain`  
`endpoints.portals.listCustomDomains`  
`endpoints.portals.update`  
  
Cloud TPU  |  Added  |  `tpu.acceleratortypes.get`  
`tpu.acceleratortypes.list`  
`tpu.locations.get`  
`tpu.locations.list`  
`tpu.nodes.create`  
`tpu.nodes.delete`  
`tpu.nodes.get`  
`tpu.nodes.list`  
`tpu.nodes.reimage`  
`tpu.nodes.reset`  
`tpu.nodes.start`  
`tpu.nodes.stop`  
`tpu.operations.get`  
`tpu.operations.list`  
`tpu.tensorflowversions.get`  
`tpu.tensorflowversions.list`  
  
Cloud TPU  |  Supported In Custom Roles  |  `tpu.acceleratortypes.get`  
`tpu.acceleratortypes.list`  
`tpu.locations.get`  
`tpu.locations.list`  
`tpu.nodes.create`  
`tpu.nodes.delete`  
`tpu.nodes.get`  
`tpu.nodes.list`  
`tpu.nodes.reimage`  
`tpu.nodes.reset`  
`tpu.nodes.start`  
`tpu.nodes.stop`  
`tpu.operations.get`  
`tpu.operations.list`  
`tpu.tensorflowversions.get`  
`tpu.tensorflowversions.list`  
  
  
## Cloud IAM changes as of 2018-06-29

Service | Change | Description  
---|---|---  
Identity and Access Management  |  Now GA  |  `iam.serviceAccounts.implicitDelegation`  
  
  
## Cloud IAM changes as of 2018-06-15

Service | Change | Description  
---|---|---  
Compute Engine  |  Supported In Custom Roles  |  `compute.backendServices.create`  
`compute.backendServices.delete`  
`compute.backendServices.get`  
`compute.backendServices.list`  
`compute.backendServices.setSecurityPolicy`  
`compute.backendServices.update`  
`compute.backendServices.use`  
`compute.regionBackendServices.create`  
`compute.regionBackendServices.delete`  
`compute.regionBackendServices.get`  
`compute.regionBackendServices.list`  
`compute.regionBackendServices.setSecurityPolicy`  
`compute.regionBackendServices.update`  
`compute.regionBackendServices.use`  
`compute.targetHttpProxies.create`  
`compute.targetHttpProxies.setUrlMap`  
`compute.targetHttpsProxies.create`  
`compute.targetHttpsProxies.setUrlMap`  
`compute.targetSslProxies.create`  
`compute.targetSslProxies.setBackendService`  
`compute.targetTcpProxies.create`  
`compute.targetTcpProxies.update`  
  
Compute Engine  |  Now GA  |  `compute.regionBackendServices.create`  
`compute.regionBackendServices.delete`  
`compute.regionBackendServices.get`  
`compute.regionBackendServices.list`  
`compute.regionBackendServices.setSecurityPolicy`  
`compute.regionBackendServices.update`  
`compute.regionBackendServices.use`  
  
  
## Cloud IAM changes as of 2018-06-08

Service | Change | Description  
---|---|---  
Compute Engine  |  Added  |  `compute.nodeGroups.addNodes`  
`compute.nodeGroups.create`  
`compute.nodeGroups.delete`  
`compute.nodeGroups.deleteNodes`  
`compute.nodeGroups.get`  
`compute.nodeGroups.list`  
`compute.nodeGroups.setNodeTemplate`  
`compute.nodeTemplates.create`  
`compute.nodeTemplates.delete`  
`compute.nodeTemplates.get`  
`compute.nodeTemplates.list`  
`compute.nodeTypes.get`  
`compute.nodeTypes.list`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.nodeGroups.addNodes`  
`compute.nodeGroups.create`  
`compute.nodeGroups.delete`  
`compute.nodeGroups.deleteNodes`  
`compute.nodeGroups.get`  
`compute.nodeGroups.list`  
`compute.nodeGroups.setNodeTemplate`  
`compute.nodeTemplates.create`  
`compute.nodeTemplates.delete`  
`compute.nodeTemplates.get`  
`compute.nodeTemplates.list`  
`compute.nodeTypes.get`  
`compute.nodeTypes.list`  
  
  
## Cloud IAM changes as of 2018-05-11

Service | Change | Description  
---|---|---  
BigQuery  |  Supported In Custom Roles  |  `bigquery.jobs.listAll`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.appProfiles.create`  
`bigtable.appProfiles.delete`  
`bigtable.appProfiles.get`  
`bigtable.appProfiles.list`  
`bigtable.appProfiles.update`  
`bigtable.clusters.create`  
`bigtable.clusters.delete`  
`bigtable.tables.checkConsistency`  
`bigtable.tables.generateConsistencyToken`  
  
Bigtable  |  Now GA  |  `bigtable.appProfiles.create`  
`bigtable.appProfiles.delete`  
`bigtable.appProfiles.get`  
`bigtable.appProfiles.list`  
`bigtable.appProfiles.update`  
`bigtable.tables.checkConsistency`  
`bigtable.tables.generateConsistencyToken`  
  
Managed Service for Apache Airflow  |  Now Beta  |  `composer.environments.create`  
`composer.environments.delete`  
`composer.environments.get`  
`composer.environments.list`  
`composer.environments.update`  
`composer.operations.delete`  
`composer.operations.get`  
`composer.operations.list`  
  
Cloud Life Sciences  |  Supported In Custom Roles  |  `genomics.operations.cancel`  
`genomics.operations.create`  
`genomics.operations.get`  
`genomics.operations.list`  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `monitoring.dashboards.create`  
`monitoring.dashboards.delete`  
`monitoring.dashboards.get`  
`monitoring.dashboards.list`  
`monitoring.dashboards.update`  
`monitoring.publicWidgets.create`  
`monitoring.publicWidgets.delete`  
`monitoring.publicWidgets.get`  
`monitoring.publicWidgets.list`  
`monitoring.publicWidgets.update`  
`monitoring.uptimeCheckConfigs.create`  
`monitoring.uptimeCheckConfigs.delete`  
`monitoring.uptimeCheckConfigs.get`  
`monitoring.uptimeCheckConfigs.list`  
`monitoring.uptimeCheckConfigs.update`  
  
Cloud Monitoring  |  Now GA  |  `monitoring.dashboards.create`  
`monitoring.dashboards.delete`  
`monitoring.dashboards.get`  
`monitoring.dashboards.list`  
`monitoring.dashboards.update`  
`monitoring.publicWidgets.create`  
`monitoring.publicWidgets.delete`  
`monitoring.publicWidgets.get`  
`monitoring.publicWidgets.list`  
`monitoring.publicWidgets.update`  
  
  
## Cloud IAM changes as of 2018-05-04

Service | Change | Description  
---|---|---  
BigQuery  |  Available In Custom Roles  |  `bigquery.jobs.listAll`  
  
Bigtable  |  Added  |  `bigtable.instances.getIamPolicy`  
`bigtable.instances.setIamPolicy`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.instances.getIamPolicy`  
`bigtable.instances.setIamPolicy`  
  
Bigtable  |  Now GA  |  `bigtable.instances.getIamPolicy`  
`bigtable.instances.setIamPolicy`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.osAdminLogin`  
`compute.instances.osLogin`  
`compute.oslogin.updateExternalUser`  
  
Compute Engine  |  Now GA  |  `compute.oslogin.updateExternalUser`  
  
Service Management  |  Supported In Custom Roles  |  `servicemanagement.services.bind`  
  
  
## Cloud IAM changes as of 2018-04-06

Service | Change | Description  
---|---|---  
Compute Engine  |  Supported In Custom Roles  |  `compute.instances.setShieldedVmIntegrityPolicy`  
`compute.instances.updateShieldedVmConfig`  
  
Compute Engine  |  Now GA  |  `compute.instances.setShieldedVmIntegrityPolicy`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.hostServiceAgent.use`  
  
Managed Service for Apache Spark  |  Supported In Custom Roles  |  `dataproc.jobs.getIamPolicy`  
`dataproc.jobs.setIamPolicy`  
`dataproc.operations.getIamPolicy`  
`dataproc.operations.setIamPolicy`  
`dataproc.workflowTemplates.getIamPolicy`  
`dataproc.workflowTemplates.setIamPolicy`  
  
Managed Service for Apache Spark  |  Now GA  |  `dataproc.jobs.getIamPolicy`  
`dataproc.jobs.setIamPolicy`  
`dataproc.operations.getIamPolicy`  
`dataproc.operations.setIamPolicy`  
`dataproc.workflowTemplates.getIamPolicy`  
`dataproc.workflowTemplates.setIamPolicy`  
  
  
## Cloud IAM changes as of 2018-03-30

Service | Change | Description  
---|---|---  
Cloud IoT  |  Now GA  |  `cloudiot.devices.create`  
`cloudiot.devices.delete`  
`cloudiot.devices.get`  
`cloudiot.devices.list`  
`cloudiot.devices.update`  
`cloudiot.devices.updateConfig`  
`cloudiot.registries.create`  
`cloudiot.registries.delete`  
`cloudiot.registries.get`  
`cloudiot.registries.getIamPolicy`  
`cloudiot.registries.list`  
`cloudiot.registries.setIamPolicy`  
`cloudiot.registries.update`  
  
  
## Cloud IAM changes as of 2018-03-23

Service | Change | Description  
---|---|---  
Cloud Life Sciences  |  Supported In Custom Roles  |  `genomics.datasets.create`  
`genomics.datasets.delete`  
`genomics.datasets.get`  
`genomics.datasets.getIamPolicy`  
`genomics.datasets.list`  
`genomics.datasets.setIamPolicy`  
`genomics.datasets.update`  
  
Pub/Sub  |  Supported In Custom Roles  |  `pubsub.snapshots.create`  
`pubsub.snapshots.delete`  
`pubsub.snapshots.list`  
  
  
## Cloud IAM changes as of 2018-03-09

Service | Change | Description  
---|---|---  
Talent Solution  |  Added  |  `cloudjobdiscovery.companies.create`  
`cloudjobdiscovery.companies.delete`  
`cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.companies.update`  
`cloudjobdiscovery.jobs.create`  
`cloudjobdiscovery.jobs.delete`  
`cloudjobdiscovery.jobs.deleteByFilter`  
`cloudjobdiscovery.jobs.get`  
`cloudjobdiscovery.jobs.search`  
`cloudjobdiscovery.jobs.update`  
`cloudjobdiscovery.tools.access`  
  
Talent Solution  |  Supported In Custom Roles  |  `cloudjobdiscovery.companies.create`  
`cloudjobdiscovery.companies.delete`  
`cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.companies.update`  
`cloudjobdiscovery.jobs.create`  
`cloudjobdiscovery.jobs.delete`  
`cloudjobdiscovery.jobs.deleteByFilter`  
`cloudjobdiscovery.jobs.get`  
`cloudjobdiscovery.jobs.search`  
`cloudjobdiscovery.jobs.update`  
`cloudjobdiscovery.tools.access`  
  
Cloud Profiler  |  Added  |  `cloudprofiler.profiles.create`  
`cloudprofiler.profiles.list`  
`cloudprofiler.profiles.update`  
  
Cloud Profiler  |  Supported In Custom Roles  |  `cloudprofiler.profiles.create`  
`cloudprofiler.profiles.list`  
`cloudprofiler.profiles.update`  
  
  
## Cloud IAM changes as of 2018-03-02

Service | Change | Description  
---|---|---  
Open Service Broker for Google Cloud  |  Added  |  `servicebroker.bindingoperations.get`  
`servicebroker.bindingoperations.list`  
`servicebroker.bindings.create`  
`servicebroker.bindings.delete`  
`servicebroker.bindings.get`  
`servicebroker.bindings.getIamPolicy`  
`servicebroker.bindings.list`  
`servicebroker.bindings.setIamPolicy`  
`servicebroker.catalogs.create`  
`servicebroker.catalogs.delete`  
`servicebroker.catalogs.get`  
`servicebroker.catalogs.getIamPolicy`  
`servicebroker.catalogs.list`  
`servicebroker.catalogs.setIamPolicy`  
`servicebroker.catalogs.validate`  
`servicebroker.instanceoperations.get`  
`servicebroker.instanceoperations.list`  
`servicebroker.instances.create`  
`servicebroker.instances.delete`  
`servicebroker.instances.get`  
`servicebroker.instances.getIamPolicy`  
`servicebroker.instances.list`  
`servicebroker.instances.setIamPolicy`  
`servicebroker.instances.update`  
  
Open Service Broker for Google Cloud  |  Supported In Custom Roles  |  `servicebroker.bindingoperations.get`  
`servicebroker.bindingoperations.list`  
`servicebroker.bindings.create`  
`servicebroker.bindings.delete`  
`servicebroker.bindings.get`  
`servicebroker.bindings.getIamPolicy`  
`servicebroker.bindings.list`  
`servicebroker.bindings.setIamPolicy`  
`servicebroker.catalogs.create`  
`servicebroker.catalogs.delete`  
`servicebroker.catalogs.get`  
`servicebroker.catalogs.getIamPolicy`  
`servicebroker.catalogs.list`  
`servicebroker.catalogs.setIamPolicy`  
`servicebroker.catalogs.validate`  
`servicebroker.instanceoperations.get`  
`servicebroker.instanceoperations.list`  
`servicebroker.instances.create`  
`servicebroker.instances.delete`  
`servicebroker.instances.get`  
`servicebroker.instances.getIamPolicy`  
`servicebroker.instances.list`  
`servicebroker.instances.setIamPolicy`  
`servicebroker.instances.update`  
  
  
## Cloud IAM changes as of 2018-02-23

Service | Change | Description  
---|---|---  
Resource Manager  |  Supported In Custom Roles  |  `resourcemanager.projects.list`  
`resourcemanager.projects.move`  
  
Service Management  |  Added  |  `servicemanagement.services.quota`  
  
Service Management  |  Supported In Custom Roles  |  `servicemanagement.services.quota`  
  
Cloud Source Repositories  |  Supported In Custom Roles  |  `source.repos.create`  
  
  
## Cloud IAM changes as of 2018-02-16

Service | Change | Description  
---|---|---  
BigQuery  |  Supported In Custom Roles  |  `bigquery.tables.update`  
`bigquery.tables.updateData`  
  
Cloud IoT  |  Supported In Custom Roles  |  `cloudiot.devices.create`  
`cloudiot.devices.delete`  
`cloudiot.devices.get`  
`cloudiot.devices.list`  
`cloudiot.devices.update`  
`cloudiot.devices.updateConfig`  
`cloudiot.registries.create`  
`cloudiot.registries.delete`  
`cloudiot.registries.get`  
`cloudiot.registries.getIamPolicy`  
`cloudiot.registries.list`  
`cloudiot.registries.setIamPolicy`  
`cloudiot.registries.update`  
  
Cloud SQL  |  Supported In Custom Roles  |  `cloudsql.instances.demoteMaster`  
  
Google Cloud Support  |  Added  |  `cloudsupport.accounts.create`  
`cloudsupport.accounts.delete`  
`cloudsupport.accounts.get`  
`cloudsupport.accounts.getIamPolicy`  
`cloudsupport.accounts.getUserRoles`  
`cloudsupport.accounts.list`  
`cloudsupport.accounts.setIamPolicy`  
`cloudsupport.accounts.update`  
`cloudsupport.accounts.updateUserRoles`  
`cloudsupport.operations.get`  
  
Compute Engine  |  Added  |  `compute.oslogin.updateExternalUser`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.addresses.create`  
`compute.disks.create`  
`compute.disks.setLabels`  
`compute.forwardingRules.create`  
`compute.globalAddresses.create`  
`compute.globalForwardingRules.create`  
`compute.images.create`  
`compute.images.setLabels`  
`compute.snapshots.create`  
`compute.snapshots.setLabels`  
`compute.targetVpnGateways.create`  
`compute.vpnTunnels.create`  
  
Managed Service for Apache Spark  |  Supported In Custom Roles  |  `dataproc.agents.create`  
`dataproc.agents.delete`  
`dataproc.agents.get`  
`dataproc.agents.list`  
`dataproc.agents.update`  
`dataproc.tasks.lease`  
`dataproc.tasks.listInvalidatedLeases`  
`dataproc.tasks.reportStatus`  
`dataproc.workflowTemplates.instantiateInline`  
  
Cloud DNS  |  Added  |  `dns.changes.create`  
`dns.changes.get`  
`dns.changes.list`  
`dns.dnsKeys.create`  
`dns.dnsKeys.delete`  
`dns.dnsKeys.get`  
`dns.dnsKeys.list`  
`dns.dnsKeys.update`  
`dns.managedZoneOperations.get`  
`dns.managedZoneOperations.list`  
`dns.managedZones.create`  
`dns.managedZones.delete`  
`dns.managedZones.get`  
`dns.managedZones.list`  
`dns.managedZones.update`  
`dns.projects.get`  
`dns.resourceRecordSets.create`  
`dns.resourceRecordSets.delete`  
`dns.resourceRecordSets.get`  
`dns.resourceRecordSets.list`  
`dns.resourceRecordSets.update`  
  
  
## Cloud IAM changes as of 2018-02-02

Service | Change | Description  
---|---|---  
Compute Engine  |  Available In Custom Roles  |  `compute.interconnectAttachments.create`  
`compute.interconnectAttachments.delete`  
`compute.interconnectAttachments.get`  
`compute.interconnectAttachments.list`  
`compute.interconnectAttachments.setLabels`  
`compute.interconnectAttachments.update`  
`compute.interconnectAttachments.use`  
`compute.interconnectLocations.get`  
`compute.interconnectLocations.list`  
`compute.interconnects.create`  
`compute.interconnects.delete`  
`compute.interconnects.get`  
`compute.interconnects.list`  
`compute.interconnects.setLabels`  
`compute.interconnects.update`  
`compute.interconnects.use`  
  
Sensitive Data Protection  |  Added  |  `dlp.jobTriggers.create`  
`dlp.jobTriggers.delete`  
`dlp.jobTriggers.get`  
`dlp.jobTriggers.list`  
`dlp.jobTriggers.update`  
  
  
## Cloud IAM changes as of 2018-01-26

Service | Change | Description  
---|---|---  
BigQuery  |  Added  |  `bigquery.jobs.listAll`  
  
Google Kubernetes Engine  |  Added  |  `container.podSecurityPolicies.create`  
`container.podSecurityPolicies.delete`  
`container.podSecurityPolicies.get`  
`container.podSecurityPolicies.list`  
`container.podSecurityPolicies.update`  
`container.podSecurityPolicies.use`  
  
  
## Cloud IAM changes as of 2018-01-19

Service | Change | Description  
---|---|---  
Compute Engine  |  Added  |  `compute.addresses.createInternal`  
`compute.addresses.deleteInternal`  
`compute.addresses.useInternal`  
  
  
## Cloud IAM changes as of 2018-01-12

Service | Change | Description  
---|---|---  
App Engine  |  Not Supported In Custom Roles  |  `appengine.runtimes.actAsAdmin`  
  
Compute Engine  |  Added  |  `compute.backendServices.setSecurityPolicy`  
`compute.securityPolicies.create`  
`compute.securityPolicies.delete`  
`compute.securityPolicies.get`  
`compute.securityPolicies.getIamPolicy`  
`compute.securityPolicies.list`  
`compute.securityPolicies.setIamPolicy`  
`compute.securityPolicies.update`  
`compute.securityPolicies.use`  
  
Compute Engine  |  Not Supported In Custom Roles  |  `compute.organizations.administerXpn`  
`compute.targetHttpProxies.create`  
`compute.targetHttpProxies.setUrlMap`  
`compute.targetHttpsProxies.create`  
`compute.targetHttpsProxies.setUrlMap`  
`compute.targetSslProxies.create`  
`compute.targetSslProxies.setBackendService`  
`compute.targetTcpProxies.create`  
`compute.targetTcpProxies.update`  
  
Compute Engine  |  Now GA  |  `compute.instances.osAdminLogin`  
`compute.instances.osLogin`  
  
  
## Cloud IAM changes as of 2017-12-22

Service | Change | Description  
---|---|---  
App Engine  |  Supported In Custom Roles  |  `appengine.applications.create`  
`appengine.applications.get`  
`appengine.applications.update`  
`appengine.instances.delete`  
`appengine.instances.get`  
`appengine.instances.list`  
`appengine.operations.get`  
`appengine.operations.list`  
`appengine.services.delete`  
`appengine.services.get`  
`appengine.services.list`  
`appengine.services.update`  
`appengine.versions.create`  
`appengine.versions.delete`  
`appengine.versions.get`  
`appengine.versions.list`  
`appengine.versions.update`  
  
App Engine  |  Not Supported In Custom Roles  |  `appengine.applications.list`  
`appengine.operations.cancel`  
`appengine.operations.delete`  
`appengine.services.create`  
  
Cloud Billing  |  Supported In Custom Roles  |  `billing.accounts.close`  
`billing.accounts.reopen`  
`billing.budgets.delete`  
`billing.budgets.update`  
  
Cloud Debugger  |  Supported In Custom Roles  |  `clouddebugger.breakpoints.create`  
`clouddebugger.breakpoints.delete`  
`clouddebugger.breakpoints.get`  
`clouddebugger.breakpoints.list`  
`clouddebugger.breakpoints.listActive`  
`clouddebugger.breakpoints.update`  
`clouddebugger.debuggees.create`  
`clouddebugger.debuggees.list`  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `cloudkms.cryptoKeyVersions.create`  
`cloudkms.cryptoKeyVersions.destroy`  
`cloudkms.cryptoKeyVersions.get`  
`cloudkms.cryptoKeyVersions.list`  
`cloudkms.cryptoKeyVersions.restore`  
`cloudkms.cryptoKeyVersions.update`  
`cloudkms.cryptoKeyVersions.useToDecrypt`  
`cloudkms.cryptoKeyVersions.useToEncrypt`  
`cloudkms.cryptoKeys.create`  
`cloudkms.cryptoKeys.get`  
`cloudkms.cryptoKeys.getIamPolicy`  
`cloudkms.cryptoKeys.list`  
`cloudkms.cryptoKeys.setIamPolicy`  
`cloudkms.cryptoKeys.update`  
`cloudkms.keyRings.create`  
`cloudkms.keyRings.get`  
`cloudkms.keyRings.getIamPolicy`  
`cloudkms.keyRings.list`  
`cloudkms.keyRings.setIamPolicy`  
  
Cloud SQL  |  Supported In Custom Roles  |  `cloudsql.backupRuns.create`  
`cloudsql.backupRuns.delete`  
`cloudsql.backupRuns.get`  
`cloudsql.backupRuns.list`  
`cloudsql.databases.create`  
`cloudsql.databases.delete`  
`cloudsql.databases.get`  
`cloudsql.databases.list`  
`cloudsql.databases.update`  
`cloudsql.instances.clone`  
`cloudsql.instances.connect`  
`cloudsql.instances.create`  
`cloudsql.instances.delete`  
`cloudsql.instances.export`  
`cloudsql.instances.failover`  
`cloudsql.instances.get`  
`cloudsql.instances.import`  
`cloudsql.instances.list`  
`cloudsql.instances.promoteReplica`  
`cloudsql.instances.resetSslConfig`  
`cloudsql.instances.restart`  
`cloudsql.instances.restoreBackup`  
`cloudsql.instances.startReplica`  
`cloudsql.instances.stopReplica`  
`cloudsql.instances.truncateLog`  
`cloudsql.instances.update`  
`cloudsql.sslCerts.create`  
`cloudsql.sslCerts.delete`  
`cloudsql.sslCerts.get`  
`cloudsql.sslCerts.list`  
`cloudsql.users.create`  
`cloudsql.users.delete`  
`cloudsql.users.list`  
`cloudsql.users.update`  
  
Cloud SQL  |  Not Supported In Custom Roles  |  `cloudsql.databases.getIamPolicy`  
`cloudsql.databases.setIamPolicy`  
`cloudsql.instances.demoteMaster`  
`cloudsql.instances.getIamPolicy`  
`cloudsql.instances.migrate`  
`cloudsql.instances.setIamPolicy`  
`cloudsql.sslCerts.createEphemeral`  
  
Cloud Trace  |  Supported In Custom Roles  |  `cloudtrace.insights.get`  
`cloudtrace.insights.list`  
`cloudtrace.stats.get`  
`cloudtrace.tasks.create`  
`cloudtrace.tasks.delete`  
`cloudtrace.tasks.get`  
`cloudtrace.tasks.list`  
`cloudtrace.traces.get`  
`cloudtrace.traces.list`  
`cloudtrace.traces.patch`  
  
Compute Engine  |  Added  |  `compute.instances.setMachineResources`  
`compute.instances.setMinCpuPlatform`  
`compute.instances.setServiceAccount`  
`compute.instances.updateAccessConfig`  
`compute.instances.updateNetworkInterface`  
`compute.licenseCodes.get`  
`compute.licenseCodes.list`  
`compute.licenseCodes.update`  
`compute.licenseCodes.use`  
  
Compute Engine  |  Supported In Custom Roles  |  `compute.acceleratorTypes.get`  
`compute.acceleratorTypes.list`  
`compute.addresses.delete`  
`compute.addresses.get`  
`compute.addresses.list`  
`compute.addresses.use`  
`compute.autoscalers.create`  
`compute.autoscalers.delete`  
`compute.autoscalers.get`  
`compute.autoscalers.list`  
`compute.autoscalers.update`  
`compute.backendBuckets.create`  
`compute.backendBuckets.delete`  
`compute.backendBuckets.get`  
`compute.backendBuckets.list`  
`compute.backendBuckets.update`  
`compute.commitments.list`  
`compute.diskTypes.get`  
`compute.diskTypes.list`  
`compute.disks.createSnapshot`  
`compute.disks.delete`  
`compute.disks.get`  
`compute.disks.list`  
`compute.disks.resize`  
`compute.disks.update`  
`compute.disks.use`  
`compute.disks.useReadOnly`  
`compute.firewalls.create`  
`compute.firewalls.delete`  
`compute.firewalls.get`  
`compute.firewalls.list`  
`compute.firewalls.update`  
`compute.forwardingRules.delete`  
`compute.forwardingRules.get`  
`compute.forwardingRules.list`  
`compute.forwardingRules.setTarget`  
`compute.globalAddresses.delete`  
`compute.globalAddresses.get`  
`compute.globalAddresses.list`  
`compute.globalAddresses.use`  
`compute.globalForwardingRules.delete`  
`compute.globalForwardingRules.get`  
`compute.globalForwardingRules.list`  
`compute.globalOperations.delete`  
`compute.globalOperations.get`  
`compute.globalOperations.list`  
`compute.httpHealthChecks.create`  
`compute.httpHealthChecks.delete`  
`compute.httpHealthChecks.get`  
`compute.httpHealthChecks.list`  
`compute.httpHealthChecks.update`  
`compute.httpHealthChecks.useReadOnly`  
`compute.httpsHealthChecks.create`  
`compute.httpsHealthChecks.delete`  
`compute.httpsHealthChecks.get`  
`compute.httpsHealthChecks.list`  
`compute.httpsHealthChecks.update`  
`compute.httpsHealthChecks.useReadOnly`  
`compute.images.delete`  
`compute.images.deprecate`  
`compute.images.get`  
`compute.images.getFromFamily`  
`compute.images.list`  
`compute.instanceGroupManagers.create`  
`compute.instanceGroupManagers.delete`  
`compute.instanceGroupManagers.get`  
`compute.instanceGroupManagers.list`  
`compute.instanceGroupManagers.update`  
`compute.instanceGroupManagers.use`  
`compute.instanceGroups.create`  
`compute.instanceGroups.delete`  
`compute.instanceGroups.get`  
`compute.instanceGroups.list`  
`compute.instanceGroups.update`  
`compute.instanceTemplates.create`  
`compute.instanceTemplates.delete`  
`compute.instanceTemplates.get`  
`compute.instanceTemplates.list`  
`compute.instanceTemplates.useReadOnly`  
`compute.instances.addAccessConfig`  
`compute.instances.attachDisk`  
`compute.instances.create`  
`compute.instances.delete`  
`compute.instances.deleteAccessConfig`  
`compute.instances.detachDisk`  
`compute.instances.get`  
`compute.instances.getSerialPortOutput`  
`compute.instances.list`  
`compute.instances.listReferrers`  
`compute.instances.reset`  
`compute.instances.setDiskAutoDelete`  
`compute.instances.setLabels`  
`compute.instances.setMachineType`  
`compute.instances.setMetadata`  
`compute.instances.setScheduling`  
`compute.instances.setTags`  
`compute.instances.start`  
`compute.instances.stop`  
`compute.instances.use`  
`compute.machineTypes.get`  
`compute.machineTypes.list`  
`compute.networks.create`  
`compute.networks.delete`  
`compute.networks.get`  
`compute.networks.list`  
`compute.networks.updatePolicy`  
`compute.organizations.disableXpnHost`  
`compute.organizations.disableXpnResource`  
`compute.organizations.enableXpnHost`  
`compute.organizations.enableXpnResource`  
`compute.projects.get`  
`compute.projects.setCommonInstanceMetadata`  
`compute.projects.setUsageExportBucket`  
`compute.regionOperations.delete`  
`compute.regionOperations.get`  
`compute.regionOperations.list`  
`compute.regions.get`  
`compute.regions.list`  
`compute.routers.create`  
`compute.routers.delete`  
`compute.routers.get`  
`compute.routers.list`  
`compute.routers.update`  
`compute.routers.use`  
`compute.routes.create`  
`compute.routes.delete`  
`compute.routes.get`  
`compute.routes.list`  
`compute.snapshots.delete`  
`compute.snapshots.get`  
`compute.snapshots.list`  
`compute.snapshots.useReadOnly`  
`compute.sslCertificates.create`  
`compute.sslCertificates.delete`  
`compute.sslCertificates.get`  
`compute.sslCertificates.list`  
`compute.subnetworks.use`  
`compute.subnetworks.useExternalIp`  
`compute.targetHttpProxies.create`  
`compute.targetHttpProxies.delete`  
`compute.targetHttpProxies.get`  
`compute.targetHttpProxies.list`  
`compute.targetHttpProxies.setUrlMap`  
`compute.targetHttpProxies.use`  
`compute.targetHttpsProxies.create`  
`compute.targetHttpsProxies.delete`  
`compute.targetHttpsProxies.get`  
`compute.targetHttpsProxies.list`  
`compute.targetHttpsProxies.setSslCertificates`  
`compute.targetHttpsProxies.setUrlMap`  
`compute.targetHttpsProxies.use`  
`compute.targetInstances.create`  
`compute.targetInstances.delete`  
`compute.targetInstances.get`  
`compute.targetInstances.list`  
`compute.targetInstances.use`  
`compute.targetPools.addHealthCheck`  
`compute.targetPools.addInstance`  
`compute.targetPools.create`  
`compute.targetPools.delete`  
`compute.targetPools.get`  
`compute.targetPools.list`  
`compute.targetPools.removeHealthCheck`  
`compute.targetPools.removeInstance`  
`compute.targetPools.update`  
`compute.targetPools.use`  
`compute.targetSslProxies.create`  
`compute.targetSslProxies.delete`  
`compute.targetSslProxies.get`  
`compute.targetSslProxies.list`  
`compute.targetSslProxies.setBackendService`  
`compute.targetSslProxies.setProxyHeader`  
`compute.targetSslProxies.setSslCertificates`  
`compute.targetSslProxies.use`  
`compute.targetTcpProxies.create`  
`compute.targetTcpProxies.delete`  
`compute.targetTcpProxies.get`  
`compute.targetTcpProxies.list`  
`compute.targetTcpProxies.update`  
`compute.targetTcpProxies.use`  
`compute.targetVpnGateways.delete`  
`compute.targetVpnGateways.get`  
`compute.targetVpnGateways.list`  
`compute.targetVpnGateways.use`  
`compute.vpnTunnels.delete`  
`compute.vpnTunnels.get`  
`compute.vpnTunnels.list`  
`compute.zoneOperations.delete`  
`compute.zoneOperations.get`  
`compute.zoneOperations.list`  
`compute.zones.get`  
`compute.zones.list`  
  
Compute Engine  |  Not Supported In Custom Roles  |  `compute.backendServices.create`  
`compute.backendServices.delete`  
`compute.backendServices.get`  
`compute.backendServices.list`  
`compute.backendServices.update`  
`compute.backendServices.use`  
`compute.healthChecks.create`  
`compute.healthChecks.delete`  
`compute.healthChecks.get`  
`compute.healthChecks.list`  
`compute.healthChecks.update`  
`compute.healthChecks.use`  
`compute.healthChecks.useReadOnly`  
`compute.interconnectAttachments.create`  
`compute.interconnectAttachments.delete`  
`compute.interconnectAttachments.get`  
`compute.interconnectAttachments.list`  
`compute.interconnectAttachments.setLabels`  
`compute.interconnectAttachments.update`  
`compute.interconnectAttachments.use`  
`compute.interconnectLocations.get`  
`compute.interconnectLocations.list`  
`compute.interconnects.create`  
`compute.interconnects.delete`  
`compute.interconnects.get`  
`compute.interconnects.list`  
`compute.interconnects.setLabels`  
`compute.interconnects.update`  
`compute.interconnects.use`  
`compute.urlMaps.create`  
`compute.urlMaps.delete`  
`compute.urlMaps.get`  
`compute.urlMaps.invalidateCache`  
`compute.urlMaps.list`  
`compute.urlMaps.update`  
`compute.urlMaps.use`  
`compute.urlMaps.validate`  
  
Google Kubernetes Engine  |  Added  |  `container.services.updateStatus`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `container.clusters.create`  
`container.clusters.delete`  
`container.clusters.get`  
`container.clusters.getCredentials`  
`container.clusters.list`  
`container.clusters.update`  
`container.operations.get`  
`container.operations.list`  
  
Managed Service for Apache Spark  |  Supported In Custom Roles  |  `dataproc.clusters.create`  
`dataproc.clusters.delete`  
`dataproc.clusters.get`  
`dataproc.clusters.getIamPolicy`  
`dataproc.clusters.list`  
`dataproc.clusters.setIamPolicy`  
`dataproc.clusters.update`  
`dataproc.clusters.use`  
`dataproc.jobs.cancel`  
`dataproc.jobs.create`  
`dataproc.jobs.delete`  
`dataproc.jobs.get`  
`dataproc.jobs.list`  
`dataproc.jobs.update`  
`dataproc.operations.cancel`  
`dataproc.operations.delete`  
`dataproc.operations.get`  
`dataproc.operations.list`  
`dataproc.workflowTemplates.create`  
`dataproc.workflowTemplates.delete`  
`dataproc.workflowTemplates.get`  
`dataproc.workflowTemplates.instantiate`  
`dataproc.workflowTemplates.list`  
`dataproc.workflowTemplates.update`  
  
Firestore  |  Not Supported In Custom Roles  |  `datastore.databases.create`  
`datastore.databases.delete`  
`datastore.databases.export`  
`datastore.databases.get`  
`datastore.databases.getIamPolicy`  
`datastore.databases.import`  
`datastore.databases.list`  
`datastore.databases.setIamPolicy`  
`datastore.databases.update`  
`datastore.entities.allocateIds`  
`datastore.entities.create`  
`datastore.entities.delete`  
`datastore.entities.get`  
`datastore.entities.list`  
`datastore.entities.update`  
`datastore.indexes.create`  
`datastore.indexes.delete`  
`datastore.indexes.get`  
`datastore.indexes.list`  
`datastore.indexes.update`  
`datastore.namespaces.get`  
`datastore.namespaces.getIamPolicy`  
`datastore.namespaces.list`  
`datastore.namespaces.setIamPolicy`  
`datastore.operations.cancel`  
`datastore.operations.delete`  
`datastore.operations.get`  
`datastore.operations.list`  
`datastore.statistics.get`  
`datastore.statistics.list`  
  
Cloud Deployment Manager  |  Supported In Custom Roles  |  `deploymentmanager.compositeTypes.create`  
`deploymentmanager.compositeTypes.delete`  
`deploymentmanager.compositeTypes.get`  
`deploymentmanager.compositeTypes.list`  
`deploymentmanager.compositeTypes.update`  
`deploymentmanager.deployments.cancelPreview`  
`deploymentmanager.deployments.create`  
`deploymentmanager.deployments.delete`  
`deploymentmanager.deployments.get`  
`deploymentmanager.deployments.getIamPolicy`  
`deploymentmanager.deployments.list`  
`deploymentmanager.deployments.setIamPolicy`  
`deploymentmanager.deployments.stop`  
`deploymentmanager.deployments.update`  
`deploymentmanager.manifests.get`  
`deploymentmanager.manifests.list`  
`deploymentmanager.operations.get`  
`deploymentmanager.operations.list`  
`deploymentmanager.resources.get`  
`deploymentmanager.resources.list`  
`deploymentmanager.typeProviders.create`  
`deploymentmanager.typeProviders.delete`  
`deploymentmanager.typeProviders.get`  
`deploymentmanager.typeProviders.list`  
`deploymentmanager.typeProviders.update`  
`deploymentmanager.types.list`  
  
Dialogflow  |  Supported In Custom Roles  |  `dialogflow.agents.export`  
`dialogflow.agents.get`  
`dialogflow.agents.import`  
`dialogflow.agents.restore`  
`dialogflow.contexts.create`  
`dialogflow.contexts.delete`  
`dialogflow.contexts.get`  
`dialogflow.contexts.list`  
`dialogflow.contexts.update`  
`dialogflow.entityTypes.create`  
`dialogflow.entityTypes.createEntity`  
`dialogflow.entityTypes.delete`  
`dialogflow.entityTypes.deleteEntity`  
`dialogflow.entityTypes.get`  
`dialogflow.entityTypes.list`  
`dialogflow.entityTypes.update`  
`dialogflow.entityTypes.updateEntity`  
`dialogflow.intents.create`  
`dialogflow.intents.delete`  
`dialogflow.intents.get`  
`dialogflow.intents.list`  
`dialogflow.intents.update`  
`dialogflow.operations.get`  
`dialogflow.sessionEntityTypes.create`  
`dialogflow.sessionEntityTypes.delete`  
`dialogflow.sessionEntityTypes.get`  
`dialogflow.sessionEntityTypes.list`  
`dialogflow.sessionEntityTypes.update`  
`dialogflow.sessions.detectIntent`  
`dialogflow.sessions.streamingDetectIntent`  
  
Error Reporting  |  Supported In Custom Roles  |  `errorreporting.applications.list`  
`errorreporting.errorEvents.create`  
`errorreporting.errorEvents.delete`  
`errorreporting.errorEvents.list`  
`errorreporting.groupMetadata.get`  
`errorreporting.groupMetadata.update`  
`errorreporting.groups.list`  
  
Identity and Access Management  |  Not Supported In Custom Roles  |  `iam.serviceAccounts.actAs`  
`iam.serviceAccounts.getAccessToken`  
`iam.serviceAccounts.signBlob`  
`iam.serviceAccounts.signJwt`  
  
Cloud Logging  |  Supported In Custom Roles  |  `logging.exclusions.create`  
`logging.exclusions.delete`  
`logging.exclusions.get`  
`logging.exclusions.list`  
`logging.exclusions.update`  
`logging.logEntries.create`  
`logging.logEntries.list`  
`logging.logMetrics.create`  
`logging.logMetrics.delete`  
`logging.logMetrics.get`  
`logging.logMetrics.list`  
`logging.logMetrics.update`  
`logging.logServiceIndexes.list`  
`logging.logServices.list`  
`logging.logs.delete`  
`logging.logs.list`  
`logging.privateLogEntries.list`  
`logging.sinks.create`  
`logging.sinks.delete`  
`logging.sinks.get`  
`logging.sinks.list`  
`logging.sinks.update`  
`logging.usage.get`  
  
AI Platform  |  Supported In Custom Roles  |  `ml.jobs.cancel`  
`ml.jobs.create`  
`ml.jobs.get`  
`ml.jobs.getIamPolicy`  
`ml.jobs.list`  
`ml.jobs.setIamPolicy`  
`ml.jobs.update`  
`ml.locations.get`  
`ml.locations.list`  
`ml.models.create`  
`ml.models.delete`  
`ml.models.get`  
`ml.models.getIamPolicy`  
`ml.models.list`  
`ml.models.predict`  
`ml.models.setIamPolicy`  
`ml.models.update`  
`ml.operations.cancel`  
`ml.operations.get`  
`ml.operations.list`  
`ml.projects.getConfig`  
`ml.versions.create`  
`ml.versions.delete`  
`ml.versions.get`  
`ml.versions.list`  
`ml.versions.predict`  
`ml.versions.update`  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `monitoring.groups.create`  
`monitoring.groups.delete`  
`monitoring.groups.get`  
`monitoring.groups.list`  
`monitoring.groups.update`  
`monitoring.metricDescriptors.create`  
`monitoring.metricDescriptors.delete`  
`monitoring.metricDescriptors.get`  
`monitoring.metricDescriptors.list`  
`monitoring.monitoredResourceDescriptors.get`  
`monitoring.monitoredResourceDescriptors.list`  
`monitoring.timeSeries.create`  
`monitoring.timeSeries.list`  
  
Pub/Sub  |  Supported In Custom Roles  |  `pubsub.topics.setIamPolicy`  
  
Service Management  |  Supported In Custom Roles  |  `servicemanagement.services.check`  
`servicemanagement.services.report`  
  
Service Management  |  Not Supported In Custom Roles  |  `servicemanagement.consumerSettings.get`  
`servicemanagement.consumerSettings.getIamPolicy`  
`servicemanagement.consumerSettings.list`  
`servicemanagement.consumerSettings.setIamPolicy`  
`servicemanagement.consumerSettings.update`  
  
Cloud Source Repositories  |  Supported In Custom Roles  |  `source.repos.delete`  
`source.repos.get`  
`source.repos.getIamPolicy`  
`source.repos.list`  
`source.repos.setIamPolicy`  
  
Cloud Source Repositories  |  Not Supported In Custom Roles  |  `source.repos.update`  
  
Spanner  |  Supported In Custom Roles  |  `spanner.databaseOperations.cancel`  
`spanner.databaseOperations.get`  
`spanner.databaseOperations.list`  
`spanner.databases.beginOrRollbackReadWriteTransaction`  
`spanner.databases.beginReadOnlyTransaction`  
`spanner.databases.create`  
`spanner.databases.drop`  
`spanner.databases.get`  
`spanner.databases.getDdl`  
`spanner.databases.getIamPolicy`  
`spanner.databases.list`  
`spanner.databases.read`  
`spanner.databases.select`  
`spanner.databases.setIamPolicy`  
`spanner.databases.updateDdl`  
`spanner.databases.write`  
`spanner.instanceConfigs.get`  
`spanner.instanceConfigs.list`  
`spanner.instanceOperations.cancel`  
`spanner.instanceOperations.delete`  
`spanner.instanceOperations.get`  
`spanner.instanceOperations.list`  
`spanner.instances.create`  
`spanner.instances.delete`  
`spanner.instances.get`  
`spanner.instances.getIamPolicy`  
`spanner.instances.list`  
`spanner.instances.setIamPolicy`  
`spanner.instances.update`  
`spanner.sessions.create`  
`spanner.sessions.delete`  
`spanner.sessions.get`  
`spanner.sessions.list`  
  
Spanner  |  Not Supported In Custom Roles  |  `spanner.databaseOperations.delete`  
`spanner.databases.update`  
  
Cloud Storage  |  Supported In Custom Roles  |  `storage.buckets.create`  
`storage.buckets.delete`  
`storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.list`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`storage.objects.create`  
`storage.objects.delete`  
`storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.list`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
  
  
## Cloud IAM changes as of 2017-12-08

Service | Change | Description  
---|---|---  
BigQuery  |  Supported In Custom Roles  |  `bigquery.datasets.create`  
`bigquery.datasets.delete`  
`bigquery.datasets.get`  
`bigquery.datasets.update`  
`bigquery.jobs.create`  
`bigquery.jobs.get`  
`bigquery.jobs.list`  
`bigquery.jobs.update`  
`bigquery.savedqueries.create`  
`bigquery.savedqueries.delete`  
`bigquery.savedqueries.get`  
`bigquery.savedqueries.list`  
`bigquery.savedqueries.update`  
`bigquery.tables.create`  
`bigquery.tables.delete`  
`bigquery.tables.export`  
`bigquery.tables.get`  
`bigquery.tables.getData`  
`bigquery.tables.list`  
  
BigQuery  |  Not Supported In Custom Roles  |  `bigquery.config.get`  
`bigquery.config.update`  
`bigquery.service.actAsSuperuser`  
`bigquery.tables.update`  
`bigquery.tables.updateData`  
`bigquery.transfers.get`  
`bigquery.transfers.update`  
  
Bigtable  |  Supported In Custom Roles  |  `bigtable.clusters.get`  
`bigtable.clusters.list`  
`bigtable.clusters.update`  
`bigtable.instances.create`  
`bigtable.instances.delete`  
`bigtable.instances.get`  
`bigtable.instances.list`  
`bigtable.instances.update`  
`bigtable.tables.create`  
`bigtable.tables.delete`  
`bigtable.tables.get`  
`bigtable.tables.list`  
`bigtable.tables.mutateRows`  
`bigtable.tables.readRows`  
`bigtable.tables.sampleRowKeys`  
`bigtable.tables.update`  
  
Compute Engine  |  Added  |  `compute.disks.getIamPolicy`  
`compute.disks.setIamPolicy`  
`compute.globalOperations.getIamPolicy`  
`compute.globalOperations.setIamPolicy`  
`compute.images.getIamPolicy`  
`compute.images.setIamPolicy`  
`compute.instances.getIamPolicy`  
`compute.instances.setIamPolicy`  
`compute.licenses.getIamPolicy`  
`compute.licenses.setIamPolicy`  
`compute.organizations.administerXpn`  
`compute.organizations.disableXpnHost`  
`compute.organizations.disableXpnResource`  
`compute.organizations.enableXpnHost`  
`compute.organizations.enableXpnResource`  
`compute.regionOperations.getIamPolicy`  
`compute.regionOperations.setIamPolicy`  
`compute.snapshots.getIamPolicy`  
`compute.snapshots.setIamPolicy`  
`compute.vpnGateways.create`  
`compute.vpnGateways.delete`  
`compute.vpnGateways.get`  
`compute.vpnGateways.list`  
`compute.vpnGateways.setLabels`  
`compute.vpnGateways.use`  
`compute.zoneOperations.getIamPolicy`  
`compute.zoneOperations.setIamPolicy`  
  
Dataflow  |  Supported In Custom Roles  |  `dataflow.jobs.cancel`  
`dataflow.jobs.create`  
`dataflow.jobs.get`  
`dataflow.jobs.list`  
`dataflow.jobs.updateContents`  
`dataflow.messages.list`  
`dataflow.metrics.get`  
  
Managed Service for Apache Spark  |  Added  |  `dataproc.workflowTemplates.instantiateInline`  
  
Sensitive Data Protection  |  Added  |  `dlp.analyzeRiskTemplates.create`  
`dlp.analyzeRiskTemplates.delete`  
`dlp.analyzeRiskTemplates.get`  
`dlp.analyzeRiskTemplates.list`  
`dlp.analyzeRiskTemplates.update`  
`dlp.deidentifyTemplates.create`  
`dlp.deidentifyTemplates.delete`  
`dlp.deidentifyTemplates.get`  
`dlp.deidentifyTemplates.list`  
`dlp.deidentifyTemplates.update`  
`dlp.inspectTemplates.create`  
`dlp.inspectTemplates.delete`  
`dlp.inspectTemplates.get`  
`dlp.inspectTemplates.list`  
`dlp.inspectTemplates.update`  
`dlp.jobs.cancel`  
`dlp.jobs.create`  
`dlp.jobs.delete`  
`dlp.jobs.get`  
`dlp.jobs.list`  
  
Pub/Sub  |  Added  |  `pubsub.snapshots.create`  
`pubsub.snapshots.delete`  
`pubsub.snapshots.get`  
`pubsub.snapshots.getIamPolicy`  
`pubsub.snapshots.list`  
`pubsub.snapshots.seek`  
`pubsub.snapshots.setIamPolicy`  
`pubsub.snapshots.update`  
  
Pub/Sub  |  Supported In Custom Roles  |  `pubsub.subscriptions.consume`  
`pubsub.subscriptions.create`  
`pubsub.subscriptions.delete`  
`pubsub.subscriptions.get`  
`pubsub.subscriptions.getIamPolicy`  
`pubsub.subscriptions.list`  
`pubsub.subscriptions.setIamPolicy`  
`pubsub.subscriptions.update`  
`pubsub.topics.attachSubscription`  
`pubsub.topics.create`  
`pubsub.topics.delete`  
`pubsub.topics.get`  
`pubsub.topics.getIamPolicy`  
`pubsub.topics.list`  
`pubsub.topics.publish`  
  
  
## Cloud IAM changes as of 2017-12-01

Service | Change | Description  
---|---|---  
Cloud Build  |  Supported In Custom Roles  |  `cloudbuild.builds.create`  
`cloudbuild.builds.get`  
`cloudbuild.builds.list`  
`cloudbuild.builds.update`  
  
Cloud Tool Results  |  Now GA  |  `cloudtoolresults.executions.create`  
`cloudtoolresults.executions.get`  
`cloudtoolresults.executions.list`  
`cloudtoolresults.executions.update`  
`cloudtoolresults.histories.create`  
`cloudtoolresults.histories.get`  
`cloudtoolresults.histories.list`  
`cloudtoolresults.settings.create`  
`cloudtoolresults.settings.get`  
`cloudtoolresults.settings.update`  
`cloudtoolresults.steps.create`  
`cloudtoolresults.steps.get`  
`cloudtoolresults.steps.list`  
`cloudtoolresults.steps.update`  
  
Compute Engine  |  Now GA  |  `compute.instances.addMaintenancePolicies`  
`compute.instances.removeMaintenancePolicies`  
`compute.maintenancePolicies.create`  
`compute.maintenancePolicies.delete`  
`compute.maintenancePolicies.get`  
`compute.maintenancePolicies.getIamPolicy`  
`compute.maintenancePolicies.list`  
`compute.maintenancePolicies.setIamPolicy`  
`compute.maintenancePolicies.use`  
`compute.targetTcpProxies.create`  
`compute.targetTcpProxies.delete`  
`compute.targetTcpProxies.get`  
`compute.targetTcpProxies.getIamPolicy`  
`compute.targetTcpProxies.list`  
`compute.targetTcpProxies.setIamPolicy`  
`compute.targetTcpProxies.update`  
`compute.targetTcpProxies.use`  
  
Google Kubernetes Engine  |  Added  |  `container.initializerConfigurations.create`  
`container.initializerConfigurations.delete`  
`container.initializerConfigurations.get`  
`container.initializerConfigurations.list`  
`container.initializerConfigurations.update`  
`container.pods.initialize`  
  
Google Kubernetes Engine  |  Now GA  |  `container.deployments.getScale`  
`container.deployments.updateScale`  
  
Dataprep by Trifacta  |  Supported In Custom Roles  |  `dataprep.projects.use`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `iam.roles.create`  
`iam.roles.delete`  
`iam.roles.get`  
`iam.roles.list`  
`iam.roles.undelete`  
`iam.roles.update`  
  
  
## Cloud IAM changes as of 2017-11-10

Service | Change | Description  
---|---|---  
Google Kubernetes Engine  |  Added  |  `container.clusters.getIamPolicy`  
`container.clusters.setIamPolicy`  
  
AI Platform  |  Added  |  `ml.locations.get`  
`ml.locations.list`  
  
Cloud Monitoring  |  Added  |  `monitoring.metricDescriptors.update`  
  
  
## Cloud IAM changes as of 2017-10-27

Service | Change | Description  
---|---|---  
Compute Engine  |  Added  |  `compute.instances.updateShieldedVmConfig`  
  
Identity-Aware Proxy  |  Added  |  `iap.web.getIamPolicy`  
`iap.web.setIamPolicy`  
`iap.webServiceVersions.accessViaIAP`  
`iap.webServiceVersions.getIamPolicy`  
`iap.webServiceVersions.setIamPolicy`  
`iap.webServiceVersions.updateIAP`  
`iap.webServices.getIamPolicy`  
`iap.webServices.setIamPolicy`  
`iap.webServices.updateIAP`  
`iap.webTypes.getIamPolicy`  
`iap.webTypes.setIamPolicy`  
`iap.webTypes.updateIAP`  
  
Service Management  |  Supported In Custom Roles  |  `servicemanagement.services.create`  
`servicemanagement.services.delete`  
`servicemanagement.services.get`  
`servicemanagement.services.getIamPolicy`  
`servicemanagement.services.list`  
`servicemanagement.services.setIamPolicy`  
`servicemanagement.services.update`  
  
  
## Cloud IAM changes as of 2017-10-06

Service | Change | Description  
---|---|---  
Managed Service for Apache Spark  |  Now GA  |  `dataproc.workflowTemplates.create`  
`dataproc.workflowTemplates.delete`  
`dataproc.workflowTemplates.get`  
`dataproc.workflowTemplates.getIamPolicy`  
`dataproc.workflowTemplates.instantiate`  
`dataproc.workflowTemplates.list`  
`dataproc.workflowTemplates.setIamPolicy`  
`dataproc.workflowTemplates.update`  
  
  
## Cloud IAM changes as of 2017-09-22

Service | Change | Description  
---|---|---  
App Engine  |  Added  |  `appengine.memcache.addKey`  
`appengine.memcache.flush`  
`appengine.memcache.get`  
`appengine.memcache.getKey`  
`appengine.memcache.list`  
`appengine.memcache.update`  
  
Cloud SQL  |  Added  |  `cloudsql.instances.demoteMaster`  
  
Cloud SQL  |  Now GA  |  `cloudsql.instances.demoteMaster`  
  
  
## Cloud IAM changes as of 2017-09-08

Service | Change | Description  
---|---|---  
Cloud Run functions  |  Added  |  `cloudfunctions.functions.call`  
`cloudfunctions.functions.create`  
`cloudfunctions.functions.delete`  
`cloudfunctions.functions.get`  
`cloudfunctions.functions.list`  
`cloudfunctions.functions.sourceCodeGet`  
`cloudfunctions.functions.sourceCodeSet`  
`cloudfunctions.functions.update`  
`cloudfunctions.locations.list`  
`cloudfunctions.operations.get`  
`cloudfunctions.operations.list`  
  
Compute Engine  |  Added  |  `compute.instances.setDeletionProtection`  
`compute.targetHttpsProxies.setUrlMap`  
  
Google Kubernetes Engine  |  Added  |  `container.statefulSets.getScale`  
`container.statefulSets.updateScale`  
  
Google Kubernetes Engine  |  Now GA  |  `container.statefulSets.getScale`  
`container.statefulSets.updateScale`  
  
Cloud Run functions  |  Added  |  `dlp.kms.encrypt`  
`dlp.riskAnalysisOperations.cancel`  
`dlp.riskAnalysisOperations.create`  
`dlp.riskAnalysisOperations.get`  
`dlp.riskAnalysisOperations.list`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
