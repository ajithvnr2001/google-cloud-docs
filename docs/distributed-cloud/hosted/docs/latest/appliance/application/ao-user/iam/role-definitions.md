---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-definitions/
title: Role definitions for projects \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:30.190590+00:00
---

# Role definitions for projects  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-definitions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Role definitions for projects Stay organized with collections  Save and categorize content based on your preferences. 

The tables of this section describe different predefined roles and their permissions. The tables contain the following columns:

  * **Name:** The name of a role displayed in the user interface (UI).
  * **Kubernetes resource name:** The name of the corresponding Kubernetes custom resource.
  * **Level:** The specification of whether this role is scoped by the organization or a project.
  * **Type:** The type of this role. For example, some possible values are `Role`, `ProjectRole`, `ClusterRole`, or `ProjectClusterRole`.
  * **Binding type:** The type of binding that you must apply to this role.
  * **Management API server or Kubernetes cluster permissions:** The permissions that this role has for the Management API server or the Kubernetes cluster. For example, some possible values are read, write, read and write, or not applicable (N/A).
  * **Escalates to:** The specification of whether this role escalates to other roles or not.



## AO persona, predefined identity and access roles

**AO persona**  
---  
**Name** | **Kubernetes resource name** | **Initial admin** | **Level** | **Type**  
Project IAM Admin | `project-iam-admin` | True | Project | `Role`  
AI Ocr Developer | `ai-ocr-developer` | False | Project | `Role`  
AI Speech Developer | `ai-speech-developer` | False | Project | `Role`  
AI Translation Developer | `ai-translation-developer` | False | Project | `Role`  
Certificate Authority Service Admin | `certificate-authority-service-admin` | False | Project | `Role`  
Certificate Service Admin | `certificate-service-admin` | False | Project | `Role`  
Custom Role Project Admin | `custom-role-project-admin` | False | Project | `Role`  
Dashboard Editor | `dashboard-editor` | False | Project | `Role`  
Dashboard Viewer | `dashboard-viewer` | False | Project | `Role`  
Debugging AuditLoggingTarget custom resource | `auditloggingtarget-monitor` | False | Project | `Role`  
Harbor Instance Viewer | `harbor-instance-viewer` | False | Project | `Role`  
Harbor Project Creator | `harbor-project-creator` | False | Project | `Role`  
K8S NetworkPolicy Admin | `k8s-networkpolicy-admin` | False | Project | `ProjectRole`  
Load Balancer Admin | `load-balancer-admin` | False | Project | `Role`  
LoggingRule Creator | `loggingrule-creator` | False | Project | `Role`  
LoggingRule Editor | `loggingrule-editor` | False | Project | `Role`  
LoggingRule Viewer | `loggingrule-viewer` | False | Project | `Role`  
LoggingTarget Creator | `loggingtarget-creator` | False | Project | `Role`  
LoggingTarget Editor | `loggingtarget-editor` | False | Project | `Role`  
LoggingTarget Viewer | `loggingtarget-viewer` | False | Project | `Role`  
Managed DNS Project Admin | `managed-dns-project-admin` | False | Project | `Role`  
Managed DNS Project Viewer | `managed-dns-project-viewer` | False | Project | `Role`  
MonitoringRule Editor | `monitoringrule-editor` | False | Project | `Role`  
MonitoringRule Viewer | `monitoringrule-viewer` | False | Project | `Role`  
MonitoringTarget Editor | `monitoringtarget-editor` | False | Project | `Role`  
MonitoringTarget Viewer | `monitoringtarget-viewer` | False | Project | `Role`  
Namespace Admin | `namespace-admin` | False | Project | `ProjectRole`  
NAT Viewer | `nat-viewer` | False | Project | `ProjectRole`  
ObservabilityPipeline Editor | `observabilitypipeline-editor` | False | Project | `Role`  
ObservabilityPipeline Viewer | `observabilitypipeline-viewer` | False | Project | `Role`  
Project Bucket Admin | `project-bucket-admin` | False | Project | `Role`  
Project Bucket Object Admin | `project-bucket-object-admin` | False | Project | `Role`  
Project Bucket Object Viewer | `project-bucket-object-viewer` | False | Project | `Role`  
Project Cortex Alertmanager Editor | `project-cortex-alertmanager-editor` | False | Project | `Role`  
Project Cortex Alertmanager Viewer | `project-cortex-alertmanager-viewer` | False | Project | `Role`  
Project Cortex Prometheus Viewer | `project-cortex-prometheus-viewer` | False | Project | `Role`  
Project FileShare Admin | `project-fileshare-admin` | False | Project | `Role`  
Project Grafana Viewer | `project-grafana-viewer` | False | Project | `Role`  
Project Maintenance Policy Admin | `project-mp-admin` | False | Project | `Role`  
Project Maintenance Policy Binding Editor | `project-mpb-editor` | False | Project | `Role`  
Project Maintenance Policy Binding Viewer | `project-mpb-viewer` | False | Project | `Role`  
Project Maintenance Policy Editor | `project-mp-editor` | False | Project | `Role`  
Project Maintenance Policy Viewer | `project-mp-viewer` | False | Project | `Role`  
Project NetworkPolicy Admin | `project-networkpolicy-admin` | False | Project | `Role`  
Project Viewer | `project-viewer` | False | Project | `Role`  
Project VirtualMachine Admin | `project-vm-admin` | False | Project | `Role`  
Project VirtualMachine Image Admin | `project-vm-image-admin` | False | Project | `Role`  
Secret Admin | `secret-admin` | False | Project | `Role`  
Secret Viewer | `secret-viewer` | False | Project | `Role`  
Spark Operator | `mkt-spark-operator` | False | Organization | `Role`  
Subnet Project Admin | `subnet-project-admin` | False | Project | `Role`  
Subnet Project Operator | `subnet-project-operator` | False | Project | `Role`  
Volume Replication Admin | `app-volume-replication-admin` | False | Organization | `ClusterRole`  
Workload Viewer | `workload-viewer` | False | Project | `ProjectRole`  
  
