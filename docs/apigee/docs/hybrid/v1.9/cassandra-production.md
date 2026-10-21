---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production/
title: Configure Cassandra for production \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:19:39.785358+00:00
---

# Configure Cassandra for production  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure Cassandra for production Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-production.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-production.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-production.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-production.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-production.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-production.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-production.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-production.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-production.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-production.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-production.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-production.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-production.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-production.html)



This topic describes steps you must take to configure the Cassandra database component for an Apigee hybrid production installation. 

## Ensure high availability

Cassandra clusters need three availability zones to maintain availability in a production environment. If one zone goes down, the remaining zones will continue responding to requests while the remaining zone comes back online. If two or more zones go down, Cassandra will be unable to respond to requests until at least two zones come back online. Apigee recommends bringing zones back online within three hours to minimize the risk of missing data updates.

##  Apply Cassandra storage settings 

To apply changes to the Cassandra storage settings in your overrides file, execute the following commands: 
    
    
    $APIGEECTL_HOME/apigeectl init -f overrides/OVERRIDES_FILE
    
    
    
    $APIGEECTL_HOME/apigeectl apply -f overrides/OVERRIDES_FILE
    

##  Configure Cassandra storage settings 

For a production installation of Apigee hybrid, Google recommends that you add the following storage and heap settings to your overrides file and apply them to the cluster: 

**Note:** All Cassandra storage settings in the overrides file are per pod. See also [Scaling Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-scaling).
    
    
    cassandra:
      ...
      replicaCount: 3
      storage:
        storageclass: your-preferred-ssd-storage #If not using default storage for your cluster
        capacity: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M

### `replicaCount`

The value of `replicaCount` must be a multiple of `3`. To determine your desired `replicaCount` value, consider the following: 

  * Estimate the traffic demands for your proxies.
  * Load test and make reasonable predictions of your CPU utilization.
  * You can specify different `replicaCount` values in different regions.
  * You can expand the `replicaCount` in the future in your overrides file.



To check the current `replicaCount` setting, execute the following command on your cluster: 
    
    
    kubectl get sts -n NAMESPACE apigee-cassandra-default -o=jsonpath='{.spec.replicas}'
      

### `storageclass`

**Note:** Once you have created your cluster and set the StorageClass, you cannot change the StorageClass.

For production, Cassandra storage must be an SSD StorageClass. Set the value of `storageclass` if you are not using the default Kubernetes StorageClass for your cluster. You can check the default StorageClass with the following command.
    
    
    kubectl get storageclass

Your output should look something like: 
    
    
    NAME                     PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
    premium-rwo              pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   6d23h
    standard                 kubernetes.io/gce-pd    Delete          Immediate              true                   6d23h
    standard-rwo **(default)**   pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   6d23h
    

Follow the instructions in [StorageClass configuration](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-config) if you want to change the default Kubernetes StorageClass. 

To check the current `storageclass` setting, execute the following command on your cluster: 
    
    
    kubectl get pvc -n NAMESPACE cassandra-data-apigee-cassandra-default-0 -o=jsonpath='{.metadata.annotations.volume\.beta\.kubernetes\.io/storage-class}'
      

### `capacity`

For production installations, Google recommends a storage capacity of at least 500Gi (gibibytes). You can change the storage capacity in response to your cluster's storage needs. See the instructions in [Expand Cassandra persistent volumes](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/expand-persistent-volumes) to change the storage capacity. 

The default for `cassandra.storage.capacity` is `10Gi`, which is insufficient for production installations. See [`cassandra.storage.capacity`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#cassandra-storage-capacity) in the Configuration property reference.

To check the current capacity setting, execute the following command on your cluster: 
    
    
    kubectl get pvc -n NAMESPACE cassandra-data-apigee-cassandra-default-0 -o=jsonpath='{.spec.resources.requests.storage}'
      

### `cpu` and `memory`

For production installations, Google recommends at least 7 CPUs and a minimum 15Gi (gibibytes) per pod. When specifying `cassandra.resources.requests.cpu` and `cassandra.resources.requests.memory`, consider the traffic volume and the CPU and Memory demands of your proxies. 

To check the current cpu setting, execute the following command on your cluster: 
    
    
    kubectl get pods -n NAMESPACE apigee-cassandra-default-0 -o=jsonpath='{.spec.containers[].resources.requests.cpu}'
      

To check the current memory setting, execute the following command on your cluster: 
    
    
    kubectl get pods -n NAMESPACE apigee-cassandra-default-0 -o=jsonpath='{.spec.containers[].resources.requests.memory}'
      

### `maxHeapSize` and `heapNewSize`

These properties determine the maximum memory heap allocated to cassandra processes and the amount by which memory is increased, respectively, in megabytes (heap sizes are specified in megabytes, not mebibytes). For production environments, Google recommends the following values: 

  * `maxHeapSize: 8192M`
  * `heapNewSize: 1200M`



Consult your Kubernetes platform provider's documentation for optimal heap size values. 

To check the current `maxHeapSize` setting, execute the following command on your cluster: 
    
    
    kubectl get sts -n NAMESPACE apigee-cassandra-default -o=jsonpath='{.spec.template.spec.containers[].env[?(@.name=="MAX_HEAP_SIZE")]}'
      

To check the current `heapNewSize` setting, execute the following command on your cluster: 
    
    
    kubectl get sts -n NAMESPACE apigee-cassandra-default -o=jsonpath='{.spec.template.spec.containers[].env[?(@.name=="HEAP_NEWSIZE")]}'
      

For more information on these property settings, see the [ Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref). 

##  Use SSD storage for production deployments 

For the Cassandra database, the hybrid runtime only supports using [ dynamically created](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic) persistent volumes to store data. Local solid state disk (SSD) drives are not supported.

If you do not currently have SSD configured for Cassandra, you must configure a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes) definition that is backed by a solid-state drive (SSD) and make it the default class. See [StorageClass configuration](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-config) for detailed steps.

Follow the instructions in [StorageClass configuration](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-config) if you want to change the default Kubernetes StorageClass. 

**Note** : The Cassandra database for hybrid should not use persistent volumes provisioned on network-attached storage (NAS) systems.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
