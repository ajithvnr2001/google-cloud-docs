---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights/
title: Database Insights roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:18.333859+00:00
---

# Database Insights roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Database Insights roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Database Insights. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Database Insights roles

Role | Permissions  
---|---  
  
#### Database Insights Admin 

(`roles/databaseinsights.admin`) Admin role for Database Insights  |  `databaseinsights.*`

  * `databaseinsights.activeQueries.fetch`
  * `databaseinsights.activeQuery.terminate`
  * `databaseinsights.activeSessionHistory.query`
  * `databaseinsights.activitySummary.fetch`
  * `databaseinsights.agentPolicies.createAgentPolicy`
  * `databaseinsights.agentPolicies.deleteAgentPolicy`
  * `databaseinsights.agentPolicies.getAgentPolicy`
  * `databaseinsights.agentPolicies.updateAgentPolicy`
  * `databaseinsights.aggregatedEvents.query`
  * `databaseinsights.aggregatedStats.query`
  * `databaseinsights.clusterEvents.query`
  * `databaseinsights.databaseIssues.troubleshoot`
  * `databaseinsights.dbCenter.query`
  * `databaseinsights.dbPerformance.query`
  * `databaseinsights.genUiAgent.deleteBlueprint`
  * `databaseinsights.genUiAgent.getBlueprint`
  * `databaseinsights.genUiAgent.listBlueprints`
  * `databaseinsights.genUiAgent.query`
  * `databaseinsights.genUiAgent.saveBlueprint`
  * `databaseinsights.goals.applyTaskRemediation`
  * `databaseinsights.goals.createGoal`
  * `databaseinsights.goals.deleteGoal`
  * `databaseinsights.goals.dismissTask`
  * `databaseinsights.goals.fixTask`
  * `databaseinsights.goals.getGoal`
  * `databaseinsights.goals.getTask`
  * `databaseinsights.goals.listGoals`
  * `databaseinsights.goals.listTasks`
  * `databaseinsights.goals.markTaskAsDone`
  * `databaseinsights.goals.restoreTask`
  * `databaseinsights.goals.updateGoal`
  * `databaseinsights.indexRecommendations.query`
  * `databaseinsights.instanceEvents.query`
  * `databaseinsights.locations.get`
  * `databaseinsights.locations.list`
  * `databaseinsights.logs.fetch`
  * `databaseinsights.operations.get`
  * `databaseinsights.performanceIssues.detect`
  * `databaseinsights.performanceIssues.investigate`
  * `databaseinsights.queryMetrics.fetch`
  * `databaseinsights.queryStats.fetch`
  * `databaseinsights.queryTimeSeries.fetch`
  * `databaseinsights.recommendations.query`
  * `databaseinsights.resourceMetadata.fetch`
  * `databaseinsights.resourceRecommendations.query`
  * `databaseinsights.systemMetrics.fetch`
  * `databaseinsights.telemetryConfig.fetch`
  * `databaseinsights.timeSeries.query`
  * `databaseinsights.traces.fetch`
  * `databaseinsights.virtualDbaAgent.createAgentPolicy`
  * `databaseinsights.virtualDbaAgent.createContextService`
  * `databaseinsights.virtualDbaAgent.createGoal`
  * `databaseinsights.virtualDbaAgent.deleteAgentPolicy`
  * `databaseinsights.virtualDbaAgent.deleteContextService`
  * `databaseinsights.virtualDbaAgent.deleteGoal`
  * `databaseinsights.virtualDbaAgent.disable`
  * `databaseinsights.virtualDbaAgent.enable`
  * `databaseinsights.virtualDbaAgent.fetchContextService`
  * `databaseinsights.virtualDbaAgent.getAgentPolicy`
  * `databaseinsights.virtualDbaAgent.getGoal`
  * `databaseinsights.virtualDbaAgent.getTask`
  * `databaseinsights.virtualDbaAgent.listGoals`
  * `databaseinsights.virtualDbaAgent.listTasks`
  * `databaseinsights.virtualDbaAgent.listTodos`
  * `databaseinsights.virtualDbaAgent.query`
  * `databaseinsights.virtualDbaAgent.updateAgentPolicy`
  * `databaseinsights.virtualDbaAgent.updateContextService`
  * `databaseinsights.virtualDbaAgent.updateGoal`
  * `databaseinsights.virtualDbxAgent.query`
  * `databaseinsights.waitEventStats.fetch`
  * `databaseinsights.waitEventTimeSeries.fetch`
  * `databaseinsights.workloadRecommendations.fetch`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Database Insights Editor 

