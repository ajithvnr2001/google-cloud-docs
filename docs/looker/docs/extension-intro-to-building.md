---
url: https://docs.cloud.google.com/looker/docs/extension-intro-to-building/
title: Building a Looker extension \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:36:58.586558+00:00
---

# Building a Looker extension  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/extension-intro-to-building/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Building a Looker extension Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate and configure a basic Looker extension template, to which you can then add functionality.

Creating a new Looker extension requires you to perform the following tasks:

  * Configure a LookML project that includes a model file and project manifest file and that is connected to Git
  * Generate the extension template files



The following procedures show how to build the previous elements.

## Configuring Looker for an extension

Looker extensions each require a LookML project that includes a model file and a manifest file to run.

  1. [Create a blank project](https://docs.cloud.google.com/looker/docs/2510/generating-a-model#blank-project) for your extension.

  2. In your new project, [create a model file](https://docs.cloud.google.com/looker/docs/2510/ide-folders#creating_files) by using the `+` at the top of the file browser in the Looker IDE.

  3. The new model file is generated with a [`connection`](https://docs.cloud.google.com/looker/docs/2510/reference/param-model-connection) parameter and an [`include`](https://docs.cloud.google.com/looker/docs/2510/reference/param-model-include) parameter:

![](https://docs.cloud.google.com/static/looker/docs/images/new-model-file-ext-2104.png)

Replace `connection_name` in the [`connection`](https://docs.cloud.google.com/looker/docs/2510/reference/param-model-connection) parameter with the name of a valid [database connection](https://docs.cloud.google.com/looker/docs/2510/admin-panel-database-connections) on your instance. The extension requires a valid model file because Looker permissions data is accessed through the LookML model. To manage access to your extension, you must associate the extension with a valid LookML model and grant users permissions to access that model. When you are done editing the model file, click **Save Changes**.

Since your extension does not require a view file, either delete the `include: "/views/*.view.lkml"` parameter or add a `#` character at the beginning of the line to make the line a comment. Leaving the `include: "/views/*.view.lkml"` parameter as is will cause the LookML validator to generate errors.

  4. [Create a project manifest file](https://docs.cloud.google.com/looker/docs/2510/ide-folders#creating_files) by using the `+` at the top of the file browser in the Looker IDE.

The project manifest file will initally be empty, but later in this procedure you will copy generated contents into your project manifest file that will include the [`application`](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-application) parameter. The `application` parameter gives the extension a label, tells Looker where to find the extension JavaScript, and provides a list of [entitlements](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-application#entitlements) for the extension. Entitlements define the Looker resources that the extension can access. The extension will not be able to access a Looker resource unless that resource is listed in the entitlements.

You can leave the manifest file as is for now, though, since you will copy the rest of the file's contents into it later in this process.

  5. [Configure a Git connection](https://docs.cloud.google.com/looker/docs/2510/setting-up-git-connection) for your new project.

You can access the **Configure Git** page either by clicking the **Configure Git** button in the top right corner of the Looker IDE, or by using the **Project Configuration** page as described in the [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/2510/setting-up-git-connection) documentation page.




Once you've set up the project for your extension and connected it to Git, you are ready to generate the extension template files.

## Generating the extension template files

There are two ways to generate extension template code files:

  * Using the `create-looker-extension` utility
  * Cloning an extension template Git repository



Both processes require [Yarn](https://yarnpkg.com/), so ensure you have Yarn installed.

### Using `create-looker-extension` to create an extension template

The `create-looker-extension` utility creates a basic Looker extension that includes all the necessary extension files and dependencies. You can then use this as a starting point and add additional code and functionality to complete your extension.

To generate the extension template:

  1. Run the `create-looker-extension` utility, replacing `<extension_name>` with the name of your extension:
         
         yarn create looker-extension <extension_name>
         

  2. Either confirm the extension name or provide a different name, and then select the language and framework you want to use to build the extension:

![](https://docs.cloud.google.com/static/looker/docs/images/yarn-create-looker-extension-output-2108.png)

The `create-looker-extension` utility will then use the framework that you specified to populate a base template and put all the generated files into a new directory that uses the name of the extension:

![](https://docs.cloud.google.com/static/looker/docs/images/yarn-create-looker-extension-ls-2104.png)

  3. Navigate to the directory that was created for your extension:
         
         cd <extension_name>
         

  4. Install the extension dependencies:
         
         yarn install
         

  5. Start the development server:
         
         yarn develop
         

The extension is now running and serving the JavaScript locally at `http://localhost:8080/bundle.js`.

  6. In your extension directory is the file `manifest.lkml`. Copy the contents of this file.

  7. In your LookML project, paste the contents of `manifest.lkml` into your project manifest file:

![](https://docs.cloud.google.com/static/looker/docs/images/ext-manifest-contents-2108.png)

Click **Save Changes** to save your project manifest file.

**Note:** The contents of the generated `manifest.lkml` file include the [`project_name` LookML parameter](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-project-name). The `project_name` parameter is used by the Local Project Import feature. See the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/2510/importing-projects#importing_local_projects) documentation page for details on importing projects.
  8. In the LookML IDE, click **Validate LookML** , then click **Commit Changes & Push**, and then click **Deploy to Production**.

  9. Reload Looker using your browser's reload function.

In the **Applications** section of the Looker main menu, you will see the name of your new extension.

  10. Select your extension from the **Applications** section to view the extension's output.




### Cloning a Git repository to create an extension template

Looker maintains a Git repository with several extension templates at <https://github.com/looker-open-source/extension-examples>. If you would like to use one of the examples there, navigate to that example's repository, and follow the instructions shown next.

This procedure requires [Yarn](https://yarnpkg.com/), so ensure that you have Yarn installed.

  1. On your local command line, use the following command to clone the Git repository:
         
         git clone git@github.com:looker-open-source/extension-examples.git
         

  2. Navigate to the directory that contains the template you want to install on your system. In this example, we'll use the React and JavaScript "Hello World" extension:
         
         cd extension-examples/react/javascript/helloworld-js
         

  3. Install the extension dependencies:
         
         yarn install
         

> You may need to update your Node version or use a [Node version manager](https://github.com/nvm-sh/nvm) to change your Node version.

  4. In your extension directory is the file `manifest.lkml`. Copy the contents of this file.

  5. In your LookML project, paste the contents of `manifest.lkml` into your project manifest file:

![](https://docs.cloud.google.com/static/looker/docs/images/ext-manifest-contents-2104.png)

Click **Save Changes** to save your project manifest file.

  6. In the top right corner of the LookML IDE, click **Validate LookML** , then click **Commit Changes & Push**, and then click **Deploy to Production**.

  7. In your terminal, start the development server:
         
         yarn develop
         

The extension is now running and serving the JavaScript on a local development server specified in the [`url`](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-application#url) parameter of the manifest file: `http://localhost:8080/bundle.js`.

  8. Reload Looker using your browser's reload function.

In the **Applications** section of the Looker main menu, you will see the name of your new extension, which is determined by the [`label` parameter](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-application) in your project manifest file.

  9. Select your extension from the **Applications** section to view the extension's output.




## Modifying the extension

Once you've created the basic extension, you can modify or add code to it by modifying the appropriate JavaScript or TypeScript file.

The `src` directory under your extension directory contains the source file where you can add code. In the previous example, for the React and JavaScript "Hello World" template, the file is called `HelloWorld.js`. Modifying or adding code to that file will modify or add to function of the extension.

Following is the output of the React and JavaScript `HelloWorld.js` file:
    
    
    import React, { useEffect, useState, useContext } from 'react'
    import { Space, ComponentsProvider, Text } from '@looker/components'
    import { ExtensionContext } from '@looker/extension-sdk-react'
    
    export const HelloWorld = () => {
      const { core40SDK } = useContext(ExtensionContext)
      const [message, setMessage] = useState()
    
      useEffect(() => {
        const initialize = async () => {
          try {
            const value = await core40SDK.ok(core40SDK.me())
            setMessage(`Hello, ${value.display_name}`)
          } catch (error) {
            setMessage('Error occured getting information about me!')
            console.error(error)
          }
        }
        initialize()
      }, [])
    
      return (
        <>
          <ComponentsProvider>
            <Space p="xxxxxlarge" width="100%" height="50vh" around>
              <Text p="xxxxxlarge" fontSize="xxxxxlarge">
                {message}
              </Text>
            </Space>
          </ComponentsProvider>
        </>
      )
    }
    

In the previous example, you could change the text output of the extension by changing the text in the line:
    
    
    setMessage(`Hello, ${value.display_name}`).
    

> Keep in mind that as you add functionality, you may need to modify the [entitlements](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-application#entitlements) granted to your extension in the [`application`](https://docs.cloud.google.com/looker/docs/2510/reference/param-manifest-application) parameter in your project manifest file.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
