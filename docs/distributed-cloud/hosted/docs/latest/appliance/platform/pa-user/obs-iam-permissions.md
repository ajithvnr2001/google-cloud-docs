---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions/
title: Prepare IAM permissions \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:45.362296+00:00
---

# Prepare IAM permissions  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Prepare IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance offers Identity and Access Management (IAM) for granular access to specific GDC air-gapped appliance resources and prevents unwanted access to other resources. IAM operates on the security principle of least privilege and controls who can access given resources using IAM roles and permissions.

A role is a collection of specific permissions mapped to certain actions on resources and assigned to individual subjects, such as users, groups of users, or service accounts. Therefore, you must have the proper IAM roles and permissions to use monitoring and logging services on GDC air-gapped appliance.

## IAM permissions for Infrastructure Operator

IAM on GDC air-gapped appliance offers predefined role types that you can obtain on the following levels of access:

  * **Management API server** : Grant a subject with permissions to manage custom resources at the project level in the project namespace of the Management API server where they want to use logging and monitoring services.
  * **Root admin cluster** : Grant a subject with permissions to manage infrastructure resources in the root admin cluster.

**Important:** The project namespace for logging and monitoring resources of Infrastructure Operators in the Management API server is the `infra-obs` namespace.

If you can't access or use a monitoring or logging service, contact your administrator to grant you the necessary roles. Request the appropriate permissions from your Security Admin.

This page describes all the roles and their respective permissions for using monitoring and logging services.

### Predefined roles at the project level

Request the appropriate permissions from your Security Admin to set up logging and monitoring in the project namespace of the Management API server where you want to manage the lifecycle of observability services.

All roles must bind to the project namespace of the Management API server where you are using the service. To grant team members resource access, assign roles by creating role bindings on the Management API server using its kubeconfig file. To grant permissions or receive role access, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings).

For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-user/iam/role-descriptions).

#### Monitoring resources

The following table provides details about the permissions assigned to each predefined role for monitoring resources:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
ConfigMap Creator | `configmap-creator` | Create `ConfigMap` objects in the project namespace. | `Role`  
Dashboard IO Creator | `dashboard-io-creator` | Create `Dashboard` custom resources in the project namespace. | `ClusterRole`  
Dashboard IO Editor | `dashboard-io-editor` | Edit or modify `Dashboard` custom resources in the project namespace. | `ClusterRole`  
Dashboard IO Viewer | `dashboard-io-viewer` | View `Dashboard` custom resources in the project namespace. | `ClusterRole`  
MonitoringRule IO Creator | `monitoringrule-io-creator` | Create `MonitoringRule` custom resources in the project namespace. | `ClusterRole`  
MonitoringRule IO Editor | `monitoringrule-io-editor` | Edit or modify `MonitoringRule` custom resources in the project namespace. | `ClusterRole`  
MonitoringRule IO Viewer | `monitoringrule-io-viewer` | View `MonitoringRule` custom resources in the project namespace. | `ClusterRole`  
MonitoringTarget IO Creator | `monitoringtarget-io-creator` | Create `MonitoringTarget` custom resources in the project namespace. | `ClusterRole`  
MonitoringTarget IO Editor | `monitoringtarget-io-editor` | Edit or modify `MonitoringTarget` custom resources in the project namespace. | `ClusterRole`  
MonitoringTarget IO Viewer | `monitoringtarget-io-viewer` | View `MonitoringTarget` custom resources in the project namespace. | `ClusterRole`  
ObservabilityPipeline IO Creator | `observabilitypipeline-io-creator` | Create `ObservabilityPipeline` custom resources in the project namespace. | `ClusterRole`  
ObservabilityPipeline IO Editor | `observabilitypipeline-io-editor` | Edit or modify `ObservabilityPipeline` custom resources in the project namespace. | `ClusterRole`  
ObservabilityPipeline IO Viewer | `observabilitypipeline-io-viewer` | View `ObservabilityPipeline` custom resources in the project namespace. | `ClusterRole`  
Project Cortex Alertmanager Editor | `project-cortex-alertmanager-editor` | Edit the Cortex Alertmanager instance in the project namespace. | `Role`  
Project Cortex Alertmanager Viewer | `project-cortex-alertmanager-viewer` | Access the Cortex Alertmanager instance in the project namespace. | `Role`  
Project Cortex Prometheus Viewer | `project-cortex-prometheus-viewer` | Access the Cortex Prometheus instance in the project namespace. | `Role`  
Project Grafana Viewer | `project-grafana-viewer` | Visualize project-related observability data on dashboards of the Grafana monitoring instance. | `Role`  
ServiceLevelObjective Viewer | `servicelevelobjective-viewer` | Visualize `ServiceLevelObjective` custom resources in the Management API server. | `ClusterRole`  
  
