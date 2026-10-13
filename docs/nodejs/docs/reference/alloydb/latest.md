---
url: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/
title: AlloyDB API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:56.843440+00:00
---

# AlloyDB API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  AlloyDB API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  1.10.1  1.9.0  1.6.0  1.4.1  1.3.0  1.2.0  0.1.1 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/alloydb.svg)](https://www.npmjs.org/package/@google-cloud/alloydb)

AlloyDB API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/CHANGELOG.md).

  * [AlloyDB API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/alloydb/latest)
  * [AlloyDB API Documentation](https://cloud.google.com/alloydb/docs)



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
  3. [Enable the AlloyDB API API](https://console.cloud.google.com/flows/enableapi?apiid=alloydb.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/alloydb
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
batch create instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.batch_create_instances.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.create_backup.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.create_cluster.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.create_instance.js)  
create secondary cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.create_secondary_cluster.js)  
create secondary instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.create_secondary_instance.js)  
create user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.create_user.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.delete_backup.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.delete_cluster.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.delete_instance.js)  
delete user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.delete_user.js)  
execute sql | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.execute_sql.js)  
export cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.export_cluster.js)  
failover instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.failover_instance.js)  
generate client certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.generate_client_certificate.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.get_backup.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.get_cluster.js)  
get connection info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.get_connection_info.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.get_instance.js)  
get user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.get_user.js)  
import cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.import_cluster.js)  
inject fault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.inject_fault.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.list_backups.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.list_clusters.js)  
list databases | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.list_databases.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.list_instances.js)  
list supported database flags | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.list_supported_database_flags.js)  
list users | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.list_users.js)  
promote cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.promote_cluster.js)  
restart instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.restart_instance.js)  
restore cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.restore_cluster.js)  
switchover cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.switchover_cluster.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.update_backup.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.update_cluster.js)  
update instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.update_instance.js)  
update user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.update_user.js)  
upgrade cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_admin.upgrade_cluster.js)  
restore from cloud s q l | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1/alloy_d_b_c_s_q_l_admin.restore_from_cloud_s_q_l.js)  
batch create instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.batch_create_instances.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_backup.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_cluster.js)  
create database | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_database.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_instance.js)  
create secondary cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_secondary_cluster.js)  
create secondary instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_secondary_instance.js)  
create user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.create_user.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.delete_backup.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.delete_cluster.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.delete_instance.js)  
delete user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.delete_user.js)  
execute sql | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.execute_sql.js)  
export cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.export_cluster.js)  
failover instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.failover_instance.js)  
generate client certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.generate_client_certificate.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.get_backup.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.get_cluster.js)  
get connection info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.get_connection_info.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.get_instance.js)  
get user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.get_user.js)  
import cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.import_cluster.js)  
inject fault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.inject_fault.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.list_backups.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.list_clusters.js)  
list databases | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.list_databases.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.list_instances.js)  
list supported database flags | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.list_supported_database_flags.js)  
list users | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.list_users.js)  
promote cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.promote_cluster.js)  
restart instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.restart_instance.js)  
restore cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.restore_cluster.js)  
switchover cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.switchover_cluster.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.update_backup.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.update_cluster.js)  
update instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.update_instance.js)  
update user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.update_user.js)  
upgrade cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_admin.upgrade_cluster.js)  
restore from cloud s q l | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1alpha/alloy_d_b_c_s_q_l_admin.restore_from_cloud_s_q_l.js)  
batch create instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.batch_create_instances.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_backup.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_cluster.js)  
create database | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_database.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_instance.js)  
create secondary cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_secondary_cluster.js)  
create secondary instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_secondary_instance.js)  
create user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.create_user.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.delete_backup.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.delete_cluster.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.delete_instance.js)  
delete user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.delete_user.js)  
execute sql | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.execute_sql.js)  
export cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.export_cluster.js)  
failover instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.failover_instance.js)  
generate client certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.generate_client_certificate.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.get_backup.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.get_cluster.js)  
get connection info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.get_connection_info.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.get_instance.js)  
get user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.get_user.js)  
import cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.import_cluster.js)  
inject fault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.inject_fault.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.list_backups.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.list_clusters.js)  
list databases | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.list_databases.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.list_instances.js)  
list supported database flags | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.list_supported_database_flags.js)  
list users | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.list_users.js)  
promote cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.promote_cluster.js)  
restart instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.restart_instance.js)  
restore cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.restore_cluster.js)  
switchover cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.switchover_cluster.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.update_backup.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.update_cluster.js)  
update instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.update_instance.js)  
update user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.update_user.js)  
upgrade cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_admin.upgrade_cluster.js)  
restore from cloud s q l | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-alloydb/samples/generated/v1beta/alloy_d_b_c_s_q_l_admin.restore_from_cloud_s_q_l.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/alloydb@legacy-8` installs client libraries for versions compatible with Node.js 8.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
