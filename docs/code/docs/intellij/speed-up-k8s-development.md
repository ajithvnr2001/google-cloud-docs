---
url: https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development/
title: Speed up development in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:18.189816+00:00
---

# Speed up development in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Speed up development in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

To speed up your local development in Cloud Code for IntelliJ, take advantage of file sync and hot reloading, automatic deployment on save, and use modules to develop portions of an application separately.

## Enable file sync and hot reloading

To improve the efficiency of your local development workflow and avoid having to rebuild, redeploy, and restart your pods, Cloud Code supports copying changed files to a deployed container. This means that when you're making changes to static and source code files, you can see your changes take effect in seconds, making for an accelerated feedback loop.

For static files (like HTML and CSS files), this file copying behavior is called **file syncing**. 

For source code files, this behavior is called as **hot reloading** and supports the following file types: 

  * Go: *.go
  * Java: *.java, *.kt, *.scala, *.groovy, *.clj
  * NodeJS: *.js, *.mjs, *.coffee, *.litcoffee, *.json



With hot reloading configured, Cloud Code detects changes to supported files and syncs these changes to the running container on your cluster. Changes to file types that don't support hot reloading trigger an image rebuild and pod restart.

Automatic file-syncing and hot reloading are enabled by default when you're working with Buildpacks as your preferred builder. For other builders like Docker, you can specify a `sync` section in your `skaffold.yaml` file for the artifact you're customizing.

Your sync setting can be one of (in order of preference):

  * `auto`: Cloud Code automatically configures the sync. (only for Jib and Buildpacks artifacts.) This is the default for Buildpacks.
  * `infer`: The destinations for each changed file are inferred from the builder.
  * `manual`: You must specify the files in your local workspace and their destination in the running container.



The following sample `sync` section in a `skaffold.yaml` file specifies a `manual` sync to synchronize all `/static-html` HTML files to the `static` folder in a container:
    
    
    build:
      artifacts:
        - image: gcr.io/k8s-skaffold/node-example
          context: node
          sync:
            manual:
              - src: 'static-html/*.html'
                dest: static

