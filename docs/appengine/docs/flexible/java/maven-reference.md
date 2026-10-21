---
url: https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference/
title: App Engine Maven Plugin Goals and Parameters \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:08.643246+00:00
---

# App Engine Maven Plugin Goals and Parameters  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  App Engine Maven Plugin Goals and Parameters Stay organized with collections  Save and categorize content based on your preferences. 

After you [add the gcloud CLI-based App Engine Maven plugin to your project](https://docs.cloud.google.com/appengine/docs/flexible/java/using-maven#adding_the_maven_plugin) , the following App Engine-specific Maven goals are available:

Goal | Description  
---|---  
`appengine:cloudSdkLogin` | Sets the global gcloud CLI state for **account**.  
`appengine:deploy` | Stages and deploys an application to App Engine.  
`appengine:deployAll` | Stages and deploys an application with all of its valid yaml configurations simultaneously to App Engine.  
`appengine:deployCron` | Stages and deploys a `cron.yaml` configuration file to App Engine.  
`appengine:deployDispatch` | Stages and deploys a `dispatch.yaml` configuration file to App Engine.  
`appengine:deployDos` | Stages and deploys a `dos.yaml` configuration file to App Engine.  
`appengine:deployIndex` | Stages and deploys an `index.yaml` configuration file to App Engine.  
`appengine:deployQueue` | Stages and deploys a `queue.yaml` configuration file to App Engine.  
`appengine:help` | Displays help information on the App Engine Maven plugin.  
`appengine:run` |  Runs the App Engine development server. When the server is running, it continuously checks to determine whether `appengine-web.xml` has changed. If it has, the server reloads the application. You do not need to stop and restart your application because of changes to `appengine-web.xml`. This goal is supported for the legacy bundled services.   
`appengine:stage` | Generates an application directory for deployment.  
`appengine:start` |  Starts running the App Engine devserver asynchronously and then returns to the command line. When this goal runs, the behavior is the same as the `run` goal except that Maven continues processing goals and exits after the server is up and running. This goal is supported for the legacy bundled services.   
`appengine:stop` | Stops a running App Engine web development server. This goal is supported for the legacy bundled services.  
**Note:** The goals [`appengine:run`](https://docs.cloud.google.com/appengine/docs/legacy/standard/java/maven-reference#appenginerun), [`appengine:start`](https://docs.cloud.google.com/appengine/docs/legacy/standard/java/maven-reference#appenginestart), and [`appengine:stop`](https://docs.cloud.google.com/appengine/docs/legacy/standard/java/maven-reference#appenginestop) only apply to apps that use the legacy bundled services and deploy with an [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) file in the standard environment.

For more information on how to set up and use Maven, see [Using Maven](https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference#appenginedeploy). 

## Using parameters

Each goal has associated parameters that you can specify in the `pom.xml` file. For example:
    
    
    <plugins>
       <plugin>
         <groupId>com.google.cloud.tools</groupId>
         <artifactId>appengine-maven-plugin</artifactId>
         <version>2.8.7</version>
         <configuration>
           <deploy.stopPreviousVersion>true</deploy.stopPreviousVersion>
           <cloudSdkHome>/usr/foo/path/to/cloudsdk</cloudSdkHome>
         </configuration>
      </plugin>
    </plugins>

**Note:** The parameter prefixes, such as `devserver`, are optional. You can add `<port>8080</port>` instead of `<devserver.port>8080</devserver.port>`.

You can also define configuration parameters in the command line, following the pattern `-D[USER_PROPERTY]=[PARAMETER_VALUE]`.

For example, to specify a directory to which to stage your application:
    
    
    mvn appengine:stage -Dapp.stage.stagingDirectory=[YOUR_STAGING_DIRECTORY]
    

See the following sections for a list of the parameters that are available for each goal.

## `appengine:deploy`

Stages and deploys an application to App Engine.

You can use the following parameters, some of which correspond to [`gcloud app deploy` command line flags](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) or [`gcloud app services` command line flags](https://docs.cloud.google.com/sdk/gcloud/reference/app/services):

Parameter | Description | User Property  
---|---|---  
`appEngineDirectory` | The directory that contains `app.yaml` and other supported App Engine configuration files. Default is `${basedir}/src/main/appengine`. | `app.stage.appEngineDirectory`  
`artifact` | The location of the JAR or WAR archive to deploy. Default is `${project.build.directory}/${project.build.finalName}.${project.packaging}`. | `app.stage.artifact`  
`bucket` | The Cloud Storage bucket used to stage files associated with the deployment. If this argument is not specified, the application's default bucket is used. | `app.deploy.bucket`  
`cloudSdkPath` | Optional parameter to configure the location of the Google Cloud CLI. Default is to automatically discover from the PATH or standard install location. | `cloudSdkPath`  
`deployables` | The YAML files for the services or configurations you want to deploy. Default is the `app.yaml` file in the staging directory. If that is not found, attempts to automatically generate necessary configuration files (such as `app.yaml`) in the staging directory. | `app.deploy.deployables`  
`dockerDirectory` | The directory containing the Dockerfile and other Docker resources. Default is `${basedir}/src/main/docker/`. | `app.stage.dockerDirectory`  
`imageUrl` | Deploy with a specific Docker image. `ImageUrl` must be a valid Artifact Registry name, for example, `docker.pkg.dev/foo`, where `foo` is the name of the image. | `app.deploy.imageUrl`  
`projectId` | The Google Cloud project name to use for this invocation. Default is the current project selected when [initializing `gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/init). | `app.deploy.projectId`  
`promote` | Promote the deployed version to receive all traffic. Default is `True`. | `app.deploy.promote`  
`server` | The App Engine server to connect to. Typically, you do not need to change this value. | `app.deploy.server`  
`stagingDirectory` | Required. The directory to which to stage the application. Default is `${project.build.directory}/appengine-staging`. | `app.stage.stagingDirectory`  
`stopPreviousVersion` | Stop the previously running version when deploying a new version that receives all traffic. | `app.deploy.stopPreviousVersion`  
`version` | The version of the app that will be created or replaced by this deployment. If you do not specify a version, one will be generated for you. | `app.deploy.version`  
  
## `appengine:help`

Displays help information on the App Engine Maven plugin. To display parameter details, call:
    
    
    mvn appengine:help -Ddetail=true -Dgoal=[GOAL_NAME]
    

You can use the following parameters:

Parameter | Description | User Property  
---|---|---  
`detail` | If true, display all settable properties for each goal. Default is `False`. | `detail`  
`goal` | The name of the goal for which to show help. If unspecified, all goals will be displayed. | `goal`  
`indentSize` | The number of spaces per indentation level. Should be a positive number. Default is `2`. | `indentSize`  
`lineLength` | The maximum length of a display line. Should be a positive number. Default is `80`. | `lineLength`  
  
## `appengine:stage`

Generates an application build directory for deployment.

You can use the following parameters:

Parameter | Description | User Property  
---|---|---  
`appEngineDirectory` | The directory that contains `app.yaml` and other supported App Engine configuration files. Default is `${basedir}/src/main/appengine`. | `app.stage.appEngineDirectory`  
`artifact` | The location of the JAR or WAR archive to deploy. Default is `${project.build.directory}/${project.build.finalName}.${project.packaging}`. | `app.stage.artifact`  
`cloudSdkPath` | Optional parameter to configure the location of the gcloud CLI. | `cloudSdkPath`  
`dockerDirectory` | The directory containing the Dockerfile and other Docker resources. Default is `${basedir}/src/main/docker/``${basedir}/src/main/docker/`. | `app.stage.dockerDirectory`  
`stagingDirectory` | Required. The directory to which to stage the application. Default is `${project.build.directory}/appengine-staging` | `app.stage.stagingDirectory`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
