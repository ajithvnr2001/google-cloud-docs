---
url: https://docs.cloud.google.com/profiler/docs/profiling-python/
title: Profiling Python applications \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:50.993936+00:00
---

# Profiling Python applications  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/profiling-python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profiling Python applications

This page describes how to modify your Python application to capture profiling data and have that data sent to your Google Cloud project. For general information about profiling, see [Profiling concepts](https://docs.cloud.google.com/profiler/docs/concepts-profiling).

**Note:** If you plan to profile applications that are running outside of Google Cloud, then you need to perform some configuration steps that aren't discussed in this document. For example, you must configure the credentials for the profiling agent and you must link the agent to your project. For information about these steps, see [Profiling applications running outside Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external).

Profile types for Python: 

  * CPU time 
  * Wall time (main thread)



Supported Python language versions: 

  * Python 3.6 through 3.11.0.



Supported profiling agent versions:

  * The most recent release of the agent is supported. In general, releases older than one year aren't supported. We recommend that you use the most recently released version of the agent.



Supported operating systems: 

  * Linux. Profiling Python applications is supported for Linux kernels whose standard C library is implemented with `glibc` or with `musl`. For configuration information specific to Linux Alpine kernels, see Running on Linux Alpine.



Supported environments:

  * Compute Engine
  * Google Kubernetes Engine (GKE)
  * App Engine flexible environment
  * App Engine standard environment (requires [Python 3 runtime environment](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime)) 
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

## Using Cloud Profiler

For best practices using Python, go to [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

###  Compute Engine 

For Compute Engine, do the following:

  1. Install the C/C++ compiler and development tools:
         
         sudo apt-get install -y build-essential
         

  2. Install pip:
         
         sudo apt-get install -y python3-pip
         

  3. Install the Profiler package:
         
         pip3 install google-cloud-profiler
         

  4. Import the `googlecloudprofiler` module and call the `googlecloudprofiler.start` function as early as possible in your initialization code:
         
         import googlecloudprofiler
         
         
         def main():
             # Profiler initialization. It starts a daemon thread which continuously
             # collects and uploads profiles. Best done as early as possible.
             try:
                 googlecloudprofiler.start(
                     service="hello-profiler",
                     service_version="1.0.1",
                     # verbose is the logging level. 0-error, 1-warning, 2-info,
                     # 3-debug. It defaults to 0 (error) if not set.
                     verbose=3,
                     # project_id must be set if not running on GCP.
                     # project_id='my-project-id',
                 )
             except (ValueError, NotImplementedError) as exc:
                 print(exc)  # Handle errors here

You must specify the `service` parameter in your `start` function. To filter by the application version in the Profiler interface, specify the `service_version` parameter. For troubleshooting and exception information, see Troubleshooting.




###  GKE 

For GKE, do the following:

  1. Modify your Dockerfile to install the Profiler package:
         
         FROM python:3
         ...
         RUN apt-get update && apt-get install -y build-essential python3-pip
         RUN pip3 install google-cloud-profiler
         

  2. Import the `googlecloudprofiler` module and call the `googlecloudprofiler.start` function as early as possible in your initialization code:
         
         import googlecloudprofiler
         
         
         def main():
             # Profiler initialization. It starts a daemon thread which continuously
             # collects and uploads profiles. Best done as early as possible.
             try:
                 googlecloudprofiler.start(
                     service="hello-profiler",
                     service_version="1.0.1",
                     # verbose is the logging level. 0-error, 1-warning, 2-info,
                     # 3-debug. It defaults to 0 (error) if not set.
                     verbose=3,
                     # project_id must be set if not running on GCP.
                     # project_id='my-project-id',
                 )
             except (ValueError, NotImplementedError) as exc:
                 print(exc)  # Handle errors here

You must specify the `service` parameter in your `start` function. To filter by the application version in the Profiler interface, specify the `service_version` parameter. For troubleshooting and exception information, see Troubleshooting.




### Flexible Environment

For App Engine flexible environment, do the following:

  1. Add `google-cloud-profiler` to your `requirements.txt` file.

  2. Import the `googlecloudprofiler` module and call the `googlecloudprofiler.start` function as early as possible in your initialization code.




For App Engine, the `service` and `service_version` are derived from your operating environment. For troubleshooting and exception information, see Troubleshooting.

### Standard Environment

For App Engine standard environment, which requires that you use the Python 3 runtime environment, do the following:

  1. Add `google-cloud-profiler` to your `requirements.txt` file.

  2. Import the `googlecloudprofiler` module and call the `googlecloudprofiler.start` function as early as possible in your initialization code.




For App Engine, the `service` and `service_version` are derived from your operating environment. For troubleshooting and exception information, see Troubleshooting.

## `start` function

The `googlecloudprofiler.start` function creates a daemon thread which continuously collects and uploads profiles. You should call `start` one time, and as early as possible in your application.

Parameter | Description  
---|---  
`service`1 |  (Required) The name for the service being profiled. For restrictions on the service name, see Service name and version arguments.   
`service_version`1 |  (Optional) The version of the service being profiled. For restrictions on the service version, see Service name and version arguments.   
`verbose` |  (Optional) The logging level. For details on the logging levels, see Agent logging.   
  
Default value is **0 (Error)**.   
`project_id`2 |  (Optional) Your Google Cloud project ID.   
`disable_cpu_profiling` |  (Optional) To disable CPU time profiling, set `disable_cpu_profiling=True`.   
  
This parameter is supported for Python versions 3.2 through 3.11.0. For all other Python versions, CPU time profiling isn't supported and this parameter is ignored.   
  
Default value is **False**.   
`disable_wall_profiling` |  (Optional) To disable Wall profiling, set `disable_wall_profiling=True`.   
  
This parameter is supported for Python versions 3.6 through 3.11.0. For all other Python versions, Wall profiling isn't supported and this parameter is ignored.   
  
For restrictions on the `start` function when Wall profiling is enabled, see Limitations.   
  
Default value is **False**.   
  
1 For only Compute Engine and GKE. For App Engine, the value is derived from the environment.  
2 For Google Cloud, the value is derived from the environment. For non-Google Cloud environments, you must provide a value. For information, see [Profiling applications running outside Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external). 

## Analyzing data

After Profiler has collected data, you can view and analyze this data using the Profiler interface.

In the Google Cloud console, go to the **Profiler** page: 

[Go to **Profiler**](https://console.cloud.google.com/profiler)

You can also find this page by using the search bar.

## Service name and version arguments

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

## Agent logging

By default, the profiling agent logs messages with a severity level of `error`. To configure the agent to log messages with lower severity levels, specify the `verbose` parameter when starting the agent. There are four supported values for `verbose`:

  * `0` : Error
  * `1` : Warning
  * `2` : Informational
  * `3` : Debug



If you set the `verbose` parameter to `1` in your call to `start`, then messages with a severity level of `Warning` or `Error` are logged, while `Informational` and `Debug` messages are ignored.

To log all messages, set `verbose` to `3` when starting the agent:
    
    
    googlecloudprofiler.start(service='service_name', verbose=3)
    

## Troubleshooting

This section lists limitations, exceptions, and known issues that are specific to profiling Python applications. See [Troubleshooting](https://docs.cloud.google.com/profiler/docs/troubleshooting) for help with common problems.

### Limitations

Profile type | Restrictions and limitations  
---|---  
Wall time | 

  * Main-thread profiling only.
  * The profile `start` function must be called from the main thread.
  * The Profiler signal handler executes only on the main thread. If the main thread cannot execute, no profiling data is captured. **Note:** Don't enable Wall profiling if your application contains a large number of threads. Use of Wall profiles in this configuration results in slow performance and no profile data. 

  
  
### Exceptions

Error | Cause | Solution  
---|---|---  
`NotImplementedError` thrown during `start` |  Application executed in a non-Linux environment.  | 

  * Execute your application in a Linux environment.

  
`ValueError` thrown during `start` |  The `start` function arguments are invalid, necessary information can't be determined from the environment variables and arguments, or profiling if both CPU time profiling and Wall time profiling are disabled.  | 

  * Ensure the service name and version meet the requirements defined in Service name and version arguments. 
  * If Wall profiling is enabled, make sure `start` is called from the main thread.
  * Ensure that you are using a supported version of Python and that CPU time or Wall time profiling is enabled. For more information, see `start` function.
  * Check that you have specified the `project_id` parameter to `start` if you are running outside of Google Cloud. For more information, see `start` function.

  
  
### Known issues

Behavior | Cause | Solution  
---|---|---  
You don't have any profile data or you enabled a new profile type and are missing profile data.  | Common causes are related to configuration.  | See [Troubleshooting](https://docs.cloud.google.com/profiler/docs/troubleshooting).   
You are using [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/index.html) and you don't have CPU time and Wall profile data for all processes.  | When uWSGI uses multiple workers to handle requests, the default behavior is to perform application initialization only in the primary ("master") process. The forked processes don't perform the initialization sequence. If you configure the profiling agent in your application's initialization sequence, for example, in `AppConfig.ready()` in a Django application, then the effect is that the profiling agent isn't configured for the forked processes. | To perform application initialization in all worker processes, set the flag [lazy-apps](https://uwsgi-docs.readthedocs.io/en/latest/Options.html#lazy-apps) to `true`. See the next topic in this table for a related issue.  
You are using [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/index.html) and you don't have Wall profile data, but you do have CPU time profile data.  | The Wall profiler depends on the Python signal module. When the Python interpreter is compiled with thread support, the default configuration disables custom signal handling for forked processes. | For uWSGI applications, enable the custom signal handling by setting the flag [py-call-osafterfork](https://uwsgi-docs.readthedocs.io/en/latest/Options.html#py-call-osafterfork) to `true`. See the previous topic in this table for a related issue.  
After enabling the profiler, the error log contains new entries:   
  
` BlockingIOError: [Errno 11] Resource temporarily unavailable Exception ignored when trying to write to the signal wakeup fd `  
  
[GitHub issue](https://github.com/GoogleCloudPlatform/cloud-profiler-python/issues/50) | Your application registered with the signal wakeup file descriptor, [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd). By default, if the file descriptor's buffer fills then a warning is logged to stderr. When Cloud Profiler collects profiles it triggers signals with high frequency. This behavior can cause the file descriptor's buffer to become full. | If your application can run safely when signals are lost, then you can use Cloud Profiler. If you are using Python 3.7 or later and want to disable the warning messages, then pass `warn_on_full_buffer=False` as a parameter to [`signal.set_wakeup_fd`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd).  If your application can't safely run when signals are lost, then we recommend that you stop using Cloud Profiler. Continued use might cause loss of signal numbers and excessive entries in the error log.   
  
## Running with Linux Alpine

**Alpha**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Python profiling agent for Linux Alpine is supported only for Google Kubernetes Engine configurations.

To build the Python profiling agent, you must install the package `build-base`. To use the Python profiling agent on Alpine without installing additional dependencies on to the final Alpine image, you can use a two-stage build and compile the Python profiling agent in the first stage. For example, the following Docker image uses a multi-stage build to compile and install the Python profiling agent:
    
    
    FROM python:3.7-alpine as builder
    
    # Install build-base to allow for compilation of the profiling agent.
    RUN apk add --update --no-cache build-base
    
    # Compile the profiling agent, generating wheels for it.
    RUN pip3 wheel --wheel-dir=/tmp/wheels google-cloud-profiler
    
    FROM python:3.7-alpine
    
    # Copy over the directory containing wheels for the profiling agent.
    COPY --from=builder /tmp/wheels /tmp/wheels
    
    # Install the profiling agent.
    RUN pip3 install --no-index --find-links=/tmp/wheels google-cloud-profiler
    
    # Install any other required modules or dependencies, and copy an app which
    # enables the profiler as described in "Enable the profiler in your
    # application".
    COPY ./bench.py .
    
    # Run the application when the docker image is run, using either CMD (as is done
    # here) or ENTRYPOINT.
    CMD python3 -u bench.py
    

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
