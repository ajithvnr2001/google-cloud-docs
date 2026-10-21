---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-maintenance-mode/
title: Use maintenance mode on a database cluster in Kubernetes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:13.787974+00:00
---

# Use maintenance mode on a database cluster in Kubernetes  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-maintenance-mode/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Use maintenance mode on a database cluster in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-maintenance-mode)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/kubernetes-maintenance-mode)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/kubernetes-maintenance-mode)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/kubernetes-maintenance-mode)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/kubernetes-maintenance-mode)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-maintenance-mode)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/kubernetes-maintenance-mode)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/kubernetes-maintenance-mode)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/kubernetes-maintenance-mode)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-maintenance-mode)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/kubernetes-maintenance-mode)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/kubernetes-maintenance-mode)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-maintenance-mode)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/kubernetes-maintenance-mode)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/kubernetes-maintenance-mode)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/kubernetes-maintenance-mode)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/kubernetes-maintenance-mode)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-maintenance-mode)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/kubernetes-maintenance-mode)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-maintenance-mode)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/kubernetes-maintenance-mode)

This page shows you how to put the database in maintenance mode in a Kubernetes cluster. 

The information on this page applies only to AlloyDB Omni using the container orchestrator. It does not apply to AlloyDB Omni using containers.

If your database runs in a Kubernetes cluster, then you can put the database in maintenance mode by disabling [liveness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) and [startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/#startup-probe), which run on your containerized application, to ensure that the database pod is in a healthy state. Maintenance mode helps you place a pod in a running state when you need to make a maintenance update or repair the pod.

## Enable maintenance mode

  1. Verify that probes exist on a database pod:

     1. Liveness probe:
            
            kubectl get po -n NAMESPACE DATABASE_POD_NAME  -o jsonpath='{.spec.containers[?(@.name=="database")].livenessProbe}'

Replace the following:

        * `NAMESPACE`: the name of a namespace used to run your database—for example, `db`.
        * `DATABASE_POD_NAME`: the name of the database pod—for example, `al-4017-dbcluster-sample-0`.

The following shows sample output with a liveness probe:
    
    {"failureThreshold":3,"httpGet":{"path":"/healthz?","port":8090,"scheme":"HTTP"},"periodSeconds":10,"successThreshold":1,"timeoutSeconds":3}
    

     2. Startup probe:
            
            kubectl get po -n NAMESPACE DATABASE_POD_NAME -o jsonpath='{.spec.containers[?(@.name=="database")].startupProbe}'

The following shows sample output with a startup probe:
            
            {"exec":{"command":["/usr/lib/postgresql/15/bin/psql","-hlocalhost","-Ualloydbadmin","-c","SELECT 1"]},"failureThreshold":180,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1}
            

  2. Set `mode` to `maintenance` in the `spec` section of your DBCluster manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
           namespace: NAMESPACE
         spec:
           allowExternalIncomingTraffic: false
           isDeleted: false
           **mode : maintenance**
           primarySpec:
           ...
         

Replace `DB_CLUSTER_NAME` with the name of this database cluster—for example, `my-db-cluster`.

  3. Apply the manifest:
         
         kubectl apply -f DB_CLUSTER_YAML

Replace `DB_CLUSTER_YAML` with the name of this database cluster manifest file—for example, `alloydb-omni-db-cluster.yaml`.

  4. To verify that maintenance mode is enabled, run the following commands:

     * Liveness probe:
           
           kubectl get po -n NAMESPACE DATABASE_POD_NAME  -o jsonpath='{.spec.containers[?(@.name=="database")].livenessProbe}'

     * Startup probe:
           
           kubectl get po -n NAMESPACE DATABASE_POD_NAME  -o jsonpath='{.spec.containers[?(@.name=="database")].startupProbe}'

The output doesn't contain the `Liveness` and `Startup` fields in the `spec` section of your `POD_NAME` pod.




## Disable maintenance mode

To return to the standard database cluster behavior with running liveliness and startup probes, use the following command to remove `maintenance` from the `spec` section of your DBCluster manifest:
    
    
    kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -p '{"spec":{"mode":""}}' --type=merge -n DB_CLUSTER_NAMESPACE --type=merge

Sample outputs:

  * With a liveness probe:
        
        {"failureThreshold":3,"httpGet":{"path":"/healthz?","port":8090,"scheme":"HTTP"},"periodSeconds":10,"successThreshold":1,"timeoutSeconds":3}
        

  * With a startup probe:
        
        {"exec":{"command":["/usr/lib/postgresql/15/bin/psql","-hlocalhost","-Ualloydbadmin","-c","SELECT 1"]},"failureThreshold":180,  "periodSeconds":10,"successThreshold":1,"timeoutSeconds":1}
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
