---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/retail/
title: AI Commerce Search API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:11:20.545682+00:00
---

# AI Commerce Search API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/retail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  AI Commerce Search API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for AI Commerce Search API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## AI Commerce Search API roles

Role | Permissions  
---|---  
  
#### Retail Admin 

(`roles/retail.admin`) Full access to Retail api resources.  |  `automlrecommendations.apiKeys.create` `automlrecommendations.apiKeys.delete` `automlrecommendations.catalogItems.*`

  * `automlrecommendations.catalogItems.create`
  * `automlrecommendations.catalogItems.delete`
  * `automlrecommendations.catalogItems.get`
  * `automlrecommendations.catalogItems.list`
  * `automlrecommendations.catalogItems.update`

`automlrecommendations.catalogs.*`

  * `automlrecommendations.catalogs.getStats`
  * `automlrecommendations.catalogs.list`
  * `automlrecommendations.catalogs.update`

`automlrecommendations.eventStores.getStats` `automlrecommendations.events.create` `automlrecommendations.events.list` `automlrecommendations.events.purge` `automlrecommendations.events.rejoin` `automlrecommendations.placements.*`

  * `automlrecommendations.placements.create`
  * `automlrecommendations.placements.delete`
  * `automlrecommendations.placements.getStats`
  * `automlrecommendations.placements.list`

`automlrecommendations.recommendations.*`

  * `automlrecommendations.recommendations.create`
  * `automlrecommendations.recommendations.delete`
  * `automlrecommendations.recommendations.list`
  * `automlrecommendations.recommendations.pause`
  * `automlrecommendations.recommendations.resume`
  * `automlrecommendations.recommendations.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `retail.*`

  * `retail.alertConfigs.get`
  * `retail.alertConfigs.update`
  * `retail.attributesConfigs.addCatalogAttribute`
  * `retail.attributesConfigs.batchRemoveCatalogAttributes`
  * `retail.attributesConfigs.exportCatalogAttributes`
  * `retail.attributesConfigs.get`
  * `retail.attributesConfigs.importCatalogAttributes`
  * `retail.attributesConfigs.removeCatalogAttribute`
  * `retail.attributesConfigs.replaceCatalogAttribute`
  * `retail.attributesConfigs.update`
  * `retail.branches.get`
  * `retail.branches.list`
  * `retail.catalogs.completeQuery`
  * `retail.catalogs.exportAnalyticsMetrics`
  * `retail.catalogs.get`
  * `retail.catalogs.import`
  * `retail.catalogs.list`
  * `retail.catalogs.update`
  * `retail.controls.create`
  * `retail.controls.delete`
  * `retail.controls.export`
  * `retail.controls.get`
  * `retail.controls.import`
  * `retail.controls.list`
  * `retail.controls.update`
  * `retail.experiments.create`
  * `retail.experiments.delete`
  * `retail.experiments.get`
  * `retail.experiments.list`
  * `retail.experiments.loadExperimentLookerDashboard`
  * `retail.experiments.queryTrafficMetrics`
  * `retail.experiments.update`
  * `retail.merchantConfigs.get`
  * `retail.merchantConfigs.update`
  * `retail.merchantControls.approverDelete`
  * `retail.merchantControls.approverGet`
  * `retail.merchantControls.approverList`
  * `retail.merchantControls.approverUpdate`
  * `retail.merchantControls.creatorCreate`
  * `retail.merchantControls.creatorDelete`
  * `retail.merchantControls.creatorGet`
  * `retail.merchantControls.creatorList`
  * `retail.merchantControls.creatorSubmit`
  * `retail.merchantControls.creatorUpdate`
  * `retail.models.create`
  * `retail.models.delete`
  * `retail.models.get`
  * `retail.models.list`
  * `retail.models.pause`
  * `retail.models.resume`
  * `retail.models.tune`
  * `retail.models.update`
  * `retail.operations.get`
  * `retail.operations.list`
  * `retail.placements.predict`
  * `retail.placements.search`
  * `retail.products.create`
  * `retail.products.delete`
  * `retail.products.export`
  * `retail.products.get`
  * `retail.products.import`
  * `retail.products.list`
  * `retail.products.purge`
  * `retail.products.setSponsorship`
  * `retail.products.update`
  * `retail.retailProjects.acceptDataTerms`
  * `retail.retailProjects.get`
  * `retail.servingConfigs.create`
  * `retail.servingConfigs.delete`
  * `retail.servingConfigs.get`
  * `retail.servingConfigs.list`
  * `retail.servingConfigs.predict`
  * `retail.servingConfigs.search`
  * `retail.servingConfigs.update`
  * `retail.userEvents.create`
  * `retail.userEvents.import`
  * `retail.userEvents.purge`
  * `retail.userEvents.rejoin`

`serviceusage.services.list`  
  
#### Retail Editor 

(`roles/retail.editor`) Full access to Retail api resources except purge, rejoin, and setSponsorship.  |  `automlrecommendations.apiKeys.create` `automlrecommendations.apiKeys.delete` `automlrecommendations.catalogItems.*`

  * `automlrecommendations.catalogItems.create`
  * `automlrecommendations.catalogItems.delete`
  * `automlrecommendations.catalogItems.get`
  * `automlrecommendations.catalogItems.list`
  * `automlrecommendations.catalogItems.update`

`automlrecommendations.catalogs.*`

  * `automlrecommendations.catalogs.getStats`
  * `automlrecommendations.catalogs.list`
  * `automlrecommendations.catalogs.update`

`automlrecommendations.eventStores.getStats` `automlrecommendations.events.create` `automlrecommendations.events.list` `automlrecommendations.placements.*`

  * `automlrecommendations.placements.create`
  * `automlrecommendations.placements.delete`
  * `automlrecommendations.placements.getStats`
  * `automlrecommendations.placements.list`

`automlrecommendations.recommendations.*`

  * `automlrecommendations.recommendations.create`
  * `automlrecommendations.recommendations.delete`
  * `automlrecommendations.recommendations.list`
  * `automlrecommendations.recommendations.pause`
  * `automlrecommendations.recommendations.resume`
  * `automlrecommendations.recommendations.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `retail.alertConfigs.*`

  * `retail.alertConfigs.get`
  * `retail.alertConfigs.update`

