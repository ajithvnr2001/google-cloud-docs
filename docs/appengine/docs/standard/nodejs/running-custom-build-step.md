---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/running-custom-build-step/
title: Running a custom build step \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:24.358287+00:00
---

# Running a custom build step  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/running-custom-build-step/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Running a custom build step Stay organized with collections  Save and categorize content based on your preferences. 

By default, the node.js runtime will execute `npm run build` if a `build` script is detected in `package.json` file. If you require additional control over your build steps before starting your application, you can provide a custom build step. Custom build steps can be executed by adding `gcp-build` in your `package.json` file.

To prevent your build from running the `npm run build` script, you must either:

  * Add a `gcp-build` script with an empty value in your `package.json` file: `"gcp-build":""`. For details about configuring the `package.json`, see [Node.js buildpacks configurations](https://docs.cloud.google.com/appengine/docs/standard/nodejs/running-custom-build-step#example). 
  * Add the [`GOOGLE_NODE_RUN_SCRIPTS`](https://docs.cloud.google.com/docs/buildpacks/nodejs#google_node_run_scripts) build environment variable with an empty value in your `app.yaml` file.
        
        build_env_variables:
          GOOGLE_NODE_RUN_SCRIPTS: ''
        


For details about specifying build environment variables see [`build_env_variables`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#runtime_and_app_elements) section in the `app.yaml` file. 

When this script is executed, the dependencies in the `dependencies` and `devDependencies` fields of your `package.json` file are available. After executing your custom build step, App Engine removes and regenerates the `node_modules` folder by only installing the production dependencies declared in the `dependencies` field of your `package.json` file.

For more information on how to configure the runtime for custom build steps, see [Executing custom build steps during deployment](https://docs.cloud.google.com/docs/buildpacks/nodejs#executing_custom_build_steps_during_deployment) for Node.js buildpacks.

## Example

A custom build script can be used for pre-processing tasks, such as pre-processing CSS, minifying client side JavaScript, or running tools, such as `webpack` or `gulp`.

For example, to compile TypeScript to JavaScript, your `package.json` file might look like the following. Note the `gcp-build` script:
    
    
    {
      "name": "appengine-typescript",
      "description": "An example TypeScript app running on Google App Engine.",
      "version": "0.0.1",
      "private": true,
      "license": "Apache Version 2.0",
      "author": "Google Inc.",
      "engines": {
        "node": ">=20.0.0"
      },
      "scripts": {
        "prepare": "npm run gcp-build",
        "pretest": "npm run gcp-build",
        "test": "c8 mocha -p -j 2 test/*.test.js --exit",
        "lint": "gts lint",
        "start": "node ./index.js",
        "deploy": "gcloud app deploy",
    ** "clean": "gts clean",**
        "compile": "tsc -p .",
        "fix": "gts fix",
        "build": "tsc -p .",
        "gcp-build": "tsc -p ."
      },
      "dependencies": {
        "@typescript-eslint/parser": "^8.0.0",
        "express": "^5.0.0"
      },
      "devDependencies": {
        "@types/express": "^5.0.0",
        "@types/node": "^20.0.0",
        "c8": "^12.0.0",
        "chai": "^6.0.0",
        "gts": "^5.0.0",
        "mocha": "^10.2.0",
        "typescript": "^5.0.0",
        "wait-port": "^1.0.0"
      }
    }

## Serving static files

When you generate or copy files during the custom build step, App Engine does not serve these static files directly from your app using either the [`static_dir`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_dir) or [`static_files`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_files) elements defined in the `app.yaml` file. Instead, App Engine uploads the static files to the serving infrastructure in the standard environment before running the custom build step. Any request to the files generated or copied during the custom build step results in a `404 NOT FOUND` HTTP error.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
