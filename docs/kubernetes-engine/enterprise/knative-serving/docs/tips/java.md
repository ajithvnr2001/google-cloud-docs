---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/java/
title: Optimizing Java applications \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:42.011896+00:00
---

# Optimizing Java applications  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Optimizing Java applications Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes optimizations for Knative serving services written in the Java programming language, along with background information to help you understand the tradeoffs involved in some of the optimizations. The information on this page supplements the [general optimization tips](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general), which also apply to Java.

Traditional Java web-based applications are designed to serve requests with high concurrency and low latency, and tend to be long-running applications. The JVM itself also optimizes the execution code over time with JIT, so that hot paths are optimized and applications run more efficiently over time.

Many of the best practices and optimizations in these traditional Java web-based application revolve around:

  * Handling concurrent requests (both thread-based and non-blocking I/O)
  * Reducing response latency using connection pooling and batching non-critical functions, for example sending traces and metrics to background tasks.



While many of these traditional optimizations work well for long-running applications, they may not work as well in a Knative serving service, which runs only when actively serving requests. This page takes you through a few different optimizations and tradeoffs for Knative serving that you can use to reduce startup time and memory usage.

## Optimizing the container image

By optimizing the container image, you can reduce load and startup times. You can optimize the image by:

  * Minimizing the container image
  * Avoiding use of nested library archive JARs
  * Using Jib



### Minimizing container image

