---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks/
title: Configure container health checks for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:53.495990+00:00
---

# Configure container health checks for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure container health checks for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

Health checks let you monitor container status and automatically restart unhealthy instances in Cloud Run worker pools. You can configure HTTP, TCP, and gRPC startup probes, along with HTTP and gRPC liveness probes, across new and existing configurations.

## Use cases

You can configure two types of health check probes:

  * _Liveness probes_ determine whether to restart a container.

    * Restarting a container in this case can increase worker pool availability in the event of bugs.
    * Liveness probes are intended to restart individual instances that can't be recovered in any other way. They should be used primarily for unrecoverable instance failures, for example, to catch a deadlock where a worker pool is running, but unable to make progress. You can require a liveness probe for every container by using [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints#require-liveness-probe).
  * _Startup probes_ determine whether the container has started.

    * When you configure a startup probe, liveness checks are disabled until the startup probe determines that the container is started, to prevent interference with the worker pool startup.
    * Startup probes are especially useful if you use liveness checks on slow starting containers, because it prevents them from being shut down prematurely before the containers are up and running.



Note that when a worker pool experiences repeated startup or liveness probe failures, Cloud Run prevents uncontrolled crash loops by limiting instance restarts to prevent.

## CPU allocation

  * CPU is always allocated when probes run.
  * All probes are billed for CPU and memory usage consumption.



## Probe requirements and behavior

Probe Type | Requirements | Behavior  
---|---|---  
TCP startup | None | If specified, Cloud Run makes a TCP connection to open the TCP Socket on the specified port. If Cloud Run is unable to establish a connection, it indicates a failure.  
  
If a startup probe does not succeed within the specified time, Cloud Run shuts down the container. The time is a maximum of 240 seconds, calculated as `failureThreshold` * `periodSeconds`, which you set when configuring the startup probe for the worker pool.  
HTTP startup | Create an HTTP health check endpoint  
Use HTTP/1 | After probe configuration, Cloud Run makes an HTTP GET request to the worker pool health check endpoint (for example, `/ready`). Any response between `200` and `400` is a success, everything else indicates failure.  
  
If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), Cloud Run shuts down the container.  
  
If the HTTP startup probe succeeds within the specified time, and you have configured an HTTP liveness probe, Cloud Run starts the HTTP liveness probe.  
HTTP liveness | Create an HTTP health check endpoint  
Use HTTP/1 | The liveness probe starts only after the startup probe is successful. After probe configuration, and any startup probe is successful, Cloud Run makes an HTTP GET request to the health check endpoint (for example, `/health`). Any response between `200` and `400` is a success, everything else indicates failure.  
  
If a liveness probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), Cloud Run shuts down the container using a `SIGKILL` signal. Any remaining requests that were still being served by the container are terminated with the HTTP status code `503`. After Cloud Run shuts down the container, Cloud Run autoscaling starts up a new container instance.  
gRPC startup | Implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run worker pool | If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), Cloud Run shuts down the container.  
gRPC liveness | Implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run worker pool | If you configure a gRPC startup probe, the liveness probe starts only after the startup probe is successful.  
  
After the liveness probe is configured, and any startup probe is successful, Cloud Run makes a health check request to the worker pool.  
  
If a liveness probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), Cloud Run shuts down the container using a `SIGKILL` signal. After Cloud Run shuts down the container, Cloud Run autoscaling starts up a new container instance.  
  
## Configure probes

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can configure HTTP, TCP, and gRPC probes using the Google Cloud console or the Cloud Run REST API:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu.

     * If you are configuring a new worker pool, click **Deploy container**.
     * If you are configuring an existing worker pool, select the worker pool, then click **Edit and deploy new revision**.
  3. If you are configuring a new worker pool, fill out the initial worker pool page, then click **Containers, Networking, Security** to expand the worker pools configuration page.

  4. In the **Container(s)** section, go to **Health checks** and click **Add health check** to open the **Add health check** configuration panel.

  5. From the **Select health check type** menu, select the type of health check you want to add.

  6. From the **Select probe type** menu, select the type of the probe you want to use, for example, HTTP or gRPC. This displays the probe configuration form.

  7. Configure the probe settings, which vary by probe type:

     * If you are using HTTP probes:

       * Use the **Path** field to specify the relative path to the endpoint, for example, `/`.

       * Select the **HTTP Headers** checkbox to specify optional custom headers. Specify the header name in the **Name** field and header value in the **Value** field. Click **Add HTTP header** to specify more headers.

     * If you are using gRPC probes, ensure that your container image implements the gRPC health check protocol. For more information, see [GRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md).

     * For both HTTP and gRPC probe types, specify the following:

       * **Initial delay** , specify the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.

       * **Period** , specify the period (in seconds) at which to perform the probe. For example, specify `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.

       * **Failure threshold** , specify the number of times to retry the probe before shutting down the container. The default value is 3.

       * **Timeout** , specify the number of seconds to wait until the probe times out. Specify a value from 1 to the smaller of 600 (1800 for GPU) and `periodSeconds`. The default is 1.

  8. Click **Add** to add the new threshold.

  9. Click **Create** or **Deploy**.




### REST API

Important: If you are configuring your Cloud Run worker pool for HTTP probes, you must also add an HTTP health check endpoint in your worker pool code to respond to the probe. If you are configuring a gRPC probe, you must also implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run worker pool.

### HTTP startup

Use the [REST API](https://docs.cloud.google.com/run/docs/reference/rpc/google.cloud.run.v2#google.cloud.run.v2.WorkerPools) to configure this.

### HTTP liveness

Use the [REST API](https://docs.cloud.google.com/run/docs/reference/rpc/google.cloud.run.v2#google.cloud.run.v2.WorkerPools) to configure this.

### gRPC startup

Use the [REST API](https://docs.cloud.google.com/run/docs/reference/rpc/google.cloud.run.v2#google.cloud.run.v2.WorkerPools) to configure this.

### gRPC liveness

Use the [REST API](https://docs.cloud.google.com/run/docs/reference/rpc/google.cloud.run.v2#google.cloud.run.v2.WorkerPools) to configure this.

## Create HTTP health check endpoints

If you configure your Cloud Run worker pool for an HTTP startup probe or liveness probe, you need to add an endpoint in your worker pool code to respond to the probe. The endpoint can have whatever name you want, for example, `/startup` or `/ready`, but the name must match the value you specify for `path` in the probe configuration. For example, if you specify `/ready` for an HTTP startup probe, specify `path` in your probe configuration as shown:
    
    
    startupProbe:
      httpGet:
        path: /ready

HTTP health check endpoints are externally accessible and follow the same principles as any other HTTP endpoints that are exposed externally.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
