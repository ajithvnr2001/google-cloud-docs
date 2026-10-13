---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-definitions/
title: Role definitions \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:40.975933+00:00
---

# Role definitions  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-definitions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Role definitions Stay organized with collections  Save and categorize content based on your preferences. 

The tables of this section describe different predefined roles and their permissions. The tables contain the following columns:

  * **Name:** The name of a role displayed in the user interface (UI).
  * **Kubernetes resource name:** The name of the corresponding Kubernetes custom resource.
  * **Level:** The specification of whether this role is scoped by the organization or a project.
  * **Type:** The type of this role. For example, some possible values are `Role`, `ProjectRole`, `ClusterRole`, or `ProjectClusterRole`.
  * **Binding type:** The type of binding that you must apply to this role.
  * **Management API server or Kubernetes cluster permissions:** The permissions that this role has for the Management API server or the Kubernetes cluster. For example, some possible values are read, write, read and write, or not applicable (N/A).
  * **Escalates to:** The specification of whether this role escalates to other roles or not.



## Role types

  * **ClusterRole** : a Kubernetes role-based access control (RBAC) role at the cluster scope in the Management API server or Kubernetes cluster.
  * **Role** : a Kubernetes RBAC role at the namespace scope in the Management API server or Kubernetes cluster.
  * **ProjectRole** : a custom resource definition (CRD) with permission defined and is bound to Kubernetes clusters and namespaces. Project roles propagate to Kubernetes clusters as a `Role`.
  * **OrganizationRole** : a CRD with permission defined, that propagates to Kubernetes clusters as a `ClusterRole` there.

**Notes:**

  * One subject can be bound to multiple roles in the Management API server and Kubernetes clusters. Permissions are purely additive; there are no deny rules.
  * A subject can be granted with only Kubernetes cluster access with `ProjectRole`s and `ProjectRoleBinding`s created by someone else, while the subject has no access in the Management API server.



## Predefined identity and access roles tables

The following tables provide details about the permissions assigned to each predefined role for the infrastructure operator (IO), platform administrator (PA), and application operator (AO) personas:

### IO Persona, predefined identity and access roles

