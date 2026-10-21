---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/predefined-role-permissions/
title: Predefined role permissions for projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:31:58.020365+00:00
---

# Predefined role permissions for projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/predefined-role-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Predefined role permissions for projects Stay organized with collections  Save and categorize content based on your preferences. 

This reference details the predefined roles and permissions available in Google Distributed Cloud (GDC) air-gapped. This information is intended for audiences within the application operator group, such as DevOps teams, when managing access to project-level resources within their deployments. For more information, see [Audiences for GDC documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## About the predefined role table

One subject can be bound to multiple roles in the global API server. Permissions are purely additive; there are no deny rules.

The role table provides you with key details about each role at the project level:

  * **Role name and description:** Lists the predefined role name displayed in the user interface (UI), the name of the corresponding Kubernetes custom resource, and a description of the role.

You might see the same UI display name used for different roles. These roles are distinct, each uniquely identified by its Kubernetes custom resource name and set of permissions. This occurs when roles offer related functionalities or different levels of access to a service.

  * **Permissions:** Lists the specific API operations the role grants. The scope labels indicate where those operations can be performed, which is determined by which API server manages the target resources:

    * **Global:** Resources managed by the global API server.
    * **Zonal:** Resources managed within a specific zone by the zonal management API server.
    * **Kubernetes cluster:** Resources managed within a Kubernetes cluster by its Kubernetes API server.

For more information on how resources are managed within these scopes, see [Global and zonal resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers) and [Kubernetes clusters in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters).




All roles listed have the role type `IAMRole`, which is a Kubernetes custom resource that defines a set of permissions. To grant these permissions to a user or group, create an `IAMRoleBinding` resource, which links the user to the `IAMRole`. For information on how to set up a role binding, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings).

Both `IAMRole` and `IAMRoleBinding` resources are managed within the global API server. This means they are global resources and their bindings are applied across all zones within your GDC organization. While roles are defined globally, the permissions they grant are exercised within a specific context, such as a project. For example, a "project-level role" grants permissions to resources within a project. Such resources might be managed at the global, zonal, or Kubernetes cluster scope.

## Project-level roles and permissions

The following roles are granted within a specific project.

**Role name and description** | **Permissions**  
---|---  
**AI Large Gemini Developer**  
(`ai-large-gemini-developer`) Grants permissions to access the large Gemini service in the project. |  **Zonal** endpoints.large-gemini.gdc.goog.cancel-batch  
endpoints.large-gemini.gdc.goog.cancel-upload  
endpoints.large-gemini.gdc.goog.chat-completions  
endpoints.large-gemini.gdc.goog.complete-upload  
endpoints.large-gemini.gdc.goog.create-batch  
endpoints.large-gemini.gdc.goog.create-cached-content  
endpoints.large-gemini.gdc.goog.create-file  
endpoints.large-gemini.gdc.goog.create-part  
endpoints.large-gemini.gdc.goog.create-upload  
endpoints.large-gemini.gdc.goog.delete-cached-content  
endpoints.large-gemini.gdc.goog.delete-file  
endpoints.large-gemini.gdc.goog.generate-content  
endpoints.large-gemini.gdc.goog.get-batch  
endpoints.large-gemini.gdc.goog.get-cached-content  
endpoints.large-gemini.gdc.goog.get-file  
endpoints.large-gemini.gdc.goog.list-available-models  
endpoints.large-gemini.gdc.goog.list-batches  
endpoints.large-gemini.gdc.goog.list-cached-contents  
endpoints.large-gemini.gdc.goog.list-files  
endpoints.large-gemini.gdc.goog.list-models  
endpoints.large-gemini.gdc.goog.stream-generate-content  
endpoints.large-gemini.gdc.goog.update-cached-content  
  
**AI Large Gemini Viewer**  
(`ai-large-gemini-viewer`) Grants permissions to access the large Gemini service in the project. |  **Zonal** endpoints.large-gemini.gdc.goog.get-batch  
endpoints.large-gemini.gdc.goog.get-cached-content  
endpoints.large-gemini.gdc.goog.get-file  
endpoints.large-gemini.gdc.goog.list-available-models  
endpoints.large-gemini.gdc.goog.list-batches  
endpoints.large-gemini.gdc.goog.list-cached-contents  
endpoints.large-gemini.gdc.goog.list-files  
  
**Backup Creator**  
(`backup-creator`) Creates backups and restores. |  **Kubernetes cluster** backupplans.backup.gdc.goog.get  
backupplans.backup.gdc.goog.list  
backupplans.backup.gdc.goog.watch  
backups.backup.gdc.goog.get  
backups.backup.gdc.goog.list  
backups.backup.gdc.goog.watch  
deletebackuprequests.backup.gdc.goog.get  
deletebackuprequests.backup.gdc.goog.list  
deletebackuprequests.backup.gdc.goog.watch  
manualbackuprequests.backup.gdc.goog.create  
manualbackuprequests.backup.gdc.goog.delete  
manualbackuprequests.backup.gdc.goog.get  
manualbackuprequests.backup.gdc.goog.list  
manualbackuprequests.backup.gdc.goog.watch  
manualrestorerequests.backup.gdc.goog.create  
manualrestorerequests.backup.gdc.goog.delete  
manualrestorerequests.backup.gdc.goog.get  
manualrestorerequests.backup.gdc.goog.list  
manualrestorerequests.backup.gdc.goog.watch  
restoreplans.backup.gdc.goog.get  
restoreplans.backup.gdc.goog.list  
restoreplans.backup.gdc.goog.watch  
restores.backup.gdc.goog.get  
restores.backup.gdc.goog.list  
restores.backup.gdc.goog.watch  
volumebackups.backup.gdc.goog.get  
volumebackups.backup.gdc.goog.list  
volumebackups.backup.gdc.goog.watch  
volumerestores.backup.gdc.goog.get  
volumerestores.backup.gdc.goog.list  
volumerestores.backup.gdc.goog.watch  
  
**Backup Viewer**  
(`backup-viewer`) Views backups and restores. |  **Kubernetes cluster** backupplans.backup.gdc.goog.get  
backupplans.backup.gdc.goog.list  
backupplans.backup.gdc.goog.watch  
backups.backup.gdc.goog.get  
backups.backup.gdc.goog.list  
backups.backup.gdc.goog.watch  
deletebackuprequests.backup.gdc.goog.get  
deletebackuprequests.backup.gdc.goog.list  
deletebackuprequests.backup.gdc.goog.watch  
manualbackuprequests.backup.gdc.goog.get  
manualbackuprequests.backup.gdc.goog.list  
manualbackuprequests.backup.gdc.goog.watch  
manualrestorerequests.backup.gdc.goog.get  
manualrestorerequests.backup.gdc.goog.list  
manualrestorerequests.backup.gdc.goog.watch  
restoreplans.backup.gdc.goog.get  
restoreplans.backup.gdc.goog.list  
restoreplans.backup.gdc.goog.watch  
restores.backup.gdc.goog.get  
restores.backup.gdc.goog.list  
restores.backup.gdc.goog.watch  
volumebackups.backup.gdc.goog.get  
volumebackups.backup.gdc.goog.list  
volumebackups.backup.gdc.goog.watch  
volumerestores.backup.gdc.goog.get  
volumerestores.backup.gdc.goog.list  
volumerestores.backup.gdc.goog.watch  
  
**Bookstore Admin**  
(`bookstore-admin`) Creates and views Bookstore Shelves. |  **Zonal** shelves.bookstore-grpc.googleapis.com.create  
shelves.bookstore-grpc.googleapis.com.get  
shelves.cloudresourcemanager.googleapis.com.create  
shelves.cloudresourcemanager.googleapis.com.get  
  
**Bookstore Viewer**  
(`bookstore-viewer`) Views Bookstore Shelves. |  **Zonal** shelves.bookstore-grpc.googleapis.com.get  
shelves.cloudresourcemanager.googleapis.com.get  
  
**Bucket Object Project Admin**  
(`project-bucket-object-admin`) Reads global project Bucket CRs; reads metadata of the corresponding backend buckets, and manages objects in those buckets, via the S3 API |  **Global** buckets.object.global.gdc.goog.get  
buckets.object.global.gdc.goog.list  
buckets.object.global.gdc.goog.read-object  
buckets.object.global.gdc.goog.watch  
buckets.object.global.gdc.goog.write-object  
  
**Zonal** bucketinfos.object.gdc.goog.get  
bucketinfos.object.gdc.goog.list  
buckets.object.gdc.goog.get  
buckets.object.gdc.goog.list  
buckets.object.gdc.goog.read-object  
buckets.object.gdc.goog.watch  
buckets.object.gdc.goog.write-object  
  
**Bucket Object Project Viewer**  
(`project-bucket-object-viewer`) Reads global project Bucket CRs; reads metadata of the corresponding backend buckets, and reads objects in those buckets, via the S3 API. |  **Global** bucketlocations.object.global.gdc.goog.get  
bucketlocations.object.global.gdc.goog.list  
buckets.object.global.gdc.goog.get  
buckets.object.global.gdc.goog.list  
buckets.object.global.gdc.goog.read-object  
buckets.object.global.gdc.goog.watch  
  
**Zonal** bucketinfos.object.gdc.goog.get  
bucketinfos.object.gdc.goog.list  
buckets.object.gdc.goog.get  
buckets.object.gdc.goog.list  
buckets.object.gdc.goog.read-object  
buckets.object.gdc.goog.watch  
  
**Bucket Project Admin**  
(`project-bucket-admin`) Manages global project Bucket CRs; reads metadata of the corresponding backend buckets, and manages objects in those buckets, via the S3 API. |  **Global** bucketlocations.object.global.gdc.goog.get  
bucketlocations.object.global.gdc.goog.list  
buckets.object.global.gdc.goog.create  
buckets.object.global.gdc.goog.delete  
buckets.object.global.gdc.goog.get  
buckets.object.global.gdc.goog.list  
buckets.object.global.gdc.goog.patch  
buckets.object.global.gdc.goog.read-object  
buckets.object.global.gdc.goog.update  
buckets.object.global.gdc.goog.watch  
buckets.object.global.gdc.goog.write-object  
  
**Zonal** bucketinfos.object.gdc.goog.get  
bucketinfos.object.gdc.goog.list  
bucketinfos.object.gdc.goog.patch  
bucketinfos.object.gdc.goog.update  
bucketinfos.object.gdc.goog.watch  
buckets.object.gdc.goog.create  
buckets.object.gdc.goog.delete  
buckets.object.gdc.goog.get  
buckets.object.gdc.goog.list  
buckets.object.gdc.goog.patch  
buckets.object.gdc.goog.read-object  
buckets.object.gdc.goog.update  
buckets.object.gdc.goog.watch  
buckets.object.gdc.goog.write-object  
  
**CA Service Certificate Requester**  
(`certificate-authority-service-certificate-requester`) Creates and views certificate requests and retrieves issued certificates. |  **Zonal** certificaterequests.pki.security.gdc.goog.create  
certificaterequests.pki.security.gdc.goog.get  
certificaterequests.pki.security.gdc.goog.list  
secrets.get  
secrets.list  
  
**CA Service Operation Manager**  
(`certificate-authority-service-operation-manager`) Manages Certificate Authorities and revokes certificates. |  **Zonal** certificateauthorities.pki.security.gdc.goog.create  
certificateauthorities.pki.security.gdc.goog.delete  
certificateauthorities.pki.security.gdc.goog.get  
certificateauthorities.pki.security.gdc.goog.list  
certificateauthorities.pki.security.gdc.goog.patch  
certificateauthorities.pki.security.gdc.goog.update  
certificateauthorities.pki.security.gdc.goog.watch  
certificaterequests.pki.security.gdc.goog.get  
certificaterequests.pki.security.gdc.goog.list  
certificaterequests.pki.security.gdc.goog.watch  
revokecertificaterequests.pki.security.gdc.goog.create  
revokecertificaterequests.pki.security.gdc.goog.delete  
revokecertificaterequests.pki.security.gdc.goog.get  
revokecertificaterequests.pki.security.gdc.goog.list  
revokecertificaterequests.pki.security.gdc.goog.patch  
revokecertificaterequests.pki.security.gdc.goog.update  
revokecertificaterequests.pki.security.gdc.goog.watch  
secrets.get  
secrets.list  
  
**Certificate Authority Service Admin**  
(`certificate-authority-service-admin`) Creates and manages CertificateAuthorities, CertificateRequests, and RevokeCertificateRequests. |  **Zonal** certificateauthorities.pki.security.gdc.goog.create  
certificateauthorities.pki.security.gdc.goog.delete  
certificateauthorities.pki.security.gdc.goog.get  
certificateauthorities.pki.security.gdc.goog.list  
certificateauthorities.pki.security.gdc.goog.patch  
certificateauthorities.pki.security.gdc.goog.update  
certificateauthorities.pki.security.gdc.goog.watch  
certificaterequests.pki.security.gdc.goog.create  
certificaterequests.pki.security.gdc.goog.delete  
certificaterequests.pki.security.gdc.goog.get  
certificaterequests.pki.security.gdc.goog.list  
certificaterequests.pki.security.gdc.goog.patch  
certificaterequests.pki.security.gdc.goog.update  
certificaterequests.pki.security.gdc.goog.watch  
revokecertificaterequests.pki.security.gdc.goog.create  
revokecertificaterequests.pki.security.gdc.goog.delete  
revokecertificaterequests.pki.security.gdc.goog.get  
revokecertificaterequests.pki.security.gdc.goog.list  
revokecertificaterequests.pki.security.gdc.goog.patch  
revokecertificaterequests.pki.security.gdc.goog.update  
revokecertificaterequests.pki.security.gdc.goog.watch  
secrets.get  
secrets.list  
  
**Certificate Authority Service Viewer**  
(`certificate-authority-service-viewer`) Viewer access to CertificateAuthorities, CertificateRequests, and RevokeCertificateRequests. |  **Zonal** certificateauthorities.pki.security.gdc.goog.get  
certificateauthorities.pki.security.gdc.goog.list  
certificaterequests.pki.security.gdc.goog.get  
certificaterequests.pki.security.gdc.goog.list  
revokecertificaterequests.pki.security.gdc.goog.get  
revokecertificaterequests.pki.security.gdc.goog.list  
secrets.get  
secrets.list  
  
**Certificate Service Admin**  
(`certificate-service-admin`) Creates and manages Certificates and CertificateIssuers. |  **Zonal** certificateissuers.pki.security.gdc.goog.create  
certificateissuers.pki.security.gdc.goog.delete  
certificateissuers.pki.security.gdc.goog.get  
certificateissuers.pki.security.gdc.goog.list  
certificateissuers.pki.security.gdc.goog.patch  
certificateissuers.pki.security.gdc.goog.update  
certificateissuers.pki.security.gdc.goog.watch  
certificates.pki.security.gdc.goog.create  
certificates.pki.security.gdc.goog.delete  
certificates.pki.security.gdc.goog.get  
certificates.pki.security.gdc.goog.list  
certificates.pki.security.gdc.goog.patch  
certificates.pki.security.gdc.goog.update  
certificates.pki.security.gdc.goog.watch  
  
**Certificate Service Viewer**  
(`certificate-service-viewer`) Views Certificates and CertificateIssuers. |  **Zonal** certificateissuers.pki.security.gdc.goog.get  
certificateissuers.pki.security.gdc.goog.list  
certificateissuers.pki.security.gdc.goog.watch  
certificates.pki.security.gdc.goog.get  
certificates.pki.security.gdc.goog.list  
certificates.pki.security.gdc.goog.watch  
  
**Cloud NAT Developer**  
(`cloud-nat-developer`) Able to CRUD CloudNAT resources in the project. |  **Zonal** cloudnatgateways.networking.gdc.goog.create  
cloudnatgateways.networking.gdc.goog.delete  
cloudnatgateways.networking.gdc.goog.get  
cloudnatgateways.networking.gdc.goog.list  
cloudnatgateways.networking.gdc.goog.patch  
cloudnatgateways.networking.gdc.goog.update  
cloudnatgateways.networking.gdc.goog.watch  
  
**Cloud NAT Manager**  
(`cloud-nat-manager`) Able to CRUD CloudNAT resources in the project. |  **Zonal** cloudnatgateways.networking.gdc.goog.create  
cloudnatgateways.networking.gdc.goog.delete  
cloudnatgateways.networking.gdc.goog.get  
cloudnatgateways.networking.gdc.goog.list  
cloudnatgateways.networking.gdc.goog.patch  
cloudnatgateways.networking.gdc.goog.update  
cloudnatgateways.networking.gdc.goog.watch  
  
**Cloud NAT Viewer**  
(`cloud-nat-viewer`) Able to view CloudNAT resources/status in the project |  **Zonal** cloudnatgateways.networking.gdc.goog.get  
cloudnatgateways.networking.gdc.goog.list  
cloudnatgateways.networking.gdc.goog.watch  
  
**Cluster Backup User**  
(`clusterbackup-user`) Grants view access to cluster backup and restore plans, and full access to cluster backups and restores. |  **Zonal** clusterbackupplans.backup.gdc.goog.get  
clusterbackupplans.backup.gdc.goog.list  
clusterbackupplans.backup.gdc.goog.watch  
clusterbackups.backup.gdc.goog.get  
clusterbackups.backup.gdc.goog.list  
clusterbackups.backup.gdc.goog.watch  
clusterrestoreplans.backup.gdc.goog.get  
clusterrestoreplans.backup.gdc.goog.list  
clusterrestoreplans.backup.gdc.goog.watch  
clusterrestores.backup.gdc.goog.get  
clusterrestores.backup.gdc.goog.list  
clusterrestores.backup.gdc.goog.watch  
manualclusterbackuprequest.backup.gdc.goog.create  
manualclusterbackuprequest.backup.gdc.goog.delete  
manualclusterbackuprequest.backup.gdc.goog.get  
manualclusterbackuprequest.backup.gdc.goog.list  
manualclusterbackuprequest.backup.gdc.goog.patch  
manualclusterbackuprequest.backup.gdc.goog.update  
manualclusterbackuprequest.backup.gdc.goog.watch  
manualclusterrestorerequest.backup.gdc.goog.create  
manualclusterrestorerequest.backup.gdc.goog.delete  
manualclusterrestorerequest.backup.gdc.goog.get  
manualclusterrestorerequest.backup.gdc.goog.list  
manualclusterrestorerequest.backup.gdc.goog.patch  
manualclusterrestorerequest.backup.gdc.goog.update  
manualclusterrestorerequest.backup.gdc.goog.watch  
  
**Cluster Backup Viewer**  
(`clusterbackup-viewer`) Grants view access to cluster backups, cluster restores, cluster backup plans, and cluster restore plans. |  **Zonal** clusterbackupplans.backup.gdc.goog.get  
clusterbackupplans.backup.gdc.goog.list  
clusterbackupplans.backup.gdc.goog.watch  
clusterbackups.backup.gdc.goog.get  
clusterbackups.backup.gdc.goog.list  
clusterbackups.backup.gdc.goog.watch  
clusterrestoreplans.backup.gdc.goog.get  
clusterrestoreplans.backup.gdc.goog.list  
clusterrestoreplans.backup.gdc.goog.watch  
clusterrestores.backup.gdc.goog.get  
clusterrestores.backup.gdc.goog.list  
clusterrestores.backup.gdc.goog.watch  
manualclusterbackuprequest.backup.gdc.goog.get  
manualclusterbackuprequest.backup.gdc.goog.list  
manualclusterbackuprequest.backup.gdc.goog.watch  
manualclusterrestorerequest.backup.gdc.goog.get  
manualclusterrestorerequest.backup.gdc.goog.list  
manualclusterrestorerequest.backup.gdc.goog.watch  
  
