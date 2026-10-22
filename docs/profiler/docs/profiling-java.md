---
url: https://docs.cloud.google.com/profiler/docs/profiling-java/
title: Profiling Java applications \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:50.811138+00:00
---

# Profiling Java applications  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/profiling-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profiling Java applications

This page describes how to modify your Java application to capture profiling data and have that data sent to your Google Cloud project. For general information about profiling, see [Profiling concepts](https://docs.cloud.google.com/profiler/docs/concepts-profiling).

**Note:** If you plan to profile applications that are running outside of Google Cloud, then you need to perform some configuration steps that aren't discussed in this document. For example, you must configure the credentials for the profiling agent and you must link the agent to your project. For information about these steps, see [Profiling applications running outside Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external).

Profile types for Java: 

  * CPU time 
  * Heap (requires Java 11 or App Engine standard environment, disabled by default)
  * Wall time (not available for Java 8 App Engine standard environment)



Supported Java language versions: 

  * HotSpot-based JVMs (including Oracle JDK and some OpenJDK builds) for Java 8, 11 or later.



Supported profiling agent versions:

  * The most recent release of the agent is supported. In general, releases older than one year aren't supported. We recommend that you use the most recently released version of the agent.



Supported operating systems: 

  * Linux. Profiling Java applications is supported for Linux kernels whose standard C library is implemented with `glibc` or with `musl`. For configuration information specific to Linux Alpine kernels, see Running on Linux Alpine.



Supported environments:

  * Compute Engine
  * Google Kubernetes Engine (GKE)
  * App Engine flexible environment
  * App Engine standard environment (requires [App Engine SDK](https://docs.cloud.google.com/appengine/docs/standard/java/download) version 1.9.64 or later) 
  * Managed Service for Apache Spark (For information, see [Configuring Cloud Profiler for Managed Service for Apache Spark Spark and Hadoop jobs](https://docs.cloud.google.com/dataproc/docs/guides/profiling).) 
  * Outside of Google Cloud (For information on the additional configuration requirements, see [Profiling applications running outside of Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external).)



## Enabling the Profiler API

Before you use the profiling agent, ensure that the underlying Profiler API is enabled. You can check the status of the API and enable it if necessary by using either the Google Cloud CLI or the Google Cloud console:

###  gcloud CLI 

  1. If you have not already installed the Google Cloud CLI on your workstation, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/docs).

  2. Run the following command:
         
         gcloud services enable cloudprofiler.googleapis.com
         




For more information, see [`gcloud services`](https://docs.cloud.google.com/sdk/gcloud/reference/services).

###  Google Cloud console 

  1. Enable the Cloud Profiler API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudprofiler.googleapis.com)

  2. If **API enabled** is displayed, then the API is already enabled. If not, click the **Enable** button.




## Grant IAM role to service account

If you are deploying your application on Google Cloud resources and if you are using the default service account and haven't modified the role grants to that service account, then you can skip this section.

If you do any of the following, then you need to grant the service account the IAM role of [Cloud Profiler Agent (`roles/cloudprofiler.agent`)](https://docs.cloud.google.com/profiler/docs/iam):

  1. You are using the default service account but modified its role grants.
  2. You are using a user-created service account.
  3. You are using [workload identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), grant the Cloud Profiler Agent role to the Kubernetes service account.



You can grant an IAM role to a service account by using the Google Cloud console or the Google Cloud CLI. For example, you could use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    
    gcloud projects add-iam-policy-binding GCP_PROJECT_ID \
        --member serviceAccount:MY_SVC_ACCT_ID@GCP_PROJECT_ID.iam.gserviceaccount.com \
        --role roles/cloudprofiler.agent
    

Before you use the previous command, replace the following:

  * GCP_PROJECT_ID: Your project ID.
  * MY_SVC_ACCT_ID: The name of your service account.



For detailed information, see [Manage access to projects, folders, and organization](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** If the service account used by the profiling agent doesn't have the IAM role of Cloud Profiler Agent, then your Google Cloud project won't have any profile data.

## Installing the Profiler agent

###  Compute Engine 

  1. Create an installation directory, for example, `/opt/cprof`, for the Profiler agent:
         
         sudo mkdir -p /opt/cprof

  2. Download the agent archive from the `storage.googleapis.com` repository and extract it into the installation directory:
         
         wget -q -O- https://storage.googleapis.com/cloud-profiler/java/latest/profiler_java_agent.tar.gz \
         | sudo tar xzv -C /opt/cprof




###  GKE 

Modify the `Dockerfile` to create an installation directory for the Profiler agent, download the agent archive, and then extract the archive into the installation directory.

**Linux (`glibc`-based C library):**

Use the following installation command:
    
    
    RUN mkdir -p /opt/cprof && \
      wget -q -O- https://storage.googleapis.com/cloud-profiler/java/latest/profiler_java_agent.tar.gz \
      | tar xzv -C /opt/cprof

**Linux Alpine (`musl`-based C library):**

**Alpha**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the following installation command:
    
    
    wget -q -O- https://storage.googleapis.com/cloud-profiler/java/latest/profiler_java_agent_alpine.tar.gz \
    | tar xzv -C /opt/cprof

### Flexible Environment

When you use the Google [Java 8 runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/dev-java-only) base image or the [Java 9 / Jetty 9 runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime) base image, the Profiler agent is pre-installed, so there are no additional steps that you need to take to install the agent.

For all other base images, you need to install the agent. For example, the following `Dockerfile` contains the instructions to use the `openjdk:11-slim` image, to install the Profiler agent, and it defines the default parameters to be used when starting the application:
    
    
    FROM openjdk:11-slim
    
    COPY . .
    RUN  apt-get update \
         && apt-get install wget \
         && rm -rf /var/lib/apt/lists/*
    
    RUN mkdir -p /opt/cprof && \
        wget -q -O- https://storage.googleapis.com/cloud-profiler/java/latest/profiler_java_agent.tar.gz \
        | tar xzv -C /opt/cprof
    
    CMD ["java", "-agentpath:/opt/cprof/profiler_java_agent.so=OPTION1,OPTION2", "-jar", "PATH_TO_YOUR_JAR_FILE"]
    

To use this `Dockerfile` with App Engine flexible environment, you need to do the following:

  * Replace `OPTION1` and `OPTION2` with the agent configuration values needed for your application, and replace `PATH_TO_YOUR_JAR_FILE` with the path to your jar file.
  * Place the `Dockerfile` in the same directory as your `app.yaml` file.
  * Modify your `app.yaml` file to specify a custom runtime. For more information, see [Building Custom Runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build).



### Standard Environment

**Note:** The Java 8 runtime [doesn't support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) `GAE_PROFILER_MODE`. To continue using the Profiler agent, you must [migrate your application](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences) to the latest supported version of Java. To configure the Profiler agent for your second-generation Java application, see Starting your program.

When you use the [Java runtime environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime), the Profiler agent is pre-installed, so there are no additional steps that you need to take to install the agent. For Java version 11 and later, it is pre-installed in `/opt/cprof`.

### Outside Google Cloud 

  1. Create an installation directory, for example, `/opt/cprof`, for the Profiler agent:
         
         sudo mkdir -p /opt/cprof

  2. Download the agent archive from the `storage.googleapis.com` repository and extract it into the installation directory:
         
         wget -q -O- https://storage.googleapis.com/cloud-profiler/java/latest/profiler_java_agent.tar.gz \
         | sudo tar xzv -C /opt/cprof




To list all versions of the agent available for downloading, run the following command:
    
    
    gcloud storage ls gs://cloud-profiler/java/cloud-profiler-*

The command response is similar to the following:
    
    
    gs://cloud-profiler/java/cloud-profiler-java-agent_20191014_RC00.tar.gz
    gs://cloud-profiler/java/cloud-profiler-java-agent_20191021_RC00.tar.gz
    gs://cloud-profiler/java/cloud-profiler-java-agent_20191028_RC00.tar.gz
    

To download a specific version of the agent, pass its URL to the download command. For example, to download the agent built on 28 October 2019, you would use the following statement:
    
    
    wget -q -O- https://storage.googleapis.com/cloud-profiler/java/cloud-profiler-java-agent_20191028_RC00.tar.gz \
      | sudo tar xzv -C /opt/cprof

The version of the agent is logged during its initialization.

## Loading the Profiler agent

To profile your application, start Java as you normally would to run your program, but specify the agent-configuration options. You specify the path to the agent library, and you can pass options to the library.

For the App Engine standard environment, the agent is automatically loaded and configured. Skip ahead to Starting your program, for details on configuring, and starting, your program.

### Agent configuration

To configure the profiling agent, include the `-agentpath` flag when starting your application:
    
    
     -agentpath:INSTALL_DIR/profiler_java_agent.so=OPTION1,OPTION2,OPTION3
    

In this expression, `INSTALL_DIR` is the path to the profiling agent, while `OPTION1`, `OPTION2`, and `OPTION3` are agent configuration options. For example, if you replace `OPTION1` with `-cprof_service=myapp` in the previous expression, then you set the service name to `myapp`. There is no restriction on the number of options or their ordering. Supported configuration options are listed in the following table:

Agent option | Description  
---|---  
**`-cprof_service`** | If your application isn't running on App Engine, then you must use this configuration option to set the service name. For service name restrictions, see Service name and version arguments.   
  
**`-cprof_service_version`** | When you want the ability to analyze profiling data using the Profiler UI by the version of the service, use this option to set the version. For version restrictions, see Service name and version arguments.   
**`-cprof_project_id`** | When you are running outside of Google Cloud, use this option to specify your Google Cloud project ID. For more information, see [Profiling applications running outside of Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external).   
**`-cprof_zone_name`** | When your application is running on Google Cloud, the profiling agent determines the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) by communicating with the [Compute Engine metadata service](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata). If the profiling agent can't communicate with the metadata service, then you need to use this option.   
**`-cprof_gce_metadata_server_retry_count`**  
**`-cprof_gce_metadata_server_retry_sleep_sec`** | Together, these two options define the retry policy that the profiler agent uses when it communicates with the [Compute Engine metadata service](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata). to gather your Google Cloud project ID and zone information.   
  
Default policy is to retry up to 3 times waiting 1 second between attempts. This policy is sufficient for most configurations.   
**`-cprof_cpu_use_per_thread_timers`** | For the most accurate CPU time profiles, set this option to true. Use of this option results in increased per-thread overhead.   
  
Default value is false.   
**`-cprof_force_debug_non_safepoints`** | By default, the profiling agent forces JVM to generate debugging information for all just in time (JIT) generated code, in addition to generating debug information for all safepoints. This results in the most accurate function and line-level location information for CPU time and heap profiles at the expense of additional agent overhead. You can disable the generation of debugging information for JIT code by setting this option to false.   
  
Default value is true.   
**`-cprof_wall_num_threads_cutoff`** | By default, wall profiles aren't collected if the total number of threads in the application exceeds 4096. The limit ensures that during profile collection, the cost of traversing the stack of threads is minimal. If your service normally has more than 4096 threads and if you want to collect profiling data at the expense of additional overhead, use this flag to increase limit.  
  
Default limit is 4096 threads.   
**`-cprof_enable_heap_sampling`** |  To enable heap profiling for Java 11 and higher, set  
`-cprof_enable_heap_sampling=true`. Heap profiling isn't supported for Java 10 and lower.  
  
Heap profiling is disabled by default.  
  
When you enable heap profiling, the sampling interval is set to 512 KiB by default. This interval is sufficient for most applications and incurs less than 0.5% overhead for the application. Sampling intervals from 256 KiB (262144) to 1024 KiB (1048576) are supported. For example, to set the sampling interval to 256 KiB, which doubles the sampling rate, add the agent option: 
    
    
    -cprof_heap_sampling_interval=262144

Similarly, to set the sampling interval to 1024 KiB, which halves the sampling rate, add the agent option: 
    
    
    -cprof_heap_sampling_interval=1048576

If you enable this profile type, then specify a new service version when you deploy your application. For more information, see [Why don't I have data for a specific profile type?](https://docs.cloud.google.com/profiler/docs/troubleshooting#missing-one-type) **Note:** Simultaneous use of multiple heap profilers disables all heap profiling support for Java. This is a JVM limitation.  
  
### Service name and version arguments

When you load the Profiler agent, you specify a service-name argument and an optional service-version argument to configure it.

**Note:** In the App Engine flexible environment, you do not have to specify these arguments; they are derived from the environment.

The **service name** lets Profiler collect profiling data for all replicas of that service. The profiler service ensures a collection rate of one profile per minute, on average, for each service name across each combination service versions and zones.

For example, if you have a service with two versions running across replicas in three zones, the profiler will create an average of 6 profiles per minute for that service.

If you use different service names for your replicas, then your service will be profiled more often than necessary, with a correspondingly higher overhead.

When selecting a service name:

  * Choose a name that clearly represents the service in your application architecture. The choice of service name is less important if you only run a single service or application. It is more important if your application runs as a set of micro-services, for example.

  * Make sure to not use any process-specific values, like a process ID, in the service-name string.

  * The service-name string must match this regular expression:

`^[a-z0-9]([-a-z0-9_.]{0,253}[a-z0-9])?$`




A good guideline is to use a static string like `imageproc-service` as the service name.

The **service version** is optional. If you specify the service version, Profiler can aggregate profiling information from multiple instances and display it correctly. It can be used to mark different versions of your services as they get deployed. The Profiler UI lets you filter the data by service version; this way, you can compare the performance of older and newer versions of the code.

The value of the service-version argument is a free-form string, but values for this argument typically look like version numbers, for example, `1.0.0` or `2.1.2`.

### Starting your program

### Compute Engine

Start Java as you normally would to run your program, and add the the agent-configuration options:
    
    
    java \
        -agentpath:/opt/cprof/profiler_java_agent.so=-cprof_service=myapp,-cprof_service_version=1.0.0 \
        JAVA_OPTIONS -jar PATH_TO_YOUR_JAR_FILE PROGRAM_OPTIONS

### GKE

Modify the service container Dockerfile to start Java as you normally would to run your program, and add the agent-configuration options:
    
    
    CMD ["java", \
        "-agentpath:/opt/cprof/profiler_java_agent.so=-cprof_service=myapp,-cprof_service_version=1.0.0", \
         "-jar", "PATH_TO_YOUR_JAR_FILE" ]
        

### Flexible Environment

Modify the `app.yaml` configuration file to set the `PROFILER_ENABLE` environment variable. Then start your program as usual:
    
    
    env_variables:
       PROFILER_ENABLE: true

See [ Defining environment variables](https://docs.cloud.google.com/appengine/docs/flexible/java/reference/app-yaml#defining_environment_variables) for more information.

### Standard Environment

**Java 21 runtime environment**

If you don't use legacy bundled services, enable the profiler collection by modifying the `app.yaml` file to specify the `agentpath` flag using either of the following methods:

  * Set the [ `JAVA_TOOL_OPTIONS`](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/envvars002.html) environment variable:
        
        runtime: java21
        env_variables:
          JAVA_TOOL_OPTIONS: "-agentpath:/opt/cprof/profiler_java_agent.so=-logtostderr,-cprof_enable_heap_sampling=true"
        

  * Specify the `agentpath` using the `entrypoint` element: 
        
        runtime: java21
        entrypoint: java \
          -agentpath:/opt/cprof/profiler_java_agent.so=-logtostderr,-cprof_enable_heap_sampling=true \
          Main.java
        




If you use legacy bundled services, enable the profiler collection by modifying the `appengine-web.xml` file to specify the `agentpath` flag using either of the following methods:

  * Set the [ `JAVA_USER_OPTS`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access#entry_point_features) environment variable:
        
        <?xml version="1.0" encoding="utf-8"?>
        <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
        <env-variables>
        <env-var name="JAVA_USER_OPTS" value="-agentpath:/opt/cprof/profiler_java_agent.so=-logtostderr,-cprof_enable_heap_sampling=true" />
        </env-variables>
        </appengine-web-app>

  * Set the [ `CPROF_ENABLE`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access#entry_point_features) environment variable:
        
        <?xml version="1.0" encoding="utf-8"?>
        <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
        <env-variables>
        <env-var name="CPROF_ENABLE" value="-agentpath:/opt/cprof/profiler_java_agent.so=-logtostderr,-cprof_enable_heap_sampling=true" />
        </env-variables>
        </appengine-web-app>

  * Specify the `agentpath` using the `entrypoint` element:
        
        <?xml version="1.0" encoding="utf-8"?>
        <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
          <entrypoint>
           java
           -agentpath:/opt/cprof/profiler_java_agent.so=-logtostderr,-cprof_enable_heap_sampling=true
          </entrypoint>
        </appengine-web-app>




If a new profile type is configured for collection, ensure that you specify a new service version when you deploy your application. For more information, see [Why don't I have data for a specific profile type?](https://docs.cloud.google.com/profiler/docs/troubleshooting#missing-one-type)

### Agent logging

The profiling agent can report logging information for App Engine flexible environment, Compute Engine, and GKE. The profiling agent supports the following logging levels:

  * `0`: Log all messages. Default logging level.
  * `1`: Log warning, error, and fatal messages.
  * `2`: Log error and fatal messages.
  * `3`: Log only fatal messages and stop the application.



To enable writing logs to standard error with the default logging level, append `-logtostderr` to the `-agentpath` configuration.

To set the logging level to log only error and fatal messages, append `-minloglevel=2` to the `-agentpath` configuration.

For example, to enable logging of error and fatal messages to standard error, append `-logtostderr` and `‑minloglevel=2` to the `-agentpath` configuration:
    
    
     java -agentpath:/opt/cprof/profiler_java_agent.so=-cprof_service=myapp,-logtostderr,-minloglevel=2 \
       -jar myApp.jar
    

## Troubleshooting

This section lists issues that are specific to profiling Java applications. See [Troubleshooting](https://docs.cloud.google.com/profiler/docs/troubleshooting) for help with common problems.

Behavior | Cause | Solution  
---|---|---  
You've enabled multiple heap profilers and have no profile data.  |  Simultaneous use of multiple heap profilers disables all heap profiling support for Java. This is a JVM limitation.  |  Enable 1 profiler.   
  
## Running with Linux Alpine

**Alpha**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Java profiling agent for Linux Alpine is supported only for Google Kubernetes Engine configurations.

To install the latest Java profiling agent for Linux Alpine, see Installing the Profiler agent. 

### Authentication error

If you use Docker images that run with [Linux Alpine](https://alpinelinux.org) (such as `golang:alpine` or just `alpine`), you might see the following authentication error:
    
    
    connection error: desc = "transport: authentication handshake failed: x509: failed to load system roots and no roots provided"
    

Note that to see the error you must have agent logging enabled. 

The error indicates that the Docker images with Linux Alpine don't have the root SSL certificates installed by default. Those certificates are necessary for the profiling agent to communicate with the profiler API. To resolve this error, add the following `apk` command to your Dockerfile:
    
    
    FROM alpine
    ...
    RUN apk add --no-cache ca-certificates
    

You then need to rebuild and redeploy your application.

## What's next

  * [Select the profiles to analyze](https://docs.cloud.google.com/profiler/docs/selecting-profiles)
  * [Interact with the flame graph](https://docs.cloud.google.com/profiler/docs/interacting-flame-graph)
  * [Filter the flame graph](https://docs.cloud.google.com/profiler/docs/filtering-profiles)
  * [Focus the flame graph](https://docs.cloud.google.com/profiler/docs/focusing-profiles)
  * [Compare profiles](https://docs.cloud.google.com/profiler/docs/comparing-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
