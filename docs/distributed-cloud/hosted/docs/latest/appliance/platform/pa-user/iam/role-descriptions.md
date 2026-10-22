---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-descriptions/
title: Predefined role descriptions \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:56.512713+00:00
---

# Predefined role descriptions  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-descriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Predefined role descriptions Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance has the following predefined roles that you can assign to team members:

## IO roles

IOs have permissions to manage the cluster and the organization's lifecycle. These are the predefined roles that you can assign to team members:

  * **Security Admin** : Creates, updates, and deletes any permissions and policies within the org infrastructure cluster. This role does not have access to organization and project resources.
  * **APPLSTOR debugger** : Access to debug appliance storage.
  * **APPLSTOR monitor** : Access to monitor appliance storage.
  * **APPLSTOR secret rotator** : Access to rotate appliance storage secrets.
  * **AuditLoggingTarget Creator** : Create `AuditLoggingTarget` custom resources in the org infrastructure cluster.
  * **AuditLoggingTarget Editor** : Edit `AuditLoggingTarget` custom resources in the org infrastructure cluster.
  * **AuditLoggingTarget Viewer** : View `AuditLoggingTarget` custom resources in the org infrastructure cluster.
  * **AuditLoggingTarget IO Creator** : Create `AuditLoggingTarget` custom resources in the project namespace.
  * **AuditLoggingTarget IO Editor** : Edit `AuditLoggingTarget` custom resources in the project namespace.
  * **AuditLoggingTarget IO Viewer** : View `AuditLoggingTarget` custom resources in the project namespace.
  * **Audit Logs Backup Restore Creator** : Create a backup transfer job configuration and restore audit logs.
  * **Audit Logs Backup Restore Editor** : Edit the backup transfer job configuration and restore audit logs.
  * **Audit Logs Infra Bucket Viewer** : View backup buckets of infrastructure audit logs.
  * **AIS Admin** : Has read and write access to GKE Identity Service (AIS) pods and deployments.
  * **AIS Debugger** : Has read and write access to AIS resources for mitigation.
  * **AIS Monitor** : Has read access to AIS resources in the `iam-system` namespace.
  * **AuthzPDP Debugger** : Has read and write access on authorization policy decision point (PDP) resources for mitigation and debugging.
  * **Cert Manager System Cluster Debugger** : Manages cert-manager related resources.
  * **Dashboard Creator** : Create `Dashboard` custom resources in the org infrastructure cluster.
  * **Dashboard Editor** : Edit `Dashboard` custom resources in the org infrastructure cluster.
  * **Dashboard Viewer** : View `Dashboard` custom resources in the org infrastructure cluster.
  * **Dashboard IO Creator** : Create `Dashboard` custom resources in the project namespace.
  * **Dashboard IO Editor** : Edit `Dashboard` custom resources in the project namespace.
  * **Dashboard IO Viewer** : View `Dashboard` custom resources in the project namespace.
  * **Debugging AuditLoggingTarget custom resource** : Monitor in the `obs-system` namespace.
  * **DNS Admin** : Updates DNS files.
  * **DNS Debugger** : Has read and write permissions on all DNS resources.
  * **DNS Monitor** : Has read permissions on all DNS resources.
  * **DNS Suffix Viewer** : Views the DNS suffix configmap.
  * **Emergency SSH Creds Admin** : Has emergency access permissions and uses the SSH node in the org infrastructure cluster.
  * **FluentBit Creator** : Create `FluentBit` custom resources in the org infrastructure cluster.
  * **FluentBit Editor** : Edit `FluentBit` custom resources in the org infrastructure cluster.
  * **FluentBit Viewer** : View `FluentBit` custom resources in the org infrastructure cluster.
  * **FluentBit IO Creator** : Create `FluentBit` custom resources in the project namespace.
  * **FluentBit IO Editor** : Edit `FluentBit` custom resources in the project namespace.
  * **FluentBit IO Viewer** : View `FluentBit` custom resources in the project namespace.
  * **Gatekeeper Admin** : Has access to restart deployments and patch secrets. 
  * **Grafana Debugger** : Grants admin access to Grafana resources in the `obs-system` namespace.
  * **Grafana Viewer** : Grants permissions to access the Grafana instance in the system namespace of the org infrastructure cluster.
  * **Hardware Admin** : Has full access to hardware resources such as switches, racks, and servers.
  * **HDWR Admin** : Has full access to hardware-related resources.
  * **HWDR Viewer** : Has read-only access to hardware-related resources.
  * **Infra PKI Debugger** : Has access to configure an infra PKI certificate issuer and certificate authority.
  * **Interconnect Admin** : Has admin access to interconnect resources. 
  * **Kiali Admin** : Grants permissions to access the Kiali dashboard to debug Istio service mesh.
  * **KUB IPAM Debugger** : Has read and write access for `CIDRClaim` custom resources. 
  * **KUB Monitor** : Has read-only permissions for all resources in KUB.
  * **LogCollector Creator** : Create `LogCollector` custom resources in the org infrastructure cluster.
  * **LogCollector Editor** : Edit `LogCollector` custom resources in the org infrastructure cluster.
  * **LogCollector Viewer** : View `LogCollector` custom resources in the org infrastructure cluster.
  * **LogCollector IO Creator** : Create `LogCollector` custom resources in the project namespace.
  * **LogCollector IO Editor** : Edit `LogCollector` custom resources in the project namespace.
  * **LogCollector IO Viewer** : View `LogCollector` custom resources in the project namespace.
  * **LoggingRule Creator** : Create `LoggingRule` custom resources in the org infrastructure cluster.
  * **LoggingRule Editor** : Edit `LoggingRule` custom resources in the org infrastructure cluster.
  * **LoggingRule Viewer** : View `LoggingRule` custom resources in the org infrastructure cluster.
  * **LoggingRule IO Creator** : Create `LoggingRule` custom resources in the project namespace.
  * **LoggingRule IO Editor** : Edit `LoggingRule` custom resources in the project namespace.
  * **LoggingRule IO Viewer** : View `LoggingRule` custom resources in the project namespace.
  * **LoggingTarget IO Creator** : Create `LoggingTarget` custom resources in the project namespace.
  * **LoggingTarget IO Editor** : Edit `LoggingTarget` custom resources in the project namespace.
  * **LoggingTarget IO Viewer** : View `LoggingTarget` custom resources in the project namespace.
  * **Log Query API Querier** : Access the Log Query API to query logs.
  * **MonitoringRule Creator** : Create `MonitoringRule` custom resources in the org infrastructure cluster.
  * **MonitoringRule Editor** : Edit `MonitoringRule` custom resources in the org infrastructure cluster.
  * **MonitoringRule Viewer** : View `MonitoringRule` custom resources in the org infrastructure cluster.
  * **MonitoringRule IO Creator** : Create `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule IO Editor** : Edit `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule IO Viewer** : View `MonitoringRule` custom resources in the project namespace.
  * **MonitoringTarget Creator** : Create `MonitoringTarget` custom resources in the org infrastructure cluster.
  * **MonitoringTarget Editor** : Edit `MonitoringTarget` custom resources in the org infrastructure cluster.
  * **MonitoringTarget Viewer** : View `MonitoringTarget` custom resources in the org infrastructure cluster.
  * **MonitoringTarget IO Creator** : Create `MonitoringTarget` custom resources in the project namespace.
  * **MonitoringTarget IO Editor** : Edit `MonitoringTarget` custom resources in the project namespace.
  * **MonitoringTarget IO Viewer** : View `MonitoringTarget` custom resources in the project namespace.
  * **Observability Admin** : Has read-write access to objects in the `obs-system` namespace.
  * **Observability Admin Debugger** : Has cluster-specific administrator access to observability resources in the `obs-system` namespace. This role grants granular control over access within the org infrastructure cluster.
  * **Observability Debugger** : Has full access to Observability resources in the `obs-system` namespace.
  * **ObservabilityPipeline Creator** : Create `ObservabilityPipeline` custom resources in the org infrastructure cluster.
  * **ObservabilityPipeline Editor** : Edit `ObservabilityPipeline` custom resources in the org infrastructure cluster.
  * **ObservabilityPipeline Viewer** : View `ObservabilityPipeline` custom resources in the org infrastructure cluster.
  * **ObservabilityPipeline IO Creator** : Create `ObservabilityPipeline` custom resources in the project namespace.
  * **ObservabilityPipeline IO Editor** : Edit `ObservabilityPipeline` custom resources in the project namespace.
  * **ObservabilityPipeline IO Viewer** : View `ObservabilityPipeline` custom resources in the project namespace.
  * **Observability System Debugger** : Has organization-wide administrator access to observability resources in the `obs-system` namespace. This role grants centralized management of observability administrator access.
  * **Observability Viewer** : Has read-only access to view objects in the `obs-system` namespace.
  * **OCLCM Debugger** : Has read and write access to debug OCLCM objects.
  * **OCLCM Viewer** : Has read-only access to view OCLCM objects.
  * **Organization Admin** : Creates and deletes organizations and manages the organization's lifecycle.
  * **Organization System Artifact Management Admin** : Has admin access to resources in all Harbor projects in the system namespace.
  * **PERF Admin Monitor** : Has read permission on PERF buckets, service accounts, and secrets.
  * **PERF Admin Resource Maintainer** : Has read and write access on all virtual machines (VM), VM disks, VM external accesses, VM requests, buckets, project service accounts, AEAD keys, Signing keys, and PERF service accounts.
  * **PERF Debugger** : Has read and write access for jobs in the project namespace.
  * **PERF System Monitor** : Has read-only access for all pods and PERF configmaps and cron jobs in the project namespace.
  * **PERF System Resource Maintainer** : Has read and write access to all services in the project namespace.
  * **PNET Debugger** : Has read and write permissions on all PNET resources.
  * **PNET Monitor** : Has read-only permissions on all PNET resources.
  * **PNET Secret Debugger** : Has access to network switch credentials.
  * **PSPF Debugger** : Has read and write permissions for Jobs in the project namespace.
  * **PSPF Monitor** : Monitors PSPF resources.
  * **Policy Admin** : Manages policy templates for the organization and has full access to constraints.
  * **Project Cortex Alertmanager Editor** : Edit the Cortex Alertmanager instance in the project namespace.
  * **Project Cortex Alertmanager Viewer** : View the Cortex Alertmanager instance in the project namespace.
  * **Project Cortex Prometheus Viewer** : View the Cortex Prometheus instance in the project namespace.
  * **Project Grafana Viewer** : View the Grafana instance in the project namespace.
  * **Remote Logger Admin** : Has full access to `remote-logger` resources.
  * **Remote Logger Viewer** : Has read-only access to `remote-logger` resources. 
  * **Root Cortex Alertmanager Editor** : Grants permissions to edit the Cortex Alertmanager instance on the org infrastructure cluster.
  * **Root Cortex Alertmanager Viewer** : Grants permissions to access the Cortex Alertmanager instance on the org infrastructure cluster.
  * **Root Cortex Prometheus Viewer** : Grants permissions to access the Cortex Prometheus instance on the org infrastructure cluster.
  * **Root Session Admin** : Grants access to perform revocation operations in the org infrastructure cluster.
  * **Security Viewer** : Has read-only access to all resources to which the Security Admin has access.
  * **SSH Infra Debugger** : Has read and write access to SSH infra secrets. 
  * **System Artifact Management Admin** : Has admin access to resources in all Harbor projects in the system namespace.
  * **System Artifact Management Secrets Admin** : Has admin access to secret resources to manage registry mirror configurations.
  * **System Artifact Registry Harbor Admin** : Has admin access to Harbor projects.
  * **System Artifact Registry Harbor Read** : Has read-only access to Harbor projects.
  * **System Artifact Registry Harbor ReadWrite** : Has read and write access to Harbor projects.
  * **System Artifact Registry Debugger** : Has read and write access to all Harbor resources.
  * **System Artifact Registry Monitor** : Has read and write access to Harbor resources in the org infrastructure cluster.
  * **System Cluster Admin** : Has read and write access to any permissions and policies within the org infrastructure cluster. This role has access at the organization level.
  * **System Cluster DNS Debugger** : Has create and read access to any permissions within the org infrastructure cluster.
  * **System Cluster Vertex AI Debugger** : Has full access to the Vertex AI platform.
  * **System Cluster Viewer** : Has read-write access to any permissions and policies within the org infrastructure cluster.
  * **System Project VirtualMachine Admin** : Has access to manage VMs in system projects.
  * **Tenable Nessus Admin** : Has read and write access to networking components that manage the Tenable.sc and Nessus applications.
  * **Transfer Appliance Request Admin** : Manages transfer appliance requests created by a Platform Administrator (PA). A transfer appliance allows you to quickly and securely transfer large amounts of data to GDC air-gapped appliance using a high-capacity storage server.
  * **Trust Bundle Root Monitor** : Has read access to trust bundles.
  * **UNET CLI Org Admin Monitor** : Has create and read permissions on UNET resources to run `gdcloud system network` commands in the org infrastructure cluster.
  * **UNET CLI Root Admin Monitor** : Has create and read permissions on UNET resources to run `gdcloud system network` commands in the org infrastructure cluster.
  * **UNET CLI System Monitor** : Has create and read permissions on UNET resources to run `gdcloud system network` commands on org infrastructure clusters.
  * **UNET CLI User Monitor** : Has permissions on UNET resources to run `gdcloud system network` commands on user clusters.
  * **Upgrade Appliance Admin** : Has read-write permissions on performing upgrades on appliances, access to Organization and read-only access to `OrganizationUpgrade`.
  * **Upgrade Debugger** : Has read-write permissions on upgrade resources in the org infrastructure cluster.
  * **User Cluster Debugger** : Has full access to debug and mitigate issues in user clusters.
  * **User Cluster DNS Debugger** : Has create and read permissions in user clusters.
  * **UI Debugger** : Has permissions to restart UI deployments.
  * **VAISEARCH Secret Rotator** : Has permissions to rotate secrets for Agent Search.
  * **VPN Debugger For Management Plane API server** : Has read and write permissions on all resources related to the VPN in the Management API server.
  * **VPN Debugger For Org Perimeter Cluster** : Has read and write permissions on all resources related to the VPN in the Perimeter Cluster.
  * **Web TLS Certificate Debugger** : Has read and write access to the Istio web-tls certificate and secret.



