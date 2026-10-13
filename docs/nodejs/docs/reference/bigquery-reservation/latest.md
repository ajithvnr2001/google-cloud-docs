---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/
title: BigQuery Reservation API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:27.351894+00:00
---

# BigQuery Reservation API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  BigQuery Reservation API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.3.1 (latest)  5.2.0  4.4.0  3.5.0  3.4.0  2.2.1  2.1.1  2.0.4  1.4.0  1.3.0  1.2.0  1.1.6 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/bigquery-reservation.svg)](https://www.npmjs.org/package/@google-cloud/bigquery-reservation)

BigQuery Reservation API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/CHANGELOG.md).

  * [BigQuery Reservation API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/reservation/latest)



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
  3. [Enable the BigQuery Reservation API API](https://console.cloud.google.com/flows/enableapi?apiid=bigqueryreservation.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/bigquery-reservation
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.create_assignment.js)  
create capacity commitment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.create_capacity_commitment.js)  
create reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.create_reservation.js)  
create reservation group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.create_reservation_group.js)  
delete assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.delete_assignment.js)  
delete capacity commitment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.delete_capacity_commitment.js)  
delete reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.delete_reservation.js)  
delete reservation group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.delete_reservation_group.js)  
failover reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.failover_reservation.js)  
get bi reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.get_bi_reservation.js)  
get capacity commitment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.get_capacity_commitment.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.get_iam_policy.js)  
get reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.get_reservation.js)  
get reservation group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.get_reservation_group.js)  
list assignments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.list_assignments.js)  
list capacity commitments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.list_capacity_commitments.js)  
list reservation groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.list_reservation_groups.js)  
list reservations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.list_reservations.js)  
merge capacity commitments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.merge_capacity_commitments.js)  
move assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.move_assignment.js)  
search all assignments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.search_all_assignments.js)  
search assignments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.search_assignments.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.set_iam_policy.js)  
split capacity commitment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.split_capacity_commitment.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.test_iam_permissions.js)  
update assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.update_assignment.js)  
update bi reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.update_bi_reservation.js)  
update capacity commitment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.update_capacity_commitment.js)  
update reservation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-bigquery-reservation/samples/generated/v1/reservation_service.update_reservation.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/bigquery-reservation@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