(`roles/databaseinsights.editor`) Editor role for Database Insights  |  `databaseinsights.*`

  * `databaseinsights.activeQueries.fetch`
  * `databaseinsights.activeQuery.terminate`
  * `databaseinsights.activeSessionHistory.query`
  * `databaseinsights.activitySummary.fetch`
  * `databaseinsights.agentPolicies.createAgentPolicy`
  * `databaseinsights.agentPolicies.deleteAgentPolicy`
  * `databaseinsights.agentPolicies.getAgentPolicy`
  * `databaseinsights.agentPolicies.updateAgentPolicy`
  * `databaseinsights.aggregatedEvents.query`
  * `databaseinsights.aggregatedStats.query`
  * `databaseinsights.clusterEvents.query`
  * `databaseinsights.databaseIssues.troubleshoot`
  * `databaseinsights.dbCenter.query`
  * `databaseinsights.dbPerformance.query`
  * `databaseinsights.genUiAgent.deleteBlueprint`
  * `databaseinsights.genUiAgent.getBlueprint`
  * `databaseinsights.genUiAgent.listBlueprints`
  * `databaseinsights.genUiAgent.query`
  * `databaseinsights.genUiAgent.saveBlueprint`
  * `databaseinsights.goals.applyTaskRemediation`
  * `databaseinsights.goals.createGoal`
  * `databaseinsights.goals.deleteGoal`
  * `databaseinsights.goals.dismissTask`
  * `databaseinsights.goals.fixTask`
  * `databaseinsights.goals.getGoal`
  * `databaseinsights.goals.getTask`
  * `databaseinsights.goals.listGoals`
  * `databaseinsights.goals.listTasks`
  * `databaseinsights.goals.markTaskAsDone`
  * `databaseinsights.goals.restoreTask`
  * `databaseinsights.goals.updateGoal`
  * `databaseinsights.indexRecommendations.query`
  * `databaseinsights.instanceEvents.query`
  * `databaseinsights.locations.get`
  * `databaseinsights.locations.list`
  * `databaseinsights.logs.fetch`
  * `databaseinsights.operations.get`
  * `databaseinsights.performanceIssues.detect`
  * `databaseinsights.performanceIssues.investigate`
  * `databaseinsights.queryMetrics.fetch`
  * `databaseinsights.queryStats.fetch`
  * `databaseinsights.queryTimeSeries.fetch`
  * `databaseinsights.recommendations.query`
  * `databaseinsights.resourceMetadata.fetch`
  * `databaseinsights.resourceRecommendations.query`
  * `databaseinsights.systemMetrics.fetch`
  * `databaseinsights.telemetryConfig.fetch`
  * `databaseinsights.timeSeries.query`
  * `databaseinsights.traces.fetch`
  * `databaseinsights.virtualDbaAgent.createAgentPolicy`
  * `databaseinsights.virtualDbaAgent.createContextService`
  * `databaseinsights.virtualDbaAgent.createGoal`
  * `databaseinsights.virtualDbaAgent.deleteAgentPolicy`
  * `databaseinsights.virtualDbaAgent.deleteContextService`
  * `databaseinsights.virtualDbaAgent.deleteGoal`
  * `databaseinsights.virtualDbaAgent.disable`
  * `databaseinsights.virtualDbaAgent.enable`
  * `databaseinsights.virtualDbaAgent.fetchContextService`
  * `databaseinsights.virtualDbaAgent.getAgentPolicy`
  * `databaseinsights.virtualDbaAgent.getGoal`
  * `databaseinsights.virtualDbaAgent.getTask`
  * `databaseinsights.virtualDbaAgent.listGoals`
  * `databaseinsights.virtualDbaAgent.listTasks`
  * `databaseinsights.virtualDbaAgent.listTodos`
  * `databaseinsights.virtualDbaAgent.query`
  * `databaseinsights.virtualDbaAgent.updateAgentPolicy`
  * `databaseinsights.virtualDbaAgent.updateContextService`
  * `databaseinsights.virtualDbaAgent.updateGoal`
  * `databaseinsights.virtualDbxAgent.query`
  * `databaseinsights.waitEventStats.fetch`
  * `databaseinsights.waitEventTimeSeries.fetch`
  * `databaseinsights.workloadRecommendations.fetch`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Database Insights Viewer 

