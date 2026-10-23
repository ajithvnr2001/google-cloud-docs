---
url: https://docs.cloud.google.com/artifact-registry/docs/nodejs/
title: Get started with Node.js packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:55.682364+00:00
---

# Get started with Node.js packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/nodejs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Get started with Node.js packages Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry supports Node.js packages that you manage with npm.

## Overview

To get familiar with Node.js packages in Artifact Registry, you can try the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/nodejs/quickstart).

When you are ready to learn more, read the following information:

  1. If you are new to npm, read about the following concepts: 
     * npm scopes
     * the .npmrc configuration file
  2. [Create a Node.js package repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) for your packages.
  3. [Grant permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to the account that will connect with the repository. Service accounts for common integrations with Artifact Registry have default [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp) for repositories in the same project.
  4. Configure your tools: 
     * [Configure authentication](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication) for npm.
     * [Configure Cloud Build](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build) to upload and download packages.
     * Learn about [deploying](https://docs.cloud.google.com/artifact-registry/docs/deploy) to Google Cloud runtime environments.
  5. [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/nodejs/manage-packages).



## Using scopes

An npm scope is a label for grouping packages. Scopes are necessary when you are working with multiple npm registries, including:

  * Publishing and installing packages in different registries without the need to switch from one registry to another. For example, your builds might include packages from both the public npm registry and an Artifact Registry repository.
  * Publishing the same packages to multiple Artifact Registry repositories across Google Cloud projects, as well as other npm registries, without package name conflicts.



We recommend that you always set a scope for your repositories. If you do not specify a scope when you publish or install package, npm uses the configured default registry, such as the public npm registry.

You set the scope for each Artifact Registry repository in the `.npmrc` configuration file. The same credentials for authentication apply across the repositories.

The following example shows configuration for two Artifact Registry repositories in different projects.

  * The `@blue` scope is for the repository in the project `blue-project`.
  * The `@green` scope is for the repository in the project `green-project`.


    
    
    @blue:registry=https://us-central1-npm.pkg.dev/blue-project/blue-npm-repo/
    //us-central1-npm.pkg.dev/blue-project/blue-npm-repo/:always-auth=true
    
    @green:registry=https://us-central1-npm.pkg.dev/green-project/green-npm-repo/
    //us-central1-npm.pkg.dev/green-project/green-npm-repo/:_authToken=""
    //us-central1-npm.pkg.dev/green-project/green-npm-repo/:always-auth=true
    

After you have authenticated to Artifact Registry, you can upload a package to a particular repository using the appropriate scope. For example, the following command uploads a package to the `blue-npm-repo` in the project `blue-project`:
    
    
    npm publish @blue/blue-npm-repo
    

For more information about scopes, see the [npm documentation](https://docs.npmjs.com/using-npm/scope.html)

## Configuring npm

Settings used for authentication are stored in the `.npmrc` configuration file. You can configure an `.npmrc` file at the project, user, or global level.

When you configure authentication with Artifact Registry, you define the repositories that you want to connect to and the credentials for authentication.

Artifact Registry repositories
    

We recommend setting the repository list in the _per-project config file_. This file is usually in the same directory as the `package.json` file in your npm project. The Artifact Registry credential helper checks this `.npmrc` file for your repositories by default.

If you do not want to expose the repository paths in your source control system, you can:

  * Add the `.npmrc` filename your source control's list of files to ignore.
  * Store the repository list in your per-user confg file instead. The per-user `.npmrc` file is in your user home directory, or is set with the npm `--userconfig` parameter or `$NPM_CONFIG_USERCONFIG` environment variable. Settings in the per-user config file apply to all your projects unless you override them at the project level.


Artifact Registry credentials
    

Store your credentials for Artifact Registry in the _per-user config file_ so that they are not available to other users. This file is located in your user home directory, or is set with the npm `--userconfig` parameter or `$NPM_CONFIG_USERCONFIG` environment variable.

    

The Artifact Registry [credential helper](https://www.npmjs.com/package/google-artifactregistry-auth) is stored in the public npm registry and does not require authentication for installation.

You should retain any existing default registry configured in your `.npmrc` file. The default is typically set to the public npm registry at `https://registry.npmjs.org/`.

To check the current default registry value run the command:
    
    
    npm get registry
    

For more information about npm configuration files, see the [npm config file](https://docs.npmjs.com/files/npmrc) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