**IO persona**  
---  
**Name** | **Kubernetes resource name** | **Initial admin** | **Level** | **Type**  
Security Admin | `security-admin` | True | Organization | `ClusterRole`  
AI Models Distributor | `ai-models-distributor` | False | Organization | `ClusterRole`  
AI Models Distributor | `ai-models-infra-distributor` | False | Organization | `ClusterRole`  
AIS Monitor | `ais-monitor` | False | Organization | `Role`  
Anthos Identity Service Admin | `ais-admin` | False | Organization | `Role`  
APPLSTOR monitor | `applstor-monitor-cp` | False | Organization | `ClusterRole`  
APPLSTOR secret rotator | `applstor-secret-rotator-cp` | False | Organization | `Role`  
Audit Logs Backup Restore Creator | `audit-logs-backup-restore-creator` | False | Organization | `Role`  
Audit Logs Backup Restore Editor | `audit-logs-backup-restore-editor` | False | Organization | `Role`  
Audit Logs Infra Bucket Viewer | `audit-logs-infra-bucket-viewer` | False | Organization | `Role`  
AuditLoggingRule Editor | `loggingrule-editor` | False | Organization | `ClusterRole`  
AuditLoggingTarget Creator | `auditloggingtarget-creator` | False | Organization | `ClusterRole`  
AuditLoggingTarget Editor | `auditloggingtarget-editor` | False | Organization | `ClusterRole`  
AuditLoggingTarget Editor | `loggingtarget-editor` | False | Organization | `ClusterRole`  
AuditLoggingTarget Viewer | `auditloggingtarget-viewer` | False | Organization | `ClusterRole`  
Bundledidp Admin | `bundledidp-admin` | False | Organization | `Role`  
Cert Manager Monitor | `platauth-cert-manager-monitor` | False | Organization | `ClusterRole`  
Credential Rotation Monitor | `platauth-credential-rotation-monitor` | False | Organization | `ClusterRole`  
Dashboard Creator | `dashboard-creator` | False | Organization | `ClusterRole`  
Dashboard Editor | `dashboard-editor` | False | Organization | `ClusterRole`  
Dashboard Viewer | `dashboard-viewer` | False | Organization | `ClusterRole`  
DNS Key Monitor | `dns-key-monitor` | False | Organization | `Role`  
DNS Monitor | `dns-monitor-cp` | False | Organization | `ClusterRole`  
Emergency SSH Creds Admin | `emergencysshcreds-admin` | False | Organization | `Role`  
FeatureGate Overrider in root admin cluster | `featuregate-overrider-root` | False | Organization | `ClusterRole`  
FeatureGate Overrider in root and org admin cluster (legacy) | `featuregate-overrider-legacy` | False | Organization | `ClusterRole`  
FILE monitor | `file-monitor-cp` | False | Organization | `ClusterRole`  
FILE secret rotator | `file-secret-rotator-cp` | False | Organization | `Role`  
FluentBit Creator | `fluentbit-creator` | False | Organization | `ClusterRole`  
FluentBit Editor | `fluentbit-editor` | False | Organization | `ClusterRole`  
FluentBit IO Creator | `fluentbit-io-creator` | False | Organization | `ClusterRole`  
FluentBit IO Editor | `fluentbit-io-editor` | False | Organization | `ClusterRole`  
FluentBit IO Viewer | `fluentbit-io-viewer` | False | Organization | `ClusterRole`  
FluentBit Viewer | `fluentbit-viewer` | False | Organization | `ClusterRole`  
Grafana Viewer | `grafana-viewer` | False | Organization | `ClusterRole`  
Harbor Instance Operator | `harbor-instance-operator` | False | Organization | `ClusterRole`  
Hardware Admin | `hardware-admin` | False | Organization | `ClusterRole`  
IAM Monitor | `iam-monitor` | False | Organization | `ClusterRole`  
IAM Monitor | `iam-monitor` | False | Organization | `Role`  
Interconnect Admin | `interconnect-admin-cp` | False | Organization | `ClusterRole`  
KUB Monitor | `kub-monitor` | False | Organization | `ClusterRole`  
Log obs-system admin clusters monitor | `log-monitor` | False | Organization | `Role`  
LogCollector Creator | `logcollector-creator` | False | Organization | `ClusterRole`  
LogCollector Editor | `logcollector-editor` | False | Organization | `ClusterRole`  
LogCollector IO Creator | `logcollector-io-creator` | False | Organization | `ClusterRole`  
LogCollector IO Editor | `logcollector-io-editor` | False | Organization | `ClusterRole`  
LogCollector IO Viewer | `logcollector-io-viewer` | False | Organization | `ClusterRole`  
LogCollector Viewer | `logcollector-viewer` | False | Organization | `ClusterRole`  
LoggingRule Creator | `loggingrule-creator` | False | Organization | `ClusterRole`  
LoggingRule Viewer | `loggingrule-viewer` | False | Organization | `ClusterRole`  
LoggingTarget Creator | `loggingtarget-creator` | False | Organization | `ClusterRole`  
LoggingTarget Viewer | `loggingtarget-viewer` | False | Organization | `ClusterRole`  
Logs Bucket Viewer | `logs-bucket-viewer` | False | Organization | `Role`  
Logs Restore Admin | `logs-restore-admin` | False | Organization | `Role`  
Logs Transfer Admin | `logs-transfer-admin` | False | Organization | `Role`  
MonitoringRule Creator | `monitoringrule-creator` | False | Organization | `ClusterRole`  
MonitoringRule Editor | `monitoringrule-editor` | False | Organization | `ClusterRole`  
MonitoringRule Viewer | `monitoringrule-viewer` | False | Organization | `ClusterRole`  
MonitoringTarget Creator | `monitoringtarget-creator` | False | Organization | `ClusterRole`  
MonitoringTarget Editor | `monitoringtarget-editor` | False | Organization | `ClusterRole`  
MonitoringTarget Viewer | `monitoringtarget-viewer` | False | Organization | `ClusterRole`  
MZ Bootstrap Anchor Reader | `mz-bootstrap-anchor-reader` | False | Organization | `ClusterRole`  
MZ Bootstrap Joining Editor | `mz-bootstrap-joining-editor` | False | Organization | `ClusterRole`  
MZ Etcd Controller Editor | `mz-etcd-controller-editor` | False | Organization | `Role`  
MZ Etcd Subcomponent Admin | `mz-etcd-subcomponent-admin` | False | Organization | `ClusterRole`  
MZ Monitor | `mz-monitor` | False | Organization | `ClusterRole`  
Observability Viewer | `observability-viewer` | False | Organization | `Role`  
ObservabilityPipeline Creator | `observabilitypipeline-creator` | False | Organization | `ClusterRole`  
ObservabilityPipeline Editor | `observabilitypipeline-editor` | False | Organization | `ClusterRole`  
ObservabilityPipeline Viewer | `observabilitypipeline-viewer` | False | Organization | `ClusterRole`  
OCLCM Viewer | `oclcm-viewer` | False | Organization | `ClusterRole`  
Organization Admin | `organization-admin` | False | Organization | `ClusterRole`  
Organization Upgrade Admin | `organization-upgrade-admin` | False | Organization | `ClusterRole`  
PNET Monitor | `pnet-monitor` | False | Organization | `ClusterRole`  
PSPF Monitor | `pspf-monitor` | False | Organization | `Role`  
Remote Logger Admin | `remote-logger-admin` | False | Organization | `Role`  
Remote Logger Admin | `remote-logger-admin-root` | False | Organization | `Role`  
Remote Logger Viewer | `remote-logger-viewer` | False | Organization | `Role`  
Remote Logger Viewer | `remote-logger-viewer-root` | False | Organization | `Role`  
Root Cortex Alertmanager Editor | `root-cortex-alertmanager-editor` | False | Organization | `Role`  
Root Cortex Alertmanager Viewer | `root-cortex-alertmanager-viewer` | False | Organization | `Role`  
Root Cortex Prometheus Viewer | `root-cortex-prometheus-viewer` | False | Organization | `Role`  
Root Session Admin | `root-session-admin` | False | Organization | `Role`  
Security Viewer | `security-viewer` | False | Organization | `ClusterRole`  
ServiceLevelObjective Viewer | `servicelevelobjective-viewer` | False | Organization | `ClusterRole`  
Storage Replication Admin | `storage-replication-admin` | False | Organization | `ClusterRole`  
Subnet Admin | `subnet-admin` | False | Organization | `ClusterRole`  
System Artifact Management Admin | `system-artifact-management-admin` | False | Organization | `Role`  
System Artifact Management Secrets Admin | `system-artifact-management-secrets-admin` | False | Organization | `Role`  
System Artifact Registry anthos-creds secret Monitor | `sar-anthos-creds-secret-monitor` | False | Organization | `Role`  
System Artifact Registry gpc-system secret Monitor | `sar-gpc-system-secret-monitor` | False | Organization | `Role`  
System Artifact Registry Harbor Admin | `sar-harbor-admin` | False | Organization | `Role`  
System Artifact Registry Harbor Admin | `sar-harbor-test` | False | Organization | `Role`  
System Artifact Registry Harbor Read | `sar-harbor-read` | False | Organization | `Role`  
System Artifact Registry Harbor ReadWrite | `sar-harbor-readwrite` | False | Organization | `Role`  
System Artifact Registry harbor-system secret Monitor | `sar-harbor-system-secret-monitor` | False | Organization | `Role`  
System Artifact Registry Monitor | `sar-monitor` | False | Organization | `ClusterRole`  
Transfer Appliance Request Admin | `transfer-appliance-request-admin` | False | Organization | `ClusterRole`  
Trust Bundle Root Monitor | `platauth-trust-bundle-root-monitor` | False | Organization | `Role`  
UNET CLI Monitor | `unet-cli-monitor-infra` | False | Organization | `ClusterRole`  
UNET CLI User Monitor | `unet-cli-user-monitor` | False | Organization | `OrganizationRole`  
UNET Monitor | `unet-monitor-infra` | False | Organization | `ClusterRole`  
Upgrade Admin | `upgrade-admin` | False | Organization | `ClusterRole`  
Upgrade Appliance Admin | `upgrade-admin-te` | False | Organization | `ClusterRole`  
User Cluster UNET Monitor | `user-cluster-unet-monitor` | False | Organization | `OrganizationRole`  
Viewer | `viewer` | False | Organization | `ClusterRole`  
  
**IO persona, predefined identity, and access roles**

**IO persona**  
---  
**Name** | **Binding type** | **Management API server permissions** | **Kubernetes cluster permissions** | **Escalates to**  
Security Admin | `ClusterRoleBinding` | 

  * **`RoleBinding`, `ClusterRoleBinding`, `Role`, `ClusterRole`, `ProjectRole`, `OrganizationClusterRole`, `ProjectRoleBinding`, and `OrganizationRoleBinding`:** Create, read, update, and delete
  * **GKE Identity Service (AIS) custom resources (CR):** Read and write

| N/A | Organization IAM Admin and all other IO roles  
AI Models Distributor (`ai-models-distributor`) | `ClusterRoleBinding` | **Buckets:** List  
**ConfigMaps and namespaces:** Get | N/A | N/A  
AI Models Distributor (`ai-models-infra-distributor`) | `ClusterRoleBinding` | **ConfigMaps and namespaces:** Get | N/A | N/A  
AIS Monitor | `RoleBinding` | **AIS resources in`anthos-identity-service` namespace:** Read | N/A | N/A  
Anthos Identity Service Admin | `RoleBinding` | 

  * **AIS pods deployments:** Read and write
  * **AIS encryption secret:** Delete