(`roles/databaseinsights.viewer`) Viewer role for Database Insights data  |  `databaseinsights.activeQueries.fetch` `databaseinsights.activeSessionHistory.query` `databaseinsights.activitySummary.fetch` `databaseinsights.agentPolicies.getAgentPolicy` `databaseinsights.aggregatedEvents.query` `databaseinsights.aggregatedStats.query` `databaseinsights.clusterEvents.query` `databaseinsights.databaseIssues.troubleshoot` `databaseinsights.dbCenter.query` `databaseinsights.dbPerformance.query` `databaseinsights.genUiAgent.getBlueprint` `databaseinsights.genUiAgent.listBlueprints` `databaseinsights.genUiAgent.query` `databaseinsights.goals.getGoal` `databaseinsights.goals.getTask` `databaseinsights.goals.listGoals` `databaseinsights.goals.listTasks` `databaseinsights.indexRecommendations.query` `databaseinsights.instanceEvents.query` `databaseinsights.locations.*`

  * `databaseinsights.locations.get`
  * `databaseinsights.locations.list`

`databaseinsights.logs.fetch` `databaseinsights.operations.get` `databaseinsights.performanceIssues.*`

  * `databaseinsights.performanceIssues.detect`
  * `databaseinsights.performanceIssues.investigate`

`databaseinsights.queryMetrics.fetch` `databaseinsights.queryStats.fetch` `databaseinsights.queryTimeSeries.fetch` `databaseinsights.recommendations.query` `databaseinsights.resourceMetadata.fetch` `databaseinsights.resourceRecommendations.query` `databaseinsights.systemMetrics.fetch` `databaseinsights.timeSeries.query` `databaseinsights.traces.fetch` `databaseinsights.virtualDbaAgent.fetchContextService` `databaseinsights.virtualDbaAgent.getAgentPolicy` `databaseinsights.virtualDbaAgent.getGoal` `databaseinsights.virtualDbaAgent.listGoals` `databaseinsights.virtualDbaAgent.listTodos` `databaseinsights.virtualDbaAgent.query` `databaseinsights.virtualDbxAgent.query` `databaseinsights.waitEventStats.fetch` `databaseinsights.waitEventTimeSeries.fetch` `databaseinsights.workloadRecommendations.fetch` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Database Insights assistant viewer Beta

(`roles/databaseinsights.assistantViewer`) Viewer role for Database Insights assistant data  |  `databaseinsights.performanceIssues.*`

  * `databaseinsights.performanceIssues.detect`
  * `databaseinsights.performanceIssues.investigate`

  
  
#### Events Service viewer 

(`roles/databaseinsights.eventsViewer`) Viewer role for Events Service data  |  `databaseinsights.aggregatedEvents.query` `databaseinsights.clusterEvents.query` `databaseinsights.instanceEvents.query`  
  
#### Database Insights intelligence viewer Beta

(`roles/databaseinsights.intelligenceViewer`) Viewer role for Database Insights intelligence data  |  `databaseinsights.databaseIssues.troubleshoot` `databaseinsights.dbCenter.query` `databaseinsights.dbPerformance.query` `databaseinsights.indexRecommendations.query` `databaseinsights.logs.fetch` `databaseinsights.queryMetrics.fetch` `databaseinsights.queryStats.fetch` `databaseinsights.queryTimeSeries.fetch` `databaseinsights.resourceMetadata.fetch` `databaseinsights.systemMetrics.fetch` `databaseinsights.traces.fetch` `databaseinsights.waitEventStats.fetch` `databaseinsights.waitEventTimeSeries.fetch`  
  
#### Database Insights monitoring viewer 

(`roles/databaseinsights.monitoringViewer`) Viewer role for Database Insights monitoring data  |  `databaseinsights.activeQueries.fetch` `databaseinsights.activeSessionHistory.query` `databaseinsights.activitySummary.fetch` `databaseinsights.aggregatedStats.query` `databaseinsights.locations.*`

  * `databaseinsights.locations.get`
  * `databaseinsights.locations.list`

