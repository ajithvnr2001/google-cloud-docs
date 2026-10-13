---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-and-maintain-metadata/
title: View and maintain VM metadata \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:08.009724+00:00
---

# View and maintain VM metadata  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-and-maintain-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  View and maintain VM metadata Stay organized with collections  Save and categorize content based on your preferences. 

Every virtual machine (VM) stores its metadata on a metadata server. You can add, remove, and view metadata on your Google Distributed Cloud (GDC) air-gapped appliance VMs as key-value pairs (KVPs).

You can use the metadata KVPs to store information that can help you identify your VM, such as a server name. You can access metadata from outside and within the VM, and use the metadata to pass information between different systems.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request permissions and access

To perform the tasks listed on this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-bindings) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Add or remove metadata

This section describes how to add and remove metadata from existing VM instances. You can use metadata to store arbitrary key-value pairs that you want to add to your VMs. For example, you might want to add and manage your own custom metadata to identify different environments, such as `test` and `production`.

### Add metadata

###  gdcloud 

  * Add metadata to a specific VM instance. You must include either one of the `--metadata` or `--metadata-from-file` flags in your command. You can also add both flags in the same command if required for your use case:
        
        gdcloud compute instances add-metadata VM_NAME
            [--project=PROJECT]
            [--metadata=KEY=KEY_VALUE,[,KEY=KEY_VALUE,...]]
            [--metadata-from-file=KEY=LOCAL_FILE_PATH,]
        

Replace the following:

    * `VM_NAME`: the name of the VM instance.
    * `PROJECT`: the name of the project where the VM resides. This value is optional.
    * `KEY`: the key for the metadata pair.
    * `KEY_VALUE`: the value for the metadata pair.
    * `LOCAL_FILE_PATH`: the value of the metadata pair from a local file.



###  API 

To add metadata with the API, you must use an `STS` token.

  1. Use the gdcloud CLI to generate an `STS` token:
         
         gdcloud auth print-identity-token --audiences="https://metadata.ORG_SUFFIX"
         

Replace `ORG_SUFFIX` with the organization suffix. For example, if the organization console URL is `https://console.example-org.com`, the `ORG_SUFFIX` is `example-org.com`

The output is similar to the following:
         
         STS-Bearer-QPN1nX6GVdoRKCpRx7FD-61gh6RAvWfM6sqjU2knw9n6RFn1jR2n4i1z1irH2HrMLf0tC3hqNaetYzoOBQ6hI2eS7-58_ZZGCMc_oARuX_T9Wmtwe4xlaIS97aDdu9KETEs0akoVYEsmFsWCu2Cu5pdiwjzSuWnRCMZwq9g8BmnPSck1Auf7rOfM7o2FoGE_lbLFZK4C8TCPdloDZAXYcLeNAQ
         

  2. Add metadata to a specific VM instance:
         
         curl -X POST "https://metadata.ORG_SUFFIX/virtual-machines/metadata/v1/projects/PROJECT/vm/VM_NAME" \
         -H "Authorization: Bearer STS_TOKEN \
         -H "Content-Type: application/json" \
         -d "{"metadata": {"items": [{"key": "test-key", "value": "test-value"}]}}"
         

Replace the following:

     * `ORG_SUFFIX`: the organization suffix. For example, if the organization console URL is `https://console.example-org.com`, the `ORG_SUFFIX` is `example-org.com`.
     * `VM_NAME`: the name of the VM instance.
     * `PROJECT`: the name of the project where the VM resides. This value is optional.
     * `STS_TOKEN`: the `STS` token generated from the gdcloud CLI.



### Remove metadata

###  gdcloud 

  * Remove metadata from a specific VM instance. If you want to remove all metadata entries, use the `--all` flag. You must use either one of the `--all` or `--keys` flags in your command:
        
        gdcloud compute instances remove-metadata VM_NAME
            [--project=PROJECT]
            [--keys=KEY,[KEY,...]]
            [--all]
        

Replace the following:

    * `VM_NAME`: the name of the VM instance.
    * `PROJECT`: the name of the project where the VM resides. This value is optional.
    * `KEY`: the key string for the metadata pair.



###  API 

To remove metadata with the API, you must use an `STS` token.

  1. Use the gdcloud CLI to generate an `STS` token:
         
         gdcloud auth print-identity-token --audiences="https://metadata.ORG_SUFFIX"
         

