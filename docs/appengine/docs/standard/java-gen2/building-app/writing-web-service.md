---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/writing-web-service/
title: Write your web service \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:29.620108+00:00
---

# Write your web service  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/writing-web-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Write your web service Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Java web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-java-service).

This guide shows how to write a Java web service to run in the App Engine standard environment. To learn more about the Java runtime and how it works, see [Java Runtime Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime).

## Before you begin

If you haven't already:

  1. [Install the latest version of the Java Development Kit (JDK)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) for the App Engine runtime version you plan to use.
  2. [Download](https://maven.apache.org/download.cgi) and [install](https://maven.apache.org/install.html) Apache Maven to build, run, and deploy the sample app.



## Key points

  * App Engine starts your application by uploading an executable JAR application.
  * Your application must have a main class that starts a web server which responds to HTTP requests on the port specified by the PORT environment variable, typically 8080.
  * You need an [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/configuring-your-app-with-app-yaml) file to deploy your service to App Engine.
  * You can use dependencies by listing them in your [`pom.xml`](https://maven.apache.org/pom.html) file. For more information, see [Using Java libraries](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/specifying-dependencies).



## Create a main class

The core of your web service is the HTTP server. The sample code in this guide uses the [Spring Boot](https://spring.io/) framework to handle HTTP requests, but you are free to use a web framework of your choice.

  1. Generate a Spring Boot project for Java that uses the Maven build system and contains the Spring Web dependency. To get started, click the following link:

[Go to Spring Initializr](https://start.spring.io/#!type=maven-project&language=java&packaging=jar&jvmVersion=21&groupId=com.example.appengine&artifactId=springboot&packageName=com.example.appengine.springboot&dependencies=web)

  2. In Spring Initializer, click the **Generate** button to generate and download your project.

  3. In the downloaded project, edit the file `springboot/src/main/java/com/example/appengine/springboot/DemoApplication.java` to add some java imports and a REST hello handler:
         
         package com.example.appengine.springboot;
         import org.springframework.boot.SpringApplication;
         import org.springframework.boot.autoconfigure.SpringBootApplication;
         import org.springframework.web.bind.annotation.GetMapping;
         import org.springframework.web.bind.annotation.RestController;
         @SpringBootApplication
         @RestController
         public class DemoApplication {
         public static void main(String[] args) {
         SpringApplication.run(DemoApplication.class, args);
         }
         @GetMapping("/")
         public String hello() {
         return "Hello world!";
         }
         }
         

The modified class is a controller that starts Spring Boot's embedded Tomcat server and responds to `GET` requests at the root path (`'/'`) with the text "Hello world!"




## Run the server locally

To run the server locally:

  1. Start a local web server using the Spring Boot Maven plugin.
         
         mvn spring-boot:run
         

  2. In your web browser, enter the following address:  
<http://localhost:8080>




The **Hello World** message from the sample app displays on the page. In your terminal window, press **Ctrl+C** to exit the web server.

## Create the `app.yaml` file

To specify settings for your app in the App Engine runtime environment:

  1. Create a file named `app.yaml` in the following directory:  
`springboot/src/main/appengine/`

  2. Add the following contents to the file:

### Java 21
         
         runtime: java21
         

The `app.yaml` file can also specify network settings, scaling settings, and more. For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).




If you used the _Spring Initializr_ link above, you should now have a file structure like the following:

  * `springboot/`
    * `pom.xml`
    * `src/main/`
      * `appengine/`
        * `app.yaml`
      * `java/com/example/appengine/springboot/`
        * `DemoApplication.java`



You can also add in the project pom.xml the Maven plugin that allows deployment of the application:
    
    
                <plugin>
                    <groupId>com.google.cloud.tools</groupId>
                    <artifactId>appengine-maven-plugin</artifactId>
                    <version>2.8.1</version>
                    <configuration>
                        <projectId>YOUR_PROJECT_NAME</projectId>
                        <version>YOUR_VERSION</version>
                        <promote>false</promote>
                    </configuration>
                </plugin>
    

## Next steps

Now that you've created a simple Java web server that listens to the correct port and you've specified the runtime in an `app.yaml` file, you're ready to [deploy your service on App Engine](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/deploying-web-service).

[ Previous arrow_back  Create your project  ](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/creating-project)

[ Next Deploy your web service  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/deploying-web-service)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