#### AO persona, predefined identity, and access roles

**AO persona**  
---  
**Name** | **Binding type** | **Management API server permissions** | **Kubernetes cluster permissions** | **Escalates to**  
Project IAM Admin | `RoleBinding` | 

  * **`RoleBinding`, `ClusterRoleBinding`, `Role`, `ClusterRole`, `ProjectRole`, `ProjectClusterRole`, `ProjectRoleBinding`, and `ProjectClusterRoleBinding`:** Create, read, update, delete, and bind
  * **`ProjectServiceAccount`:** Create, read, update, and delete
  * List project namespace

| N/A | All other AO roles  
AI Ocr Developer | `RoleBinding` | **OCR resources:** Read and write | N/A | N/A  
AI Speech Developer | `RoleBinding` | **Speech resources:** Read and write | N/A | N/A  
AI Translation Developer | `RoleBinding` | **Translation resources:** Read and write | N/A | N/A  
Certificate Authority Service Admin | `RoleBinding` | **Certificate authorities and certificate requests:** Get, list, watch, update, create, delete, and patch | N/A | N/A  
Certificate Service Admin | `RoleBinding` | **Certificates and certificate issuers:** Get, list, watch, update, create, delete, and patch | N/A | N/A  
Custom Role Project Admin | `RoleBinding` | **Custom Role Project resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Dashboard Editor | `RoleBinding` | **`Dashboard` custom resources:** Get, read, create, update, delete, and patch | N/A | N/A  
Dashboard Viewer | `RoleBinding` | **`Dashboard`:** Get and read | N/A | N/A  
Debugging AuditLoggingTarget custom resource | `RoleBinding` | 

  * **DNS registrations:** Get, list
  * **`Audit logging targets` :**Get, list, update, delete, patch

