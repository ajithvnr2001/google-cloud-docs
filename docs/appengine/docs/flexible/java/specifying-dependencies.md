---
url: https://docs.cloud.google.com/appengine/docs/flexible/java/specifying-dependencies/
title: Specifying dependencies \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:09.911758+00:00
---

# Specifying dependencies  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/java/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specifying dependencies Stay organized with collections  Save and categorize content based on your preferences. 

You can use any Java compatible libraries with the Java runtime on the App Engine flexible environment. These instructions use Apache Maven to build, run, and deploy a sample app using a [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) Java runtime. For more information about using supported Java versions, see the [Java runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime).

For details about installing Maven, see [Using Apache Maven and the App Engine plugin](https://docs.cloud.google.com/appengine/docs/flexible/java/using-maven). 

## Declare and manage dependencies

To manage dependencies using Maven, you need to specify the dependencies in the `<dependencies>` section inside the [`pom.xml`](http://maven.apache.org/guides/introduction/introduction-to-the-pom.html) file of your project.

To manage your project's dependency on Maven itself, you can use the [Maven Wrapper](https://maven.apache.org/wrapper/). If you do not use the Maven Wrapper, App Engine defaults to using a recent version of Maven when running [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy).

## Specify the Java servlet library

Eclipse Jetty and Tomcat apps require the Java servlet library. Specify it in your `pom.xml` file's `<dependencies>` entry: 
    
    
    <dependency>
      <groupId>com.example.appengine</groupId>
      <artifactId>simple-jetty-main</artifactId>
      <version>1</version>
      <scope>provided</scope>
    </dependency>

Note that frameworks such as [SparkJava](http://sparkjava.com/) or [Spring Boot](http://projects.spring.io/spring-boot/) won't require the servlet library. 

## Use the Cloud Client Libraries

[Cloud Client Libraries for Java](https://github.com/googleapis/google-cloud-java) provide idiomatic access to Google Cloud services. To use a library, declare it as a dependency.

Typically, you only declare dependencies on the specific libraries that your app needs. For example, to use the Cloud Storage library: 
    
    
    <!--  Using libraries-bom to manage versions.
    See https://github.com/GoogleCloudPlatform/cloud-opensource-java/wiki/The-Google-Cloud-Platform-Libraries-BOM -->
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.28.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
      </dependency>
    </dependencies>

You can configure the Cloud Client Libraries for Java to [handle authentication automatically](https://docs.cloud.google.com/docs/authentication/client-libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