Replace `ORG_SUFFIX` with the organization suffix. For example, if the organization console URL is `https://console.example-org.com`, the `ORG_SUFFIX` is `example-org.com`.

The output is similar to the following:
         
         STS-Bearer-QPN1nX6GVdoRKCpRx7FD-61gh6RAvWfM6sqjU2knw9n6RFn1jR2n4i1z1irH2HrMLf0tC3hqNaetYzoOBQ6hI2eS7-58_ZZGCMc_oARuX_T9Wmtwe4xlaIS97aDdu9KETEs0akoVYEsmFsWCu2Cu5pdiwjzSuWnRCMZwq9g8BmnPSck1Auf7rOfM7o2FoGE_lbLFZK4C8TCPdloDZAXYcLeNAQ
         

  2. Remove metadata from a specific VM instance:
         
         curl -X POST "https://metadata.ORG_SUFFIX/virtual-machines/metadata/v1/projects/PROJECT/vm/VM_NAME" \
         -H "Authorization: Bearer STS_TOKEN" \
         -H "Content-Type: application/json" \
         -d "{"metadata": {"items": [{"key": "test-key", "value": "test-value"}]}}"
         

Replace the following:

     * `ORG_SUFFIX`: the organization suffix. For example, if the organization console URL is `https://console.example-org.com`, the `ORG_SUFFIX` is `example-org.com`.
     * `VM_NAME`: the name of the VM instance.
     * `PROJECT`: the name of the project where the VM resides.
     * `STS_TOKEN`: the `STS` token generated from the gdcloud CLI.



## Query metadata

###  gdcloud 

  * List all VM instance metadata to view metadata details:
        
        gdcloud compute instances describe VM_NAME
            [--project=PROJECT]
        

Replace the following:

    * `VM_NAME`: the name of the VM instance.
    * `PROJECT`: the name of the project where the VM resides. This value is optional.

The output is similar to the following:
    
    ...
    metadata:
      items:
      - key: Key-1
        value: val12
      - key: key2
        value:
          lksdjfhk-user1
    




###  API 

  1. Use the gdcloud CLI to generate an `STS` token:
         
         gdcloud auth print-identity-token --audiences="https://metadata.ORG_SUFFIX"
         

Replace `ORG_SUFFIX` with the organization suffix.

The output is similar to the following:
         
         STS-Bearer-QPN1nX6GVdoRKCpRx7FD-61gh6RAvWfM6sqjU2knw9n6RFn1jR2n4i1z1irH2HrMLf0tC3hqNaetYzoOBQ6hI2eS7-58_ZZGCMc_oARuX_T9Wmtwe4xlaIS97aDdu9KETEs0akoVYEsmFsWCu2Cu5pdiwjzSuWnRCMZwq9g8BmnPSck1Auf7rOfM7o2FoGE_lbLFZK4C8TCPdloDZAXYcLeNAQ
         

  2. List all VM instance metadata to view metadata details:
         
         curl "https://metadata.ORG_SUFFIX/virtual-machines/metadata/v1/projects/PROJECT/vm/VM_NAME" \
         -H "Authorization: Bearer STS_TOKEN" \
         -H "Content-Type: application/json"
         

Replace the following:

     * `ORG_SUFFIX`: the organization suffix. For example, if the organization console URL is `https://console.example-org.com`, the `ORG_SUFFIX` is `example-org.com`
     * `VM_NAME`: the name of the VM instance.
     * `PROJECT`: the name of the project where the VM resides. This value is optional.
     * `STS_TOKEN`: the `STS` token generated from the gdcloud CLI.

The output is similar to the following:
    
    ...
    metadata:
      items:
      - key: Key-1
        value: val12
      - key: key2
        value:
          lksdjfhk-user1
    




### Query metadata from within a VM

You can query VM metadata from within the VM, without having to connect to the metadata server. To do so, use the `curl` command and append the applicable metadata key to the metadata URL.

#### Query a single KVP

Query a single KVP from within a VM:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/KEY" -H "Metadata-Flavor: Google"
    

Replace `KEY` with the key for the metadata pair you want to query.

#### Query all KVP pairs with values

Query all KVP pairs from within a VM with key-values:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=true" -H "Metadata-Flavor: Google"
    

#### Query all metadata-keys with no values

Query all metadata keys from within a VM with no key-values:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=false" -H "Metadata-Flavor: Google"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
