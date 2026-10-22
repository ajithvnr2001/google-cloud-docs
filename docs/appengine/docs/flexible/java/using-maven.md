---
url: https://docs.cloud.google.com/appengine/docs/flexible/java/using-maven/
title: Using Apache Maven and the App Engine Plugin \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:45.532568+00:00
---

# Using Apache Maven and the App Engine Plugin  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/java/using-maven/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using Apache Maven and the App Engine Plugin Stay organized with collections  Save and categorize content based on your preferences. 

[Apache Maven](http://maven.apache.org/) is a build automation tool for Java.

App Engine provides a Maven plugin that you can use to build and deploy your app to App Engine. The plugin does not support Enterprise Application Archive (EAR) projects.

**Note:** For information about other ways to build and deploy your app, see [Testing and deploying your app](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app).

## Before you start

  1. Determine if Maven is installed and which version you have by running the following command:
         
         mvn -v
         

If Maven is installed, a long string of information beginning with `Apache Maven` and followed by a version number such as `3.9.1` will display.

  2. If you don't have Maven 3.9.1 or newer installed:

     1. [Download](https://maven.apache.org/download.cgi) Maven 3.9.1 or newer.
     2. [Install](https://maven.apache.org/install.html) Maven 3.9.1 or newer.

Default Linux package managers, such as `apt` or `apt-get` on Ubuntu and Debian provide older Maven versions and might not include Maven 3.9.1 or newer. To install a supported version on Linux, download the binary archive directly from the [Apache Maven](https://maven.apache.org/download.cgi) site, and follow the [installation instructions](https://maven.apache.org/install.html).

  3. If you haven't already done so, follow the steps [here](https://docs.cloud.google.com/appengine/docs/flexible/setting-up-environment) to download the gcloud CLI, create your Google Cloud project, and initialize your App Engine app.

  4. Install the gcloud CLI `app-engine-java` component:
         
         gcloud components install app-engine-java
         




## Adding the App Engine Maven plugin

To use the [App Engine Maven plugin](https://github.com/GoogleCloudPlatform/appengine-plugins/tree/main/app-maven-plugin), add the following lines to the `plugins` section in your project's `pom.xml` file:
    
    
    <plugins>
       <plugin>
         <groupId>com.google.cloud.tools</groupId>
         <artifactId>appengine-maven-plugin</artifactId>
         <version>2.8.7</version>
       </plugin>
       <plugin>
         <groupId>org.eclipse.jetty</groupId>
         <artifactId>jetty-maven-plugin</artifactId>
         <version>9.4.56.v20240826</version>
       </plugin>
    </plugins>

**Note:** If there is a newer version of the App Engine Maven plugin, you should upgrade to the [latest version](http://mvnrepository.com/artifact/com.google.cloud.tools/appengine-maven-plugin). The App Engine plugin includes the Jetty Maven plugin, which you can use to test your application quickly without creating a WAR file. 

## Using the Jetty Maven plugin to test your app locally

During the development phase, you can run and test your app at any time in the development server by invoking the Jetty Maven plugin.

To run your app in the development server:

  1. Build your app if you haven't already done so:
         
         mvn package
         

  2. Change directory to the top level of your project (for example, to `myapp`), and run your app by invoking Maven:
         
         mvn jetty:run
         

  3. Wait for the server to start and use your browser to visit [`http://localhost:8080/`](http://localhost:8080) to access your app.

  4. Shut down the app and the development server by pressing **Control+C**.




## Building and deploying your app

After you add the App Engine Maven plugin to your project's `pom.xml` file, you can use the following command to build deploy your app:
    
    
    mvn package appengine:deploy -Dapp.deploy.projectId=PROJECT_ID

Replace PROJECT_ID with the ID of your Google Cloud project. If your `pom.xml` file already [specifies your project ID](https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference#appenginedeploy), you don't need to include the `-Dapp.deploy.projectId` property in the command you run. 

The `package` goal builds and packages your app, and the [`appengine:deploy` goal](https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference#appenginedeploy) does the following:

  1. Generates a unique version ID for the new version of your app.

  2. Deploys the new version to App Engine.

  3. Routes all traffic to the new version.




## Changing the deployment defaults

You can change the default deployment behavior by passing parameters in the `appengine:deploy` command. For example, the following command deploys the service defined in your `pom.xml` file to a specific Google Cloud project, assigns a custom version ID to the service, and turns off automatic traffic routing for the new version:
    
    
    mvn appengine:deploy -Dapp.deploy.projectId=PROJECT_ID -Dapp.deploy.version=VERSION_ID -Dapp.deploy.promote=False

You can also use the `appengine:deploy` command to deploy configuration files, such as `cron.yaml`, `dispatch.yaml`, and `index.yaml`.

For more information, see the `appengine:deploy` [reference](https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference#appenginedeploy) .

## What's next

  * Review the [JDK 21 App Engine Maven plugin sample](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/appengine-java21/helloworld).
  * Explore the plugin code and report issues on [GitHub](https://github.com/GoogleCloudPlatform/app-maven-plugin).
  * Learn how to specify parameters for tasks by referring to [App Engine Maven Goals and Parameters](https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference#appenginedeploy). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
