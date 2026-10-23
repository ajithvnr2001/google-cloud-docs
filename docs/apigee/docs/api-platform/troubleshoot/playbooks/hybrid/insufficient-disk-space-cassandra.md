---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/insufficient-disk-space-cassandra/
title: Insufficient disk space in Cassandra \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:48.917163+00:00
---

# Insufficient disk space in Cassandra  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/insufficient-disk-space-cassandra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Insufficient disk space in Cassandra Stay organized with collections  Save and categorize content based on your preferences. 

## Symptom

Your Apigee hybrid installation process fails due to insufficient disk space for the Cassandra database. The installation process fails with the following error message:
    
    
    Error: UPGRADE FAILED: cannot patch "default" with kind ApigeeDatastore:
    Internal error occurred
    

Additionally, the Cassandra log contains a warning similar to the following: 
    
    
    WARN  [main] 2024-06-18 12:34:55,583 DatabaseDescriptor.java:579 - Only
    62.440GiB free across all data volumes. Consider adding more capacity to your
    cluster or removing obsolete snapshots

## Common diagnosis steps

Use the [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather) script to collect the logs from the Cassandra pods for review.

## Possible cause

Cause | Description  
---|---  
Out of disk space | The available disk space for Cassandra is less than 50%.  
  
### Cause 1: Out of disk space

When upgrading Apigee hybrid, ensure you have more than 50% disk space available for all Cassandra pods.

#### Diagnosis

  1. From the [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather) script, examine the output of the following command to check the total size of the volume associated with Cassandra:
         
         kubectl get pv -n APIGEE_NAMESPACE

Sample Output
         
         NAME                                     CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM                                            STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON    AGE
         pvc-0b6b2daa-d512-4780-9021-fc97293a8154 10Gi     RWO          Delete         Bound  apigee/cassandra-data-apigee-cassandra-default-1 standard-rwo    <unset>                 -        20d
         pvc-2263fc7c-e057-406a-ad60-38573733c92d 10Gi     RWO          Delete         Bound  apigee/cassandra-data-apigee-cassandra-default-2 standard-rwo    <unset>                 -        20d
         pvc-8c854fe9-adaa-440f-90d9-d15497e7f530 10Gi     RWO          Delete         Bound  apigee/cassandra-data-apigee-cassandra-default-0 standard-rwo    <unset>                 -        20d
         

  2. Check the `nodetool` status output to see the disk utilized by each Cassandra pod. The disk space utilization for Persistent Volume Claims (PVCs) assigned to Cassandra pods should not surpass 50% of the available storage capacity. Refer to the following command: 
         
         kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec apigee-cassandra-default-1 -- bash -c 'nodetool -u cassandra -pw $CASS_PASSWORD status'

Where CASS_PASSWORD is the `cassandra.auth.default.password` as mentioned in [ Configuration property reference.](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#cassandra)

Sample Output
         
         Datacenter: us-west3
         ========================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load        Tokens  Owns (effective)  Host ID                               Rack
         UN  10.10.10.1   6.69 GiB   256     100.0%            2a184030-444-4155-8375-156e87539711      a
         UN  10.10.10.2   7.42 GiB   256     53.1%             f22b66c7-4444-4000-b9c0-5a71ee6315a8     c
         UJ  10.10.10.3   7.39 GiB   256     ?                 78fb2737-4444-4468-a786-e473ead115b5     b
         UN  10.10.10.4   7.81 GiB   256     47.0%             779fcdf1-4444-4186-bcbb-2844e59629c2     b
         UN  10.10.10.5   6.91 GiB   256     53.0%             55ca07b2-4444-4967-b321-6477d50f9846     b
         UN  10.10.10.6   7.41 GiB   256     46.9%             0cf33585-444-46ce-811f-9c6376ed58ac      c
         

(Optional) Use `kubectl` to execute a command inside the Cassandra container to check the disk usage percentage.
         
         kubectl exec -it apigee-cassandra-default-0 -n apigee – df -h /opt/apigee/data
         kubectl exec -it apigee-cassandra-default-1 -n apigee – df -h /opt/apigee/data
         kubectl exec -it apigee-cassandra-default-2 -n apigee – df -h /opt/apigee/data
         

Example

The following example shows where disk space utilization is over 50%. This would cause problems for Apigee hybrid upgrades.
         
         kubectl exec -it apigee-cassandra-default-0 -n apigee -- df -h /opt/apigee/data
         
         
         Defaulted container "apigee-cassandra" out of: apigee-cassandra, apigee-cassandra-ulimit-init (init)
         Filesystem      Size    Used    Avail   Use%    Mounted on
         /dev/sdb         10G    6G      4G      60%     /opt/apigee/data
         
         
         
         
          kubectl exec -it apigee-cassandra-default-1 -n apigee -- df -h /opt/apigee/data
         
         
         Defaulted container "apigee-cassandra" out of: apigee-cassandra, apigee-cassandra-ulimit-init (init)
         Filesystem      Size    Used    Avail   Use%    Mounted on
         /dev/sdb         10G    5.9G    4.1G    59%     /opt/apigee/data
         
         
         
         
         kubectl exec -it apigee-cassandra-default-2 -n apigee -- df -h /opt/apigee/data
         
         
         Defaulted container "apigee-cassandra" out of: apigee-cassandra, apigee-cassandra-ulimit-init (init)
         Filesystem      Size    Used    Avail   Use%    Mounted on
         /dev/sdb         10G    5.6G    4.4G    56%     /opt/apigee/data
         
         
         
         




#### Resolution

If you find disk utilization is above 50%, scale the Cassandra disk capacity to ensure it is below 50% before performing an Apigee hybrid upgrade.

To expand disk capacity, see [Manage Cassandra persistent storage size](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/expand-persistent-volumes).

## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support): 

  * Your Google Cloud Project ID. 
  * Your Apigee hybrid organization.
  * The `overrides.yaml` files from both the source and new regions (remember to mask any sensitive information).
  * The outputs from the commands in [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
