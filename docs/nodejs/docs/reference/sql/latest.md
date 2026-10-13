---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/
title: Cloud SQL Admin API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:15.571224+00:00
---

# Cloud SQL Admin API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud SQL Admin API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/sql.svg)](https://www.npmjs.org/package/@google-cloud/sql)

Cloud SQL Admin API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/CHANGELOG.md).

  * [Cloud SQL Admin API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/sql/latest)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Versioning

  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Cloud SQL Admin API API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/sql
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backup_runs_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backup_runs_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backup_runs_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backup_runs_service.list.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backups_service.create_backup.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backups_service.delete_backup.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backups_service.get_backup.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backups_service.list_backups.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_backups_service.update_backup.js)  
generate ephemeral cert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_connect_service.generate_ephemeral_cert.js)  
get connect settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_connect_service.get_connect_settings.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_databases_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_databases_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_databases_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_databases_service.list.js)  
patch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_databases_service.patch.js)  
update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_databases_service.update.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_flags_service.list.js)  
acquire ssrs lease | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.acquire_ssrs_lease.js)  
add entra id certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.add_entra_id_certificate.js)  
add server ca | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.add_server_ca.js)  
add server certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.add_server_certificate.js)  
clone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.clone.js)  
create ephemeral | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.create_ephemeral.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.delete.js)  
demote | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.demote.js)  
demote master | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.demote_master.js)  
execute sql | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.execute_sql.js)  
export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.export.js)  
failover | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.failover.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.get.js)  
get disk shrink config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.get_disk_shrink_config.js)  
get latest recovery time | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.get_latest_recovery_time.js)  
import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.import.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.list.js)  
list entra id certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.list_entra_id_certificates.js)  
list server cas | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.list_server_cas.js)  
list server certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.list_server_certificates.js)  
patch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.patch.js)  
perform disk shrink | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.perform_disk_shrink.js)  
point in time restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.point_in_time_restore.js)  
pre check major version upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.pre_check_major_version_upgrade.js)  
promote replica | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.promote_replica.js)  
reencrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.reencrypt.js)  
release ssrs lease | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.release_ssrs_lease.js)  
reschedule maintenance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.reschedule_maintenance.js)  
reset replica size | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.reset_replica_size.js)  
reset ssl config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.reset_ssl_config.js)  
restart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.restart.js)  
restore backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.restore_backup.js)  
rotate entra id certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.rotate_entra_id_certificate.js)  
rotate server ca | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.rotate_server_ca.js)  
rotate server certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.rotate_server_certificate.js)  
start external sync | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.start_external_sync.js)  
start replica | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.start_replica.js)  
stop replica | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.stop_replica.js)  
switchover | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.switchover.js)  
truncate log | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.truncate_log.js)  
update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.update.js)  
verify external sync settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_instances_service.verify_external_sync_settings.js)  
cancel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_operations_service.cancel.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_operations_service.get.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_operations_service.list.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_ssl_certs_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_ssl_certs_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_ssl_certs_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_ssl_certs_service.list.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_tiers_service.list.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_users_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_users_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_users_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_users_service.list.js)  
update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1/sql_users_service.update.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backup_runs_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backup_runs_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backup_runs_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backup_runs_service.list.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backups_service.create_backup.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backups_service.delete_backup.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backups_service.get_backup.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backups_service.list_backups.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_backups_service.update_backup.js)  
generate ephemeral cert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_connect_service.generate_ephemeral_cert.js)  
get connect settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_connect_service.get_connect_settings.js)  
resolve connect settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_connect_service.resolve_connect_settings.js)  
stream sql data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_data_service.stream_sql_data.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_databases_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_databases_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_databases_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_databases_service.list.js)  
patch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_databases_service.patch.js)  
update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_databases_service.update.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_flags_service.list.js)  
acquire ssrs lease | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.acquire_ssrs_lease.js)  
add entra id certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.add_entra_id_certificate.js)  
add server ca | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.add_server_ca.js)  
add server certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.add_server_certificate.js)  
clone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.clone.js)  
create ephemeral | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.create_ephemeral.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.delete.js)  
demote | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.demote.js)  
demote master | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.demote_master.js)  
execute sql | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.execute_sql.js)  
export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.export.js)  
failover | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.failover.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.get.js)  
get disk shrink config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.get_disk_shrink_config.js)  
get latest recovery time | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.get_latest_recovery_time.js)  
import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.import.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.list.js)  
list entra id certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.list_entra_id_certificates.js)  
list server cas | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.list_server_cas.js)  
list server certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.list_server_certificates.js)  
patch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.patch.js)  
perform disk shrink | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.perform_disk_shrink.js)  
point in time restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.point_in_time_restore.js)  
pre check major version upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.pre_check_major_version_upgrade.js)  
promote replica | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.promote_replica.js)  
reencrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.reencrypt.js)  
release ssrs lease | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.release_ssrs_lease.js)  
reschedule maintenance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.reschedule_maintenance.js)  
reset replica size | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.reset_replica_size.js)  
reset ssl config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.reset_ssl_config.js)  
restart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.restart.js)  
restore backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.restore_backup.js)  
rotate entra id certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.rotate_entra_id_certificate.js)  
rotate server ca | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.rotate_server_ca.js)  
rotate server certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.rotate_server_certificate.js)  
start external sync | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.start_external_sync.js)  
start replica | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.start_replica.js)  
stop replica | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.stop_replica.js)  
switchover | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.switchover.js)  
truncate log | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.truncate_log.js)  
update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.update.js)  
verify external sync settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_instances_service.verify_external_sync_settings.js)  
cancel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_operations_service.cancel.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_operations_service.get.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_operations_service.list.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_ssl_certs_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_ssl_certs_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_ssl_certs_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_ssl_certs_service.list.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_tiers_service.list.js)  
delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_users_service.delete.js)  
get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_users_service.get.js)  
insert | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_users_service.insert.js)  
list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_users_service.list.js)  
update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-sql/samples/generated/v1beta4/sql_users_service.update.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/sql@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