`databaseinsights.queryStats.fetch` `databaseinsights.queryTimeSeries.fetch` `databaseinsights.timeSeries.query` `databaseinsights.waitEventStats.fetch` `databaseinsights.waitEventTimeSeries.fetch` `databaseinsights.workloadRecommendations.fetch` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Database Insights performing operations 

(`roles/databaseinsights.operationsAdmin`) Admin role for performing Database Insights operations  |  `databaseinsights.activeQuery.terminate` `databaseinsights.operations.get` `databaseinsights.virtualDbaAgent.disable` `databaseinsights.virtualDbaAgent.enable`  
  
#### Database Insights recommendation viewer 

(`roles/databaseinsights.recommendationViewer`) Viewer role for Database Insights recommendation data  |  `databaseinsights.indexRecommendations.query` `databaseinsights.locations.*`

  * `databaseinsights.locations.get`
  * `databaseinsights.locations.list`

`databaseinsights.recommendations.query` `databaseinsights.resourceRecommendations.query` `databaseinsights.workloadRecommendations.fetch` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Telemetry Config Fetcher Beta

(`roles/databaseinsights.telemetryConfigFetcher`) Role used to fetch telemetry configuration.  |  `databaseinsights.telemetryConfig.fetch`  
  
#### Database Insights virtual Dbx viewer Beta

(`roles/databaseinsights.virtualDbxViewer`) Viewer role for Database Insights virtual Dbx data  |  `databaseinsights.virtualDbxAgent.query`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Database Insights Service Agent 

(`roles/databaseinsights.serviceAgent`) Default role for the Database Insights service agent.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `alloydb.clusters.get` `alloydb.clusters.list` `alloydb.databases.list` `alloydb.instances.get` `alloydb.instances.list` `alloydb.locations.*`

  * `alloydb.locations.get`
  * `alloydb.locations.list`

`alloydb.operations.get` `alloydb.operations.list` `alloydb.supportedDatabaseFlags.list` `bigtable.appProfiles.list` `bigtable.backups.list` `bigtable.clusters.get` `bigtable.clusters.list` `bigtable.instances.get` `bigtable.instances.list` `bigtable.locations.list` `bigtable.tables.get` `bigtable.tables.list` `cloudsql.backupRuns.list` `cloudsql.databases.get` `cloudsql.databases.list` `cloudsql.instances.get` `cloudsql.instances.list` `cloudtrace.traces.patch` `databasecenter.databaseGroups.list` `databasecenter.fleetStats.list` `databasecenter.userLabels.list` `databasecenter.userTags.list` `databaseinsights.agentPolicies.*`

  * `databaseinsights.agentPolicies.createAgentPolicy`
  * `databaseinsights.agentPolicies.deleteAgentPolicy`
  * `databaseinsights.agentPolicies.getAgentPolicy`
  * `databaseinsights.agentPolicies.updateAgentPolicy`

`databaseinsights.databaseIssues.troubleshoot` `databaseinsights.dbCenter.query` `databaseinsights.dbPerformance.query` `databaseinsights.goals.createGoal` `databaseinsights.goals.deleteGoal` `databaseinsights.goals.dismissTask` `databaseinsights.goals.fixTask` `databaseinsights.goals.getGoal` `databaseinsights.goals.getTask` `databaseinsights.goals.listGoals` `databaseinsights.goals.listTasks` `databaseinsights.goals.markTaskAsDone` `databaseinsights.goals.restoreTask` `databaseinsights.goals.updateGoal` `databaseinsights.indexRecommendations.query` `databaseinsights.logs.fetch` `databaseinsights.queryMetrics.fetch` `databaseinsights.queryStats.fetch` `databaseinsights.queryTimeSeries.fetch` `databaseinsights.resourceMetadata.fetch` `databaseinsights.systemMetrics.fetch` `databaseinsights.traces.fetch` `databaseinsights.virtualDbaAgent.query` `databaseinsights.virtualDbxAgent.query` `databaseinsights.waitEventStats.fetch` `databaseinsights.waitEventTimeSeries.fetch` `datastore.backupSchedules.list` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.locations.list` `datastore.operations.get` `datastore.operations.list` `discoveryengine.collections.get` `discoveryengine.dataConnectors.acquireAccessToken` `discoveryengine.dataConnectors.get` `logging.logEntries.create` `logging.logEntries.list` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricsScopes.link` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`resourcemanager.projects.get` `serviceusage.operations.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.use` `spanner.backupOperations.list` `spanner.databaseOperations.list` `spanner.databaseRoles.list` `spanner.databases.get` `spanner.databases.list` `spanner.instanceConfigs.get` `spanner.instanceConfigs.list` `spanner.instanceOperations.list` `spanner.instancePartitions.list` `spanner.instances.get` `spanner.instances.list` `telemetry.traces.write`  
  
