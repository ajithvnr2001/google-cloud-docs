---
url: https://docs.cloud.google.com/profiler/docs/profiling-go/
title: Profiling Go applications \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:51.367529+00:00
---

# Profiling Go applications  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/profiling-go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profiling Go applications

This page describes how to modify your Go application to capture profiling data and have that data sent to your Google Cloud project. For general information about profiling, see [Profiling concepts](https://docs.cloud.google.com/profiler/docs/concepts-profiling).

**Note:** If you plan to profile applications that are running outside of Google Cloud, then you need to perform some configuration steps that aren't discussed in this document. For example, you must configure the credentials for the profiling agent and you must link the agent to your project. For information about these steps, see [Profiling applications running outside Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external).

Profile types for Go: 

  * CPU time 
  * Heap 
  * Allocated heap 
  * Contention (Go mutex)
  * Threads (Go goroutine)



Supported Go language versions: 

  * All officially maintained Go releases, unless otherwise noted. For more information, see [Go language release policy](https://golang.org/doc/devel/release.html#policy). 



Supported profiling agent versions:

  * The most recent release of the agent is supported. In general, releases older than one year aren't supported. We recommend that you use the most recently released version of the agent.



Supported operating systems: 

  * Linux. Profiling Go applications is supported for Linux kernels whose standard C library is implemented with `glibc` or with `musl`. For configuration information specific to Linux Alpine kernels, see Running on Linux Alpine.



Supported environments:

  * Compute Engine
  * Google Kubernetes Engine (GKE)
  * App Engine flexible environment
  * App Engine standard environment (requires Go 1.11 or higher) 
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

In all of the supported environments, you use the Profiler by importing the package in your application and then initializing the Profiler as early as possible in your application.

You can enable Mutex-contention profiling (“Contention” in the interface) by setting the `MutexProfiling` configuration option to `true`.

For more information on the Profiler API, including all the configuration options, see the [public API docs](https://godoc.org/cloud.google.com/go/profiler).

###  Compute Engine 

For Compute Engine, in `profiler.Config` set `Service` with a name for the service being profiled and optionally set `ServiceVersion` with the service version:
    
    
    // snippets is an example of starting cloud.google.com/go/profiler.
    package main
    
    import (
    	"cloud.google.com/go/profiler"
    )
    
    func main() {
    	cfg := profiler.[Config](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Config){
    		Service:        "myservice",
    		ServiceVersion: "1.0.0",
    		// ProjectID must be set if not running on GCP.
    		// ProjectID: "my-project",
    
    		// For OpenCensus users:
    		// To see Profiler agent spans in APM backend,
    		// set EnableOCTelemetry to true
    		// EnableOCTelemetry: true,
    	}
    
    	// Profiler initialization, best done as early as possible.
    	if err := profiler.[Start](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Start)(cfg); err != nil {
    		// TODO: Handle error.
    	}
    }
    

If you have dependencies in your source code that are fetched manually, then you might need to add the following to your build script or Dockerfile: 
    
    
    go get cloud.google.com/go/profiler

###  GKE 

For GKE, in `profiler.Config` set `Service` with a name for the service being profiled and optionally set `ServiceVersion` with the service version:
    
    
    // snippets is an example of starting cloud.google.com/go/profiler.
    package main
    
    import (
    	"cloud.google.com/go/profiler"
    )
    
    func main() {
    	cfg := profiler.[Config](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Config){
    		Service:        "myservice",
    		ServiceVersion: "1.0.0",
    		// ProjectID must be set if not running on GCP.
    		// ProjectID: "my-project",
    
    		// For OpenCensus users:
    		// To see Profiler agent spans in APM backend,
    		// set EnableOCTelemetry to true
    		// EnableOCTelemetry: true,
    	}
    
    	// Profiler initialization, best done as early as possible.
    	if err := profiler.[Start](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Start)(cfg); err != nil {
    		// TODO: Handle error.
    	}
    }
    

If you have dependencies in your source code that are fetched manually, then you might need to add the following to your build script or Dockerfile: 
    
    
    go get cloud.google.com/go/profiler

###  App Engine 

For the App Engine flexible environment and the App Engine standard environment, the code additions are nearly identical to those for Compute Engine and GKE. There is one exception. In both App Engine environments, the `Service` and `ServiceVersion` parameters are derived from the environment, so you don't have to specify them.
    
    
    // appengine is an example of starting cloud.google.com/go/profiler on
    // App Engine.
    package main
    
    import (
    	"cloud.google.com/go/profiler"
    )
    
    func main() {
    	// Profiler initialization, best done as early as possible.
    	if err := profiler.[Start](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Start)(profiler.[Config](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Config){
    		// Service and ServiceVersion can be automatically inferred when running
    		// on App Engine.
    		// ProjectID must be set if not running on GCP.
    		// ProjectID: "my-project",
    	}); err != nil {
    		// TODO: Handle error.
    	}
    }
    

When you run the application locally, set the `ProjectID` (the ID of your Google Cloud project) and `Service` parameters in `profiler.Config`, since they cannot be derived from a local environment. You don't need to set `ServiceVersion`.

If you are using App Engine standard environment, see [Migrating your app to Go 1.11](https://docs.cloud.google.com/appengine/docs/standard/go111/go-differences) for detailed information on changes you might need to make to your application. Also, you must use Google Cloud CLI version 226.0.0 or later. To update the Google Cloud CLI, run the following command:
    
    
    gcloud components update
    

To run your application:

  1. Update the dependencies:
         
         go get cloud.google.com/go/profiler
         

  2. Deploy the application to your App Engine flexible environment or to your App Engine standard environment:
         
         gcloud app deploy [DEPLOYMENT]
         

where `DEPLOYMENT` is the path to your configuration file. For example, `DEPLOYMENT` might be `main/app.yaml`.

     * For App Engine flexible environment deployment details, see [Testing and deploying your application](https://docs.cloud.google.com/appengine/docs/flexible/go/testing-and-deploying-your-app).
     * For App Engine standard environment deployment details, see [Testing and deploying your application](https://docs.cloud.google.com/appengine/docs/standard/go111/testing-and-deploying-your-app).



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

The profiling agent can report debug information in its logs. By default, agent logging is disabled.

To enable agent logging, set the `DebugLogging` option to `true` when starting the agent:
    
    
    profiler.Start(profiler.Config{..., DebugLogging: true});
    

## Troubleshooting

This section lists issues that are specific to profiling Go applications. See [Troubleshooting](https://docs.cloud.google.com/profiler/docs/troubleshooting) for help with common problems. 

Behavior | Cause | Solution  
---|---|---  
CPU time profiles aren't collected for applications built with `-buildmode=c-archive`. Heap, contention, and thread profiles are collected. [GitHub issue](https://github.com/googleapis/google-cloud-go/issues/993) | By default, CPU profiling isn't enabled for Go applications when the `-buildmode` flag is `c-archive` or `c-shared`. | Add a call to  
`signal.Notify(make(  
chan os.Signal), syscall.SIGPROF)` before calling `profiler.Start`.  
[Response to GitHub issue.](https://github.com/googleapis/google-cloud-go/issues/993#issuecomment-387209470)  
  
## Running with Linux Alpine

The Go profiling agent for Linux Alpine is supported only for Google Kubernetes Engine configurations.

### Authentication error

If you use Docker images that run with [Linux Alpine](https://alpinelinux.org) (such as `golang:alpine` or just `alpine`), you might see the following authentication error:
    
    
    connection error: desc = "transport: authentication handshake failed: x509: failed to load system roots and no roots provided"
    

Note that to see the error you must have agent logging enabled. By default the agent for Go doesn't output any log messages. 

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