`retail.attributesConfigs.addCatalogAttribute` `retail.attributesConfigs.exportCatalogAttributes` `retail.attributesConfigs.get` `retail.attributesConfigs.importCatalogAttributes` `retail.attributesConfigs.replaceCatalogAttribute` `retail.attributesConfigs.update` `retail.branches.*`

  * `retail.branches.get`
  * `retail.branches.list`

`retail.catalogs.*`

  * `retail.catalogs.completeQuery`
  * `retail.catalogs.exportAnalyticsMetrics`
  * `retail.catalogs.get`
  * `retail.catalogs.import`
  * `retail.catalogs.list`
  * `retail.catalogs.update`

`retail.controls.*`

  * `retail.controls.create`
  * `retail.controls.delete`
  * `retail.controls.export`
  * `retail.controls.get`
  * `retail.controls.import`
  * `retail.controls.list`
  * `retail.controls.update`

`retail.experiments.*`

  * `retail.experiments.create`
  * `retail.experiments.delete`
  * `retail.experiments.get`
  * `retail.experiments.list`
  * `retail.experiments.loadExperimentLookerDashboard`
  * `retail.experiments.queryTrafficMetrics`
  * `retail.experiments.update`

`retail.merchantConfigs.*`

  * `retail.merchantConfigs.get`
  * `retail.merchantConfigs.update`

`retail.merchantControls.*`

  * `retail.merchantControls.approverDelete`
  * `retail.merchantControls.approverGet`
  * `retail.merchantControls.approverList`
  * `retail.merchantControls.approverUpdate`
  * `retail.merchantControls.creatorCreate`
  * `retail.merchantControls.creatorDelete`
  * `retail.merchantControls.creatorGet`
  * `retail.merchantControls.creatorList`
  * `retail.merchantControls.creatorSubmit`
  * `retail.merchantControls.creatorUpdate`

`retail.models.*`

  * `retail.models.create`
  * `retail.models.delete`
  * `retail.models.get`
  * `retail.models.list`
  * `retail.models.pause`
  * `retail.models.resume`
  * `retail.models.tune`
  * `retail.models.update`

`retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.create` `retail.products.delete` `retail.products.export` `retail.products.get` `retail.products.import` `retail.products.list` `retail.products.update` `retail.retailProjects.get` `retail.servingConfigs.*`

  * `retail.servingConfigs.create`
  * `retail.servingConfigs.delete`
  * `retail.servingConfigs.get`
  * `retail.servingConfigs.list`
  * `retail.servingConfigs.predict`
  * `retail.servingConfigs.search`
  * `retail.servingConfigs.update`

`retail.userEvents.create` `retail.userEvents.import` `serviceusage.services.list`  
  
#### Retail Viewer 

(`roles/retail.viewer`) Grants access to read all resources in Retail.  |  `automlrecommendations.catalogItems.get` `automlrecommendations.catalogItems.list` `automlrecommendations.catalogs.getStats` `automlrecommendations.catalogs.list` `automlrecommendations.eventStores.getStats` `automlrecommendations.events.list` `automlrecommendations.placements.getStats` `automlrecommendations.placements.list` `automlrecommendations.recommendations.list` `resourcemanager.projects.get` `retail.alertConfigs.get` `retail.attributesConfigs.exportCatalogAttributes` `retail.attributesConfigs.get` `retail.branches.*`

  * `retail.branches.get`
  * `retail.branches.list`

`retail.catalogs.completeQuery` `retail.catalogs.exportAnalyticsMetrics` `retail.catalogs.get` `retail.catalogs.list` `retail.controls.export` `retail.controls.get` `retail.controls.list` `retail.experiments.get` `retail.experiments.list` `retail.experiments.loadExperimentLookerDashboard` `retail.experiments.queryTrafficMetrics` `retail.merchantConfigs.get` `retail.models.get` `retail.models.list` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.export` `retail.products.get` `retail.products.list` `retail.retailProjects.get` `retail.servingConfigs.get` `retail.servingConfigs.list` `retail.servingConfigs.predict` `retail.servingConfigs.search` `serviceusage.services.list`  
  
#### Retail Merchant Approver Beta

(`roles/retail.merchantApprover`) Grants access and approval rights to MerchantControls in the merchant console.  |  `automlrecommendations.catalogItems.get` `automlrecommendations.catalogItems.list` `automlrecommendations.catalogs.getStats` `automlrecommendations.catalogs.list` `automlrecommendations.eventStores.getStats` `automlrecommendations.events.list` `automlrecommendations.placements.getStats` `automlrecommendations.placements.list` `automlrecommendations.recommendations.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `retail.alertConfigs.get` `retail.attributesConfigs.exportCatalogAttributes` `retail.attributesConfigs.get` `retail.branches.*`

  * `retail.branches.get`
  * `retail.branches.list`

`retail.catalogs.completeQuery` `retail.catalogs.exportAnalyticsMetrics` `retail.catalogs.get` `retail.catalogs.list` `retail.controls.delete` `retail.controls.export` `retail.controls.get` `retail.controls.list` `retail.controls.update` `retail.experiments.get` `retail.experiments.list` `retail.experiments.loadExperimentLookerDashboard` `retail.experiments.queryTrafficMetrics` `retail.merchantConfigs.*`

  * `retail.merchantConfigs.get`
  * `retail.merchantConfigs.update`

`retail.merchantControls.*`

  * `retail.merchantControls.approverDelete`
  * `retail.merchantControls.approverGet`
  * `retail.merchantControls.approverList`
  * `retail.merchantControls.approverUpdate`
  * `retail.merchantControls.creatorCreate`
  * `retail.merchantControls.creatorDelete`
  * `retail.merchantControls.creatorGet`
  * `retail.merchantControls.creatorList`
  * `retail.merchantControls.creatorSubmit`
  * `retail.merchantControls.creatorUpdate`

