---
url: https://docs.cloud.google.com/appengine/docs/flexible/debugging-an-instance/
title: Debugging an instance \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:13.409915+00:00
---

# Debugging an instance  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/debugging-an-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Debugging an instance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide is applicable to all runtimes in the flexible environment except for .NET. 

You can enable debug mode for a VM. In debug mode, principals who have the Owner, Editor, and App Engine Admin roles on the project have root access to the VM. While debug mode is turned on, the automatic rollout of operating system updates and security patches is disabled. However, the VM is still part of the load balancer pool, and continues to receive external requests.

Whenever you enable or disable debugging, a "VM instance debugging enable/disable" event appears in the Google Cloud console and the event will be logged in the VM's `/var/log/syslog.log` file.

**Important:** Any changes you make to the VM while in debug mode are temporary; you will lose your changes when you disable debug mode. VMs that are being debugged restart periodically, which can make it difficult to debug long running tasks.

## Enabling and disabling debug mode

You can use `gcloud` to enable and disable debug mode for an instance. In order to debug an instance, your role must contain the `appengine.instances.enableDebug` permission.

**Note:** To enable debug mode in the Google Cloud console, you must connect using SSH.

To enable and disable debug mode in `gcloud`:

  1. Use the [gcloud app instances enable-debug](https://docs.cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug) command to debug the VMs for a particular instance and version, as follows: 
         
         gcloud app --project PROJECT-ID instances enable-debug

Replace PROJECT-ID with your own project ID, and follow the prompts to specify the instance version to debug. 
  2. When finished debugging, disable debug mode as follows: 
         
         gcloud app --project PROJECT-ID instances disable-debug

Follow the prompts to specify the instance version 



When you disable debug mode, the VM is stopped and a new instance of your app is started, running on a clean, new VM.

## Connecting to the instance

### Console

**Note:** If [OS Login is enabled](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-os-login#checking_if_os_login_is_enabled) in project metadata, use the gcloud CLI to connect to the instance.

To connect to an instance in the console:

  1. Visit the Google Cloud console instances page for your project:

[Go to the instances page ](https://console.cloud.google.com/appengine/instances)

  2. Click **SSH** in the far right of the row containing the instance you want to access:

![](https://docs.cloud.google.com/static/appengine/docs/flexible/images/ssh_console_flex.png)

This puts the instance into debug mode, and opens an SSH session for the instance in a terminal window.

You can also select different options to start an SSH session from the drop-down list.

  3. At this point you are in the instance host, which has several [containers](https://kubernetes.io/docs/concepts/overview/) running in it. See Understanding common containers next for more information about these.

  4. In the terminal window, list the containers running in the instance: 
         
         sudo docker ps

  5. The output of the `sudo docker ps` command lists each container by row; locate the row that contains your project ID: this is the container running your code. Note the NAME of this container.

  6. Optionally, list logging information for your application by invoking: 
         
         sudo docker logs CONTAINER-NAME

  7. Start a shell in the container that is running your code: 
         
         sudo docker exec -it CONTAINER-NAME /bin/bash

  8. When finished debugging, enter `exit` to exit the container, then `exit` again to exit the SSH session.

  9. Disable debugging for your instance to allow it to resume normal operation.




### gcloud

To connect to an instance using gcloud:

  1. With the instance enabled for debugging, invoke the command: 
         
         gcloud beta app instances --project PROJECT-ID ssh INSTANCE-NAME --service SERVICE --version VERSION

  2. At this point you are in the instance host, which has several [containers](http://kubernetes.io/docs/whatisk8s/) running. See Understanding common containers next for more information about these.

  3. In the terminal window, list the containers running in the instance: 
         
         sudo docker ps

  4. The output of the `sudo docker ps` command lists each container by row; locate the row that contains your project ID: this is the container running your code. Note the NAME of this container.

  5. Optionally, list logging information for your application by invoking: 
         
         sudo docker logs CONTAINER-NAME

  6. Start a shell in the container that is running your code: 
         
         docker exec -it CONTAINER-NAME /bin/bash

  7. When finished debugging, enter `exit` to exit the container, then `exit` again to exit the SSH session.

  8. Disable debugging for your instance to allow it to resume normal operation.




## Understanding common containers

In addition to the container running your application code, your instance may also have the following containers:

Container and Source Code | Description  
---|---  
[cloud-sql](https://github.com/GoogleCloudPlatform/cloud-sql-proxy) | Ensures secure connections to your Cloud SQL instance.  
[fluentd_logger](https://github.com/GoogleCloudPlatform/google-fluentd) | Logging agent.  
[nginx_proxy](https://github.com/cloudendpoints/esp) | Proxies requests to the application.  
[opentelemetry-collector](https://github.com/GoogleCloudPlatform/appengine-sidecars-docker/tree/main/opentelemetry_collector) | Receives, processes, and exports telemetry data.  
[stackdriver-monitoring-agent](https://github.com/Stackdriver/collectd) | Collects, stores, and monitors system information.  
  
Note that these sidecar containers are subject to change without notice.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
