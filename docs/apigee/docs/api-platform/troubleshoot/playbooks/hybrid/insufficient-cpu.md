---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/insufficient-cpu/
title: Insufficient CPU \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:17.354441+00:00
---

# Insufficient CPU  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/insufficient-cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Insufficient CPU Stay organized with collections  Save and categorize content based on your preferences. 

## Symptom

When starting up, the telemetry pods go in and out of `CrashLoopBackoff` state. This can cause periodic gaps in your metrics or graphs as the pods restart. You could also see discrepancies with analytics data as some sections of data are missing. 

## Error messages

When you use `kubectl` to view the pod states, you will see one or more metric pods in the `CrashLoopBackoff` state. Refer to the following command:
    
    
    kubectl get pods -n APIGEE_NAMESPACE

Where APIGEE_NAMESPACE is the Kubernetes namespace for your Apigee hybrid components. For more information, see [Create the apigee namespace](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-create-namespace).

Sample Output
    
    
    NAME                                                      READY   STATUS             RESTARTS   AGE
    apigee-metrics-default-telemetry-proxy-1104-hvwoo-zlmlw   0/1     CrashLoopBackoff   10         10m
    apigee-metrics-adapter-apigee-telemetry-1104-7fyff-tts65  0/1     CrashLoopBackoff   10         10m
    apigee-metrics-default-telemetry-proxy-1104-hvwoo-zlmlw   0/1     FailedScheduling   0          12m

## Common diagnosis steps

  1. Check the events for issues with telemetry pods with the following command: 
         
         kubectl -n apigee get event 

Sample Output
         
         LAST SEEN   TYPE      REASON           OBJECT                                                           MESSAGE
         53m         Normal    SuccessfulCreate job/apigee-cassandra-schema-val-jghunt-20250709-0820206-29251940 Created pod: apigee-cassandra-schema-val-jghunt-20250709-0820206-292519fkt7j
         53m         Normal    Completed        job/apigee-cassandra-schema-val-jghunt-20250709-0820206-29251940 Job completed
         43m         Normal    SuccessfulCreate job/apigee-cassandra-schema-val-jghunt-20250709-0820206-29251950 Created pod: apigee-cassandra-schema-val-jghunt-20250709-0820206-292519l87m8
         43m         Normal    Completed        job/apigee-cassandra-schema-val-jghunt-20250709-0820206-29251950 Job completed
         33m         Normal    SuccessfulCreate job/apigee-cassandra-schema-val-jghunt-20250709-0820206-29251960 Created pod: apigee-cassandra-schema-val-jghunt-20250709-0820206-29251962ncc
             

  2. You can also check the events of telemetry pods with a `CrashLoopBackOff` state using the following command: 
         
         kubectl -n apigee describe POD_NAME

Where POD_NAME is the name of the pod that is in a `CrashLoopBackOff` state.

Sample Output
         
         apigee-metrics-apigee-telemetry-app-1101-qc36n-dxzrv    

  3. You can also check the `cpu` status of the pods with the following command: 
         
         kubectl -n apigee get hpa | grep unknown

Sample Output
         
         apigee-metrics-apigee-telemetry-app-1101-qc36n-dxzrv   ReplicaSet/apigee-metrics-apigee-telemetry-app-1101-qc36n-dxzrv   /80%                                2         10        2          8h
          




## Possible causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
`metrics.app.resources.requests.cpu` and `metrics.app.resources.limits.cpu` are missing | The `cpu` must be specified in the `overrides.yaml` file. | Apigee hybrid  
  
### Cause

`cpu` is not mentioned in the `overrides.yaml` file, so `cpu` gets an undefined value. 

### Diagnosis

Check your `overrides.yaml` file to see if both `cpu` values are defined for `metrics.app.resources.requests.cpu` and `metrics.app.resources.limits.cpu`. 

### Resolution

If `cpu` settings are missing in your `overrides.yaml` file for metrics, provide both `cpu` values in the `overrides.yaml` file. 

  1. Add the following configuration under the `metrics` section in your `overrides.yaml` file: 
         
         metrics:
           app: # The apigee-prometheus-app container in the "app" pod
             resources:
               requests:
                 memory: 512Mi # Default value: 512Mi
                 cpu: 500m # Default value: 500m
               limits:
                 memory: 2Gi # default: 1Gi
                 cpu: 500m # Default value: 500m
           

  2. Apply changes using the following command: 
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
         --install \
         --namespace APIGEE_NAMESPACE \
         --set env=ENV_NAME \
         -f OVERRIDES_FILE

     * Where ENV_RELEASE_NAME is a unique name used to track installation and upgrade of the `apigee-env` chart. While it's typically the same as the ENV_NAME, it must be different if your environment has the same name as your environment group. For example, if both are named `dev`, you would use `dev-env-release` and `dev-envgroup-release` to distinguish them.

     * Where APIGEE_NAMESPACE is the Kubernetes namespace for your Apigee hybrid components. For more information, see [Create the apigee namespace](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-create-namespace).

     * Where ENV_NAME is the name you used when you created the environment in the UI.

     * Where OVERRIDES_FILE is the `overrides.yaml` file that is used during upgrades or install.


For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/latest/config-prop-ref#metrics). 

## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The `overrides.yaml` file.
  2. The output from the [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather) script.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
