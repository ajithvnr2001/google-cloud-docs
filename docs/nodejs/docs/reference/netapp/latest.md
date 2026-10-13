---
url: https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/
title: NetApp API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:19.467574+00:00
---

# NetApp API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  NetApp API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.15.0  0.12.0  0.8.0  0.7.0  0.6.0  0.2.1 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/netapp.svg)](https://www.npmjs.org/package/@google-cloud/netapp)

NetApp API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/CHANGELOG.md).

  * [NetApp API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/netapp/latest)
  * [NetApp API Documentation](https://cloud.google.com/netapp/volumes/docs/discover/overview)



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
  3. [Enable the NetApp API API](https://console.cloud.google.com/flows/enableapi?apiid=netapp.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/netapp
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create active directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_active_directory.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_backup.js)  
create backup policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_backup_policy.js)  
create backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_backup_vault.js)  
create host group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_host_group.js)  
create kms config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_kms_config.js)  
create quota rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_quota_rule.js)  
create replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_replication.js)  
create snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_snapshot.js)  
create storage pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_storage_pool.js)  
create volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.create_volume.js)  
delete active directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_active_directory.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_backup.js)  
delete backup policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_backup_policy.js)  
delete backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_backup_vault.js)  
delete host group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_host_group.js)  
delete kms config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_kms_config.js)  
delete quota rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_quota_rule.js)  
delete replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_replication.js)  
delete snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_snapshot.js)  
delete storage pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_storage_pool.js)  
delete volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.delete_volume.js)  
encrypt volumes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.encrypt_volumes.js)  
establish peering | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.establish_peering.js)  
establish volume peering | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.establish_volume_peering.js)  
execute ontap delete | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.execute_ontap_delete.js)  
execute ontap get | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.execute_ontap_get.js)  
execute ontap patch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.execute_ontap_patch.js)  
execute ontap post | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.execute_ontap_post.js)  
get active directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_active_directory.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_backup.js)  
get backup policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_backup_policy.js)  
get backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_backup_vault.js)  
get host group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_host_group.js)  
get kms config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_kms_config.js)  
get quota rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_quota_rule.js)  
get replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_replication.js)  
get snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_snapshot.js)  
get storage pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_storage_pool.js)  
get volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.get_volume.js)  
list active directories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_active_directories.js)  
list backup policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_backup_policies.js)  
list backup vaults | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_backup_vaults.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_backups.js)  
list host groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_host_groups.js)  
list kms configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_kms_configs.js)  
list quota rules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_quota_rules.js)  
list replications | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_replications.js)  
list snapshots | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_snapshots.js)  
list storage pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_storage_pools.js)  
list volumes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.list_volumes.js)  
restore backup files | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.restore_backup_files.js)  
resume replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.resume_replication.js)  
reverse replication direction | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.reverse_replication_direction.js)  
revert volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.revert_volume.js)  
stop replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.stop_replication.js)  
switch active replica zone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.switch_active_replica_zone.js)  
sync replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.sync_replication.js)  
update active directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_active_directory.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_backup.js)  
update backup policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_backup_policy.js)  
update backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_backup_vault.js)  
update host group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_host_group.js)  
update kms config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_kms_config.js)  
update quota rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_quota_rule.js)  
update replication | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_replication.js)  
update snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_snapshot.js)  
update storage pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_storage_pool.js)  
update volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.update_volume.js)  
validate directory service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.validate_directory_service.js)  
verify kms config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-netapp/samples/generated/v1/net_app.verify_kms_config.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/netapp@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