## Database Insights permissions

Permission | Included in roles  
---|---  
  
#### `databaseinsights.activeQueries.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.activeQuery.terminate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights performing operations](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.operationsAdmin) (`roles/databaseinsights.operationsAdmin`)   
  
#### `databaseinsights.activeSessionHistory.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.activitySummary.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.agentPolicies.createAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.agentPolicies.deleteAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.agentPolicies.getAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.agentPolicies.updateAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.aggregatedEvents.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Events Service viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.eventsViewer) (`roles/databaseinsights.eventsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.aggregatedStats.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.clusterEvents.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Events Service viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.eventsViewer) (`roles/databaseinsights.eventsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.databaseIssues.troubleshoot`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.dbCenter.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.dbPerformance.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.genUiAgent.deleteBlueprint`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.genUiAgent.getBlueprint`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.genUiAgent.listBlueprints`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.genUiAgent.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.genUiAgent.saveBlueprint`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.goals.applyTaskRemediation`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.goals.createGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.deleteGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.dismissTask`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.fixTask`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.getGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.getTask`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.listGoals`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.listTasks`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.markTaskAsDone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.restoreTask`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.goals.updateGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.indexRecommendations.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Database Insights recommendation viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.recommendationViewer) (`roles/databaseinsights.recommendationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.instanceEvents.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Events Service viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.eventsViewer) (`roles/databaseinsights.eventsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Database Insights recommendation viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.recommendationViewer) (`roles/databaseinsights.recommendationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Database Insights recommendation viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.recommendationViewer) (`roles/databaseinsights.recommendationViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.logs.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights performing operations](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.operationsAdmin) (`roles/databaseinsights.operationsAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.performanceIssues.detect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights assistant viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.assistantViewer) (`roles/databaseinsights.assistantViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.performanceIssues.investigate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights assistant viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.assistantViewer) (`roles/databaseinsights.assistantViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.queryMetrics.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.queryStats.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.queryTimeSeries.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.recommendations.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights recommendation viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.recommendationViewer) (`roles/databaseinsights.recommendationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.resourceMetadata.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.resourceRecommendations.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights recommendation viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.recommendationViewer) (`roles/databaseinsights.recommendationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.systemMetrics.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.telemetryConfig.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Telemetry Config Fetcher](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.telemetryConfigFetcher) (`roles/databaseinsights.telemetryConfigFetcher`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.timeSeries.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.traces.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.virtualDbaAgent.createAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.createContextService`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.createGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.deleteAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.deleteContextService`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.deleteGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights performing operations](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.operationsAdmin) (`roles/databaseinsights.operationsAdmin`)   
  
#### `databaseinsights.virtualDbaAgent.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights performing operations](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.operationsAdmin) (`roles/databaseinsights.operationsAdmin`)   
  
#### `databaseinsights.virtualDbaAgent.fetchContextService`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.getAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.getGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.getTask`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.listGoals`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.listTasks`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.listTodos`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `databaseinsights.virtualDbaAgent.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.virtualDbaAgent.updateAgentPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.updateContextService`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbaAgent.updateGoal`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)   
  
#### `databaseinsights.virtualDbxAgent.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights virtual Dbx viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.virtualDbxViewer) (`roles/databaseinsights.virtualDbxViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.waitEventStats.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.waitEventTimeSeries.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights intelligence viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.intelligenceViewer) (`roles/databaseinsights.intelligenceViewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 

  
  
#### `databaseinsights.workloadRecommendations.fetch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Database Insights Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.admin) (`roles/databaseinsights.admin`)  [Database Insights Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.editor) (`roles/databaseinsights.editor`)  [Database Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)  [Database Insights monitoring viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) (`roles/databaseinsights.monitoringViewer`)  [Database Insights recommendation viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.recommendationViewer) (`roles/databaseinsights.recommendationViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