**Custom Role Project Admin**  
(`custom-role-project-admin`) Manages custom roles in project namespaces. |  **Global** customroles.iam.global.gdc.goog.create  
customroles.iam.global.gdc.goog.delete  
customroles.iam.global.gdc.goog.get  
customroles.iam.global.gdc.goog.list  
customroles.iam.global.gdc.goog.patch  
customroles.iam.global.gdc.goog.update  
customroles.iam.global.gdc.goog.watch  
iamroles.iam.global.gdc.goog.get  
iamroles.iam.global.gdc.goog.list  
roles.rbac.authorization.k8s.io.get  
  
**Zonal** customroles.iam.gdc.goog.create  
customroles.iam.gdc.goog.delete  
customroles.iam.gdc.goog.get  
customroles.iam.gdc.goog.list  
customroles.iam.gdc.goog.patch  
customroles.iam.gdc.goog.update  
customroles.iam.gdc.goog.watch  
projectroles.resourcemanager.gdc.goog.get  
roles.rbac.authorization.k8s.io.get  
  
**Custom Role Project Viewer**  
(`custom-role-project-viewer`) Views custom roles in project namespaces. |  **Global** customroles.iam.global.gdc.goog.get  
customroles.iam.global.gdc.goog.list  
customroles.iam.global.gdc.goog.watch  
iamroles.iam.global.gdc.goog.get  
iamroles.iam.global.gdc.goog.list  
roles.rbac.authorization.k8s.io.get  
  
**Zonal** customroles.iam.gdc.goog.get  
customroles.iam.gdc.goog.list  
customroles.iam.gdc.goog.watch  
projectroles.resourcemanager.gdc.goog.get  
roles.rbac.authorization.k8s.io.get  
  
**Dashboard Editor**  
(`dashboard-editor`) Edits dashboards. |  **Zonal** configmaps.create  
configmaps.delete  
configmaps.get  
configmaps.list  
configmaps.patch  
configmaps.update  
configmaps.watch  
dashboards.observability.gdc.goog.delete  
dashboards.observability.gdc.goog.get  
dashboards.observability.gdc.goog.list  
dashboards.observability.gdc.goog.patch  
dashboards.observability.gdc.goog.update  
dashboards.observability.gdc.goog.watch  
  
**Dashboard Viewer**  
(`dashboard-viewer`) Views dashboards. |  **Zonal** dashboards.observability.gdc.goog.get  
dashboards.observability.gdc.goog.list  
dashboards.observability.gdc.goog.watch  
  
**Database Project Admin**  
(`project-db-admin`) Manages global project database resources. |  **Global** backupplans.alloydbomni.dbadmin.gdc.goog.create  
backupplans.alloydbomni.dbadmin.gdc.goog.delete  
backupplans.alloydbomni.dbadmin.gdc.goog.get  
backupplans.alloydbomni.dbadmin.gdc.goog.list  
backupplans.alloydbomni.dbadmin.gdc.goog.patch  
backupplans.alloydbomni.dbadmin.gdc.goog.update  
backupplans.alloydbomni.dbadmin.gdc.goog.watch  
backupplans.oracle.dbadmin.gdc.goog.create  
backupplans.oracle.dbadmin.gdc.goog.delete  
backupplans.oracle.dbadmin.gdc.goog.get  
backupplans.oracle.dbadmin.gdc.goog.list  
backupplans.oracle.dbadmin.gdc.goog.patch  
backupplans.oracle.dbadmin.gdc.goog.update  
backupplans.oracle.dbadmin.gdc.goog.watch  
backupplans.postgresql.dbadmin.gdc.goog.create  
backupplans.postgresql.dbadmin.gdc.goog.delete  
backupplans.postgresql.dbadmin.gdc.goog.get  
backupplans.postgresql.dbadmin.gdc.goog.list  
backupplans.postgresql.dbadmin.gdc.goog.patch  
backupplans.postgresql.dbadmin.gdc.goog.update  
backupplans.postgresql.dbadmin.gdc.goog.watch  
backups.alloydbomni.dbadmin.gdc.goog.get  
backups.alloydbomni.dbadmin.gdc.goog.list  
backups.alloydbomni.dbadmin.gdc.goog.watch  
backups.oracle.dbadmin.gdc.goog.get  
backups.oracle.dbadmin.gdc.goog.list  
backups.oracle.dbadmin.gdc.goog.watch  
backups.postgresql.dbadmin.gdc.goog.get  
backups.postgresql.dbadmin.gdc.goog.list  
backups.postgresql.dbadmin.gdc.goog.watch  
configmaps.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.create  
dbclusters.alloydbomni.dbadmin.gdc.goog.delete  
dbclusters.alloydbomni.dbadmin.gdc.goog.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.list  
dbclusters.alloydbomni.dbadmin.gdc.goog.patch  
dbclusters.alloydbomni.dbadmin.gdc.goog.update  
dbclusters.alloydbomni.dbadmin.gdc.goog.watch  
dbclusters.oracle.dbadmin.gdc.goog.create  
dbclusters.oracle.dbadmin.gdc.goog.delete  
dbclusters.oracle.dbadmin.gdc.goog.get  
dbclusters.oracle.dbadmin.gdc.goog.list  
dbclusters.oracle.dbadmin.gdc.goog.patch  
dbclusters.oracle.dbadmin.gdc.goog.update  
dbclusters.oracle.dbadmin.gdc.goog.watch  
dbclusters.postgresql.dbadmin.gdc.goog.create  
dbclusters.postgresql.dbadmin.gdc.goog.delete  
dbclusters.postgresql.dbadmin.gdc.goog.get  
dbclusters.postgresql.dbadmin.gdc.goog.list  
dbclusters.postgresql.dbadmin.gdc.goog.patch  
dbclusters.postgresql.dbadmin.gdc.goog.update  
dbclusters.postgresql.dbadmin.gdc.goog.watch  
exports.alloydbomni.dbadmin.gdc.goog.create  
exports.alloydbomni.dbadmin.gdc.goog.delete  
exports.alloydbomni.dbadmin.gdc.goog.get  
exports.alloydbomni.dbadmin.gdc.goog.list  
exports.alloydbomni.dbadmin.gdc.goog.watch  
exports.oracle.dbadmin.gdc.goog.create  
exports.oracle.dbadmin.gdc.goog.delete  
exports.oracle.dbadmin.gdc.goog.get  
exports.oracle.dbadmin.gdc.goog.list  
exports.oracle.dbadmin.gdc.goog.watch  
exports.postgresql.dbadmin.gdc.goog.create  
exports.postgresql.dbadmin.gdc.goog.delete  
exports.postgresql.dbadmin.gdc.goog.get  
exports.postgresql.dbadmin.gdc.goog.list  
exports.postgresql.dbadmin.gdc.goog.watch  
externalservers.alloydbomni.dbadmin.gdc.goog.create  
externalservers.alloydbomni.dbadmin.gdc.goog.delete  
externalservers.alloydbomni.dbadmin.gdc.goog.get  
externalservers.alloydbomni.dbadmin.gdc.goog.list  
externalservers.alloydbomni.dbadmin.gdc.goog.patch  
externalservers.alloydbomni.dbadmin.gdc.goog.update  
externalservers.alloydbomni.dbadmin.gdc.goog.watch  
externalservers.postgresql.dbadmin.gdc.goog.create  
externalservers.postgresql.dbadmin.gdc.goog.delete  
externalservers.postgresql.dbadmin.gdc.goog.get  
externalservers.postgresql.dbadmin.gdc.goog.list  
externalservers.postgresql.dbadmin.gdc.goog.patch  
externalservers.postgresql.dbadmin.gdc.goog.update  
externalservers.postgresql.dbadmin.gdc.goog.watch  
failovers.fleet.dbadmin.gdc.goog.create  
failovers.fleet.dbadmin.gdc.goog.delete  
failovers.fleet.dbadmin.gdc.goog.get  
failovers.fleet.dbadmin.gdc.goog.list  
failovers.fleet.dbadmin.gdc.goog.watch  
imports.alloydbomni.dbadmin.gdc.goog.create  
imports.alloydbomni.dbadmin.gdc.goog.delete  
imports.alloydbomni.dbadmin.gdc.goog.get  
imports.alloydbomni.dbadmin.gdc.goog.list  
imports.alloydbomni.dbadmin.gdc.goog.watch  
imports.oracle.dbadmin.gdc.goog.create  
imports.oracle.dbadmin.gdc.goog.delete  
imports.oracle.dbadmin.gdc.goog.get  
imports.oracle.dbadmin.gdc.goog.list  
imports.oracle.dbadmin.gdc.goog.watch  
imports.postgresql.dbadmin.gdc.goog.create  
imports.postgresql.dbadmin.gdc.goog.delete  
imports.postgresql.dbadmin.gdc.goog.get  
imports.postgresql.dbadmin.gdc.goog.list  
imports.postgresql.dbadmin.gdc.goog.watch  
migrations.alloydbomni.dbadmin.gdc.goog.create  
migrations.alloydbomni.dbadmin.gdc.goog.delete  
migrations.alloydbomni.dbadmin.gdc.goog.get  
migrations.alloydbomni.dbadmin.gdc.goog.list  
migrations.alloydbomni.dbadmin.gdc.goog.patch  
migrations.alloydbomni.dbadmin.gdc.goog.update  
migrations.alloydbomni.dbadmin.gdc.goog.watch  
migrations.postgresql.dbadmin.gdc.goog.create  
migrations.postgresql.dbadmin.gdc.goog.delete  
migrations.postgresql.dbadmin.gdc.goog.get  
migrations.postgresql.dbadmin.gdc.goog.list  
migrations.postgresql.dbadmin.gdc.goog.patch  
migrations.postgresql.dbadmin.gdc.goog.update  
migrations.postgresql.dbadmin.gdc.goog.watch  
replications.postgresql.dbadmin.gdc.goog.create  
replications.postgresql.dbadmin.gdc.goog.delete  
replications.postgresql.dbadmin.gdc.goog.get  
replications.postgresql.dbadmin.gdc.goog.list  
replications.postgresql.dbadmin.gdc.goog.patch  
replications.postgresql.dbadmin.gdc.goog.update  
replications.postgresql.dbadmin.gdc.goog.watch  
restores.alloydbomni.dbadmin.gdc.goog.create  
restores.alloydbomni.dbadmin.gdc.goog.delete  
restores.alloydbomni.dbadmin.gdc.goog.get  
restores.alloydbomni.dbadmin.gdc.goog.list  
restores.alloydbomni.dbadmin.gdc.goog.watch  
restores.oracle.dbadmin.gdc.goog.create  
restores.oracle.dbadmin.gdc.goog.delete  
restores.oracle.dbadmin.gdc.goog.get  
restores.oracle.dbadmin.gdc.goog.list  
restores.oracle.dbadmin.gdc.goog.watch  
restores.postgresql.dbadmin.gdc.goog.create  
restores.postgresql.dbadmin.gdc.goog.delete  
restores.postgresql.dbadmin.gdc.goog.get  
restores.postgresql.dbadmin.gdc.goog.list  
restores.postgresql.dbadmin.gdc.goog.watch  
secrets.create  
secrets.delete  
secrets.get  
secrets.list  
secrets.update  
  
**Zonal** backupplans.alloydbomni.dbadmin.gdc.goog.create  
backupplans.alloydbomni.dbadmin.gdc.goog.delete  
backupplans.alloydbomni.dbadmin.gdc.goog.get  
backupplans.alloydbomni.dbadmin.gdc.goog.list  
backupplans.alloydbomni.dbadmin.gdc.goog.patch  
backupplans.alloydbomni.dbadmin.gdc.goog.update  
backupplans.alloydbomni.dbadmin.gdc.goog.watch  
backupplans.oracle.dbadmin.gdc.goog.create  
backupplans.oracle.dbadmin.gdc.goog.delete  
backupplans.oracle.dbadmin.gdc.goog.get  
backupplans.oracle.dbadmin.gdc.goog.list  
backupplans.oracle.dbadmin.gdc.goog.patch  
backupplans.oracle.dbadmin.gdc.goog.update  
backupplans.oracle.dbadmin.gdc.goog.watch  
backupplans.postgresql.dbadmin.gdc.goog.create  
backupplans.postgresql.dbadmin.gdc.goog.delete  
backupplans.postgresql.dbadmin.gdc.goog.get  
backupplans.postgresql.dbadmin.gdc.goog.list  
backupplans.postgresql.dbadmin.gdc.goog.patch  
backupplans.postgresql.dbadmin.gdc.goog.update  
backupplans.postgresql.dbadmin.gdc.goog.watch  
backups.alloydbomni.dbadmin.gdc.goog.get  
backups.alloydbomni.dbadmin.gdc.goog.list  
backups.alloydbomni.dbadmin.gdc.goog.watch  
backups.oracle.dbadmin.gdc.goog.get  
backups.oracle.dbadmin.gdc.goog.list  
backups.oracle.dbadmin.gdc.goog.watch  
backups.postgresql.dbadmin.gdc.goog.get  
backups.postgresql.dbadmin.gdc.goog.list  
backups.postgresql.dbadmin.gdc.goog.watch  
configmaps.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.create  
dbclusters.alloydbomni.dbadmin.gdc.goog.delete  
dbclusters.alloydbomni.dbadmin.gdc.goog.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.list  
dbclusters.alloydbomni.dbadmin.gdc.goog.patch  
dbclusters.alloydbomni.dbadmin.gdc.goog.update  
dbclusters.alloydbomni.dbadmin.gdc.goog.watch  
dbclusters.oracle.dbadmin.gdc.goog.create  
dbclusters.oracle.dbadmin.gdc.goog.delete  
dbclusters.oracle.dbadmin.gdc.goog.get  
dbclusters.oracle.dbadmin.gdc.goog.list  
dbclusters.oracle.dbadmin.gdc.goog.patch  
dbclusters.oracle.dbadmin.gdc.goog.update  
dbclusters.oracle.dbadmin.gdc.goog.watch  
dbclusters.postgresql.dbadmin.gdc.goog.create  
dbclusters.postgresql.dbadmin.gdc.goog.delete  
dbclusters.postgresql.dbadmin.gdc.goog.get  
dbclusters.postgresql.dbadmin.gdc.goog.list  
dbclusters.postgresql.dbadmin.gdc.goog.patch  
dbclusters.postgresql.dbadmin.gdc.goog.update  
dbclusters.postgresql.dbadmin.gdc.goog.watch  
exports.alloydbomni.dbadmin.gdc.goog.create  
exports.alloydbomni.dbadmin.gdc.goog.delete  
exports.alloydbomni.dbadmin.gdc.goog.get  
exports.alloydbomni.dbadmin.gdc.goog.list  
exports.alloydbomni.dbadmin.gdc.goog.watch  
exports.oracle.dbadmin.gdc.goog.create  
exports.oracle.dbadmin.gdc.goog.delete  
exports.oracle.dbadmin.gdc.goog.get  
exports.oracle.dbadmin.gdc.goog.list  
exports.oracle.dbadmin.gdc.goog.watch  
exports.postgresql.dbadmin.gdc.goog.create  
exports.postgresql.dbadmin.gdc.goog.delete  
exports.postgresql.dbadmin.gdc.goog.get  
exports.postgresql.dbadmin.gdc.goog.list  
exports.postgresql.dbadmin.gdc.goog.watch  
externalservers.alloydbomni.dbadmin.gdc.goog.create  
externalservers.alloydbomni.dbadmin.gdc.goog.delete  
externalservers.alloydbomni.dbadmin.gdc.goog.get  
externalservers.alloydbomni.dbadmin.gdc.goog.list  
externalservers.alloydbomni.dbadmin.gdc.goog.patch  
externalservers.alloydbomni.dbadmin.gdc.goog.update  
externalservers.alloydbomni.dbadmin.gdc.goog.watch  
externalservers.postgresql.dbadmin.gdc.goog.create  
externalservers.postgresql.dbadmin.gdc.goog.delete  
externalservers.postgresql.dbadmin.gdc.goog.get  
externalservers.postgresql.dbadmin.gdc.goog.list  
externalservers.postgresql.dbadmin.gdc.goog.patch  
externalservers.postgresql.dbadmin.gdc.goog.update  
externalservers.postgresql.dbadmin.gdc.goog.watch  
failovers.fleet.dbadmin.gdc.goog.create  
failovers.fleet.dbadmin.gdc.goog.delete  
failovers.fleet.dbadmin.gdc.goog.get  
failovers.fleet.dbadmin.gdc.goog.list  
failovers.fleet.dbadmin.gdc.goog.watch  
imports.alloydbomni.dbadmin.gdc.goog.create  
imports.alloydbomni.dbadmin.gdc.goog.delete  
imports.alloydbomni.dbadmin.gdc.goog.get  
imports.alloydbomni.dbadmin.gdc.goog.list  
imports.alloydbomni.dbadmin.gdc.goog.watch  
imports.oracle.dbadmin.gdc.goog.create  
imports.oracle.dbadmin.gdc.goog.delete  
imports.oracle.dbadmin.gdc.goog.get  
imports.oracle.dbadmin.gdc.goog.list  
imports.oracle.dbadmin.gdc.goog.watch  
imports.postgresql.dbadmin.gdc.goog.create  
imports.postgresql.dbadmin.gdc.goog.delete  
imports.postgresql.dbadmin.gdc.goog.get  
imports.postgresql.dbadmin.gdc.goog.list  
imports.postgresql.dbadmin.gdc.goog.watch  
migrations.alloydbomni.dbadmin.gdc.goog.create  
migrations.alloydbomni.dbadmin.gdc.goog.delete  
migrations.alloydbomni.dbadmin.gdc.goog.get  
migrations.alloydbomni.dbadmin.gdc.goog.list  
migrations.alloydbomni.dbadmin.gdc.goog.patch  
migrations.alloydbomni.dbadmin.gdc.goog.update  
migrations.alloydbomni.dbadmin.gdc.goog.watch  
migrations.postgresql.dbadmin.gdc.goog.create  
migrations.postgresql.dbadmin.gdc.goog.delete  
migrations.postgresql.dbadmin.gdc.goog.get  
migrations.postgresql.dbadmin.gdc.goog.list  
migrations.postgresql.dbadmin.gdc.goog.patch  
migrations.postgresql.dbadmin.gdc.goog.update  
migrations.postgresql.dbadmin.gdc.goog.watch  
replications.postgresql.dbadmin.gdc.goog.create  
replications.postgresql.dbadmin.gdc.goog.delete  
replications.postgresql.dbadmin.gdc.goog.get  
replications.postgresql.dbadmin.gdc.goog.list  
replications.postgresql.dbadmin.gdc.goog.patch  
replications.postgresql.dbadmin.gdc.goog.update  
replications.postgresql.dbadmin.gdc.goog.watch  
restores.alloydbomni.dbadmin.gdc.goog.create  
restores.alloydbomni.dbadmin.gdc.goog.delete  
restores.alloydbomni.dbadmin.gdc.goog.get  
restores.alloydbomni.dbadmin.gdc.goog.list  
restores.alloydbomni.dbadmin.gdc.goog.watch  
restores.oracle.dbadmin.gdc.goog.create  
restores.oracle.dbadmin.gdc.goog.delete  
restores.oracle.dbadmin.gdc.goog.get  
restores.oracle.dbadmin.gdc.goog.list  
restores.oracle.dbadmin.gdc.goog.watch  
restores.postgresql.dbadmin.gdc.goog.create  
restores.postgresql.dbadmin.gdc.goog.delete  
restores.postgresql.dbadmin.gdc.goog.get  
restores.postgresql.dbadmin.gdc.goog.list  
restores.postgresql.dbadmin.gdc.goog.watch  
secrets.create  
secrets.delete  
secrets.get  
secrets.list  
secrets.update  
  
