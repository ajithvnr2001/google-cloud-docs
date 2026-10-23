---
url: https://docs.cloud.google.com/service-catalog/docs/dm-based-solution/
title: Creating a Deployment Manager-based solution \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:51.016698+00:00
---

# Creating a Deployment Manager-based solution  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/dm-based-solution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating a Deployment Manager-based solution

When creating Service Catalog solutions for users in your organization, you can create a Deployment Manager (DM) solution, which users launch using a Deployment Manager template. After you create a solution, you can share it with your users by adding it to [catalogs](https://docs.cloud.google.com/service-catalog/docs/create-catalog).

**Note:** We recommend [creating a Terraform configuration](https://docs.cloud.google.com/service-catalog/docs/terraform-configuration) to take advantage of the open-source infrastructure as code software tool.

## Before you begin

  * You must have the [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) (`roles/cloudprivatecatalogproducer.admin`) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) (`roles/cloudprivatecatalogproducer.manager`) role for the Google Cloud organization associated with the Google Cloud project which has Service Catalog enabled. If you don't have this role, contact your Organization Administrator to request access.

  * Enable the Cloud Deployment Manager and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=deploymentmanager,compute_component)




## Preparing your deployment template

To create a Deployment Manager solution in Service Catalog, you first prepare a [Deployment Manager template](https://cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template) zip file to upload, which must contain the following files:

  * A Jinja template file ending in the `.jinja` extension or a Python template file ending in the `.py` extension.
  * A [schema file](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas) ending in the `.jinja.schema` extension for a Jinja template or the `py.schema` extension for a Python template.



The name of the zip file must match the names of both the schema and Jinja or Python files. For example, if the zip file is named `android-dev-environment.zip`, the Jinja schema file inside the zip must be named `android-dev-environment.jinja.schema` and the Jinja template must be named `android-dev-environment.jinja`.

The following code sample illustrates a schema file to create a deployment form:
    
    
    
    info:
      title: Single Google Compute Engine Machine
      author: Google Inc.
      description: Creates a virtual machine based on zone and machine type selection.
    
    required:
      - machinetype
      - zone
    
    properties:
      machinetype:
        title: Machine type
        type: string
        enum:
          - n2-standard-2
          - n2-standard-4
          - n2-standard-8
          - n2-highmem-2
          - n2-highmem-4
          - n2-highmem-8
          - n2-highcpu-2
          - n2-highcpu-4
          - n2-highcpu-8
      zone:
        title: Zone
        type: string
        enum:
          - us-central1-a
          - us-central1-c
          - us-east1-b
          - us-east1-c
          - us-west1-a
          - us-west1-b
          - us-west1-c
    
    

The following code sample illustrates a Jinja file to create a persistent VM:
    
    
    
    # Creates a Persistent VM
    resources:
    - type: compute.v1.instance
      name: vm-{{ env["deployment"] }}
      properties:
        zone: {{ properties["zone"] }}
        # Note the machineType definition at the end. n2-custom-4-5120 specifies n2 machine family with 4 CPUs and 5GB (5120 MB) of RAM. For custom machine types, refer to https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type
        machineType: https://www.googleapis.com/compute/v1/projects/{{ env["project"] }}/zones/{{ properties["zone"] }}/machineTypes/{{ properties["machinetype"] }}
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            diskName: disk-{{ env["deployment"] }}
            sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-9
        networkInterfaces:
        - network: https://www.googleapis.com/compute/v1/projects/{{ env["project"] }}/global/networks/default
          # Access Config required to give the instance a public IP address
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    
    

## Creating the solution in Service Catalog

To create a Deployment Manager template-based solution:

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/catalog/admin/solutions)

  2. Click **Select** to choose the Google Cloud project.

  3. Click **CREATE SOLUTION**. In the drop-down list, select **Create a DM solution**.

  4. Enter a name, description, and tagline for your solution. The tagline is a short description of a solution that users see as they browse Service Catalog.

  5. Upload a zip file, containing the files for a deployment [configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).

  6. Optionally, upload an icon for the solution. The recommended dimensions for an icon are 80 by 80 pixels.

  7. Optionally, enter a support link and contact information for the creator.

  8. Optionally, add a link to the documentation for the solution.

  9. Click **CREATE**.




The following screenshot illustrates creating a DM-based solution:

![Create a Cloud Deployment Manager template-based solution](https://docs.cloud.google.com/static/service-catalog/images/screen-privatecatalog-create-template.png)

## Next steps

  * [Assign the solution](https://docs.cloud.google.com/service-catalog/docs/assign-solutions) to a catalog, so that users in your organization can access and deploy the solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
