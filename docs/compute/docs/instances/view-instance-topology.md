---
url: https://docs.cloud.google.com/compute/docs/instances/view-instance-topology/
title: View the physical location of a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:00:22.393822+00:00
---

# View the physical location of a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-instance-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View the physical location of a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view the physical location of the running Compute Engine instances in your Google Cloud organization.

After you create and start compute instances, you can view which physical host each compute instance runs on in a zone. Use the physical location of the compute instances in your cluster to do the following:

  * **Minimize network latency** : adjust your application or workload design to run latency-sensitive jobs on compute instances that are the closest to each other.

  * **Improve workload reliability** : distribute compute instances across separate physical hosts to limit the impact of host errors in your application.




To verify which compute instances run in your project, [view a list of compute instances](https://docs.cloud.google.com/compute/docs/instances/get-list).

## Limitations

You can view the ID of the cluster, block, sub-block, and host of compute instances that meet one or more of the following requirements:

  * The compute instance uses one of the following machine types:

    * A4X Max

    * A4X

    * A4

    * A3 Ultra

    * A3 Mega

    * A3 High with 8 GPUs

    * A3 Edge

    * H4D

  * The compute instance specifies a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

  * The compute instance belongs to a managed instance group (MIG) that specifies a [workload policy with a high throughput (`HIGH_THROUGHPUT`) type](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).




If a compute instance doesn't meet any of the preceding requirements, then you can view its host ID after you expose it, as described in this document.

## Understand compute instance topology

Each compute instance runs on a physical server, a _host_ , that exists in a server block. Each block belongs to a cluster in a zone. When you view the details of compute instances that meet specific requirements, you can understand their topology relative to other compute instances that meet the same requirements.

Compute Engine exposes the following sub-fields in the `physicalHostTopology` field of each compute instance. The more sub-fields that two running compute instances share, the closer they reside to each other.

  * **Cluster (`cluster`)**: the global name of the cluster where your compute instance exists. A _cluster_ is a high-level logical grouping of multiple hosts, which can span across several blocks, that work together as a single pool of resources.

  * **Block (`block`)**: the organization-specific ID of the block where your compute instance exists. A _block_ is a collection of multiple hosts grouped together.

  * **Sub-block (`subBlock`)**: the organization-specific ID of the sub-block where your compute instance exists. A _sub-block_ is a physical subdivision in a block, grouping hosts within a single physical enclosure.

  * **Host (`host`)**: the organization or project-specific ID of the host on which your compute instance runs. The host ID changes as follows:

    * If the compute instance specifies a compact placement policy or a workload policy, then the host ID is specific to your project.

    * If the compute instance specifies a supported machine series or you expose its host ID, then the host ID is specific to your organization.




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




### Required roles

To get the permissions that you need to verify the topology of your compute instances, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to verify the topology of your compute instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to verify the topology of your compute instances:

  * To view the details of a compute instance: compute.instances.get 
  * To view a list of compute instances: compute.instances.list 
  * To expose the host ID when you create a compute instance: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To expose the host ID when you create an instance template: compute.instanceTemplates.create 
  * To expose or hide the host ID in an existing compute instance: compute.instances.update 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Expose or hide host ID

Unless a compute instance meets specific requirements, its host ID is hidden by default. You can expose the host ID when you create or update compute instances. When you view the details of your compute instances, you can see their host IDs specific to your Google Cloud organization. You can't see the IDs of the block, sub-block, or cluster for the compute instances.

**Important:** To expose the host ID for a compute instance, you must contact your account team or the sales team to request access to this feature. If you attempt to expose the host ID without access, then your request fails.

To expose or hide the host ID in a compute instance, use one of the following methods:

  * Expose or hide host ID in an existing compute instance

  * Expose host ID in a new compute instance

  * Expose host ID in new compute instances in bulk

  * Expose host ID in a new instance template




If you want to prevent host ID exposure for one or more projects in your organization, then you can create a custom constraint. This constraint is useful when, for example, you want to run security-sensitive workloads. For more information, see [Custom constraints](https://docs.cloud.google.com/compute/docs/access/custom-constraints).

### Expose or hide host ID in an existing compute instance

You can expose or hide the host ID in an existing compute instance without a restart. If you disable the setting that exposes the host ID for a compute instance that shows the host ID by default, then one of the following occurs:

  * If the compute instance specifies a compact placement policy or a workload policy, then you see the project-specific host ID and related physical location information.

  * If the compute instance uses an H4D machine type or an A3 High machine type with 8 GPUs (or later generations), then Compute Engine ignores the request.




To expose or hide the host ID of an existing compute instance, select one of the following options:

###  gcloud 

To expose or hide the host ID for an existing compute instance, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) with one of the following flags:

  * To expose the host ID, include the `--expose-host-topology` flag:
        
        gcloud compute instances update INSTANCE_NAME \
            --expose-host-topology \
            --zone=ZONE
        

  * To hide the host ID, include the `--no-expose-host-topology` flag:
        
        gcloud compute instances update INSTANCE_NAME \
            --no-expose-host-topology \
            --zone=ZONE
        




Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `ZONE`: the zone where the compute instance exists.




###  REST 

  1. To view the properties for an existing compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where you created the compute instance.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of the compute instance.

  2. To update a compute instance to expose or hide the host ID, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). In the request body, use the `GET` request output from the previous step. However, in the `scheduling` field, you must add the `exposeHostTopology` field to expose or hide the host ID. If the `scheduling` field doesn't exist in the request output, then add it as well.

