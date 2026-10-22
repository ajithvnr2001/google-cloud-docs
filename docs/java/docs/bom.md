---
url: https://docs.cloud.google.com/java/docs/bom/
title: Use Bill of Materials (BOM) with Cloud Client Libraries for Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:52.158120+00:00
---

# Use Bill of Materials (BOM) with Cloud Client Libraries for Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/bom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Use Bill of Materials (BOM) with Cloud Client Libraries for Java Stay organized with collections  Save and categorize content based on your preferences. 

To make sure that your projects have compatible versions of Cloud Client Libraries, use the versions specified in the Google Cloud Libraries Bill of Materials (BOM). The libraries in the BOM don't have dependency conflicts that would manifest as `NoSuchMethodError` or `NoClassDefFoundError`.

The BOM is necessary because Google publishes over two hundred open source Java libraries that make it easier to use services in Google Cloud. The Google Cloud libraries depend on several foundational libraries that can be used for general purposes.

These recommendations apply to the components of the following libraries:

  * [guava](https://github.com/google/guava)
  * [protobuf](https://github.com/protocolbuffers/protobuf)
  * [grpc-java](https://github.com/grpc/grpc-java)
  * [google-http-java-client](https://github.com/googleapis/google-http-java-client)



## Updating your project to use the BOM

To make sure that your projects uses compatible versions of the libraries and their component artifacts, import `com.google.cloud:libraries-bom` and use the BOM to specify dependency versions. Be sure to remove any versions that you set previously.

If you encounter compatibility issues with protobuf-java 4.x, update your codebase and dependencies to ensure compatibility, see release notes of [libraries-bom v26.50.0](https://github.com/googleapis/java-cloud-bom/releases/tag/v26.50.0) and [libraries-bom v26.75.0](https://github.com/googleapis/java-cloud-bom/releases/tag/v26.75.0) for potential compatibility issues.

### Maven

Import the BOM in the `dependencyManagement` section of your `pom.xml` file. Include specific artifacts you depend on in the `dependencies` section, but don't specify the artifacts' versions in the `dependencies` section. The example below demonstrates how you would import the BOM and include the `google-cloud-storage` artifact.
    
    
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
        <artifactId>google-cloud-storage</artifactId>
      </dependency>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage-control</artifactId>
      </dependency>
    </dependencies>

In this example, because the BOM manages library versions, the version of `google-cloud-storage` is omitted.

### Gradle

BOMs are supported by default in Gradle 5.x or later. Add a `platform` dependency on `com.google.cloud:libraries-bom` and remove the version from the dependency declarations in the artifact's `build.gradle` file.
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-storage'

The `platform` and `enforcedPlatform` keywords supply dependency versions declared in a BOM. The `enforcedPlatform` keyword enforces the dependency versions declared in the BOM and thus overrides what you specified. For more details of the `platform` and `enforcedPlatform` keywords Gradle 5.x or higher, see [Gradle: Importing Maven BOMs](https://docs.gradle.org/current/userguide/platforms.html#sub:bom_import).

If you're using Gradle 4.6 or later, add `enableFeaturePreview('IMPROVED_POM_SUPPORT')` to your `settings.gradle` file. For details, see [Gradle 4.6 Release Notes: BOM import](https://docs.gradle.org/4.6/release-notes.html#bom-import). Versions of Gradle earlier than 4.6 don't support BOMs.

### SBT

SBT [doesn't support BOMs](https://github.com/sbt/sbt/issues/4531). You can find recommended versions of libraries from a particular BOM version on the [dashboard](https://storage.googleapis.com/cloud-opensource-java-dashboard/com.google.cloud/libraries-bom/index.html) and set the versions manually.

### Bazel

Bazel [doesn't support BOMs](https://github.com/bazelbuild/rules_jvm_external/issues/229). You can find recommended versions of libraries from a particular BOM version on the [dashboard](https://storage.googleapis.com/cloud-opensource-java-dashboard/com.google.cloud/libraries-bom/index.html) and set the versions manually.

### Guava Versions `-jre` or `-android`

Since the release of version 21.0.0, the Libraries BOM includes Guava's `-jre` version (which supports Java 8+). The section below is not applicable for Java 8 users.

* * *

Google's Guava release contains two versions of artifacts: "-jre" and "-android" versions. The one with "-jre" (such as `com.google.guava:guava:31.1-jre`) is for Java 8 and supports lambda functions and streams. The other version with the "-android" suffix (such as `com.google.guava:guava:31.1-android`) is for Java 7 and Android development.

The Google Cloud Libraries BOM contains Guava with the "-android" version to make sure that the BOM works in Java 7. However, this means the version of Guava in the BOM doesn't have some methods that are intended for Java 8 lambda functions, such as `ImmutableList.toImmutableList()`.

If your project requires Java 8 or later and uses Guava classes such as `com.google.common.collect.Streams`, you should add a dependency on a JRE version of Guava.

In Maven:
    
    
      <dependencyManagement>
        <dependencies>
          <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>31.1-jre</version>  <!-- "-jre" for Java 8 or higher -->
          </dependency>
        </dependencies>
        <dependencies>
          <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            ...
      </dependencyManagement>
    

In Gradle:
    
    
    dependencies {
      constraints {
        implementation 'com.google.guava:guava:31.1-jre' // "-jre" for Java 8 or higher
      }
      implementation platform('com.google.cloud:libraries-bom:26.12.0')
      ...
    }
    

The previous sample doesn't work if you use `enforcedPlatform` because `enforcedPlatform` takes precedence over `constraints`. If you want to use `enforcedPlatform` with the Guava version, you can configure [`ResolutionStrategy`](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