**Database Project Editor**  
(`project-db-editor`) Edits global project database resources. |  **Global** backupplans.alloydbomni.dbadmin.gdc.goog.get  
backupplans.alloydbomni.dbadmin.gdc.goog.list  
backupplans.alloydbomni.dbadmin.gdc.goog.watch  
backupplans.oracle.dbadmin.gdc.goog.get  
backupplans.oracle.dbadmin.gdc.goog.list  
backupplans.oracle.dbadmin.gdc.goog.watch  
backupplans.postgresql.dbadmin.gdc.goog.get  
backupplans.postgresql.dbadmin.gdc.goog.list  
backupplans.postgresql.dbadmin.gdc.goog.watch  
backups.alloydbomni.dbadmin.gdc.goog.get  
backups.alloydbomni.dbadmin.gdc.goog.list  
backups.alloydbomni.dbadmin.gdc.goog.watch  
backups.oracle.dbadmin.gdc.goog.get  
backups.oracle.dbadmin.gdc.goog.list  
backups.oracle.dbadmin.gdc.goog.watch  
backups.postgresql.dbadmin.gdc.goog.get  
backups.postgresql.dbadmin.gdc.goog.list  
backups.postgresql.dbadmin.gdc.goog.watch  
dbclusters.alloydbomni.dbadmin.gdc.goog.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.list  
dbclusters.alloydbomni.dbadmin.gdc.goog.patch  
dbclusters.alloydbomni.dbadmin.gdc.goog.update  
dbclusters.alloydbomni.dbadmin.gdc.goog.watch  
dbclusters.oracle.dbadmin.gdc.goog.get  
dbclusters.oracle.dbadmin.gdc.goog.list  
dbclusters.oracle.dbadmin.gdc.goog.patch  
dbclusters.oracle.dbadmin.gdc.goog.update  
dbclusters.oracle.dbadmin.gdc.goog.watch  
dbclusters.postgresql.dbadmin.gdc.goog.get  
dbclusters.postgresql.dbadmin.gdc.goog.list  
dbclusters.postgresql.dbadmin.gdc.goog.patch  
dbclusters.postgresql.dbadmin.gdc.goog.update  
dbclusters.postgresql.dbadmin.gdc.goog.watch  
exports.alloydbomni.dbadmin.gdc.goog.create  
exports.alloydbomni.dbadmin.gdc.goog.delete  
exports.alloydbomni.dbadmin.gdc.goog.get  
exports.alloydbomni.dbadmin.gdc.goog.list  
exports.alloydbomni.dbadmin.gdc.goog.watch  
exports.oracle.dbadmin.gdc.goog.create  
exports.oracle.dbadmin.gdc.goog.delete  
exports.oracle.dbadmin.gdc.goog.get  
exports.oracle.dbadmin.gdc.goog.list  
exports.oracle.dbadmin.gdc.goog.watch  
exports.postgresql.dbadmin.gdc.goog.create  
exports.postgresql.dbadmin.gdc.goog.delete  
exports.postgresql.dbadmin.gdc.goog.get  
exports.postgresql.dbadmin.gdc.goog.list  
exports.postgresql.dbadmin.gdc.goog.watch  
externalservers.alloydbomni.dbadmin.gdc.goog.create  
externalservers.alloydbomni.dbadmin.gdc.goog.delete  
externalservers.alloydbomni.dbadmin.gdc.goog.get  
externalservers.alloydbomni.dbadmin.gdc.goog.list  
externalservers.alloydbomni.dbadmin.gdc.goog.patch  
externalservers.alloydbomni.dbadmin.gdc.goog.update  
externalservers.alloydbomni.dbadmin.gdc.goog.watch  
externalservers.postgresql.dbadmin.gdc.goog.create  
externalservers.postgresql.dbadmin.gdc.goog.delete  
externalservers.postgresql.dbadmin.gdc.goog.get  
externalservers.postgresql.dbadmin.gdc.goog.list  
externalservers.postgresql.dbadmin.gdc.goog.patch  
externalservers.postgresql.dbadmin.gdc.goog.update  
externalservers.postgresql.dbadmin.gdc.goog.watch  
failovers.fleet.dbadmin.gdc.goog.create  
failovers.fleet.dbadmin.gdc.goog.delete  
failovers.fleet.dbadmin.gdc.goog.get  
failovers.fleet.dbadmin.gdc.goog.list  
failovers.fleet.dbadmin.gdc.goog.watch  
imports.alloydbomni.dbadmin.gdc.goog.create  
imports.alloydbomni.dbadmin.gdc.goog.delete  
imports.alloydbomni.dbadmin.gdc.goog.get  
imports.alloydbomni.dbadmin.gdc.goog.list  
imports.alloydbomni.dbadmin.gdc.goog.watch  
imports.oracle.dbadmin.gdc.goog.create  
imports.oracle.dbadmin.gdc.goog.delete  
imports.oracle.dbadmin.gdc.goog.get  
imports.oracle.dbadmin.gdc.goog.list  
imports.oracle.dbadmin.gdc.goog.watch  
imports.postgresql.dbadmin.gdc.goog.create  
imports.postgresql.dbadmin.gdc.goog.delete  
imports.postgresql.dbadmin.gdc.goog.get  
imports.postgresql.dbadmin.gdc.goog.list  
imports.postgresql.dbadmin.gdc.goog.watch  
migrations.alloydbomni.dbadmin.gdc.goog.get  
migrations.alloydbomni.dbadmin.gdc.goog.list  
migrations.alloydbomni.dbadmin.gdc.goog.patch  
migrations.alloydbomni.dbadmin.gdc.goog.update  
migrations.alloydbomni.dbadmin.gdc.goog.watch  
migrations.postgresql.dbadmin.gdc.goog.get  
migrations.postgresql.dbadmin.gdc.goog.list  
migrations.postgresql.dbadmin.gdc.goog.patch  
migrations.postgresql.dbadmin.gdc.goog.update  
migrations.postgresql.dbadmin.gdc.goog.watch  
replications.postgresql.dbadmin.gdc.goog.get  
replications.postgresql.dbadmin.gdc.goog.list  
replications.postgresql.dbadmin.gdc.goog.patch  
replications.postgresql.dbadmin.gdc.goog.update  
replications.postgresql.dbadmin.gdc.goog.watch  
restores.alloydbomni.dbadmin.gdc.goog.get  
restores.alloydbomni.dbadmin.gdc.goog.list  
restores.alloydbomni.dbadmin.gdc.goog.watch  
restores.oracle.dbadmin.gdc.goog.get  
restores.oracle.dbadmin.gdc.goog.list  
restores.oracle.dbadmin.gdc.goog.watch  
restores.postgresql.dbadmin.gdc.goog.get  
restores.postgresql.dbadmin.gdc.goog.list  
restores.postgresql.dbadmin.gdc.goog.watch  
secrets.create  
secrets.delete  
secrets.get  
secrets.list  
secrets.update  
  
**Zonal** backupplans.alloydbomni.dbadmin.gdc.goog.get  
backupplans.alloydbomni.dbadmin.gdc.goog.list  
backupplans.alloydbomni.dbadmin.gdc.goog.watch  
backupplans.oracle.dbadmin.gdc.goog.get  
backupplans.oracle.dbadmin.gdc.goog.list  
backupplans.oracle.dbadmin.gdc.goog.watch  
backupplans.postgresql.dbadmin.gdc.goog.get  
backupplans.postgresql.dbadmin.gdc.goog.list  
backupplans.postgresql.dbadmin.gdc.goog.watch  
backups.alloydbomni.dbadmin.gdc.goog.get  
backups.alloydbomni.dbadmin.gdc.goog.list  
backups.alloydbomni.dbadmin.gdc.goog.watch  
backups.oracle.dbadmin.gdc.goog.get  
backups.oracle.dbadmin.gdc.goog.list  
backups.oracle.dbadmin.gdc.goog.watch  
backups.postgresql.dbadmin.gdc.goog.get  
backups.postgresql.dbadmin.gdc.goog.list  
backups.postgresql.dbadmin.gdc.goog.watch  
dbclusters.alloydbomni.dbadmin.gdc.goog.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.list  
dbclusters.alloydbomni.dbadmin.gdc.goog.patch  
dbclusters.alloydbomni.dbadmin.gdc.goog.update  
dbclusters.alloydbomni.dbadmin.gdc.goog.watch  
dbclusters.oracle.dbadmin.gdc.goog.get  
dbclusters.oracle.dbadmin.gdc.goog.list  
dbclusters.oracle.dbadmin.gdc.goog.patch  
dbclusters.oracle.dbadmin.gdc.goog.update  
dbclusters.oracle.dbadmin.gdc.goog.watch  
dbclusters.postgresql.dbadmin.gdc.goog.get  
dbclusters.postgresql.dbadmin.gdc.goog.list  
dbclusters.postgresql.dbadmin.gdc.goog.patch  
dbclusters.postgresql.dbadmin.gdc.goog.update  
dbclusters.postgresql.dbadmin.gdc.goog.watch  
exports.alloydbomni.dbadmin.gdc.goog.create  
exports.alloydbomni.dbadmin.gdc.goog.delete  
exports.alloydbomni.dbadmin.gdc.goog.get  
exports.alloydbomni.dbadmin.gdc.goog.list  
exports.alloydbomni.dbadmin.gdc.goog.watch  
exports.oracle.dbadmin.gdc.goog.create  
exports.oracle.dbadmin.gdc.goog.delete  
exports.oracle.dbadmin.gdc.goog.get  
exports.oracle.dbadmin.gdc.goog.list  
exports.oracle.dbadmin.gdc.goog.watch  
exports.postgresql.dbadmin.gdc.goog.create  
exports.postgresql.dbadmin.gdc.goog.delete  
exports.postgresql.dbadmin.gdc.goog.get  
exports.postgresql.dbadmin.gdc.goog.list  
exports.postgresql.dbadmin.gdc.goog.watch  
externalservers.alloydbomni.dbadmin.gdc.goog.create  
externalservers.alloydbomni.dbadmin.gdc.goog.delete  
externalservers.alloydbomni.dbadmin.gdc.goog.get  
externalservers.alloydbomni.dbadmin.gdc.goog.list  
externalservers.alloydbomni.dbadmin.gdc.goog.patch  
externalservers.alloydbomni.dbadmin.gdc.goog.update  
externalservers.alloydbomni.dbadmin.gdc.goog.watch  
externalservers.postgresql.dbadmin.gdc.goog.create  
externalservers.postgresql.dbadmin.gdc.goog.delete  
externalservers.postgresql.dbadmin.gdc.goog.get  
externalservers.postgresql.dbadmin.gdc.goog.list  
externalservers.postgresql.dbadmin.gdc.goog.patch  
externalservers.postgresql.dbadmin.gdc.goog.update  
externalservers.postgresql.dbadmin.gdc.goog.watch  
failovers.fleet.dbadmin.gdc.goog.create  
failovers.fleet.dbadmin.gdc.goog.delete  
failovers.fleet.dbadmin.gdc.goog.get  
failovers.fleet.dbadmin.gdc.goog.list  
failovers.fleet.dbadmin.gdc.goog.watch  
imports.alloydbomni.dbadmin.gdc.goog.create  
imports.alloydbomni.dbadmin.gdc.goog.delete  
imports.alloydbomni.dbadmin.gdc.goog.get  
imports.alloydbomni.dbadmin.gdc.goog.list  
imports.alloydbomni.dbadmin.gdc.goog.watch  
imports.oracle.dbadmin.gdc.goog.create  
imports.oracle.dbadmin.gdc.goog.delete  
imports.oracle.dbadmin.gdc.goog.get  
imports.oracle.dbadmin.gdc.goog.list  
imports.oracle.dbadmin.gdc.goog.watch  
imports.postgresql.dbadmin.gdc.goog.create  
imports.postgresql.dbadmin.gdc.goog.delete  
imports.postgresql.dbadmin.gdc.goog.get  
imports.postgresql.dbadmin.gdc.goog.list  
imports.postgresql.dbadmin.gdc.goog.watch  
migrations.alloydbomni.dbadmin.gdc.goog.get  
migrations.alloydbomni.dbadmin.gdc.goog.list  
migrations.alloydbomni.dbadmin.gdc.goog.patch  
migrations.alloydbomni.dbadmin.gdc.goog.update  
migrations.alloydbomni.dbadmin.gdc.goog.watch  
migrations.postgresql.dbadmin.gdc.goog.get  
migrations.postgresql.dbadmin.gdc.goog.list  
migrations.postgresql.dbadmin.gdc.goog.patch  
migrations.postgresql.dbadmin.gdc.goog.update  
migrations.postgresql.dbadmin.gdc.goog.watch  
replications.postgresql.dbadmin.gdc.goog.get  
replications.postgresql.dbadmin.gdc.goog.list  
replications.postgresql.dbadmin.gdc.goog.patch  
replications.postgresql.dbadmin.gdc.goog.update  
replications.postgresql.dbadmin.gdc.goog.watch  
restores.alloydbomni.dbadmin.gdc.goog.get  
restores.alloydbomni.dbadmin.gdc.goog.list  
restores.alloydbomni.dbadmin.gdc.goog.watch  
restores.oracle.dbadmin.gdc.goog.get  
restores.oracle.dbadmin.gdc.goog.list  
restores.oracle.dbadmin.gdc.goog.watch  
restores.postgresql.dbadmin.gdc.goog.get  
restores.postgresql.dbadmin.gdc.goog.list  
restores.postgresql.dbadmin.gdc.goog.watch  
secrets.create  
secrets.delete  
secrets.get  
secrets.list  
secrets.update  
  
**Database Project Viewer**  
(`project-db-viewer`) Views global project database resources. |  **Global** backupplans.alloydbomni.dbadmin.gdc.goog.get  
backupplans.alloydbomni.dbadmin.gdc.goog.list  
backupplans.alloydbomni.dbadmin.gdc.goog.watch  
backupplans.oracle.dbadmin.gdc.goog.get  
backupplans.oracle.dbadmin.gdc.goog.list  
backupplans.oracle.dbadmin.gdc.goog.watch  
backupplans.postgresql.dbadmin.gdc.goog.get  
backupplans.postgresql.dbadmin.gdc.goog.list  
backupplans.postgresql.dbadmin.gdc.goog.watch  
backups.alloydbomni.dbadmin.gdc.goog.get  
backups.alloydbomni.dbadmin.gdc.goog.list  
backups.alloydbomni.dbadmin.gdc.goog.watch  
backups.oracle.dbadmin.gdc.goog.get  
backups.oracle.dbadmin.gdc.goog.list  
backups.oracle.dbadmin.gdc.goog.watch  
backups.postgresql.dbadmin.gdc.goog.get  
backups.postgresql.dbadmin.gdc.goog.list  
backups.postgresql.dbadmin.gdc.goog.watch  
configmaps.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.list  
dbclusters.alloydbomni.dbadmin.gdc.goog.watch  
dbclusters.oracle.dbadmin.gdc.goog.get  
dbclusters.oracle.dbadmin.gdc.goog.list  
dbclusters.oracle.dbadmin.gdc.goog.watch  
dbclusters.postgresql.dbadmin.gdc.goog.get  
dbclusters.postgresql.dbadmin.gdc.goog.list  
dbclusters.postgresql.dbadmin.gdc.goog.watch  
exports.alloydbomni.dbadmin.gdc.goog.get  
exports.alloydbomni.dbadmin.gdc.goog.list  
exports.alloydbomni.dbadmin.gdc.goog.watch  
exports.oracle.dbadmin.gdc.goog.get  
exports.oracle.dbadmin.gdc.goog.list  
exports.oracle.dbadmin.gdc.goog.watch  
exports.postgresql.dbadmin.gdc.goog.get  
exports.postgresql.dbadmin.gdc.goog.list  
exports.postgresql.dbadmin.gdc.goog.watch  
externalservers.alloydbomni.dbadmin.gdc.goog.get  
externalservers.alloydbomni.dbadmin.gdc.goog.list  
externalservers.alloydbomni.dbadmin.gdc.goog.watch  
externalservers.postgresql.dbadmin.gdc.goog.get  
externalservers.postgresql.dbadmin.gdc.goog.list  
externalservers.postgresql.dbadmin.gdc.goog.watch  
failovers.fleet.dbadmin.gdc.goog.get  
failovers.fleet.dbadmin.gdc.goog.list  
failovers.fleet.dbadmin.gdc.goog.watch  
imports.alloydbomni.dbadmin.gdc.goog.get  
imports.alloydbomni.dbadmin.gdc.goog.list  
imports.alloydbomni.dbadmin.gdc.goog.watch  
imports.oracle.dbadmin.gdc.goog.get  
imports.oracle.dbadmin.gdc.goog.list  
imports.oracle.dbadmin.gdc.goog.watch  
imports.postgresql.dbadmin.gdc.goog.get  
imports.postgresql.dbadmin.gdc.goog.list  
imports.postgresql.dbadmin.gdc.goog.watch  
migrations.alloydbomni.dbadmin.gdc.goog.get  
migrations.alloydbomni.dbadmin.gdc.goog.list  
migrations.alloydbomni.dbadmin.gdc.goog.watch  
migrations.postgresql.dbadmin.gdc.goog.get  
migrations.postgresql.dbadmin.gdc.goog.list  
migrations.postgresql.dbadmin.gdc.goog.watch  
replications.postgresql.dbadmin.gdc.goog.get  
replications.postgresql.dbadmin.gdc.goog.list  
replications.postgresql.dbadmin.gdc.goog.watch  
restores.alloydbomni.dbadmin.gdc.goog.get  
restores.alloydbomni.dbadmin.gdc.goog.list  
restores.alloydbomni.dbadmin.gdc.goog.watch  
restores.oracle.dbadmin.gdc.goog.get  
restores.oracle.dbadmin.gdc.goog.list  
restores.oracle.dbadmin.gdc.goog.watch  
restores.postgresql.dbadmin.gdc.goog.get  
restores.postgresql.dbadmin.gdc.goog.list  
restores.postgresql.dbadmin.gdc.goog.watch  
secrets.get  
secrets.list  
  
