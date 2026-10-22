---
url: https://docs.cloud.google.com/dataform/docs/use-packages/
title: Use JavaScript packages \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:22.525027+00:00
---

# Use JavaScript packages  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/use-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Use JavaScript packages Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to do the following:

  * Install a JavaScript package in a Dataform repository.
  * Authenticate a private NPM package to enable its installation in a repository.
  * Create a custom JavaScript package that you can use to develop workflows.



## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Do one or both of the following:

     1. To install a package in a repository or authenticate a private NPM package to enable its installation, follow these steps: 
        1. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).
        2. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).
        3. Optional: To install a private package, authenticate the private package.
        4. If your repository doesn't contain a `package.json` file, [create `package.json` and move the Dataform core package](https://docs.cloud.google.com/dataform/docs/manage-repository#move-to-package-json).
     2. To create a package, follow these steps: 
        1. [Create a Dataform repository](https://docs.cloud.google.com/dataform/docs/create-repository) that's dedicated to your package. Match the repository name to the name of your package.
        2. [Connect the repository](https://docs.cloud.google.com/dataform/docs/connect-repository) to a third-party Git repository that will host your package.
        3. [Create and initialize a workspace](https://docs.cloud.google.com/dataform/docs/create-workspace) in the Dataform repository.
  3. Ensure that you have the necessary permissions to complete the tasks in this document.




### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the following IAM roles: 

  * [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on workspaces and repositories
  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`) on repositories



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Install a package

This section shows you how to install a JavaScript package and import it to a JavaScript file and a SQLX file so that you can use the package to develop workflows in Dataform.

To use a package in Dataform, you need to install it in your repository.

You can install the following types of packages in Dataform:

  * Published public NPM packages
  * Non-published public NPM packages
  * Authenticated private NPM packages



Then, to use the package in a JavaScript or SQLX file, you need to import selected contents of the package to the file. You can also import a whole package to a JavaScript or SQLX file instead of its selected contents.

To prevent issues with package installation in your production environment, we recommend that you do the following:

  * Explicitly specify the package version in `package.json`, for example, `3.0.0`. Don't use other [`dependencies` options](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#dependencies) of `package.json`, for example, `>version`.

  * Test new package versions in a non-production environment. For more information about configuring different workflow lifecycle environments, see [Best practices for the workflow lifecycle](https://docs.cloud.google.com/dataform/docs/managing-code-lifecycle).




### Add a package as a dependency

To install a package inside a Dataform repository, you need to add it as a dependency in the `package.json` file:

  1. In your workspace, in the **Files** pane, select `package.json`.
  2. Add the package to the `dependencies` block:

     1. Add a published public NPM package in the following format:
            
            "PACKAGE-NAME": "PACKAGE-VERSION"
            

Replace the following:

        * PACKAGE-NAME with the name of the package.
        * PACKAGE-VERSION with the latest version of the published public NPM package. To prevent issues with package installation, explicitly specify the version, for example, `3.0.0`.
     2. Add a non-published public NPM package in the following format:
            
            "PACKAGE-NAME": "PACKAGE-URL"
            

Replace the following:

        * PACKAGE-NAME with the name of the package.
        * PACKAGE-URL with the `tar.gz` URL of the third-party package repository, for example `https://github.com/user/sample-package-repository/archive/master.tar.gz`.
     3. Add an authenticated private NPM package in the following format:
            
            "REGISTRY-SCOPE/PACKAGE-NAME": "PACKAGE-URL"
            

Replace the following:

        * REGISTRY-SCOPE with the name of the package. REGISTRY-SCOPE must match the registry scope defined in the `.npmrc` file in your repository.
        * PACKAGE-NAME with the name of the package.
        * PACKAGE-URL with the `tar.gz` URL of the package repository, for example `https://github.com/user/sample-package-repository/archive/master.tar.gz`.
  3. Click **Install packages**.

  4. [Commit](https://docs.cloud.google.com/dataform/docs/manage-repository#commit-changes) and [push](https://docs.cloud.google.com/dataform/docs/manage-repository#push-changes) your changes.




The following code sample shows the public open-source Slowly changing dimensions package package added to the `.package.json` file:
    
    
     ```json
     {
       "name": "repository-name",
       "dependencies": {
         "@dataform/core": "2.0.3",
         "dataform-scd": "https://github.com/dataform-co/dataform-scd/archive/0.3.tar.gz"
       }
     }
     ```
    

### Import a package function or constant to a JavaScript file in Dataform

To use a function or a constant from a package inside a JavaScript file in Dataform, you need to first import it to the file.

To import a function or a constant from a package to a JavaScript file, follow these steps:

  1. In your workspace, in the **Files** pane, select a `.js` file in which you want to use the package.
  2. In the file, import a function or a constant in the following format:
         
         const { EXPORT-NAME } = require("PACKAGE-NAME");
         

     1. Replace EXPORT-NAME with the name of the function or constant that you want to use, declared in `module.exports` in the package `index.js` file.
     2. Replace PACKAGE-NAME with the name of the package that you want to use.
  3. [Commit](https://docs.cloud.google.com/dataform/docs/manage-repository#commit-changes) and [push](https://docs.cloud.google.com/dataform/docs/manage-repository#push-changes) your changes.




The following code sample shows the `getDomain` function from the `postoffice` package imported and used in a JavaScript file:
    
    
    /*
     * Contents of postoffice index.js:
     * module.exports = { getDomain };
     */
    
    const { getDomain } = require("postoffice");
    getDomain();
    

### Import a whole package to a JavaScript file in Dataform

To import the whole package to a JavaScript file instead of importing selected functions or constants to a JavaScript file, follow these steps:

  1. In your workspace, in the **Files** pane, select a `.js` file in which you want to use the package.
  2. In the file, import the package in the following format:
         
         const CONSTANT-NAME = require("PACKAGE-NAME");
         

     1. Replace CONSTANT-NAME with a name for the constant.
     2. Replace PACKAGE-NAME with the name of the package that you want to use.
  3. [Commit](https://docs.cloud.google.com/dataform/docs/manage-repository#commit-changes) and [push](https://docs.cloud.google.com/dataform/docs/manage-repository#push-changes) your changes.




The following code sample shows the `getDomain` function from the imported `postoffice` package used in a JavaScript file:
    
    
    /*
     * Contents of postoffice index.js:
     * module.exports = { getDomain };
     */
    
    const postoffice = require("postoffice");
    postoffice.getDomain();
    

### Import a package function or constant to a SQLX file in Dataform

To use a function or a constant from a package inside a SQLX file, you need to first import it to the file.

To import a function or a constant from a package to a SQLX file, follow these steps:

  1. In your workspace, in the **Files** pane, select a `.sqlx` file in which you want to use the package.
  2. In the file, enter the following `js` block:
         
         js {
           const { EXPORT-NAME } = require("PACKAGE-NAME");
         }
         

     1. Replace EXPORT-NAME with the name of the function or constant that you want to use, declared in `module.exports` in the package `index.js` file.
     2. Replace PACKAGE-NAME with the name of the package that you want to use.
  3. [Commit](https://docs.cloud.google.com/dataform/docs/manage-repository#commit-changes) and [push](https://docs.cloud.google.com/dataform/docs/manage-repository#push-changes) your changes.




The following code sample shows the `getDomain` function from the `postoffice` package imported in a `js` block and used in a `SELECT` statement in a SQLX file:
    
    
    /*
     * Contents of postoffice index.js:
     * module.exports = { getDomain };
     */
    
    config {
        type: "table",
    }
    
    js {
      const { getDomain } = require("postoffice");
    }
    
    SELECT ${getDomain("email")} as test
    

### Import a whole package to a SQLX file in Dataform

To import the whole package to a SQLX file instead of importing selected functions or constants to a JavaScript file, follow these steps:

  1. In your workspace, in the **Files** pane, select a `.sqlx` file in which you want to use the package.
  2. In the file, import the package in the following format:
         
         js {
           const CONSTANT-NAME = require("PACKAGE-NAME");
         }
         

     1. Replace CONSTANT-NAME with a name for the constant.
     2. Replace PACKAGE-NAME with the name of the package that you want to use.
  3. [Commit](https://docs.cloud.google.com/dataform/docs/manage-repository#commit-changes) and [push](https://docs.cloud.google.com/dataform/docs/manage-repository#push-changes) your changes.




The following code sample shows the `postoffice` package imported in a `js` block and its `getDomain` function used in a `SELECT` statement in a SQLX file:
    
    
    /*
     * Contents of postoffice index.js:
     * module.exports = { getDomain };
     */
    
    config {
        type: "table",
    }
    
    js {
      const postoffice = require("postoffice");
    }
    
    SELECT ${postoffice.getDomain("email")} as test
    

## Authenticate a private package

**Caution:** Secrets shared with the Dataform service agent (such as private NPM registry tokens) can potentially be accessed by users who can edit code or trigger compilation results in the repository. For more information, see [Secrets access during package installation](https://docs.cloud.google.com/dataform/docs/access-control#secret-access-risk).

This section shows you how to authenticate a private NPM package in Dataform to enable its installation in a Dataform repository.

To install a [private NPM package](https://docs.npmjs.com/about-private-packages) in a Dataform repository and use it to develop your workflow, you need to first authenticate the package in Dataform. The authentication process is different for the first private package in a repository and a subsequent private package in a repository.

### Authenticate the first private package in a Dataform repository

To authenticate private NPM packages in Dataform, you need to do the following before you install the first private NPM package in a Dataform repository:

  1. Create a Secret Manager secret dedicated to storing authentication tokens of private NPM packages in the Dataform repository.

     1. Add the authentication token of the package, obtained from your NPM registry, to the secret.

You need to store all authentication tokens of the private NPM packages in your repository in a single secret. You need to create one dedicated secret per a Dataform repository. The secret must be in the JSON format.

  2. Upload the secret to the Dataform repository.

  3. Create an `.npmrc` file and add the authentication token of the package to the file.

The authentication token in the `.npmrc` file must match the authentication token in the uploaded secret.




After you authenticate the private NPM package, you can install the package in the Dataform repository.

#### Create a secret for authentication of private packages

To authenticate private NPM packages in a Dataform repository, you need to create a Secret Manager secret and define authentication tokens for all private packages that you want to install in the Dataform repository inside the secret. Define one authentication token for each private NPM package, and store all authentication tokens in a single secret for each repository. The secret must be in the JSON format.

To create a secret with authentication tokens for private NPM packages, follow these steps:

  1. In Secret Manager, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

     1. In the **Secret value** field, enter one or multiple authentication tokens in the following format:
    
    {
      "AUTHENTICATION_TOKEN_NAME": "TOKEN_VALUE"
    }
    

Replace the following:

     * AUTHENTICATION_TOKEN_NAME: a unique name for the token that identifies the package it authenticates.
     * TOKEN_VALUE: the value of the authentication token, obtained from your NPM registry.
  2. [Grant access to the secret to the Dataform service agent](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

The Dataform service agent ID is in the following format:
         
         service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
         

     1. When granting access, make sure to grant the [`roles/secretmanager.secretAccessor`](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor) role to the Dataform service agent.



#### Upload the secret for authentication of private packages to a Dataform repository

Before you install a private NPM package in a Dataform repository for the first time, upload your secret containing the authentication token of the package to the repository.

To upload the secret with private NPM packages authentication tokens to a Dataform repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select the repository in which you want to install private NPM packages.

  3. On the repository page, click **Settings > Configure private NPM packages**.

  4. In the **Add NPM package secret token** pane, in the **Secret** menu, select your secret containing authentication tokens for private NPM packages.

  5. Click **Save**.




#### Create an `.npmrc` file for authentication of private packages

To authenticate private NPM packages in a Dataform repository, you need to create a top-level `.npmrc` file in the repository. You need to store authentication tokens for all private NPM packages to be installed in the repository inside the `.npmrc` file. The authentication tokens in the `.npmrc` file must match the authentication tokens in the secret uploaded to the repository. For more information about `.npmrc` files, see [npmrc documentation](https://docs.npmjs.com/cli/v9/configuring-npm/npmrc).

To create a top-level `.npmrc` file in your repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select the repository in which you want to install private NPM packages, and then select a workspace.

  3. In the **Files** pane, click more_vert **More** , and then click **Create file**.

  4. In the **Create new file** pane, do the following:

     1. In the **Add a file path** field, enter `.npmrc`.

     2. Click **Create file**.




#### Add an authentication token to the `.npmrc` file in a Dataform repository

To authenticate a private NPM package in a Dataform repository that already contains a secret with package authentication tokens and a `.npmrc` file, you need to add the authentication token for the private package to the `.npmrc` file in the repository.

In the `.npmrc` file, you need to define the scope of your NPM registry and add the authentication token for the private package accessed in that scope. For more information about `.npmrc` files, see [npmrc documentation](https://docs.npmjs.com/cli/v9/configuring-npm/npmrc).

The authentication token in the `.npmrc` file must match the authentication token in the secret uploaded to the repository.

To add an authentication token to the `.npmrc` file in a Dataform repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select the repository in which you want to install private NPM packages, and then select a workspace.

  3. In the **Files** pane, select the `.npmrc` file.

  4. In the `.npmrc` file, define the NPM registry scope and the authentication token for the private package in following format:
         
         @REGISTRY-SCOPE:registry=NPM-REGISTRY-URL
         NPM-REGISTRY-URL:_authToken=$AUTHENTICATION-TOKEN
         

Replace the following:

     * REGISTRY-SCOPE: the NPM registry scope to which you want to apply the authentication token.
     * NPM-REGISTRY-URL: the URL of your NPM registry, for example, `https://npm.pkg.github.com`.
     * AUTHENTICATION-TOKEN: the authentication token for the private NPM package. The authentication token in the `.npmrc` file must match the authentication token in the uploaded secret. The authentication token is provided as an environment variable in the `.npmrc` file, so make sure you add the opening `${` and `}` closing brackets.

You can enter multiple authentication tokens.




The following code sample shows an authentication token for a private NPM package added to the `.npmrc` file in a Dataform repository:
    
    
    @company:registry=https://npm.pkg.github.com
    //npm.pkg.github.com/:_authToken=${AUTHENTICATION_TOKEN}
    

### Authenticate a subsequent private package in a Dataform repository

To authenticate a private NPM package in a Dataform repository that already contains a secret with package authentication tokens and an `.npmrc` file, follow these steps:

  1. In Secret Manager, [list secrets](https://docs.cloud.google.com/secret-manager/docs/view-secret-details) and select the secret that stores authentication tokens of private NPM packages of your repository.

  2. [Add a new version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) to the secret.

Dataform uses the latest version of the secret by default.

     1. Add the authentication token for the private package to the secret value in the following format:
    
    {
      "AUTHENTICATION_TOKEN_NAME": "TOKEN_VALUE"
    }
    

Replace the following:

     * AUTHENTICATION_TOKEN_NAME: a unique name for the token that identifies the package it authenticates.
     * TOKEN_VALUE: the value of the authentication token, obtained from your NPM registry.

You can add multiple authentication tokens at once.

  3. In Dataform, add the authentication token to the `.npmrc` file in your repository.




After you authenticate the private NPM package, you can install the package in the Dataform repository.

## Create a package

This section shows you how to create a custom JavaScript package that you can use to develop workflows in Dataform.

To create a package that you can reuse in multiple Dataform repositories, you need to create a Dataform repository dedicated to the package and connect it to a third-party Git repository to make it available to other Dataform repositories.

Then, you need to create a top-level `index.js` file and add your exportable package contents, such as functions and constants, to the file. For an example of a package created in Dataform, see [`dataform-package-base`](https://github.com/dataform-co/dataform-package-base) on GitHub.

After you create the package, you can install the package in a different Dataform repository and use the exportable contents on the package, such as constants and functions, to develop workflows.

As an alternative to creating a package, you can reuse JavaScript functions and constants across a single Dataform repository with includes. For more information, see [Reuse variables and functions with includes in Dataform](https://docs.cloud.google.com/dataform/docs/reuse-code-includes).

To create your own package with JavaScript code that you can reuse in Dataform, follow these steps in your workspace:

  1. In the **Files** pane, click more_vert **More**.

  2. Click **Create file**.

     1. In the **Create new file** pane, do the following:

     2. In the **Add a file path** field, enter `index.js`.

     3. Click **Create file**.

  3. In the `index.js` file, enter the JavaScript code that you want your package to export.

     1. Create constants in the following format:
            
            const CONSTANT_NAME = CONSTANT_VALUE;
            module.exports = { CONSTANT_NAME };
            

Replace the following:

        * `CONSTANT_NAME`: the name of your constant
        * `CONSTANT_VALUE`: the value of your constant
     2. Create functions in the following format:
            
            function FUNCTION_NAME(PARAMETERS) { FUNCTION_BODY }
            
            module.exports = { FUNCTION_NAME }
            

Replace the following:

        * `FUNCTION_NAME`: the name of your function.
        * `PARAMETERS`: the parameters of your function.
        * `FUNCTION_BODY`: the code that you want the function to run.
  4. Optional: Click **Format**.

  5. Optional: In the `definitions` directory, add the code of your package that won't be exported.

  6. [Commit](https://docs.cloud.google.com/dataform/docs/manage-repository#commit-changes) and [push](https://docs.cloud.google.com/dataform/docs/manage-repository#push-changes) your changes.




The following package code sample shows the `index.js` file of the `postoffice` package that exports the `getDomain` function:
    
    
    // filename index.js
    // package name postoffice
    
    const GENERIC_DOMAINS = "('samplemail.com','samplemail.co.uk','examplemailbox.com'";
    
    function getDomain(email) {
      let cleanEmail = `trim(${email})`
      const domain = `substr(${cleanEmail}, strpos(${cleanEmail}, '@') + 1)`;
      return `case
                when ${domain} in ${common.GENERIC_DOMAINS} then ${cleanEmail}
                when ${domain} = "othermailbox.com" then "other.com"
                when ${domain} = "mailbox.com" then "mailbox.global"
                when ${domain} = "support.postman.com" then "postman.com"
                else ${domain}
              end`;
    }
    
    module.exports = { getDomain }
    

## What's next

  * To learn how to manage the required Dataform core package, see [Manage the Dataform core package](https://docs.cloud.google.com/dataform/docs/manage-repository#manage-dataform-core-package).
  * To learn more about packages in Dataform, see [Reuse code across multiple repositories with packages](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_multiple_repositories_with_packages).
  * To learn how to write JavaScript variables and functions that you can reuse in Dataform, see [Reuse variables and functions with includes in Dataform](https://docs.cloud.google.com/dataform/docs/reuse-code-includes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
