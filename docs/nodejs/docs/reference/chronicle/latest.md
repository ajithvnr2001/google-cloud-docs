---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/
title: Chronicle API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:29.931463+00:00
---

# Chronicle API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Chronicle API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/chronicle.svg)](https://www.npmjs.org/package/@google-cloud/chronicle)

Chronicle API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/CHANGELOG.md).

  * [Chronicle API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/chronicle/latest)
  * [Chronicle API Documentation](https://cloud.google.com/chronicle/docs/secops/secops-overview)



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
  3. [Enable the Chronicle API API](https://console.cloud.google.com/flows/enableapi?apiid=chronicle.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/chronicle
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
get big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/big_query_export_service.get_big_query_export.js)  
provision big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/big_query_export_service.provision_big_query_export.js)  
update big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/big_query_export_service.update_big_query_export.js)  
batch get dashboard charts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/dashboard_chart_service.batch_get_dashboard_charts.js)  
get dashboard chart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/dashboard_chart_service.get_dashboard_chart.js)  
execute dashboard query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/dashboard_query_service.execute_dashboard_query.js)  
get dashboard query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/dashboard_query_service.get_dashboard_query.js)  
create data access label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.create_data_access_label.js)  
create data access scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.create_data_access_scope.js)  
delete data access label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.delete_data_access_label.js)  
delete data access scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.delete_data_access_scope.js)  
get data access label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.get_data_access_label.js)  
get data access scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.get_data_access_scope.js)  
list data access labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.list_data_access_labels.js)  
list data access scopes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.list_data_access_scopes.js)  
update data access label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.update_data_access_label.js)  
update data access scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_access_control_service.update_data_access_scope.js)  
bulk create data table rows | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.bulk_create_data_table_rows.js)  
bulk get data table rows | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.bulk_get_data_table_rows.js)  
bulk replace data table rows | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.bulk_replace_data_table_rows.js)  
bulk update data table rows | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.bulk_update_data_table_rows.js)  
create data table | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.create_data_table.js)  
create data table row | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.create_data_table_row.js)  
delete data table | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.delete_data_table.js)  
delete data table row | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.delete_data_table_row.js)  
get data table | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.get_data_table.js)  
get data table operation errors | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.get_data_table_operation_errors.js)  
get data table row | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.get_data_table_row.js)  
list data table rows | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.list_data_table_rows.js)  
list data tables | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.list_data_tables.js)  
update data table | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.update_data_table.js)  
update data table row | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/data_table_service.update_data_table_row.js)  
create watchlist | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/entity_service.create_watchlist.js)  
delete watchlist | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/entity_service.delete_watchlist.js)  
get watchlist | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/entity_service.get_watchlist.js)  
list watchlists | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/entity_service.list_watchlists.js)  
update watchlist | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/entity_service.update_watchlist.js)  
get featured content native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/featured_content_native_dashboard_service.get_featured_content_native_dashboard.js)  
install featured content native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/featured_content_native_dashboard_service.install_featured_content_native_dashboard.js)  
list featured content native dashboards | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/featured_content_native_dashboard_service.list_featured_content_native_dashboards.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/instance_service.get_instance.js)  
add chart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.add_chart.js)  
create native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.create_native_dashboard.js)  
delete native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.delete_native_dashboard.js)  
duplicate chart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.duplicate_chart.js)  
duplicate native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.duplicate_native_dashboard.js)  
edit chart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.edit_chart.js)  
export native dashboards | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.export_native_dashboards.js)  
get native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.get_native_dashboard.js)  
import native dashboards | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.import_native_dashboards.js)  
list native dashboards | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.list_native_dashboards.js)  
remove chart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.remove_chart.js)  
update native dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/native_dashboard_service.update_native_dashboard.js)  
create reference list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/reference_list_service.create_reference_list.js)  
get reference list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/reference_list_service.get_reference_list.js)  
list reference lists | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/reference_list_service.list_reference_lists.js)  
update reference list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/reference_list_service.update_reference_list.js)  
create retrohunt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.create_retrohunt.js)  
create rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.create_rule.js)  
delete rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.delete_rule.js)  
get retrohunt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.get_retrohunt.js)  
get rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.get_rule.js)  
get rule deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.get_rule_deployment.js)  
list retrohunts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.list_retrohunts.js)  
list rule deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.list_rule_deployments.js)  
list rule revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.list_rule_revisions.js)  
list rules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.list_rules.js)  
update rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.update_rule.js)  
update rule deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-chronicle/samples/generated/v1/rule_service.update_rule_deployment.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/chronicle@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
