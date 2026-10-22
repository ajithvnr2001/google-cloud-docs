---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/gradle-reference/
title: App Engine Gradle Plugin Tasks and Properties \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:13.486941+00:00
---

# App Engine Gradle Plugin Tasks and Properties  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/gradle-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  App Engine Gradle Plugin Tasks and Properties Stay organized with collections  Save and categorize content based on your preferences. 

After the App Engine Gradle plugin is [added to your project](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/using-gradle#creating_a_new_project), you can use the following App Engine-specific Gradle tasks:

Task | Description  
---|---  
`tasks` | Displays help information on installed tasks.  
`appengineStage` | Generates an application directory for deployment.  
`appengineDeploy` | Stages and deploys an application to App Engine.  
`appengineDeployCron` | Deploys a `cron.yaml` configuration file to App Engine.  
`appengineDeployDispatch` | Deploys a `dispatch.yaml` configuration file to App Engine.  
`appengineDeployDos` | Deploys a `dos.yaml` configuration file to App Engine.  
`appengineDeployIndex` | Deploys an `index.yaml` configuration file to App Engine.  
`appengineDeployQueue` | Deploys a `queue.yaml` configuration file to App Engine.  
`jettyRun` |  Runs the development server using Jetty's default configurations. To find out more about the [Gretty plugin](https://github.com/akhikhl/gretty), see [Gretty Configuration](http://akhikhl.github.io/gretty-doc/Gretty-configuration.html) and [Gretty Tasks](http://akhikhl.github.io/gretty-doc/Gretty-tasks)  
  
To see a list of all the tasks:
    
    
    gradle tasks
    

For more information on how to set up and use Gradle, see [Using App Engine Gradle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/using-gradle) and the [`app-gradle-plugin`](https://github.com/GoogleCloudPlatform/app-gradle-plugin) repository on GitHub.

## Task properties

The contents of the `gradle.build` file are a set of rules to describe your build. It's written in a domain specific language for describing builds, based on the [Groovy language](http://www.groovy-lang.org/).

Each task has associated properties below that you can use. You can specify these properties in the `gradle.build` file using a [configuration closure](https://docs.gradle.org/current/userguide/custom_plugins.html#sec:getting_input_from_the_build), task, and properties.

In this example:

  * The configuration closure for the plugin is `appengine`.
  * The task is `deploy`.
  * The properties, `stopPreviousVersion` and `promote`, are set to `true`.


    
    
    appengine {
      deploy {   // deploy configuration
        stopPreviousVersion = true  // default - stop the current version
        promote = true              // default - & make this the current version
      }
    }

If you only have a to specify a few properties, you can set them in a single line: 
    
    
      appengine.deploy.stopPreviousVersion = true

See the following sections for a list of the properties that are available for each task.

## appengineStage

**task(stage)**

Generates an application directory for deployment. Used by the `appengineDeploy` task and the `jettyRun` task.

You can use the following properties:

Property | Description  
---|---  
`artifact` |  Built artifact that has all of the classes, resources, and manifests. Default is `build/libs/[YOUR_SERVLET].war`.   
`appEngineDirectory` |  Location of the `app.yaml` file. Default is `src/main/appengine`.   
`dockerDirectory` |  Location of the `Dockerfile`. Default is `src/main/docker`.   
`stagingDirectory` |  Required. The directory to which to stage the application. Default is `build/staged-app`.   
  
## appengineDeploy

**task(deploy)**

Stages and deploys an application to App Engine.

Each task has associated properties below that you can use. You can specify these properties in the `gradle.build` file using a [configuration closure](https://docs.gradle.org/current/userguide/custom_plugins.html#sec:getting_input_from_the_build), task, and properties.

In the following example:

  * The configuration closure for the plugin is `appengine`.
  * The task is `run`.
  * The property, `port`, is set to `8080`.


    
    
    appengine {  // App Engine tasks configuration
      run {      // local (dev_appserver) configuration (standard environments only)
        port = 8080                 // default
      }
    
      deploy {   // deploy configuration
        stopPreviousVersion = true  // default - stop the current version
        promote = true              // default - & make this the current version
      }
    }

If you only have a to specify a few properties, you can set them in a single line:
    
    
      appengine.run.port = 8888

Property | Description  
---|---  
`appEngineDirectory` |  Location of `.yaml` configuration files (cron, index, etc) from which configuration specific deployments (appengineDeployCron, etc) will deploy from. For flexible applications, this defaults to `src/main/appengine`.   
`bucket` |  The Cloud Storage bucket used to stage files associated with the deployment. If this argument is not specified, the application's default bucket is used.   
`deployables` |  The YAML files for the services or configurations you want to deploy. Default is the `app.yaml` file in the staging directory. If that is not found, attempts to automatically generate necessary configuration files (such as `app.yaml`) in the staging directory.   
`imageUrl` |  Deploy with a specific Docker image. Docker URL must be from one of the valid Artifact Registry hostnames.   
`project` |  The Google Cloud Platform project name to use for this invocation. Default is the current project selected when [initializing the gcloud tool](https://docs.cloud.google.com/sdk/gcloud/reference/init). To verify, use `gcloud config list project`.   
`promote` |  Promote the deployed version to receive all traffic. Default is True.   
`server` |  The App Engine server to connect to. Typically, you do not need to change this value.   
`stopPreviousVersion` |  Stop the previously running version when deploying a new version that receives all traffic.   
`version` |  The version of the app that will be created or replaced by this deployment. If you do not specify a version, one will be generated for you.  
  
## Global properties

Property | Description   
---|---  
`tools.cloudSdkHome` |  Optional property to configure the location of the Google Cloud CLI. Typically the plugin finds this in the gcloud CLI when it is installed with `gcloud components install app-engine-java`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