Refer to the general tips page on [minimizing container](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general#minimize-container) for more context on this issue. The general tips page recommends reducing container image content to only what's needed. For example, make sure your container image _does not contain_ :

  * Source code
  * Maven build artifacts
  * Build tools
  * Git directories
  * Unused binaries/utilities



If you are building the code from within a Dockerfile, use Docker multi-stage build so that the final container image only has the JRE and the application JAR file itself.

### Avoiding nested library archives JARs

Some popular frameworks, like Spring Boot, create an application archive (JAR) file that contains additional library JAR files (nested JARs). These files need to be unpacked/decompressed during startup time and can increase startup speed in Knative serving. When possible, create a thin JAR with externalized libraries: this can be automated by using Jib to containerize your application

### Using Jib

Use the [Jib plugin](https://github.com/GoogleContainerTools/jib) to create a minimal container and flatten the application archive automatically. Jib works with both Maven and Gradle, and works with Spring Boot applications out of the box. Some application frameworks may require additional Jib configurations.

## JVM Optimizations

Optimizing the JVM for a Knative serving service can result in better performance and memory usage.

### Using container-aware JVM Versions

In VM and machines, for CPU and memory allocations, the JVM understands the CPU and memory it can use from well known locations, for example, in Linux, `/proc/cpuinfo`, and `/proc/meminfo`. However, when running in a container, the CPU and memory constraints are stored in`/proc/cgroups/...`. Older version of the JDK continue to look in `/proc` instead of `/proc/cgroups`, which can result in more CPU and memory usage than was assigned. This can cause:

  * An excessive number of threads because thread pool size is configured by `Runtime.availableProcessors()`
  * A default max heap that exceeds the container memory limit. The JVM aggressively uses the memory before it garbage collects. This can easily cause the container to exceed the container memory limit, and get OOMKilled.



So, use a container aware JVM version. OpenJDK versions greater or equal to version `8u192` is container aware by default.

### Understanding JVM Memory Usage

The JVM memory usage is composed of native memory usage and heap usage. Your application working memory is usually in the heap. The size of the heap is constrained by the Max Heap configuration. With a Knative serving 256MB RAM instance, you cannot assign all 256MB to the Max Heap, because the JVM and the OS also require native memory, for example, thread stack, code caches, file handles, buffers, etc. If your application is getting OOMKilled and you need to know the JVM memory usage (native memory + heap), turn on Native Memory Tracking to see usages upon a successful application exit. If your application gets OOMKilled, then it won't be able to print out the information. In that case, run the application with more memory first so that it can successfully generate the output.

Native Memory Tracking cannot be turned on via the `JAVA_TOOL_OPTIONS` environment variable. You need to add the Java command line startup argument to your container image entrypoint, so that your application is started with these arguments:
    
    
    java -XX:NativeMemoryTracking=summary \
      -XX:+UnlockDiagnosticVMOptions \
      -XX:+PrintNMTStatistics \
      ...
    

The native memory usage can be estimated based on the number of classes to load. Consider using an open source [Java Memory Calculator](https://github.com/cloudfoundry/java-buildpack-memory-calculator) to estimate memory needs.

### Turning off the optimization compiler

By default, JVM has several phases of JIT compilation. Although these phases improve the efficiency of your application over time, they can also add overhead to memory usage, and increase the startup time.

For short running, serverless applications (for example, functions), consider turning off the optimization phases to trade long term efficiency for reduced startup time.

For a Knative serving service, configure the environmental variable:
    
    
    JAVA_TOOL_OPTIONS="-XX:+TieredCompilation -XX:TieredStopAtLevel=1"
    

### Using application class-data sharing

To further reduce JIT time and memory usage, consider using [application class data sharing](https://openjdk.java.net/jeps/310) (AppCDS) to share the ahead-of-time compiled Java classes as an archive. The AppCDS archive can be re-used when starting another instance of the same Java application. The JVM can re-use the pre-computed data from the archive, which reduces startup time.

The following considerations apply to using AppCDS:

  * The AppCDS archive to be re-used must be reproduced by exactly the same OpenJDK distribution, version, and architecture that was originally used to produce it.
  * You must run your application at least once to generate the list of classes to be shared, and then use that list to generate the AppCDS archive.
  * The coverage of the classes depends on the codepath executed during the run of the application. To increase coverage, programmatically trigger more codepaths.
  * The application must exit successfully to generate this classes list. Consider implementing an application flag that is used to indicate generation of AppCDS archive, and so it can exit immediately.
  * The AppCDS archive can only be re-used if you launch new instances in exactly the same way that the archive was generated.
  * The AppCDS archive only works with a regular JAR file package; you can't use nested JARs.



#### Spring Boot example using a shaded JAR file

Spring Boot applications use a nested uber JAR by default, which won't work for AppCDS. So, if you're using AppCDS, you need to create a shaded JAR. For example, using Maven and the Maven Shade Plugin:
    
    
    <build>
      <finalName>helloworld</finalName>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-shade-plugin</artifactId>
          <configuration>
            <keepDependenciesWithProvidedScope>true</keepDependenciesWithProvidedScope>
            <createDependencyReducedPom>true</createDependencyReducedPom>
            <filters>
              <filter>
                <artifact>*:*</artifact>
                <excludes>
                  <exclude>META-INF/*.SF</exclude>
                  <exclude>META-INF/*.DSA</exclude>
                  <exclude>META-INF/*.RSA</exclude>
                </excludes>
              </filter>
            </filters>
          </configuration>
          <executions>
            <execution>
              <phase>package</phase>
              <goals><goal>shade</goal></goals>
              <configuration>
                <transformers>
                  <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                    <resource>META-INF/spring.handlers</resource>
                  </transformer>
                  <transformer implementation="org.springframework.boot.maven.PropertiesMergingResourceTransformer">
                    <resource>META-INF/spring.factories</resource>
                  </transformer>
                  <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                    <resource>META-INF/spring.schemas</resource>
                  </transformer>
                  <transformer implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer" />
                  <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                    <mainClass>${mainClass}</mainClass>
                  </transformer>
                </transformers>
              </configuration>
            </execution>
          </executions>
        </plugin>
      </plugins>
    </build>
    

If your shaded JAR contains all the dependencies, you can produce a simple archive during the container build using a `Dockerfile`:
    
    
    # Use Docker's multi-stage build
    FROM adoptopenjdk:11-jre-hotspot as APPCDS
    
    COPY target/helloworld.jar /helloworld.jar
    
    # Run the application, but with a custom trigger that exits immediately.
    # In this particular example, the application looks for the '--appcds' flag.
    # You can implement a similar flag in your own application.
    RUN java -XX:DumpLoadedClassList=classes.lst -jar helloworld.jar --appcds=true
    
    # From the captured list of classes (based on execution coverage),
    # generate the AppCDS archive file.
    RUN java -Xshare:dump -XX:SharedClassListFile=classes.lst -XX:SharedArchiveFile=appcds.jsa --class-path helloworld.jar
    
    FROM adoptopenjdk:11-jre-hotspot
    
    # Copy both the JAR file and the AppCDS archive file to the runtime container.
    COPY --from=APPCDS /helloworld.jar /helloworld.jar
    COPY --from=APPCDS /appcds.jsa /appcds.jsa
    
    # Enable Application Class-Data sharing
    ENTRYPOINT java -Xshare:on -XX:SharedArchiveFile=appcds.jsa -jar helloworld.jar
    

### Turning off class verification

When the JVM loads classes into memory for execution, it verifies that the class is untampered and has no malicious edits or corruptions. If your software delivery pipeline is trusted (for example, you can verify and validate every output), if you can fully trust the bytecode in your container image and your application doesn't load classes from arbitrary remote sources, then you can consider turning off verification. Turning off verification may improve startup speed if a large number of classes are loaded at startup time.

For a Knative serving service, configure the environmental variable:
    
    
    JAVA_TOOL_OPTIONS="-noverify"
    

**Note:** [This option is deprecated for OpenJDK 13 and above](https://www.oracle.com/java/technologies/javase/13all-relnotes.html).

### Reducing thread stack size

Most Java web applications are thread-per-connection based. Each Java thread consumes native memory (not in heap). This is known as the thread stack, and it is defaulted to 1MB per thread. If your application handles 80 concurrent requests, then it may have at least 80 threads, which translates to 80MB of thread stack space used. The memory is in addition to the heap size. The default may be larger than necessary. You can reduce the thread stack size.

If you reduce too much, then you will see `java.lang.StackOverflowError`. You can profile your application and find the optimal thread stack size to configure.

For a Knative serving service, configure the environmental variable:
    
    
    JAVA_TOOL_OPTIONS="-Xss256k"
    

## Reducing threads

You can optimize memory by reducing the number of threads, by using non-blocking reactive strategies and avoiding background activities.

### Reducing number of threads

Each Java thread may increase the memory usage due to the Thread Stack. Knative serving allows a maximum of 80 concurrent requests. With thread-per-connection model, you need at maximum 80 threads to handle all the concurrent requests. Most web servers and frameworks allow you to configure the max number of threads and connections. For example, in Spring Boot, you can cap the maximum connections in the `applications.properties` file:
    
    
    server.tomcat.max-threads=80
    

### Writing non-blocking reactive code to optimize memory and startup

To truly reduce the number of threads, consider adopting a non-blocking reactive programming model, so that the number of threads can be significantly reduced while handling more concurrent requests. Application frameworks like Spring Boot with Webflux, Micronaut, and Quarkus support reactive web applications.

Reactive frameworks such as Spring Boot with Webflux, Micronaut, Quarkus generally have faster startup times.

If you continue to write blocking code in a non-blocking framework, the throughput and error rates will be significantly worse in a Knative serving service. This is because non-blocking frameworks will only have a few threads, for example, 2 or 4. If your code is blocking, then it can handle very few concurrent requests.

These non-blocking frameworks may also offload blocking code to an unbounded thread pool - meaning that while it can accept many concurrent requests, the blocking code will execute in new threads. If threads accumulate in an unbounded way, you will exhaust the CPU resource and start to thrash. Latency will be severely impacted. If you use a non-blocking framework, be sure to understand the thread pool models and bound the pools accordingly.

### Avoiding background activities

Knative serving [throttles an instance CPU](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract#cpu-request) when this instance no longer receives requests. Traditional workloads that have background tasks need special consideration when running in Knative serving.

For example, if you are collecting application metrics and batching the metrics in the background to send periodically, then those metrics won't send when the CPU is throttled. If your application is constantly receiving requests, you may see fewer issues. If your application has low QPS, then the backgrounded task may never execute.

Some well known patterns that are backgrounded that you need to pay attention to:

  * JDBC Connection Pools - clean ups and connection checks usually happens in the background
  * Distributed Trace Senders - Distributed traces are usually batched and sent periodically or when the buffer is full in the background.
  * Metrics Senders - Metrics are usually batched and sent periodically in the background.
  * For Spring Boot, any methods annotated with `@Async` annotation
  * Timers - any Timer-based triggers (e.g., ScheduledThreadPoolExecutor, Quartz, or `@Scheduled` Spring annotation) may not execute when CPUs are throttled.
  * Message receivers - For example, Pub/Sub streaming pull clients, JMS clients, or Kafka clients, usually run in the background threads without need of requests. These will not work when your application has no requests. Receiving messages this way is not recommended in Knative serving.



## Application optimizations

In your Knative serving service code, you can also optimize for faster startup times and memory usage.

### Reducing startup tasks

Traditional Java web-based applications can have many tasks to complete during startup, e.g., preloading of data, warming up the cache, establishing connection pools, etc. These tasks, when executed sequentially, can be slow. However, if you want them to execute in parallel, you should increase the number of CPU cores.

Knative serving currently sends a real user request to trigger a cold start instance. Users who have a request assigned to a newly started instance may experience long delays. Knative serving currently does not have a "readiness" check to avoid sending requests to unready applications.

### Using connection pooling

If you use connection pools, be aware that connection pools may evict unneeded connections in the background (see Avoiding background tasks). If your application has low QPS, and can tolerate high latency, consider opening and closing connections per request. If your application has high QPS, then background evictions may continue to execute as long as there are active requests.

In both cases, the application's database access will be bottlenecked by the maximum connections allowed by the database. Calculate the maximum connections you can establish per Knative serving instance, and [configure Knative serving maximum instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/max-instances) so that the maximum instances times connections per instance is less than the maximum connections allowed.

## Using Spring Boot

If you use Spring Boot, you need to consider the following optimizations

### Using Spring Boot version 2.2 or greater

Starting with version 2.2, Spring Boot has been heavily optimized for startup speed. If you are using Spring Boot versions less than 2.2, consider upgrading, or [apply individual optimizations manually](https://spring.io/blog/2018/12/12/how-fast-is-spring).

### Using lazy initialization

There is a global lazy initialization flag that can be turned on in Spring Boot 2.2 and greater. This will improve the startup speed, but with the trade off that the first request may have longer latency because it will need to wait for components to initialize for the first time.

You can turn on lazy initialization in `application.properties`:
    
    
    spring.main.lazy-initialization=true
    

Or, by using an environmental variable:
    
    
    SPRING_MAIN_LAZY_INITIALIZATIION=true
    

However, if you are using min-instances, then lazy initialization is not going to help, since initialization should have occurred when the min-instance started.

### Avoiding class scanning

Class scanning will cause additional disk reads in Knative serving because in Knative serving, disk access is generally slower than a regular machine. Make sure that Component Scan is limited or completely avoided. Consider using Spring Context Indexer, to pre-generate an index. Whether this will improve your startup speed will vary based on your application.

For example, in your Maven `pom.xml` add the indexer dependency (it's actually an annotation processor):
    
    
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context-indexer</artifactId>
      <optional>true</optional>
    </dependency>
    

### Using Spring Boot developer tools not in production

If you use [Spring Boot Developer Tool](https://docs.spring.io/spring-boot/docs/current/reference/html/using.html#using.devtools) during development, make sure it is not packaged in the production container image. This may happen if you built the Spring Boot application without the Spring Boot build plugins (for example, using the Shade plugin, or using Jib to containerize).

In these cases, make sure the build tool excludes Spring Boot Dev tool explicitly. Or, [turn off the Spring Boot Developer Tool explicitly](https://docs.spring.io/spring-boot/docs/current/reference/html/using.html#using.devtools).

## What's next

For more tips, see

  * [General tips](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general)
  * [Migrating an Existing Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrating)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
