---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/set-up-environment/
title: Setting up a development environment \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:18.312646+00:00
---

# Setting up a development environment  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/set-up-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Setting up a development environment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up your development environment to build and deploy your backend API using Cloud Endpoints Frameworks for the App Engine standard environment. This page uses the [Endpoints Frameworks version 2.0 skeleton](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java8/endpoints-v2-skeleton) code sample to explain the basic software and components you need to get started.

You might want to use the `endpoints-skeleton-archetype` or the `hello-endpoints-archetype` described in [Using Apache Maven and the App Engine plugin (Google Cloud CLI-based)](https://docs.cloud.google.com/endpoints/docs/frameworks/java/using-maven) to create a new Endpoints Frameworks version 2.0 project.

To get a better understanding of the steps required to deploy a sample API using Endpoints Frameworks, see the tutorial [Getting started with Endpoints Frameworks on App Engine](https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make a note of the Google Cloud project ID because it is needed later. 



## Installing and configuring required software

  1. If you don't have Java 8 installed, download the Java Development Kit (JDK) from [ Oracle's site](http://www.java.com/en/download/manual.jsp) and install it. 
  2. Install either Maven or Gradle: 

### Maven

     1. [ Download Apache Maven version 3.3.9 or greater](https://maven.apache.org/download.cgi)
     2. [Install](https://maven.apache.org/install) and [configure](https://maven.apache.org/configure.html) Maven for your local development environment. 

### Gradle

     * [Install Gradle](https://gradle.org/gradle-download/).

  3. [Download and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). 
  4. Run the following commands: 
     1. Make sure that the gcloud CLI is authorized to access your data and services on Google Cloud: 
            
            gcloud auth login

     2. Use application default credentials: 
            
            gcloud auth application-default login

     3. Install the Google Cloud SDK `app-engine-java` component: 
            
            gcloud components install app-engine-java

     4. Update to the latest version of the Google Cloud SDK and all components: 
            
            gcloud components update

  5. Create an App Engine application: 
     1. Set the default project to your Google Cloud project ID: 
            
            gcloud config set project YOUR_PROJECT_ID

Replace `YOUR_PROJECT_ID` with your Google Cloud project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

     2. Select the region where you want to create your App Engine application. See [App Engine locations](https://docs.cloud.google.com/appengine/docs/locations) for a list of regions. 
     3. Create an App Engine application. Replace `YOUR_PROJECT_ID` with your Google Cloud project ID and `YOUR_REGION` with the region that you want the App Engine application created in. 
            
            gcloud app create \
              --project=YOUR_PROJECT_ID \
              --region=YOUR_REGION




## Getting the Endpoints Frameworks skeleton sample

The Endpoints Frameworks version 2.0 skeleton sample contains the necessary build scripts for Maven and Gradle. It also contains the required files to get started creating your first API.

  1. Clone the sample repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples
         

  2. Change to the directory containing the Endpoints Frameworks skeleton sample:
         
         cd java-docs-samples/appengine-java8/endpoints-v2-skeleton/
         

The sample has the following directory structure:

![Endpoints Frameworks skeleton sample layout](https://docs.cloud.google.com/static/endpoints/docs/frameworks/java/images/endpoints-skeleton-file-structure.png)

     * `MyApi.java` contains an empty class that you can use to get started writing your API. See the [echo example](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java8/endpoints-v2-backend/src/main/java/com/example/echo) for sample code to help you get started.

     * [`web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java/config/webxml) is a standard file that is used to configure a [servlet](https://wikipedia.org/wiki/Java_servlet).

     * [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref) defines information that is required to deploy the API to the App Engine standard environment by using Java 8.

     * [`pom.xml`](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) contains project and configuration information used by Maven to build the project and deploy the API to App Engine.

     * [`build.gradle`](https://docs.gradle.org/current/userguide/tutorial_using_tasks.html) contains project and configuration information used by Gradle to build the project and deploy the API to App Engine.




## Configuring the build files

This section describes the Maven `pom.xml` and Gradle `build.gradle` files included in the sample code. Except for entering your Google Cloud project ID so that it can be used in the hostname, the build files are ready for you to get started creating your API.

### About the minimum configuration

This section describes the minimum configuration needed in your build file.

### Maven

**Minimum dependencies**

The following shows the minimum dependencies required in your `pom.xml` to get started:
    
    
    <dependencies>
      <!-- Compile/runtime dependencies -->
      <dependency>
        <groupId>com.google.endpoints</groupId>
        <artifactId>endpoints-framework</artifactId>
        <version>2.2.2</version>
      </dependency>
      <dependency>
        <groupId>com.google.appengine</groupId>
        <artifactId>appengine-api-1.0-sdk</artifactId>
        <version>2.0.23</version>
      </dependency>
      <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.1.0</version>
        <type>jar</type>
        <scope>provided</scope>
      </dependency>
      <dependency>
        <groupId>javax.inject</groupId>
        <artifactId>javax.inject</artifactId>
        <version>1</version>
      </dependency>
    </dependencies>

  * The `endpoints-framework` dependency contains the necessary classes for creating your API. 
  * You need the [App Engine Standard API SDK](https://docs.cloud.google.com/appengine/docs/standard) (`appengine-api-sdk`) to deploy your project to the App Engine standard environment.
  * The standard [ `javax.servlet`](https://docs.oracle.com/javaee/7/api/javax/servlet/Servlet.html) package is required to build a servlet. 
  * The standard [ `javax.inject`](https://docs.oracle.com/javaee/6/api/javax/inject/package-summary.html) package is required to support [ dependency injection.](https://wikipedia.org/wiki/Dependency_injection)



**Apply plugins**

The following plugins are applied to enable them:
    
    
    <build>
      <!-- for hot reload of the web application-->
      <outputDirectory>${project.build.directory}/${project.build.finalName}/WEB-INF/classes</outputDirectory>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-war-plugin</artifactId>
          <version>3.4.0</version>
          <configuration>
            <webResources>
              <resources>
                <directory>${basedir}/src/main/webapp/WEB-INF</directory>
                <filtering>true</filtering>
                <targetPath>WEB-INF</targetPath>
              </resources>
            </webResources>
          </configuration>
        </plugin>
        <plugin>
          <groupId>com.google.cloud.tools</groupId>
          <artifactId>appengine-maven-plugin</artifactId>
          <version>2.5.0</version>
          <configuration>
            <!-- deploy configuration -->
            <projectId>GCLOUD_CONFIG</projectId>
            <version>GCLOUD_CONFIG</version>
          </configuration>
        </plugin>
        <plugin>
          <groupId>com.google.cloud.tools</groupId>
          <artifactId>endpoints-framework-maven-plugin</artifactId>
          <version>2.1.0</version>
          <configuration>
            <!-- plugin configuration -->
            <!--
            You must replace YOUR_PROJECT_ID with your
            Google Cloud Project Id
          -->
            <hostname>YOUR_PROJECT_ID.appspot.com</hostname>
          </configuration>
        </plugin>
      </plugins>
    </build>

  * The `maven-war-plugin` extends the `java` plugin to add support for assembling a web application.
  * The [ `appengine-maven-plugin`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/using-maven) is required to run the API on App Engine. 
  * The [ `endpoints-framework-maven-plugin`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/maven-endpoints-frameworks-plugin) provides tasks and configurations to build Endpoints Frameworks projects.



### Gradle

**Plugin dependencies**

The following shows the plugins required to build your API:
    
    
    buildscript {
      repositories {
        mavenCentral()
      }
    
      dependencies {
        classpath 'com.google.cloud.tools:endpoints-framework-gradle-plugin:2.1.0'
        classpath 'com.google.cloud.tools:appengine-gradle-plugin:2.5.0'
      }
    }

  * The [ Endpoints Frameworks Gradle plugin](https://docs.cloud.google.com/endpoints/docs/frameworks/java/gradle-endpoints-frameworks-plugin) is used to generate an OpenAPI document and to generate client libraries.
  * You need the [ App Engine Gradle plugin](https://docs.cloud.google.com/appengine/docs/standard/java/tools/migrate-gradle) to deploy your project to App Engine.



**Apply plugins**

The following plugins are applied to enable them in your Gradle build script:
    
    
    apply plugin: 'java'
    apply plugin: 'war'
    apply plugin: 'com.google.cloud.tools.endpoints-framework-server'
    apply plugin: 'com.google.cloud.tools.appengine'

  * The `java` plugin adds Java-specific compilation and build steps to your project.
  * The `war` plugin extends the `java` plugin to add support for assembling a web application.
  * The `endpoints-framework-server` plugin provides server-side support to the Endpoints Frameworks Gradle plugin.
  * The `appengine` plugin is required to run the API on App Engine. 



**Project dependencies**

The following dependencies are used by the project:
    
    
    dependencies {
        compile 'com.google.endpoints:endpoints-framework:2.2.2'
        compile 'com.google.appengine:appengine-api-1.0-sdk:2.0.23'
    
        compile 'javax.inject:javax.inject:1'
        compileOnly 'javax.servlet:javax.servlet-api:3.1.0'
    }

  * The `endpoints-framework` dependency contains the necessary classes for creating your API. 
  * The [App Engine Standard API SDK](https://docs.cloud.google.com/appengine/docs/standard) (`appengine-api-sdk`) is needed to deploy your project to the App Engine standard environment.
  * The standard [ `javax.servlet`](https://docs.oracle.com/javaee/7/api/javax/servlet/Servlet.html) package is required to build a [ servlet](https://wikipedia.org/wiki/Java_servlet). 
  * The standard [ `javax.inject`](https://docs.oracle.com/javaee/6/api/javax/inject/package-summary.html) package is required to support [ dependency injection.](https://wikipedia.org/wiki/Dependency_injection)



### Defining the hostname for your service

Endpoints Frameworks uses DNS-compatible names to uniquely identify services. Because Google Cloud project IDs are guaranteed to be globally unique, you should use your Google Cloud project ID as part of your API's service name.

You must add your Google Cloud project ID to the build files to configure the hostname for your service. The hostname should be in the following format:

`YOUR_PROJECT_ID.appspot.com`

When you deploy the API to App Engine, a DNS entry with a name in the format `YOUR_PROJECT_ID.appspot.com` is created automatically. The hostname is both the name of the Cloud Endpoints service and the domain name that you use to send requests to your API.

### Maven
    
    
    <plugin>
      <groupId>com.google.cloud.tools</groupId>
      <artifactId>endpoints-framework-maven-plugin</artifactId>
      <version>2.1.0</version>
      <configuration>
        <!-- plugin configuration -->
        <!--
        You must replace YOUR_PROJECT_ID with your
        Google Cloud Project Id
      -->
        <hostname>YOUR_PROJECT_ID.appspot.com</hostname>
      </configuration>
    </plugin>

In the `hostname` field, replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

### Gradle
    
    
    // You must replace YOUR_PROJECT_ID with your Google Cloud Project Id
    def projectId = 'YOUR_PROJECT_ID'
    
    endpointsServer {
      // Endpoints Framework Plugin server-side configuration
      hostname = "${projectId}.appspot.com"
    }

Set the variable `projectID` to your Google Cloud project ID. For example: `def projectId = 'example-project-12345'`

## Configuring the Endpoints servlet

The Endpoints servlet handles incoming requests and forwards them to the backend service running on App Engine. The Endpoints servlet is required for your API to be [managed by Endpoints](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).

For more information about `web.xml`, see [The deployment descriptor: `web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java/config/webxml).
    
    
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
             http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
             version="3.1">
        <!-- Wrap the backend with Endpoints Frameworks v2. -->
        <servlet>
            <servlet-name>EndpointsServlet</servlet-name>
            <servlet-class>com.google.api.server.spi.EndpointsServlet</servlet-class>
            <init-param>
                <param-name>services</param-name>
                <param-value>com.example.skeleton.MyApi</param-value>
            </init-param>
        </servlet>
        <!-- Route API method requests to the backend. -->
        <servlet-mapping>
            <servlet-name>EndpointsServlet</servlet-name>
            <url-pattern>/_ah/api/*</url-pattern>
        </servlet-mapping>
    </web-app>

## Configuring your App Engine deployment

The `appengine-web.xml` file is used to define the App Engine standard environment configuration when the API is deployed. See [`appengine-web.xml` reference](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref) for more information.
    
    
    <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
        <runtime>java8</runtime>
        <threadsafe>true</threadsafe>
    
        <system-properties>
            <property name="java.util.logging.config.file" value="WEB-INF/logging.properties"/>
        </system-properties>
    </appengine-web-app>

## What's next

  * [Write and annotate your backend API code](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code).
  * [Learn more about annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations).
  * [Add API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).
  * [Deploy and test your API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy).
  * [Learn more about supported parameter and return types](https://docs.cloud.google.com/endpoints/docs/frameworks/java/parameter-and-return-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
