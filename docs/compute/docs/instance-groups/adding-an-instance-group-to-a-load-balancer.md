---
url: https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer/
title: Add an instance group to a load balancer \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:06.465496+00:00
---

# Add an instance group to a load balancer  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add an instance group to a load balancer Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add an existing managed instance group (MIG) to the backend service or target pool of a load balancer.

A load balancer distributes user traffic which helps in reducing the risk of experiencing performance issues in your application. Cloud Load Balancing uses [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups), both managed and unmanaged, to serve traffic. Depending on the [type of load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) you are using, you can add instance groups to a target pool or backend service.

For information about creating a specific type of load balancer with a MIG backend, see the [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) documentation.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Add a managed instance group to a backend service

A backend service is necessary for creating most types of load balancers.

A backend service can contain multiple backends. An instance group is a type of backend. The instances in the instance group respond to traffic from the load balancer. The backend service in turn knows which instances it can use, how much traffic they can handle, and how much traffic they are currently handling. In addition, the backend service monitors health checking and does not send new connections to unhealthy instances.

Use these instructions to add a managed instance group to a backend service.

###  Console 

  1. Go to the Load balancing page in the Google Cloud console. 

[Go to the Load balancing page](https://console.cloud.google.com/net-services/loadbalancing/backends/list)

  2. Click the name of the backend service to which you are adding the managed instance group.
  3. Click **Edit**.
  4. Click **+Add backend**.
  5. Select the instance group you want to add.
  6. Edit any optional settings you want to change.
  7. Save your changes.



###  gcloud 

Use the [`add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend):
    
    
        gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
            --instance-group=INSTANCE_GROUP \
            [--instance-group-region=INSTANCE_GROUP_REGION | --instance-group-zone=INSTANCE_GROUP_ZONE] \
            --balancing-mode=BALANCING_MODE
    

Balancing mode support differs based on the type of load balancer. For the complete list, see [Balancing mode available for each load balancer](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution).

Additional parameters are required depending on the balancing mode of the managed instance group. For more information, see the [`add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) in the SDK.

###  REST 

To add a backend service using the REST API, see [backendServices](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).

### Limitations

[Load balancing](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a regional MIG doesn't support the `max-rate` target capacity in `RATE` and `UTILIZATION` balancing modes. To learn more about the usage guidelines for each load balancer, see [Balancing modes and target capacity settings](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode-combos). 

## Add a managed instance group to a target pool

A target pool is an object that contains one or more virtual machine instances. A target pool is used in [regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network), where the load balancer forwards user requests to the attached target pool. The instances that are part of that target pool serve these requests and return a response. You can add a managed instance group to a target pool so that when instances are added or removed from the instance group, the target pool is also automatically updated with the changes.

Before you can add a managed instance group to a target pool, the target pool must exist. For more information, see the documentation for [Adding a target pool](https://docs.cloud.google.com/compute/docs/load-balancing/network/target-pools#add_a_target_pool).

To add an existing managed instance group to a target pool, follow these instructions. This causes all VM instances that are part of the managed instance group to be added to the target pool.

**Note:** While the instance is being added, the instance's `currentAction` will change to [`REFRESHING`](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers#currentActions.refreshing). You can not use the instance while it is currently `REFRESHING` but you can use the [`wait-until-stable`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable) command to poll the instance until it becomes stable.

###  Console 

  1. Go to the Target Pools page in the Google Cloud console. 

[Go to the Target Pools page](https://console.cloud.google.com/net-services/loadbalancing/advanced/targetPools/list)

  2. Click the target pool you want to add the instance group to.
  3. Click the **Edit** button.
  4. Scroll down to the **VM instances** section and click on **Select instance groups**.
  5. Select an instance group from the drop-down menu.
  6. Save your changes.



###  gcloud 

Use the [`set-target-pools` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools):
    
    
    gcloud compute instance-groups managed set-target-pools INSTANCE_GROUP \
            --target-pools TARGET_POOL,..

where:

  * `INSTANCE_GROUP` is the name of the instance group.
  * `TARGET_POOL,..` is the name of one or more target pools to add this instance group to.



###  REST 

Call the `setTargetPools` method for a [regional MIG](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/setTargetPools) or [zonal MIG](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/setTargetPools). For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/regionInstanceGroupManagers/INSTANCE_GROUP/setTargetPools

where:

  * `PROJECT_ID` is the project ID for this request.
  * `REGION` is the region for the instance group.
  * `INSTANCE_GROUP` is the name of the instance group.



The request body should contain a list of URIs to the target pools you want to add this group. For example:
    
    
    {
      "targetPools": [
        "regions/us-central1/targetPools/example-targetpool-1",
        "regions/us-central1/targetPools/example-targetpool-2"
      ]
    }

## Assign named ports to managed instance groups

Named ports are key-value pairs that represent a port's name and number. The port name represents a name of a service or application. The port number represents the port that service or application runs on.

Named ports are used by Cloud Load Balancing. Load balancers that act as proxies subscribe to a single named port in their backend service configuration. The port's name is translated to a port number based on the named port's mapping of each instance group backend.

For example, a backend service can subscribe to a port that is named `http-port`. The backend instance group can have a port named `http-port:80`. The backend instance group instructs the load balancer to send traffic to a VM in the group on port 80 using a protocol (such as TCP). The protocol is defined in the load balancer's backend service.

Named ports are simple metadata used by [proxy load balancers](https://docs.cloud.google.com/load-balancing/docs/backend-service#named_ports). Named ports do not control network or firewall resources in Compute Engine.

### Multiple port numbers for a named port

You can assign multiple ports for each service name. You can also assign multiple service names for each port.

Keep in mind the following points:

  * Traffic is balanced between all ports with the same port name.
  * A given backend service can only forward traffic to one named port at a time.
  * If you use multiple port numbers for a named port, the ports must all be for the same application.

For example, `http:80,http:8080` works, but `http:80,http:443` doesn't work because port 80 generally doesn't support TLS.




You can assign multiple named ports in an instance group. To illustrate, consider an example backend service that subscribes to the named port `http-port`, and that has two backend instance groups:

  * `instance-group-a` with a named port of `http-port:80`
  * `instance-group-b` with a named port of `http-port:79`



This backend service sends traffic to port 80 for VMs in `instance-group-a` and port 79 for VMs in `instance-group-b`.

When you add the same instance group to multiple backend services (for multiple load balancers) and the instance group serves different ports on each load balancer, don't add all the port numbers to a single named port. Instead create a unique named port and map it to a set of ports that each backend service should serve.

For example, suppose you have three applications, each with its own load balancer. Each application has its own port number: 81 for `app1`, 82 for `app2`, and 83 for `app3`. Assuming that all three backend services are using a common instance group, assign the named ports for this instance group as `[app1:81, app2:82, app3:83]`.

### Named ports and health checks

For a named port with multiple port numbers on a backend service to work in an external Application Load Balancer or an internal Application Load Balancer, the health check must have the `--use-serving-port` flag instead of a specific port number. This option is not available in the Google Cloud console. To set `--use-serving-port`, you must use the Google Cloud CLI or the API.

For example, suppose you have an application that load balances the traffic on three different ports (81, 82, 83) on the same backend service with a single instance group. You can assign the ports for this instance groups as `[app:81, 82, 83]`. The health check in this scenario must have the `--use-serving-port` flag.

For more information, see the [load balancing health check documentation](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_port_specification).

### Named ports and firewall rules

Named ports do **not** create or modify Google Cloud [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls). To permit traffic to backend VMs, you must still create the necessary firewall rules.

### Named ports and backend services

In addition to the instance group configuration, you must also configure the backend service. For example, suppose you set the named port on an instance group with the name `my-service-name` and the port `8888`:
    
    
    gcloud compute instance-groups set-named-ports my-unmanaged-ig \
        --named-ports=my-service-name:8888
    

Then you must refer to the named port in the backend service configuration with the `--port-name` on the backend service set to `my-service-name`:
    
    
    gcloud compute backend-services update my-backend-service \
        --port-name=my-service-name
    

### Create named ports

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroups.update` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group where you want to specify named ports. A page opens with the instance group properties.
  3. Click **Edit** to modify this managed instance group.
  4. In the **Port mapping** section, click **Add port** , and enter the desired port name and the port numbers that you want to associate with that name. If you need more entries, click **Add port** again.
  5. Click **Save** to save your changes and apply the named ports to the instances in the managed instance group.



###  gcloud 

For managed instance groups, set one or more named ports using the [`instance-groups managed set-named-ports` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports). For unmanaged groups, use the [`instance-groups set-named-ports` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/set-named-ports).
    
    
    gcloud compute instance-groups managed set-named-ports INSTANCE_GROUP \
          --named-ports PORT_NAME:PORT,PORT_NAME:PORT

For example:
    
    
    gcloud compute instance-groups managed set-named-ports INSTANCE_GROUP \
          --named-ports name1:80,name2:8080

To assign multiple ports to each service name or multiple names for each service, create more than one entry for each name or port. For example, if ports `10`, `20`, and `80` are for the same application, you can assign `name1` to all of those ports. Additionally, you might assign two names, `name2` and `name3` to port `8080`. Finally, you might assign port `9000` to `name4`, as in the following example:
    
    
    gcloud compute instance-groups managed set-named-ports INSTANCE_GROUP \
          --named-ports name1:10,name1:20,name1:80,\
                        name2:8080,name3:8080,\
                        name4:9000

Check the named ports assignments for a managed instance group using the `get-named-ports` command:
    
    
    gcloud compute instance-groups managed get-named-ports INSTANCE_GROUP
    
    
    NAME  PORT
    name1 10
    name1 20
    name1 80
    name2 8080
    name3 8080
    name4 9000

###  REST 

The [`instanceGroupManagers` API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers) doesn't offer a `setNamedPorts` API method. Instead, use the [`instanceGroups` API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/setNamedPorts) to perform this task.

Construct a request to the `instanceGroups` API and include the name of the instance group. Obtain the current `fingerprint` value for the instance group by [getting information about a specific group](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties). Include the `fingerprint` and one or more `namedPorts` value pairs in the request body:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroups/INSTANCE_GROUP/setNamedPorts
    
    {
      "fingerprint": "42WmSpB8rSM=",
      "namedPorts": [
        {
           "name": "PORT_NAME",
           "port": PORT_NUMBER
        },
        {
           "name": "PORT_NAME",
           "port": PORT_NUMBER
        }
      ]
     }
     

For example, if ports `10`, `20`, and `80` are for the same application, you can assign `name1` to all of those ports. Additionally, you might assign two names, `name2` and `name3` to port `8080`. Finally, you might assign port `9000` to `name4`, as in the following example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-group/setNamedPorts
    
    {
       "fingerprint": "42WmSpB8rSM=",
       "namedPorts": [
          {
           "name": "name1",
           "port": 8080
          },
          {
           "name": "name2",
           "port": 9000
          }
       ]
    }
    

To assign multiple ports to each service name, create multiple entries for that service name. For example, you can assign ports `10`, `20`, and `80` to `name1`. Also assign port `8080` to `name2`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-group/setNamedPorts
    
    {
       "fingerprint": "42WmSpB8rSM=",
       "namedPorts": [
          {
           "name": "name1",
           "port": 10
          },
          {
           "name": "name1",
           "port": 20
          }
          {
           "name": "name1",
           "port": 80
          }
          {
           "name": "name2",
           "port": 8080
          }
          {
           "name": "name3",
           "port": 80
          }
          {
           "name": "name4",
           "port": 8080
          }
       ]
    }
    

To list the named ports that are already assigned to a managed instance group, construct a `GET` request that points to the group:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP
    

## What's next

  * Try the tutorial, [Using load balancing for highly available apps](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-load-balancing).
  * [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates) that you can use for a managed instance group.
  * Create a [regional managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).
  * Enable [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) for your managed instance group.
  * Enable [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) for your managed instance group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
