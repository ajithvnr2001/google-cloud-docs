---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-java/
title: Specify dependencies in Java \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.099623+00:00
---

# Specify dependencies in Java  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-java/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Specify dependencies in Java

You can use any Java compatible libraries with a [supported Java runtime](https://docs.cloud.google.com/functions/1stgendocs/runtime-support#java) to write Cloud Run functions in Java. You can use either [Maven](https://maven.apache.org/) or [Gradle](https://gradle.org/) to manage dependencies for your Java Cloud Run functions.

## Declaring and managing dependencies

You can declare and manage dependencies using either Maven or Gradle:

  * To manage dependencies using Maven:

    * Specify the dependencies in the `<dependencies>` section inside the [`pom.xml`](http://maven.apache.org/guides/introduction/introduction-to-the-pom.html) file of your project.

    * To manage your project's dependency on Maven itself, you can use the [Maven Wrapper](https://maven.apache.org/wrapper/). If you do not use the Maven Wrapper, Cloud Run functions defaults to using a recent version of Maven when running [`gcloud functions deploy`](https://sdk/gcloud/reference/functions/deploy).

  * To manage dependencies using Gradle, you specify the dependencies in the [`build.gradle`](https://docs.gradle.org/current/userguide/tutorial_using_tasks.html) file of your project.




The [Functions Framework](https://docs.cloud.google.com/functions/docs/functions-framework) is a required dependency for all functions. Although Cloud Run functions installs it on your behalf when the function is created, we recommend that you include it as an explicit dependency for clarity. 

If your function relies on private dependencies, we recommend that you mirror `functions-framework` to your private registry. Include the mirrored `functions-framework` as a dependency to your function to avoid installing the package from the public internet.

## Using the Google Cloud Client Libraries for Java

[Google Cloud Client Libraries for Java](https://github.com/googleapis/google-cloud-java) provide idiomatic access to Google Cloud services. To use a library, declare it as a dependency.

Typically you only declare dependencies on the specific libraries that your function needs. For example:

### Maven
    
    
    <project xmlns="http://maven.apache.org/POM/4.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
    
      <groupId>com.example.functions</groupId>
      <artifactId>functions-hello-world</artifactId>
      <version>1.0.0-SNAPSHOT</version>
      <properties>
        <maven.compiler.target>11</maven.compiler.target>
        <maven.compiler.source>11</maven.compiler.source>
      </properties>
    
      <dependencies>
        <!-- Required for Function primitives -->
        <dependency>
          <groupId>com.google.cloud.functions</groupId>
          <artifactId>functions-framework-api</artifactId>
          <version>1.1.0</version>
          <scope>provided</scope>
        </dependency>
      </dependencies>
    
      <build>
        <plugins>
          <plugin>
            <!--
              Google Cloud Functions Framework Maven plugin
    
              This plugin allows you to run Cloud Functions Java code
              locally. Use the following terminal command to run a
              given function locally:
    
              mvn function:run -Drun.functionTarget=your.package.yourFunction
            -->
            <groupId>com.google.cloud.functions</groupId>
            <artifactId>function-maven-plugin</artifactId>
            <version>0.11.0</version>
            <configuration>
              <functionTarget>functions.HelloWorld</functionTarget>
            </configuration>
          </plugin>
        </plugins>
      </build>
    </project>

### Gradle

Note that this `build.gradle` file includes a custom task to help you run functions locally. For more discussion of local testing, see [Your First Function: Java](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-java-1st-gen#building_and_testing_locally).
    
    
    apply plugin: 'java'
    
    repositories {
      jcenter()
      mavenCentral()
    }
    configurations {
        invoker
    }
    
    dependencies {
      // Every function needs this dependency to get the Functions Framework API.
      compileOnly 'com.google.cloud.functions:functions-framework-api:1.1.0'
    
      // To run function locally using Functions Framework's local invoker
      invoker 'com.google.cloud.functions.invoker:java-function-invoker:1.3.1'
    
      // These dependencies are only used by the tests.
      testImplementation 'com.google.cloud.functions:functions-framework-api:1.1.0'
      testImplementation 'junit:junit:4.13.2'
      testImplementation 'com.google.truth:truth:1.4.0'
      testImplementation 'org.mockito:mockito-core:5.10.0'
    
    }
    
    // Register a "runFunction" task to run the function locally
    tasks.register("runFunction", JavaExec) {
      main = 'com.google.cloud.functions.invoker.runner.Invoker'
      classpath(configurations.invoker)
      inputs.files(configurations.runtimeClasspath, sourceSets.main.output)
      args(
        '--target', project.findProperty('run.functionTarget') ?: '',
        '--port', project.findProperty('run.port') ?: 8080
      )
      doFirst {
        args('--classpath', files(configurations.runtimeClasspath, sourceSets.main.output).asPath)
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
