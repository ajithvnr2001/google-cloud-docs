---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-logging-cluster/
title: Configure logging for an AlloyDB Omni cluster \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:55.626023+00:00
---

# Configure logging for an AlloyDB Omni cluster  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-logging-cluster/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Configure logging for an AlloyDB Omni cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-logging-cluster)

AlloyDB Omni lets you redirect logs from all data path components, such as the database engine, monitor, or other services, to a dedicated disk mounted on each node. This practice is recommended for production environments to prevent logs from consuming space on the primary data disk and improve observability and debuggability. 

## Configure log redirection

To enable log redirection, you must define an `ObsDisk` in your resource specification. For the full `DBCluster` resource specification file, see [Prepare resource specifications](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster). Add the following details to the file:
    
    
    DBCluster:
      ...
      spec:
        ...
        primarySpec:
          ...
          resources:
            ...
            disks:
              - name: ObsDisk
                path: OBS_DISK_PATH
    

Replace the following:

  * `OBS_DISK_PATH`: The file system path in the database host where logs are stored. The `ObsDisk` must be an external volume individually mounted on all VM nodes provisioned within the Red Hat orchestrator to ensure log persistence and prevent logs from consuming primary data disk space. These external volumes should be sized appropriately to hold logs over a required period of time, ensuring sufficient capacity for observability and troubleshooting.



## Log configurations

The following table outlines how each AlloyDB Omni component is deployed and where its logs are generated.

Host group | Component | File names  
---|---|---  
`primary_instance_nodes` | AlloyDB Omni | `alloydbomni.log`  
`primary_instance_nodes` | AlloyDB Omni monitor | `alloydbomni_monitor.log`  
`load_balancer_nodes` | HAProxy | `haproxy.log`  
`load_balancer_nodes` if provided, else `primary_instance_nodes` | keepalived | `keepalived.log`  
`load_balancer_nodes` if provided, else `primary_instance_nodes` | pgBouncer | `pgbouncer.log`  
  
## Limitations

  * Logs are collected to the `ObsDisk`. Transferring or sending the logs to a centralized log server is unsupported.
  * Logs stored in the `ObsDisk` aren't rotated. You must configure sending logs out of `ObsDisk` and cleanup space. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
