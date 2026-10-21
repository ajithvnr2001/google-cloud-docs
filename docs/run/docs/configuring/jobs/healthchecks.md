---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/healthchecks/
title: Configure container health checks for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:07:07.535819+00:00
---

# Configure container health checks for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/healthchecks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure container health checks for jobs Stay organized with collections  Save and categorize content based on your preferences. 

Startup probes let you verify that a container has successfully initialized before running workloads in Cloud Run jobs. You can configure HTTP, TCP, or gRPC probes for both new and existing jobs to detect startup failures early.

## Use cases

You can configure startup health check probes to determine whether the container has started and is ready to execute the job.

When a job repeatedly fails to start, Cloud Run limits task restarts to prevent uncontrolled crash loops.

## Probe requirements and behavior

Probe Type | Requirements | Behavior  
---|---|---  
TCP startup | None | If Cloud Run can't establish a connection, it indicates a failure.  
  
If a startup probe does not succeed within the specified time interval, Cloud Run shuts down the container. This time interval is calculated as `failureThreshold` * `periodSeconds` and can't exceed 600 seconds (1800 for GPU).  
HTTP startup | Create an HTTP health check endpoint  
Use HTTP/1 | After you configure the probe, Cloud Run makes an HTTP GET request to the job health check endpoint (for example, `/ready`). Any response between `200` and `400` is a success, everything else indicates failure.  
  
If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), the container is shut down  
gRPC startup | Implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run job | If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), the container is shut down  
  
## Configure probes

Configure HTTP, TCP, and gRPC probes using the Google Cloud console or YAML:

### Console

Important: If you are configuring your Cloud Run job for HTTP probes, you must also add an HTTP health check endpoint in your job code to respond to the probe. If you are configuring a gRPC probe, you must also implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run job.

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. For a new job, click **Deploy container**. For an existing job, click the **Jobs** tab, click the job you want, then click **View and edit job configuration**.

  3. Expand **Containers, Networking, Security**.

  4. In the **Container(s)** section, go to **Health checks** and click **Add health check** to open the **Add health check** configuration panel.

  5. From the **Select health check type** menu, select the health check startup type.

  6. From the **Select probe type** menu, select the type of the probe, such as HTTP or gRPC. This displays the probe configuration form.

  7. Note that probe configuration varies by probe type. Configure the probe settings:

     * If you are using HTTP probes: 
       * Use the **Path** field to specify the relative path to the endpoint, for example, `/`.
       * Select the **HTTP Headers** checkbox to specify optional custom headers. Then specify the header name in the **Name** field and header value in the **Value** field. Click **Add HTTP header** to specify more headers.
     * For **Port** , specify the port where the job container listens for the probe.
     * For **Initial delay** , specify how many seconds to wait after the container starts before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * For **Period** , specify the time interval (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
     * For **Failure threshold** , specify how many times to retry the probe before shutting down the container. The default value is 3.
     * For **Timeout** , specify how many seconds to wait until the probe times out. _This value cannot exceed the value specified for`periodSeconds`._ Specify a value from 1 to 600 (1800 for GPU). The default is 1.
  8. Click **Add** to add the new threshold




### YAML

Important: If you are configuring your Cloud Run job for HTTP probes, you must also add an endpoint in your job code to respond to the probe. If you are configuring a gRPC probe, you must also implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run job.

### TCP startup

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB_NAME --format export > job.yaml

  2. Configure the `startupProbe` attribute as shown:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
          name: JOB
         spec:
          template:
            metadata:
            spec:
              containers:
              - image: IMAGE_URL
                startupProbe:
                  tcpSocket:
                    port: CONTAINER_PORT
                  initialDelaySeconds: DELAY
                  timeoutSeconds: TIMEOUT
                  failureThreshold: THRESHOLD
                  periodSeconds: PERIOD

Replace the following variables:

     * JOB with the name of your Cloud Run job.
     * IMAGE_URL with the URL of the job container image, for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * Optional: CONTAINER_PORT with the port where the job container listens for the probe.
     * DELAY with the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * Optional: TIMEOUT with the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
     * THRESHOLD with the number of times to retry the probe before shutting down the container. The default value is 3.
     * PERIOD with the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml




### HTTP startup

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB_NAME --format export > job.yaml

  2. Configure the `startupProbe` attribute as shown:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             metadata:
             spec:
               containers:
               - image: IMAGE_URL
                 startupProbe:
                   httpGet:
                     path: PATH
                     port: CONTAINER_PORT
                     httpHeaders:
                       - name: HEADER_NAME
                         value: HEADER_VALUE
                   initialDelaySeconds: DELAY
                   timeoutSeconds: TIMEOUT
                   failureThreshold: THRESHOLD
                   periodSeconds: PERIOD

Replace the following variables:

     * JOB with the name of your Cloud Run job.
     * IMAGE_URL with the URL of the job container image, for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * PATH with the relative path to the HTTP endpoint, for example, `/ready`.
     * Optional: CONTAINER_PORT with the port where the job container listens for the probe.
     * Optional: `httpHeaders` can be used to supply multiple or repeated custom headers using the HEADER_NAME and HEADER_VALUE fields as shown.
     * Optional: DELAY with number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * Optional: TIMEOUT with the number of seconds to wait until the probe times out. _This value cannot exceed the value specified for`periodSeconds`._ Specify a value from 1 to 600 (1800 for GPU). The default is 1.
     * Optional: THRESHOLD with the number of times to retry the probe before shutting down the container. The default value is 3.
     * Optional: PERIOD with the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml




### gRPC startup

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB_NAME --format export > job.yaml

  2. Configure the `startupProbe` attribute as shown:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             metadata:
             spec:
               containers:
               - image: IMAGE_URL
                 startupProbe:
                   grpc:
                     service: GRPC_SERVICE
                     port: CONTAINER_PORT
                   initialDelaySeconds: DELAY
                   timeoutSeconds: TIMEOUT
                   failureThreshold: THRESHOLD
                   periodSeconds: PERIOD

Replace the following variables:

     * JOB with the name of your Cloud Run job.
     * IMAGE_URL with the URL of the job container image, for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * Optional: GRPC_SERVICE. If set, this is used in the service field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` RPC is called.
     * Optional: CONTAINER_PORT with the port where the job container listens for the probe.
     * Optional: DELAY with the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * Optional: TIMEOUT with the number of seconds to wait until the probe times out. This value cannot exceed the value specified for periodSeconds. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
     * Optional: THRESHOLD with the number of times to retry the probe before shutting down the container. The default value is 3.
     * Optional: PERIOD with the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml




## Create HTTP health check endpoints

If you configure your Cloud Run job for an HTTP startup probe, you must add an endpoint in your job code to respond to the probe. You can use any name for the endpoint, such as, `/startup` or `/ready`. The name must match the values you specify for `path` in the probe configuration. For example, if you specify `/ready` for an HTTP startup probe, specify `path` in your probe configuration as shown:
    
    
    startupProbe:
      httpGet:
        path: /ready

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