| N/A | N/A  
APPLSTOR monitor | `ClusterRoleBinding` | `asmconfigs`: Get, list | N/A | N/A  
APPLSTOR secret rotator | `RoleBinding` | `Object storage secrets`: Get, patch | N/A | N/A  
Audit Logs Backup Restore Creator | `RoleBinding` | **Audit Logs Backup Restore resources:** Create, get, list, and watch | N/A | N/A  
Audit Logs Backup Restore Editor | `RoleBinding` | **Backup buckets** : Read and write | N/A | N/A  
Audit Logs Infra Bucket Viewer | `RoleBinding` | **Backup buckets** : Read | N/A | N/A  
AuditLoggingRule Editor | `ClusterRoleBinding` | **`LoggingRule` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
AuditLoggingTarget Creator | `ClusterRoleBinding` | **AuditLoggingTarget resources:** Create, get, list, and watch | N/A | N/A  
AuditLoggingTarget Editor (`auditloggingtarget-editor`) | `ClusterRoleBinding` | **`AuditLoggingTarget` resources:** Get, list, watch, update, patch, and delete | N/A | N/A  
AuditLoggingTarget Editor (`loggingtarget-editor`) | `ClusterRoleBinding` | **`LoggingTarget` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
AuditLoggingTarget Viewer | `ClusterRoleBinding` | **AuditLoggingTarget resources:** Get, list, and watch | N/A | N/A  
Bundledidp Admin | `RoleBinding` | **Bundledidp resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Cert Manager Monitor | `ClusterRoleBinding` | **Cert Manager resources:** Get, list, and watch | N/A | N/A  
Credential Rotation Monitor | `ClusterRoleBinding` | **Credential Rotation resources:** Get, list, and watch | N/A | N/A  
Dashboard Creator | `ClusterRoleBinding` | `Dashboard` custom resources: Get, list, watch, create | N/A | N/A  
Dashboard Editor | `ClusterRoleBinding` | **`Dashboard` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
Dashboard Viewer | `ClusterRoleBinding` | **`Dashboard`:** Get and read | N/A | N/A  
DNS Key Monitor | `RoleBinding` | **Domain Name System (DNS) Key resources:** Get, list, and watch | N/A | N/A  
DNS Monitor | `ClusterRoleBinding` | N/A | **Configmaps, secrets, DNS Registration API, DNS services, DNS deployments:** Read | N/A  
Emergency SSH Creds Admin | `RoleBinding` | N/A | **`EmergencySshCredentials`:** Create, read, and patch | N/A  
FeatureGate Overrider in root admin cluster | `ClusterRoleBinding` | **`KubeAPIServer` resources:** Get, list, and watch | N/A | N/A  
FeatureGate Overrider in root and org admin cluster (legacy) | `ClusterRoleBinding` | **`KubeAPIServer` and `ControlPlane` resources:** Get, list, and watch | N/A | N/A  
FILE monitor | `ClusterRoleBinding` | **`asmconfigs` and `InventoryMachine` resources:** Get and list | N/A | N/A  
FILE secret rotator | `RoleBinding` | **FILE secret rotator resources:** Get, list, patch, and update secrets | N/A | N/A  
FluentBit Creator | `ClusterRoleBinding` | **FluentBit resources:** Create, get, list, and watch | N/A | N/A  
FluentBit Editor | `ClusterRoleBinding` | **`FluentBit` resources:** Get, list, watch, update, patch, and delete | N/A | N/A  
FluentBit IO Creator | `ClusterRoleBinding` | `FluentBit` custom resources: Read and write | N/A | N/A  
FluentBit IO Editor | `ClusterRoleBinding` | `FluentBit` custom resources: Read and write | N/A | N/A  
FluentBit IO Viewer | `ClusterRoleBinding` | `FluentBit` custom resources: Read | N/A | N/A  
FluentBit Viewer | `ClusterRoleBinding` | **FluentBit resources:** Get, list, and watch | N/A | N/A  
Grafana Viewer | `ClusterRoleBinding` | **`GrafanaSystem` and Grafana:** Read and write | N/A | N/A  
Harbor Instance Operator | `ClusterRoleBinding` | **Harbor instance deployments and deployment logs:** Get, patch, and update | N/A | N/A  
Hardware Admin | `ClusterRoleBinding` | **Hardware-related CRD:** Read and write | N/A | N/A  
IAM Monitor (`iam-monitor`, `ClusterRole`) | `ClusterRoleBinding` | **Identity and Access Management (IAM) resources:** Get, list, and watch | N/A | N/A  
IAM Monitor (`iam-monitor`, `Role`) | `RoleBinding` | **IAM resources:** Get, list, and watch | N/A | N/A  
Interconnect Admin | `ClusterRoleBinding` | N/A | **Interconnect attachments and attachment groups** : Get, list, watch, create, update, delete, patch | N/A  
KUB Monitor | `ClusterRoleBinding` | **User cluster (KUB) resources:** Read | N/A | N/A  
Log obs-system admin clusters monitor | `RoleBinding` | **Log obs-system admin clusters monitor resources:** Get, list, and watch | N/A | N/A  
LogCollector Creator | `ClusterRoleBinding` | **LogCollector resources:** Create, get, list, and watch | N/A | N/A  
LogCollector Editor | `ClusterRoleBinding` | **`LogCollector` resources:** Get, list, watch, update, patch, and delete | N/A | N/A  
LogCollector IO Creator | `ClusterRoleBinding` | `LogCollector` custom resources: Read and write | N/A | N/A  
LogCollector IO Editor | `ClusterRoleBinding` | `LogCollector` custom resources: Read and write | N/A | N/A  
LogCollector IO Viewer | `ClusterRoleBinding` | `LogCollector` custom resources: Read | N/A | N/A  
LogCollector Viewer | `ClusterRoleBinding` | **LogCollector resources:** Get, list, and watch | N/A | N/A  
LoggingRule Creator | `ClusterRoleBinding` | **`LoggingRule` custom resources:** Create, get, list, and watch | N/A | N/A  
LoggingRule Viewer | `ClusterRoleBinding` | **`LoggingRule` custom resources:** Read | N/A | N/A  
LoggingTarget Creator | `ClusterRoleBinding` | **`LoggingTarget` custom resources:** Create, get, list, and watch | N/A | N/A  
LoggingTarget Viewer | `ClusterRoleBinding` | **`LoggingTarget` custom resources:** Read | N/A | N/A  
Logs Bucket Viewer | `RoleBinding` | **Logs Bucket resources:** Get, list, and watch | N/A | N/A  
Logs Restore Admin | `RoleBinding` | **Logs Restore resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Logs Transfer Admin | `RoleBinding` | **Logs Transfer resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
MonitoringRule Creator | `ClusterRoleBinding` | **`MonitoringRule` resources:** Create, get, list, and watch | N/A | N/A  
MonitoringRule Editor | `ClusterRoleBinding` | **`MonitoringRule` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
MonitoringRule Viewer | `ClusterRoleBinding` | **`MonitoringRule` custom resources:** Read | N/A | N/A  
MonitoringTarget Creator | `ClusterRoleBinding` | `MonitoringTarget` custom resources: Get, list, watch, create | N/A | N/A  
MonitoringTarget Editor | `ClusterRoleBinding` | **`MonitoringTarget` custom resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
MonitoringTarget Viewer | `ClusterRoleBinding` | **`MonitoringTarget` custom resources:** Read | N/A | N/A  
MZ Bootstrap Anchor Reader | `ClusterRoleBinding` | **Zones, global API zones, services, config maps, and DNS registrations:** Get, list, and watch | N/A | N/A  
MZ Bootstrap Joining Editor | `ClusterRoleBinding` | **Multi-zone (MZ) Bootstrap Joining resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
MZ Etcd Controller Editor | `RoleBinding` | **Etcd controller deployments, replica sets, and pods:** Get and patch | N/A | N/A  
MZ Etcd Subcomponent Admin | `ClusterRoleBinding` | **`Subcomponent` resources:** Get, list, update, patch, and delete | N/A | N/A  
MZ Monitor | `ClusterRoleBinding` | **MZ resources:** Get, list, and watch | N/A | N/A  
Observability Viewer | `RoleBinding` | **`obs-system` namespace:** Read | **`obs-system` namespace:** Read | N/A  
ObservabilityPipeline Creator | `ClusterRoleBinding` | **ObservabilityPipeline resources:** Create, get, list, and watch | N/A | N/A  
ObservabilityPipeline Editor | `ClusterRoleBinding` | **`ObservabilityPipeline` resources:** Get, list, watch, update, delete, and patch | N/A | N/A  
ObservabilityPipeline Viewer | `ClusterRoleBinding` | **`ObservabilityPipeline` resources:** Get and read | N/A | N/A  
OCLCM Viewer | `ClusterRoleBinding` | `oclcm-viewer`: 

  * **Components, component rollouts, subcomponents, subcomponent overrides:** Read

