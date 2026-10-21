---
url: https://docs.cloud.google.com/run/docs/configuring/instances/healthchecks/
title: Configure container health checks for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:50.230999+00:00
---

# Configure container health checks for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/healthchecks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure container health checks for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run health checks ensure that your container instances are running correctly and are able to serve traffic. With Cloud Run health checks, you can customize when your container is ready to receive requests, and when your container should be considered unhealthy to require a restart.

## Use cases

You can configure the following types of health check probes:

  * Startup probes determine whether the container has started and is ready to accept traffic.
  * Liveness probes determine whether to restart a container. 
    * Restarting a container in this case can increase instance availability in the event of bugs.
    * Liveness probes are intended to restart individual instances that can't be recovered in any other way. They should be used primarily for unrecoverable instance failures, such as catching a deadlock where an instance is running, but is unable to make progress. You can require a liveness probe for every container by using [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints#require-liveness-probe).
    * When an instance experiences repeated probe failures, Cloud Run limits instance restarts to prevent uncontrolled crash loops.
  * Readiness probes (Preview)

Readiness probes determine when an instance in your Cloud Run instance should serve traffic. The readiness checks begin after the container's startup probe successfully passes. If an instance fails its readiness probe beyond the failure threshold value you configure, Cloud Run stops sending new traffic to it. Cloud Run doesn't terminate the instance and sends traffic back to the instance when it starts passing its readiness probe again.




Your container is required to implement the startup, liveness, and readiness probes consistently. Once the startup check passes, Cloud Run considers your container ready to serve traffic.

We recommend that you encapsulate your logic so the startup probe accounts for readiness. Since Cloud Run can route traffic to a new instance before the first readiness probe completes, make sure that passing the startup probe also ensures readiness to safely serve traffic immediately. When the startup probe succeeds, we treat the container as ready to receive traffic.

## Configure startup probes

You can configure HTTP, TCP, and gRPC probes using the Google Cloud CLI or YAML:

###  gcloud 

### TCP startup

Run the following command:
    
    
      gcloud beta run instances create INSTANCE \
          --image=IMAGE_URL \
          --startup-probe tcpSocket.port=CONTAINER_PORT,initialDelaySeconds=DELAY,failureThreshold=THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * CONTAINER_PORT (Optional): the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
  * DELAY: number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
  * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
  * THRESHOLD: the number of times to retry the probe before shutting down the container. The default value is 3.
  * PERIOD: period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.



### HTTP startup

