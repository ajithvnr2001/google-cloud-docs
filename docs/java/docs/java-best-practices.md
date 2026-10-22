---
url: https://docs.cloud.google.com/java/docs/java-best-practices/
title: Java best practices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:52.597773+00:00
---

# Java best practices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/java-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Java best practices Stay organized with collections  Save and categorize content based on your preferences. 

Keeping your applications current has become important and difficult. This document provides some basic steps for Java developers to get started with DevOps practices. It is by no means an exhaustive list. Most of these ideas come from the [DORA DevOps research and assessment](https://dora.dev/) studies which provide a fuller overview of best practices. Other sources include [_Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations_](https://itrevolution.com/accelerate-book/) by _Nicole Forsgren PhD_ , _Jez Humble_ , and _Gene Kim_ ; and [_Software Engineering at Google_](https://abseil.io/resources/swe-book) curated by _Titus Winters_ , _Tom Manshreck_ and _Hyrum Wright_.

Before reading this page it's recommended that you read: [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

Every development organization's needs are unique, but a basic system could be constructed using one of the following tech stacks:

Sample Tech Stack 1 | Sample Tech Stack 2  
---|---  
  
  * Cloud Source Repositories, GitHub, or Bitbucket for source code.
  * Whitesource RenovateBot for keeping artifacts and libraries up to date. 
  * Cloud Build for unit / presubmit testing
  * Cloud Build for integration testing
  * Cloud Deploy for deployment

| 

  * GitHub for source code.
  * GitHub Dependabot for keeping artifacts and libraries up to date.
  * GitHub Actions for presubmit testing
  * GitHub Actions for integration testing
  * GitHub Actions for deployment

  
  
A system built with these components can allow you to improve quality and cycle time. It can also allow you to keep your code up to date with the latest bug fixes and security updates.

## Version Control

Research ([page 17](https://services.google.com/fh/files/misc/state-of-devops-2014.pdf) , [page 14](https://services.google.com/fh/files/misc/state-of-devops-2015.pdf) , [page 31](https://services.google.com/fh/files/misc/state-of-devops-2016.pdf) , and [page 60](https://services.google.com/fh/files/misc/state-of-devops-2018.pdf)) has found that [version control](https://dora.dev/devops-capabilities/technical/version-control/) for source code combined with automation and testing predicts improved quality and many other benefits.

  * [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories) [[Quickstart](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)] provide a free [Git](https://git-scm.com/) workflow for your source code.
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry) [[Containers](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images)] [[Java Packages](https://docs.cloud.google.com/artifact-registry/docs/java/store-java)] is a great place to keep your built Java artifacts.



[GitHub](https://github.com/), [Gitlab](https://about.gitlab.com/), and [Bitbucket](https://bitbucket.org/) are also good homes for your source code.

## Automated Testing

[Test automation](https://dora.dev/devops-capabilities/technical/test-automation/) can be critical to your success using most of these techniques. For additional thoughts about testing best practices, take a look at the [SRE Book chapter Testing for Reliability](https://sre.google/sre-book/testing-reliability/) and the [Google Testing blog](https://testing.googleblog.com/).

Java developers are mostly concerned with automated unit tests and integration testing. [JUnit](https://junit.org/junit5/), [Testing with Spring](https://docs.spring.io/spring-framework/docs/current/reference/html/testing.html), [Apache Maven Surefire](https://maven.apache.org/surefire/index.html), and [Gradle Java testing](https://docs.gradle.org/current/userguide/java_testing.html) are useful resources for Java developers.

## Continuous Integration / Deployment Automation

[Continuous integration](https://dora.dev/devops-capabilities/technical/continuous-integration/) and [Deployment automation](https://dora.dev/devops-capabilities/technical/deployment-automation/) power modern DevOps jobs. Build, Test, and Deploy.

  * [Cloud Build](https://docs.cloud.google.com/build) [[Quickstarts](https://docs.cloud.google.com/build/docs/quickstarts)] [[Java Specific](https://docs.cloud.google.com/build/docs/building/build-java)] [[Deployment](https://docs.cloud.google.com/build/docs/how-to#deploy)] [[Trigger](https://docs.cloud.google.com/build/docs/how-to#trigger)] provides a [free](https://docs.cloud.google.com/build/pricing) (120 build minutes / day) or low cost easy-to-use build system that can be easily customized for most jobs.
  * [Tekton](https://tekton.dev/) is an open source project that lets you adapt the Cloud Build ideas to your systems.
  * [Spinnaker](https://spinnaker.io/) is an open-source, multi-cloud continuous delivery platform that helps you release software changes with high velocity and confidence. It helps you manage the process of releasing and rolling back complex software systems.
  * [GitHub's Actions](https://github.com/features/actions) is a third-party solution that lets you set up tests and run them on GitHub.
  * There are also many other solutions such as [Gitlab](https://about.gitlab.com/), [Circle CI](https://circleci.com/), and [Travis CI](https://travis-ci.org/).



## Cloud Client Libraries

There are many ways of using Google services, but the preferred way is to follow the instructions on the [Cloud Client Libraries](https://docs.cloud.google.com/java/docs/setup#install_the_gcp_client_library_for_java) page. For Java, the [Libraries-BOM](https://github.com/GoogleCloudPlatform/cloud-opensource-java/wiki/The-Google-Cloud-Platform-Libraries-BOM) can help ensure that you're using compatible versions of each artifact.

If you choose to pick your own versions of client libraries, it is possible that an incompatible artifact might get selected. This is known as the [diamond dependency problem](https://jlbp.dev/why-doesnt-the-compiler-catch-diamond-dependency-conficts). If you still must pick your individual libraries, then update them one at a time and test to see if the update introduced an error. The latest versions are always listed on this [page](https://github.com/googleapis/google-cloud-java#google-cloud-java-client-libraries), or can be found by searching [Maven-Central](https://search.maven.org/search?q=g:com.google.cloud).

## Keep dependencies current

To protect against malicious actors, it's critical that you keep your dependencies up to date. There are many third party tools that help you with this:

  * [GitHub's DependaBot](https://dependabot.com/)
  * [Whitesource RenovateBot](https://www.whitesourcesoftware.com/free-developer-tools/renovate/)
  * [Snyk](https://snyk.io/)



These tools, when configured properly, help you keep your dependencies up to date. When you combine automated testing and Continuous Integration / Continuous Deployment the flow becomes:

  * Dependency automation proposes a change to your source control.
  * The continuous build system builds and tests the change.
  * A human reviews the proposal, and if acceptable, accepts the change, possibly along with other changes.
  * After changes are accepted, a proposal is made to the Continuous Delivery system to release the code to production. (Or your custom process is followed.)



## Use a supported Java Runtime Environment (JRE)

The JRE, a subset of the Java Development Kit, sits on top of your operating system and provides the software and resources required to run a Java application. Most users prefer to use the latest [LTS version](https://en.wikipedia.org/wiki/Java_version_history) in production so that they have access to updates, security, and bug fixes. It is usually possible to update to a later JRE even if your code is compiled against an earlier JDK.

**Important:** There are a few cases where using a different JRE will break, most commonly when you're using a Java Application Server that requires a specific version.

If you work with multiple JDK versions, [SDKMAN!](https://sdkman.io/) can helps you use and manage different JDK versions.

### Using containers (Google Kubernetes Engine, Cloud Run, GKE clusters)

If you're using Docker containers with either RenovateBot or DependaBot, the bot periodically proposes updates to your JRE and your JDK – you'll want to keep the JDK and the JRE on the same version.

If you manually update your Dockerfile, just change the JRE to latest and rebuild.

### Using Compute Engine

This tends to be very application specific. We [recommend using a startup script](https://docs.cloud.google.com/java/getting-started/getting-started-on-compute-engine). To upgrade, you should update the script.

### App Engine flexible environment

[Supports Java 8](https://docs.cloud.google.com/appengine/docs/flexible/java/dev-java-only) only.

### App Engine Standard

See [Migrating your App Engine app from Java 8 to Java 11.](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/java-differences)

## Use a LTS version of the Java Development Kit

The JDK is a set of tools for developing Java applications. New language features are tied to a particular JDK. We recommend you pin your usage to a JDK with Long Term Support (LTS), upgrading to the next LTS version when it's appropriate for your application. We recommend that you use the latest minor release of the pinned major LTS release.

Most users will want to keep the JDK and JRE in sync. Sometimes that isn't possible (for example when the JDK is no longer supported), and you need to compile with a later JDK and run on an earlier JRE.

To do this with Maven:

Set the language level you want to code in and the target JRE. Update your `pom.xml` file as follows (for Java 8): `xml <maven.compiler.source>1.8</maven.compiler.source> <maven.compiler.target>1.8</maven.compiler.target>`

To update to Java 11 you would change it to:
    
    
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    

If you're using Gradle, then update your `build.gradle` file for Java 8 with:
    
    
    compileJava {
      sourceCompatibility = 1.8
      targetCompatibility = 1.8
    }
    

Or for Java 11:
    
    
    compileJava {
      sourceCompatibility = 11
      targetCompatibility = 11
    }
    

Note that for Java 8 and earlier the versions had a `1.` prefix (`1.7` for Java 7, `1.8` for Java 8) that was dropped after Java 8.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