## PA roles

Platform Administrators (PA) manage organization level resources and project lifecycle management. You can assign the following predefined roles to team members:

  * **Organization IAM Admin:** Creates, updates, and deletes any permissions and allow policies within the organization.
  * **AI Platform Admin** : Grant permissions to manage pre-trained services.
  * **Audit Logs Platform Restore Bucket Creator:** Create backup buckets to restore the platform audit logs.
  * **Audit Logs Platform Bucket Viewer:** View backup buckets of platform audit logs.
  * **Bucket Admin:** Manages storage buckets within organizations and projects and the objects in those buckets.
  * **Bucket Admin (global):** Manages single zone buckets within the organization and projects, as well as the objects in those buckets.
  * **Bucket Object Admin:** Has read-only access on buckets within an organization, and read-write access on the objects in those buckets.
  * **Bucket Object Admin (global)** Has read-only on dual-zone buckets within the organization and its projects, as well as read-write on the objects in those buckets.
  * **Bucket Object Viewer:** Has read-only access on buckets within a organization and the objects in those buckets.
  * **Bucket Object Viewer (global)** Has read-only on dual-zone buckets within the organization and its projects, as well as read-only on the objects in those buckets.
  * **Dashboard PA Creator** : Creates `Dashboard` custom resources for the entire organization.
  * **Dashboard PA Editor** : Has read and write access on `Dashboard` custom resources for the entire organization.
  * **Dashboard PA Viewer** : Has read-only access on `Dashboard` custom resources for the entire organization.
  * **Flow Log Admin** : Manages flow log resources for logging network traffic metadata.
  * **Flow Log Viewer** : Provides read-only access to flow log configurations.
  * **GDCH Restrict By Attributes Policy Admin:** Has full access to the `GDCHRestrictByAttributes` constraint.
  * **GDCH Restricted Service Policy Admin:** Manages policy templates for the organization and has full access to constraints. Applies or rolls back policies for an organization or project.
  * **IdP Federation Admin** : Has full access to configure identity providers.
  * **Infra PKI Admin** : Has access to configure an infra PKI certificate issuer and certificate authority. 
  * **Interconnect Admin** : Has admin access to interconnect resources. 
  * **Log Query API Querier** : Has read-only access to reach the audit log or operational log endpoint from the Log Query API to view logs for a project.
  * **LoggingRule PA Creator** : Creates `LoggingRule` custom resources for the entire organization.
  * **LoggingRule PA Editor** : Edits `LoggingRule` custom resources for the entire organization.
  * **LoggingRule PA Viewer** : Views `LoggingRule` custom resources for the entire organization.
  * **LoggingTarget PA Creator** : Creates `LoggingTarget` custom resources for the entire organization.
  * **LoggingTarget PA Editor** : Edits `LoggingTarget` custom resources for the entire organization.
  * **LoggingTarget PA Viewer** : Views `LoggingTarget` custom resources for the entire organization.
  * **MonitoringRule PA Creator** : Creates `MonitoringRule` custom resources for the entire organization.
  * **MonitoringRule PA Editor** : Has read and write access to `MonitoringRule` resources for the entire organization.
  * **MonitoringRule PA Viewer** : Has read-only access to `MonitoringRule` custom resources for the entire organization.
  * **MonitoringTarget PA Creator** : Creates `MonitoringTarget` custom resources for the entire organization.
  * **MonitoringTarget PA Editor** : Has read and write access to `MonitoringTarget` custom resources for the entire organization.
  * **MonitoringTarget PA Viewer** : Has read-only access to `MonitoringTarget` custom resources for the entire organization.
  * **MP OCLCM Debugger** : Debugs OCLCM related objects.
  * **MP OCLCM Viewer** : Views OCLCM related objects.
  * **ObservabilityPipeline PA Creator** : Creates `ObservabilityPipeine` custom resources for the entire organization.
  * **ObservabilityPipeline PA Editor** : Has read and write access on `ObservabilityPipeine` custom resources for the entire organization.
  * **ObservabilityPipeline PA Viewer** : Has read-only access on `ObservabilityPipeline` custom resources for the entire organization. 
  * **Org Session Admin** : Has access to the revocation command. Users bound to this `Role` are added to the ACLs for authentication and authorization. 
  * **Organization Grafana Viewer:** Visualize organization-related observability data on dashboards of the Grafana monitoring instance.
  * **Organization IAM Viewer:** Has read-only access to all resources that the Organization IAM Administrator has access to.
  * **Organization Upgrade Admin:** Modifies maintenance windows for an organization. Maintenance windows are created automatically during organization creation.
  * **Organization Upgrade Viewer:** Views maintenance windows.
  * **Project Bucket Admin:** Manages the dual-zone buckets of a project, as well as the objects in those buckets.
  * **Project Bucket Object Admin:** Has read-only on dual-zone buckets within a project, as well as read-write on the objects in those buckets.
  * **Project Bucket Object Viewer:** Has read-only on dual-zone buckets within a project, as well as read-only on the objects in those buckets.
  * **Project Creator:** Creates new projects.
  * **Project Editor:** Deletes projects.
  * **SIEM Export Org Creator** : Creates `SIEMOrgForwarder` custom resources.
  * **SIEM Export Org Editor** : Has read and write access on `SIEMOrgForwarder` custom resources.
  * **SIEM Export Org Viewer** Has read-only access to view `SIEMOrgForwarder` custom resources.
  * **Transfer Appliance Request Creator:** Can read and create transfer appliance requests, which allow you to quickly and securely transfer large amounts of data to GDC air-gapped appliance using a high capacity storage server.
  * **User Cluster Admin:** Creates, updates, and deletes the user cluster, and manages the user cluster's lifecycle.
  * **User Cluster CRD Viewer** : Read-only access to Custom Resource Definitions (CRDs) within a user cluster.
  * **User Cluster Developer:** Has cluster admin permissions in user clusters.
  * **User Cluster Node Viewer:** Has read-only cluster admin permissions in user clusters.
  * **VPN Admin:** Has read and write permissions on all VPN-related resources.
  * **VPN Viewer:** Has read permissions on all VPN-related resources.