The `PUT` request is similar to the following:
         
         PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=REFRESH
         
         {
           "scheduling": {
             "exposeHostTopology": EXPOSE_HOST_ID
           },
           ...
         }
         

Replace `EXPOSE_HOST_ID` with one of the following values:

     * To expose the host ID: `true`

     * To hide the host ID: `false`




### Expose host ID in a new compute instance

To expose the host ID while you create a compute instance, select one of the following options:

###  gcloud 

To expose the host ID while you create a compute instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--expose-host-topology` flag:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --machine-type=MACHINE_TYPE \
        --expose-host-topology \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `MACHINE_TYPE`: the machine type that you want your compute instance to use.

  * `ZONE`: the zone in which you want to create the compute instance.




###  REST 

To expose the host ID while you create a compute instance, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `scheduling.exposeHostTopology` field set to `true`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "scheduling": {
        "exposeHostTopology": true
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the compute instance.

  * `ZONE`: the zone in which you want to create the compute instance.

  * `INSTANCE_NAME`: the name for the compute instance.

  * `MACHINE_TYPE`: the machine type that you want your compute instance to use.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public OS images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, then the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




### Expose host ID in new compute instances in bulk

To expose the host ID when you create compute instances in bulk, select one of the following options:

###  gcloud 

To expose the host ID when you create compute instances in bulk, run the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--expose-host-topology` flag.

For example, to create compute instances in bulk in a single zone and specify to expose their host ID, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --name-pattern="NAME_PATTERN" \
        --expose-host-topology \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of compute instances to create.

  * `MACHINE_TYPE`: the machine type that you want your compute instances to use.

  * `NAME_PATTERN`: the name pattern for the compute instances. To replace a sequence of numbers in a compute instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates compute instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of compute instances specified by `COUNT`.

  * `ZONE`: the zone in which you want to create compute instances in bulk.




###  REST 

To expose the host ID when you create compute instances in bulk, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `instanceProperties.scheduling.exposeHostTopology` field set to `true`.

For example, to create compute instances in bulk in a single zone and specify to expose their host ID, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      "count": "COUNT",
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "exposeHostTopology": true
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the compute instances.

  * `ZONE`: the zone in which you want to create the compute instances.

  * `COUNT`: the number of compute instances to create.

  * `NAME_PATTERN`: the name pattern for the compute instances. To replace a sequence of numbers in a compute instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates compute instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of compute instances specified by `COUNT`.

  * `MACHINE_TYPE`: the machine type that you want your compute instances to use.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public OS images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, then the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




### Expose host ID in a new instance template

After you create an instance template that specifies to expose the host ID, you can use the instance template to do the following:

  * Expose the host ID in the compute instances of a managed instance group (MIG) when you do the following:

    * [Create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group)

    * [Apply new compute instance configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs)

  * [Create a compute instance that exposes the host ID](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)




To expose the host ID while you create an instance template, select one of the following options:

###  gcloud 