#### Logging resources

The following table provides details about the permissions assigned to each predefined role for logging resources:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
AuditLoggingTarget IO Creator | `auditloggingtarget-io-creator` | Create `AuditLoggingTarget` custom resources in the project namespace. | `ClusterRole`  
AuditLoggingTarget IO Editor | `auditloggingtarget-io-editor` | Edit or modify `AuditLoggingTarget` custom resources in the project namespace. | `ClusterRole`  
AuditLoggingTarget IO Viewer | `auditloggingtarget-io-viewer` | View `AuditLoggingTarget` custom resources in the project namespace. | `ClusterRole`  
Audit Logs Backup Restore Creator | `audit-logs-backup-restore-creator` | Create a backup transfer job configuration and restore audit logs. | `Role`  
Audit Logs Backup Restore Editor | `audit-logs-backup-restore-editor` | Edit the backup transfer job configuration and restore audit logs. | `Role`  
Audit Logs Infra Bucket Viewer | `audit-logs-infra-bucket-viewer` | View backup buckets of infrastructure audit logs. | `Role`  
FluentBit IO Creator | `fluentbit-io-creator` | Create `FluentBit` custom resources in the project namespace. | `ClusterRole`  
FluentBit IO Editor | `fluentbit-io-editor` | Edit or modify `FluentBit` custom resources in the project namespace. | `ClusterRole`  
FluentBit IO Viewer | `fluentbit-io-viewer` | View `FluentBit` custom resources in the project namespace. | `ClusterRole`  
LogCollector IO Creator | `logcollector-io-creator` | Create `LogCollector` custom resources in the project namespace. | `ClusterRole`  
LogCollector IO Editor | `logcollector-io-editor` | Edit or modify `LogCollector` custom resources in the project namespace. | `ClusterRole`  
LogCollector IO Viewer | `logcollector-io-viewer` | View `LogCollector` custom resources in the project namespace. | `ClusterRole`  
LoggingRule IO Creator | `loggingrule-io-creator` | Create `LoggingRule` custom resources in the project namespace. | `ClusterRole`  
LoggingRule IO Editor | `loggingrule-io-editor` | Edit or modify `LoggingRule` custom resources in the project namespace. | `ClusterRole`  
LoggingRule IO Viewer | `loggingrule-io-viewer` | View `LoggingRule` custom resources in the project namespace. | `ClusterRole`  
LoggingTarget IO Creator | `loggingtarget-io-creator` | Create `LoggingTarget` custom resources in the project namespace. | `ClusterRole`  
LoggingTarget IO Editor | `loggingtarget-io-editor` | Edit or modify `LoggingTarget` custom resources in the project namespace. | `ClusterRole`  
LoggingTarget IO Viewer | `loggingtarget-io-viewer` | View `LoggingTarget` custom resources in the project namespace. | `ClusterRole`  
  
### Predefined roles in the root admin cluster

Request the appropriate permissions from your Security Admin to use logging and monitoring services in the root admin cluster.

To grant team members resource access, assign roles by creating role bindings on the root admin cluster using its kubeconfig file. To grant permissions or receive role access, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings).

For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-user/iam/role-descriptions).

#### Monitoring resources

