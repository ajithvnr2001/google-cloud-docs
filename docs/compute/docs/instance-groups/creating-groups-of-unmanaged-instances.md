---
url: https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances/
title: Group unmanaged VMs together \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:02.447215+00:00
---

# Group unmanaged VMs together  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Group unmanaged VMs together Stay organized with collections  Save and categorize content based on your preferences. 

An unmanaged instance group is a collection of virtual machine (VM) instances that reside in a single project, zone, VPC network, and subnet. An unmanaged instance group is useful for grouping together VMs that require individual configuration settings or tuning. You can use an unmanaged instance group in a load balancer's [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service#backends).

For VMs that require consistent configuration settings, you can use a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that's based on an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates). When possible, consider using managed instance groups instead of unmanaged ones. To create a managed instance group, see [Create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

You can add either type of instance group as a backend to a Google Cloud load balancer. For more information, see [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). For the number of VMs per instance group that Cloud Load Balancing supports, see [VMs per instance group](https://docs.cloud.google.com/load-balancing/docs/quotas#vms_per_instance_group).

To learn more about instance groups, see [Instance groups overview](https://docs.cloud.google.com/compute/docs/instance-groups).

**Note:** While you can create a regional managed instance group, you cannot create a regional _unmanaged_ instance group.

## Before you begin

  * Read about the [difference](https://docs.cloud.google.com/compute/docs/instance-groups) between managed and unmanaged instance groups.
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




## Working with unmanaged instance groups

### Creating groups

Unlike [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), unmanaged instance groups are just collections of distinct VMs that do not share a common instance template. You simply create a group, and add individual VMs to the group.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**.
  3. Click **New unmanaged instance group**.
  4. Enter a name for the unmanaged instance group.
  5. Under **Location** , select a region and a zone.
  6. Select a **Network** and **Subnetwork**.
  7. Under **VM instances** , select the VMs to add to this group.
  8. Click **Create**.



###  gcloud 

To create a new unmanaged instance group, use the [instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) command:
    
    
    gcloud compute instance-groups unmanaged create instance-group-name \
        --zone=zone
    

Replace the following:

  * `instance-group-name`: The name of the group you want to create.
  * `zone`: The zone where you want to create the group.



###  REST 

To create an unmanaged instance group with REST, send a `POST` request using the [instanceGroups.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/insert) method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups
    
    {
       "name": "instance-group-name"
    }
    

Replace the following:

  * `instance-group-name`: The name of the group you want to create.
  * `zone`: The zone where you want to create the group.
  * `project-id`: The project ID for the project containing the group.



When you create a new unmanaged instance group with Google Cloud CLI or REST, no VMs are added to it automatically. You can add VMs to the unmanaged instance group manually.

### Listing and describing groups

Retrieve a list of existing unmanaged instance groups.

###  Console 

In the Google Cloud console, the **Instance groups** page lists existing unmanaged and [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

###  gcloud 

To list all unmanaged instance groups in your project with the Google Cloud CLI, use [instance-groups unmanaged list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/list):
    
    
    gcloud compute instance-groups unmanaged list
    

To see information about a specific unmanaged instance group, use the [instance-groups unmanaged describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/describe) command:
    
    
    gcloud compute instance-groups unmanaged describe instance-group-name \
       --zone=zone
    

Replace the following:

  * `instance-group-name`: The name of the group to describe.
  * `zone`: The zone of the group.



###  REST 

To list instance groups with REST, send a `GET` request using the [instanceGroups.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/list) method:

**Note:** This API request lists both unmanaged and [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups
    

To obtain information about a specific unmanaged instance group with the API, send a `GET` request using the [instanceGroups.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/get) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups/instance-group-name
    

Replace the following:

  * `instance-group-name`: The name of the group to describe.
  * `zone`: The zone of the group.
  * `project-id`: The project ID for the project containing the group.



### Deleting groups

Unlike a managed instance group, deleting an unmanaged instance group does not delete any of the VMs within the group. Deleting an unmanaged instance group only removes the logical grouping of VMs.

You can't delete an instance group if the group is a backend of a Google Cloud load balancer. You must first [remove the backend from the backend service](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Select one or more unmanaged instance groups from the list.
  3. Click **Delete** to remove the groups. The groups are removed, but the VMs in the groups are not deleted.



###  gcloud 

To delete an unmanaged instance group, use the [instance-groups unmanaged delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete) command:
    
    
    gcloud compute instance-groups unmanaged delete instance-group-name \
        --zone=zone
    

Replace the following:

  * `instance-group-name`: The name of the group you want to delete.
  * `zone`: The zone of the group.



###  REST 

To delete an unmanaged instance group with REST, send a `DELETE` request using the [instanceGroups.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups/instance-group-name
    

Replace the following:

  * `instance-group-name`: The name of the group you want to delete.
  * `zone`: The zone of the group.
  * `project-id`: The project ID for the project containing the group.



## Group membership

### Adding VMs

After you create an unmanaged instance group, you can add VMs to the group. However, you can only group VMs together if the first or only network interface (`nic0`) of each VM is attached to the same VPC network. The maximum number of VMs that you can add to an unmanaged instance group is 2,000. If you want to add more than 2,000 VMs to the group, [contact support](https://cloud.google.com/support-hub/).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the instance group where you want to add your VMs. A page opens with the instance group properties and a list of VMs that are already part of the group.
  3. Click **Edit** to modify this unmanaged instance group.
  4. Under **VM instances** select one or more existing VMs to add to the group. You can only select VMs that are in the same zone, VPC network, and subnet as existing VMs.
  5. Click **Save** to add the new VMs to the group.



###  gcloud 

To add instances to an unmanaged instance group, use the [instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) command:
    
    
    gcloud compute instance-groups unmanaged add-instances instance-group-name \
        --zone=zone \
        --instances=list-of-VM-names
    

Replace the following:

  * `instance-group-name`: The name of the group to which you want to add VMs.
  * `zone`: The zone of the group.
  * `list-of-VM-names`: A comma-delimited list of VMs in the same zone, VPC network, and subnet.



###  REST 

To add VMs to an unmanaged instance group, send a `POST` request using the [instanceGroups.addInstances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/addInstances) method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups/instance-group-name/addInstances
    
       {
          "instances": [
             {
             "instance": "https://www.googleapis.com/compute/v1/projects/project-id/zones/zone/instances/instance-1-name",
             "instance": "https://www.googleapis.com/compute/v1/projects/project-id/zones/zone/instances/instance-2-name",
             ....
             }
          ]
       }
    

Replace the following:

  * `instance-group-name`: The name of the group to which you want to add VMs.
  * `zone`: The zone of the group.
  * `project-id`: The project ID for the project containing the group.
  * `instance-1-name` and `instance-2-name`: These are names of the VMs, in the same zone, VPC network, and subnet, that you want to add to the group.



### Listing VMs

You can retrieve a list of member VMs in an unmanaged instance group.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the unmanaged instance group that you want to view. A page with the list of instances that are included in the group appears.



###  gcloud 

To list the VMs in an unmanaged instance group, use the [instance-groups unmanaged list-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/list-instances) command:
    
    
    gcloud compute instance-groups unmanaged list-instances instance-group-name \
       --zone=zone
    

Replace the following:

  * `instance-group-name`: The name of the group whose members you want to list.
  * `zone`: The zone of the group.



###  REST 

To list VMs in an unmanaged instance group, send a `POST` request using the [instanceGroups.listInstances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/listInstances) method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups/instance-group-name/listInstances
    

Replace the following:

  * `instance-group-name`: The name of the group whose members you want to list.
  * `zone`: The zone of the group.
  * `project-id`: The project ID for the project containing the group.



### Removing VMs

You can remove VMs from an unmanaged instance group. Removing a VM from the instance group does not delete the VM.

**Note:** If the group is attached to backend service that has [connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) enabled, it can take up to 60 seconds _after_ the connection draining timeout for the VM instance to be removed from the unmanaged instance group.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the instance group from which you want to remove VMs. A page opens with the instance group properties and a list of VMs that are included in the group.
  3. In the list, select one or more VMs that you want to remove from the group.
  4. Click **Remove from group**. VMs that you remove from an unmanaged instance group continue to exist and run unless you stop or delete them.



###  gcloud 

To remove VMs from an unmanaged instance group, use the [instance-groups unmanaged remove-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances) command:
    
    
    gcloud compute instance-groups unmanaged remove-instances instance-group-name \
        --zone=zone \
        --instances=list-of-VM-names
    

Replace the following:

  * `instance-group-name`: The name of the group that contains instances to remove.
  * `zone`: The zone of the group.
  * `list-of-VM-names`: A comma-delimited list of VMs that you want to remove from the group.



###  REST 

To remove VMs from an unmanaged instance group with, send a `POST` request using the [instanceGroups.removeInstances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/removeInstances) method. You can simultaneously remove multiple VMs as shown below:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups/instance-group-name/removeInstances
    {
        "instances": [
            {
            "instance": "https://www.googleapis.com/compute/v1/projects/project-id/zones/zone/instances/instance-1-name",
            "instance": "https://www.googleapis.com/compute/v1/projects/project-id/zones/zone/instances/instance-2-name",
            ....
            }
        ]
    }
    

Replace the following:

  * `instance-group-name`: The name of the group that contains instances to remove.
  * `zone`: The zone of the group.
  * `project-id`: The project ID for the project containing the group.
  * `instance-1-name` and `instance-2-name`: These are names of the VMs that you want to disassociate from the group.



## Working with named ports

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
    

### Creating named ports

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance Groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the instance group where you want to specify named ports. A page opens with the instance group properties.
  3. Click **Edit** to modify this unmanaged instance group.
  4. In the **Port mapping** section, click **Add port** , and enter a port name and its number. Add or remove other named ports as necessary.
  5. Click **Save** to update the list of named ports for the unmanaged instance group.



###  gcloud 

To add named ports to an unmanaged instance group, use the [`instance-groups unmanaged set-named-ports` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/set-named-ports):
    
    
    gcloud compute instance-groups unmanaged set-named-ports instance-group-name \
        --zone=zone \
        --named-ports=port-name:port-number,...
    

To list named ports in an unmanaged instance group use the [`instance-groups unmanaged get-named-ports` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/get-named-ports):

Set one or more named ports using the `set-named-ports` command:
    
    
    gcloud compute instance-groups unmanaged set-named-ports INSTANCE_GROUP \
          --named-ports PORT_NAME:PORT,PORT_NAME:PORT

For example:
    
    
    gcloud compute instance-groups unmanaged set-named-ports INSTANCE_GROUP \
          --named-ports name1:80,name2:8080

To assign multiple ports to each service name or multiple names for each service, create more than one entry for each name or port. For example, if ports `10`, `20`, and `80` are for the same application, you can assign `name1` to all of those ports. Additionally, you might assign two names, `name2` and `name3` to port `8080`. Finally, you might assign port `9000` to `name4`, as in the following example:
    
    
    gcloud compute instance-groups unmanaged set-named-ports INSTANCE_GROUP \
          --named-ports name1:10,name1:20,name1:80,\
                        name2:8080,name3:8080,\
                        name4:9000

To remove all named ports from an unmanaged instance group with the Google Cloud CLI, use [instance-groups unmanaged set-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/set-named-ports) with an empty list of named ports:
    
    
    gcloud compute instance-groups unmanaged set-named-ports instance-group-name \
        --zone=zone \
        --named-ports=""
    

In all the examples above, replace the following if present:

  * `instance-group-name`: The name of the instance group.
  * `zone`: The zone of the group.
  * `port-name` and `port-number`: The port name and number represent a mapping from a name you choose to a port number. You can specify multiple mappings separated by commas; for example, `port-one:80,port-two:8080` is a valid list of named ports.



###  REST 

  1. Describe the instance group and note the fingerprint.

  2. To add named ports, send a `POST` request using the [instanceGroups.setNamedPorts](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/setNamedPorts) method. If you want to remove all named ports, set `namedPorts` to an empty list.
         
         POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroups/instance-group-name/setNamedPorts
         
         {
             "fingerprint": "fingerprint",
             "namedPorts": [
                 {
                 "name": "port-name",
                 "port": port-number
                 },
                 {
                 "name": "port-name",
                 "port": port-number
                 },
                 ....
             ]
         }
         

Replace the following:

     * `instance-group-name`: The name of the instance group.
     * `zone`: The zone of the group.
     * `project-id`: The project ID for the project containing the group.
     * `port-name` and `port-number`: The port name and number represent a mapping from a name you choose to a port number.
     * `fingerprint`: This is the fingerprint from the previous step.



## What's next

  * Create a [managed instance group with VMs in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).
  * Create a [managed instance group with VMs in multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).
  * Learn about [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
