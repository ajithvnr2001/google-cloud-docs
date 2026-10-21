---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/java-deploy/
title: Java Deployment Options \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.007354+00:00
---

# Java Deployment Options  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/java-deploy/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Java Deployment Options

You have two choices for deploying a Java function:

  * From source. For a general discussion of this topic, see [Deploy a Cloud Function](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics).
  * From a pre-packaged JAR file.



## Deploy from source

Your function's source code must be in the usual place for Maven projects (`src/main/java`). The sample functions in this document are directly in `src/main/java`, with no package declaration in the `.java` source file. For non-trivial code, you would likely introduce a package. If that package is `com.example`, then your hierarchy would look like this:
    
    
    myfunction/
    ├─ pom.xml
    ├─ src
        ├─main
            ├─ java
                ├─ com
                    ├─ example
                        ├─ MyFunction.java
    

Use the following command to deploy an HTTP function:
    
    
    gcloud functions deploy $name --trigger-http --no-gen2 \
        --entry-point $function_class --runtime java17
    

Where:

  * `$name` is an arbitrary, descriptive name that will be the name of the function once deployed. `$name` can only contain letters, numbers, underscores, and hyphens.
  * `$function_class` is the fully qualified name of your class (for example, `com.example.MyFunction` or just `MyFunction` if you don't use a package).



Use the following command to deploy an event-driven function:
    
    
    gcloud functions deploy $name --no-gen2 --entry-point $function_class \
        --trigger-resource $resource_name \
        --trigger-event $event_name \
        --runtime java17
    

Where:

  * `$name` is an arbitrary, descriptive name that will be the name of the function once deployed.
  * `$function_class` is the fully qualified name of your class (for example, `com.example.MyFunction` or just `MyFunction` if you don't use a package).
  * `$resource_name` and `$event_name` are specific to the events that trigger your function. Examples of supported resources and events are [Google Cloud Pub/Sub](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) and [Google Cloud Storage](https://docs.cloud.google.com/functions/1stgendocs/calling/storage).

**Note:** For a more detailed discussion of deploying HTTP and event-driven functions, see [Deploy a Cloud Function](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics).

When deploying a function from source, the Google Cloud CLI uploads the source directory (and everything in it) to Google Cloud to build. To avoid sending unnecessary files, you can use the `.gcloudignore` [file](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore). Edit the `.gcloudignore` file to ignore common directories like `.git` and `target/`. For example, a `.gcloudignore` file might contain the following:
    
    
    .git
    target
    build
    .idea
    

## Deploy from a JAR

You can deploy a pre-built JAR that contains the function. This is useful especially if you need to deploy a function that uses dependencies from a private artifact repository that cannot be accessed from Google Cloud's build pipeline when building from source. The JAR can be an uber JAR that contains the function class and all of its dependency classes, or a thin JAR that has `Class-Path` entries for dependency JARs in the `META-INF/MANIFEST.MF` file.

### Build and deploy an Uber JAR

An uber JAR is a JAR file that contains the function classes as well as all of its dependencies. You can build an uber JAR with both Maven and Gradle. To deploy a Uber JAR, it must be the only JAR file in its own directory, for example:
    
    
    my-function-deployment/
     ├─ my-function-with-all-dependencies.jar
    

You can either copy the file into this directory structure, or use Maven and Gradle plugins to generate the correct deployment directory.

### Maven

Use the [Maven Shade plugin](https://maven.apache.org/plugins/maven-shade-plugin/) to build an uber JAR. Configure your `pom.xml` with Shade plugin:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <project ...>
      ...
      <build>
        ...
        <plugins>
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <executions>
              <execution>
                <phase>package</phase>
                <goals><goal>shade</goal></goals>
                <configuration>
                  <outputFile>${project.build.directory}/deployment/${build.finalName}.jar</outputFile>
                  <transformers>
                    <!-- This may be needed if you need to shade a signed JAR -->
                    <transformer implementation="org.apache.maven.plugins.shade.resource.DontIncludeResourceTransformer">
                      <resource>.SF</resource>
                      <resource>.DSA</resource>
                      <resource>.RSA</resource>
                    </transformer>
                    <!-- This is needed if you have dependencies that use Service Loader. Most Google Cloud client libraries does. -->
                    <transformer implementation=
           "org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                  </transformers>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </project>
    

**Note:** Some libraries (including Google Cloud Java client libraries) may use [Service Loader](https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html) to configure runtime service implementation classes. It's important to use Shade with the `ServicesResourceTransformer` to retain services information in the final JAR package's `META-INF/services` directory. Instead of Shade, you can also use [Maven Assembly Plugin](http://maven.apache.org/plugins/maven-assembly-plugin/usage.html).

Build the uber JAR:
    
    
    mvn package

Then deploy with the following command:
    
    
    gcloud functions deploy jar-example \
        --entry-point=Example \
        --no-gen2 \
        --runtime=java17 \
        --trigger-http \
        --source=target/deployment
    

### Gradle

Use the [Shadow plugin](https://imperceptiblethoughts.com/shadow/) for Gradle. Setup the plugin in your `build.gradle` file:
    
    
    buildscript {
       repositories {
           jcenter()
       }
       dependencies {
           ...
           classpath "com.github.jengelman.gradle.plugins:shadow:5.2.0"
       }
    }
    
    plugins {
       id 'java'
       ...
    }
    sourceCompatibility = '17.0'
    targetCompatibility = '17.0'
    apply plugin: 'com.github.johnrengelman.shadow'
    
    shadowJar {
       mergeServiceFiles()
    }
    ...
    

Now you can run Gradle with the `shadowJar` command:
    
    
    gradle shadowJar
    

Then deploy with the following command:
    
    
    gcloud functions deploy jar-example \
       --entry-point=Example \
       --no-gen2 \
       --runtime=java17 \
       --trigger-http \
       --source=build/libs
    

### Build and deploy a thin JAR with external dependencies

You can build and deploy a thin JAR file rather than an uber JAR. A thin JAR is a JAR file that contains only the function classes without the dependencies embedded in the same JAR file. Because the dependencies are still needed for deployment, you need to set things up as follows:

  * The dependencies must be in a subdirectory relative to the JAR to be deployed.
  * The JAR must have a `META-INF/MANIFEST.MF` file that includes a `Class-Path` attribute whose value lists the required dependency paths.



For example, your JAR file my-function.jar has a `META-INF/MANIFEST.MF` file that has 2 dependencies in the `libs/` directory (a space-separated list of relative paths):
    
    
    Manifest-Version: 1.0
    Class-Path: libs/dep1.jar libs/dep2.jar
    

Your deployment directory should then contain your main function JAR file, as well as a subdirectory with the two dependencies your function depends on:
    
    
    function-deployment/
    ├─ my-function.jar
    ├─ libs
           ├─ dep1.jar
           ├─ dep2.jar
    

You can build a thin JAR with both Maven and Gradle:

### Maven

Use Maven JAR plugin to automatically configure `MANIFEST.MF` with the paths to the dependencies, and then use the [Maven Dependency plugin](https://maven.apache.org/plugins/maven-dependency-plugin/usage.html#dependency:copy-dependencies) to copy the dependencies.
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <project ...>
      ...
      <build>
        ...
        <plugins>
          <plugin>
            <artifactId>maven-jar-plugin</artifactId>
            <configuration>
              <archive>
                <manifest>
                  <addClasspath>true</addClasspath>
                  <classpathPrefix>libs/</classpathPrefix>
                </manifest>
              </archive>
            </configuration>
          </plugin>
          <plugin>
            <artifactId>maven-dependency-plugin</artifactId>
            <executions>
              <execution>
                <phase>package</phase>
                <goals>
                  <goal>copy-dependencies</goal>
                </goals>
                <configuration>
                  <overWriteReleases>false</overWriteReleases>
                  <includeScope>runtime</includeScope>
                  <outputDirectory>${project.build.directory}/libs</outputDirectory>
                </configuration>
              </execution>
            </executions>
          </plugin>
          <plugin>
            <artifactId>maven-resources-plugin</artifactId>
            <executions>
              <execution>
                <id>copy-resources</id>
                <phase>package</phase>
                <goals><goal>copy-resources</goal></goals>
                <configuration>
                  <outputDirectory>${project.build.directory}/deployment</outputDirectory>
                  <resources>
                    <resource>
                      <directory>${project.build.directory}</directory>
                      <includes>
                        <include>${build.finalName}.jar</include>
                        <include>libs/**</include>
                      </includes>
                      <filtering>false</filtering>
                    </resource>
                  </resources>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </project>
    

Build the thin JAR:
    
    
    mvn package

Then deploy with the following command:
    
    
    gcloud functions deploy jar-example \
        --entry-point=Example \
        --no-gen2 \
        --runtime=java17 \
        --trigger-http \
        --source=target/deployment
    

### Gradle

Update your `build.gradle` project file to add a new task to fetch the dependencies:
    
    
    dependencies {
       // API available at compilation only, but provided at runtime
       compileOnly 'com.google.cloud.functions:functions-framework-api:1.0.1'
       // dependencies needed by the function
       // ...
    }
    
    jar {
     manifest {
       attributes(
         "Class-Path": provider {
             configurations.runtimeClasspath
               .collect { "libs/${it.name}" }.join(' ')
         }
       )
     }
    }
    
    task prepareDeployment(type: Copy) {
     into("${buildDir}/deployment")
     into('.') {
       from jar
     }
     into('libs') {
       from configurations.runtimeClasspath
     }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


