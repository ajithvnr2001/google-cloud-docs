---
url: https://docs.cloud.google.com/docs/buildpacks/nodejs/
title: Building a Node.js application \u00a0|\u00a0 Buildpacks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:42.386472+00:00
---

# Building a Node.js application  |  Buildpacks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/nodejs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Guides ](https://docs.cloud.google.com/docs/buildpacks/overview)



Send feedback 

#  Building a Node.js application Stay organized with collections  Save and categorize content based on your preferences. 

## Specify versions of Node.js

The buildpacks project provides support for the Current and Active LTS releases of Node.js. Older releases of Node.js are available but might not be actively maintained by the project.

### Use `package.json`

You can specify the Node.js version of your application during deployment by configuring the `engines.node` field in the `package.json` file. To configure the buildpack to use the [latest version of Node.js](https://docs.cloud.google.com/static/docs/buildpacks/runtime-support#node.js) when deploying your app, add the following values in your `package.json`:
    
    
    "engines": {
      "node": "24.x.x"
    }
    

### Use `GOOGLE_NODEJS_VERSION`

You can also specify the Node.js version using the `GOOGLE_NODEJS_VERSION` environment variable. If both configurations are set, the `GOOGLE_NODEJS_VERSION` value takes precedence over the `engines.node` property. If you don't provide a version, then the buildpack uses the most recent LTS version of Node.js.

To configure the buildpack to use Node.js 24 when deploying your app, run the following command:
    
    
    pack build --builder=gcr.io/buildpacks/builder \
       sample-functions-framework-node \
       --env GOOGLE_NODEJS_VERSION=24.x.x
    

You can also use a `project.toml` project descriptor to encode the environment variable alongside your project files. See instructions on [building the application with environment variables](https://docs.cloud.google.com/docs/buildpacks/set-environment-variables#build_the_application_with_environment_variables\)). 

### Tips

  * `engines.node` field can take a semver constraint. The specific library we use for the Node.js buildpacks is [Masterminds/semver](https://github.com/Masterminds/semver)
  * Avoid using greater than (>) specifiers in the `engines.node` field.
  * When deploying the application into App Engine standard environment, the `engines.node` property should be compatible with the runtime specified in `app.yaml`. For more information about the `engines.node` configuration option in `package.json` file, see the official NPM documentation for the [engines topic](https://docs.npmjs.com/cli/v8/configuring-npm/package-json).
  * When deploying a function onto Cloud Run functions, the `engines.node` property should be compatible with the runtime used to deploy your function



## Install dependencies

NPM is the default package manager for all versions of Node.js. The following section includes the compatible dependencies for your Node.js applications.

### NPM package manager

  * NPM is the default package manager.
  * Whenever possible, use `package-lock.json` to improve cache performance.
  * By default only production dependencies are installed.
  * Specify the npm version using the `engines.npm` field in your `package.json` file. For more information, see the [NPM](https://docs.npmjs.com/) documentation.



### Yarn package manager

  * buildpack uses Yarn when you include the `yarn.lock` file in your project.
  * Specify the yarn version in the `engines.yarn` field of your `package.json` file.
  * buildpack supports Yarn2 PnP mode if your project includes a `.yarn/cache` folder.



### Pnpm package manager

  * buildpack uses Pnpm when you include the `pnpm-lock.yaml` file in your project.
  * Specify pnpm version in the `engines.pnpm` field of your `package.json` file.
  * For a working example, see [sample-node-pnpm](https://github.com/GoogleCloudPlatform/buildpack-samples/tree/master/sample-node-pnpm).



### Bun package manager

The Node.js buildpack supports the Bun package manager, `google.nodejs.bun buildpack` for installing dependencies. To use the Bun package manager, follow these steps:

  * Create a `bun.lock` or `bun.lockb` file in the root directory for automatic detection.
  * Alternatively, you can also explicitly set the `GOOGLE_PACKAGE_MANAGER` environment variable to `bun`. With this method, you don't need to create and maintain lockfiles.
  * Your project must include a `package.json` file. You can specify a Bun version in the `engines.bun` or `packageManager` field of your `package.json` file. If no version is specified, the buildpack defaults to the latest stable release.



For more information on deploying to Cloud Run, see [Specify dependencies in Node.js](https://docs.cloud.google.com/run/docs/runtimes/nodejs-dependencies#bun_package_manager).

For more information about the Bun package manager, see the [Bun documentation](https://bun.sh/docs/cli/install).

## Package manager precedence

The Node.js buildpack determines the package manager based on the configuration in the following order of precedence:

  1. The buildpack first checks for lockfiles in the following order:

     * Yarn - `yarn.lock`
     * pnpm - `pnpm-lock.yaml`
     * Bun - `bun.lock` or `bun.lockb`
     * NPM - `package-lock.json`
  2. If you don't use lockfiles, the Node.js buildpack uses the value you assign the `GOOGLE_PACKAGE_MANAGER` environment variable.

  3. If you don't use a lockfile or set the environment variable, the buildpack defaults to using NPM.




## Private modules

Use a [private npm module](https://docs.npmjs.com/private-modules/intro) by providing settings for authenticating with the registry in a `.npmrc` file in the function's directory. If you're using Yarn version 2 or later as your package manager, this file is named `.yarnrc.yml`.

### Private modules from Artifact Registry

An [Artifact Registry Node.js package repository](https://docs.cloud.google.com/artifact-registry/docs/nodejs/quickstart) can host private modules for your function. When you deploy a Buildpacks function, the build process automatically generates Artifact Registry credentials for the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). You only need to list the Artifact Registry repository in your `.npmrc` file when using NPM or Yarn version 1. For example, when using NPM or Yarn version 1:
    
    
    @SCOPE:registry=https://REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME
    //REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME:always-auth=true
    

If you're using Yarn version 2 or later, you only need to list the Artifact Registry repository in your `.yarnrc.yml` file without additional credentials. For example:
    
    
    npmScopes:
      SCOPE:
        npmRegistryServer: https://REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME
        npmAlwaysAuth: true
    

### Private modules from other repositories

The [npm documentation](https://docs.npmjs.com/getting-started/working_with_tokens) explains how to create custom read-only access tokens. We discourage using the `.npmrc` file created in the home directory because it contains a read-write token. Write permissions are not required during deployment, and could pose a security risk.

Don't include the `.npmrc` file if you're not using private repositories, as it can increase the deployment time for your functions.

**Note:** If you're using any custom permissions (such as those necessary for [VPC](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc)), make sure that you explicitly allow your functions to access the target private repository.

#### File format

If you're using an `.npmrc` file to set a custom auth token, include the following:
    
    
    //REGISTRY_DOMAIN/:_authToken=AUTH_TOKEN
    

Replace:

  * REGISTRY_DOMAIN: the domain name of your private npm registry. For example if your repository host is `npmjs.org`, set this field to `registry.npmjs.org`.
  * AUTH_TOKEN: the authorization token for your npm registry. This can either be the literal text value of the token or the text string `${NPM_TOKEN}`, which the `npm` command replaces with the actual token value from the environment.

You can set the `$NPM_TOKEN` environment variable with the [`--set-build-env-vars`](https://docs.cloud.google.com/functions/docs/configuring/env-var#using_build_environment_variables) argument to your [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command. See the [NPM tutorial on private modules](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow#create-and-check-in-a-project-specific-npmrc-file) for more details of the NPM auth token.




## Execute custom build steps during deployment

By default, `npm run build` is run if a script is specified in your `package.json` file. However, you can instead specify custom build steps to override the default behavior and run only the scripts that you want during the build. You can control the build steps by using either the `GOOGLE_NODE_RUN_SCRIPTS` environment variable or `gcp-build` in your `package.json` file.

You can only use one method. Note that the `GOOGLE_NODE_RUN_SCRIPTS` environment variable takes precedence and overrides anything that is specified for `gcp-build` in your `package.json`.

By default, when you configure custom build steps, both the `dependencies` and `devDependencies` in your `package.json` file are installed first before any scripts or commands are executed. To override the default behavior, you can use the `NODE_ENV` environment variable.

### Use `GOOGLE_NODE_RUN_SCRIPTS`

You can pass the `GOOGLE_NODE_RUN_SCRIPTS` environment variable to the build to control what scripts run. You can specify one or more scripts, or instead pass an empty environment variable to prevent the default behavior from running, like `GOOGLE_NODE_RUN_SCRIPTS=`. For complete details, see Environment variables.

### Use `package.json`

Adding `gcp-build` in your `package.json` file only runs `npm run gcp-build`, meaning that it overrides the default behavior. You can specify one or more commands, or instead specify an empty string to prevent any command from running, like `"gcp-build":""`.
    
    
    "scripts": {
      ...
      "gcp-build": "npm run lint && npm run build"
      ...
    }
    

## Application entrypoint

The Node.js buildpack executes the command you specify in the `scripts.start` field of your `package.json` file. If you don't configure the `scripts.start` field, the buildpack runs the `npm start` command.

We recommend using a Procfile because it takes the package manager out of the path and allows for direct execution.

## Environment variables

You can [set environment variables to configure builds](https://docs.cloud.google.com/docs/buildpacks/set-environment-variables) of your container image.

The Node.js buildpack supports the following environment variables to customize your container.

### `NODE_ENV`

Specifies the development environment during the build; set for `npm install`.

**Example:** `NODE_ENV=development` installs both the `dependencies` and `devDependencies` specified in `package.json`.

### `NPM_CONFIG_<key>`

Specifies the configuration parameter, for example, `NPM_CONFIG_FLAG=value` passes `-flag=value` to `npm` commands.

For information about this environment variable, see [Config](https://docs.npmjs.com/misc/config#environment-variables) in the NPM documentation.

### `GOOGLE_PACKAGE_MANAGER`

You can configure this environment variable to use a supported package manager. For example, `GOOGLE_PACKAGE_MANAGER=bun` forces the use of Bun even if you don't create a lockfile. This variable supports values such as, `npm`, `yarn`, `pnpm`, or `bun`.

### `GOOGLE_NODE_RUN_SCRIPTS`

Specifies an ordered list of npm scripts from `package.json` to run after installing dependencies. The list must be comma-separated and runs in the order that you list each script.

When you specify `GOOGLE_NODE_RUN_SCRIPTS`, only the scripts that you list are run. For example, if you want to prevent the default `npm run build` from running, specify the environment variable without a value.

**Examples:**

  * `GOOGLE_NODE_RUN_SCRIPTS=lint,build` runs `npm run lint` and then `npm run build`.
  * `GOOGLE_NODE_RUN_SCRIPTS=` runs no scripts.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