| `oclcm-viewer-root`: 

  * **Components, component rollouts, subcomponents, and subcomponent overrides:** Read

| N/A  
Organization Admin | `ClusterRoleBinding` | 

  * **Organization CR:** Read and write
  * **Organization upgrade and release metadata:** Read

| N/A | N/A  
Organization Upgrade Admin | `ClusterRoleBinding` | **Upgrade config maps:** Get | N/A | N/A  
PNET Monitor | `ClusterRoleBinding` | N/A | **Physical networking (PNET) deployments, deployment logs, pods, pod logs, subnet claims, and switches:** Read | N/A  
PSPF Monitor | `RoleBinding` | N/A | **Policy proxy (PSPF) deployment logs, pods, pod log:** Get, list, watch | N/A  
Remote Logger Admin (`remote-logger-admin`) | `RoleBinding` | **Deployments:** Read, update, patch, and delete | **Deployments:** Read, update, patch, and delete | N/A  
Remote Logger Admin (`remote-logger-admin-root`) | `RoleBinding` | **Deployments:** Read, update, patch, and delete | **Deployments:** Read, update, patch, and delete | N/A  
Remote Logger Viewer (`remote-logger-viewer`) | `RoleBinding` | **Deployments:** Read | **Deployments:** Read | N/A  
Remote Logger Viewer (`remote-logger-viewer-root`) | `RoleBinding` | **Deployments:** Read | **Deployments:** Read | N/A  
Root Cortex Alertmanager Editor | `RoleBinding` | N/A | **Cortex Alertmanager, logging rules, and monitoring rules custom resources:** Create, delete, read, patch, and update | N/A  
Root Cortex Alertmanager Viewer | `RoleBinding` | **N/A** | **Cortex Alertmanager, logging rules, and monitoring rules custom resources:** Read | N/A  
Root Cortex Prometheus Viewer | `RoleBinding` | N/A | **Cortex system and Cortex Prometheus:** Read | N/A  
Root Session Admin | `RoleBinding` | N/A | **Istio resource manager:** Create, read, update, delete, and patch | N/A  
Security Viewer | `ClusterRoleBinding` | 

  * **`RoleBinding` and `ClusterRoleBinding`:** Read
  * **`Role` and `ClusterRole`:** Read
  * **AIS CR:** Read

| N/A | N/A  
ServiceLevelObjective Viewer | `ClusterRoleBinding` | **ServiceLevelObjective resources:** Get, list, and watch | N/A | N/A  
Storage Replication Admin | `ClusterRoleBinding` | **Storage cluster peerings, storage virtual machine peerings, volume replication relationships, and volume failovers:** Create, get, list, watch, and delete | N/A | N/A  
Subnet Admin | `ClusterRoleBinding` | **Subnet resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
System Artifact Management Admin | `RoleBinding` | **`HarborProjects`:** Admin, create, read, write, delete, and view | 

  * **Harbor projects and user credentials:** Create, delete, and read
  * **`HarborProjects`:** Admin, read, write
  * **Distribute artifacts:** Create, delete, update, and read
  * **`image-label-map` configmap:** Create, delete, update, and read
  * **Servers, trust store configmaps:** Read

| N/A  
System Artifact Management Secrets Admin | `RoleBinding` | N/A | 

  * **In-cluster registry:** Read
  * **Upgrade registry mirror:** Create, read, update, and delete

| N/A  
System Artifact Registry anthos-creds secret Monitor | `RoleBinding` | **`anthos-creds` secrets:** Get and read | **`anthos-creds` secrets:** Get and read | N/A  
System Artifact Registry gpc-system secret Monitor | `RoleBinding` | **`gpc-system` secrets:** Get and read | **`gpc-system` secrets:** Get and read | N/A  
System Artifact Registry Harbor Admin (`sar-harbor-admin`) | `RoleBinding` | Harbor projects: Create, read, update, patch, and delete | **Harbor projects:** Create, read, update, patch, and delete | N/A  
System Artifact Registry Harbor Admin (`sar-harbor-test`) | `RoleBinding` | Harbor projects: Create, read, update, patch, and delete | **Harbor projects:** Create, read, update, patch, and delete | N/A  
System Artifact Registry Harbor Read | `RoleBinding` | N/A | **Harbor projects:** Read | N/A  
System Artifact Registry Harbor ReadWrite | `RoleBinding` | N/A | **Harbor projects:** Create, read, and write | N/A  
System Artifact Registry harbor-system secret Monitor | `RoleBinding` | **`harbor-system` secrets:** Get and read | **`harbor-system` secrets:** Get and read | N/A  
System Artifact Registry Monitor | `ClusterRoleBinding` | N/A | **Harbor clusters, secrets, and CRDs:** Read | N/A  
Transfer Appliance Request Admin | `ClusterRoleBinding` | **`TransferApplianceRequest` resources and status:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Trust Bundle Root Monitor | `RoleBinding` | **Trust bundle config maps:** Get, list, and watch | N/A | N/A  
UNET CLI Monitor | `ClusterRoleBinding` | **Upper networking (UNET) command-line interface (CLI) resources:** Get, list, and watch | N/A | N/A  
UNET CLI User Monitor | `OrganizationRoleBinding` | N/A | 

  * **Networking resources, secrets, configmaps, Cilium endpoints, virtual machines (VM), VM runtimes, deployments, clusters, namespaces, CRDs:** Read
  * **Pods:** Read and create

| N/A  
UNET Monitor | `ClusterRoleBinding` | **UNET resources:** Get, list, and watch | N/A | N/A  
Upgrade Admin | `ClusterRoleBinding` | **Upgrade resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Upgrade Appliance Admin | `ClusterRoleBinding` | **SubcomponentOverrides:** Get, list, create, update, and patch | 

  * **Organization:** Get, list, update, patch,and watch 
  * **OrganizationUpgrade:** Get

