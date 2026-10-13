---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard
title: REST Resource: projects.locations.instances.legacySoarDashboard \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:33.262491+00:00
---

# REST Resource: projects.locations.instances.legacySoarDashboard  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.legacySoarDashboard Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource
  * Methods



## Resource

There is no persistent data associated with this resource.

## Methods  
  
---  
  
### `[legacyAddOrUpdateDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyAddOrUpdateDashboard)`

|  Adds a new dashboard or updates an existing one (determined by dashboard identifier).  
  
### `[legacyAddOrUpdateDashboardWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyAddOrUpdateDashboardWidget)`

|  Adds a new dashboard widget or updates an existing one (determined by widget identifier).  
  
### `[legacyDeleteDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyDeleteDashboard)`

|  Deletes a dashboard and all its associated widgets.  
  
### `[legacyDeleteDashboardWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyDeleteDashboardWidget)`

|  Deletes a specific dashboard widget.  
  
### `[legacyGetCasesTimeToRespond](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetCasesTimeToRespond)`

|  Returns the average time taken to respond to cases within a specific dashboard, filtered by the provided time range.  
  
### `[legacyGetDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboard)`

|  Returns a detailed data model of a dashboard identified by its ID, including its configuration, allowed environments, and all contained widgets.  
  
### `[legacyGetDashboardCards](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardCards)`

|  Returns a mapping of dashboard IDs to their names for all dashboards accessible by the requesting user.  
  
### `[legacyGetDashboardCustomWidgetCaseIds](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardCustomWidgetCaseIds)`

|  Returns a list of case IDs associated with a custom widget.  
  
### `[legacyGetDashboardPlaybookRuns](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardPlaybookRuns)`

|  Returns a list of recent playbook runs associated with a specific dashboard widget.  
  
### `[legacyGetDashboardPlaybooks](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardPlaybooks)`

|  Returns a list of playbooks that have available data for dashboard reporting.  
  
### `[legacyGetDashboardWidgetCaseIds](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardWidgetCaseIds)`

|  Returns a list of case IDs involved in the widgets presented in the dashboard.  
  
### `[legacyGetDashboardWidgetDefinitions](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardWidgetDefinitions)`

|  Returns all available widget definitions that can be used to construct a dashboard.  
  
### `[legacyGetDashboardWidgetValues](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetDashboardWidgetValues)`

|  Returns the calculated data series and values for a specific dashboard widget.  
  
### `[legacyGetOpenedAndClosedCasesTrends](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetOpenedAndClosedCasesTrends)`

|  Returns the historical trends of opened versus closed cases over a specified time period.  
  
### `[legacyGetPlaybookMonitoring](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyGetPlaybookMonitoring)`

|  Returns a monitoring-focused dashboard view for a specific playbook.  
  
### `[legacyImportDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacyImportDashboard)`

|  Imports a dashboard configuration from a JSON file.  
  
### `[legacySaveDashboardAsReportTemplate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacySaveDashboardAsReportTemplate)`

|  Saves the current dashboard configuration as a report template.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-02 UTC."],[],[]] 