To expose the host ID while you create an instance template, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--expose-host-topology` flag.

For example, use the following command to create a regional instance template. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --expose-host-topology \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name for the instance template.

  * `REGION`: the region in which to create the instance template.

  * `MACHINE_TYPE`: the machine type that you want your compute instances to use.




###  REST 

To expose the host ID while you create an instance template, make a `POST` request to one of the following methods. In the request body, include the `properties.scheduling.exposeHostTopology` field set to `true`.

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).




For example, to create a regional instance template that exposes the host ID, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "exposeHostTopology": true
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `REGION`: the region in which you want to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public OS images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type that you want your compute instances to use.




## Verify compute instance physical location

You can only view the physical location of your running compute instances if they meet specific requirements or you expose their host IDs.

To verify the physical location of the running compute instances in your organization, use one of the following methods:

  * Verify physical location by using the Google Cloud console, gcloud CLI, or REST

  * Verify physical location by querying metadata key




### Verify physical location by using the Google Cloud console, gcloud CLI, or REST

To view the physical location for multiple compute instances at once, use the REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the compute instance that you want to view the details of. A page that gives the details of the instance appears and the **Details** tab is selected.

  3. In the **Basic information** section, check the value of the **Physical host** field.




###  gcloud 

To view the physical location of a running compute instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with the `--flatten=resourceStatus.physicalHostTopology` flag:
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --flatten=resourceStatus.physicalHostTopology \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the compute instance name.

  * `ZONE`: the zone where the compute instance exists.




The output is similar to one of the following:

  * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following:
        
        ---
        block: 3e3056e23cf91a5cb4a8621b6a52c100
        cluster: europe-west1-cluster-jfhb
        host: 1215168a4ecdfb434fd4d28056589059
        subBlock: 0fc09525cbd5abd734342893ca1c083f
        

  * If you can only view the ID of the host after you expose it, then the output is similar to the following:
        
        ---
        block: null
        cluster: null
        host: 1215168a4ecdfb434fd4d28056589059
        subBlock: null
        




###  REST 

To view the physical location of your running compute instances, make one of the following `GET` requests. When you make a request, you must include the `fields` query parameter and limit the output to the `name`, `machineType`, and `physicalHostTopology` fields of a compute instance. You must also include the `filter` query parameter and limit the results to running compute instances.

  * To view a list of your instances across all zones: [`instances.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList)
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/instances?fields=items.name,items.machineType,items.resourceStatus.physicalHostTopology&filter=status=RUNNING
        

  * To view a list of your instances in a specific zone: [`instances.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list)
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances?fields=items.name,items.machineType,items.resourceStatus.physicalHostTopology&filter=status=RUNNING
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the compute instances exist.

  * `ZONE`: the zone where the compute instances exist.




The output is similar to one of the following:

  * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following. In the following example, the compute instances `vm-01` and `vm-02` are located in the same block.
        
        {
          "items": [
            {
              "name": "vm-01",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "block": "3e3056e23cf91a5cb4a8621b6a52c100",
                  "cluster": "europe-west1-cluster-jfhb",
                  "host": "1215168a4ecdfb434fd4d28056589059",
                  "subBlock": "0fc09525cbd5abd734342893ca1c083f"
                }
              }
            },
            {
              "name": "vm-02",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "block": "3e3056e23cf91a5cb4a8621b6a52c100",
                  "cluster": "europe-west1-cluster-jfhb",
                  "host": "2326279b5ecdfc545fd5e39167698168",
                  "subBlock": "1fc18636cbd4abd623553784ca2c174e"
                }
              }
            },
            ...
          ]
        }
        

  * If you can only view the ID of the host after you expose it, then the output is similar to the following:
        
        {
          "items": [
            {
              "name": "vm-01",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "block": null,
                  "cluster": null,
                  "host": "1215168a4ecdfb434fd4d28056589059",
                  "subBlock": null
                }
              }
            },
            {
              "name": "vm-02",
              "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/machineTypes/a3-ultragpu-8g",
              "resourceStatus": {
                "physicalHostTopology": {
                  "block": null,
                  "cluster": null,
                  "host": "2326279b5ecdfc545fd5e39167698168",
                  "subBlock": null
                }
              }
            },
            ...
          ]
        }
        




If you want to refine your list of compute instances, then edit the filter expression in the [`filter` query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#body.QUERY_PARAMETERS.filter).

### Verify physical location by querying metadata key

To view the physical location of a running compute instance by querying the `physical_host_topology` metadata key, select one of the following options:

###  Linux instances 

  1. Connect to your Linux instance.

  2. Query the `physical_host_topology` metadata key by using [`curl`](https://curl.se/):
         
         user@myinst:~$ curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology
         

The output is similar to one of the following:

     * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following:
           
           {
             "block": "3e3056e23cf91a5cb4a8621b6a52c100",
             "cluster": "europe-west1-cluster-jfhb",
             "host": "2326279b5ecdfc545fd5e39167698168",
             "subBlock": "1fc18636cbd4abd623553784ca2c174e"
           }
           

     * If you can only view the ID of the host after you expose it, then the output is similar to the following:
           
           {
             "block": null,
             "cluster": null,
             "host": "2326279b5ecdfc545fd5e39167698168",
             "subBlock": null
           }
           




###  Windows instances 

  1. Connect to your Windows instance.

  2. Query the `physical_host_topology` metadata key by using the [`Invoke-RestMethod` command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod):
         
         PS C:\> 
         $value = (Invoke-RestMethod `
                 -Headers @{'Metadata-Flavor' = 'Google'} `
                 -Uri "http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology")
         $value
         

The output is similar to one of the following:

     * If you can view the ID of the cluster, block, sub-block, and host of a compute instance, then the output is similar to the following:
           
           {
             "block": "3e3056e23cf91a5cb4a8621b6a52c100",
             "cluster": "europe-west1-cluster-jfhb",
             "host": "2326279b5ecdfc545fd5e39167698168",
             "subBlock": "1fc18636cbd4abd623553784ca2c174e"
           }
           

     * If you can only view the ID of the host after you expose it, then the output is similar to the following:
           
           {
             "block": null,
             "cluster": null,
             "host": "2326279b5ecdfc545fd5e39167698168",
             "subBlock": null
           }
           




## What's next

  * Learn more about [host events in a compute instance](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).

  * Learn how to [monitor compute instances](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
