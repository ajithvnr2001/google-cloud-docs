---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-notification/latest/overview/
title: google-cloud-notification overview (0.217.0-beta) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:51.089911+00:00
---

# google-cloud-notification overview (0.217.0-beta)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-notification/latest/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  google-cloud-notification overview (0.217.0-beta) Stay organized with collections  Save and categorize content based on your preferences. 

0.217.0-beta (latest)  0.213.0-beta  0.212.0-beta  0.211.0-beta  0.209.0-beta  0.206.0-beta  0.205.0-beta  0.203.0-beta  0.201.0-beta  0.200.0-beta  0.198.0-beta  0.196.0-beta  0.194.0-beta  0.193.0-beta  0.192.0-beta  0.191.0-beta  0.190.0-beta  0.188.0-beta  0.186.0-beta  0.185.0-beta  0.182.0-beta  0.181.0-beta  0.180.0-beta  0.178.0-beta  0.177.0-beta  0.176.0-beta  0.175.0-beta  0.174.0-beta  0.173.0-beta  0.172.0-beta  0.171.0-beta  0.170.0-beta  0.169.0-beta  0.167.0-beta  0.166.0-beta  0.165.0-beta  0.164.0-beta  0.163.0-beta  0.162.0-beta  0.161.0-beta  0.160.0-beta  0.159.0-beta  0.158.0-beta  0.157.0-beta  0.155.0-beta  0.154.0-beta  0.153.0-beta  0.152.0-beta  0.151.0-beta  0.150.0-beta  0.149.0-beta  0.148.0-beta  0.147.0-beta  0.146.0-beta  0.145.0-beta  0.142.0-beta  0.141.0-beta  0.140.0-beta  0.139.0-beta  0.138.0-beta  0.137.0-beta  0.136.0-beta  0.135.0-beta  0.134.0-beta  0.133.0-beta  0.132.0-beta  0.131.0-beta  0.130.0-beta  0.129.0-beta  0.127.0-beta  0.126.0-beta  0.125.0-beta  0.124.0-beta  0.123.21-beta  0.122.29-beta 

## Key Reference Links

**Google Cloud Pub/Sub Notifications for GCS Description:** null

[Google Cloud Pub/Sub Notifications for GCS Product Reference](https://docs.cloud.google.com/java/docs/reference/google-cloud-notification/latest/null) | [GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-notification) | [Maven artifact](https://central.sonatype.com/artifact/com.google.cloud/google-cloud-notification)  
---|---|---  
  
## Getting Started

In order to use this library, you first need to go through the following steps:

  * [Install a JDK (Java Development Kit)](https://cloud.google.com/java/docs/setup#install_a_jdk_java_development_kit)
  * [Select or create a Cloud Platform project](https://console.cloud.google.com/project)
  * [Enable billing for your project](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
  * [Enable the API](https://console.cloud.google.com/apis/library/notification.googleapis.com)
  * [Set up authentication](https://cloud.google.com/docs/authentication/client-libraries)



## Use the Google Cloud Pub/Sub Notifications for GCS for Java

To ensure that your project uses compatible versions of the libraries and their component artifacts, import `com.google.cloud:libraries-bom` and use the BOM to specify dependency versions. Be sure to remove any versions that you set previously. For more information about BOMs, see [Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).

### Maven

Import the BOM in the `dependencyManagement` section of your `pom.xml` file. Include specific artifacts you depend on in the `dependencies` section, but don't specify the artifacts' versions in the `dependencies` section.

The example below demonstrates how you would import the BOM and include the `google-cloud-notification` artifact.
    
    
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
       <artifactId>google-cloud-notification</artifactId>
     </dependency>
    </dependencies>

### Gradle

BOMs are supported by default in Gradle 5.x or later. Add a `platform` dependency on `com.google.cloud:libraries-bom` and remove the version from the dependency declarations in the artifact's `build.gradle` file.

The example below demonstrates how you would import the BOM and include the `google-cloud-notification` artifact.
    
    
    implementation(platform("com.google.cloud:libraries-bom:26.90.0"))
    implementation("com.google.cloud:google-cloud-notification")

The `platform` and `enforcedPlatform` keywords supply dependency versions declared in a BOM. The `enforcedPlatform` keyword enforces the dependency versions declared in the BOM and thus overrides what you specified.

For more details of the `platform` and `enforcedPlatform` keywords Gradle 5.x or higher, see [Gradle: Importing Maven BOMs](https://docs.gradle.org/current/userguide/platforms.html#sub:bom_import).

If you're using Gradle 4.6 or later, add `enableFeaturePreview('IMPROVED_POM_SUPPORT')` to your `settings.gradle` file. For details, see [Gradle 4.6 Release Notes: BOM import](https://docs.gradle.org/4.6/release-notes.html#bom-import). Versions of Gradle earlier than 4.6 don't support BOMs.

### SBT

SBT [doesn't support BOMs](https://github.com/sbt/sbt/issues/4531). You can find recommended versions of libraries from a particular BOM version on the [dashboard](https://storage.googleapis.com/cloud-opensource-java-dashboard/com.google.cloud/libraries-bom/index.html) and set the versions manually. To use the latest version of this library, add this to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-notification" % "0.217.0-beta"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