| N/A  
User Cluster UNET Monitor | `OrganizationRoleBinding` | N/A | **Projects, project network policies, configmaps, secrets, certificates, certificate issuers, bundles, deployments, daemon sets, stateful sets, pods, pod logs, services, endpoints, endpoint slices, network policies, network loggings, cilium, networks, network interfaces, VMs, VM instances, networking, cluster Classless Inter-Domain Routing (CIDR) configs, flat IP modes, configmap forwarders, secret forwarders, health checks, node pool claims, node pools, AddOn configurations, flow logs, and flow logs status, Border Gateway Protocol (BGP) peers, BGP advertised routes, BGP received routes, BGP sessions, BGP load balancers, egress network address translation (NAT) policies, network gateway groups, network gateway nodes, flat IP modes, multi-cluster connectivity configs, virtual private network (VPN) tunnels, and traffic steerings:** Get and read | N/A  
Viewer | `ClusterRoleBinding` | **Viewer resources:** Get, list, and watch | N/A | N/A  
  
### IO Persona, predefined debugger roles

When you run into issues, IOs use predefined debugger roles to troubleshoot and resolve them. These roles give IOs organization-wide administrative access with elevated read and write permissions. With that access, IOs can inspect logs, modify configurations, and manage resources across your entire infrastructure, including the Management API server, the organization infrastructure cluster, and user Kubernetes clusters.

All debugger roles share the following characteristics:

  * Are scoped at the organization level.
  * Aren't assigned to the initial administrator by default.
  * Don't escalate to other roles.



The following table lists the permissions that IOs use during these operations:

**IO persona debugger roles**  
---  
**Name** | **Kubernetes resource name** | **Binding type** | **Management API server permissions** | **Kubernetes cluster permissions**  
AIS Debugger | `ais-debugger` | `RoleBinding` | **AIS resources in the`anthos-identity-service` namespace (configmaps, deployments, stateful sets, pods, pod logs, persistent volume claims (PVCs), events, secrets, rotatable secrets, and rotation requests):** Create, read, update, patch, and delete | N/A  
APPLSTOR debugger | `applstor-debugger-cp` | `ClusterRoleBinding` | **`asmconfigs`:** All operations  
**Namespaces and secrets:** Get and list | N/A  
ASM Debugger | `asm-admin-debugger` | `ClusterRoleBinding` | **Istio service mesh resources (`ManagedServiceMesh`, `IstioOperator`, `IstioAuthorizationResource`, gateways, virtual services, destination rules, envoy filters, peer authentications, authorization policies, and telemetries), deployments, daemon sets, stateful sets, replica sets, pods, pod logs, pod port-forwarding, configmaps, secrets, services, endpoints, and service accounts:** Create, get, list, watch, update, patch, and delete | N/A  
ASM User Debugger | `asm-user-debugger` | `OrganizationRoleBinding` | N/A | **Pods, services, pod port-forwarding, Istio security, networking, and telemetry resources, and`IstioAuthorizationResource` resources:** All operations  
**Nodes and`IstioOperator` resources:** Get and list  
Cert Manager Debugger | `platauth-cert-manager-debugger` | `ClusterRoleBinding` | **Certificates, certificate requests, issuers, cluster issuers, Automated Certificate Management Environment (ACME) challenges, and orders:** Create, get, list, watch, update, patch, and delete | N/A  
Cert Manager User Cluster Debugger | `platauth-cert-manager-user-debugger` | `OrganizationRoleBinding` | N/A | **Certificates, certificate requests, issuers, cluster issuers, challenges, and orders:** Create, get, list, watch, update, patch, and delete  
Credential Rotation Debugger | `platauth-credential-rotation-debugger` | `ClusterRoleBinding` | **Secret rotation requests (`RotationRequest`), rotatable secrets (`RotatableSecret`), and secrets:** Create, get, list, watch, update, patch, and delete | N/A  
Debugging AuditLoggingTarget's istio resources | `auditloggingtarget-istio-monitor` | `RoleBinding` | **Istio resources (`VirtualService`, `Gateway`), services, secrets, and certificates:** Get and list | N/A  
DNS Debugger | `dns-debugger-cp` | `ClusterRoleBinding` | 

  * **Configmaps and secrets:** Create, read, and delete
  * **DNS registrations:** Create and read
  * **Services:** Read and update
  * **Deployments and deployment logs:** Read, patch, and update
  * **Pods:** Create and read
  * **Pod logs:** Read

| N/A  
DNS Key Debugger | `dns-key-debugger` | `RoleBinding` | **Domain Name System Security Extensions (DNSSEC) signing key secrets and configmaps in the`dns-system` namespace:** Create, get, list, watch, update, patch, and delete | N/A  
EZ Debugger | `ez-debugger` | `ClusterRoleBinding` | **Software as a service (SaaS) runtime resources (`SaasInstance`, `ModuleInstance`, and `LocalRollout`) and maintenance policy resources (`MaintenancePolicy` and `MaintenancePolicyBinding`):** Create, get, list, watch, update, patch, and delete | N/A  
FILE debugger | `file-debugger-cp` | `ClusterRoleBinding` | **`InventoryMachine`, namespaces, and secrets:** Get and list | N/A  
Grafana Admin | `grafana-debugger` | `RoleBinding` | **Apps, deployments, stateful sets, and pods:** Read, update, delete, and patch | **Apps, deployments, stateful sets, and pods:** Read, update, delete, and patch  
Grafana Admin | `grafana-debugger-cp` | `ClusterRoleBinding` | **Apps, deployments, stateful sets, and pods:** Read, update, delete, and patch | **Apps, deployments, stateful sets, and pods:** Read, update, delete, and patch  
Harbor Instance Debugger | `harbor-instance-debugger` | `ClusterRoleBinding` | 

  * **Harbor instances, Harbor instance backups, backup plans, backup repositories, and restores (database and registry):** Create, get, list, watch, update, patch, and delete
  * **Shadow projects:** Create, get, list, watch, update, and delete
  * **Deployments, deployment logs, monitoring targets, metrics proxy sidecars, and CRDs:** Get, list, watch, update, and patch
  * **Certificates, cluster issuers, issuers, and Istio authorization policies:** Get, list, watch, update, and delete
  * **Pods and pod exec:** Create, get, list, and watch
  * **Audit logging targets, logging targets, buckets, PostgreSQL database clusters, project network policies, and pod logs:** Get, list, and watch

| N/A  
IAM Debugger | `iam-debugger` | `ClusterRoleBinding` | **IAM CRs, identity providers, role bindings, cluster role bindings, and webhook configurations:** Create, get, list, watch, update, patch, and delete | N/A  
IAM Debugger | `iam-debugger` | `RoleBinding` | **IAM deployments, pods, pod logs, configmaps, and secrets in the`iam-system` namespace:** Create, get, list, watch, update, patch, and delete | N/A  
KUB IPAM Debugger | `kub-ipam-debugger` | `ClusterRoleBinding` | **IP address management (IPAM) CRs (`CIDRClaim`, `AddressPoolClaim`, and `Subnet`):** Read and write | N/A  
Log obs-system organization administrator debugger | `log-debugger` | `RoleBinding` | 

  * **Pods, pod exec, pod port-forwarding, and Istio telemetries in the`obs-system` namespace:** Create, get, list, watch, update, patch, and delete
  * **Deployments, deployment scale, stateful sets, horizontal pod autoscalers, persistent volumes, and PVCs:** Get, list, watch, update, patch, and delete
  * **Daemon sets, log collectors, and monitoring targets:** Get, list, watch, and patch
  * **Secrets:** Get, list, and delete
  * **Audit logging targets, logging pipelines, certificates, configmaps, pod logs, daemon set logs, deployment logs, stateful set logs, events, nodes, services, envoy filters, and virtual services:** Get, list, and watch

