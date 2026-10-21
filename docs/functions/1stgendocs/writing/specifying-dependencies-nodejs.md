---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-nodejs/
title: Specify dependencies in Node.js \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:28.499644+00:00
---

# Specify dependencies in Node.js  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-nodejs/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Specify dependencies in Node.js

A function is allowed to use external Node.js modules as well as local data. Dependencies in Node.js are managed with [npm](https://docs.npmjs.com/) and expressed in a metadata file called [`package.json`](https://docs.npmjs.com/files/package.json). The Cloud Run functions Node.js runtimes support installing using [npm](https://docs.npmjs.com/), [yarn](https://yarnpkg.com/en/), or [pnpm](https://pnpm.io/).

To specify a dependency for your function, add it to your `package.json` file.

**Note:** If a `package-lock.json`, `yarn.lock`, or `pnpm-lock.yaml` file is found within your project, that lock file will be respected when dependencies are installed using `npm ci`, `yarn install` or `pnpm install`.

In this example, a dependency is listed in the `package.json` file:
    
    
    {
      "dependencies": {
        "escape-html": "^1.0.3"
      }
    }

The dependency is then imported in the function:
    
    
    const functions = require('@google-cloud/functions-framework');
    const escapeHtml = require('escape-html');
    
    /**
     * Responds to an HTTP request using data from the request body parsed according
     * to the "content-type" header.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('helloHttp', (req, res) => {
      const name =
        (req.query && req.query.name) || (req.body && req.body.name) || 'World';
    
      res.send(`Hello ${escapeHtml(name)}!`);
    });

The [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework) is a required dependency for all functions. Although Cloud Run functions installs it on your behalf when the function is created, we recommend that you include it as an explicit dependency for clarity.

If your function relies on private dependencies, we recommend that you mirror `functions-framework` to your private registry. Include the mirrored `functions-framework` as a dependency to your function to avoid installing the package from the public internet.

## Using `npm` to install Node.js modules locally

The easiest way to install a Node.js module locally is to use the `npm install` command in the folder containing your function. For instance, the following command adds the `uuid` module:
    
    
    npm install uuid
    

This combines two steps:

  1. It marks the latest version of the module as a dependency in your `package.json` file. This is very important: Cloud Run functions only installs modules that are declared in your `package.json` file.
  2. It downloads the module into your `node_modules` directory. This lets you use the module when developing locally.



If you don't have npm installed on your machine, [get npm](https://www.npmjs.com/get-npm).

**Note:** npm packages are available for a variety of Google Cloud products. See the list [here](https://github.com/googleapis/google-cloud-node#google-cloud-nodejs-client-libraries).

## Configuring deployment dependencies

You can install production dependencies for NPM, Yarn, or Pnpm:

### NPM

When you deploy your function, Cloud Run functions installs dependencies declared in the `package.json` file using the [`npm install`](https://docs.npmjs.com/cli/install) command:
    
    
    npm install --production
    

### Yarn

In the Node.js 8 runtime and higher, if a `yarn.lock` file exists, Cloud Run functions instead uses the [`yarn install`](https://yarnpkg.com/lang/en/docs/cli/install/) command:
    
    
    yarn install --production
    

### Pnpm

In the Node.js 8 runtime and higher, if a `pnpm-lock.yaml` file exists, Cloud Run functions instead uses the [`pnpm install`](https://pnpm.io/next/cli/install) command:
    
    
    pnpm install
    

**Note:** Dependencies declared in subdirectories are not installed. If you are using a monorepo, you may want to execute a custom build script during deployment to install those dependencies.

### Executing custom build steps during deployment

After you deploy, you can perform a custom build step during the function build process by adding a [`gcp-build` script](https://docs.cloud.google.com/appengine/docs/standard/nodejs/running-custom-build-step#example) in your `package.json` file.

When this script is executed, the dependencies in the `dependencies` and `devDependencies` fields of your `package.json` file are available. After executing your custom build step, Cloud Run functions removes and regenerates the `node_modules` folder by only installing the production dependencies declared in the `dependencies` field of your `package.json` file.

If there is no `gcp-build` script in `package.json`, Cloud Run functions just installs production dependencies.

## Using system packages

The Node.js runtime also includes a number of [system packages](https://docs.cloud.google.com/functions/docs/reference/nodejs-system-packages) in the execution environment. If your function uses a dependency that requires a package that is not listed, you can [request a package](https://docs.cloud.google.com/functions/docs/reference/nodejs-system-packages#requesting_a_package).

**Note:** you can also deploy containerized versions of your Node.js Cloud Run functions to [Cloud Run](https://docs.cloud.google.com/run/docs) using the [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework).

## Including local Node.js modules

You can also include local Node.js modules as part of your function. You can achieve this by declaring your module in `package.json` using the [`file:` prefix](https://docs.npmjs.com/files/package.json#local-paths). In the following example, `mymodule` refers to your module name and `mymoduledir` is the directory containing your module:
    
    
    {
      "dependencies": {
        "mymodule": "file:mymoduledir"
      }
    }

The code for this local module should be stored somewhere other than the `node_modules` folder within your function's root directory.

**Note:** if you deploy using the `gcloud` command-line tool, `gcloud` automatically creates a [`.gcloudignore`](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file in your function's directory. By default, the `node_modules` folder is added to this `.gcloudignore` and is not uploaded as part of your deployment. You don't need to include the `node_modules` folder when you manually upload code as a .zip file—you can successfully deploy your function without the the `node_modules` folder.

## Loading Node.js modules

Use the Node.js [`require()`](https://nodejs.org/api/modules.html#modules_require) function to load any Node.js module you have installed. You can also use the `require()` function to import local files you deploy alongside your function.

## Using private modules

You can use a [private npm module](https://docs.npmjs.com/private-modules/intro) by providing settings for authenticating with the registry in a `.npmrc` file in the function's directory. If you're using Yarn v2 or higher as your package manager, this file is named `.yarnrc.yml`.

### Private modules from Artifact Registry

An [Artifact Registry Node.js package repository](https://docs.cloud.google.com/artifact-registry/docs/nodejs/quickstart) can host private modules for your function. When you deploy a Cloud Run functions function, the build process automatically generates Artifact Registry credentials for the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). You only need to list the Artifact Registry repository in your `.npmrc` without generating additional credentials. For example:
    
    
    @SCOPE:registry=https://REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME
    //REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME:always-auth=true
    

This approach also works for the Yarn v1 package manager. If you're using Yarn v2 or higher, you only need to list the Artifact Registry repository in your `.yarnrc.yml` without additional credentials. For example:
    
    
    npmScopes:
      SCOPE:
        npmRegistryServer: https://REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME
        npmAlwaysAuth: true
    

### Private modules from other repositories

The [npm documentation](https://docs.npmjs.com/getting-started/working_with_tokens) explains how to create custom read-only access tokens. We discourage using the `.npmrc` file created in the home directory because it contains a read-write token. Write permissions are not required during deployment, and could pose a security risk.

Don't include the `.npmrc` file if you're not using private repositories, as it can increase the deployment time for your functions.

**Note:** If you're using any custom permissions (such as those necessary for [VPC](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc)), make sure that you explicitly allow your functions to access the target private repository.

#### File format

If you're using an `.npmrc` file to set a custom auth token, it should include the line shown below.
    
    
    //REGISTRY_DOMAIN/:_authToken=AUTH_TOKEN
    

Replace:

  * REGISTRY_DOMAIN: the domain name of your private npm registry. If your repository is hosted with `npmjs.org`, set this field to `registry.npmjs.org`.
  * AUTH_TOKEN: the authorization token for your npm registry. This can either be the literal text value of the token or the text string `${NPM_TOKEN}`, which `npm` replaces with the actual token value from the environment.

You can set the `$NPM_TOKEN` environment variable with the [`--set-build-env-vars`](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var#using_build_environment_variables) argument to your [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command. See the [NPM tutorial on private modules](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow#create-and-check-in-a-project-specific-npmrc-file) for more details of the NPM auth token.




## Build your function with vendored dependencies

Vendored dependencies are those whose source is included directly in your source code package and rebuilt alongside your own code. You create vendored Node.js dependencies and skip installing them during deployment by using the GOOGLE_VENDOR_NPM_DEPENDENCIES build environment variable.

### Prerequisites for vendored dependencies

  1. Ensure that you have a working function with all the dependencies that you want to vendor defined in your `package.json` file.

  2. Install these dependencies locally by running:
         
         npm install
         

  3. Remove `node_modules` from the .gcloudignore file in your working directory.

  4. Deploy the function, ensuring that your local Node.js version is the same as the one you specify during deployment.

  5. Deploy your function and the vendored dependencies with the following command:
         
         gcloud functions deploy FUNCTION_NAME \
             --runtime RUNTIME_NAME \
             --set-build-env-vars GOOGLE_VENDOR_NPM_DEPENDENCIES=true
         

Replace:

     * FUNCTION_NAME: the name of the Cloud Run functions function you're deploying
     * RUNTIME_NAME: the name of the Node.js runtime to run your deployed function under. This must be the same Node.js version as you've used in your local development environment



The Functions framework package is a required dependency for functions. For faster builds, we recommend vendoring this package. If you don't, it is downloaded and installed when your function is built.

If you specify an npm engine in the package.json file, the specified version of npm is downloaded at build time. To suppress this behavior, remove it from your package.json file.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
