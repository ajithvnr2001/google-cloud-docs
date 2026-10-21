---
url: https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services/
title: Services supported by the restricted VIP \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:04.452738+00:00
---

# Services supported by the restricted VIP  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Services supported by the restricted VIP Stay organized with collections  Save and categorize content based on your preferences. 

Use the restricted Virtual IP (VIP) with Private Google Access to provide a private network route for requests to Google Cloud services without exposing the requests to the internet. The restricted VIP supports all of the APIs that a VPC Service Controls can protect. In addition to the services that VPC Service Controls supports, the restricted VIP supports several additional services as dependencies.

The following table provides the list of [Google Cloud services](https://cloud.google.com/terms/services) that the restricted VIP supports.

**Note:** The list of service names listed in the table is not exhaustive.

In addition to the service names listed in the table, the restricted VIP includes some additional endpoints as dependencies of the listed endpoints. For example, Container Registry uses `gcr.io` and `*.gcr.io`.

**Note:** For more information on the stages of support, refer to the [product launch stages](https://cloud.google.com/products/#product-launch-stages). The support stages in this table refer to what level of support the integration of a service with the restricted VIP receives.

The table provides the level of support for each integration. The table includes the following stages of support: 

  * **GA:** This integration is fully supported by the restricted VIP and can be protected by VPC Service Controls perimeters. 
  * **Beta:** This integration receives a beta-stage level of support for the restricted VIP and can be protected by VPC Service Controls perimeters. 
  * **Alpha:** This integration receives an alpha-stage level of support for the restricted VIP and can be protected by VPC Service Controls perimeters for testing purposes only. 
  * **Restricted VIP only:** This service is integrated with the restricted VIP in order to support the use of other services and resources inside a service perimeter. It cannot be added to a perimeter as a protected service. 
  * **Other:** This service has not yet been assigned a support stage. 

Services  |  Support stage   
---|---  
`discovery.googleapis.com` |  Restricted VIP only   
`oauth2.googleapis.com` |  Restricted VIP only   
`openidconnect.googleapis.com` |  Restricted VIP only   
`reauth.googleapis.com` |  Restricted VIP only   
`accessapproval.googleapis.com` |  GA   
`accesscontextintelligence.googleapis.com` |  GA   
`addressvalidation.googleapis.com` |  GA   
`agentregistry.googleapis.com` |  GA   
`aiplatform.googleapis.com` |  GA   
`alloydb.googleapis.com` |  GA   
`analyticshub.googleapis.com` |  GA   
`apigee.googleapis.com` |  GA   
`apigeeconnect.googleapis.com` |  GA   
`apihub.googleapis.com` |  GA   
`apikeys.googleapis.com` |  GA   
`apphub.googleapis.com` |  GA   
`apptopology.googleapis.com` |  GA   
`artifactregistry.googleapis.com` |  GA   
`assuredoss.googleapis.com` |  GA   
`auditmanager.googleapis.com` |  GA   
`automl.googleapis.com` |  GA   
`autoscaling.googleapis.com` |  GA   
`backupdr.googleapis.com` |  GA   
`baremetalsolution.googleapis.com` |  GA   
`batch.googleapis.com` |  GA   
`beyondcorp.googleapis.com` |  GA   
`biglake.googleapis.com` |  GA   
`bigquery.googleapis.com` |  GA   
`bigquerydatapolicy.googleapis.com` |  GA   
`bigquerydatatransfer.googleapis.com` |  GA   
`bigquerymigration.googleapis.com` |  GA   
`bigtable.googleapis.com` |  GA   
`binaryauthorization.googleapis.com` |  GA   
`blockchainnodeengine.googleapis.com` |  GA   
`certificatemanager.googleapis.com` |  GA   
`ces.googleapis.com` |  GA   
`chronicle.googleapis.com` |  GA   
`chronicleservicemanager.googleapis.com` |  GA   
`cloud.googleapis.com` |  GA   
`cloudaicompanion.googleapis.com` |  GA   
`cloudasset.googleapis.com` |  GA   
`cloudbuild.googleapis.com` |  GA   
`cloudcontrolspartner.googleapis.com` |  GA   
`clouddeploy.googleapis.com` |  GA   
`clouderrorreporting.googleapis.com` |  GA   
`cloudfunctions.googleapis.com` |  GA   
`cloudkms.googleapis.com` |  GA   
`cloudprofiler.googleapis.com` |  GA   
`cloudquotas.googleapis.com` |  GA   
`cloudscheduler.googleapis.com` |  GA   
`cloudsearch.googleapis.com` |  GA   
`cloudtasks.googleapis.com` |  GA   
`cloudtrace.googleapis.com` |  GA   
`commerceorggovernance.googleapis.com` |  GA   
`composer.googleapis.com` |  GA   
`compute.googleapis.com` |  GA   
`confidentialcomputing.googleapis.com` |  GA   
`config.googleapis.com` |  GA   
`configdelivery.googleapis.com` |  GA   
`connectgateway.googleapis.com` |  GA   
`connectors.googleapis.com` |  GA   
`contactcenteraiplatform.googleapis.com` |  GA   
`contactcenterinsights.googleapis.com` |  GA   
`container.googleapis.com` |  GA   
`containeranalysis.googleapis.com` |  GA   
`containerfilesystem.googleapis.com` |  GA   
`containerregistry.googleapis.com` |  GA   
`containersecurity.googleapis.com` |  GA   
`containerthreatdetection.googleapis.com` |  GA   
`contentwarehouse.googleapis.com` |  GA   
`databasecenter.googleapis.com` |  GA   
`databaseinsights.googleapis.com` |  GA   
`datacatalog.googleapis.com` |  GA   
`dataflow.googleapis.com` |  GA   
`dataform.googleapis.com` |  GA   
`datafusion.googleapis.com` |  GA   
`datalineage.googleapis.com` |  GA   
`datamigration.googleapis.com` |  GA   
`datapipelines.googleapis.com` |  GA   
`dataplex.googleapis.com` |  GA   
`dataproc.googleapis.com` |  GA   
`datastream.googleapis.com` |  GA   
`developerconnect.googleapis.com` |  GA   
`discoveryengine.googleapis.com` |  GA   
`dlp.googleapis.com` |  GA   
`dns.googleapis.com` |  GA   
`documentai.googleapis.com` |  GA   
`earthengine.googleapis.com` |  GA   
`edgecontainer.googleapis.com` |  GA   
`edgenetwork.googleapis.com` |  GA   
`essentialcontacts.googleapis.com` |  GA   
`eventarc.googleapis.com` |  GA   
`eventarcpublishing.googleapis.com` |  GA   
`file.googleapis.com` |  GA   
`financialservices.googleapis.com` |  GA   
`firebaseappcheck.googleapis.com` |  GA   
`firebaseapphosting.googleapis.com` |  GA   
`firebasedataconnect.googleapis.com` |  GA   
`firebaserules.googleapis.com` |  GA   
`firebasevertexai.googleapis.com` |  GA   
`firestore.googleapis.com` |  GA   
`fpnv.googleapis.com` |  GA   
`gameservices.googleapis.com` |  GA   
`geminidataanalytics.googleapis.com` |  GA   
`gkebackup.googleapis.com` |  GA   
`gkeconnect.googleapis.com` |  GA   
`gkehub.googleapis.com` |  GA   
`gkemulticloud.googleapis.com` |  GA   
`gkeonprem.googleapis.com` |  GA   
`healthcare.googleapis.com` |  GA   
`hypercomputecluster.googleapis.com` |  GA   
`iamcredentials.googleapis.com` |  GA   
`iap.googleapis.com` |  GA   
`iaptunnel.googleapis.com` |  GA   
`identitytoolkit.googleapis.com` |  GA   
`ids.googleapis.com` |  GA   
`integrations.googleapis.com` |  GA   
`kmsinventory.googleapis.com` |  GA   
`krmapihosting.googleapis.com` |  GA   
`kubernetesmetadata.googleapis.com` |  GA   
`language.googleapis.com` |  GA   
`licensemanager.googleapis.com` |  GA   
`livestream.googleapis.com` |  GA   
`logging.googleapis.com` |  GA   
`looker.googleapis.com` |  GA   
`lustre.googleapis.com` |  GA   
`maintenance.googleapis.com` |  GA   
`managedidentities.googleapis.com` |  GA   
`managedkafka.googleapis.com` |  GA   
`memcache.googleapis.com` |  GA   
`memorystore.googleapis.com` |  GA   
`meshca.googleapis.com` |  GA   
`meshconfig.googleapis.com` |  GA   
`metastore.googleapis.com` |  GA   
`microservices.googleapis.com` |  GA   
`migrationcenter.googleapis.com` |  GA   
`ml.googleapis.com` |  GA   
`modelarmor.googleapis.com` |  GA   
`monitoring.googleapis.com` |  GA   
`netapp.googleapis.com` |  GA   
`networkconnectivity.googleapis.com` |  GA   
`networkmanagement.googleapis.com` |  GA   
`networksecurity.googleapis.com` |  GA   
`networkservices.googleapis.com` |  GA   
`notebooks.googleapis.com` |  GA   
`ondemandscanning.googleapis.com` |  GA   
`opsconfigmonitoring.googleapis.com` |  GA   
`oracledatabase.googleapis.com` |  GA   
`orgpolicy.googleapis.com` |  GA   
`osconfig.googleapis.com` |  GA   
`oslogin.googleapis.com` |  GA   
`parallelstore.googleapis.com` |  GA   
`parametermanager.googleapis.com` |  GA   
`policysimulator.googleapis.com` |  GA   
`policytroubleshooter.googleapis.com` |  GA   
`privateca.googleapis.com` |  GA   
`privilegedaccessmanager.googleapis.com` |  GA   
`publicca.googleapis.com` |  GA   
`pubsub.googleapis.com` |  GA   
`pubsublite.googleapis.com` |  GA   
`rapidmigrationassessment.googleapis.com` |  GA   
`recaptchaenterprise.googleapis.com` |  GA   
`recommender.googleapis.com` |  GA   
`redis.googleapis.com` |  GA   
`run.googleapis.com` |  GA   
`secretmanager.googleapis.com` |  GA   
`securesourcemanager.googleapis.com` |  GA   
`securetoken.googleapis.com` |  GA   
`securitycenter.googleapis.com` |  GA   
`securitycentermanagement.googleapis.com` |  GA   
`servicecontrol.googleapis.com` |  GA   
`servicedirectory.googleapis.com` |  GA   
`servicehealth.googleapis.com` |  GA   
`servicenetworking.googleapis.com` |  GA   
`serviceusage.googleapis.com` |  GA   
`spanner.googleapis.com` |  GA   
`speakerid.googleapis.com` |  GA   
`speech.googleapis.com` |  GA   
`sqladmin.googleapis.com` |  GA   
`ssh-serialport.googleapis.com` |  GA   
`storage.googleapis.com` |  GA   
`storagebatchoperations.googleapis.com` |  GA   
`storageinsights.googleapis.com` |  GA   
`storagetransfer.googleapis.com` |  GA   
`sts.googleapis.com` |  GA   
`telemetry.googleapis.com` |  GA   
`texttospeech.googleapis.com` |  GA   
`timeseriesinsights.googleapis.com` |  GA   
`tpu.googleapis.com` |  GA   
`trafficdirector.googleapis.com` |  GA   
`transcoder.googleapis.com` |  GA   
`translate.googleapis.com` |  GA   
`vectorsearch.googleapis.com` |  GA   
`videointelligence.googleapis.com` |  GA   
`videostitcher.googleapis.com` |  GA   
`vision.googleapis.com` |  GA   
`visualinspection.googleapis.com` |  GA   
`vmmigration.googleapis.com` |  GA   
`vmwareengine.googleapis.com` |  GA   
`vpcaccess.googleapis.com` |  GA   
`webrisk.googleapis.com` |  GA   
`websecurityscanner.googleapis.com` |  GA   
`workflows.googleapis.com` |  GA   
`workloadmanager.googleapis.com` |  GA   
`workstations.googleapis.com` |  GA   
`adsdatahub.googleapis.com` |  Beta support   
`assuredworkloads.googleapis.com` |  Beta support   
`businessaicode.googleapis.com` |  Beta support   
`cloudcode.googleapis.com` |  Beta support   
`cloudlocationfinder.googleapis.com` |  Beta support   
`cloudresourcemanager.googleapis.com` |  Beta support   
`cloudsecuritycompliance.googleapis.com` |  Beta support   
`cloudsupport.googleapis.com` |  Beta support   
`designcenter.googleapis.com` |  Beta support   
`dialogflow.googleapis.com` |  Beta support   
`domains.googleapis.com` |  Beta support   
`firebasecrashlytics.googleapis.com` |  Beta support   
`geminicloudassist.googleapis.com` |  Beta support   
`geocoding-backend.googleapis.com` |  Beta support   
`iam.googleapis.com` |  Beta support   
`lifesciences.googleapis.com` |  Beta support   
`places.googleapis.com` |  Beta support   
`retail.googleapis.com` |  Beta support   
`saasservicemgmt.googleapis.com` |  Beta support   
`seclm.googleapis.com` |  Beta support   
`visionai.googleapis.com` |  Beta support   
`workloadidentity.googleapis.com` |  Beta support   
  
## What's next

  * To configure private connectivity, see [Set up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).
  * To configure DNS for `gcr.io`, if you're using Google Kubernetes Engine (GKE), see [Setting up Container Registry for GKE private clusters](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-gke#configure-dns).
  * Learn how to [troubleshoot common VPC Service Controls issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).
  * Learn how to [troubleshoot common issues with different Google Cloud services](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshoot-services-within-perimeter).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