| N/A  
Observability Admin | `observability-admin-debugger` | `RoleBinding` | 

  * **`obs-system` namespace:** Read
  * **Anthos audit logs forwarder and Anthos log forwarder:** Update, patch, and delete

| 

  * **`obs-system` namespace:** Read
  * **`audit-logs-loki`, `loki`, `cortex`, `anthos-audit-logs-forwarder`, `anthos-log-forwarder`:** Update, patch, and delete

  
Observability Admin | `observability-admin-debugger-root` | `RoleBinding` | 

  * **`obs-system` namespace:** Read
  * **Anthos audit logs forwarder and Anthos log forwarder:** Update, patch, and delete

| 

  * **`obs-system` namespace:** Read
  * **`audit-logs-loki`, `loki`, `cortex`, `anthos-audit-logs-forwarder`, `anthos-log-forwarder`:** Update, patch, and delete

  
Observability Debugger | `observability-debugger` | `OrganizationRoleBinding` | 

  * **Deployments, stateful sets, daemon sets, secrets, configmaps:** Read, create, delete, patch, and update
  * **Certificates:** Read

| N/A  
OCLCM Debugger | `oclcm-debugger` | `ClusterRoleBinding` | `oclcm-debugger`: 

  * **Components:** Create and read
  * **Component rollouts and subcomponents:** Read, patch, and update
  * **Subcomponent overrides:** Create, read, update, and patch

| `oclcm-debugger-root`: 

  * **Components:** Create and read
  * **Component rollouts and subcomponents:** Read, patch, and update
  * **Subcomponent overrides:** Create, read, update, and patch

  
PNET Debugger | `pnet-debugger` | `ClusterRoleBinding` | N/A | 

  * **PNET deployments and deployment logs:** Read, patch, and update
  * **Pods, pod logs, subnet claims, and switches:** Read

  
PNET Debugger | `pnet-debugger` | `RoleBinding` | N/A | 

  * **PNET deployments and deployment logs:** Read, patch, and update
  * **Pods, pod logs, subnet claims, and switches:** Read

  
PNET Secret Debugger | `pnet-secret-debugger` | `RoleBinding` | N/A | **PNET secrets:** Get, list, watch, create, update, patch, delete  
PSPF Debugger | `pspf-debugger` | `RoleBinding` | N/A | 

  * **PSPF deployments:** Get, list, watch, create, update, patch, delete
  * **PSPF deployment logs, pods, pod logs:** Get, list, watch

  
SSH Infra Debugger | `platauth-ssh-infra-debugger` | `RoleBinding` | N/A | **Secure Shell (SSH) secrets:** Get, list, watch, patch, update, create, delete  
System Artifact Registry Debugger | `sar-debugger` | `ClusterRoleBinding` | N/A | 

  * **Harbor clusters, secrets, distribution policies, manual distribution, and configmaps:** Create, read, update, patch and delete
  * **PVCs, pods, and Harbor robot accounts:** Create, read, and delete
  * **Release metadata, organizations, database clusters, Harbor projects, certificates, servers, and clusters:** Read
  * **Database and CRDs:** Read and delete
  * **Deployments:** Read, update, patch, and delete
  * **Persistent volumes:** Read, update, and patch

  
System Artifact Registry harbor-system secret Debugger | `sar-harbor-system-secret-debugger` | `RoleBinding` | **`harbor-system` secrets:** Create, get, list, watch, update, patch, and delete | N/A  
System Cluster Vertex AI Debugger | `system-cluster-vai-debugger` | `ClusterRoleBinding` | **Vertex AI system cluster resources (app configs, basic services, cluster configs, emergency configs, endpoints, experiment configs, host maintenances, microservices, packages, and resource pools) and secrets:** Create, get, list, watch, update, patch, and delete | N/A  
UNET Debugger | `unet-debugger-infra` | `ClusterRoleBinding` | **UNET resources (BGP routes, peers, sessions, gateways, and load balancers, Bidirectional Forwarding Detection (BFD) profiles, IP address pools, Layer 2 (L2) advertisements, Cilium network policies, endpoints, identities, and nodes, cluster CIDR configs, cluster DNS, egress NAT policies, flat IP modes, multi-cluster connectivity configs, network gateway groups and nodes, network interfaces, network loggings, networks, and VPN tunnels), configmaps, daemon sets, deployments, services, endpoints, and endpoint slices:** Create, get, list, watch, update, patch, and delete | N/A  
Upgrade Debugger | `upgrade-debugger` | `ClusterRoleBinding` | N/A | 

  * **Upgrade resources (node upgrades, release metadata, component release metadata, preflight checks, maintenance windows, configmaps, and secrets):** Create, read, update, delete, and patch
  * **Harbor projects:** Harbor-admin

  
User Cluster Debugger | `user-cluster-debugger` | `OrganizationRoleBinding` | N/A | 

  * **User clusters, bare metal clusters, add-on configurations, inventory machines, machines, node pools, node pool claims, nodes, pods, pod exec, pod logs, jobs, configmaps, and secrets:** Create, get, list, watch, update, patch, and delete
  * **Address pool claims, CIDR claims, subnet claims, organizations, and servers:** Create, get, list, watch, update, and patch
  * **Daemon sets, deployments, and replica sets:** Get, list, watch, and patch
  * **Upgrade preflight checks:** Get, list, watch, and delete
  * **Subnets, graphics processing unit (GPU) allocations, Harbor clusters, hardware security module (HSM) clusters, and VMs:** Get, list, and watch

  
User Cluster DNS Debugger | `user-cluster-dns-debugger` | `OrganizationRoleBinding` | N/A | 

  * **Deployments, Deployment logs, Pods, Pod logs:** Read
  * **Pods:** Create

  
User Cluster UNET Debugger | `user-cluster-unet-debugger` | `OrganizationRoleBinding` | N/A | 

  * **Configmaps:** Get, update, and read
  * **Deployments, deployment logs, daemon sets, and daemon sets logs:** Get, read, patch, and update
  * **Pods and pod logs:** Get, read, create, and delete
  * **Services, cilium, and network policies:** Get, read, create, update, and delete
  * **Flow logs and flow logs status:** Get, read, create, patch, update, and delete

  
Vertex AI Debugger | `vai-debugger` | `ClusterRoleBinding` | **Vertex AI packages, projects, deployments, UI resources, and add-on sets:** Create, get, list, watch, update, patch, and delete  
**Secrets:** Get, list, and delete | N/A  
VPN Debugger For Org Infrastructure Cluster | `vpn-debugger-infra` | `ClusterRoleBinding` | **Network gateway nodes and groups, BGP routes, peers, and sessions, VPN tunnels, and traffic steerings:** Get, list, and watch | N/A  
Web TLS Certificate Debugger | `platauth-web-tls-cert-debugger` | `RoleBinding` | N/A | **Secrets and public key infrastructure (PKI) certificates:** Get, list, watch, update, patch, create, delete  
  
