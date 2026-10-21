---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-iam-permissions/
title: Prepare IAM permissions \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:01.564318+00:00
---

# Prepare IAM permissions  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Prepare IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped offers Identity and Access Management (IAM) for granular access to specific Distributed Cloud resources and prevents unwanted access to other resources. IAM operates on the security principle of least privilege and controls who can access given resources using IAM roles and permissions.

A role is a collection of specific permissions mapped to certain actions on resources and assigned to individual subjects, such as users, groups of users, or service accounts. Therefore, you must have the proper IAM roles and permissions to use monitoring and logging services on Distributed Cloud.

IAM on Distributed Cloud offers the following access levels for permissions:

  * **Organization-level roles** : Grant a subject with permissions at the _organization_ level to deploy custom resources across all project namespaces of the global API server and enable services in all projects of your entire organization.
  * **Project-level roles** : Grant a subject with permissions at the _project_ level to deploy custom resources into the project namespace of the global API server and enable services only in your project namespace.

**Important:** The project namespace for logging and monitoring resources of Platform Administrators in the global API server is the `platform-obs` namespace. When granting the roles described on this page, create the role bindings in the `platform-obs` namespace using the kubeconfig file for the `org-management` cluster.

If you can't access or use a monitoring or logging service, contact your administrator to grant you the necessary roles. Request the appropriate permissions from your Project IAM Admin for a given project. If you require permissions at the organization level, ask your Organization IAM Admin instead.




This page describes all the roles and their respective permissions for using monitoring and logging services.

## Predefined roles at the organization level

Request the appropriate permissions from your Organization IAM Admin to set up logging and monitoring in an organization and manage the lifecycle of a project that uses observability services.

To grant team members organization-wide resource access, assign roles by creating role bindings on the global API server using its kubeconfig file. To grant permissions or receive role access to resources at the organization level, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

**Important:** Organization-level roles let you deploy custom resources across all project namespaces of the global API server and enable services in all projects of your entire organization.

### Monitoring resources

The following table provides details about the permissions assigned to each predefined role for monitoring resources:

Role name | Kubernetes resource name | Permission description  
---|---|---  
Dashboard PA Creator | `dashboard-pa-creator` | Create `Dashboard` custom resources.  
Dashboard PA Editor | `dashboard-pa-editor` | Edit or modify `Dashboard` custom resources.  
Dashboard PA Viewer | `dashboard-pa-viewer` | View `Dashboard` custom resources.  
MonitoringRule PA Creator | `monitoringrule-pa-creator` | Create `MonitoringRule` custom resources.  
MonitoringRule PA Editor | `monitoringrule-pa-editor` | Edit or modify `MonitoringRule` custom resources.  
MonitoringRule PA Viewer | `monitoringrule-pa-viewer` | View `MonitoringRule` custom resources.  
MonitoringTarget PA Creator | `monitoringtarget-pa-creator` | Create `MonitoringTarget` custom resources.  
MonitoringTarget PA Editor | `monitoringtarget-pa-editor` | Edit or modify `MonitoringTarget` custom resources.  
MonitoringTarget PA Viewer | `monitoringtarget-pa-viewer` | View `MonitoringTarget` custom resources.  
ObservabilityPipeline PA Creator | `observabilitypipeline-pa-creator` | Create `ObservabilityPipeline` custom resources.  
ObservabilityPipeline PA Editor | `observabilitypipeline-pa-editor` | Edit or modify `ObservabilityPipeline` custom resources.  
ObservabilityPipeline PA Viewer | `observabilitypipeline-pa-viewer` | View `ObservabilityPipeline` custom resources.  
Organization Grafana Viewer | `organization-grafana-viewer` | Visualize organization-related observability data on dashboards of the Grafana monitoring instance.  
  
### Logging resources

The following table provides details about the permissions assigned to each predefined role for logging resources:

Role name | Kubernetes resource name | Permission description  
---|---|---  
LoggingRule PA Creator | `loggingrule-pa-creator` | Create `LoggingRule` custom resources.  
LoggingRule PA Editor | `loggingrule-pa-editor` | Edit or modify `LoggingRule` custom resources.  
LoggingRule PA Viewer | `loggingrule-pa-viewer` | View `LoggingRule` custom resources.  
LoggingTarget PA Creator | `loggingtarget-pa-creator` | Create `LoggingTarget` custom resources.  
LoggingTarget PA Editor | `loggingtarget-pa-editor` | Edit or modify `LoggingTarget` custom resources.  
LoggingTarget PA Viewer | `loggingtarget-pa-viewer` | View `LoggingTarget` custom resources.  
  
