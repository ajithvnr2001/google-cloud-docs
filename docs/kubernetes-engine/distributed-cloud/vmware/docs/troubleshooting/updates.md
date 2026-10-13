---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/updates/
title: Troubleshoot Google Distributed Cloud update issues \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:46.754833+00:00
---

# Troubleshoot Google Distributed Cloud update issues  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot Google Distributed Cloud update issues Stay organized with collections  Save and categorize content based on your preferences. 

If you have problems with updating Google Distributed Cloud, the following sections might help you to troubleshoot the issue. For more information on what settings can be updated, see [What can and cannot be updated in clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general).

## Update timeout

The update timeout is dynamically calculated based on the resources to update. However, the calculation isn't always accurate. When the update times out, errors similar to the following are displayed:

  * In the user cluster:
        
        Failed to update the cluster:...timed out waiting for the condition...
        

  * In the admin cluster:
        
        Failed to update the admin cluster:...timed out waiting for the condition...
        




This kind of timeout error can be safely ignored and you can retry the update command. If you retry the command and it times out again with the same error message, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).

## Update contains multiple changes

The `gkectl update admin` and `gkectl update cluster` commands don't allow updating multiple settings in one command. When the config contains a diff with multiple settings being changed, and an error similar to the following example is returned:
    
    
    Update summary for cluster X:
        antiAffinityGroups: enabled to be set to true from false          &config.AAGSpec{
            -   Enabled: false,
            +   Enabled: true,
              }
        user master cpu to be set to 5 from 4          config.NodePoolProps{
                Role:        "master",
                MachineType: "standard-master",
            -   CPUs:        4,
            +   CPUs:        5,
                MemoryMB:    8192,
                Replicas:    3,
                ... // 2 identical fields
                Labels:         nil,
                NodeTaints:     nil,
            -   Vsphere:        nil,
            &config.NodePoolVsphereSpec{Datastore: "lifecycle-workloads1-datastore1"},
            +   Vsphere:        nil,
                BootDiskSizeGB: nil,
                OSImageType:    "",
                ... // 5 identical fields
              }
    
    Exit with error:
    Failed to update the cluster: the update contains multiple changes. Please
    update only one feature at a time
    

This error could happen for various reasons, including the following:

  * A mistake or misconfiguration.
  * You ran `gkectl upgrade` before with the configuration diff, and expected the changes to be applied. 
    * `gkectl upgrade` doesn't apply any configuration diffs except the version bump.
  * You edited the configuration for another feature update before, but forgot to run the `gkectl update` command.



If you encounter this behaviour, review the diff in the error message and update the required settings one by one with multiple `gkectl update` commands. To help identify changes, you can use `gkectl get-config` to [generate configuration files from a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster) and view the existing state and configuration.

## Unsupported changes

The `gkectl update cluster` and `gkectl update admin` commands ignore unsupported changes, and display error messages similar to the following examples:
    
    
    detected unsupported changes: (-current +desired)
        ...
    -   AdvancedNetworking:       &true,
    +   AdvancedNetworking:       &false,
        ...
    , which will be ignored
    

If you encounter this behaviour, review the diff in the error message and perform the following actions:

  * If the change is unintended, edit the config YAML file and update with only the correct, intended changes. 
    * In the previous example, if you didn't intend to disable `AdvancedNetworking`, set `advancedNetworking: true` in the config YAML file.
  * If the change is intended, the error indicates that the change isn't supported. Perform one of the following actions: 
    * Recreate the cluster if applicable.
    * Reach out to [Google Support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).



## OS image doesn't exist

The `gkectl update cluster` and `gkectl update admin` commands might fail with `OS Images` preflight check failures similar to the following examples:

  * In the user cluster:
        
        - Validation Category: OS Images
            - [FAILURE] User cluster OS images exist: os images  [xxxx] don't exist,
            please run `gkectl prepare` to upload os images.
        

  * In the admin cluster:
        
        - Validation Category: OS Images
            - [FAILURE] Admin cluster OS images exist: os images [xxxx] don't exist,
            please run `gkectl prepare` to upload os images.
        




These errors can happen if the OS image was removed unexpectedly in your vCenter environment, such as by a periodical cleanup job.

To re-import the import OS images, run the `gkectl prepare` command, as follows:
    
    
    gkectl prepare \
        --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --skip-upload-container-images
    

## Not enough datastore free space for new node pools

When you add new node pools, the `gkectl update cluster` command might fail with `VSphere Datastore FreeSpace` preflight check errors similar to the following example:
    
    
      - [FAILURE] VSphere Datastore FreeSpace: vCenter datastore: xxxx insufficient
      FreeSpace, requires at least xxx  GB
    

This failure indicates that the datastore doesn't have sufficient free space to run the new node pools. Use one of the following options helps to provide space for the operation to succeed:

  * Free up space from the datastore.
  * Configure a different `nodePools[].vsphere.datastore` datastore for the node pool.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
