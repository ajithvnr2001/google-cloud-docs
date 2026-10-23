---
url: https://docs.cloud.google.com/java/docs/compile-native-images/
title: Compile native images \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:22.047408+00:00
---

# Compile native images  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/compile-native-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Compile native images Stay organized with collections  Save and categorize content based on your preferences. 

Using the Cloud Client Libraries for Java, you can compile applications as native images. This approach provides performance benefits to your application by leveraging ahead-of-time compilation to reduce the cold start-up time and memory footprint of your application.

## Client library versions

Make sure that you are using version 25.4.0 or later of the [Cloud Libraries Bill of Materials](https://docs.cloud.google.com/java/docs/bom) (`libraries-bom`) or that you are using client libraries published after May 2022.

Most users manage their client library versions using the `libraries-bom`. This is an easy way to check that the versions of all the client libraries in your project are compatible with each other and up-to-date.

For more information about applying the `libraries-bom` to your project on Maven and Gradle, see [Updating your project to use the BOM](https://docs.cloud.google.com/java/docs/bom#updating_your_project_to_use_the_bom).

## Supported libraries

The stable Google Cloud Client Libraries for Java listed in the [Supported APIs table](https://github.com/googleapis/google-cloud-java#supported-apis) support native image compilation.

## Before you begin

To use native image compilation with the desired Google Cloud Client Libraries for Java, follow these prerequisite steps:

  1. If you have not already, create a [Google Cloud Project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  2. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which allows you to run the sample with your project's credentials.

  3. After installing the Google Cloud CLI, log in with Application Default Credentials using the following command:
         
         gcloud auth application-default login
         

**Note:** Although authenticating with Application Default Credentials is convenient during development, we recommend [alternate methods of authentication](https://docs.cloud.google.com/docs/authentication/production) during production use.
  4. Install an appropriate JDK distribution such as [GraalVM](https://www.graalvm.org/latest/docs/getting-started/).

  5. Make sure that you installed the native image extension by running the following command:
         
         gu install native-image
         

  6. Verify that the default version of Java is set correctly by running `java -version` in a terminal. The output is similar to the following:
         
         java -version
         openjdk version "17.0.9" 2023-10-17
         OpenJDK Runtime Environment GraalVM CE 17.0.9+9.1 (build 17.0.9+9-jvmci-23.0-b22)
         OpenJDK 64-Bit Server VM GraalVM CE 17.0.9+9.1 (build 17.0.9+9-jvmci-23.0-b22, mixed mode, sharing)
         




## Build an application as a native image

The following instructions use the native build tools plugins to build an application as a native image.

### Maven setup instructions

  1. Copy and paste this text into your application's POM to use the native [Maven plugin](https://graalvm.github.io/native-build-tools/latest/index.html) to build the native image for the application. Be sure to replace MAIN_CLASS with the name of your main class and VERSION with the version of the native Maven plugin, such as `0.10.1`.
         
         <profiles>
             <profile>
                 <id>native</id>
                 <build>
                     <plugins>
                         <plugin>
                             <groupId>org.graalvm.buildtools</groupId>
                             <artifactId>native-maven-plugin</artifactId>
                             <version>VERSION</version>
                             <extensions>true</extensions>
                             <configuration>
                                 <mainClass>$MAIN_CLASS</mainClass>
                                 <buildArgs>
                                     <buildArg>--no-fallback</buildArg>
                                     <buildArg>--no-server</buildArg>
                                 </buildArgs>
                             </configuration>
                             <executions>
                                 <execution>
                                     <id>build-native</id>
                                     <goals>
                                         <goal>build</goal>
                                     </goals>
                                     <phase>package</phase>
                                 </execution>
                             </executions>
                         </plugin>
                     </plugins>
                 </build>
             </profile>
         </profiles>
         

  2. Run `mvn package -Pnative` to generate the native image in the `./target` folder.

  3. Run the application like you run any executable. For example, `./target/$IMAGE_NAME`. The plugin defaults to the artifact ID of the project.




### Gradle setup instructions

  1. Set the main class of your application by pasting the following text in your `build.gradle` file.
         
         application {
             mainClass.set('$MAIN_CLASS')
         }
         

  2. Add the native-gradle plugin as described in [Adding the plugin](https://graalvm.github.io/native-build-tools/latest/gradle-plugin.html#_adding_the_plugin).

  3. Call `./gradlew nativeCompile` to build the native image into the `./build/native/nativeCompile` directory.

  4. Run the application as an executable. For example, `./build/native/nativeCompile/$PROJECT_NAME`. With the plugin, the image name defaults to the project name.




## Common Issues

### SLF4J compatibility

If you are performing native image compilation on a client library with the [SLF4J](https://www.slf4j.org/) dependency, you may see the following built-time error.
    
    
    Fatal error: com.oracle.graal.pointsto.util.AnalysisError$ParsingError: Error encountered while parsing io.grpc.netty.shaded.io.netty.util.internal.SystemPropertyUtil.getBoolean(java.lang.String, boolean)
    Parsing context:
       at io.grpc.netty.shaded.io.netty.util.internal.SystemPropertyUtil.getBoolean(SystemPropertyUtil.java:96)
       at io.grpc.netty.shaded.io.netty.channel.epoll.Epoll.<clinit>(Epoll.java:33)
       at org.graalvm.nativeimage.pointsto/com.oracle.graal.pointsto.util.AnalysisError.parsingError(AnalysisError.java:153)
    ...
    java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:165)
    Caused by: com.oracle.graal.pointsto.constraints.UnsupportedFeatureException: No instances of org.slf4j.jul.JDK14LoggerAdapter are allowed in the image heap as this class should be initialized at image runtime. To see how this object got instantiated use --trace-object-instantiation=org.slf4j.jul.JDK14LoggerAdapter.
    

Add `--initialize-at-run-time=io.grpc.netty.shaded.io.netty` to your `META-INF/native-image/$GROUP_ID/$ARTIFACT_ID/native-image.properties` file to address this issue.

However, this configuration may incur a performance cost for the generated native image, depending on the code path your application follows.

Alternatively, consider using a different logging library such as [Flogger](https://google.github.io/flogger/) or the java.util.logging library.

## Questions

Please report any issues and questions related to Java native image compilation from the [GitHub issues page](https://github.com/googleapis/google-cloud-java/issues).

## What's next?

  * [Review the native image sample project using Secret Manager](https://github.com/googleapis/google-cloud-java/tree/main/java-samples/native-image-sample).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