### PA Persona, predefined identity and access roles

**PA persona**  
---  
**Name** | **Kubernetes resource name** | **Initial admin** | **Level** | **Type**  
Organization IAM Admin | `organization-iam-admin` | True | Organization | `ClusterRole`  
AI Platform Admin | `ai-platform-admin` | False | Organization | `Role`  
Bucket Admin | `bucket-admin` | False | Organization | `ClusterRole`  
Bucket Object Admin | `bucket-object-admin` | False | Organization | `ClusterRole`  
Bucket Object Viewer | `bucket-object-viewer` | False | Organization | `ClusterRole`  
ConfigMap Editor | `observabilitypipeline-configmap-editor` | False | Organization | `Role`  
Custom Role Org Admin | `custom-role-org-admin` | False | Organization | `ClusterRole`  
Dashboard PA Creator | `dashboard-pa-creator` | False | Organization | `ClusterRole`  
Dashboard PA Editor | `dashboard-pa-editor` | False | Organization | `ClusterRole`  
Dashboard PA Viewer | `dashboard-pa-viewer` | False | Organization | `ClusterRole`  
Flow Log Admin | `flowlog-admin` | False | Organization | `ClusterRole`  
Flow Log Viewer | `flowlog-viewer` | False | Organization | `ClusterRole`  
GDCHRestrictByAttributes Policy Admin | `gdchrestrictbyattributes-policy-admin` | False | Organization | `ClusterRole`  
GDCHRestrictedService Policy Admin | `gdchrestrictedservice-policy-admin` | False | Organization | `ClusterRole`  
Identity Provider Federation Admin | `idp-federation-admin` | False | Organization | `Role`  
Infra PKI Admin | `infra-pki-admin` | False | Organization | `Role`  
Interconnect Admin | `interconnect-admin-mp` | False | Organization | `ClusterRole`  
LoggingRule PA Creator | `loggingrule-pa-creator` | False | Organization | `ClusterRole`  
LoggingRule PA Editor | `loggingrule-pa-editor` | False | Organization | `ClusterRole`  
LoggingRule PA Viewer | `loggingrule-pa-viewer` | False | Organization | `ClusterRole`  
LoggingTarget PA Creator | `loggingtarget-pa-creator` | False | Organization | `ClusterRole`  
LoggingTarget PA Editor | `loggingtarget-pa-editor` | False | Organization | `ClusterRole`  
LoggingTarget PA Viewer | `loggingtarget-pa-viewer` | False | Organization | `ClusterRole`  
MonitoringRule PA Creator | `monitoringrule-pa-creator` | False | Organization | `ClusterRole`  
MonitoringRule PA Editor | `monitoringrule-pa-editor` | False | Organization | `ClusterRole`  
MonitoringRule PA Viewer | `monitoringrule-pa-viewer` | False | Organization | `ClusterRole`  
MonitoringTarget PA Creator | `monitoringtarget-pa-creator` | False | Organization | `ClusterRole`  
MonitoringTarget PA Editor | `monitoringtarget-pa-editor` | False | Organization | `ClusterRole`  
MonitoringTarget PA Viewer | `monitoringtarget-pa-viewer` | False | Organization | `ClusterRole`  
MP OCLCM Debugger | `mp-oclcm-debugger` | False | Organization | `ClusterRole`  
MP OCLCM Viewer | `mp-oclcm-viewer` | False | Organization | `ClusterRole`  
ObservabilityPipeline PA Creator | `observabilitypipeline-pa-creator` | False | Organization | `ClusterRole`  
ObservabilityPipeline PA Editor | `observabilitypipeline-pa-editor` | False | Organization | `ClusterRole`  
ObservabilityPipeline PA Viewer | `observabilitypipeline-pa-viewer` | False | Organization | `ClusterRole`  
Org Network Policy Admin | `org-network-policy-admin` | False | Organization | `Role`  
Org Session Admin | `org-session-admin` | False | Organization | `Role`  
Organization Grafana Viewer | `organization-grafana-viewer` | False | Organization | `Role`  
Organization IAM Viewer | `organization-iam-viewer` | False | Organization | `ClusterRole`  
Organization Upgrade Admin | `organization-upgrade-admin` | False | Organization | `ClusterRole`  
Organization Upgrade Viewer | `organization-upgrade-viewer` | False | Organization | `ClusterRole`  
Project Creator | `project-creator` | False | Organization | `ClusterRole`  
Project Editor | `project-editor` | False | Organization | `ClusterRole`  
Subnet Organization Admin | `subnet-org-admin` | False | Organization | `ClusterRole`  
Transfer Appliance Request Creator | `transfer-appliance-request-creator` | False | Organization | `ClusterRole`  
Trust Store Viewer | `trust-store-viewer` | False | Organization | `Role`  
User Cluster Admin | `user-cluster-admin` | False | Organization | `ClusterRole`  
User Cluster Developer | `user-cluster-developer` | False | Organization | `OrganizationRole`  
User Cluster Node Viewer | `user-cluster-node-viewer` | False | Organization | `OrganizationRole`  
Volume Replication Admin | `volume-replication-admin` | False | Organization | `ClusterRole`  
VPN Admin | `vpn-admin` | False | Organization | `Role`  
VPN Viewer | `vpn-viewer` | False | Organization | `Role`  
Web TLS Certificate Admin | `web-tls-cert-admin` | False | Organization | `Role`  
  
#### PA persona, predefined identity, and access roles

**PA persona**  
---  
**Name** | **Binding type** | **Management API server permissions** | **Kubernetes cluster permissions** | **Escalates to**  
Organization IAM Admin | `ClusterRoleBinding` | 

  * **`RoleBinding`, `ClusterRoleBinding`, `Role`, `ClusterRole`, `ProjectRole`, `OrganizationClusterRole`, `ProjectRoleBinding`, and `OrganizationClusterRoleBinding`:** Create, read, update, and delete
  * List project namespace

| N/A | Project IAM Admin and all other PA roles  
AI Platform Admin | `RoleBinding` | 

  * **Pre-trained services:** Create, read, update, and delete

| N/A | N/A  
Bucket Admin | `ClusterRoleBinding` | **Bucket and objects:** Read and write | N/A | N/A  
Bucket Object Admin | `ClusterRoleBinding` | 

  * **Bucket:** Read
  * **Objects:** Read and write

| N/A | N/A  
Bucket Object Viewer | `ClusterRoleBinding` | **Bucket and objects:** Read | N/A | N/A  
ConfigMap Editor | `RoleBinding` | **`ConfigMap` resources:** Create, get, list, watch, update, and patch | N/A | N/A  
Custom Role Org Admin | `ClusterRoleBinding` | **Custom Role Org resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Dashboard PA Creator | `ClusterRoleBinding` | `Dashboard` custom resources: Read and write | N/A | N/A  
Dashboard PA Editor | `ClusterRoleBinding` | `Dashboard` custom resources: Read and write | N/A | N/A  
Dashboard PA Viewer | `ClusterRoleBinding` | `Dashboard` custom resources: Read | N/A | N/A  
Flow Log Admin | `ClusterRoleBinding` | **Flow log resources:** Create, get, read, patch, update, and delete | **Flow log resources:** Create, get, read, patch, update, and delete | N/A  
Flow Log Viewer | `ClusterRoleBinding` | **Flow log resources:** Get and read | **Flow log resources:** Get and read | N/A  
GDCHRestrictByAttributes Policy Admin | `ClusterRoleBinding` | **GDCH restricted attributes policies:** Create, edit, and delete | N/A | N/A  
GDCHRestrictedService Policy Admin | `ClusterRoleBinding` | **GDCHRestrictedService Policy resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Identity Provider Federation Admin | `RoleBinding` | **Identity provider configs and secrets:** Create, read, update, patch, and delete | N/A | N/A  
Infra PKI Admin | `RoleBinding` | N/A | 

  * **PKI certificate issuers and certificate authorities** : Get, list, watch, create, update, delete, patch
  * **PKI secrets** : Get, list

