---
url: https://docs.cloud.google.com/application-integration/docs/marketplace/create-vm-deploy-tf/
title: Create a Terraform deployment module for the VM \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:44.926534+00:00
---

# Create a Terraform deployment module for the VM  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/marketplace/create-vm-deploy-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Terraform deployment module for the VM

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to create a virtual machine (VM) and Terraform deployment module for the VM.

### Create the licensed VM Image

  1. To ensure that the development VM is non impacted, create a copy of the disk used in the VM by running the following gcloud command: 
         
         gcloud compute disks create CLONE_DISK \ --description="cloned disk" \ --source-disk=projects/PROJECT/zones/ZONE/disks/SOURCE_VM_DISK

  2. Create the clone of the VM. For information, see [Create a VM similar to an existing VM](https://cloud.google.com/compute/docs/instances/create-vm-from-similar-instance).
  3. In the **Advanced options** section, attach the cloned disk.
  4. Create the VM.
  5. Verify that the server is running for this VM. The startup script ensures that the VM is running.
  6. Stop and remove connector-service in docker.
  7. Remove the home directory and any other file which is not required for running the server. The same disk will be used for creating the VM image and will be accessible by customers later. This VM must only have libraries required for running the service.
  8. Edit the VM and select the deletion rule to **Keep disk**
  9. Delete this VM.
  10. For creating the licensed image, get the license from the producer portal. Visit [Producer portal](https://console.cloud.google.com/producer-portal?project=). **Note:** If you can't access Producer Portal, verify that you've selected the correct project. If you still can't access it, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Application Integration](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  11. Create a new Virtual Machine product. Visit the **Deployment Package** section and copy the VM license.
  12. To create the licensed VM image, run the following command:
    
    gcloud compute images create VM_IMAGE_NAME \
     --project PUBLIC_PROJECT_NAME \
     --source-disk projects/DEV_PROJECT_NAME/zones/ZONE/disks/SOURCE_VM_DISK \
     --licenses LICENSE \
     --description VM_IMAGE_DESCRIPTION

For more information, see [Building your VM](https://cloud.google.com/marketplace/docs/partners/vm/build-vm-image). 




### Create a terraform deployment module

Marketplace provides the [Autogen tool](https://github.com/GoogleCloudPlatform/marketplace-autogen) to generate the terraform modules for the deployment of VM image on Marketplace. 

This tool uses [Autogen proto definition](https://github.com/GoogleCloudPlatform/marketplace-autogen/blob/master/java/com/google/cloud/deploymentmanager/autogen/autogen.proto) to generate the deployment. For more information, see [Example config](https://github.com/GoogleCloudPlatform/marketplace-autogen/blob/master/example-config/solution.yaml). 

  1. Add the details of your solution:
    
    solutionInfo:
      name:   packagedSoftwareGroups:
        - type: SOFTWARE_GROUP_OS
          components:
            - name: Ubuntu
              version: 16.04 LTS
        - components:
            - name: Apache
              version: 2.4.23

  2. For connectors, create a module with a VM. Enter the project name, VM image name and [labels](https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking) for the image in your public project.
  3. Use n2d-standard-2 as the default machine type with min CPU as 2 and RAM as 8 Gb. N2d-standard is optimal for medium traffic web servers. The default VM can be set with 2 cores. If customers expect higher traffic, this can be changed during the VM creation from the Marketplace. For information about pricing for different machine types, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing#vm-instance-pricing). 
         
         machineType:
               # Check http://cloud.google.com/compute/docs/machine-types for all available types
               defaultMachineType:
                 gceMachineType: n2d-standard-2
               # Minimum CPU and memory constraints for the machine type to run your solution properly
               minimum:
                 cpu: 2
                 ramGb: 8

  4. Use **pd-standard** as the default disk type. 
         
         bootDisk:
               diskType:
                 defaultType: pd-standard

  5. Add the startup script to the autogen config. Stringify the startup script and add it in bashScriptContent. 
         
         gceStartupScript:
            bashScriptContent: 

  6. Define the input fields which will be taken as input from customers during VM creation. 
         
         deployInput:
               sections:
                 # The place int he Deployment Manager config that this section will appear. More details in deployment_package_autogen_spec.proto
                 - placement: CUSTOM_TOP
                   name: CONNECTOR_SETTINGS
                   title: Connectors settings
                   description: Connectors settings
                   tooltip: Setting with which connector VM will be running
                   # List of input fields that this section has
                   fields:
                     - required: false
                       name: TEST_DATA
                       title: Test Data
                       description: Test data
                       tooltip: random data for testing
                       string_box: {}
                     - required: false
                       name: PORT
                       title: Port to run service
                       tooltip: Port to run connector service
                       string_box: {}
                     - required: false
                       name: LOG_LEVEL
                       title: Log level
                       description: Log level for the web service. Allowed values are DEBUG, INFO, WARNING, ERROR. Default is INFO
                       string_box: {}

Keep the placement as **CUSTOM_TOP** and name as **CONNECTOR_SETTINGS**. 

Define the field, and the type of input required for them. In this example, the **Test Data** and **Port to run service** fields appear for the customers of the Marketplace connector. 

  7. Define the Compute Engine metadata items. While defining the VM metadata. Map the name of the input field to the metadata key. 
         
         gce_metadata_items:
               - key: CONNECTOR_ENV_PORT
                 value_from_deploy_input_field: PORT
               - key: CONNECTOR_ENV_TEST_DATA
                 value_from_deploy_input_field: TEST_DATA
         - key: CONNECTOR_ENV_LOG_LEVEL
                 value_from_deploy_input_field: LOG_LEVEL

  8. Add the steps details which will be shown to customers post deployment. 
         
         postDeploy:
               # List of suggested action items for users, after deployment is successful
               actionItems:
                 - heading: Create the Private service attachment
                   description: Now the connector service is running on the VM, please create the PSC service attachment to create the connection. Follow https://cloud.google.com/integration-connectors/docs/configure-psc for the detailed guide.
                 - heading: Create the connection
                   description: After creating the connectors endpoint attachment, use the endpoint attachment to create a connection to the partner connector.

  9. To setup the autogen, run the following command: 
         
         alias autogen='docker run \
           --rm \
           --workdir /mounted \
           --mount type=bind,source="$(pwd)",target=/mounted \
           --user $(id -u):$(id -g) \
           gcr.io/cloud-Marketplace-tools/dm/autogen'
         
         autogen --help

  10. To generate the terraform module, run the following command: 
         
         mkdir solution_folder
         
         autogen \
           --input_type YAML \
           --single_input example-config/solution.yaml \
           --output_type PACKAGE \
           --output solution_folder

The solution_folder contains the terraform module. This module will be used while publishing products on Marketplace. 




## What's next

  * Learn how to [submit the VM image for approval](https://docs.cloud.google.com/integration-connectors/docs/marketplace/submit-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
