---
url: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/overview/
title: google-auth-library overview (1.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:22.637579+00:00
---

# google-auth-library overview (1.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  google-auth-library overview (1.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.54.0 (latest)  1.50.0  1.49.0  1.48.0  1.46.0  1.43.0  1.42.1  1.41.0  1.40.0  1.39.1  1.38.0  1.37.1  1.36.0  1.35.0  1.34.0  1.33.1  1.32.1  1.31.0  1.30.1  1.29.1-SNAPSHOT  1.28.0  1.27.0  1.26.0  1.25.0  1.24.1  1.20.0  1.19.0  1.18.0  1.7.0  1.6.1  1.4.0  1.3.0 

## Key Reference Links

**Google Auth Library Description:** null

[Google Auth Library Product Reference](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/null) | [GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/google-cloud-java) | [Maven artifact](https://central.sonatype.com/artifact/com.google.auth/google-auth-library)  
---|---|---  
  
## Getting Started

In order to use this library, you first need to go through the following steps:

  * [Install a JDK (Java Development Kit)](https://cloud.google.com/java/docs/setup#install_a_jdk_java_development_kit)
  * [Select or create a Cloud Platform project](https://console.cloud.google.com/project)
  * [Enable billing for your project](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
  * [Enable the API](https://console.cloud.google.com/apis/library/google-auth-library.googleapis.com)
  * [Set up authentication](https://cloud.google.com/docs/authentication/client-libraries)



## Use the Google Auth Library for Java

To ensure that your project uses compatible versions of the libraries and their component artifacts, import `com.google.cloud:libraries-bom` and use the BOM to specify dependency versions. Be sure to remove any versions that you set previously. For more information about BOMs, see [Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).

### Maven

Import the BOM in the `dependencyManagement` section of your `pom.xml` file. Include specific artifacts you depend on in the `dependencies` section, but don't specify the artifacts' versions in the `dependencies` section.

The example below demonstrates how you would import the BOM and include the `google-auth-library` artifact.
    
    
    <dependencyManagement>
     <dependencies>
       <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
       </dependency>
     </dependencies>
    </dependencyManagement>
    
    <dependencies>
     <dependency>
       <groupId>com.google.cloud</groupId>
       <artifactId>google-auth-library</artifactId>
     </dependency>
    </dependencies>

### Gradle

BOMs are supported by default in Gradle 5.x or later. Add a `platform` dependency on `com.google.cloud:libraries-bom` and remove the version from the dependency declarations in the artifact's `build.gradle` file.

The example below demonstrates how you would import the BOM and include the `google-auth-library` artifact.
    
    
    implementation(platform("com.google.cloud:libraries-bom:26.90.0"))
    implementation("com.google.auth:google-auth-library")

The `platform` and `enforcedPlatform` keywords supply dependency versions declared in a BOM. The `enforcedPlatform` keyword enforces the dependency versions declared in the BOM and thus overrides what you specified.

For more details of the `platform` and `enforcedPlatform` keywords Gradle 5.x or higher, see [Gradle: Importing Maven BOMs](https://docs.gradle.org/current/userguide/platforms.html#sub:bom_import).

If you're using Gradle 4.6 or later, add `enableFeaturePreview('IMPROVED_POM_SUPPORT')` to your `settings.gradle` file. For details, see [Gradle 4.6 Release Notes: BOM import](https://docs.gradle.org/4.6/release-notes.html#bom-import). Versions of Gradle earlier than 4.6 don't support BOMs.

### SBT

SBT [doesn't support BOMs](https://github.com/sbt/sbt/issues/4531). You can find recommended versions of libraries from a particular BOM version on the [dashboard](https://storage.googleapis.com/cloud-opensource-java-dashboard/com.google.cloud/libraries-bom/index.html) and set the versions manually. To use the latest version of this library, add this to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-auth-library" % "1.54.0"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
