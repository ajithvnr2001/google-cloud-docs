---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/expand-persistent-volumes/
title: Manage Cassandra persistent volume size \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:08:41.855678+00:00
---

# Manage Cassandra persistent volume size  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/expand-persistent-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage Cassandra persistent volume size Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/expand-persistent-volumes.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/expand-persistent-volumes.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/expand-persistent-volumes.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/expand-persistent-volumes.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/expand-persistent-volumes.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/expand-persistent-volumes.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/expand-persistent-volumes.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/expand-persistent-volumes.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/expand-persistent-volumes.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/expand-persistent-volumes.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/expand-persistent-volumes.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/expand-persistent-volumes.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/expand-persistent-volumes.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/expand-persistent-volumes.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/expand-persistent-volumes.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/expand-persistent-volumes.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/expand-persistent-volumes.html)



This process allows you to expand the persistent volumes used by the Apigee hybrid Cassandra database to accommodate greater storage needs without needing to create new nodes just to provide more storage. 

##  Overview 

The Apigee hybrid `cassandra` component uses persistent volumes to store data. Persistent volume size is defined during installation and initial configuration. This initial storage size is an immutable value and cannot be changed. Therefore, any new node added to the cluster will use the same persistent volume size.

It is possible to increase the size of the existing persistent volume by making the changes directly on the Persistent volume Claim. New nodes will still use the smaller initial persistent volume size.

If your hybrid Cassandra database is nearing its storage capacity, you can use this procedure to expand the existing persistent volumes and allow new nodes to expand their persistent volumes as well.

**Note:** This process only applies to Kubernetes storage classes that support PersistentVolume expansion. See the **[Allow Volume Expansion list](https://kubernetes.io/docs/concepts/storage/storage-classes/#allow-volume-expansion)** in the Kubernetes documentation. 

If you do not know what storage class your hybrid installation uses, you can check with the following command. 
    
    
    kubectl -n APIGEE_NAMESPACE get sc standard -o json | grep 'provisioner'

The output will look something like: 
    
    
        "provisioner": "kubernetes.io/gce-pd",

Where `gce-pd` is an abbreviation for the _gcePersistentDisk_ storage class. You can find a list of storage class abbreviations in the **[Parameters list](https://kubernetes.io/docs/concepts/storage/storage-classes/#parameters)** in the Kubernetes documentation. 

## Expand Cassandra persistent volumes

  1. Update the volume size to the desired size: 
         
         kubectl -n APIGEE_NAMESPACE edit pvc

  2. Check the updated volume capacity: 
         
         kubectl get pvc -n APIGEE_NAMESPACE
         
         NAME                                       STATUS  VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
         cassandra-data-apigee-cassandra-default-0  Bound   pvc-92234ba7-941b-4dab-82c6-8a5288a2c8d4   **500Gi**      RWO            standard       21m
         cassandra-data-apigee-cassandra-default-1  Bound   pvc-6be911fc-91f7-465d-a02e-933428ee10b2   **500Gi**      RWO            standard       20m
         cassandra-data-apigee-cassandra-default-2  Bound   pvc-14ba34e4-fd5c-4d59-8413-a331dcad3404   **500Gi**      RWO            standard       19m
         

  3. Backup, delete and recreate the statefulset with the new storage size. The following commands creates a configuration file `apigee-cassandra-default.yaml` you can use to capture the current Cassandra configuration. You then modify and apply this configuration: 
     1. kubectl -n APIGEE_NAMESPACE get sts apigee-cassandra-default -o yaml > apigee-cassandra-default.yaml

     2. kubectl -n APIGEE_NAMESPACE delete sts --cascade=orphan apigee-cassandra-default

     3. Check that the `delete` operation is complete: 
            
            kubectl get sts -n APIGEE_NAMESPACE

Your output should look like: 
            
            No resources found in apigee namespace.

     4. Update the storage size in the `apigee-cassandra-default.yaml` file with the new storage size. This must match the size you intend to apply in your `overrides.yaml`. For example: 
            
            resources:
                    requests:
                      storage: 500Gi

     5. Re-apply the statefulset configuration with the updated storage size: 
            
            kubectl apply -f apigee-cassandra-default.yaml

     6. Verify that statefulset was re-created correctly: 
            
            kubectl get sts -n APIGEE_NAMESPACE

Your output should look something like: 
            
            NAME                       READY   AGE
            apigee-cassandra-default   3/3     6m56s

  4. Update the your overrides file with new volume size that you specified when you edited the pvc: 
         
         cassandra:
           storage:
             storageSize: 500Gi

See [`cassandra.storage.capacity`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/config-prop-ref#cassandra-storage-capacity) for more details.

  5. Apply the updated configuration to the cluster: 
         
         helm upgrade datastore apigee-datastore/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "datastore" has no deployed releases`, replace `upgrade` with `install` and try the command again.
  6. Check if the newly created sts has the updated storage size: 
         
         kubectl get sts -n APIGEE_NAMESPACE apigee-cassandra -o yaml |grep storage
         
         storage: 500Gi

  7. Check if C* pods data volume got updated with new size: 
         
         kubectl exec -n APIGEE_NAMESPACE -it apigee-cassandra-default-0 -- df -h|grep "/opt/apigee/data"
         
         /dev/sdb         99G   69M   99G   1% /opt/apigee/data




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
