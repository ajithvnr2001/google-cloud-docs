---
url: https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime/
title: The Node.js runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:03.376201+00:00
---

# The Node.js runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Node.js runtime Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [Node.js runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime#newversions) to use the latest version of Node.js. 

The Node.js runtime is the software stack responsible for installing your application code and dependencies, and then running that application in the flexible environment.

## Node.js versions

Node.js 26 (preview) uses [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview). The default Node.js engine uses the [latest LTS release](https://nodejs.org/en/blog/release/). For the full list of supported Node.js versions, and their corresponding Ubuntu version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs).

To use a [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs) Node.js version, you must:

  * Install `gcloud CLI` version **420.0.0 or later**. You can update your CLI tooling by running the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update)command. To view your installed version, run the [`gcloud version`](https://docs.cloud.google.com/sdk/gcloud/reference/version) command.

  * Include the `runtime_config` and `operating_system` settings in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) file to specify an operating system.

  * Optionally, specify a version by:

    * Adding the `runtime_version` setting in your `app.yaml` file. By default, the latest Node.js version is used if the `runtime_version` setting isn't specified. For example:

      * To specify Node.js 26 (preview) on Ubuntu 24:
            
            runtime: nodejs
              env: flex
            
              runtime_config:
                  operating_system: "ubuntu24"
                  runtime_version: "26"
            

      * To specify the latest supported Node.js version on Ubuntu 24:
            
            runtime: nodejs
              env: flex
            
              runtime_config:
                  operating_system: "ubuntu24"
            

The `runtime_version` setting supports semver.

    * Including the latest supported Node.js version in your application's [`package.json`](https://docs.npmjs.com/files/package.json) file using the [`engines`](https://docs.npmjs.com/files/package.json#engines) field. When you use the `engines` field to specify a version, the `runtime_version` setting takes precedence. To prevent unexpected breakages, we recommend that you specify a Node.js version in the [`engines`](https://docs.npmjs.com/files/package.json#engines) field, along with the `runtime_version`. For example:
          
          {
              "engines": {
                "node": "26.x"
              }
            }
          

The `engines.node` property can be a [semver range](https://www.npmjs.com/package/semver#ranges). If you specify this property, the runtime downloads and installs the latest version of Node.js that matches the semver range. If no match is found, the application fails to deploy and the runtime returns an error.




### Previous runtime versions

**Warning:** Node.js **version 16 and earlier** have reached end of support. App Engine blocks you from deploying your applications using runtimes that have reached end of support. We recommend that you migrate your app to use a [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs) of Node.js or use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes).

For Node.js runtime **version 16 and earlier** , specify a version in your application's [`package.json`](https://docs.npmjs.com/files/package.json) file using the [`engines`](https://docs.npmjs.com/files/package.json#engines) field.

The following example configures the runtime to use the Node 9 release:
    
    
    {
      "engines": {
        "node": "9.x"
      }
    }
    

