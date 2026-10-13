---
url: https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/
title: Developer Connect API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:42.136154+00:00
---

# Developer Connect API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Developer Connect API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.5.0  0.3.1  0.2.0  0.1.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/developerconnect.svg)](https://www.npmjs.org/package/@google-cloud/developerconnect)

Developer Connect API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/CHANGELOG.md).

  * [Developer Connect API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/developerconnect/latest)
  * [Developer Connect API Documentation](https://cloud.google.com/developer-connect/docs/overview)



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
  3. [Enable the Developer Connect API API](https://console.cloud.google.com/flows/enableapi?apiid=developerconnect.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/developerconnect
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create account connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.create_account_connector.js)  
create connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.create_connection.js)  
create git repository link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.create_git_repository_link.js)  
delete account connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.delete_account_connector.js)  
delete connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.delete_connection.js)  
delete git repository link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.delete_git_repository_link.js)  
delete self | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.delete_self.js)  
delete user | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.delete_user.js)  
fetch access token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_access_token.js)  
fetch git hub installations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_git_hub_installations.js)  
fetch git refs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_git_refs.js)  
fetch linkable git repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_linkable_git_repositories.js)  
fetch read token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_read_token.js)  
fetch read write token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_read_write_token.js)  
fetch self | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.fetch_self.js)  
finish o auth | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.finish_o_auth.js)  
get account connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.get_account_connector.js)  
get connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.get_connection.js)  
get git repository link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.get_git_repository_link.js)  
list account connectors | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.list_account_connectors.js)  
list connections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.list_connections.js)  
list git repository links | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.list_git_repository_links.js)  
list users | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.list_users.js)  
start o auth | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.start_o_auth.js)  
update account connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.update_account_connector.js)  
update connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/developer_connect.update_connection.js)  
create insights config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.create_insights_config.js)  
delete insights config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.delete_insights_config.js)  
get deployment event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.get_deployment_event.js)  
get insights config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.get_insights_config.js)  
list deployment events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.list_deployment_events.js)  
list insights configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.list_insights_configs.js)  
update insights config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-developerconnect/samples/generated/v1/insights_config_service.update_insights_config.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/developerconnect@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
