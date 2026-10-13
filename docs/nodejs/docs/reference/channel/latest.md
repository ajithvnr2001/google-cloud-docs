---
url: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/
title: Cloud Channel API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:30.038980+00:00
---

# Cloud Channel API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Channel API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.2  3.6.0  3.2.1  3.0.0  2.5.1  2.4.1  2.2.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/channel.svg)](https://www.npmjs.org/package/@google-cloud/channel)

Cloud Channel API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/CHANGELOG.md).

  * [Cloud Channel API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/channel/latest)



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
  3. [Enable the Cloud Channel API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudchannel.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/channel
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
fetch report results | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_reports_service.fetch_report_results.js)  
list reports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_reports_service.list_reports.js)  
run report job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_reports_service.run_report_job.js)  
activate entitlement | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.activate_entitlement.js)  
cancel entitlement | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.cancel_entitlement.js)  
change offer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.change_offer.js)  
change parameters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.change_parameters.js)  
change renewal settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.change_renewal_settings.js)  
check cloud identity accounts exist | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.check_cloud_identity_accounts_exist.js)  
create channel partner link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.create_channel_partner_link.js)  
create channel partner repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.create_channel_partner_repricing_config.js)  
create customer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.create_customer.js)  
create customer repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.create_customer_repricing_config.js)  
create entitlement | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.create_entitlement.js)  
delete channel partner repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.delete_channel_partner_repricing_config.js)  
delete customer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.delete_customer.js)  
delete customer repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.delete_customer_repricing_config.js)  
get channel partner link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.get_channel_partner_link.js)  
get channel partner repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.get_channel_partner_repricing_config.js)  
get customer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.get_customer.js)  
get customer repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.get_customer_repricing_config.js)  
get entitlement | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.get_entitlement.js)  
import customer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.import_customer.js)  
list channel partner links | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_channel_partner_links.js)  
list channel partner repricing configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_channel_partner_repricing_configs.js)  
list customer repricing configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_customer_repricing_configs.js)  
list customers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_customers.js)  
list entitlement changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_entitlement_changes.js)  
list entitlements | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_entitlements.js)  
list offers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_offers.js)  
list products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_products.js)  
list purchasable offers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_purchasable_offers.js)  
list purchasable skus | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_purchasable_skus.js)  
list sku group billable skus | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_sku_group_billable_skus.js)  
list sku groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_sku_groups.js)  
list skus | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_skus.js)  
list subscribers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_subscribers.js)  
list transferable offers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_transferable_offers.js)  
list transferable skus | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.list_transferable_skus.js)  
lookup offer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.lookup_offer.js)  
provision cloud identity | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.provision_cloud_identity.js)  
query eligible billing accounts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.query_eligible_billing_accounts.js)  
register subscriber | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.register_subscriber.js)  
start paid service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.start_paid_service.js)  
suspend entitlement | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.suspend_entitlement.js)  
transfer entitlements | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.transfer_entitlements.js)  
transfer entitlements to google | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.transfer_entitlements_to_google.js)  
unregister subscriber | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.unregister_subscriber.js)  
update channel partner link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.update_channel_partner_link.js)  
update channel partner repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.update_channel_partner_repricing_config.js)  
update customer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.update_customer.js)  
update customer repricing config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-channel/samples/generated/v1/cloud_channel_service.update_customer_repricing_config.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/channel@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