For a detailed look at file syncing and specifying sync rules, see the [Skaffold guide on file sync](https://skaffold.dev/docs/filesync/).

## Add new features when developing on Kubernetes

After setting up file sync and hot reloading, start an iteration cycle and add more features to your project. Your changes are deployed to your Kubernetes cluster without stopping and removing the deployment, manually building and tagging the image, or updating the cluster.

A standard iteration cycle resembles the following:

  1. Make a change in your project. For example, if using the Cloud Code Java Guestbook app, add a new endpoint to the `FrontendController` class as follows:

     1. Open the `FrontendController.java` file from `src/main/java/cloudcode/guestbook/frontend` and add the following:
            
            @RequestMapping("/greeting")
            @ResponseBody
            public String greeting(@RequestParam(value="name", defaultValue="World") String name) {
               return String.format("Hello from Kubernetes with IntelliJ, %s!", name);
            }
            

     2. Add the necessary imports for the new annotations, `RequestMapping` and `ResponseBody`.

  2. Save your changes (`Ctrl`/`Cmd+S`) or build the project.

You can watch the progress and deployment logs in the console window. After the changes are deployed, confirm the updates.

  3. To end the continuous development session, click the **Stop** icon.

Cloud Code deletes all Kubernetes resources used for the development session.




## Develop microservices applications using `skaffold.yaml` configurations

When developing microservice applications, it can be useful to work on separate sections independently to simplify debugging and deployment.

You can develop and debug parts of your application independently by splitting your application into [modules](https://docs.cloud.google.com/code/docs/intellij/skaffold-modules). For example, the [Bank of Anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos) sample is an application containing ten microservices. The sample's [`skaffold.yaml`](https://github.com/GoogleCloudPlatform/bank-of-anthos/blob/main/skaffold.yaml) file groups these services into five modules named `setup`, `db`, `frontend`, `backend`, and `loadgenerator`.

### Define modules and configuration dependencies

To define modules and configuration dependencies:

  1. Open the project where you want to define the modules.

  2. Open the `skaffold.yaml` file.

  3. If your `skaffold.yaml` file has multiple configurations, to make a configuration a module, specify the following line:
         
         metadata:
           name: MODULE_NAME_1
         

For example, in the Bank of Anthos `skaffold.yaml`, the `db` module defines database deployments:
         
         apiVersion: skaffold/v3
         kind: Config
         metadata:
           name: db # module defining database deployments
         requires:
         - configs:
           - setup
         build:
           artifacts:
           - image: accounts-db
             context: src/accounts-db
           - image: ledger-db
             context: src/ledger-db
         manifests:
           rawYaml:
           - dev-kubernetes-manifests/accounts-db.yaml
           - dev-kubernetes-manifests/ledger-db.yaml
         deploy:
           kubectl: {}

  4. For configurations that rely on another configuration being deployed before the current configuration can be deployed, you must add the config to your dependencies. To specify a config dependency, add a `configs` list to the `requires` section of your `skaffold.yaml` file.

For example, the Bank of Anthos `skaffold.yaml` file includes the configuration dependency `setup`.

To define a dependency, add the following to your `skaffold.yaml` file where DEPENDENCY_NAME is the name of your dependency.
         
         requires:
             - configs: DEPENDENCY_NAME
         

Configurations listed this way can reference dependencies defined in the same file or other `skaffold.yaml` files in the current project.

  5. Test your configuration dependencies by building each of the modules separately to make sure that they're deployed with their dependencies by following the steps in Build specific modules and their dependencies.




### Build specific modules and their dependencies

After you've defined your modules and their dependencies, you can specify which modules you want to run in the **Build / Deploy** tab when you select **Run** > **Edit configurations**. **Note:** If a project has no modules, including older `skaffold.yaml` configurations, no additional configuration is required and only the **Build and deploy with all dependencies** option is available.

  1. Install the latest [Insiders builds](https://docs.cloud.google.com/code/docs/intellij/insiders#get).

  2. Go to **Run** > **Edit configurations** and open the **Build / Deploy** tab.

  3. For **Skaffold configuration** , select skaffold.yaml.

Choose one of the following:

     * **Build and deploy with all modules and dependencies**
     * **Build and deploy with** (if modules are available) and select the modules you want to build and deploy.



Your selection persists for subsequent deployments. If you select a subset of modules, Cloud Code displays a warning about deploying a subset of modules and not the whole system.

## Continuous development on Kubernetes

Once you have configured your run target with the options you want, you can either opt for a regular run of your application or start a development iteration cycle on your IDE to propagate any changes made to your source and dependencies to your live application.

The **Develop on Kubernetes** run target starts the development cycle on your Kubernetes cluster. After you start the development cycle, Cloud Code builds an image for the project, and then tags it, pushes it to the configured repository, and uses kubectl to deploy the project Kubernetes manifests.

  1. Click the **Develop on Kubernetes** icon and then click **Edit Configurations** to open the **Run/Debug Configurations** dialog.
  2. Customize your deployment using the [available configuration options](https://docs.cloud.google.com/code/docs/intellij/k8s-overview#customize_your_launch_configuration).
  3. If you want Cloud Code to redeploy your application automatically after your changes are saved, under **Watch mode - rebuild and redeploy** , select **On file save**. New Kubernetes applications have **On demand** selected by default. For more information about watch modes, see [Watch modes](https://docs.cloud.google.com/code/docs/intellij/watch-modes).
  4. If your application is configured to use [modules](https://docs.cloud.google.com/code/docs/intellij/skaffold-modules), you can select to only build or deploy specific modules.
  5. After you're satisfied with your configuration, click **OK** and then click the **Run** icon.



## What's next

  * Use Cloud Code's built in [minikube cluster](https://docs.cloud.google.com/code/docs/intellij/minikube-local-development) for local development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/debug)
  * Read the details on the [file sync feature](https://skaffold.dev/docs/filesync/)



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