**Zonal** backupplans.alloydbomni.dbadmin.gdc.goog.get  
backupplans.alloydbomni.dbadmin.gdc.goog.list  
backupplans.alloydbomni.dbadmin.gdc.goog.watch  
backupplans.oracle.dbadmin.gdc.goog.get  
backupplans.oracle.dbadmin.gdc.goog.list  
backupplans.oracle.dbadmin.gdc.goog.watch  
backupplans.postgresql.dbadmin.gdc.goog.get  
backupplans.postgresql.dbadmin.gdc.goog.list  
backupplans.postgresql.dbadmin.gdc.goog.watch  
backups.alloydbomni.dbadmin.gdc.goog.get  
backups.alloydbomni.dbadmin.gdc.goog.list  
backups.alloydbomni.dbadmin.gdc.goog.watch  
backups.oracle.dbadmin.gdc.goog.get  
backups.oracle.dbadmin.gdc.goog.list  
backups.oracle.dbadmin.gdc.goog.watch  
backups.postgresql.dbadmin.gdc.goog.get  
backups.postgresql.dbadmin.gdc.goog.list  
backups.postgresql.dbadmin.gdc.goog.watch  
configmaps.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.get  
dbclusters.alloydbomni.dbadmin.gdc.goog.list  
dbclusters.alloydbomni.dbadmin.gdc.goog.watch  
dbclusters.oracle.dbadmin.gdc.goog.get  
dbclusters.oracle.dbadmin.gdc.goog.list  
dbclusters.oracle.dbadmin.gdc.goog.watch  
dbclusters.postgresql.dbadmin.gdc.goog.get  
dbclusters.postgresql.dbadmin.gdc.goog.list  
dbclusters.postgresql.dbadmin.gdc.goog.watch  
exports.alloydbomni.dbadmin.gdc.goog.get  
exports.alloydbomni.dbadmin.gdc.goog.list  
exports.alloydbomni.dbadmin.gdc.goog.watch  
exports.oracle.dbadmin.gdc.goog.get  
exports.oracle.dbadmin.gdc.goog.list  
exports.oracle.dbadmin.gdc.goog.watch  
exports.postgresql.dbadmin.gdc.goog.get  
exports.postgresql.dbadmin.gdc.goog.list  
exports.postgresql.dbadmin.gdc.goog.watch  
externalservers.alloydbomni.dbadmin.gdc.goog.get  
externalservers.alloydbomni.dbadmin.gdc.goog.list  
externalservers.alloydbomni.dbadmin.gdc.goog.watch  
externalservers.postgresql.dbadmin.gdc.goog.get  
externalservers.postgresql.dbadmin.gdc.goog.list  
externalservers.postgresql.dbadmin.gdc.goog.watch  
failovers.fleet.dbadmin.gdc.goog.get  
failovers.fleet.dbadmin.gdc.goog.list  
failovers.fleet.dbadmin.gdc.goog.watch  
imports.alloydbomni.dbadmin.gdc.goog.get  
imports.alloydbomni.dbadmin.gdc.goog.list  
imports.alloydbomni.dbadmin.gdc.goog.watch  
imports.oracle.dbadmin.gdc.goog.get  
imports.oracle.dbadmin.gdc.goog.list  
imports.oracle.dbadmin.gdc.goog.watch  
imports.postgresql.dbadmin.gdc.goog.get  
imports.postgresql.dbadmin.gdc.goog.list  
imports.postgresql.dbadmin.gdc.goog.watch  
migrations.alloydbomni.dbadmin.gdc.goog.get  
migrations.alloydbomni.dbadmin.gdc.goog.list  
migrations.alloydbomni.dbadmin.gdc.goog.watch  
migrations.postgresql.dbadmin.gdc.goog.get  
migrations.postgresql.dbadmin.gdc.goog.list  
migrations.postgresql.dbadmin.gdc.goog.watch  
replications.postgresql.dbadmin.gdc.goog.get  
replications.postgresql.dbadmin.gdc.goog.list  
replications.postgresql.dbadmin.gdc.goog.watch  
restores.alloydbomni.dbadmin.gdc.goog.get  
restores.alloydbomni.dbadmin.gdc.goog.list  
restores.alloydbomni.dbadmin.gdc.goog.watch  
restores.oracle.dbadmin.gdc.goog.get  
restores.oracle.dbadmin.gdc.goog.list  
restores.oracle.dbadmin.gdc.goog.watch  
restores.postgresql.dbadmin.gdc.goog.get  
restores.postgresql.dbadmin.gdc.goog.list  
restores.postgresql.dbadmin.gdc.goog.watch  
secrets.get  
secrets.list  
  
**External Load Balancer Viewer**  
(`external-load-balancer-viewer`) Views external load balancer resources within a project. |  **Global** backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.watch  
forwardingruleexternals.networking.global.gdc.goog.get  
forwardingruleexternals.networking.global.gdc.goog.list  
forwardingruleexternals.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.watch  
forwardingruleexternals.networking.gdc.goog.get  
forwardingruleexternals.networking.gdc.goog.list  
forwardingruleexternals.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.watch  
  
**File Share Project Admin**  
(`project-fileshare-admin`) Manage fileshares, exportgroupbindings, and export groups. |  **Zonal** exportgroupbindings.file.gdc.goog.create  
exportgroupbindings.file.gdc.goog.delete  
exportgroupbindings.file.gdc.goog.get  
exportgroupbindings.file.gdc.goog.list  
exportgroupbindings.file.gdc.goog.patch  
exportgroupbindings.file.gdc.goog.update  
exportgroupbindings.file.gdc.goog.watch  
exportgroups.file.gdc.goog.create  
exportgroups.file.gdc.goog.delete  
exportgroups.file.gdc.goog.get  
exportgroups.file.gdc.goog.list  
exportgroups.file.gdc.goog.patch  
exportgroups.file.gdc.goog.update  
exportgroups.file.gdc.goog.watch  
fileshares.file.gdc.goog.create  
fileshares.file.gdc.goog.delete  
fileshares.file.gdc.goog.get  
fileshares.file.gdc.goog.list  
fileshares.file.gdc.goog.patch  
fileshares.file.gdc.goog.update  
fileshares.file.gdc.goog.watch  
  
**File Share Project Viewer**  
(`project-fileshare-viewer`) View fileshares, exportgroupbindings, and export groups. |  **Zonal** exportgroupbindings.file.gdc.goog.get  
exportgroupbindings.file.gdc.goog.list  
exportgroupbindings.file.gdc.goog.watch  
exportgroups.file.gdc.goog.get  
exportgroups.file.gdc.goog.list  
exportgroups.file.gdc.goog.watch  
fileshares.file.gdc.goog.get  
fileshares.file.gdc.goog.list  
fileshares.file.gdc.goog.watch  
  
**Global External Load Balancer Admin**  
(`external-load-balancer-admin`) Creates and manages global external load balancer resources within a global project. |  **Global** backendservicepolicies.networking.global.gdc.goog.create  
backendservicepolicies.networking.global.gdc.goog.delete  
backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.patch  
backendservicepolicies.networking.global.gdc.goog.update  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.create  
backendservices.networking.global.gdc.goog.delete  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.patch  
backendservices.networking.global.gdc.goog.update  
backendservices.networking.global.gdc.goog.watch  
forwardingruleexternals.networking.global.gdc.goog.create  
forwardingruleexternals.networking.global.gdc.goog.delete  
forwardingruleexternals.networking.global.gdc.goog.get  
forwardingruleexternals.networking.global.gdc.goog.list  
forwardingruleexternals.networking.global.gdc.goog.patch  
forwardingruleexternals.networking.global.gdc.goog.update  
forwardingruleexternals.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.create  
healthchecks.networking.global.gdc.goog.delete  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.patch  
healthchecks.networking.global.gdc.goog.update  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.create  
backends.networking.gdc.goog.delete  
backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.patch  
backends.networking.gdc.goog.update  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.create  
backendservicepolicies.networking.gdc.goog.delete  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.patch  
backendservicepolicies.networking.gdc.goog.update  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.create  
backendservices.networking.gdc.goog.delete  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.patch  
backendservices.networking.gdc.goog.update  
backendservices.networking.gdc.goog.watch  
forwardingruleexternals.networking.gdc.goog.create  
forwardingruleexternals.networking.gdc.goog.delete  
forwardingruleexternals.networking.gdc.goog.get  
forwardingruleexternals.networking.gdc.goog.list  
forwardingruleexternals.networking.gdc.goog.patch  
forwardingruleexternals.networking.gdc.goog.update  
forwardingruleexternals.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.create  
healthchecks.networking.gdc.goog.delete  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.patch  
healthchecks.networking.gdc.goog.update  
healthchecks.networking.gdc.goog.watch  
  
**Global Internal Load Balancer Admin**  
(`internal-load-balancer-admin`) Creates and manages global internal load balancer resources within a global project. |  **Global** backendservicepolicies.networking.global.gdc.goog.create  
backendservicepolicies.networking.global.gdc.goog.delete  
backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.patch  
backendservicepolicies.networking.global.gdc.goog.update  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.create  
backendservices.networking.global.gdc.goog.delete  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.patch  
backendservices.networking.global.gdc.goog.update  
backendservices.networking.global.gdc.goog.watch  
forwardingruleinternals.networking.global.gdc.goog.create  
forwardingruleinternals.networking.global.gdc.goog.delete  
forwardingruleinternals.networking.global.gdc.goog.get  
forwardingruleinternals.networking.global.gdc.goog.list  
forwardingruleinternals.networking.global.gdc.goog.patch  
forwardingruleinternals.networking.global.gdc.goog.update  
forwardingruleinternals.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.create  
healthchecks.networking.global.gdc.goog.delete  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.patch  
healthchecks.networking.global.gdc.goog.update  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.create  
backends.networking.gdc.goog.delete  
backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.patch  
backends.networking.gdc.goog.update  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.create  
backendservicepolicies.networking.gdc.goog.delete  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.patch  
backendservicepolicies.networking.gdc.goog.update  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.create  
backendservices.networking.gdc.goog.delete  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.patch  
backendservices.networking.gdc.goog.update  
backendservices.networking.gdc.goog.watch  
forwardingruleinternals.networking.gdc.goog.create  
forwardingruleinternals.networking.gdc.goog.delete  
forwardingruleinternals.networking.gdc.goog.get  
forwardingruleinternals.networking.gdc.goog.list  
forwardingruleinternals.networking.gdc.goog.patch  
forwardingruleinternals.networking.gdc.goog.update  
forwardingruleinternals.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.create  
healthchecks.networking.gdc.goog.delete  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.patch  
healthchecks.networking.gdc.goog.update  
healthchecks.networking.gdc.goog.watch  
  
**Global Internal Load Balancer Viewer**  
(`internal-load-balancer-viewer`) Views global internal load balancer resources within a global project. |  **Global** backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.watch  
forwardingruleinternals.networking.global.gdc.goog.get  
forwardingruleinternals.networking.global.gdc.goog.list  
forwardingruleinternals.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.watch  
forwardingruleinternals.networking.gdc.goog.get  
forwardingruleinternals.networking.gdc.goog.list  
forwardingruleinternals.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.watch  
  
**Global Load Balancer Developer**  
(`load-balancer-developer`) Creates and manages global load balancer health checks and backend services within a global project. |  **Global** backendservicepolicies.networking.global.gdc.goog.create  
backendservicepolicies.networking.global.gdc.goog.delete  
backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.patch  
backendservicepolicies.networking.global.gdc.goog.update  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.create  
backendservices.networking.global.gdc.goog.delete  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.patch  
backendservices.networking.global.gdc.goog.update  
backendservices.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.create  
healthchecks.networking.global.gdc.goog.delete  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.patch  
healthchecks.networking.global.gdc.goog.update  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.create  
backends.networking.gdc.goog.delete  
backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.patch  
backends.networking.gdc.goog.update  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.create  
backendservicepolicies.networking.gdc.goog.delete  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.patch  
backendservicepolicies.networking.gdc.goog.update  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.create  
backendservices.networking.gdc.goog.delete  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.patch  
backendservices.networking.gdc.goog.update  
backendservices.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.create  
healthchecks.networking.gdc.goog.delete  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.patch  
healthchecks.networking.gdc.goog.update  
healthchecks.networking.gdc.goog.watch  
  
**Global MZAEADKey Deleter**  
(`global-mzaeadkey-deleter`) Deletes MZAEADKeys in their project. |  **Global** mzaeadkeys.kms.global.gdc.goog.delete  
mzaeadkeys.kms.global.gdc.goog.get  
mzaeadkeys.kms.global.gdc.goog.list  
mzaeadkeys.kms.global.gdc.goog.watch  
  
**Harbor Instance Admin**  
(`harbor-instance-admin`) Manages Harbor instances, projects, and backups. |  **Zonal** harborinstancebackupplans.artifactregistry.gdc.goog.create  
harborinstancebackupplans.artifactregistry.gdc.goog.delete  
harborinstancebackupplans.artifactregistry.gdc.goog.get  
harborinstancebackupplans.artifactregistry.gdc.goog.list  
harborinstancebackupplans.artifactregistry.gdc.goog.patch  
harborinstancebackupplans.artifactregistry.gdc.goog.update  
harborinstancebackupplans.artifactregistry.gdc.goog.watch  
harborinstancebackuprepositories.artifactregistry.gdc.goog.create  
harborinstancebackuprepositories.artifactregistry.gdc.goog.delete  
harborinstancebackuprepositories.artifactregistry.gdc.goog.get  
harborinstancebackuprepositories.artifactregistry.gdc.goog.list  
harborinstancebackuprepositories.artifactregistry.gdc.goog.patch  
harborinstancebackuprepositories.artifactregistry.gdc.goog.update  
harborinstancebackuprepositories.artifactregistry.gdc.goog.watch  
harborinstancebackups.artifactregistry.gdc.goog.create  
harborinstancebackups.artifactregistry.gdc.goog.delete  
harborinstancebackups.artifactregistry.gdc.goog.get  
harborinstancebackups.artifactregistry.gdc.goog.list  
harborinstancebackups.artifactregistry.gdc.goog.patch  
harborinstancebackups.artifactregistry.gdc.goog.update  
harborinstancebackups.artifactregistry.gdc.goog.watch  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.create  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.delete  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.get  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.list  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.patch  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.update  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.watch  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.create  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.delete  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.get  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.list  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.patch  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.update  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.watch  
harborinstanceprojects.artifactregistry.gdc.goog.create  
harborinstanceprojects.artifactregistry.gdc.goog.get  
harborinstanceprojects.artifactregistry.gdc.goog.patch  
harborinstanceprojects.artifactregistry.gdc.goog.update  
harborinstanceprojects.artifactregistry.gdc.goog.watch  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.create  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.delete  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.get  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.list  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.patch  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.update  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.watch  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.create  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.delete  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.get  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.list  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.patch  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.update  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.watch  
harborinstancerestores.artifactregistry.gdc.goog.create  
harborinstancerestores.artifactregistry.gdc.goog.delete  
harborinstancerestores.artifactregistry.gdc.goog.get  
harborinstancerestores.artifactregistry.gdc.goog.list  
harborinstancerestores.artifactregistry.gdc.goog.patch  
harborinstancerestores.artifactregistry.gdc.goog.update  
harborinstancerestores.artifactregistry.gdc.goog.watch  
harborinstances.artifactregistry.gdc.goog.create  
harborinstances.artifactregistry.gdc.goog.delete  
harborinstances.artifactregistry.gdc.goog.get  
harborinstances.artifactregistry.gdc.goog.list  
harborinstances.artifactregistry.gdc.goog.patch  
harborinstances.artifactregistry.gdc.goog.update  
harborinstances.artifactregistry.gdc.goog.watch  
  
**Harbor Instance Viewer**  
(`harbor-instance-viewer`) Views Harbor instances, projects, and backups. |  **Zonal** harborinstancebackupplans.artifactregistry.gdc.goog.get  
harborinstancebackupplans.artifactregistry.gdc.goog.list  
harborinstancebackupplans.artifactregistry.gdc.goog.watch  
harborinstancebackuprepositories.artifactregistry.gdc.goog.get  
harborinstancebackuprepositories.artifactregistry.gdc.goog.list  
harborinstancebackuprepositories.artifactregistry.gdc.goog.watch  
harborinstancebackups.artifactregistry.gdc.goog.get  
harborinstancebackups.artifactregistry.gdc.goog.list  
harborinstancebackups.artifactregistry.gdc.goog.watch  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.get  
harborinstancedatabasebackups.artifactregistry.private.gdc.goog.list  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.get  
harborinstancedatabaserestores.artifactregistry.private.gdc.goog.list  
harborinstanceprojects.artifactregistry.gdc.goog.get  
harborinstanceprojects.artifactregistry.gdc.goog.watch  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.get  
harborinstanceregistrybackups.artifactregistry.private.gdc.goog.list  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.get  
harborinstanceregistryrestores.artifactregistry.private.gdc.goog.list  
harborinstancerestores.artifactregistry.gdc.goog.get  
harborinstancerestores.artifactregistry.gdc.goog.list  
harborinstancerestores.artifactregistry.gdc.goog.watch  
harborinstances.artifactregistry.gdc.goog.get  
harborinstances.artifactregistry.gdc.goog.list  
harborinstances.artifactregistry.gdc.goog.watch  
  
**Harbor Project Creator**  
(`harbor-project-creator`) Creates and views Harbor instance projects. |  **Zonal** harborinstanceprojects.artifactregistry.gdc.goog.create  
harborinstanceprojects.artifactregistry.gdc.goog.get  
harborinstanceprojects.artifactregistry.gdc.goog.watch  
  
**IAM Project Admin**  
(`project-iam-admin`) Manages project permissions. |  **Global** customroles.iam.global.gdc.goog.create  
customroles.iam.global.gdc.goog.delete  
customroles.iam.global.gdc.goog.get  
customroles.iam.global.gdc.goog.list  
customroles.iam.global.gdc.goog.patch  
customroles.iam.global.gdc.goog.update  
customroles.iam.global.gdc.goog.watch  
iamrolebindings.iam.global.gdc.goog.create  
iamrolebindings.iam.global.gdc.goog.delete  
iamrolebindings.iam.global.gdc.goog.get  
iamrolebindings.iam.global.gdc.goog.list  
iamrolebindings.iam.global.gdc.goog.patch  
iamrolebindings.iam.global.gdc.goog.update  
iamrolebindings.iam.global.gdc.goog.watch  
iamroles.iam.global.gdc.goog.create  
iamroles.iam.global.gdc.goog.delete  
iamroles.iam.global.gdc.goog.get  
iamroles.iam.global.gdc.goog.list  
iamroles.iam.global.gdc.goog.patch  
iamroles.iam.global.gdc.goog.update  
iamroles.iam.global.gdc.goog.watch  
projectserviceaccounts.resourcemanager.global.gdc.goog.create  
projectserviceaccounts.resourcemanager.global.gdc.goog.delete  
projectserviceaccounts.resourcemanager.global.gdc.goog.get  
projectserviceaccounts.resourcemanager.global.gdc.goog.list  
projectserviceaccounts.resourcemanager.global.gdc.goog.patch  
projectserviceaccounts.resourcemanager.global.gdc.goog.update  
rolebindings.rbac.authorization.k8s.io.create  
rolebindings.rbac.authorization.k8s.io.delete  
rolebindings.rbac.authorization.k8s.io.get  
rolebindings.rbac.authorization.k8s.io.list  
rolebindings.rbac.authorization.k8s.io.patch  
rolebindings.rbac.authorization.k8s.io.update  
rolebindings.rbac.authorization.k8s.io.watch  
roles.rbac.authorization.k8s.io.create  
roles.rbac.authorization.k8s.io.delete  
roles.rbac.authorization.k8s.io.get  
roles.rbac.authorization.k8s.io.list  
roles.rbac.authorization.k8s.io.patch  
roles.rbac.authorization.k8s.io.update  
roles.rbac.authorization.k8s.io.watch  
  
