---
url: https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml/
title: app.yaml Configuration File \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:02:25.115478+00:00
---

# app.yaml Configuration File  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/flexible/apis)



Send feedback 

#  app.yaml Configuration File Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

**Note:** Some [Python runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) to use the latest version of Python. 

The `app.yaml` file defines your configuration settings for your runtime as well as general app, network, and other resource settings.

Do not add `app.yaml` to the [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file. `app.yaml` might be required for deployment, and adding it to `.gcloudignore` will cause the deployment to fail.

## Syntax

The syntax of the `app.yaml` file is the [YAML format](http://www.yaml.org/). The YAML format supports comments, where any line that begins with the hash symbol (`#`) character is ignored, for example:
    
    
    # This is a comment.
    

URL and file path patterns use [POSIX extended regular expression syntax](http://en.wikipedia.org/wiki/Regular_expression), excluding collating elements and collation classes. Back-references to grouped matches (e.g. `\1`) are supported, as are these Perl extensions: `\w \W \s \S \d \D`.

## General settings

An `app.yaml` file can include these general settings. Note that some of them are required:

Name| Description  
---|---  
`build_env_variables` |  Optional. If you are using a runtime that supports [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview), you can define build environment variables in your `app.yaml` file. To learn more, see [ Using build environment variables](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app#build-env-vars).  
`runtime` |  Required. The name of the runtime environment that is used by your app. For example, to specify the runtime environment, use: 
    
    
    runtime: python

Specifying `python` selects a full implementation of the Python 2.7 or 3.7 runtime. To specify a supported version of Python or to use the new Python runtimes, see the `runtime_config` setting. These runtimes do not support any App Engine APIs. You must use the APIs available for the service you want to use, like [Google Cloud APIs](https://docs.cloud.google.com/apis).  For more information and an example, see [Python runtime](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime) and [Configuring your app with app.yaml](https://docs.cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml).   
`runtime_config` | Specifies the Python runtime version. Starting in Python version 3.8, you must specify the version of the operating system. 
    
    
    runtime_config:
        operating_system: "ubuntu24"
        runtime_version: "3.14"

  * `operating_system`: Specifies the version of the Ubuntu operating system that you want to use. Required for Python version 3.8 and later. Not supported for Python version 3.7 and earlier. See the supported Ubuntu versions and runtimes on the [Python runtimes](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime) page.
  * `runtime_version`: Optional for all runtime versions. Specifies the version of the Python runtime that you want to use. See the supported versions and the default values on the [Python runtimes](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime) page. 

  
`env: flex` | Required: Select the flexible environment.  
`entrypoint` |  The command to start your application. The entrypoint starts a process that responds to HTTP requests on the port defined by the environment variable `PORT`.   
`service: service_name` |  Required if creating a service. Optional for the default service. Each service and each version must have a name. A name can contain numbers, letters, and hyphens. In the flexible environment, the combined length of `VERSION-dot-SERVICE-dot-PROJECT_ID` (where `VERSION` is the name of your version, `SERVICE` is the name of your service, and `PROJECT_ID` is your project ID) cannot be longer than 63 characters and cannot start or end with a hyphen.  If you deploy without specifying a service name, then a new version of the default service is created. If you deploy with a service name that already exists, a new version of that service is created. If you deploy with a new service name that doesn't exist, a new service and version are created. We recommend using a unique name for each service-version combination.  **Note:** Services were previously called "modules."  
`service_account` |  Optional. The `service_account` element lets you specify a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/user-managed-service-accounts) as the identity for the version. The specified service account will be used when accessing other Google Cloud services and executing tasks.  The service account must be provided in the following format: 
    
    
    service_account: [SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com  
  
`skip_files` |  Optional. The `skip_files` element specifies which files in the application directory are not to be uploaded to App Engine. The value is either a regular expression, or a list of regular expressions. Any filename that matches any of the regular expressions is omitted from the list of files to upload when the application is uploaded.  For example, to skip files whose names end in `.bak`, add a `skip_files` section like the following: 
    
    
    skip_files:
    - ^.*\.bak$  
  
## Runtime-specific settings

See the [Python](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#interpreter) runtime page to learn more about specifying a Python interpreter using the `runtime_config` settings.

## Network settings

You can specify network settings in your `app.yaml` configuration file, for example:
    
    
    network:
      name: NETWORK_NAME
      instance_ip_mode: INSTANCE_IP_MODE
      instance_tag: TAG_NAME
      subnetwork_name: SUBNETWORK_NAME
      session_affinity: true
      forwarded_ports:
        - PORT
        - HOST_PORT:CONTAINER_PORT
        - PORT/tcp
        - HOST_PORT:CONTAINER_PORT/udp

You can use the following options when configuring network settings:

Option | Description  
---|---  
`name` | Every VM instance in the flexible environment is assigned to a [Google Compute Engine network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls) when it is created. Use this setting to specify a network name. Give the short name, not the resource path (for example, `default` rather than `https://www.googleapis.com/compute/v1/projects/my-project/global/networks/default`). If you do not specify a network name, instances are assigned to the project's default network (which has the name `default`). If you want to specify a subnetwork name, you must specify a network name.  
`instance_ip_mode` | Optional. To prevent instances from receiving an ephemeral external IP address, set to `internal` and enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). If your instance was previously deployed without this setting, or was deployed with this set to `external`, redeploying with it set to `internal` removes ephemeral external IP addresses from your instances. The `internal` setting has [limitations](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip#limitations). Default is `external`.  
`instance_tag` | Optional. A tag with that name is assigned to each instance of the service when it is created. Tags can be useful in `gcloud` commands to target an action to a group of instances. For example, see the use of the `--source-tags` and `--target-tags` flags in the [compute firewalls-create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) command.   
  
If not specified, the instance is tagged with `aef-INSTANCE_ID` when Shared VPC is not used. If Shared VPC is used, the instance is tagged with both `aef-INSTANCE_ID` and `aef-instance`.``  
`subnetwork_name` | Optional. You can segment your network and use a custom subnetwork. Ensure that the network `name` is specified. Give the short name, not the resource path (for example, `default` rather than `https://www.googleapis.com/compute/v1/projects/my-project/global/networks/default/subnetworks/default`).The subnetwork must be in the same region as the application.  
`session_affinity` | Optional. Set to `true` to configure App Engine to route multiple sequential requests for a given user to the same App Engine instance such as when storing user data locally during a session. [Session affinity](https://docs.cloud.google.com/appengine/docs/flexible/using-websockets-and-session-affinity#understanding_session_affinity) enables inspecting the value of a cookie to identify multiple requests by the same user and then directs all such requests to the same instance. If the instance is rebooted, unhealthy, overloaded or becomes unavailable when the number of instances has been scaled down, session affinity will be broken and further requests are then routed to a different instance. Note that enabling session affinity can affect your load balancing setup. This parameter is disabled by default.  
`forwarded_ports` | Optional. You can forward ports from your instance (`HOST_PORT`) to the Docker container (`CONTAINER_PORT`). `HOST_PORT` must be between 1024 and 65535 and cannot conflict with the following ports: 22, 8080, 8090, 8443, 10000, 10001, 10400-10500, 11211, 24231. `CONTAINER_PORT` must be between 1 and 65535 and cannot conflict with the following ports: 22, 10001, 10400-10500, 11211. If you only specify a `PORT`, then App Engine assumes that it is the same port on the host and the container. By default, both TCP and UDP traffic are forwarded. Traffic must be directly addressed to the target instance's IP address rather than over the appspot.com domain or your custom domain.  
  
### Advanced network configuration

You can segment your Compute Engine network into subnetworks. This allows you to enable VPN scenarios, such as accessing databases within your corporate network.

To enable subnetworks for your App Engine application:

  1. [Create a custom subnet network](https://docs.cloud.google.com/compute/docs/subnetworks#creating_a_new_network_with_custom_subnet_ranges).

  2. Add the network name and subnetwork name to your `app.yaml` file, as specified above.

  3. To establish a simple VPN based on static routing, [create a gateway and a tunnel for a custom subnet network](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-policy-based-vpns#creating_a_gateway_and_tunnel). Otherwise, see how to [create other types of VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to).




### Port forwarding

Port forwarding allows for direct connections to the Docker container on your instances. This traffic can travel over any protocol. Port forwarding is intended to help with situations where you might need to attach a debugger or profiler. Traffic must be directly addressed to the target instance's IP address rather than over the appspot.com domain or your custom domain.

By default, incoming traffic from outside your network is not allowed through the [Google Cloud Platform firewalls](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#firewalls). After you have specified port forwarding in your `app.yaml` file, you must add a firewall rule that allows traffic from the ports you want opened.

You can specify a firewall rule in the Networking Firewall Rules page in the [Google Cloud console](https://console.cloud.google.com/networking/firewalls) or [using `gcloud` commands](https://docs.cloud.google.com/compute/docs/vpc/using-firewalls).

For example, if you want to forward TCP traffic from port `2222`:

  1. In the network settings of your `app.yaml`, include:
         
         network:
           forwarded_ports:
             - 2222/tcp
         

     1. If you use the Python runtime, modify the `app.yaml` to include:
            
            entrypoint: gunicorn -b :$PORT -b :2222 main:app
            

  2. Specify a firewall rule in the [Google Cloud console](https://console.cloud.google.com/networking/firewalls) or using [`gcloud compute firewall-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) to allow traffic from any source (`0.0.0.0/0`) and from `tcp:2222`.




## Resource settings

These settings control the computing resources. App Engine assigns a [machine type](https://docs.cloud.google.com/compute/docs/machine-types) based on the amount of CPU and memory you've specified. The machine is guaranteed to have at least the level of resources you've specified, it might have more.

You can specify up to eight volumes of [tmpfs](https://www.kernel.org/doc/Documentation/filesystems/tmpfs.txt) in the resource settings. You can then enable workloads that require shared memory via tmpfs and can improve file system I/O.

For example:
    
    
    resources:
      cpu: 2
      memory_gb: 2.3
      disk_size_gb: 10
      volumes:
      - name: ramdisk1
        volume_type: tmpfs
        size_gb: 0.5
    

You can use the following options when configuring resource settings:

Option | Description | Default  
---|---|---  
`cpu` | The number of cores; it must be one, an even number between 2 and 32, or a multiple of 4 between 32 and 80. | 1 core  
`memory_gb` |  RAM in GB. The requested memory for your application, which does not include the ~0.4 GB of memory that is required for the overhead of some processes. Each CPU core requires a total memory between 1.0 and 6.5 GB. To calculate the requested memory: `memory_gb` = `cpu` * [1.0 - 6.5] - 0.4 For the example above where you have specified 2 cores, you can request between 1.6 and 12.6 GB. The total amount of memory available to the application is set by the runtime environment as the environment variable `GAE_MEMORY_MB`. | 0.6 GB  
`disk_size_gb` | Size in GB. The minimum is 10 GB and the maximum is 10240 GB. | 13 GB  
`name` |  Required, if using volumes. Name of the volume. Names must be unique and between 1 and 63 characters. Characters can be lowercase letters, numbers, or dashes. The first character must be a letter, and the last character cannot be a dash. The volume is mounted in the app container as `/mnt/NAME`.  |   
`volume_type` | Required, if using volumes. Must be `tmpfs`. |   
`size_gb` |  Required, if using volumes. Size of the volume, in GB. The minimum is 0.001 GB and the maximum is the amount of memory available in the application container and on the underlying device. Google does not add additional RAM to your system to satisfy the disk requirements. RAM allocated for tmpfs volumes will be subtracted from memory available to the app container. The precision is system dependent.  |   
  
## Split health checks

By default, split health checks are enabled. You can use periodic health check requests to confirm that a VM instance has been successfully deployed, and to check that a running instance maintains a healthy status. Each health check must be answered within a specified time interval.

An instance is unhealthy when it fails to respond to a specified number of consecutive health check requests. If an instance is not live, then it is restarted. If an instance is not ready, then it will not receive any client requests. A health check can also fail if there is no free disk space.

There are two types of health checks that you can use:

  * Liveness checks confirm that the VM and Docker container are running. App Engine restarts unhealthy instances.
  * Readiness checks confirm your instance is ready to accept incoming requests. Instances that fail the readiness check are not added to the pool of available instances.

**Warning:** Legacy health checks using the `/_ah/health` path are now deprecated, and you should migrate to [use split health checks](https://docs.cloud.google.com/appengine/docs/flexible/migrating-to-split-health-checks).

By default, HTTP requests from health checks are not forwarded to your application container. If you want to extend health checks to your application, then specify a path for liveness checks or readiness checks. A customized health check to your application is considered successful if it returns a `200 OK` response code.

### Liveness checks

Liveness checks confirm that the VM and the Docker container are running. Instances that are deemed unhealthy are restarted.

You can customize liveness check requests by adding an optional `liveness_check` section to your `app.yaml` file, for example:
    
    
    liveness_check:
      path: "/liveness_check"
      check_interval_sec: 30
      timeout_sec: 4
      failure_threshold: 2
      success_threshold: 2
    

The following settings are available for liveness checks:

Field | Default | Range (Minimum-Maximum) | Description  
---|---|---|---  
`path` | None |  | If you want liveness checks to be forwarded to your application container, specify a URL path, such as `"/liveness_check"`  
`timeout_sec` | 4 seconds | 1-300 | Timeout interval for each request, in seconds.  
`check_interval_sec` | 30 seconds | 1-300 |  Time interval between checks, in seconds. Note that this value must be greater than timeout_sec.   
`failure_threshold` | 4 checks | 1-10 |  An instance is unhealthy after failing this number of consecutive checks.   
`success_threshold` | 2 checks | 1-10 |  An unhealthy instance becomes healthy again after successfully responding to this number of consecutive checks.   
`initial_delay_sec` | 300 seconds | 0-3600 |  The delay, in seconds, after the instance starts during which health check responses are ignored. This setting applies to each newly created instance and can allow a new instance more time to get up and running. The setting delays autohealing from checking on and potentially prematurely recreating the instance if the instance is in the process of starting up. The initial delay timer starts when the instance is in RUNNING mode. For example, you may want to increase the delay if your application has initialization tasks that take a long time before it is ready to serve traffic.   
  
### Readiness checks

Readiness checks confirm that an instance can accept incoming requests. Instances that don't pass the readiness check are not added to the pool of available instances.

You can customize health check requests by adding an optional `readiness_check` section to your `app.yaml` file, for example:
    
    
    readiness_check:
      path: "/readiness_check"
      check_interval_sec: 5
      timeout_sec: 4
      failure_threshold: 2
      success_threshold: 2
      app_start_timeout_sec: 300
    

The following settings are available for readiness checks:

Field | Default | Range (Minimum-Maximum) | Description  
---|---|---|---  
`path` | None |  | If you want readiness checks to be forwarded to your application container, specify a URL path, such as `"/readiness_check"`  
`timeout_sec` | 4 seconds | 1-300 | Timeout interval for each request, in seconds.  
`check_interval_sec` | 5 seconds | 1-300 |  Time interval between checks, in seconds. Note that this value must be greater than timeout_sec.   
`failure_threshold` | 2 checks | 1-10 |  An instance is unhealthy after failing this number of consecutive checks.   
`success_threshold` | 2 checks | 1-10 |  An unhealthy instance becomes healthy after successfully responding to this number of consecutive checks.   
`app_start_timeout_sec` | 300 seconds | 1-1800 |  This setting applies to new deployments, not individual VMs. It specifies the maximum time in seconds allowed for a sufficient number of instances in a deployment to pass health checks. If this duration is exceeded then the deployment fails and is rolled back. The timer starts when the Compute Engine instances have been provisioned and the Load Balancer backend service has been created. For example, you might want to increase the timeout if you wish to provide longer timeouts during deployments for a sufficient number of instances to become healthy.   
  
### Health check frequency

To ensure high availability, App Engine creates redundant copies of each health checker. If a health checker fails, a redundant one can take over with no delay.

If you examine the `nginx.health_check` logs for your application, you might see health check polling happening more frequently than you have configured, due to the redundant health checkers that are also following your settings. These redundant health checkers are created automatically and you cannot configure them.

## Service scaling settings

The keys used to control scaling of a service depend on the type of [scaling](https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed#instance_scaling) you assign to the service.

You can use either automatic or manual scaling. The default is automatic scaling.

### Automatic scaling

You can configure automatic scaling by adding an `automatic_scaling` section to your `app.yaml` file. For example:
    
    
    automatic_scaling:
      min_num_instances: 1
      max_num_instances: 15
      cool_down_period_sec: 180
      cpu_utilization:
        target_utilization: 0.6
      target_concurrent_requests: 100
    

The following table lists the settings you can use with automatic scaling:

Name | Description  
---|---  
`automatic_scaling` |  Automatic scaling is assumed by default. Include this line if you are going to specify any of the automatic scaling settings.   
`min_num_instances` |  The minimum number of instances given to your service. When a service is deployed, it is given this many instances and scales according to traffic. Must be `1` or greater, default is `2` to reduce latency. **Note:** The number of running instances may drop below this value for a short period of time during some events. If your application requires running continuously on a certain number of instances, consider [ overprovisioning](https://docs.cloud.google.com/appengine/docs/flexible/known-issues#overprovisioning).   
`max_num_instances` |  The maximum number of instances that your service can scale up to. The maximum number of instances in your project is limited by your project's [resource quota](https://docs.cloud.google.com/compute/docs/resource-quotas). Default is `20`.   
`cool_down_period_sec` |  The number of seconds that the autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. The cool-down period must be greater than or equal to 60 seconds. Default is `120`.   
`cpu_utilization` |  Use this header if you are going to specify the target CPU utilization.   
`target_utilization` |  Target CPU utilization. CPU use is averaged across all running instances and is used to decide when to reduce or increase the number of instances. Note that instances are downscaled irrespective of in-flight requests 25 seconds after an instance receives the shutdown signal. Default is `0.5`.   
`target_concurrent_requests` |  (_Beta_) Target number of concurrent connections per instance. If you specify a value for this parameter, then the autoscaler uses the average number of concurrent connections across all running instances to decide when to reduce or increase the number of instances. An instance is downscaled 25 seconds after it receives the shutdown signal, regardless of requests that are in process. If you don't specify a value for this parameter, then the autoscaler doesn't target a number of concurrent connections per instance. Connections are different from requests. A connection can be reused by a client to send multiple requests. **Note:** flexible environment has a limit of 4,096 worker connections in Nginx per instance.   
  
### Manual scaling

You can configure manual scaling by adding a `manual_scaling` section to your `app.yaml` file. For example:
    
    
    manual_scaling:
      instances: 5
    

The following table lists the settings you can use with manual scaling:

Name| Description  
---|---  
`manual_scaling` | Required to enable manual scaling for a service.  
`instances` |  The number of instances to assign to the service. **Note:** The number of running instances may drop below this value for a short period of time during some events. If your application requires running continuously on a certain number of instances, consider [ overprovisioning](https://docs.cloud.google.com/appengine/docs/flexible/known-issues#overprovisioning).   
  
## Defining environment variables

You can define environment variables in `app.yaml` to make them available to your app, for example:
    
    
    env_variables:
      MY_VAR: "my value"
    

where `MY_VAR` and `my value` are the name and value of the environment variable that you want to define and each environment variable entry is indented two spaces under the `env_variables` element.

### Using your environment variables

To retrieve and your environment variable for the Python runtime, use [`os.environ`](https://docs.python.org/3/library/os.html#os.environ).

Also see the list of [runtime environment variables](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#environment_variables) that cannot be overwritten. For example, all the environment variables that are prefixed with `GAE` are reserved for system use.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