| N/A | N/A  
Harbor Instance Viewer | `RoleBinding` | **Harbor instances:** Read | N/A | N/A  
Harbor Project Creator | `RoleBinding` | **Harbor instance projects:** Create, get, and watch | N/A | N/A  
K8S NetworkPolicy Admin | `ProjectRoleBinding` | N/A | **`NetworkPolicy` resources:** Create, read, get, update, delete, and patch | N/A  
Load Balancer Admin | `RoleBinding` | N/A | 

  * **`Backend`:** Get, watch, list, create, patch, update, and delete
  * **`HealthCheck`:** Get, watch, list, create, patch, update, and delete
  * **`BackendService`:** Get, watch, list, create, patch, update, and delete
  * **`ForwardingRuleExternal`:** Get, watch, list, create, patch, update, and delete
  * **`ForwardingRuleInternal`:** Get, watch, list, create, patch, update, and delete

| N/A  
LoggingRule Creator | `RoleBinding` | **`LoggingRule` custom resources:** Create, get, list, and watch | N/A | N/A  
LoggingRule Editor | `RoleBinding` | **`LoggingRule` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
LoggingRule Viewer | `RoleBinding` | **`LoggingRule` custom resources:** Read | N/A | N/A  
LoggingTarget Creator | `RoleBinding` | **`LoggingTarget` custom resources:** Create, get, list, and watch | N/A | N/A  
LoggingTarget Editor | `RoleBinding` | **`LoggingTarget` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
LoggingTarget Viewer | `RoleBinding` | **`LoggingTarget` custom resources:** Read | N/A | N/A  
Managed DNS Project Admin | `RoleBinding` | 

  * **Managed DNS zones and resource record sets (`ManagedDNSZone`, `ResourceRecordSet`):** Create, read, update, patch, and delete

| N/A | N/A  
Managed DNS Project Viewer | `RoleBinding` | **Managed DNS zones and resource record sets (`ManagedDNSZone`, `ResourceRecordSet`):** Get, list, and watch | N/A | N/A  
MonitoringRule Editor | `RoleBinding` | **`MonitoringRule` custom resources:** Create, read, update, delete, and patch | N/A | N/A  
MonitoringRule Viewer | `RoleBinding` | **`MonitoringRule` custom resources:** Read | N/A | N/A  
MonitoringTarget Editor | `RoleBinding` | **`MonitoringTarget` custom resources:** Create, read, update, delete, and patch | N/A | N/A  
MonitoringTarget Viewer | `RoleBinding` | **`MonitoringTarget` custom resources:** Read | N/A | N/A  
Namespace Admin | `ProjectRoleBinding` | N/A | **All resources:** Read and write access in the project namespace | N/A  
NAT Viewer | `ProjectRoleBinding` | N/A | **Deployments:** Get and read | N/A  
ObservabilityPipeline Editor | `RoleBinding` | **`ObservabilityPipeline` resources:** Get, read, create, update, delete, and patch | N/A | N/A  
ObservabilityPipeline Viewer | `RoleBinding` | **`ObservabilityPipeline` resources:** Get and read | N/A | N/A  
Project Bucket Admin | `RoleBinding` | **Bucket:** Read and write in the project namespace | N/A | N/A  
Project Bucket Object Admin | `RoleBinding` | 

  * **Bucket:** Read
  * **Objects:** Read and write