## Predefined roles at the project level

Request the appropriate permissions from your Project IAM Admin to use logging and monitoring services in a project. All roles must bind to the project namespace where you are using the service.

To grant team members project-wide resource access, assign roles by creating role bindings on the global API server using its kubeconfig file. To grant permissions or receive role access to resources at the project level, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

**Important:** Project-level roles let you deploy custom resources into the project namespace of the global API server and enable services only in your project namespace.

### Monitoring resources

The following table provides details about the permissions assigned to each predefined role for monitoring resources:

Role name | Kubernetes resource name | Permission description  
---|---|---  
ConfigMap Creator | `configmap-creator` | Create `ConfigMap` objects in the project namespace.  
Dashboard Editor | `dashboard-editor` | Edit or modify `Dashboard` custom resources in the project namespace.  
Dashboard Viewer | `dashboard-viewer` | View `Dashboard` custom resources in the project namespace.  
MonitoringRule Editor | `monitoringrule-editor` | Edit or modify `MonitoringRule` custom resources in the project namespace.  
MonitoringRule Viewer | `monitoringrule-viewer` | View `MonitoringRule` custom resources in the project namespace.  
MonitoringTarget Editor | `monitoringtarget-editor` | Edit or modify `MonitoringTarget` custom resources in the project namespace.  
MonitoringTarget Viewer | `monitoringtarget-viewer` | View `MonitoringTarget` custom resources in the project namespace.  
ObservabilityPipeline Editor | `observabilitypipeline-editor` | Edit or modify `ObservabilityPipeline` custom resources in the project namespace.  
ObservabilityPipeline Viewer | `observabilitypipeline-viewer` | View `ObservabilityPipeline` custom resources in the project namespace.  
Project Cortex Alertmanager Editor | `project-cortex-alertmanager-editor` | Edit the Cortex Alertmanager instance in the project namespace.  
Project Cortex Alertmanager Viewer | `project-cortex-alertmanager-viewer` | Access the Cortex Alertmanager instance in the project namespace.  
Project Cortex Prometheus Viewer | `project-cortex-prometheus-viewer` | Access the Cortex Prometheus instance in the project namespace.  
Project Grafana Viewer | `project-grafana-viewer` | Visualize project-related observability data on dashboards of the Grafana monitoring instance.  
  
### Logging resources

The following table provides details about the permissions assigned to each predefined role for logging resources:

Role name | Kubernetes resource name | Permission description  
---|---|---  
Audit Logs Platform Restore Bucket Creator | `audit-logs-platform-restore-bucket-creator` | Create backup buckets to restore the platform audit logs.  
Audit Logs Platform Bucket Viewer | `audit-logs-platform-bucket-viewer` | View backup buckets of platform audit logs.  
Audit Logging Target Monitor | `auditloggingtarget-monitor` | Debugging `AuditLoggingTarget` custom resource.  
LoggingRule Creator | `loggingrule-creator` | Create `LoggingRule` custom resources in the project namespace.  
LoggingRule Editor | `loggingrule-editor` | Edit or modify `LoggingRule` custom resources in the project namespace.  
LoggingRule Viewer | `loggingrule-viewer` | View `LoggingRule` custom resources in the project namespace.  
LoggingTarget Creator | `loggingtarget-creator` | Create `LoggingTarget` custom resources in the project namespace.  
LoggingTarget Editor | `loggingtarget-editor` | Edit or modify `LoggingTarget` custom resources in the project namespace.  
LoggingTarget Viewer | `loggingtarget-viewer` | View `LoggingTarget` custom resources in the project namespace.  
Log Query API Querier | `log-query-api-querier` | Access the Log Query API to query logs.  
SIEM Export Org Creator | `siemexport-org-creator` | Create `SIEMOrgForwarder` custom resources in the project namespace.  
SIEM Export Org Editor | `siemexport-org-editor` | Edit or modify `SIEMOrgForwarder` custom resources in the project namespace.  
SIEM Export Org Viewer | `siemexport-org-viewer` | View `SIEMOrgForwarder` custom resources in the project namespace.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
