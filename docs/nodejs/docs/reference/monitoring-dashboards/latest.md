---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/
title: Monitoring Dashboards: Node.js Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:18.924507+00:00
---

# Monitoring Dashboards: Node.js Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Monitoring Dashboards: Node.js Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.2.0  2.9.2  2.8.0  2.6.1  2.5.1  2.4.2  2.3.4 

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/monitoring-dashboards.svg)](https://www.npmjs.org/package/@google-cloud/monitoring-dashboards)

interact with dashboards for viewing and analyzing metric data

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-monitoring-dashboard/CHANGELOG.md).

  * [Monitoring Dashboards Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest)
  * [Monitoring Dashboards Documentation](https://cloud.google.com/monitoring/docs)
  * [github.com/googleapis/google-cloud-node/packages/google-monitoring-dashboard](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-monitoring-dashboard)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart
    * Before you begin
    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Monitoring Dashboards API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/monitoring-dashboards
    

### Using the client library
    
    
    // Imports the Google Cloud client library
    const {
      DashboardsServiceClient,
    } = require('[@google-cloud/monitoring-dashboards](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)');
    
    // Creates a client
    const ds = new [DashboardsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)();
    
    // parent = 'projects/my-project', // Project to list dashboards for.
    
    async function listDashboards() {
      const [dashboards] = await ds.listDashboards({
        parent,
      });
      console.info('Listing Dashboards:');
      for (const dashboard of dashboards) {
        console.info(`\t${dashboard.displayName}`);
      }
    }
    listDashboards();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-monitoring-dashboard/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Dashboards_service.create_dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.create_dashboard.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.create_dashboard.js,packages/google-monitoring-dashboard/samples/README.md)  
Dashboards_service.delete_dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.delete_dashboard.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.delete_dashboard.js,packages/google-monitoring-dashboard/samples/README.md)  
Dashboards_service.get_dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.get_dashboard.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.get_dashboard.js,packages/google-monitoring-dashboard/samples/README.md)  
Dashboards_service.list_dashboards | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.list_dashboards.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.list_dashboards.js,packages/google-monitoring-dashboard/samples/README.md)  
Dashboards_service.update_dashboard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.update_dashboard.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-monitoring-dashboard/samples/generated/v1/dashboards_service.update_dashboard.js,packages/google-monitoring-dashboard/samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-monitoring-dashboard/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-monitoring-dashboard/samples/quickstart.js,packages/google-monitoring-dashboard/samples/README.md)  
  
The [Monitoring Dashboards Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/monitoring-dashboards@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