| N/A | N/A  
Project Bucket Object Viewer | `RoleBinding` | **Bucket and objects:** Read | N/A | N/A  
Project Cortex Alertmanager Editor | `RoleBinding` | **Cortex system and Cortex Alertmanager:** Read and write | N/A | N/A  
Project Cortex Alertmanager Viewer | `RoleBinding` | **Cortex system and Cortex Alertmanager:** Read | N/A | N/A  
Project Cortex Prometheus Viewer | `RoleBinding` | **Cortex system and Cortex Prometheus:** Read | N/A | N/A  
Project FileShare Admin | `RoleBinding` | **File shares, export groups, and export group bindings:** Create, get, list, watch, and delete | N/A | N/A  
Project Grafana Viewer | `RoleBinding` | **Grafana system and Grafana:** Read and write | N/A | N/A  
Project Maintenance Policy Admin | `RoleBinding` | **Project Maintenance Policy resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Project Maintenance Policy Binding Editor | `RoleBinding` | **Project Maintenance Policy Binding resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Project Maintenance Policy Binding Viewer | `RoleBinding` | **Project Maintenance Policy Binding resources:** Get, list, and watch | N/A | N/A  
Project Maintenance Policy Editor | `RoleBinding` | **Project Maintenance Policy resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Project Maintenance Policy Viewer | `RoleBinding` | **Project Maintenance Policy resources:** Get, list, and watch | N/A | N/A  
Project NetworkPolicy Admin | `RoleBinding` | **Project network policies:** Read and write in the project namespace | N/A | N/A  
Project Viewer | `RoleBinding` | **All resources in the project namespace:** Read | N/A | N/A  
Project VirtualMachine Admin | `RoleBinding` | 

  * **Virtual machines, disks, access requests, external access, backup requests, backups, restore requests, delete backup requests, restores, and password reset requests:** Read, create, update, and delete 
  * **Virtual machine restart:** Put
  * **Virtual machine images, backup plans, and backup plan templates:** Read

| N/A | N/A  
Project VirtualMachine Image Admin | `RoleBinding` | 

  * **VM images:** Read 
  * **VM image imports:** Read and write
  * **Buckets:** Create
  * **"vm-images-bucket" Bucket:** Read and write

| N/A | N/A  
Secret Admin | `RoleBinding` | **Kubernetes secrets:** Read, create, update, delete, and patch | N/A | N/A  
Secret Viewer | `RoleBinding` | **Kubernetes secrets:** Read | N/A | N/A  
Spark Operator | `RoleBinding` | **Spark resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Subnet Project Admin | `RoleBinding` | **Subnet Project resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Subnet Project Operator | `RoleBinding` | **`Subnet` resources:** Create, get, list, and delete | N/A | N/A  
Volume Replication Admin | `ClusterRoleBinding` | **`Volume failovers, volume relationship replicas`:** Create, get, list, watch, delete | N/A | N/A  
Workload Viewer | `ProjectRoleBinding` | N/A | 

  * **Pod custom resources in the project namespace:** Read
  * **Deployment custom resources in the project namespace:** Read

| N/A  
  
## Common predefined identity and access roles

**Common roles**  
---  
**Name** | **Kubernetes resource name** | **Initial admin** | **Level** | **Type**  
Dashboard Editor | `dashboard-editor` | False | Organization / Project | `ClusterRole` / `Role`  
Dashboard Viewer | `dashboard-viewer` | False | Organization / Project | `ClusterRole` / `Role`  
Flow Log Admin | `flowlog-admin` | False | Organization | `ClusterRole`  
Flow Log Viewer | `flowlog-viewer` | False | Organization | `ClusterRole`  
LoggingRule Creator | `loggingrule-creator` | False | Organization / Project | `ClusterRole` / `Role`  
LoggingRule Editor | `loggingrule-editor` | False | Organization / Project | `ClusterRole` / `Role`  
LoggingRule Viewer | `loggingrule-viewer` | False | Organization / Project | `ClusterRole` / `Role`  
LoggingTarget Creator | `loggingtarget-creator` | False | Organization / Project | `ClusterRole` / `Role`  
LoggingTarget Editor | `loggingtarget-editor` | False | Organization / Project | `ClusterRole` / `Role`  
LoggingTarget Viewer | `loggingtarget-viewer` | False | Organization / Project | `ClusterRole` / `Role`  
MonitoringRule Editor | `monitoringrule-editor` | False | Organization / Project | `ClusterRole` / `Role`  
MonitoringRule Viewer | `monitoringrule-viewer` | False | Organization / Project | `ClusterRole` / `Role`  
MonitoringTarget Editor | `monitoringtarget-editor` | False | Organization / Project | `ClusterRole` / `Role`  
MonitoringTarget Viewer | `monitoringtarget-viewer` | False | Organization / Project | `ClusterRole` / `Role`  
ObservabilityPipeline Editor | `observabilitypipeline-editor` | False | Organization / Project | `ClusterRole` / `Role`  
ObservabilityPipeline Viewer | `observabilitypipeline-viewer` | False | Organization / Project | `ClusterRole` / `Role`  
System Artifact Registry anthos-creds secret Monitor | `sar-anthos-creds-secret-monitor` | False | Organization | `Role`  
  