The following table provides details about the permissions assigned to each predefined role for monitoring resources:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
Dashboard Creator | `dashboard-creator` | Create `Dashboard` custom resources in the root admin cluster. | `ClusterRole`  
Dashboard Editor | `dashboard-editor` | Edit or modify `Dashboard` custom resources in the root admin cluster. | `ClusterRole`  
Dashboard Viewer | `dashboard-viewer` | View `Dashboard` custom resources in the root admin cluster. | `ClusterRole`  
Grafana Viewer | `grafana-viewer` | Visualize observability data on dashboards of the Grafana monitoring instance in the root admin cluster. | `ClusterRole`  
MonitoringRule Creator | `monitoringrule-creator` | Create `MonitoringRule` custom resources in the root admin cluster. | `ClusterRole`  
MonitoringRule Editor | `monitoringrule-editor` | Edit or modify `MonitoringRule` custom resources in the root admin cluster. | `ClusterRole`  
MonitoringRule Viewer | `monitoringrule-viewer` | View `MonitoringRule` custom resources in the root admin cluster. | `ClusterRole`  
MonitoringTarget Creator | `monitoringtarget-creator` | Create `MonitoringTarget` custom resources in the root admin cluster. | `ClusterRole`  
MonitoringTarget Editor | `monitoringtarget-editor` | Edit or modify `MonitoringTarget` custom resources in the root admin cluster. | `ClusterRole`  
MonitoringTarget Viewer | `monitoringtarget-viewer` | View `MonitoringTarget` custom resources in the root admin cluster. | `ClusterRole`  
ObservabilityPipeline Creator | `observabilitypipeline-creator` | Create `ObservabilityPipeline` custom resources in the root admin cluster. | `ClusterRole`  
ObservabilityPipeline Editor | `observabilitypipeline-editor` | Edit or modify `ObservabilityPipeline` custom resources in the root admin cluster. | `ClusterRole`  
ObservabilityPipeline Viewer | `observabilitypipeline-viewer` | View `ObservabilityPipeline` custom resources in the root admin cluster. | `ClusterRole`  
Root Cortex Alertmanager Editor | `root-cortex-alertmanager-editor` | Edit the Cortex Alertmanager instance in the root admin cluster. | `Role`  
Root Cortex Alertmanager Viewer | `root-cortex-alertmanager-viewer` | Access the Cortex Alertmanager instance in the root admin cluster. | `Role`  
Root Cortex Prometheus Viewer | `root-cortex-prometheus-viewer` | Access the Cortex Prometheus instance in the root admin cluster. | `Role`  
ServiceLevelObjective Viewer | `servicelevelobjective-viewer` | Visualize `ServiceLevelObjective` custom resources in the root admin cluster. | `ClusterRole`  
  
#### Logging resources

The following table provides details about the permissions assigned to each predefined role for logging resources:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
AuditLoggingTarget Creator | `auditloggingtarget-creator` | Create `AuditLoggingTarget` custom resources in the root admin cluster. | `ClusterRole`  
AuditLoggingTarget Editor | `auditloggingtarget-editor` | Edit or modify `AuditLoggingTarget` custom resources in the root admin cluster. | `ClusterRole`  
AuditLoggingTarget Viewer | `auditloggingtarget-viewer` | View `AuditLoggingTarget` custom resources in the root admin cluster. | `ClusterRole`  
Audit Logs Backup Restore Creator | `audit-logs-backup-restore-creator` | Create a backup transfer job configuration and restore audit logs. | `Role`  
Audit Logs Backup Restore Editor | `audit-logs-backup-restore-editor` | Edit the backup transfer job configuration and restore audit logs. | `Role`  
Audit Logs Infra Bucket Viewer | `audit-logs-infra-bucket-viewer` | View backup buckets of infrastructure audit logs. | `Role`  
FluentBit Creator | `fluentbit-creator` | Create `FluentBit` custom resources in the root admin cluster. | `ClusterRole`  
FluentBit Editor | `fluentbit-editor` | Edit or modify `FluentBit` custom resources in the root admin cluster. | `ClusterRole`  
FluentBit Viewer | `fluentbit-viewer` | View `FluentBit` custom resources in the root admin cluster. | `ClusterRole`  
LogCollector Creator | `logcollector-creator` | Create `LogCollector` custom resources in the root admin cluster. | `ClusterRole`  
LogCollector Editor | `logcollector-editor` | Edit or modify `LogCollector` custom resources in the root admin cluster. | `ClusterRole`  
LogCollector Viewer | `logcollector-viewer` | View `LogCollector` custom resources in the root admin cluster. | `ClusterRole`  
LoggingRule Creator | `loggingrule-creator` | Create `LoggingRule` custom resources in the root admin cluster. | `ClusterRole`  
LoggingRule Editor | `loggingrule-editor` | Edit or modify `LoggingRule` custom resources in the root admin cluster. | `ClusterRole`  
LoggingRule Viewer | `loggingrule-viewer` | View `LoggingRule` custom resources in the root admin cluster. | `ClusterRole`  
  
## IAM permissions for Platform Administrator (PA) and Application Operator

