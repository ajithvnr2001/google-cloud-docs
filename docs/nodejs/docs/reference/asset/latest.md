---
url: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/
title: Cloud Asset API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:01.574308+00:00
---

# Cloud Asset API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Asset API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.3.3  5.5.0  5.3.0  5.2.0  5.1.0  5.0.1  4.6.3  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  3.23.1  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.1  3.15.5  3.14.1  3.13.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/asset.svg)](https://www.npmjs.org/package/@google-cloud/asset)

Cloud Asset API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/CHANGELOG.md).

  * [Cloud Asset API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/asset/latest)



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
  3. [Enable the Cloud Asset API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudasset.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/asset
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
analyze iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.analyze_iam_policy.js)  
analyze iam policy longrunning | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.analyze_iam_policy_longrunning.js)  
analyze move | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.analyze_move.js)  
analyze org policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.analyze_org_policies.js)  
analyze org policy governed assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.analyze_org_policy_governed_assets.js)  
analyze org policy governed containers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.analyze_org_policy_governed_containers.js)  
batch get assets history | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.batch_get_assets_history.js)  
batch get effective iam policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.batch_get_effective_iam_policies.js)  
create feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.create_feed.js)  
create saved query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.create_saved_query.js)  
delete feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.delete_feed.js)  
delete saved query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.delete_saved_query.js)  
export assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.export_assets.js)  
get feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.get_feed.js)  
get saved query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.get_saved_query.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.list_assets.js)  
list feeds | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.list_feeds.js)  
list saved queries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.list_saved_queries.js)  
query assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.query_assets.js)  
search all iam policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.search_all_iam_policies.js)  
search all resources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.search_all_resources.js)  
update feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.update_feed.js)  
update saved query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1/asset_service.update_saved_query.js)  
search all iam policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p1beta1/asset_service.search_all_iam_policies.js)  
search all resources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p1beta1/asset_service.search_all_resources.js)  
create feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p2beta1/asset_service.create_feed.js)  
delete feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p2beta1/asset_service.delete_feed.js)  
get feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p2beta1/asset_service.get_feed.js)  
list feeds | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p2beta1/asset_service.list_feeds.js)  
update feed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p2beta1/asset_service.update_feed.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p5beta1/asset_service.list_assets.js)  
export assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-asset/samples/generated/v1p7beta1/asset_service.export_assets.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/asset@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
