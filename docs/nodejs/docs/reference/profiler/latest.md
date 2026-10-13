---
url: https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:06.287985+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 5.0.3 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/)
  * [ 5.0.2 ](https://docs.cloud.google.com/nodejs/docs/reference/profiler/5.0.2/)
  * [ 4.1.5 ](https://docs.cloud.google.com/nodejs/docs/reference/profiler/4.1.5/)



# [Cloud Profiler: Node.js Client](https://github.com/googleapis/cloud-profiler-nodejs)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/profiler.svg)](https://www.npmjs.org/package/@google-cloud/profiler)

Adds support for Cloud Profiler to Node.js applications

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/cloud-profiler-nodejs/blob/main/CHANGELOG.md).

  * [Cloud Profiler Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/profiler/latest)
  * [Cloud Profiler Documentation](https://cloud.google.com/profiler)
  * [github.com/googleapis/cloud-profiler-nodejs](https://github.com/googleapis/cloud-profiler-nodejs)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Samples

  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable the Cloud Profiler API](https://console.cloud.google.com/flows/enableapi?apiid=cloudprofiler.googleapis.com).
  3. [Set up authentication with a service account](https://cloud.google.com/docs/authentication/getting-started) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/profiler
    

### Prerequisites

  1. Your application will need to be using Node.js 10.4.1 or greater or Node.js
  2. The profiler will not be enabled when using earlier versions of 10 because versions of Node.js 10 prior to 10.4.1 are impacted by [this](https://bugs.chromium.org/p/chromium/issues/detail?id=847863) issue, which can cause garbage collection to take several minutes when heap profiling is enabled.

  3. `@google-cloud/profiler` depends on the [`pprof`](https://www.npmjs.com/package/pprof) module, a module with a native component that is used to collect profiles with v8's CPU and Heap profilers. You may need to install additional dependencies to build the `pprof` module.

     * For Linux: `pprof` has prebuilt binaries available for Linux and Alpine Linux for Node 10 and 12. No additional dependencies are required.
     * For other environments: when using `@google-cloud/profiler` on environments that `pprof` does not have prebuilt binaries for, the module [`node-gyp`](https://www.npmjs.com/package/node-gyp) will be used to build binaries. See `node-gyp`'s [documentation](https://github.com/nodejs/node-gyp#installation) for information on dependencies required to build binaries with `node-gyp`.
  4. You will need a project in the [Google Developers Console][cloud-console]. Your application can run anywhere, but the profiler data is associated with a particular project.

  5. You will need to enable the Cloud Profiler API for your project.




### Basic Set-up

  1. Install `@google-cloud/profiler` with [`npm`](https://www.npmjs.com) or add to your [`package.json`](https://docs.npmjs.com/files/package.json#dependencies).
         
         # Install through npm while saving to the local 'package.json'
         npm install --save @google-cloud/profiler
         

  2. Include and start the profiler at the beginning of your application:
         
         require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)().catch((err) => {
         console.log(`Failed to start profiler: ${err}`);
         });
         

Some environments require a configuration to be passed to the `start()` function. For more details on this, see instructions for running outside of Google Cloud Platform, on App Engine flexible environment, on Google Compute Engine, and on Google Container Engine.

  3. If you are running your application locally, or on a machine where you are using the [Google Cloud SDK][gcloud-sdk], make sure to log in with the application default credentials:
         
         gcloud beta auth application-default login
         

Alternatively, you can set `GOOGLE_APPLICATION_CREDENTIALS`. For more details on this, see Running elsewhere




### Configuration

See [the default configuration](https://github.com/googleapis/cloud-profiler-nodejs/blob/master/src/config.ts) for a list of possible configuration options. These options can be passed to the agent through the object argument to the start command shown below:
    
    
    await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({disableTime: true});
    

Alternatively, you can provide the configuration through a config file. This can be useful if you want to load our module using `--require` on the command line (which requires and starts the agent) instead of editing your main script. The `GCLOUD_PROFILER_CONFIG` environment variable should point to your configuration file.
    
    
    export GCLOUD_PROFILER_CONFIG=./path/to/your/profiler/configuration.js
    

#### Changing log level

The profiler writes log statements to the console log for diagnostic purposes. By default, the log level is set to warn. You can adjust this by setting `logLevel` in the config. Setting `logLevel` to 0 will disable logging, 1 sets log level to error, 2 sets it to warn (default), 3 sets it to info, and 4 sets it to debug.

So, for example, to start the profiler with the log level at debug, you would do this:
    
    
    await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({logLevel: 4});
    

#### Disabling heap or time profile collection

By default, the profiler collects both heap profiles, which show memory allocations, and time profiles, which capture how much wall-clock time is spent in different locations of the code. Using the configuration, it is possible to disable the collection of either type of profile.

To disable time profile collection, set `disableTime` to true:
    
    
    await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({disableTime: true});
    

To disable heap profile collection, set `disableHeap` to true:
    
    
    await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({disableHeap: true});
    

### Running on Google Cloud Platform

There are three different services that can host Node.js applications within Google Cloud Platform: Google App Engine flexible environment, Google Compute Engine, and Google Container Engine. After installing `@google-cloud/profiler` in your project and ensuring that the environment you are using uses a supported version of Node.js, follow the service-specific instructions to enable the profiler.

#### Running on App Engine flexible environment

To enable the profiling agent for a Node.js program running in the App Engine flexible environment, import the agent at the top of your application’s main script or entry point by including the following code snippet:
    
    
    require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)();
    

You can specify which version of Node.js you're using by adding a snippet like the following to your `package.json`:
    
    
    "engines": {
        "node": ">=10.4.1"
    }
    

The above snippet will ensure that you're using 10.4.1 or greater.

Deploy your application to App Engine Flexible environment as usual.

#### Running on Google Compute Engine

To enable the profiling agent for a Node.js program running in the Google Compute Engine environment, import the agent at the top of your application’s main script or entry point by including the following code snippet:
    
    
    require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({
    serviceContext: {
        service: 'your-service',
        version: '1.0.0'
    }
    });
    

#### Running on Google Container Engine

To enable the profiling agent for a Node.js program running in the Google Container Engine environment, import the agent at the top of your application’s main script or entry point by including the following code snippet:
    
    
    require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({
    serviceContext: {
        service: 'your-service',
        version: '1.0.0'
    }
    });
    

#### Running on Istio

On Istio, the GCP Metadata server may not be available for a few seconds after your application has started. When this occurs, the profiling agent may fail to start because it cannot initialize required fields. One can retry when starting the profiler with the following snippet.
    
    
    const profiler = require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)');
    async function startProfiler() {
    for (let i = 0; i < 3; i++) {
        try {
        await profiler.[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({
            serviceContext: {
            service: 'your-service',
            version: '1.0.0',
            },
        });
        } catch(e) {
        console.log(`Failed to start profiler: ${e}`);
        }
    
        // Wait for 1 second before trying again.
        await new Promise(r => setTimeout(r, 1000));
    }
    }
    startProfiler();
    

### Running elsewhere

You can still use `@google-cloud/profiler` if your application is running outside of Google Cloud Platform, for example, running locally, on-premise, or on another cloud provider.

  1. You will need to specify your project id and the service you want the collected profiles to be associated with, and (optionally) the version of the service when starting the profiler:


    
    
        await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({
        projectId: 'project-id',
        serviceContext: {
            service: 'your-service',
            version: '1.0.0'
        }
        });
    

  1. You will need to provide credential for your application.


  * If you are running your application on a development machine or test environment where you are using the [`gcloud` command line tools][gcloud-sdk], and are logged using `gcloud beta auth application-default login`, you already have sufficient credentials, and a service account key is not required.

  * You can provide credentials via [Application Default Credentials][app-default-credentials]. This is the recommended method.

    1. [Create a new JSON service account key][service-account].
    2. Copy the key somewhere your application can access it. Be sure not to expose the key publicly.
    3. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the full path to the key. The profiler will automatically look for this environment variable.
  * You may set the `keyFilename` or `credentials` configuration field to the full path or contents to the key file, respectively. Setting either of these fields will override either setting `GOOGLE_APPLICATION_CREDENTIALS` or logging in using `gcloud`.

This is how you would set `keyFilename`:
        
        await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({
            projectId: 'project-id',
            serviceContext: {
            service: 'your-service',
            version: '1.0.0'
            },
            keyFilename: '/path/to/keyfile'
        });
        

This is how you would set `credentials`:
        
        await require('[@google-cloud/profiler](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/profiler/latest/overview.html)({
            projectId: 'project-id',
            serviceContext: {
            service: 'your-service',
            version: '1.0.0'
            },
            credentials: {
            client_email: 'email',
            private_key: 'private_key'
            }
        });
        




## Samples

Samples are in the [`samples/`](https://github.com/googleapis/cloud-profiler-nodejs/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
App | [source code](https://github.com/googleapis/cloud-profiler-nodejs/blob/main/samples/app.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/cloud-profiler-nodejs&page=editor&open_in_editor=samples/app.js,samples/README.md)  
Snippets | [source code](https://github.com/googleapis/cloud-profiler-nodejs/blob/main/samples/snippets.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/cloud-profiler-nodejs&page=editor&open_in_editor=samples/snippets.js,samples/README.md)  
  
The [Cloud Profiler Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/profiler/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://nodejs.org/en/about/releases/). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/profiler@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/cloud-profiler-nodejs/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/cloud-profiler-nodejs/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