| N/A  
Interconnect Admin | `ClusterRoleBinding` | N/A | **Interconnect attachments and attachment groups** : Get, list, watch, create, update, delete, patch | N/A  
LoggingRule PA Creator | `ClusterRoleBinding` | `LoggingRule` custom resources: Read and write | N/A | N/A  
LoggingRule PA Editor | `ClusterRoleBinding` | `LoggingRule` custom resources: Read and write | N/A | N/A  
LoggingRule PA Viewer | `ClusterRoleBinding` | `LoggingRule` custom resources: Read | N/A | N/A  
LoggingTarget PA Creator | `ClusterRoleBinding` | `LoggingTarget` custom resources: Read and write | N/A | N/A  
LoggingTarget PA Editor | `ClusterRoleBinding` | `LoggingTarget` custom resources: Read and write | N/A | N/A  
LoggingTarget PA Viewer | `ClusterRoleBinding` | `LoggingTarget` custom resources: Read | N/A | N/A  
MonitoringRule PA Creator | `ClusterRoleBinding` | `MonitoringRule` custom resources: Read and write | N/A | N/A  
MonitoringRule PA Editor | `ClusterRoleBinding` | `MonitoringRule` custom resources: Read and write | N/A | N/A  
MonitoringRule PA Viewer | `ClusterRoleBinding` | `MonitoringRule` custom resources: Read | N/A | N/A  
MonitoringTarget PA Creator | `ClusterRoleBinding` | `MonitoringTarget` custom resources: Read and write | N/A | N/A  
MonitoringTarget PA Editor | `ClusterRoleBinding` | `MonitoringTarget` custom resources: Read and write | N/A | N/A  
MonitoringTarget PA Viewer | `ClusterRoleBinding` | `MonitoringTarget` custom resources: Read | N/A | N/A  
MP OCLCM Debugger | `ClusterRoleBinding` | 

  * **Components:** Get, list, create
  * **ComponentOverrides, SubcomponentOverrides:** Get, list, create, update, patch
  * **ComponentRollouts, Subcomponents:** Get, list, update, patch

| N/A | N/A  
MP OCLCM Viewer | `ClusterRoleBinding` | **Components, ComponentOverrides, SubcomponentOverrides, ComponentRollouts, Subcomponents:** Get, list | N/A | N/A  
ObservabilityPipeline PA Creator | `ClusterRoleBinding` | `ObservabilityPipeline` custom resources: Read and write | N/A | N/A  
ObservabilityPipeline PA Editor | `ClusterRoleBinding` | `ObservabilityPipeline` custom resources: Read and write | N/A | N/A  
ObservabilityPipeline PA Viewer | `ClusterRoleBinding` | `ObservabilityPipeline` custom resources: Read | N/A | N/A  
Org Network Policy Admin | `RoleBinding` | **`OrganizationNetworkPolicy` in `platform` namespace:** Create, read, update, and delete | N/A | N/A  
Org Session Admin | `RoleBinding` | **Istio authorization resource:** Create, read, update, and delete | N/A | N/A  
Organization Grafana Viewer | `RoleBinding` | **`GrafanaSystem` and Grafana:** Read and write | N/A | N/A  
Organization IAM Viewer | `ClusterRoleBinding` | 

  * **Role-based access control (RBAC) objects:** Read
  * **`OrganizationClusterRole` and `OrganizationClusterRoleBinding`:** Read

| N/A | N/A  
Organization Upgrade Admin | `ClusterRoleBinding` | **Maintenance windows:** Get, list, watch, update, and patch | N/A | N/A  
Organization Upgrade Viewer | `ClusterRoleBinding` | **Maintenance windows:** Get, list, and watch | N/A | N/A  
Project Creator | `ClusterRoleBinding` | 

  * **Project custom resources (CR):** Read and create
  * **Fleet CR:** Read and create
  * **Clusters:** Read

| N/A | N/A  
Project Editor | `ClusterRoleBinding` | 

  * **Project custom resources (CR):** Read, delete, patch, update, and view
  * **Fleet CR:** Read and delete
  * **Cluster CR:** Read

| N/A | N/A  
Subnet Organization Admin | `ClusterRoleBinding` | **Subnet Organization resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
Transfer Appliance Request Creator | `ClusterRoleBinding` | **Transfer Appliance Request resources:** Create, get, list, and watch | N/A | N/A  
Trust Store Viewer | `RoleBinding` | **Trust store secrets:** Get | N/A | N/A  
User Cluster Admin | `ClusterRoleBinding` | 

  * **`AddressPoolClaims`:** Create, read, update, and delete
  * **`UserClusterUpgrade`:** Read and write
  * **`UserClusterMetadata`, `ClusterBgpRouters`, `InventoryMachines`, and project custom resources (CR):** Read
  * **`CidrClaims`:** Create, read, update, and delete
  * **`Namespace`:** Create and delete
  * **`ClusterCidrConfigs` and clusters:** Create, read, update, patch, and delete
  * **`NodeUpgrades`:** Read, create, patch, and update
  * **`HarborClusters`, `Projects`, `UserClusterUpgradeRequests`:** Read

| 

  * **`Clusters` and `NodePoolClaims`:** Read and write
  * **`NodePools`, `MachineClasses`, `VirtualMachineTypes`, and `ClusterInfos`:** Read

| N/A  
User Cluster Developer | `OrganizationRoleBinding` | N/A | **Clusters:** Read and write | N/A  
User Cluster Node Viewer | `OrganizationRoleBinding` | N/A | **Clusters:** Read | N/A  
Volume Replication Admin | `ClusterRoleBinding` | **`Volume failovers, volume relationship replicas`:** Create, get, list, watch, delete | N/A | N/A  
VPN Admin | `RoleBinding` | N/A | 

  * **`VPNGateway`:** Create, read, write
  * **`PeerGateway`:** Create, read, write
  * **`VPNBGPPeer`:** Create, read, write
  * **`VPNTunnel`:** Create, read, write

| N/A  
VPN Viewer | `RoleBinding` | N/A | 

  * **`VPNGateway`:** Read
  * **`PeerGateway`:** Read
  * **`VPNBGPPeer`:** Read
  * **`VPNTunnel`:** Read

| N/A  
Web TLS Certificate Admin | `RoleBinding` | **Web TLS Certificate resources:** Create, get, list, watch, update, patch, and delete | N/A | N/A  
  
### AO Persona, predefined identity and access roles

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
  
### Common predefined identity and access roles

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