`retail.models.get` `retail.models.list` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.export` `retail.products.get` `retail.products.list` `retail.retailProjects.get` `retail.servingConfigs.get` `retail.servingConfigs.list` `retail.servingConfigs.predict` `retail.servingConfigs.search` `retail.servingConfigs.update` `serviceusage.services.list`  
  
#### Retail Merchant Creator Beta

(`roles/retail.merchantCreator`) Grants access to own MerchantControls in the merchant console.  |  `automlrecommendations.catalogItems.get` `automlrecommendations.catalogItems.list` `automlrecommendations.catalogs.getStats` `automlrecommendations.catalogs.list` `automlrecommendations.eventStores.getStats` `automlrecommendations.events.list` `automlrecommendations.placements.getStats` `automlrecommendations.placements.list` `automlrecommendations.recommendations.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `retail.alertConfigs.get` `retail.attributesConfigs.exportCatalogAttributes` `retail.attributesConfigs.get` `retail.branches.*`

  * `retail.branches.get`
  * `retail.branches.list`

`retail.catalogs.completeQuery` `retail.catalogs.exportAnalyticsMetrics` `retail.catalogs.get` `retail.catalogs.list` `retail.controls.export` `retail.controls.get` `retail.controls.list` `retail.experiments.get` `retail.experiments.list` `retail.experiments.loadExperimentLookerDashboard` `retail.experiments.queryTrafficMetrics` `retail.merchantConfigs.get` `retail.merchantControls.creatorCreate` `retail.merchantControls.creatorDelete` `retail.merchantControls.creatorGet` `retail.merchantControls.creatorList` `retail.merchantControls.creatorSubmit` `retail.merchantControls.creatorUpdate` `retail.models.get` `retail.models.list` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.export` `retail.products.get` `retail.products.list` `retail.retailProjects.get` `retail.servingConfigs.get` `retail.servingConfigs.list` `retail.servingConfigs.predict` `retail.servingConfigs.search` `serviceusage.services.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Retail Service Agent 

(`roles/retail.serviceAgent`) Retail service uploads product feeds and user events from Cloud Storage and BigQuery, reports results to the customer Cloud Storage bucket, writes logs to customer projects, and writes and reads Google Cloud Observability metrics for customer projects.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.jobs.list` `bigquery.jobs.update` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `cloudnotifications.activities.list` `dataflow.jobs.*`

  * `dataflow.jobs.cancel`
  * `dataflow.jobs.create`
  * `dataflow.jobs.get`
  * `dataflow.jobs.list`
  * `dataflow.jobs.snapshot`
  * `dataflow.jobs.updateContents`

`dataflow.messages.list` `dataflow.metrics.get` `logging.logEntries.create` `logging.logEntries.route` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.resourceMetadata.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.buckets.create` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## AI Commerce Search API permissions

Permission | Included in roles  
---|---  
  
#### `retail.alertConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.alertConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.attributesConfigs.addCatalogAttribute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.attributesConfigs.batchRemoveCatalogAttributes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `retail.attributesConfigs.exportCatalogAttributes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.attributesConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.attributesConfigs.importCatalogAttributes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.attributesConfigs.removeCatalogAttribute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `retail.attributesConfigs.replaceCatalogAttribute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.attributesConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.branches.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.branches.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.catalogs.completeQuery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.catalogs.exportAnalyticsMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.catalogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.catalogs.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.catalogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.catalogs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.controls.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.controls.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.controls.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.controls.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.controls.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.controls.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.controls.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.experiments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.experiments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.experiments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.experiments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.experiments.loadExperimentLookerDashboard`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.experiments.queryTrafficMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.experiments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.merchantConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.merchantConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.merchantControls.approverDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.merchantControls.approverGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.merchantControls.approverList`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.merchantControls.approverUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.merchantControls.creatorCreate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.merchantControls.creatorDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.merchantControls.creatorGet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.merchantControls.creatorList`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.merchantControls.creatorSubmit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.merchantControls.creatorUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.models.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.models.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.models.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.models.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.models.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `retail.models.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `retail.models.tune`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `retail.models.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.placements.predict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.placements.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.products.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.products.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.products.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.products.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.products.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.products.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.products.purge`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `retail.products.setSponsorship`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `retail.products.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.retailProjects.acceptDataTerms`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `retail.retailProjects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.servingConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.servingConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.servingConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.servingConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.servingConfigs.predict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.servingConfigs.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `retail.servingConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)   
  
#### `retail.userEvents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.userEvents.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `retail.userEvents.purge`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `retail.userEvents.rejoin`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
