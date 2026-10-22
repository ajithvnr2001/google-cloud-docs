---
url: https://docs.cloud.google.com/java/docs/troubleshooting/
title: Troubleshoot Cloud Client Libraries for Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:29.192809+00:00
---

# Troubleshoot Cloud Client Libraries for Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Troubleshoot Cloud Client Libraries for Java Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of logging and troubleshooting common issues with Cloud Client Libraries for Java.

## Logging

There are two ways to enable logging for the client libraries: using `java.util.logging`, or using Client Library Debug Logging with SLF4J.

### Using `java.util.logging`

Cloud Client Libraries for Java uses the Java logging API (`java.util.logging`) package. Configuring the logging level reveals information that helps you troubleshoot, including:

  * Timing of underlying client-server communication.
  * Request and response message headers.
  * Verbose messages in underlying dependency libraries.



To quickly enable verbose logging for Cloud Client Libraries for Java, create a file `logging.properties` with the following content:
    
    
    # run java program pointing to this properties file with the java arg
    #   -Djava.util.logging.config.file=path/to/logging.properties
    handlers=java.util.logging.ConsoleHandler
    java.util.logging.SimpleFormatter.format=%1$tF %1$tT,%1$tL %4$-8s %3$-50s - %5$s %6$s%n
    
    # --- ConsoleHandler ---
    java.util.logging.ConsoleHandler.level=ALL
    java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter
    .level=INFO
    
    # --- Specify logging level for certain packages ---
    # com.google.api is for HTTP 1.1 layer
    com.google.api.level=ALL
    # io.grpc is for gRPC + Netty layer
    io.grpc.level=FINE
    # com.google.auth is for authentication
    com.google.auth.level=FINE
    
    # Example when you specify the storage library's level. This works when
    # the target Cloud library uses the logging API.
    com.google.cloud.storage.level=INFO
    

Next, run your application with `-Djava.util.logging.config.file=path/to/logging.properties` as the `VM argument`, not the `Program argument`.

If you use IntelliJ, you specify the VM argument in **Run/Debug Configuration** :

![IntelliJ Run/Debug Configuration showing where to specify VM arguments](https://docs.cloud.google.com/static/java/docs/images/logging_vm_options.png)

If the JVM of your program is running with the configuration correctly, you see the FINE-level logging in your console.

Example output:
    
    
    2023-04-05 13:03:01,761 FINE     com.google.auth.oauth2.DefaultCredentialsProvider  - Attempting to load credentials from well known file: /usr/local/google/home/suztomo/.config/gcloud/application_default_credentials.json
    2023-04-05 13:03:01,847 FINE     io.grpc.ManagedChannelRegistry                     - Unable to find OkHttpChannelProvider
    java.lang.ClassNotFoundException: io.grpc.okhttp.OkHttpChannelProvider
        at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:581)
        at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:178)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:522)
        at java.base/java.lang.Class.forName0(Native Method)
        at java.base/java.lang.Class.forName(Class.java:315)
    ...
    

**Note:** You might see many stacktraces printed there. As long as the stacktraces are at the 'FINE' level, they are not errors.