**Zonal** *.visibility.resourcemanager.gdc.goog.get  
customroles.iam.gdc.goog.create  
customroles.iam.gdc.goog.delete  
customroles.iam.gdc.goog.get  
customroles.iam.gdc.goog.list  
customroles.iam.gdc.goog.patch  
customroles.iam.gdc.goog.update  
customroles.iam.gdc.goog.watch  
projectrolebindings.resourcemanager.gdc.goog.create  
projectrolebindings.resourcemanager.gdc.goog.delete  
projectrolebindings.resourcemanager.gdc.goog.get  
projectrolebindings.resourcemanager.gdc.goog.list  
projectrolebindings.resourcemanager.gdc.goog.patch  
projectrolebindings.resourcemanager.gdc.goog.update  
projectrolebindings.resourcemanager.gdc.goog.watch  
projectroles.resourcemanager.gdc.goog.create  
projectroles.resourcemanager.gdc.goog.delete  
projectroles.resourcemanager.gdc.goog.get  
projectroles.resourcemanager.gdc.goog.list  
projectroles.resourcemanager.gdc.goog.patch  
projectroles.resourcemanager.gdc.goog.update  
projectroles.resourcemanager.gdc.goog.watch  
projectserviceaccounts.resourcemanager.gdc.goog.create  
projectserviceaccounts.resourcemanager.gdc.goog.delete  
projectserviceaccounts.resourcemanager.gdc.goog.get  
projectserviceaccounts.resourcemanager.gdc.goog.list  
projectserviceaccounts.resourcemanager.gdc.goog.patch  
projectserviceaccounts.resourcemanager.gdc.goog.update  
projectserviceaccounts.resourcemanager.gdc.goog.watch  
rolebindings.rbac.authorization.k8s.io.create  
rolebindings.rbac.authorization.k8s.io.delete  
rolebindings.rbac.authorization.k8s.io.get  
rolebindings.rbac.authorization.k8s.io.list  
rolebindings.rbac.authorization.k8s.io.patch  
rolebindings.rbac.authorization.k8s.io.update  
rolebindings.rbac.authorization.k8s.io.watch  
roles.rbac.authorization.k8s.io.create  
roles.rbac.authorization.k8s.io.delete  
roles.rbac.authorization.k8s.io.get  
roles.rbac.authorization.k8s.io.list  
roles.rbac.authorization.k8s.io.patch  
roles.rbac.authorization.k8s.io.update  
roles.rbac.authorization.k8s.io.watch  
standardclusterrolebindings.iam.gdc.goog.create  
standardclusterrolebindings.iam.gdc.goog.delete  
standardclusterrolebindings.iam.gdc.goog.get  
standardclusterrolebindings.iam.gdc.goog.list  
standardclusterrolebindings.iam.gdc.goog.patch  
standardclusterrolebindings.iam.gdc.goog.update  
standardclusterrolebindings.iam.gdc.goog.watch  
standardclusterroles.iam.gdc.goog.create  
standardclusterroles.iam.gdc.goog.delete  
standardclusterroles.iam.gdc.goog.get  
standardclusterroles.iam.gdc.goog.list  
standardclusterroles.iam.gdc.goog.patch  
standardclusterroles.iam.gdc.goog.update  
standardclusterroles.iam.gdc.goog.watch  
  
**IAM Project Viewer**  
(`project-iam-viewer`) Views project permissions. |  **Global** customroles.iam.global.gdc.goog.get  
customroles.iam.global.gdc.goog.list  
customroles.iam.global.gdc.goog.watch  
iamrolebindings.iam.global.gdc.goog.get  
iamrolebindings.iam.global.gdc.goog.list  
iamrolebindings.iam.global.gdc.goog.watch  
iamroles.iam.global.gdc.goog.get  
iamroles.iam.global.gdc.goog.list  
iamroles.iam.global.gdc.goog.watch  
projectserviceaccounts.resourcemanager.global.gdc.goog.get  
projectserviceaccounts.resourcemanager.global.gdc.goog.list  
rolebindings.rbac.authorization.k8s.io.get  
rolebindings.rbac.authorization.k8s.io.list  
rolebindings.rbac.authorization.k8s.io.watch  
roles.rbac.authorization.k8s.io.get  
roles.rbac.authorization.k8s.io.list  
roles.rbac.authorization.k8s.io.watch  
  
**Zonal** *.visibility.resourcemanager.gdc.goog.get  
customroles.iam.gdc.goog.get  
customroles.iam.gdc.goog.list  
customroles.iam.gdc.goog.watch  
projectrolebindings.resourcemanager.gdc.goog.get  
projectrolebindings.resourcemanager.gdc.goog.list  
projectrolebindings.resourcemanager.gdc.goog.watch  
projectroles.resourcemanager.gdc.goog.get  
projectroles.resourcemanager.gdc.goog.list  
projectroles.resourcemanager.gdc.goog.watch  
projectserviceaccounts.resourcemanager.gdc.goog.get  
projectserviceaccounts.resourcemanager.gdc.goog.list  
projectserviceaccounts.resourcemanager.gdc.goog.watch  
rolebindings.rbac.authorization.k8s.io.get  
rolebindings.rbac.authorization.k8s.io.list  
rolebindings.rbac.authorization.k8s.io.watch  
roles.rbac.authorization.k8s.io.get  
roles.rbac.authorization.k8s.io.list  
roles.rbac.authorization.k8s.io.watch  
standardclusterrolebindings.iam.gdc.goog.get  
standardclusterrolebindings.iam.gdc.goog.list  
standardclusterrolebindings.iam.gdc.goog.watch  
standardclusterroles.iam.gdc.goog.get  
standardclusterroles.iam.gdc.goog.list  
standardclusterroles.iam.gdc.goog.watch  
  
**K8S Network Policy Admin**  
(`k8s-networkpolicy-admin`) Create and manage k8s Network Policies. |  **Kubernetes cluster** networkpolicies.networking.k8s.io.create  
networkpolicies.networking.k8s.io.delete  
networkpolicies.networking.k8s.io.get  
networkpolicies.networking.k8s.io.list  
networkpolicies.networking.k8s.io.patch  
networkpolicies.networking.k8s.io.update  
networkpolicies.networking.k8s.io.watch  
  
**K8S Network Policy Viewer**  
(`k8s-networkpolicy-viewer`) View k8s Network Policies. |  **Kubernetes cluster** networkpolicies.networking.k8s.io.get  
networkpolicies.networking.k8s.io.list  
networkpolicies.networking.k8s.io.watch  
  
**KMS Admin**  
(`kms-admin`) Manages KMS keys in their project and reads KeyImports and KeyExports. |  **Zonal** aeadkeys.kms.gdc.goog.create  
aeadkeys.kms.gdc.goog.decrypt  
aeadkeys.kms.gdc.goog.delete  
aeadkeys.kms.gdc.goog.encrypt  
aeadkeys.kms.gdc.goog.generatedatakey  
aeadkeys.kms.gdc.goog.get  
aeadkeys.kms.gdc.goog.list  
aeadkeys.kms.gdc.goog.patch  
aeadkeys.kms.gdc.goog.update  
aeadkeys.kms.gdc.goog.watch  
keyexports.kms.gdc.goog.get  
keyexports.kms.gdc.goog.list  
keyexports.kms.gdc.goog.watch  
keyimports.kms.gdc.goog.get  
keyimports.kms.gdc.goog.list  
keyimports.kms.gdc.goog.watch  
signingkeys.kms.gdc.goog.create  
signingkeys.kms.gdc.goog.delete  
signingkeys.kms.gdc.goog.get  
signingkeys.kms.gdc.goog.list  
signingkeys.kms.gdc.goog.patch  
signingkeys.kms.gdc.goog.sign  
signingkeys.kms.gdc.goog.update  
signingkeys.kms.gdc.goog.watch  
  
**KMS Creator**  
(`kms-creator`) Creates and reads KMS keys in their project. |  **Zonal** aeadkeys.kms.gdc.goog.create  
aeadkeys.kms.gdc.goog.get  
aeadkeys.kms.gdc.goog.list  
aeadkeys.kms.gdc.goog.watch  
signingkeys.kms.gdc.goog.create  
signingkeys.kms.gdc.goog.get  
signingkeys.kms.gdc.goog.list  
signingkeys.kms.gdc.goog.watch  
  
**KMS Developer**  
(`kms-developer`) Performs crypto operations using KMS keys in their project. |  **Zonal** aeadkeys.kms.gdc.goog.decrypt  
aeadkeys.kms.gdc.goog.encrypt  
aeadkeys.kms.gdc.goog.generatedatakey  
aeadkeys.kms.gdc.goog.get  
aeadkeys.kms.gdc.goog.list  
aeadkeys.kms.gdc.goog.watch  
signingkeys.kms.gdc.goog.get  
signingkeys.kms.gdc.goog.list  
signingkeys.kms.gdc.goog.sign  
signingkeys.kms.gdc.goog.watch  
  
**KMS Key Export Admin**  
(`kms-keyexport-admin`) Exports KMS keys in their project as wrapped keys from the KMS. |  **Zonal** keyexports.kms.gdc.goog.create  
keyexports.kms.gdc.goog.delete  
keyexports.kms.gdc.goog.get  
keyexports.kms.gdc.goog.list  
keyexports.kms.gdc.goog.patch  
keyexports.kms.gdc.goog.update  
keyexports.kms.gdc.goog.watch  
  
**KMS Key Import Admin**  
(`kms-keyimport-admin`) Imports KMS keys to the KMS as wrapped keys in their project. |  **Zonal** keyimports.kms.gdc.goog.create  
keyimports.kms.gdc.goog.delete  
keyimports.kms.gdc.goog.get  
keyimports.kms.gdc.goog.list  
keyimports.kms.gdc.goog.patch  
keyimports.kms.gdc.goog.update  
keyimports.kms.gdc.goog.watch  
  
**KMS Viewer**  
(`kms-viewer`) Reads KMS keys in their project. |  **Zonal** aeadkeys.kms.gdc.goog.get  
aeadkeys.kms.gdc.goog.list  
aeadkeys.kms.gdc.goog.watch  
keyexports.kms.gdc.goog.get  
keyexports.kms.gdc.goog.list  
keyexports.kms.gdc.goog.watch  
keyimports.kms.gdc.goog.get  
keyimports.kms.gdc.goog.list  
keyimports.kms.gdc.goog.watch  
signingkeys.kms.gdc.goog.get  
signingkeys.kms.gdc.goog.list  
signingkeys.kms.gdc.goog.watch  
  
**LibraryAgent User**  
(`libraryagent-user`) Allow Customers to use APIs of Libraryagent Demo service |  **Zonal** shelves.cloudresourcemanager.googleapis.com.list  
shelves.libraryagent.api.v1alpha1.get  
  
**Load Balancer Admin**  
(`load-balancer-admin`) Load Balancer Admin |  **Global** backendservicepolicies.networking.global.gdc.goog.create  
backendservicepolicies.networking.global.gdc.goog.delete  
backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.patch  
backendservicepolicies.networking.global.gdc.goog.update  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.create  
backendservices.networking.global.gdc.goog.delete  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.patch  
backendservices.networking.global.gdc.goog.update  
backendservices.networking.global.gdc.goog.watch  
forwardingruleexternals.networking.global.gdc.goog.create  
forwardingruleexternals.networking.global.gdc.goog.delete  
forwardingruleexternals.networking.global.gdc.goog.get  
forwardingruleexternals.networking.global.gdc.goog.list  
forwardingruleexternals.networking.global.gdc.goog.patch  
forwardingruleexternals.networking.global.gdc.goog.update  
forwardingruleexternals.networking.global.gdc.goog.watch  
forwardingruleinternals.networking.global.gdc.goog.create  
forwardingruleinternals.networking.global.gdc.goog.delete  
forwardingruleinternals.networking.global.gdc.goog.get  
forwardingruleinternals.networking.global.gdc.goog.list  
forwardingruleinternals.networking.global.gdc.goog.patch  
forwardingruleinternals.networking.global.gdc.goog.update  
forwardingruleinternals.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.create  
healthchecks.networking.global.gdc.goog.delete  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.patch  
healthchecks.networking.global.gdc.goog.update  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.create  
backends.networking.gdc.goog.delete  
backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.patch  
backends.networking.gdc.goog.update  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.create  
backendservicepolicies.networking.gdc.goog.delete  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.patch  
backendservicepolicies.networking.gdc.goog.update  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.create  
backendservices.networking.gdc.goog.delete  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.patch  
backendservices.networking.gdc.goog.update  
backendservices.networking.gdc.goog.watch  
forwardingruleexternals.networking.gdc.goog.create  
forwardingruleexternals.networking.gdc.goog.delete  
forwardingruleexternals.networking.gdc.goog.get  
forwardingruleexternals.networking.gdc.goog.list  
forwardingruleexternals.networking.gdc.goog.patch  
forwardingruleexternals.networking.gdc.goog.update  
forwardingruleexternals.networking.gdc.goog.watch  
forwardingruleinternals.networking.gdc.goog.create  
forwardingruleinternals.networking.gdc.goog.delete  
forwardingruleinternals.networking.gdc.goog.get  
forwardingruleinternals.networking.gdc.goog.list  
forwardingruleinternals.networking.gdc.goog.patch  
forwardingruleinternals.networking.gdc.goog.update  
forwardingruleinternals.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.create  
healthchecks.networking.gdc.goog.delete  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.patch  
healthchecks.networking.gdc.goog.update  
healthchecks.networking.gdc.goog.watch  
  
**Load Balancer Viewer**  
(`load-balancer-viewer`) Load Balancer Viewer. |  **Global** backendservicepolicies.networking.global.gdc.goog.get  
backendservicepolicies.networking.global.gdc.goog.list  
backendservicepolicies.networking.global.gdc.goog.watch  
backendservices.networking.global.gdc.goog.get  
backendservices.networking.global.gdc.goog.list  
backendservices.networking.global.gdc.goog.watch  
forwardingruleexternals.networking.global.gdc.goog.get  
forwardingruleexternals.networking.global.gdc.goog.list  
forwardingruleexternals.networking.global.gdc.goog.watch  
forwardingruleinternals.networking.global.gdc.goog.get  
forwardingruleinternals.networking.global.gdc.goog.list  
forwardingruleinternals.networking.global.gdc.goog.watch  
healthchecks.networking.global.gdc.goog.get  
healthchecks.networking.global.gdc.goog.list  
healthchecks.networking.global.gdc.goog.watch  
  
**Zonal** backends.networking.gdc.goog.get  
backends.networking.gdc.goog.list  
backends.networking.gdc.goog.watch  
backendservicepolicies.networking.gdc.goog.get  
backendservicepolicies.networking.gdc.goog.list  
backendservicepolicies.networking.gdc.goog.watch  
backendservices.networking.gdc.goog.get  
backendservices.networking.gdc.goog.list  
backendservices.networking.gdc.goog.watch  
forwardingruleexternals.networking.gdc.goog.get  
forwardingruleexternals.networking.gdc.goog.list  
forwardingruleexternals.networking.gdc.goog.watch  
forwardingruleinternals.networking.gdc.goog.get  
forwardingruleinternals.networking.gdc.goog.list  
forwardingruleinternals.networking.gdc.goog.watch  
healthchecks.networking.gdc.goog.get  
healthchecks.networking.gdc.goog.list  
healthchecks.networking.gdc.goog.watch  
  
**Log Querier**  
(`log-query-api-querier`) Access the Log Query API to query logs in AO project. |  **Zonal** labels.goog.gdc.logging.v1.get  
labels.goog.gdc.logging.v1.list  
labelvalues.goog.gdc.logging.v1.get  
labelvalues.goog.gdc.logging.v1.list  
listlabelsrequests.goog.gdc.logging.v1.get  
listlabelsrequests.goog.gdc.logging.v1.list  
listlabelsresponses.goog.gdc.logging.v1.get  
listlabelsresponses.goog.gdc.logging.v1.list  
listlabelvaluesrequests.goog.gdc.logging.v1.get  
listlabelvaluesrequests.goog.gdc.logging.v1.list  
listlabelvaluesresponses.goog.gdc.logging.v1.get  
listlabelvaluesresponses.goog.gdc.logging.v1.list  
listlogsfilters.goog.gdc.logging.v1.get  
listlogsfilters.goog.gdc.logging.v1.list  
listlogsrequests.goog.gdc.logging.v1.get  
listlogsrequests.goog.gdc.logging.v1.list  
listlogsresponses.goog.gdc.logging.v1.get  
listlogsresponses.goog.gdc.logging.v1.list  
logs.goog.gdc.logging.v1.get  
logs.goog.gdc.logging.v1.list  
  
**Logging Audit Logging Target Resource Debugger**  
(`auditloggingtarget-monitor`) Views and updates audit logging targets. |  **Zonal** auditloggingtargets.logging.private.gdc.goog.get  
auditloggingtargets.logging.private.gdc.goog.list  
auditloggingtargets.logging.private.gdc.goog.update  
dnsregistrations.network.private.gdc.goog.get  
dnsregistrations.network.private.gdc.goog.list  
  
**Logging Rule Creator**  
(`loggingrule-creator`) Creates and views logging rules. |  **Zonal** loggingrules.logging.gdc.goog.create  
loggingrules.logging.gdc.goog.get  
loggingrules.logging.gdc.goog.list  
loggingrules.logging.gdc.goog.watch  
  
**Logging Rule Editor**  
(`loggingrule-editor`) Edits logging rules. |  **Zonal** loggingrules.logging.gdc.goog.delete  
loggingrules.logging.gdc.goog.get  
loggingrules.logging.gdc.goog.list  
loggingrules.logging.gdc.goog.patch  
loggingrules.logging.gdc.goog.update  
loggingrules.logging.gdc.goog.watch  
  
**Logging Rule Viewer**  
(`loggingrule-viewer`) Views logging rules. |  **Zonal** loggingrules.logging.gdc.goog.get  
loggingrules.logging.gdc.goog.list  
loggingrules.logging.gdc.goog.watch  
  
**Logging Target Creator**  
(`loggingtarget-creator`) Creates and views logging targets. |  **Zonal** loggingtargets.logging.gdc.goog.create  
loggingtargets.logging.gdc.goog.get  
loggingtargets.logging.gdc.goog.list  
loggingtargets.logging.gdc.goog.watch  
  
**Logging Target Editor**  
(`loggingtarget-editor`) Edits logging targets. |  **Zonal** loggingtargets.logging.gdc.goog.delete  
loggingtargets.logging.gdc.goog.get  
loggingtargets.logging.gdc.goog.list  
loggingtargets.logging.gdc.goog.patch  
loggingtargets.logging.gdc.goog.update  
loggingtargets.logging.gdc.goog.watch  
  
**Logging Target Viewer**  
(`loggingtarget-viewer`) Views logging targets. |  **Zonal** loggingtargets.logging.gdc.goog.get  
loggingtargets.logging.gdc.goog.list  
loggingtargets.logging.gdc.goog.watch  
  
**Maintenance Policy Binding Project Editor**  
(`project-mpb-editor`) Manages MaintenancePolicyBinding resources in the project. |  **Zonal** maintenancepolicybindings.maintenance.goog.create  
maintenancepolicybindings.maintenance.goog.delete  
maintenancepolicybindings.maintenance.goog.get  
maintenancepolicybindings.maintenance.goog.list  
maintenancepolicybindings.maintenance.goog.patch  
maintenancepolicybindings.maintenance.goog.update  
maintenancepolicybindings.maintenance.goog.watch  
  
**Maintenance Policy Binding Project Viewer**  
(`project-mpb-viewer`) Reads MaintenancePolicyBinding resources in the project. |  **Zonal** maintenancepolicybindings.maintenance.goog.get  
maintenancepolicybindings.maintenance.goog.list  
maintenancepolicybindings.maintenance.goog.watch  
  
**Maintenance Policy Project Admin**  
(`project-mp-admin`) Manages Maintenance Policy and Maintenance Policy Binding resources in the project. |  **Zonal** maintenancepolicies.maintenance.goog.create  
maintenancepolicies.maintenance.goog.delete  
maintenancepolicies.maintenance.goog.get  
maintenancepolicies.maintenance.goog.list  
maintenancepolicies.maintenance.goog.patch  
maintenancepolicies.maintenance.goog.update  
maintenancepolicies.maintenance.goog.watch  
maintenancepolicybindings.maintenance.goog.create  
maintenancepolicybindings.maintenance.goog.delete  
maintenancepolicybindings.maintenance.goog.get  
maintenancepolicybindings.maintenance.goog.list  
maintenancepolicybindings.maintenance.goog.patch  
maintenancepolicybindings.maintenance.goog.update  
maintenancepolicybindings.maintenance.goog.watch  
  
**Maintenance Policy Project Editor**  
(`project-mp-editor`) Manages MaintenancePolicy resources in the project. |  **Zonal** maintenancepolicies.maintenance.goog.create  
maintenancepolicies.maintenance.goog.delete  
maintenancepolicies.maintenance.goog.get  
maintenancepolicies.maintenance.goog.list  
maintenancepolicies.maintenance.goog.patch  
maintenancepolicies.maintenance.goog.update  
maintenancepolicies.maintenance.goog.watch  
  