## AO roles

An Application Operator (AO) is a member of the development team within the Platform Administrator (PA) organization. AOs interact with project-level resources. You can assign the following predefined roles to team members:

  * **Project IAM Admin:** Manages the IAM allow policies of projects.
  * **AI OCR Developer** : Access the Optical Character Recognition service to detect text in images.
  * **AI Speech Developer** : Access the Speech-to-Text service to recognize speech and transcribe audio.
  * **AI Translation Developer** : Access the Vertex AI Translation service to translate text.
  * **Artifact Management Admin** : Has admin access to resources in all Harbor projects in the project namespace.
  * **Artifact Management Editor** : Has read and write access to resources in all Harbor projects in the project namespace.
  * **Certificate Authority Service Admin** : Has access to manage certificate authorities and certificate requests in their project.
  * **Certificate Service Admin** : Has access to manage certificates and certificate issuers in their project.
  * **Dashboard Editor** : Has read and write access on `Dashboard` custom resources.
  * **Dashboard Viewer** : Has read-only access on `Dashboard` custom resources.
  * **Harbor Instance Admin** : Has full access to manage Harbor instances in a project.
  * **Harbor Instance Viewer** : Has read-only access to view Harbor instances in a project.
  * **Harbor Project Creator** : Has access to manage Harbor instance projects.
  * **K8s Network Policy Admin** : Manages network policies in Kubernetes clusters.
  * **LoggingRule Creator** : Creates `LoggingRule` custom resources in the project namespace.
  * **LoggingRule Editor** : Edits `LoggingRule` custom resources in the project namespace.
  * **LoggingRule Viewer** : Views `LoggingRule` custom resources in the project namespace.
  * **LoggingTarget Creator** : Creates `LoggingTarget` custom resources in the project namespace.
  * **LoggingTarget Editor** : Edits `LoggingTarget` custom resources in the project namespace.
  * **LoggingTarget Viewer** : Views `LoggingTarget` custom resources in the project namespace.
  * **Load Balancer Admin** : has read and write permissions on all load balancer resources in project namespace.
  * **MonitoringRule Editor** : Has read and write access to `MonitoringRule` resources.
  * **MonitoringRule Viewer** : Has read-only access to `MonitoringRule` custom resources.
  * **MonitoringTarget Editor** : Has read and write access to `MonitoringTarget` custom resources.
  * **MonitoringTarget Viewer** : Has read-only access to `MonitoringTarget` custom resources.
  * **NAT Viewer** : Has read-only access to deployments in Kubernetes clusters.
  * **Namespace Admin** : Manages all resources within the project namespace.
  * **ObservabilityPipeline Editor** : Has read and write access on `ObservabilityPipeine` custom resources.
  * **ObservabilityPipeline Viewer** : Has read-only access on `ObservabilityPipeline` custom resources.
  * **Project Bucket Admin** : Manages the storage buckets and objects within buckets.
  * **Project Bucket Object Admin** : Has read-only access on buckets within a project, and read-write access on the objects in those buckets.
  * **Project Bucket Object Viewer** : Has read-only access on buckets within a project and the objects in those buckets.
  * **Project Cortex Alertmanager Editor** : Grants permissions to edit the Cortex Alertmanager instance in the project namespace.
  * **Project Cortex Alertmanager Viewer** : Grants permissions to access the Cortex Alertmanager instance in the project namespace.
  * **Project Cortex Prometheus Viewer** : Grants permissions to access the Cortex Prometheus instance in the project namespace.
  * **Project Grafana Viewer** : Accesses the Grafana instance in the project namespace of the fleet admin cluster.
  * **Project NetworkPolicy Admin:** Manages the project network policies in the project namespace.
  * **Project Viewer:** Has read-only access to all resources within project namespaces.
  * **Project VirtualMachine Admin** : Manages VMs in the project namespace.
  * **Project VirtualMachine Image Admin** : Manages VM images in the project namespace.
  * **Secret Admin** : Manages Kubernetes secrets in projects.
  * **Secret Viewer** : Views Kubernetes secrets in projects.
  * **Service Configuration Admin** : Has read and write access to service configurations within a project namespace.
  * **Service Configuration Viewer** : Has read access to service configurations within a project namespace.
  * **Volume Replication Admin** : Manages volume replication resources.
  * **Workbench Notebooks Admin** : Get read and write access to all notebook resources within a project namespace.
  * **Workbench Notebooks Viewer** : Get read-only access to all notebook resources within a project namespace and view the Vertex AI Workbench user interface.
  * **Workload Viewer** : Has read access to workloads in a project.



## Common roles

The following predefined common roles apply to all authenticated users:

  * **AI Platform Viewer** : Grants permissions to view pre-trained services.
  * **DNS Suffix Viewer** : Accesses the domain name service (DNS) suffix config map.
  * **Flow Log Admin** : Has read and write access to all Flow Log resources.
  * **Flow Log Viewer** : Has read-only access to all Flow Log resources.
  * **Project Discovery Viewer** : Has read access for all authenticated users to the project view.
  * **Public Image Viewer** : Has read access for all authenticated users on the public VM images in the namespace `vm-images`.
  * **System Artifact Registry anthos-creds secret Monitor** : Has read-only access to secrets in the `anthos-creds` namespace.
  * **System Artifact Registry gpc-system secret Monitor** : Has read-only access to secrets in the `gpc-system` namespace.
  * **System Artifact Registry harbor-system secret Monitor** : Has read-only access to secrets in the `harbor-system` namespace.
  * **Virtual Machine Type Viewer** : Has read access to cluster-scoped virtual machine types.
  * **VM Type Viewer** : Has read access to the predefined virtual machine types on the admin clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