#### Common predefined identity and access roles

**Common roles**  
---  
**Name** | **Binding type** | **Admin cluster permissions** | **Kubernetes cluster permissions** | **Escalates to**  
Dashboard Editor | `ClusterRoleBinding` / `RoleBinding` | **`Dashboard` custom resources:** Get, read, create, update, delete, and patch | N/A | N/A  
Dashboard Viewer | `ClusterRoleBinding` / `RoleBinding` | **`Dashboard`:** Get and read | N/A | N/A  
Flow Log Admin | `ClusterRoleBinding` | **Flow log resources:** Create, get, read, patch, update, and delete | **Flow log resources:** Create, get, read, patch, update, and delete | N/A  
Flow Log Viewer | `ClusterRoleBinding` | **Flow log resources:** Get and read | **Flow log resources:** Get and read | N/A  
LoggingRule Creator | `ClusterRoleBinding` / `RoleBinding` | **`LoggingRule` custom resources:** Create, get, list, and watch | N/A | N/A  
LoggingRule Editor | `ClusterRoleBinding` / `RoleBinding` | **`LoggingRule` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
LoggingRule Viewer | `ClusterRoleBinding` / `RoleBinding` | **`LoggingRule` custom resources:** Read | N/A | N/A  
LoggingTarget Creator | `ClusterRoleBinding` / `RoleBinding` | **`LoggingTarget` custom resources:** Create, get, list, and watch | N/A | N/A  
LoggingTarget Editor | `ClusterRoleBinding` / `RoleBinding` | **`LoggingTarget` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
LoggingTarget Viewer | `ClusterRoleBinding` / `RoleBinding` | **`LoggingTarget` custom resources:** Read | N/A | N/A  
MonitoringRule Editor | `ClusterRoleBinding` / `RoleBinding` | **`MonitoringRule` custom resources:** Create, read, update, delete, and patch | N/A | N/A  
MonitoringRule Viewer | `ClusterRoleBinding` / `RoleBinding` | **`MonitoringRule` custom resources:** Read | N/A | N/A  
MonitoringTarget Editor | `ClusterRoleBinding` / `RoleBinding` | **`MonitoringTarget` custom resources:** Create, read, update, delete, and patch | N/A | N/A  
MonitoringTarget Viewer | `ClusterRoleBinding` / `RoleBinding` | **`MonitoringTarget` custom resources:** Read | N/A | N/A  
ObservabilityPipeline Editor | `ClusterRoleBinding` / `RoleBinding` | **`ObservabilityPipeline` resources:** Get, read, create, update, delete, and patch | N/A | N/A  
ObservabilityPipeline Viewer | `ClusterRoleBinding` / `RoleBinding` | **`ObservabilityPipeline` resources:** Get and read | N/A | N/A  
System Artifact Registry anthos-creds secret Monitor | `RoleBinding` | **`anthos-creds` secrets:** Get and read | **`anthos-creds` secrets:** Get and read | N/A  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