**Maintenance Policy Project Viewer**  
(`project-mp-viewer`) Reads MaintenancePolicy and Maintenance Policy Binding resources in the project. |  **Zonal** maintenancepolicies.maintenance.goog.get  
maintenancepolicies.maintenance.goog.list  
maintenancepolicies.maintenance.goog.watch  
  
**Managed DNS Project Admin**  
(`managed-dns-project-admin`) Manages all aspects of Managed DNS zones and resource record sets within a project in the Global API. |  **Global** manageddnszones.networking.global.gdc.goog.create  
manageddnszones.networking.global.gdc.goog.delete  
manageddnszones.networking.global.gdc.goog.get  
manageddnszones.networking.global.gdc.goog.list  
manageddnszones.networking.global.gdc.goog.patch  
manageddnszones.networking.global.gdc.goog.update  
manageddnszones.networking.global.gdc.goog.watch  
resourcerecordsets.networking.global.gdc.goog.create  
resourcerecordsets.networking.global.gdc.goog.delete  
resourcerecordsets.networking.global.gdc.goog.get  
resourcerecordsets.networking.global.gdc.goog.list  
resourcerecordsets.networking.global.gdc.goog.patch  
resourcerecordsets.networking.global.gdc.goog.update  
resourcerecordsets.networking.global.gdc.goog.watch  
  
**Managed DNS Project Viewer**  
(`managed-dns-project-viewer`) Views Managed DNS zones and resource record sets within a project in the Global API. |  **Global** manageddnszones.networking.global.gdc.goog.get  
manageddnszones.networking.global.gdc.goog.list  
resourcerecordsets.networking.global.gdc.goog.get  
resourcerecordsets.networking.global.gdc.goog.list  
  
**Marketplace Catalog Editor**  
(`marketplace-catalog-editor`) Views, lists, creates, updates and deletes service catalogs. |  **Global** servicecatalogs.marketplace.global.gdc.goog.create  
servicecatalogs.marketplace.global.gdc.goog.delete  
servicecatalogs.marketplace.global.gdc.goog.get  
servicecatalogs.marketplace.global.gdc.goog.list  
servicecatalogs.marketplace.global.gdc.goog.patch  
servicecatalogs.marketplace.global.gdc.goog.update  
servicecatalogs.marketplace.global.gdc.goog.watch  
  
**Marketplace Catalog Viewer**  
(`marketplace-catalog-viewer`) Views service catalogs. |  **Global** projects.resourcemanager.global.gdc.goog.get  
projects.resourcemanager.global.gdc.goog.list  
projects.resourcemanager.global.gdc.goog.watch  
servicecatalogbindings.marketplace.global.gdc.goog.get  
servicecatalogbindings.marketplace.global.gdc.goog.list  
servicecatalogbindings.marketplace.global.gdc.goog.watch  
  
**Marketplace Editor**  
(`marketplace-editor`) Creates, updates and deletes service instances. |  **Zonal** serviceinstances.marketplace.gdc.goog.create  
serviceinstances.marketplace.gdc.goog.delete  
serviceinstances.marketplace.gdc.goog.get  
serviceinstances.marketplace.gdc.goog.list  
serviceinstances.marketplace.gdc.goog.patch  
serviceinstances.marketplace.gdc.goog.update  
serviceinstances.marketplace.gdc.goog.watch  
  
**Marketplace Service Consumer**  
(`marketplace-service-consumer`) Creates, updates and deletes service instances. |  **Zonal** serviceinstances.marketplace.gdc.goog.create  
serviceinstances.marketplace.gdc.goog.delete  
serviceinstances.marketplace.gdc.goog.get  
serviceinstances.marketplace.gdc.goog.list  
serviceinstances.marketplace.gdc.goog.patch  
serviceinstances.marketplace.gdc.goog.update  
serviceinstances.marketplace.gdc.goog.watch  
  
**Marketplace Service Editor**  
(`marketplace-service-editor`) Views, lists, creates, updates and deletes service versions and service descriptions. |  **Global** servicedescriptions.marketplace.global.gdc.goog.create  
servicedescriptions.marketplace.global.gdc.goog.delete  
servicedescriptions.marketplace.global.gdc.goog.get  
servicedescriptions.marketplace.global.gdc.goog.list  
servicedescriptions.marketplace.global.gdc.goog.patch  
servicedescriptions.marketplace.global.gdc.goog.update  
servicedescriptions.marketplace.global.gdc.goog.watch  
serviceversions.marketplace.global.gdc.goog.create  
serviceversions.marketplace.global.gdc.goog.delete  
serviceversions.marketplace.global.gdc.goog.get  
serviceversions.marketplace.global.gdc.goog.list  
serviceversions.marketplace.global.gdc.goog.patch  
serviceversions.marketplace.global.gdc.goog.update  
serviceversions.marketplace.global.gdc.goog.watch  
  
**Zonal** servicedescriptions.marketplace.gdc.goog.create  
servicedescriptions.marketplace.gdc.goog.delete  
servicedescriptions.marketplace.gdc.goog.get  
servicedescriptions.marketplace.gdc.goog.list  
servicedescriptions.marketplace.gdc.goog.patch  
servicedescriptions.marketplace.gdc.goog.update  
servicedescriptions.marketplace.gdc.goog.watch  
serviceversions.marketplace.gdc.goog.create  
serviceversions.marketplace.gdc.goog.delete  
serviceversions.marketplace.gdc.goog.get  
serviceversions.marketplace.gdc.goog.list  
serviceversions.marketplace.gdc.goog.patch  
serviceversions.marketplace.gdc.goog.update  
serviceversions.marketplace.gdc.goog.watch  
  
**Marketplace Service Viewer**  
(`marketplace-service-viewer`) Views and lists service versions, service descriptions and service catalogs. |  **Global** servicecatalogs.marketplace.global.gdc.goog.get  
servicecatalogs.marketplace.global.gdc.goog.list  
servicecatalogs.marketplace.global.gdc.goog.watch  
servicedescriptions.marketplace.global.gdc.goog.get  
servicedescriptions.marketplace.global.gdc.goog.list  
servicedescriptions.marketplace.global.gdc.goog.watch  
serviceversions.marketplace.global.gdc.goog.get  
serviceversions.marketplace.global.gdc.goog.list  
serviceversions.marketplace.global.gdc.goog.watch  
  
**Zonal** catalogbundles.marketplaceview.gdc.goog.get  
catalogbundles.marketplaceview.gdc.goog.list  
catalogbundles.marketplaceview.gdc.goog.watch  
servicedescriptions.marketplace.gdc.goog.get  
servicedescriptions.marketplace.gdc.goog.list  
servicedescriptions.marketplace.gdc.goog.watch  
serviceinstances.marketplace.gdc.goog.get  
serviceinstances.marketplace.gdc.goog.list  
serviceinstances.marketplace.gdc.goog.watch  
serviceversions.marketplace.gdc.goog.get  
serviceversions.marketplace.gdc.goog.list  
serviceversions.marketplace.gdc.goog.watch  
  
**Monitoring Project Alertmanager Editor**  
(`project-cortex-alertmanager-editor`) Edits project Cortex Alertmanager and rules. |  **Zonal** ${.ProjectNamespace}-cortex-system/cortex-alertmanager.istio.resourcemanager.gdc.goog.DELETE  
${.ProjectNamespace}-cortex-system/cortex-alertmanager.istio.resourcemanager.gdc.goog.GET  
${.ProjectNamespace}-cortex-system/cortex-alertmanager.istio.resourcemanager.gdc.goog.POST  
loggingrules.logging.gdc.goog.create  
loggingrules.logging.gdc.goog.delete  
loggingrules.logging.gdc.goog.get  
loggingrules.logging.gdc.goog.list  
loggingrules.logging.gdc.goog.patch  
loggingrules.logging.gdc.goog.update  
loggingrules.monitoring.gdc.goog.create  
loggingrules.monitoring.gdc.goog.delete  
loggingrules.monitoring.gdc.goog.get  
loggingrules.monitoring.gdc.goog.list  
loggingrules.monitoring.gdc.goog.patch  
loggingrules.monitoring.gdc.goog.update  
monitoringrules.monitoring.gdc.goog.create  
monitoringrules.monitoring.gdc.goog.delete  
monitoringrules.monitoring.gdc.goog.get  
monitoringrules.monitoring.gdc.goog.list  
monitoringrules.monitoring.gdc.goog.patch  
monitoringrules.monitoring.gdc.goog.update  
  
**Monitoring Project Alertmanager Viewer**  
(`project-cortex-alertmanager-viewer`) Views project Cortex Alertmanager. |  **Zonal** ${.ProjectNamespace}-cortex-system/cortex-alertmanager.istio.resourcemanager.gdc.goog.GET  
${.ProjectNamespace}-cortex-system/cortex-alertmanager.istio.resourcemanager.gdc.goog.POST  
loggingrules.logging.gdc.goog.get  
loggingrules.logging.gdc.goog.list  
loggingrules.monitoring.gdc.goog.get  
loggingrules.monitoring.gdc.goog.list  
monitoringrules.monitoring.gdc.goog.get  
monitoringrules.monitoring.gdc.goog.list  
  
**Monitoring Project Prometheus Viewer**  
(`project-cortex-prometheus-viewer`) Manages project Cortex Prometheus and Metrics. |  **Zonal** ${.ProjectNamespace}-cortex-system/cortex-metrics.istio.resourcemanager.gdc.goog.GET  
${.ProjectNamespace}-cortex-system/cortex-metrics.istio.resourcemanager.gdc.goog.POST  
${.ProjectNamespace}-cortex-system/cortex-prometheus.istio.resourcemanager.gdc.goog.GET  
${.ProjectNamespace}-cortex-system/cortex-prometheus.istio.resourcemanager.gdc.goog.POST  
  
**MonitoringRule Editor**  
(`monitoringrule-editor`) Manages monitoring rules. |  **Zonal** monitoringrules.monitoring.gdc.goog.delete  
monitoringrules.monitoring.gdc.goog.get  
monitoringrules.monitoring.gdc.goog.list  
monitoringrules.monitoring.gdc.goog.patch  
monitoringrules.monitoring.gdc.goog.update  
monitoringrules.monitoring.gdc.goog.watch  
  
**MonitoringRule Viewer**  
(`monitoringrule-viewer`) Views monitoring rules. |  **Zonal** monitoringrules.monitoring.gdc.goog.get  
monitoringrules.monitoring.gdc.goog.list  
monitoringrules.monitoring.gdc.goog.watch  
  
**MonitoringTarget Editor**  
(`monitoringtarget-editor`) Edits monitoring targets. |  **Zonal** monitoringtargets.monitoring.gdc.goog.delete  
monitoringtargets.monitoring.gdc.goog.get  
monitoringtargets.monitoring.gdc.goog.list  
monitoringtargets.monitoring.gdc.goog.patch  
monitoringtargets.monitoring.gdc.goog.update  
monitoringtargets.monitoring.gdc.goog.watch  
  
**MonitoringTarget Viewer**  
(`monitoringtarget-viewer`) Views monitoring targets. |  **Zonal** monitoringtargets.monitoring.gdc.goog.get  
monitoringtargets.monitoring.gdc.goog.list  
monitoringtargets.monitoring.gdc.goog.watch  
  
**NAT Viewer**  
(`nat-viewer`) Read deployments in user clusters. |  **Kubernetes cluster** deployments.apps.get  
deployments.apps.list  
  
**Namespace Admin**  
(`namespace-admin`) Manages all project resources. |  **Kubernetes cluster** *.*.create  
*.*.delete  
*.*.get  
*.*.list  
*.*.patch  
*.*.update  
*.*.watch  
  
**Namespace Viewer**  
(`namespace-viewer`) Views all project resources. |  **Kubernetes cluster** *.*.get  
*.*.list  
*.*.watch  
  
**ObservabilityPipeline Editor**  
(`observabilitypipeline-editor`) Edits observability pipelines. |  **Zonal** observabilitypipelines.observability.gdc.goog.delete  
observabilitypipelines.observability.gdc.goog.get  
observabilitypipelines.observability.gdc.goog.list  
observabilitypipelines.observability.gdc.goog.patch  
observabilitypipelines.observability.gdc.goog.update  
observabilitypipelines.observability.gdc.goog.watch  
  
**ObservabilityPipeline Viewer**  
(`observabilitypipeline-viewer`) Views observability pipelines. |  **Zonal** observabilitypipelines.observability.gdc.goog.get  
observabilitypipelines.observability.gdc.goog.list  
observabilitypipelines.observability.gdc.goog.watch  
  