Add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your instance code to respond to the probe. The endpoint name (for example, `/startup`, `/health` or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP instance endpoints. 

Run the following command:
    
    
      gcloud beta run instances create INSTANCE \
          --image=IMAGE_URL \
          --startup-probe httpGet.path=PATH,httpGet.port=CONTAINER_PORT,initialDelaySeconds=DELAY,failureThreshold=THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * PATH: a relative path to the HTTP endpoint, for example, `/health`.
  * CONTAINER_PORT (Optional): set to the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
  * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
  * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
  * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for periodSeconds. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
  * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.



### gRPC startup

Ensure that your container image implements the [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). 

Run the following command:
    
    
      gcloud beta run instances create INSTANCE \
          --image=IMAGE_URL \
          --startup-probe grpc.port=CONTAINER_PORT,grpc.instance=GRPC_INSTANCE,initialDelaySeconds=DELAY,failureThreshold=THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * GRPC_INSTANCE (Optional): If set, this is used in the instance field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` rpc is called.
  * CONTAINER_PORT (Optional): the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
  * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
  * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
  * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for periodSeconds. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
  * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.



### YAML

### TCP startup

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `startupProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
          name: INSTANCE
          annotations:
             run.googleapis.com/launch-stage: BETA
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

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * CONTAINER_PORT (Optional): the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
     * DELAY: number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
     * THRESHOLD: the number of times to retry the probe before shutting down the container. The default value is 3.
     * PERIOD: period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
  3. Create or update the instance using the following command: 
         
         gcloud beta run instances replace instance.yaml




### HTTP startup

Add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your instance code to respond to the probe. The endpoint name (for example, `/startup`, `/health` or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP instance endpoints. 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `startupProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
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

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * PATH: a relative path to the HTTP endpoint, for example, `/health`.
     * CONTAINER_PORT (Optional): set to the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
     * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
     * Optional: `httpHeaders` can be used to supply multiple or repeated custom headers using the HEADER_NAME and HEADER_VALUE fields as shown.
     * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for periodSeconds. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
     * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
     1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
            
            gcloud beta run instances describe INSTANCE --format export > instance.yaml




### gRPC startup

Ensure that your container image implements the [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `startupProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - image: IMAGE_URL
             startupProbe:
               grpc:
                 instance: GRPC_INSTANCE
                 port: CONTAINER_PORT
               initialDelaySeconds: DELAY
               timeoutSeconds: TIMEOUT
               failureThreshold: THRESHOLD
               periodSeconds: PERIOD

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * GRPC_INSTANCE (Optional): If set, this is used in the instance field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` rpc is called.
     * CONTAINER_PORT (Optional): the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
     * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
     * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for periodSeconds. Specify a value from 1 to 600 (1800 for GPU). The default is 1.
     * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 600 seconds (1800 for GPU). The default value is 10 seconds.
  3. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml




### The default TCP startup probe

If you don't explicitly configure a TCP startup probe for a new Cloud Run instance, Cloud Run automatically configures a TCP startup probe with the following default values:
    
    
    startupProbe:
              timeoutSeconds: 240
              periodSeconds: 240
              failureThreshold: 1
    

You can change these default values following the instructions in the probe configuration section on this page.

### Startup probe requirements and behavior

Probe Type | Requirements | Behavior  
---|---|---  
TCP startup | None | By default, Cloud Run makes a TCP connection to open the TCP Socket on the specified port. If Cloud Run is unable to establish a connection, it indicates a failure.  
  
If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), the container is shut down. See also TCP defaults.  
HTTP startup | Create an HTTP health check endpoint   
Use HTTP/1 | After probe configuration, Cloud Run makes an HTTP GET request to the health check endpoint (for example, `/health`). Any `2XX` or `3XX` response is a success, everything else indicates failure.  
  
If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), the container is shut down.  
  
gRPC startup | Implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run instance | If a startup probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), which cannot exceed 600 seconds (1800 for GPU), the container is shut down.  
  
## Configure liveness probes

You can configure HTTP and gRPC probes using Google Cloud SDK or YAML:

###  gcloud 

### HTTP liveness

Add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your instance code to respond to the probe. The endpoint name (for example, `/startup`, `/health` or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP instance endpoints. 

Run the following command:
    
    
      gcloud beta run instances deploy INSTANCE \
          --image=IMAGE_URL \
          --liveness-probe httpGet.path=PATH,httpGet.port=CONTAINER_PORT,initialDelaySeconds=DELAY,failureThreshold=THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * PATH: a relative path to the HTTP endpoint, for example, `/health`.
  * CONTAINER_PORT (Optional): set to the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
  * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
  * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
  * Optional. TIMEOUT: the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 3600.The default is 1.
  * Optional. PERIOD: the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 3600 seconds. The default value is 10 seconds.



### gRPC liveness

Ensure that your container image implements the [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). 

Run the following command:
    
    
      gcloud beta run instances deploy INSTANCE \
          --image=IMAGE_URL \
          --liveness-probe grpc.port=CONTAINER_PORT,grpc.service=GRPC_SERVICE,initialDelaySeconds=DELAY,failureThreshold=THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * GRPC_INSTANCE (Optional): If set, this is used in the instance field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` rpc is called.
  * CONTAINER_PORT (Optional): the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
  * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
  * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
  * Optional. TIMEOUT: the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 3600.The default is 1.
  * Optional. PERIOD: the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 3600 seconds. The default value is 10 seconds.



### YAML

### HTTP liveness

Add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your instance code to respond to the probe. The endpoint name (for example, `/startup`, `/health` or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP instance endpoints. 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1): 
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `livenessProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - image: IMAGE_URL
             livenessProbe:
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

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * PATH: a relative path to the HTTP endpoint, for example, `/health`.
     * CONTAINER_PORT (Optional): set to the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
     * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
     * Optional: `httpHeaders` can be used to supply multiple or repeated custom headers using the HEADER_NAME and HEADER_VALUE fields as shown.
     * Optional. TIMEOUT: the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 3600.The default is 1.
     * Optional. PERIOD: the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 3600 seconds. The default value is 10 seconds.
  3. Create or update the instance using the following command: 
         
         gcloud beta run instances replace instance.yaml




### gRPC liveness

Ensure that your container image implements the [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1): 
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `livenessProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - image: IMAGE_URL
             livenessProbe:
               grpc:
                 port: CONTAINER_PORT
                 service: GRPC_SERVICE
                 initialDelaySeconds: DELAY
                 timeoutSeconds: TIMEOUT
                 failureThreshold: THRESHOLD
                 periodSeconds: PERIOD

Replace the following: 

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * GRPC_INSTANCE (Optional): If set, this is used in the instance field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` rpc is called.
     * CONTAINER_PORT (Optional): the [container port](https://docs.cloud.google.com/run/docs/configuring/instances/containers#configure-port) used for your instance.
     * DELAY (Optional): the number of seconds to wait after the container has started before performing the first probe. Specify a value from 0 seconds to 600 seconds (1800 for GPU). The default value is 0 seconds.
     * THRESHOLD (Optional): the number of times to retry the probe before shutting down the container. The default value is 3.
     * Optional. TIMEOUT: the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 3600.The default is 1.
     * Optional. PERIOD: the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 second to 3600 seconds. The default value is 10 seconds.
  3. Create or update the instance using the following command: 
         
         gcloud beta run instances replace instance.yaml




### Liveness probe requirements and behavior

Probe Type | Requirements | Behavior  
---|---|---  
HTTP liveness | Create an HTTP health check endpoint   
Use HTTP/1 | The liveness probe starts only after the startup probe is successful. After probe configuration, and any startup probe is successful, Cloud Run makes an HTTP GET request to the health check endpoint (for example, `/health`). Any `2XX` or `3XX` response is a success, everything else indicates failure.  
  
If a liveness probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), the container is shut down using a `SIGKILL` signal. Any remaining requests that were still being served by the container are terminated with the HTTP status code `503`. After the container is shut down, Cloud Run autoscaling starts up a new container instance.  
gRPC liveness | Implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run instance | If you configure a gRPC startup probe, the liveness probe starts only after the startup probe is successful.  
  
After the liveness probe is configured, and any startup probe is successful, Cloud Run makes a health check request to the instance.  
  
If a liveness probe does not succeed within the specified time (`failureThreshold` * `periodSeconds`), the container is shut down using a `SIGKILL` signal. After the container is shut down, Cloud Run autoscaling starts up a new container instance.  
  
## Configure readiness probes

**Preview — Readiness probes**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following limitations apply to readiness probes: 

  * If you enable session affinity, Cloud Run continues to send requests to the same instance, even if its readiness check fails.



You can configure a readiness probe using the Google Cloud CLI or YAML:

###  gcloud 

### HTTP readiness

Add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your instance code to respond to the probe. The endpoint name (for example, `/startup`, `/health` or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP instance endpoints. 

Run the following command:
    
    
    gcloud beta run instances deploy INSTANCE \
        --image=IMAGE_URL \
        --readiness-probe httpGet.path=PATH,httpGet.port=CONTAINER_PORT,successThreshold=SUCCESS_THRESHOLD,failureThreshold=FAILURE_THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * PATH (Optional): the relative path to the HTTP endpoint, for example, `/are_you_ready`. The default path is `/`.
  * CONTAINER_PORT (Optional): the container port used for your instance. The default port is the main ingress port.
  * SUCCESS_THRESHOLD (Optional): the minimum consecutive successes for the probe to be considered successful after failure. The default is 2.
  * FAILURE_THRESHOLD (Optional): the number of times to retry the probe before reporting a failure, which causes the instance to stop receiving traffic. The default is 3.
  * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 300. The default is 1.
  * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 to 300. The default value is 10 seconds.



### gRPC readiness

Ensure that your container image implements the [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). 

Run the following command:
    
    
    gcloud beta run instances deploy INSTANCE \
        --image=IMAGE_URL \
        --readiness-probe grpc.port=CONTAINER_PORT,grpc.instance=GRPC_INSTANCE,successThreshold=SUCCESS_THRESHOLD,failureThreshold=FAILURE_THRESHOLD,timeoutSeconds=TIMEOUT,periodSeconds=PERIOD
    

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
  * CONTAINER_PORT (Optional): the container port used for your instance. The default port is the main ingress port.
  * GRPC_INSTANCE (Optional): If set, this is used in the instance field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` rpc is called.
  * SUCCESS_THRESHOLD (Optional): the minimum consecutive successes for the probe to be considered successful after failure. The default is 2.
  * FAILURE_THRESHOLD (Optional): the number of times to retry the probe before reporting a failure, which causes the instance to stop receiving traffic. The default is 3.
  * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 300. The default is 1.
  * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 to 300. The default value is 10 seconds.



###  YAML 

### HTTP readiness

Add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your instance code to respond to the probe. The endpoint name (for example, `/startup`, `/health` or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP instance endpoints. 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1): 
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `readinessProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           template:
             metadata:
             spec:
               containers:
               - image: IMAGE_URL
                 readinessProbe:
                   httpGet:
                     path: PATH
                     port: CONTAINER_PORT
                   successThreshold: SUCCESS_THRESHOLD
                   failureThreshold: FAILURE_THRESHOLD
                   timeoutSeconds: TIMEOUT
                   periodSeconds: PERIOD

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * PATH (Optional): the relative path to the HTTP endpoint, for example, `/are_you_ready`. The default path is `/`.
     * CONTAINER_PORT (Optional): the container port used for your instance. The default port is the main ingress port.
     * SUCCESS_THRESHOLD (Optional): the minimum consecutive successes for the probe to be considered successful after failure. The default is 2.
     * FAILURE_THRESHOLD (Optional): the number of times to retry the probe before reporting a failure, which causes the instance to stop receiving traffic. The default is 3.
     * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 300. The default is 1.
     * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 to 300. The default value is 10 seconds.
  3. Create or update the instance using the following command: 
         
         gcloud beta run instances replace instance.yaml




### gRPC readiness

Ensure that your container image implements the [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1): 
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Configure the `readinessProbe` attribute as shown:
         
         apiVersion: serving.knative.dev/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           template:
             metadata:
             spec:
               containers:
               - image: IMAGE_URL
                 readinessProbe:
                   grpc:
                     port: CONTAINER_PORT
                     instance: GRPC_INSTANCE
                   successThreshold: SUCCESS_THRESHOLD
                   failureThreshold: FAILURE_THRESHOLD
                   timeoutSeconds: TIMEOUT
                   periodSeconds: PERIOD

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * IMAGE_URL: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the repository REPO_NAME must already be created. The URL has the shape `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`.
     * CONTAINER_PORT (Optional): the container port used for your instance. The default port is the main ingress port.
     * GRPC_INSTANCE (Optional): If set, this is used in the instance field of the `grpc.health.v1.HealthCheckRequest` when the `grpc.health.v1.Health.Check` rpc is called.
     * SUCCESS_THRESHOLD (Optional): the minimum consecutive successes for the probe to be considered successful after failure. The default is 2.
     * FAILURE_THRESHOLD (Optional): the number of times to retry the probe before reporting a failure, which causes the instance to stop receiving traffic. The default is 3.
     * TIMEOUT (Optional): the number of seconds to wait until the probe times out. This value cannot exceed the value specified for `periodSeconds`. Specify a value from 1 to 300. The default is 1.
     * PERIOD (Optional): the period (in seconds) at which to perform the probe. For example `2` to perform the probe every 2 seconds. Specify a value from 1 to 300. The default value is 10 seconds.
  3. Create or update the instance using the following command: 
         
         gcloud beta run instances replace instance.yaml




### Readiness probe requirements and behavior

Probe Type | Requirements | Behavior  
---|---|---  
HTTP readiness | Create an HTTP health check endpoint   
Use HTTP/1 | The readiness probe starts only after the startup probe is successful. After probe configuration, and any startup probe is successful, Cloud Run makes an HTTP GET request to the health check endpoint (for example, `/are_you_ready`). Any `2XX` or `3XX` response is a success, everything else indicates failure.  
  
If an instance fails its readiness probe beyond the configured `failureThreshold`, Cloud Run stops routing new requests to the instance without shutting it down, and resumes routing requests once the instance passes its readiness probe (`successThreshold` consecutive times).  
gRPC readiness | Implement the [gRPC Health Checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) in your Cloud Run instance | The readiness probe starts only after any configured startup probe is successful. Cloud Run makes a gRPC health check request to the instance.  
  
If an instance fails its readiness probe beyond the configured `failureThreshold`, Cloud Run stops routing new requests to the instance without shutting it down, and resumes routing requests once the instance passes its readiness probe (`successThreshold` consecutive times).  
  
## CPU allocation

  * CPU is always allocated when probes run.
  * All probes are billed for CPU and memory usage consumption, but there is no request-based charge.



## What's next

  * Learn how to configure a [gRPC health check protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