The `engines.node` property can be a [semver range](https://www.npmjs.com/package/semver#ranges). If you specify this property, the runtime downloads and installs the latest version of Node.js that matches the semver range. If no match is found, the application fails to deploy and the runtime returns an error message.

### Support for other Node.js runtimes

If you need to use a Node.js version that isn't [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs), you can create a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) and select a valid base image with the Node.js version you need.

For Google-supplied base images or [Docker Node.js base images](https://hub.docker.com/_/node), see [Building custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base).

## Package manager

During deployment, the runtime uses either the [npm](https://docs.npmjs.com/about-npm), or [yarn](https://yarnpkg.com/), or [Pnpm](https://pnpm.io/installation) package manager to install dependencies and start the application. The package manager is set with the following logic:

  * The default package manager is `npm`.
  * If a `yarn.lock` file is present in your application's root directory, the runtime instead uses the `yarn` package manager.
  * For only Node.js version 18 and later, if a `pnpm-lock.yaml` file is present in your application's root directory, the runtime instead uses the `Pnpm` package manager.
  * If both a `package-lock.json`, and `yarn.lock` or `pnpm-lock.yaml` exist, your deployment will fail with an error. If you need the `package-lock.json` file, you must specify the other package manager files in the [`skip_files` section of your `app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) file to resolve which package manager to use.



### Package manager version

The runtime image aims to use the latest `yarn` release and the release of `npm` that is available in the [latest Node.js LTS release](https://nodejs.org/en/blog/release/).

You can specify a different package manager version to use in your application's [`package.json`](https://docs.npmjs.com/files/package.json) file by using the [`engines`](https://docs.npmjs.com/files/package.json#engines) field. In this case, the runtime ensures that the package manager used for the deployment has a version that matches the specification listed in the [`engines`](https://docs.npmjs.com/files/package.json#engines) field.

If both a `yarn` and `npm` version specification is given, only the package manager that is used for the deployment will be updated if needed. This saves deployment time by not installing a custom version of a package manager if it is not actually being used to deploy your application.

The following example configures the runtime to use a custom version of `npm`:
    
    
    {
      "engines": {
        "npm": "5.x"
      }
    }
    

The next example configures the runtime to use a custom version of `yarn`:
    
    
    {
      "engines": {
        "yarn": ">=1.0.0 <2.0.0"
      }
    }
    

The `engines.npm` and `engines.yarn` properties can both be a [semver range](https://www.npmjs.com/package/semver#ranges).

## Dependencies

During deployment, the runtime will use either the [npm](https://docs.npmjs.com/about-npm) or [yarn](https://yarnpkg.com/) package manager to install dependencies by running `npm install` or `yarn install`. See the Package Manager section for more information on how the runtime selects the package manager to use.

Also, for more information about managing Node.js packages on Google App Engine, see [Using Node.js Libraries](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/specifying-dependencies).

To enable the use of Node.js packages that require native extensions, the following [Ubuntu packages](https://packages.ubuntu.com/) are pre-installed in the [Docker image](https://github.com/GoogleCloudPlatform/nodejs-docker).

  * `build-essential`
  * `ca-certificates`
  * `curl`
  * `git`
  * `imagemagick`
  * `libkrb5-dev`
  * `netbase`
  * `python`



If your application requires additional operating-system-level dependencies, you will need to use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) based on this runtime to install the appropriate packages.

## NPM build script

For Node.js runtime **version 18 and later** , the runtime environment executes `npm run build` if a `build` script is detected in `package.json` by default. If you require additional control over your build steps before starting your application, you can provide a [custom build step](https://docs.cloud.google.com/docs/buildpacks/nodejs#executing_custom_build_steps_during_deployment) by adding a `gcp-build` script to your `package.json` file.

To prevent your build from running the `npm run build` script, you must either:

  * Add a `gcp-build` script with an empty value in your `package.json` file: `"gcp-build":""`. 
  * Add the [`GOOGLE_NODE_RUN_SCRIPTS`](https://docs.cloud.google.com/docs/buildpacks/nodejs#google_node_run_scripts) build environment variable with an empty value in your `app.yaml` file.
        
        build_env_variables:
          GOOGLE_NODE_RUN_SCRIPTS: ''
        


For details about specifying build environment variables see [`build_env_variables`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) section in the `app.yaml` file. 

## Application startup

The runtime starts your application by using [`npm start`](https://docs.npmjs.com/cli/start), which uses the command specified in [`package.json`](https://docs.npmjs.com/files/package.json#scripts). For example:
    
    
    "scripts": {
      "start": "node app.js"
    }
    

Your start script should start a web server that responds to HTTP requests on the port specified by the `PORT` environment variable, typically 8080.

## Extending the runtime

You can use [custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) to add additional functionality to a Node.js app running in the App Engine flexible environment. To configure a custom runtime, replace the following line in your [`app.yaml` file](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml):
    
    
    runtime: nodejs
    

with this line:
    
    
    runtime: custom
    

You must also add `Dockerfile` and `.dockerignore` files in the same directory that contains the `app.yaml` file.

Visit the [Custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) documentation to learn how to define a Dockerfile in a custom runtime.

## HTTPS and forwarding proxies

App Engine terminates the HTTPS connection at the load balancer and forwards the request to your application. Some applications need to determine the original request IP and protocol. The user's IP address is available in the standard `X-Forwarded-For` header. Applications that require this information should configure their web framework to trust the proxy.

With [Express.js](http://expressjs.com/guide/behind-proxies.html), use the `trust proxy` setting:
    
    
    app.set('trust proxy', true);
    

For information on enforcing HTTPS connections, see [How Requests are Handled](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-handled#forcing_https_connections).

## Environment variables

The following environment variables are set by the runtime environment:

Environment variable | Description  
---|---  
`GAE_INSTANCE` | The name of the current instance.  
`GAE_MEMORY_MB` | The amount of memory available to the application process.  
`GAE_SERVICE` |  The service name specified in your application's `app.yaml` file, or if no service name is specified, it is set to `default`.   
`GAE_VERSION` | The version label of the current application.  
`GOOGLE_CLOUD_PROJECT` | The Project ID associated with your application, which is visible in the Google Cloud console  
`NODE_ENV` | When your app is deployed, the value is `production`.  
`PORT` |  The port that will receive HTTP requests. Set to `8080`.   
  
You can set additional environment variables with [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#defining_environment_variables).

## Metadata server

Each instance of your application can use the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to query information about the instance, including its hostname, external IP address, instance ID, custom metadata, and service account information. App Engine does not allow you to set custom metadata for each instance, but you can set [project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide) and read it from your App Engine and Compute Engine instances.

This example function uses the metadata server to get the external IP address of the instance.
    
    
    import express from 'express';
    import fetch from 'node-fetch';
    
    const app = express();
    app.enable('trust proxy');
    
    const METADATA_NETWORK_INTERFACE_URL =
      'http://metadata/computeMetadata/v1/' +
      '/instance/network-interfaces/0/access-configs/0/external-ip';
    
    const getExternalIp = async () => {
      const options = {
        headers: {
          'Metadata-Flavor': 'Google',
        },
        json: true,
      };
    
      try {
        const response = await fetch(METADATA_NETWORK_INTERFACE_URL, options);
        const ip = await response.json();
        return ip;
      } catch (err) {
        console.log('Error while talking to metadata server, assuming localhost');
        return 'localhost';
      }
    };
    
    app.get('/', async (req, res, next) => {
      try {
        const externalIp = await getExternalIp();
        res.status(200).send(`External IP: ${externalIp}`).end();
      } catch (err) {
        next(err);
      }
    });
    
    const PORT = parseInt(process.env.PORT) || 8080;
    app.listen(PORT, () => {
      console.log(`App listening on port ${PORT}`);
      console.log('Press Ctrl+C to quit.');
    });

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