This is one way to configure logging level. For more information about Java logging API usage, see [Java Logging Overview](https://docs.oracle.com/javase/8/docs/technotes/guides/logging/overview.html).

### Client Library Debug Logging (SLF4J)

Cloud Client Libraries comes with opt-in Debug Logging that can help you troubleshoot your application's integration with the API. When logging is activated, key events such as requests and responses, along with data payloads and metadata, such as headers, are logged to the standard error stream.

**WARNING:** Client Library Debug Logging includes your data payloads in plaintext, which could include sensitive data such as PII for yourself or your customers, private keys, or other security data that could be compromised if leaked. Always practice good data hygiene with your application logs, and follow the principle of least access. Google also recommends that client library debug logging be enabled only temporarily during active debugging, and not used permanently in production.

#### Prerequisite

Our libraries support debug logging using the [SLF4J](https://www.slf4j.org/) interface.

Client libraries and Libraries BOM does not include slf4j-api dependency. You will need to set up logging dependencies including SLF4J and corresponding logging implementations and configurations before turning on client library debug logging.

**NOTE** : You need to have SLF4J and corresponding logging providers, e.g., logback, log4j2, etc., in your classpath in order to use the client library debug logging feature; otherwise, no debug logging even if you enable it using environment variable.

#### Enable Logging with an environment variable

Debug logging is turned off by default. Debug logging is not turned on unless explicitly even if the prerequisites are met.

You can enable client library debug logging by setting the environment variable `GOOGLE_SDK_JAVA_LOGGING` to `true`, case insensitive. If unset or any other value, then client library debug logging is disabled.

#### Example logging setups

The documentation provides an example of debug logging using Logback.

Add Logback dependencies to your application, this will bring in slf4j dependency transitively. Users should refer to the [Logback setup](https://logback.qos.ch/setup.html) for latest versions. You can skip this step if your application already has logback dependencies in the classpath.

If you are using Maven:
    
    
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>LATEST_VERSION</version>
    </dependency>
    

Add the content to the logback configuration file if you want to see DEBUG level logs. You can skip this step if you only need INFO level logs. Refer to the [Logback configuration](https://logback.qos.ch/manual/configuration.html) for more information.
    
    
    <!-- set Client Library log level to DEBUG -->
    <logger name="com.google.api"  level="DEBUG"/>
    <!-- set Auth Library log level to DEBUG -->
    <logger name="com.google.auth" level="DEBUG"/>
    

## ALPN is not configured properly

If you see exceptions related to `ALPN is not configured properly`, such as:
    
    
    Caused by: java.lang.IllegalArgumentException: ALPN is not configured properly. See https://github.com/grpc/grpc-java/blob/master/SECURITY.md#troubleshooting for more information.
    

Use the [compatibility checker](https://github.com/googleapis/google-cloud-java/tree/master/google-cloud-util/google-cloud-compat-checker) to see if your environment is compatible with gRPC-based clients.

Incompatibility might mean one of the following:

  * You are not on a [supported platform](https://github.com/googleapis/google-cloud-java/#supported-platforms).
  * There are classpath conflicts with `netty`.
  * You are seeing any of the conflicts specified in [gRPC Troubleshooting guide](https://github.com/grpc/grpc-java/blob/master/SECURITY.md#troubleshooting).



## Troubleshoot `ClassNotFoundException`, `NoSuchMethodError`, and `NoClassDefFoundError`

These errors are often caused by having multiple versions or conflicting versions of the same dependency in the classpath. These dependency conflicts often occur with `guava` or `protobuf-java`.

Multiple sources might cause classpath conflicts:

  * Multiple versions of the same transitive dependency in the dependency tree.
  * Your runtime classpath has different versions of dependencies than what you specified in the build.



For example, if you have a direct or a transitive dependency on Guava version 19.0, and `google-cloud-java` uses Guava version 30.0, then `google-cloud-java` might be using Guava methods that don't exist in Guava 19.0, and cause `NoSuchMethodError`.

Similarly, if your classpath has an older version of `protobuf-java`, but `google-cloud-java` requires a later version, then you might see `NoClassDefFoundError` that fails to initialize `google-cloud-java` classes.

For example:
    
    
    java.lang.NoClassDefFoundError: Could not initialize class com.google.pubsub.v1.PubsubMessage$AttributesDefaultEntryHolder
    

### Validate the conflict

Check the dependency tree to see if you have multiple versions of the same dependencies:
    
    
    $ mvn dependency:tree
    

Look for versions of potentially conflicting dependencies such as `guava` or `protobuf-java`.

If you experience the error only during runtime, then your runtime environment might be introducing conflicting JARs into your runtime classpath. A typical case is that Hadoop, Spark, or other server software that your application runs on has conflicting versions `netty`, `guava`, or `protobuf-java` JARs in the classpath.

### Detect conflicts during build

To detect dependency linkage errors at compile time, add the [Linkage Checker Enforcer Rule](https://github.com/GoogleCloudPlatform/cloud-opensource-java/tree/master/enforcer-rules) in your pom.xml:
    
    
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-enforcer-plugin</artifactId>
            <version>3.0.0-M3</version>
            <dependencies>
              <dependency>
                <groupId>com.google.cloud.tools</groupId>
                <artifactId>linkage-checker-enforcer-rules</artifactId>
                <version>1.5.7</version>
              </dependency>
            </dependencies>
            <executions>
              <execution>
                <id>enforce-linkage-checker</id>
                <!-- Important! Should run after compile -->
                <phase>verify</phase>
                <goals>
                  <goal>enforce</goal>
                </goals>
                <configuration>
                  <rules>
                    <LinkageCheckerRule
                        implementation="com.google.cloud.tools.dependencies.enforcer.LinkageCheckerRule"/>
                  </rules>
                </configuration>
              </execution>
            </executions>
          </plugin>
    

However, there is no way to detect runtime classpath conflicts. You must be fully aware of which JARs/classes are included in the runtime classpath because every server environment is different.

### Resolve the conflict

There are different strategies to resolve conflicts, but you must understand the root cause of the conflicts:

  * If you control the dependency tree, upgrade the conflicting dependencies (for example, upgrading Guava). This approach is the most robust, but it can require significant effort and multiple library releases to ensure compatibility.
  * If you can't modify and push new versions of your dependencies, import `com.google.cloud:libraries-bom:25.1.0` (or a more recent version) to select consistent dependency versions. This approach simplifies dependency management. For example, this is how you can depend on consistent versions of Guava and `com.google.cloud:google-cloud-storage` without explicitly setting the version of either one:


    
    
      ...
      <dependencyManagement>
        <dependencies>
          <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>25.1.0</version>
            <type>pom</type>
            <scope>import</scope>
           </dependency>
         </dependencies>
      </dependencyManagement>
      ...
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>google-cloud-storage</artifactId>
        </dependency>
        <dependency>
          <groupId>com.google.guava</groupId>
          <artifactId>guava</artifactId>
        </dependency>
        ...
      </dependencies>
      ...
    

  * The libraries-bom release notes show the compatible dependency libraries. For example, https://github.com/googleapis/java-cloud-bom/releases/tag/v26.31.0 shows:
        
        These client libraries are built with the following Java libraries:
        
        - Guava: 32.1.3-jre
        - Protobuf Java: 3.25.2
        - Google Auth Library: 1.22.0
        - Google API Client: 2.2.0
        - gRPC: 1.61.0
        - GAX: 2.41.0
        - Google Cloud Core: 2.31.0
        

By examining the dependency graph of your project (`mvn dependency:tree -Dverbose`, `gradle dependencies`, or `sbt dependencyTree`), you might find some dependencies have unexpected versions, which might cause dependency conflicts.

  * If changing dependency versions introduces other failures, consider [shading dependencies](https://maven.apache.org/plugins/maven-shade-plugin/) that conflict with Google Cloud Java libraries.

For example, to shade `guava` and `protobuf-java`:
        
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>...</version>
            <executions>
              <execution>
                <phase>package</phase>
                <goals>
                  <goal>shade</goal>
                </goals>
                <configuration>
                  <keepDependenciesWithProvidedScope>false</keepDependenciesWithProvidedScope>
                  <relocations>
                    <!-- move protobuf to a shaded package -->
                    <relocation>
                      <pattern>com.google.protobuf</pattern>
                      <shadedPattern>myapp.shaded.com.google.protobuf</shadedPattern>
                    </relocation>
                    <!-- move Guava to a shaded package -->
                    <relocation>
                      <pattern>com.google.common</pattern>
                      <shadedPattern>myapp.shaded.com.google.common</shadedPattern>
                    </relocation>
                  </relocations>
                </configuration>
              </execution>
            </executions>
          </plugin>
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