IAM on GDC air-gapped appliance offers the following two predefined PA/AO role types, depending on the level of access you need:

  * **`ClusterRole`** : Grant a subject with permissions at the _organization_ level. Organization-level roles let you deploy custom resources across all project namespaces of the Management API server and enable services in all projects of your entire organization.
  * **`Role`** : Grant a subject with permissions at the _project_ level by propagating roles to Kubernetes namespaces. Project-level roles let you deploy custom resources into the project namespace of the Management API server and enable services only in your project namespace.

**Important:** The project namespace for Platform Administrators in the Management API server is the `platform-obs` namespace.

If you can't access or use a monitoring or logging service, contact your administrator to grant you the necessary roles. Request the appropriate permissions from your Project IAM Admin for a given project. If you require permissions at the organization level, ask your Organization IAM Admin instead.

This page describes all the roles and their respective permissions for using monitoring and logging services.

### Predefined roles at the project level

Request the appropriate permissions from your Project IAM Admin to use logging and monitoring services in a project. All roles must bind to the project namespace where you are using the service.

**Important:** Project-level roles let you deploy custom resources into the project namespace of the Management API server and enable services only in your project namespace.

To grant permissions or receive role access to resources at the project level, see [Grant access to project resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-bindings).

#### Monitoring resources

The following table provides details about the permissions assigned to each predefined role for monitoring resources:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
ConfigMap Creator | `configmap-creator` | Create `ConfigMap` objects in the project namespace. | `Role`  
Dashboard Editor | `dashboard-editor` | Edit or modify `Dashboard` custom resources in the project namespace. | `Role`  
Dashboard Viewer | `dashboard-viewer` | View `Dashboard` custom resources in the project namespace. | `Role`  
MonitoringRule Editor | `monitoringrule-editor` | Edit or modify `MonitoringRule` custom resources in the project namespace. | `Role`  
MonitoringRule Viewer | `monitoringrule-viewer` | View `MonitoringRule` custom resources in the project namespace. | `Role`  
MonitoringTarget Editor | `monitoringtarget-editor` | Edit or modify `MonitoringTarget` custom resources in the project namespace. | `Role`  
MonitoringTarget Viewer | `monitoringtarget-viewer` | View `MonitoringTarget` custom resources in the project namespace. | `Role`  
ObservabilityPipeline Editor | `observabilitypipeline-editor` | Edit or modify `ObservabilityPipeline` custom resources in the project namespace. | `Role`  
ObservabilityPipeline Viewer | `observabilitypipeline-viewer` | View `ObservabilityPipeline` custom resources in the project namespace. | `Role`  
Project Cortex Alertmanager Editor | `project-cortex-alertmanager-editor` | Edit the Cortex Alertmanager instance in the project namespace. | `Role`  
Project Cortex Alertmanager Viewer | `project-cortex-alertmanager-viewer` | Access the Cortex Alertmanager instance in the project namespace. | `Role`  
Project Cortex Prometheus Viewer | `project-cortex-prometheus-viewer` | Access the Cortex Prometheus instance in the project namespace. | `Role`  
Project Grafana Viewer | `project-grafana-viewer` | Visualize project-related observability data on dashboards of the Grafana monitoring instance. | `Role`  
  
#### Logging resources

The following table provides details about the permissions assigned to each predefined role for logging resources:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
Audit Logs Platform Restore Bucket Creator | `audit-logs-platform-restore-bucket-creator` | Create backup buckets to restore the platform audit logs. | `Role`  
Audit Logs Platform Bucket Viewer | `audit-logs-platform-bucket-viewer` | View backup buckets of platform audit logs. | `Role`  
LoggingRule Creator | `loggingrule-creator` | Create `LoggingRule` custom resources in the project namespace. | `Role`  
LoggingRule Editor | `loggingrule-editor` | Edit or modify `LoggingRule` custom resources in the project namespace. | `Role`  
LoggingRule Viewer | `loggingrule-viewer` | View `LoggingRule` custom resources in the project namespace. | `Role`  
LoggingTarget Creator | `loggingtarget-creator` | Create `LoggingTarget` custom resources in the project namespace. | `Role`  
LoggingTarget Editor | `loggingtarget-editor` | Edit or modify `LoggingTarget` custom resources in the project namespace. | `Role`  
LoggingTarget Viewer | `loggingtarget-viewer` | View `LoggingTarget` custom resources in the project namespace. | `Role`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