**Project Grafana Viewer**  
(`project-grafana-viewer`) Views project Grafana instance. |  **Zonal** ${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.DELETE  
${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.GET  
${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.HEAD  
${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.OPTIONS  
${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.PATCH  
${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.POST  
${.ProjectNamespace}-grafana-system/grafana.istio.resourcemanager.gdc.goog.PUT  
  
**Project Network Policy Admin**  
(`project-networkpolicy-admin`) Create and manage Project Network Policies. |  **Global** projectnetworkpolicies.networking.global.gdc.goog.create  
projectnetworkpolicies.networking.global.gdc.goog.delete  
projectnetworkpolicies.networking.global.gdc.goog.get  
projectnetworkpolicies.networking.global.gdc.goog.list  
projectnetworkpolicies.networking.global.gdc.goog.patch  
projectnetworkpolicies.networking.global.gdc.goog.update  
projectnetworkpolicies.networking.global.gdc.goog.watch  
projectnetworkpolicyreplicas.networking.global.gdc.goog.create  
projectnetworkpolicyreplicas.networking.global.gdc.goog.delete  
projectnetworkpolicyreplicas.networking.global.gdc.goog.get  
projectnetworkpolicyreplicas.networking.global.gdc.goog.list  
projectnetworkpolicyreplicas.networking.global.gdc.goog.patch  
projectnetworkpolicyreplicas.networking.global.gdc.goog.update  
projectnetworkpolicyreplicas.networking.global.gdc.goog.watch  
  
**Zonal** projectnetworkpolicies.networking.gdc.goog.create  
projectnetworkpolicies.networking.gdc.goog.delete  
projectnetworkpolicies.networking.gdc.goog.get  
projectnetworkpolicies.networking.gdc.goog.list  
projectnetworkpolicies.networking.gdc.goog.patch  
projectnetworkpolicies.networking.gdc.goog.update  
projectnetworkpolicies.networking.gdc.goog.watch  
  
**Project Network Policy Viewer**  
(`project-networkpolicy-viewer`) View Project Network Policies. |  **Global** projectnetworkpolicies.networking.global.gdc.goog.get  
projectnetworkpolicies.networking.global.gdc.goog.list  
projectnetworkpolicies.networking.global.gdc.goog.watch  
projectnetworkpolicyreplicas.networking.global.gdc.goog.get  
projectnetworkpolicyreplicas.networking.global.gdc.goog.list  
projectnetworkpolicyreplicas.networking.global.gdc.goog.watch  
  
**Zonal** projectnetworkpolicies.networking.gdc.goog.get  
projectnetworkpolicies.networking.gdc.goog.list  
projectnetworkpolicies.networking.gdc.goog.watch  
  
**Project Quota Administrator**  
(`project-quota-admin`) Manages Global Project Level Quota Resources for an Organization. |  **Global** quotavalues.quotamanagement.global.gdc.goog.create  
quotavalues.quotamanagement.global.gdc.goog.delete  
quotavalues.quotamanagement.global.gdc.goog.get  
quotavalues.quotamanagement.global.gdc.goog.list  
quotavalues.quotamanagement.global.gdc.goog.patch  
quotavalues.quotamanagement.global.gdc.goog.update  
quotavalues.quotamanagement.global.gdc.goog.watch  
  
**Project Quota Viewer**  
(`project-quota-viewer`) Views Global Project Level Quota Resources for an Organization. |  **Global** quotavalues.quotamanagement.global.gdc.goog.get  
quotavalues.quotamanagement.global.gdc.goog.list  
quotavalues.quotamanagement.global.gdc.goog.watch  
  
**Project Viewer**  
(`project-viewer`) Views project resources and permissions. |  **Zonal** *.visibility.resourcemanager.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.list  
clusterinfos.resourcemanager.private.gdc.goog.watch  
customresourcedefinitions.apiextensions.k8s.io.get  
customresourcedefinitions.apiextensions.k8s.io.list  
customresourcedefinitions.apiextensions.k8s.io.watch  
projectrolebindings.resourcemanager.gdc.goog.get  
projectrolebindings.resourcemanager.gdc.goog.list  
projectrolebindings.resourcemanager.gdc.goog.watch  
projectroles.resourcemanager.gdc.goog.get  
projectroles.resourcemanager.gdc.goog.list  
projectroles.resourcemanager.gdc.goog.watch  
rolebindings.rbac.authorization.k8s.io.get  
rolebindings.rbac.authorization.k8s.io.list  
rolebindings.rbac.authorization.k8s.io.watch  
roles.rbac.authorization.k8s.io.get  
roles.rbac.authorization.k8s.io.list  
roles.rbac.authorization.k8s.io.watch  
  
**SIEM Export Org Creator**  
(`siemexport-org-creator`) Creates and views SIEM export resources. |  **Zonal** secrets.create  
secrets.get  
secrets.list  
secrets.watch  
siemorgforwarders.logging.gdc.goog.create  
siemorgforwarders.logging.gdc.goog.get  
siemorgforwarders.logging.gdc.goog.list  
siemorgforwarders.logging.gdc.goog.watch  
  
**SIEM Export Org Editor**  
(`siemexport-org-editor`) Manages SIEM export resources. |  **Zonal** secrets.delete  
secrets.get  
secrets.list  
secrets.patch  
secrets.update  
secrets.watch  
siemorgforwarders.logging.gdc.goog.delete  
siemorgforwarders.logging.gdc.goog.get  
siemorgforwarders.logging.gdc.goog.list  
siemorgforwarders.logging.gdc.goog.patch  
siemorgforwarders.logging.gdc.goog.update  
siemorgforwarders.logging.gdc.goog.watch  
  
**SIEM Export Org Viewer**  
(`siemexport-org-viewer`) Views SIEM export resources. |  **Zonal** secrets.get  
secrets.list  
secrets.watch  
siemorgforwarders.logging.gdc.goog.get  
siemorgforwarders.logging.gdc.goog.list  
siemorgforwarders.logging.gdc.goog.watch  
  
**Secret Admin**  
(`secret-admin`) Manages Kubernetes secrets in project namespaces. |  **Global** secrets.create  
secrets.delete  
secrets.get  
secrets.list  
secrets.patch  
secrets.update  
  
**Zonal** secrets.create  
secrets.delete  
secrets.get  
secrets.list  
secrets.patch  
secrets.update  
secrets.watch  
  
**Secret Viewer**  
(`secret-viewer`) Views Kubernetes secrets in project namespaces. |  **Global** secrets.get  
secrets.list  
secrets.watch  
  
**Zonal** secrets.get  
secrets.list  
secrets.watch  
  
**Standard Cluster Admin**  
(`standard-cluster-admin`) Manages the creation and update for Standard Clusters |  **Zonal** *.visibility.resourcemanager.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.list  
clusterinfos.resourcemanager.private.gdc.goog.watch  
clusters.cluster.gdc.goog.create  
clusters.cluster.gdc.goog.delete  
clusters.cluster.gdc.goog.get  
clusters.cluster.gdc.goog.list  
clusters.cluster.gdc.goog.patch  
clusters.cluster.gdc.goog.update  
clusters.cluster.gdc.goog.watch  
projectbindings.resourcemanager.gdc.goog.create  
projectbindings.resourcemanager.gdc.goog.delete  
projectbindings.resourcemanager.gdc.goog.get  
projectbindings.resourcemanager.gdc.goog.list  
projectbindings.resourcemanager.gdc.goog.watch  
projects.resourcemanager.gdc.goog.get  
projects.resourcemanager.gdc.goog.list  
projects.resourcemanager.gdc.goog.watch  
userclusterupgraderequests.cluster.gdc.goog.create  
userclusterupgraderequests.cluster.gdc.goog.delete  
userclusterupgraderequests.cluster.gdc.goog.get  
userclusterupgraderequests.cluster.gdc.goog.list  
userclusterupgraderequests.cluster.gdc.goog.patch  
userclusterupgraderequests.cluster.gdc.goog.update  
userclusterupgraderequests.cluster.gdc.goog.watch  
userclusterupgrades.upgrade.private.gdc.goog.create  
userclusterupgrades.upgrade.private.gdc.goog.delete  
userclusterupgrades.upgrade.private.gdc.goog.get  
userclusterupgrades.upgrade.private.gdc.goog.list  
userclusterupgrades.upgrade.private.gdc.goog.patch  
userclusterupgrades.upgrade.private.gdc.goog.update  
userclusterupgrades.upgrade.private.gdc.goog.watch  
  
**Standard Cluster Viewer**  
(`standard-cluster-viewer`) Views the creation and update for Standard Clusters |  **Zonal** *.visibility.resourcemanager.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.list  
clusterinfos.resourcemanager.private.gdc.goog.watch  
clusters.cluster.gdc.goog.get  
clusters.cluster.gdc.goog.list  
clusters.cluster.gdc.goog.watch  
projectbindings.resourcemanager.gdc.goog.get  
projectbindings.resourcemanager.gdc.goog.list  
projectbindings.resourcemanager.gdc.goog.watch  
projects.resourcemanager.gdc.goog.get  
projects.resourcemanager.gdc.goog.list  
projects.resourcemanager.gdc.goog.watch  
userclusterupgraderequests.cluster.gdc.goog.get  
userclusterupgraderequests.cluster.gdc.goog.list  
userclusterupgraderequests.cluster.gdc.goog.watch  
userclusterupgrades.upgrade.private.gdc.goog.get  
userclusterupgrades.upgrade.private.gdc.goog.list  
userclusterupgrades.upgrade.private.gdc.goog.watch  
  
**Subnet Project Admin**  
(`subnet-project-admin`) Creates and manages subnets in the project. |  **Global** subnets.ipam.global.gdc.goog.create  
subnets.ipam.global.gdc.goog.delete  
subnets.ipam.global.gdc.goog.get  
subnets.ipam.global.gdc.goog.list  
subnets.ipam.global.gdc.goog.patch  
subnets.ipam.global.gdc.goog.update  
subnets.ipam.global.gdc.goog.watch  
  
**Zonal** subnets.ipam.gdc.goog.create  
subnets.ipam.gdc.goog.customized-allocate  
subnets.ipam.gdc.goog.delete  
subnets.ipam.gdc.goog.get  
subnets.ipam.gdc.goog.list  
subnets.ipam.gdc.goog.patch  
subnets.ipam.gdc.goog.update  
subnets.ipam.gdc.goog.watch  
  
**Subnet Project Operator**  
(`subnet-project-operator`) Creates and manages subnets in the project. |  **Zonal** subnets.ipam.gdc.goog.create  
subnets.ipam.gdc.goog.delete  
subnets.ipam.gdc.goog.get  
subnets.ipam.gdc.goog.list  
subnets.ipam.gdc.goog.patch  
subnets.ipam.gdc.goog.update  
subnets.ipam.gdc.goog.watch  
  
**Subnet Project Viewer**  
(`subnet-project-viewer`) Views subnets in the project. |  **Global** subnets.ipam.global.gdc.goog.get  
subnets.ipam.global.gdc.goog.list  
subnets.ipam.global.gdc.goog.watch  
  
**Zonal** subnets.ipam.gdc.goog.get  
subnets.ipam.gdc.goog.list  
subnets.ipam.gdc.goog.watch  
  
**User Cluster Backup Admin**  
(`usercluster-backup-admin`) Standard user cluster backup administrator in Project scope. |  **Zonal** backupplans.backup.gdc.goog.create  
backupplans.backup.gdc.goog.delete  
backupplans.backup.gdc.goog.get  
backupplans.backup.gdc.goog.list  
backupplans.backup.gdc.goog.patch  
backupplans.backup.gdc.goog.update  
backupplans.backup.gdc.goog.watch  
backups.backup.gdc.goog.create  
backups.backup.gdc.goog.delete  
backups.backup.gdc.goog.get  
backups.backup.gdc.goog.list  
backups.backup.gdc.goog.patch  
backups.backup.gdc.goog.update  
backups.backup.gdc.goog.watch  
deletebackuprequests.backup.gdc.goog.create  
deletebackuprequests.backup.gdc.goog.delete  
deletebackuprequests.backup.gdc.goog.get  
deletebackuprequests.backup.gdc.goog.list  
deletebackuprequests.backup.gdc.goog.patch  
deletebackuprequests.backup.gdc.goog.update  
deletebackuprequests.backup.gdc.goog.watch  
manualbackuprequests.backup.gdc.goog.create  
manualbackuprequests.backup.gdc.goog.delete  
manualbackuprequests.backup.gdc.goog.get  
manualbackuprequests.backup.gdc.goog.list  
manualbackuprequests.backup.gdc.goog.patch  
manualbackuprequests.backup.gdc.goog.update  
manualbackuprequests.backup.gdc.goog.watch  
manualrestorerequests.backup.gdc.goog.create  
manualrestorerequests.backup.gdc.goog.delete  
manualrestorerequests.backup.gdc.goog.get  
manualrestorerequests.backup.gdc.goog.list  
manualrestorerequests.backup.gdc.goog.patch  
manualrestorerequests.backup.gdc.goog.update  
manualrestorerequests.backup.gdc.goog.watch  
restoreplans.backup.gdc.goog.create  
restoreplans.backup.gdc.goog.delete  
restoreplans.backup.gdc.goog.get  
restoreplans.backup.gdc.goog.list  
restoreplans.backup.gdc.goog.patch  
restoreplans.backup.gdc.goog.update  
restoreplans.backup.gdc.goog.watch  
restores.backup.gdc.goog.create  
restores.backup.gdc.goog.delete  
restores.backup.gdc.goog.get  
restores.backup.gdc.goog.list  
restores.backup.gdc.goog.patch  
restores.backup.gdc.goog.update  
restores.backup.gdc.goog.watch  
volumebackups.backup.gdc.goog.get  
volumebackups.backup.gdc.goog.list  
volumebackups.backup.gdc.goog.watch  
volumerestores.backup.gdc.goog.get  
volumerestores.backup.gdc.goog.list  
volumerestores.backup.gdc.goog.watch  
  
**User Cluster Backup Viewer**  
(`usercluster-backup-viewer`) Standard user cluster backup viewer in Project scope. |  **Zonal** backupplans.backup.gdc.goog.get  
backupplans.backup.gdc.goog.list  
backupplans.backup.gdc.goog.watch  
backups.backup.gdc.goog.get  
backups.backup.gdc.goog.list  
backups.backup.gdc.goog.watch  
deletebackuprequests.backup.gdc.goog.get  
deletebackuprequests.backup.gdc.goog.list  
deletebackuprequests.backup.gdc.goog.watch  
manualbackuprequests.backup.gdc.goog.get  
manualbackuprequests.backup.gdc.goog.list  
manualbackuprequests.backup.gdc.goog.watch  
manualrestorerequests.backup.gdc.goog.get  
manualrestorerequests.backup.gdc.goog.list  
manualrestorerequests.backup.gdc.goog.watch  
restoreplans.backup.gdc.goog.get  
restoreplans.backup.gdc.goog.list  
restoreplans.backup.gdc.goog.watch  
restores.backup.gdc.goog.get  
restores.backup.gdc.goog.list  
restores.backup.gdc.goog.watch  
volumebackups.backup.gdc.goog.get  
volumebackups.backup.gdc.goog.list  
volumebackups.backup.gdc.goog.watch  
volumerestores.backup.gdc.goog.get  
volumerestores.backup.gdc.goog.list  
volumerestores.backup.gdc.goog.watch  
  
**VAISEARCH Admin**  
(`vaisearch-admin`) Administers all VAISEARCH resources in the project. |  **Zonal** answers.discoveryengine.gdc.goog.get  
collections.discoveryengine.gdc.goog.create  
collections.discoveryengine.gdc.goog.delete  
collections.discoveryengine.gdc.goog.get  
collections.discoveryengine.gdc.goog.list  
collections.discoveryengine.gdc.goog.update  
dataconnectorruns.discoveryengine.gdc.goog.list  
dataconnectorruns.discoveryengine.gdc.goog.start  
dataconnectors.discoveryengine.gdc.goog.get  
dataconnectors.discoveryengine.gdc.goog.setup  
dataconnectors.discoveryengine.gdc.goog.update  
dataconnectorsources.discoveryengine.gdc.goog.get  
dataconnectorsources.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.create  
datastores.discoveryengine.gdc.goog.delete  
datastores.discoveryengine.gdc.goog.get  
datastores.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.update  
documents.discoveryengine.gdc.goog.create  
documents.discoveryengine.gdc.goog.delete  
documents.discoveryengine.gdc.goog.get  
documents.discoveryengine.gdc.goog.import  
documents.discoveryengine.gdc.goog.list  
documents.discoveryengine.gdc.goog.update  
engines.discoveryengine.gdc.goog.create  
engines.discoveryengine.gdc.goog.delete  
engines.discoveryengine.gdc.goog.get  
engines.discoveryengine.gdc.goog.list  
engines.discoveryengine.gdc.goog.search  
engines.discoveryengine.gdc.goog.update  
files.discoveryengine.gdc.goog.create  
files.discoveryengine.gdc.goog.delete  
files.discoveryengine.gdc.goog.get  
files.discoveryengine.gdc.goog.list  
identitymappingstores.discoveryengine.gdc.goog.create  
identitymappingstores.discoveryengine.gdc.goog.delete  
identitymappingstores.discoveryengine.gdc.goog.get  
identitymappingstores.discoveryengine.gdc.goog.import  
identitymappingstores.discoveryengine.gdc.goog.list  
identitymappingstores.discoveryengine.gdc.goog.listidentitymappings  
identitymappingstores.discoveryengine.gdc.goog.purge  
operations.discoveryengine.gdc.goog.get  
operations.discoveryengine.gdc.goog.list  
sessions.discoveryengine.gdc.goog.answer  
sessions.discoveryengine.gdc.goog.create  
sessions.discoveryengine.gdc.goog.delete  
sessions.discoveryengine.gdc.goog.get  
sessions.discoveryengine.gdc.goog.list  
sessions.discoveryengine.gdc.goog.update  
  
**VAISEARCH Console UI Admin**  
(`vaisearch-admin-ui`) Administers VAISEARCH resources through the console UI. |  **Zonal** collections.discoveryengine.gdc.goog.list  
dataconnectorruns.discoveryengine.gdc.goog.list  
dataconnectors.discoveryengine.gdc.goog.get  
dataconnectorsources.discoveryengine.gdc.goog.get  
dataconnectorsources.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.create  
datastores.discoveryengine.gdc.goog.delete  
datastores.discoveryengine.gdc.goog.get  
datastores.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.patch  
datastores.discoveryengine.gdc.goog.update  
datastores.discoveryengine.gdc.goog.watch  
documents.discoveryengine.gdc.goog.import  
engines.discoveryengine.gdc.goog.create  
engines.discoveryengine.gdc.goog.delete  
engines.discoveryengine.gdc.goog.get  
engines.discoveryengine.gdc.goog.list  
engines.discoveryengine.gdc.goog.patch  
engines.discoveryengine.gdc.goog.update  
engines.discoveryengine.gdc.goog.watch  
files.discoveryengine.gdc.goog.create  
files.discoveryengine.gdc.goog.delete  
files.discoveryengine.gdc.goog.get  
files.discoveryengine.gdc.goog.list  
operations.discoveryengine.gdc.goog.get  
  
**VAISEARCH Developer**  
(`vaisearch-developer`) Manages all VAISEARCH resources in the project. |  **Zonal** answers.discoveryengine.gdc.goog.get  
collections.discoveryengine.gdc.goog.create  
collections.discoveryengine.gdc.goog.delete  
collections.discoveryengine.gdc.goog.get  
collections.discoveryengine.gdc.goog.list  
collections.discoveryengine.gdc.goog.update  
dataconnectorruns.discoveryengine.gdc.goog.list  
dataconnectorruns.discoveryengine.gdc.goog.start  
dataconnectors.discoveryengine.gdc.goog.get  
dataconnectors.discoveryengine.gdc.goog.setup  
dataconnectors.discoveryengine.gdc.goog.update  
dataconnectorsources.discoveryengine.gdc.goog.get  
dataconnectorsources.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.create  
datastores.discoveryengine.gdc.goog.delete  
datastores.discoveryengine.gdc.goog.get  
datastores.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.update  
documents.discoveryengine.gdc.goog.create  
documents.discoveryengine.gdc.goog.delete  
documents.discoveryengine.gdc.goog.get  
documents.discoveryengine.gdc.goog.import  
documents.discoveryengine.gdc.goog.list  
documents.discoveryengine.gdc.goog.update  
engines.discoveryengine.gdc.goog.create  
engines.discoveryengine.gdc.goog.delete  
engines.discoveryengine.gdc.goog.get  
engines.discoveryengine.gdc.goog.list  
engines.discoveryengine.gdc.goog.search  
engines.discoveryengine.gdc.goog.update  
files.discoveryengine.gdc.goog.create  
files.discoveryengine.gdc.goog.delete  
files.discoveryengine.gdc.goog.get  
files.discoveryengine.gdc.goog.list  
identitymappingstores.discoveryengine.gdc.goog.create  
identitymappingstores.discoveryengine.gdc.goog.delete  
identitymappingstores.discoveryengine.gdc.goog.get  
identitymappingstores.discoveryengine.gdc.goog.import  
identitymappingstores.discoveryengine.gdc.goog.list  
identitymappingstores.discoveryengine.gdc.goog.listidentitymappings  
identitymappingstores.discoveryengine.gdc.goog.purge  
operations.discoveryengine.gdc.goog.get  
operations.discoveryengine.gdc.goog.list  
sessions.discoveryengine.gdc.goog.answer  
sessions.discoveryengine.gdc.goog.create  
sessions.discoveryengine.gdc.goog.delete  
sessions.discoveryengine.gdc.goog.get  
sessions.discoveryengine.gdc.goog.list  
sessions.discoveryengine.gdc.goog.update  
  
**VAISEARCH User**  
(`vaisearch-user`) Interacts with VAISEARCH chat UI. |  **Zonal** answers.discoveryengine.gdc.goog.get  
engines.discoveryengine.gdc.goog.search  
files.discoveryengine.gdc.goog.create  
files.discoveryengine.gdc.goog.delete  
files.discoveryengine.gdc.goog.get  
files.discoveryengine.gdc.goog.list  
sessions.discoveryengine.gdc.goog.answer  
  
**VAISEARCH Viewer**  
(`vaisearch-viewer`) Views all VAISEARCH resources in the project. |  **Zonal** answers.discoveryengine.gdc.goog.get  
collections.discoveryengine.gdc.goog.get  
collections.discoveryengine.gdc.goog.list  
dataconnectorruns.discoveryengine.gdc.goog.list  
dataconnectors.discoveryengine.gdc.goog.get  
dataconnectorsources.discoveryengine.gdc.goog.get  
dataconnectorsources.discoveryengine.gdc.goog.list  
datastores.discoveryengine.gdc.goog.get  
datastores.discoveryengine.gdc.goog.list  
documents.discoveryengine.gdc.goog.get  
documents.discoveryengine.gdc.goog.list  
engines.discoveryengine.gdc.goog.get  
engines.discoveryengine.gdc.goog.list  
engines.discoveryengine.gdc.goog.search  
files.discoveryengine.gdc.goog.get  
files.discoveryengine.gdc.goog.list  
identitymappingstores.discoveryengine.gdc.goog.get  
identitymappingstores.discoveryengine.gdc.goog.list  
identitymappingstores.discoveryengine.gdc.goog.listidentitymappings  
operations.discoveryengine.gdc.goog.get  
operations.discoveryengine.gdc.goog.list  
sessions.discoveryengine.gdc.goog.answer  
sessions.discoveryengine.gdc.goog.get  
sessions.discoveryengine.gdc.goog.list  
  
**Vertex AI Gemini Flash Developer**  
(`ai-gemini-flash-developer`) Performs predict and chat-completions requests on Gemini Flash model endpoints. |  **Zonal** endpoints.gemini-flash.gdc.goog.chat-completions  
endpoints.gemini-flash.gdc.goog.predict  
  
**Vertex AI Multimodal Embedding Developer**  
(`ai-multimodal-embedding-developer`) Performs predict requests on Multimodal Embedding model endpoints. |  **Zonal** endpoints.multimodal-embedding.gdc.goog.predict  
  
**Vertex AI OCR Developer**  
(`ai-ocr-developer`) Accesses the OCR service. |  **Zonal** annotators.vision.gdc.goog.async-batch-annotate-files  
annotators.vision.gdc.goog.async-batch-annotate-images  
annotators.vision.gdc.goog.batch-annotate-files  
annotators.vision.gdc.goog.batch-annotate-images  
annotators.vision.gdc.goog.create  
annotators.vision.gdc.goog.delete  
annotators.vision.gdc.goog.get  
annotators.vision.gdc.goog.list  
annotators.vision.gdc.goog.patch  
annotators.vision.gdc.goog.update  
annotators.vision.gdc.goog.watch  
  
**Vertex AI Prediction Admin**  
(`vertex-ai-prediction-admin`) Manages Online Prediction related resources. |  **Kubernetes cluster** deployedmodels.prediction.aiplatform.gdc.goog.create  
deployedmodels.prediction.aiplatform.gdc.goog.delete  
deployedmodels.prediction.aiplatform.gdc.goog.deletecollection  
deployedmodels.prediction.aiplatform.gdc.goog.get  
deployedmodels.prediction.aiplatform.gdc.goog.list  
deployedmodels.prediction.aiplatform.gdc.goog.patch  
deployedmodels.prediction.aiplatform.gdc.goog.update  
deployedmodels.prediction.aiplatform.gdc.goog.watch  
endpoints.aiplatform.gdc.goog.create  
endpoints.aiplatform.gdc.goog.delete  
endpoints.aiplatform.gdc.goog.deletecollection  
endpoints.aiplatform.gdc.goog.get  
endpoints.aiplatform.gdc.goog.list  
endpoints.aiplatform.gdc.goog.patch  
endpoints.aiplatform.gdc.goog.update  
endpoints.aiplatform.gdc.goog.watch  
resourcepools.prediction.aiplatform.gdc.goog.create  
resourcepools.prediction.aiplatform.gdc.goog.delete  
resourcepools.prediction.aiplatform.gdc.goog.deletecollection  
resourcepools.prediction.aiplatform.gdc.goog.get  
resourcepools.prediction.aiplatform.gdc.goog.list  
resourcepools.prediction.aiplatform.gdc.goog.patch  
resourcepools.prediction.aiplatform.gdc.goog.update  
resourcepools.prediction.aiplatform.gdc.goog.watch  
  
**Vertex AI Prediction User**  
(`vertex-ai-prediction-user`) Performs predict requests on AI Platform endpoints. |  **Zonal** endpoints.aiplatform.googleapis.com.predict  
  
**Vertex AI Speech Chirp Developer**  
(`ai-speech-chirp-developer`) Accesses the Speech Chirp service. |  **Zonal** recognizers.speech.gdc.goog.create  
recognizers.speech.gdc.goog.delete  
recognizers.speech.gdc.goog.get  
recognizers.speech.gdc.goog.list  
recognizers.speech.gdc.goog.patch  
recognizers.speech.gdc.goog.recognize  
recognizers.speech.gdc.goog.streaming-recognize  
recognizers.speech.gdc.goog.update  
recognizers.speech.gdc.goog.watch  
  
**Vertex AI Speech Developer**  
(`ai-speech-developer`) Accesses the Speech service. |  **Zonal** recognizers.speech.gdc.goog.create  
recognizers.speech.gdc.goog.delete  
recognizers.speech.gdc.goog.get  
recognizers.speech.gdc.goog.list  
recognizers.speech.gdc.goog.patch  
recognizers.speech.gdc.goog.recognize  
recognizers.speech.gdc.goog.streaming-recognize  
recognizers.speech.gdc.goog.update  
recognizers.speech.gdc.goog.watch  
  
**Vertex AI Text Embedding Developer**  
(`ai-text-embedding-developer`) Performs predict requests on Text Embedding model endpoints. |  **Zonal** endpoints.text-embedding-005.gdc.goog.predict  
endpoints.text-embedding.gdc.goog.predict  
  
**Vertex AI Text Embedding Multilingual Developer**  
(`ai-text-embedding-multilingual-developer`) Performs predict requests on Text Embedding Multilingual model endpoints. |  **Zonal** endpoints.text-embedding-multilingual.gdc.goog.predict  
  
**Vertex AI Translation Developer**  
(`ai-translation-developer`) Accesses the Translation service. |  **Zonal** operations.translation.gdc.goog.batch-translate-document  
operations.translation.gdc.goog.create  
operations.translation.gdc.goog.create-glossary  
operations.translation.gdc.goog.delete  
operations.translation.gdc.goog.delete-glossary  
operations.translation.gdc.goog.detect-language  
operations.translation.gdc.goog.get  
operations.translation.gdc.goog.get-glossary  
operations.translation.gdc.goog.get-supported-languages  
operations.translation.gdc.goog.list  
operations.translation.gdc.goog.list-glossaries  
operations.translation.gdc.goog.patch  
operations.translation.gdc.goog.translate-document  
operations.translation.gdc.goog.translate-text  
operations.translation.gdc.goog.update  
operations.translation.gdc.goog.watch  
translators.translation.gdc.goog.batch-translate-document  
translators.translation.gdc.goog.create  
translators.translation.gdc.goog.create-glossary  
translators.translation.gdc.goog.delete  
translators.translation.gdc.goog.delete-glossary  
translators.translation.gdc.goog.detect-language  
translators.translation.gdc.goog.get  
translators.translation.gdc.goog.get-glossary  
translators.translation.gdc.goog.get-supported-languages  
translators.translation.gdc.goog.list  
translators.translation.gdc.goog.list-glossaries  
translators.translation.gdc.goog.patch  
translators.translation.gdc.goog.translate-document  
translators.translation.gdc.goog.translate-text  
translators.translation.gdc.goog.update  
translators.translation.gdc.goog.watch  
  
**Virtual Machine Image Project Admin**  
(`project-vm-image-admin`) Manages VM images in project namespace. |  **Global** virtualmachineimages.virtualmachine.global.gdc.goog.get  
virtualmachineimages.virtualmachine.global.gdc.goog.list  
virtualmachineimages.virtualmachine.global.gdc.goog.watch  
  
**Zonal** buckets.object.gdc.goog.create  
buckets.object.gdc.goog.delete  
buckets.object.gdc.goog.get  
buckets.object.gdc.goog.list  
buckets.object.gdc.goog.patch  
buckets.object.gdc.goog.read-object  
buckets.object.gdc.goog.update  
buckets.object.gdc.goog.watch  
buckets.object.gdc.goog.write-object  
virtualmachineimage.virtualmachineview.gdc.goog.get  
virtualmachineimage.virtualmachineview.gdc.goog.list  
virtualmachineimage.virtualmachineview.gdc.goog.watch  
virtualmachineimageimports.virtualmachine.gdc.goog.create  
virtualmachineimageimports.virtualmachine.gdc.goog.delete  
virtualmachineimageimports.virtualmachine.gdc.goog.get  
virtualmachineimageimports.virtualmachine.gdc.goog.list  
virtualmachineimageimports.virtualmachine.gdc.goog.patch  
virtualmachineimageimports.virtualmachine.gdc.goog.update  
virtualmachineimageimports.virtualmachine.gdc.goog.watch  
virtualmachineimages.virtualmachine.gdc.goog.get  
virtualmachineimages.virtualmachine.gdc.goog.list  
virtualmachineimages.virtualmachine.gdc.goog.watch  
  
**Virtual Machine Image Project Viewer**  
(`project-vm-image-viewer`) Views VM images in project namespace. |  **Global** virtualmachineimages.virtualmachine.global.gdc.goog.get  
virtualmachineimages.virtualmachine.global.gdc.goog.list  
virtualmachineimages.virtualmachine.global.gdc.goog.watch  
  
**Zonal** virtualmachineimage.virtualmachineview.gdc.goog.get  
virtualmachineimage.virtualmachineview.gdc.goog.list  
virtualmachineimage.virtualmachineview.gdc.goog.watch  
virtualmachineimages.virtualmachine.gdc.goog.get  
virtualmachineimages.virtualmachine.gdc.goog.list  
virtualmachineimages.virtualmachine.gdc.goog.watch  
  
**Virtual Machine Project Admin**  
(`project-vm-admin`) Manages VMs in project namespace. |  **Global** virtualmachineimages.virtualmachine.global.gdc.goog.get  
virtualmachineimages.virtualmachine.global.gdc.goog.list  
virtualmachineimages.virtualmachine.global.gdc.goog.watch  
virtualmachinetemplates.virtualmachine.global.gdc.goog.create  
virtualmachinetemplates.virtualmachine.global.gdc.goog.delete  
virtualmachinetemplates.virtualmachine.global.gdc.goog.get  
virtualmachinetemplates.virtualmachine.global.gdc.goog.list  
virtualmachinetemplates.virtualmachine.global.gdc.goog.watch  
volumereplicationrelationships.storage.global.gdc.goog.create  
volumereplicationrelationships.storage.global.gdc.goog.delete  
volumereplicationrelationships.storage.global.gdc.goog.get  
volumereplicationrelationships.storage.global.gdc.goog.list  
volumereplicationrelationships.storage.global.gdc.goog.patch  
volumereplicationrelationships.storage.global.gdc.goog.update  
volumereplicationrelationships.storage.global.gdc.goog.watch  
  
**Zonal** projectnetworkpolicies.networking.gdc.goog.get  
projectnetworkpolicies.networking.gdc.goog.list  
secrets.get  
secrets.list  
virtualmachineaccessrequests.virtualmachine.gdc.goog.create  
virtualmachineaccessrequests.virtualmachine.gdc.goog.delete  
virtualmachineaccessrequests.virtualmachine.gdc.goog.get  
virtualmachineaccessrequests.virtualmachine.gdc.goog.list  
virtualmachineaccessrequests.virtualmachine.gdc.goog.patch  
virtualmachineaccessrequests.virtualmachine.gdc.goog.update  
virtualmachineaccessrequests.virtualmachine.gdc.goog.watch  
virtualmachinebackupplans.virtualmachine.gdc.goog.delete  
virtualmachinebackupplans.virtualmachine.gdc.goog.get  
virtualmachinebackupplans.virtualmachine.gdc.goog.list  
virtualmachinebackupplans.virtualmachine.gdc.goog.patch  
virtualmachinebackupplans.virtualmachine.gdc.goog.update  
virtualmachinebackupplans.virtualmachine.gdc.goog.watch  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.create  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.delete  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.get  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.list  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.patch  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.update  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.watch  
virtualmachinebackuprequests.virtualmachine.gdc.goog.create  
virtualmachinebackuprequests.virtualmachine.gdc.goog.delete  
virtualmachinebackuprequests.virtualmachine.gdc.goog.get  
virtualmachinebackuprequests.virtualmachine.gdc.goog.list  
virtualmachinebackuprequests.virtualmachine.gdc.goog.watch  
virtualmachinebackups.virtualmachine.gdc.goog.get  
virtualmachinebackups.virtualmachine.gdc.goog.list  
virtualmachinebackups.virtualmachine.gdc.goog.watch  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.create  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.delete  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.get  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.list  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.watch  
virtualmachinedisks.virtualmachine.gdc.goog.create  
virtualmachinedisks.virtualmachine.gdc.goog.delete  
virtualmachinedisks.virtualmachine.gdc.goog.get  
virtualmachinedisks.virtualmachine.gdc.goog.list  
virtualmachinedisks.virtualmachine.gdc.goog.patch  
virtualmachinedisks.virtualmachine.gdc.goog.update  
virtualmachinedisks.virtualmachine.gdc.goog.watch  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.create  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.delete  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.get  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.list  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.patch  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.update  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.watch  
virtualmachineimages.virtualmachine.gdc.goog.get  
virtualmachineimages.virtualmachine.gdc.goog.list  
virtualmachineimages.virtualmachine.gdc.goog.watch  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.create  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.delete  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.get  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.list  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.patch  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.update  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.watch  
virtualmachinerestorerequests.virtualmachine.gdc.goog.create  
virtualmachinerestorerequests.virtualmachine.gdc.goog.delete  
virtualmachinerestorerequests.virtualmachine.gdc.goog.get  
virtualmachinerestorerequests.virtualmachine.gdc.goog.list  
virtualmachinerestorerequests.virtualmachine.gdc.goog.watch  
virtualmachinerestores.virtualmachine.gdc.goog.delete  
virtualmachinerestores.virtualmachine.gdc.goog.get  
virtualmachinerestores.virtualmachine.gdc.goog.list  
virtualmachinerestores.virtualmachine.gdc.goog.patch  
virtualmachinerestores.virtualmachine.gdc.goog.update  
virtualmachinerestores.virtualmachine.gdc.goog.watch  
virtualmachines.virtualmachine.gdc.goog.console  
virtualmachines.virtualmachine.gdc.goog.create  
virtualmachines.virtualmachine.gdc.goog.delete  
virtualmachines.virtualmachine.gdc.goog.get  
virtualmachines.virtualmachine.gdc.goog.getmetadata  
virtualmachines.virtualmachine.gdc.goog.list  
virtualmachines.virtualmachine.gdc.goog.patch  
virtualmachines.virtualmachine.gdc.goog.setmetadata  
virtualmachines.virtualmachine.gdc.goog.update  
virtualmachines.virtualmachine.gdc.goog.watch  
virtualmachines/restart.virtualmachineoperations.gdc.goog.update  
  
**Virtual Machine Project Viewer**  
(`project-vm-viewer`) Views VMs in project namespace. |  **Global** virtualmachineimages.virtualmachine.global.gdc.goog.get  
virtualmachineimages.virtualmachine.global.gdc.goog.list  
virtualmachineimages.virtualmachine.global.gdc.goog.watch  
volumereplicationrelationships.storage.global.gdc.goog.get  
volumereplicationrelationships.storage.global.gdc.goog.list  
volumereplicationrelationships.storage.global.gdc.goog.watch  
  
**Zonal** projectnetworkpolicies.networking.gdc.goog.get  
projectnetworkpolicies.networking.gdc.goog.list  
secrets.get  
secrets.list  
virtualmachineaccessrequests.virtualmachine.gdc.goog.get  
virtualmachineaccessrequests.virtualmachine.gdc.goog.list  
virtualmachineaccessrequests.virtualmachine.gdc.goog.watch  
virtualmachinebackupplans.virtualmachine.gdc.goog.get  
virtualmachinebackupplans.virtualmachine.gdc.goog.list  
virtualmachinebackupplans.virtualmachine.gdc.goog.watch  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.get  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.list  
virtualmachinebackupplantemplates.virtualmachine.gdc.goog.watch  
virtualmachinebackuprequests.virtualmachine.gdc.goog.get  
virtualmachinebackuprequests.virtualmachine.gdc.goog.list  
virtualmachinebackuprequests.virtualmachine.gdc.goog.watch  
virtualmachinebackups.virtualmachine.gdc.goog.get  
virtualmachinebackups.virtualmachine.gdc.goog.list  
virtualmachinebackups.virtualmachine.gdc.goog.watch  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.get  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.list  
virtualmachinedeletebackuprequests.virtualmachine.gdc.goog.watch  
virtualmachinedisks.virtualmachine.gdc.goog.get  
virtualmachinedisks.virtualmachine.gdc.goog.list  
virtualmachinedisks.virtualmachine.gdc.goog.watch  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.get  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.list  
virtualmachineexternalaccesses.virtualmachine.gdc.goog.watch  
virtualmachineimages.virtualmachine.gdc.goog.get  
virtualmachineimages.virtualmachine.gdc.goog.list  
virtualmachineimages.virtualmachine.gdc.goog.watch  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.get  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.list  
virtualmachinepasswordresetrequests.virtualmachine.gdc.goog.watch  
virtualmachinerestorerequests.virtualmachine.gdc.goog.get  
virtualmachinerestorerequests.virtualmachine.gdc.goog.list  
virtualmachinerestorerequests.virtualmachine.gdc.goog.watch  
virtualmachinerestores.virtualmachine.gdc.goog.get  
virtualmachinerestores.virtualmachine.gdc.goog.list  
virtualmachinerestores.virtualmachine.gdc.goog.watch  
virtualmachines.virtualmachine.gdc.goog.get  
virtualmachines.virtualmachine.gdc.goog.getmetadata  
virtualmachines.virtualmachine.gdc.goog.list  
virtualmachines.virtualmachine.gdc.goog.watch  
  
**Virtual Machines Backup User**  
(`vmbackup-user`) Grants create access to VM backups and restores, and view access to VM backup plans. |  **Zonal** virtualmachinebackupplans.virtualmachine.gdc.goog.get  
virtualmachinebackupplans.virtualmachine.gdc.goog.list  
virtualmachinebackupplans.virtualmachine.gdc.goog.watch  
virtualmachinebackuprequest.virtualmachine.gdc.goog.create  
virtualmachinebackuprequest.virtualmachine.gdc.goog.delete  
virtualmachinebackuprequest.virtualmachine.gdc.goog.get  
virtualmachinebackuprequest.virtualmachine.gdc.goog.list  
virtualmachinebackuprequest.virtualmachine.gdc.goog.patch  
virtualmachinebackuprequest.virtualmachine.gdc.goog.update  
virtualmachinebackuprequest.virtualmachine.gdc.goog.watch  
virtualmachinebackups.virtualmachine.gdc.goog.get  
virtualmachinebackups.virtualmachine.gdc.goog.list  
virtualmachinebackups.virtualmachine.gdc.goog.watch  
virtualmachinerestorerequest.virtualmachine.gdc.goog.create  
virtualmachinerestorerequest.virtualmachine.gdc.goog.delete  
virtualmachinerestorerequest.virtualmachine.gdc.goog.get  
virtualmachinerestorerequest.virtualmachine.gdc.goog.list  
virtualmachinerestorerequest.virtualmachine.gdc.goog.patch  
virtualmachinerestorerequest.virtualmachine.gdc.goog.update  
virtualmachinerestorerequest.virtualmachine.gdc.goog.watch  
virtualmachinerestores.virtualmachine.gdc.goog.get  
virtualmachinerestores.virtualmachine.gdc.goog.list  
virtualmachinerestores.virtualmachine.gdc.goog.watch  
  
**Virtual Machines Backup Viewer**  
(`vmbackup-viewer`) Grants view access to vm backups, vm restores, vm backup plans, and vm restore plans. |  **Zonal** virtualmachinebackupplans.virtualmachine.gdc.goog.get  
virtualmachinebackupplans.virtualmachine.gdc.goog.list  
virtualmachinebackupplans.virtualmachine.gdc.goog.watch  
virtualmachinebackuprequest.virtualmachine.gdc.goog.get  
virtualmachinebackuprequest.virtualmachine.gdc.goog.list  
virtualmachinebackuprequest.virtualmachine.gdc.goog.watch  
virtualmachinebackups.virtualmachine.gdc.goog.get  
virtualmachinebackups.virtualmachine.gdc.goog.list  
virtualmachinebackups.virtualmachine.gdc.goog.watch  
virtualmachinerestorerequest.virtualmachine.gdc.goog.get  
virtualmachinerestorerequest.virtualmachine.gdc.goog.list  
virtualmachinerestorerequest.virtualmachine.gdc.goog.watch  
virtualmachinerestores.virtualmachine.gdc.goog.get  
virtualmachinerestores.virtualmachine.gdc.goog.list  
virtualmachinerestores.virtualmachine.gdc.goog.watch  
  
**Workbench Notebooks Admin**  
(`workbench-notebooks-admin`) Create, read and delete access to Workbench Notebooks. Read access to ClusterInfos |  **Zonal** clusterinfos.resourcemanager.private.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.list  
notebook/notebook-root.istio.resourcemanager.gdc.goog.CONNECT  
notebook/notebook-root.istio.resourcemanager.gdc.goog.DELETE  
notebook/notebook-root.istio.resourcemanager.gdc.goog.GET  
notebook/notebook-root.istio.resourcemanager.gdc.goog.HEAD  
notebook/notebook-root.istio.resourcemanager.gdc.goog.OPTIONS  
notebook/notebook-root.istio.resourcemanager.gdc.goog.PATCH  
notebook/notebook-root.istio.resourcemanager.gdc.goog.POST  
notebook/notebook-root.istio.resourcemanager.gdc.goog.PUT  
notebook/notebook-root.istio.resourcemanager.gdc.goog.TRACE  
notebooks.aiplatform.gdc.goog.create  
notebooks.aiplatform.gdc.goog.delete  
notebooks.aiplatform.gdc.goog.deletecollection  
notebooks.aiplatform.gdc.goog.get  
notebooks.aiplatform.gdc.goog.list  
notebooks.aiplatform.gdc.goog.patch  
notebooks.aiplatform.gdc.goog.update  
notebooks.aiplatform.gdc.goog.watch  
notebooks/status.aiplatform.gdc.goog.get  
notebooks/status.aiplatform.gdc.goog.list  
  
**Workbench Notebooks Viewer**  
(`workbench-notebooks-viewer`) Read access to Workbench Notebooks |  **Zonal** clusterinfos.resourcemanager.private.gdc.goog.get  
clusterinfos.resourcemanager.private.gdc.goog.list  
notebook/notebook-root.istio.resourcemanager.gdc.goog.CONNECT  
notebook/notebook-root.istio.resourcemanager.gdc.goog.DELETE  
notebook/notebook-root.istio.resourcemanager.gdc.goog.GET  
notebook/notebook-root.istio.resourcemanager.gdc.goog.HEAD  
notebook/notebook-root.istio.resourcemanager.gdc.goog.OPTIONS  
notebook/notebook-root.istio.resourcemanager.gdc.goog.PATCH  
notebook/notebook-root.istio.resourcemanager.gdc.goog.POST  
notebook/notebook-root.istio.resourcemanager.gdc.goog.PUT  
notebook/notebook-root.istio.resourcemanager.gdc.goog.TRACE  
notebooks.aiplatform.gdc.goog.get  
notebooks.aiplatform.gdc.goog.list  
notebooks/status.aiplatform.gdc.goog.get  
notebooks/status.aiplatform.gdc.goog.list  
  
**Workload Viewer**  
(`workload-viewer`) Views pods and deployments in a project. |  **Kubernetes cluster** deployments.apps.get  
deployments.apps.list  
deployments.apps.watch  
pods.get  
pods.list  
pods.watch  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
