---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-metrics-pods-in-crashloopbackoff/
title: Apigee Metrics pods in CrashLoopBackOff status \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:46.570136+00:00
---

# Apigee Metrics pods in CrashLoopBackOff status  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-metrics-pods-in-crashloopbackoff/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Apigee Metrics pods in CrashLoopBackOff status Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid version 1.11 and earlier only. 

## Symptom

When starting up, the Metrics pods remain in the CrashLoopBackoff state. This may cause periodic gaps in your metrics/graphs as the pods restart. This may also cause discrepancies with Analytics data as some sections of data are missing.

This issue can occur if your hybrid installation produces a large amount of metrics data. A large amount of data can be produced due to a high traffic load (resulting in a large number of underlying resources, for example MPs emitting metrics), or a large number of Apigee resources (for example, proxies, targets, envs, policies etc) being monitored.

## Error messages

When you use kubectl to view the pod states, you see that one or more Metric pods are in the CrashLoopBackoff state. For example:
    
    
    kubectl get pods -n NAMESPACE
    NAME                                              READY   STATUS            RESTARTS   AGE
    
    apigee-metrics-default-telemetry-proxy-1a2b3c4    0/1     CrashLoopBackoff  10         10m
    apigee-metrics-adapter-apigee-telemetry-a2b3c4d   0/1     CrashLoopBackoff  10         10m
    ...

## Possible causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
Metrics pods are out of memory | Telemetry pods are in CrashLoopBackoff because of insufficient memory | Apigee hybrid  
  
## Cause 1

Metric Pods are Out of Memory (OOM) with error reason `OOMKilled`.

### Diagnosis

Check that the issue is occurring by inspecting the pod logs:

  1. List the pods to get the ID of the Metrics pod that is failing: 
         
         kubectl get pods -n APIGEE_NAMESPACE -l "app in (app, proxy, collector)"

  2. Check the failing pod's log: 
         
         kubectl -n APIGEE_NAMESPACE describe pods POD_NAME




For Example:
    
    
    kubectl describe -n apigee pods apigee-metrics-default-telemetry-proxy-1a2b3c4
    

Investigate the apigee-prometheus-agg section of the output. Output like the following indicates that the container is repeatedly hitting an OOM condition: 
    
    
    Containers:
      apigee-prometheus-agg:
        Container ID:  docker://cd893dbb06c2672c41a7d6f3f7d0de4d76742e68cef70d4250bf2d5cdfcdeae6
        Image:         us.gcr.io/apigee-saas-staging-repo/thirdparty/apigee-prom-prometheus/master:v2.9.2
        Image ID:      docker-pullable://us.gcr.io/apigee-saas-staging-repo/thirdparty/apigee-prom-prometheus/master@sha256:05350e0d1a577674442046961abf56b3e883dcd82346962f9e73f00667958f6b
        Port:          19090/TCP
        Host Port:     0/TCP
        Args:
          --config.file=/etc/prometheus/agg/prometheus.yml
          --storage.tsdb.path=/prometheus/agg/
          --storage.tsdb.retention=48h
          --web.enable-admin-api
          --web.listen-address=127.0.0.1:19090
        State:          Waiting
          Reason:       CrashLoopBackOff
        Last State:     Terminated
          Reason:       OOMKilled
          Exit Code:    137
          Started:      Wed, 21 Oct 2020 16:53:42 +0000
          Finished:     Wed, 21 Oct 2020 16:54:28 +0000
        Ready:          False
        Restart Count:  1446
        Limits:
          cpu:     500m
          memory:  512Mi
        Requests:
          cpu:     100m
          memory:  256Mi
    

**NOTE** : Logs like `level=warn ts=2023-10-05T13:51:05.262Z caller=queue_manager.go:534 component=queue_manager msg="Unrecoverable error sending samples to remote storage" err="rpc error: code = InvalidArgument desc = One or more TimeSeries could not be written` are known to be produced from the `apigee-stackdriver-exporter` container and can be ignored as they have not been seen to impact metrics publishing.

### Resolution

  1. Check the current container limits with the following command 
         
         kubectl -n APIGEE_NAMESPACE describe pods POD_NAME
         

  2. Configure the metrics pod limits in your `overrides.yaml` file with the following properties: 
     * [`metrics.aggregator.resources.limits.memory`](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/config-prop-ref#metrics-aggregator-resources-limits-memory)
     * [`metrics.app.resources.limits.memory`](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/config-prop-ref#metrics-app-resources-limits-memory)
**Note** : that this requires that the telemetry controller is running in the cluster (this is the default behavior unless explicitly disabled).
    
    metrics:
      aggregator: # The apigee-prometheus-agg container in the "proxy" pod
        resources:
          limits:
            memory: 32Gi # default: 3Gi
      app: # The apigee-prometheus-app container in the "app" pod
        resources:
          limits:
            memory: 16Gi # default: 1Gi
    

**Note:** The limit can be set as high as the memory available on the underlying nodes. 
  3. Apply the changes with the `helm upgrade`: 
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

**Note** : For older versions that support the `apigeectl` command (v1.11 and below), use: 
         
         apigeectl apply --telemetry -f overrides.yaml
         

If the OOM error is still encountered after increasing the limit, you can upsize the underlying nodes to allow for more memory usage. 




## Related documents

[Manage runtime plane components](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/customize-services)

## Must gather diagnostic information

Gather the following diagnostic information, and then contact Apigee Support: 

Gather Data from Prometheus Container for Troubleshooting

Start port-forwarding for the prometheus container. Repeat for both app and proxy pods. For example:
    
    
    kubectl port-forward -n apigee apigee-metrics-apigee-telemetry-app-1a2-b3c4-d5ef 8081:9090
    

Use the script below within their cluster to collect data:
    
    
    #!/bin/bash
    
    set -e
    
    # check if jq is installed
    jq --version &> /dev/null
    if [ $? -ne 0 ]; then
      echo "jq not installed"
      exit 1
    fi
    
    # check if curl is installed
    curl --version &> /dev/null
    if [ $? -ne 0 ] ; then
      echo "curl not installed"
      exit 1
    fi
    
    # Simple check for missing arguments
    if [[ $# -eq 0 ]] ; then
      echo 'No arguments provided'
      exit 1
    fi
    
    # Simple check for missing arguments
    if [[ $# -ne 3 ]]; then
      echo 'Illegal number of arguments'
      exit 1
    fi
    
    FORWARDED_PORT=${1}
    DEST_DIR=${2}
    CASE_NUMBER=${3}
    DIR_FULL_PATH=${DEST_DIR}/${CASE_NUMBER}_$(date +%Y_%m_%d_%H_%M_%S)
    CURRENT_DATE=$(date +%Y-%m-%d)
    
    # we set the default start date for query at 10 days before current date
    START_DATE=$(date +%Y-%m-%d -d "10 days ago")
    
    mkdir -pv ${DIR_FULL_PATH}
    
    set -x
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/status' | tee ${DIR_FULL_PATH}/prometheus_status_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).txt
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/config' | tee ${DIR_FULL_PATH}/prometheus_config_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).txt
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/api/v1/targets' | tee ${DIR_FULL_PATH}/prometheus_targets_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).json
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/api/v1/status/config' | jq . | tee ${DIR_FULL_PATH}/prometheus_status_config_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).json
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/debug/pprof/heap' --output ${DIR_FULL_PATH}/prometheus_heap_$(date +%Y.%m.%d_%H.%M.%S).hprof
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/debug/pprof/heap?debug=1' | tee ${DIR_FULL_PATH}/prometheus_heap_$(date +%Y.%m.%d_%H.%M.%S).txt
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/debug/pprof/goroutine' --output ${DIR_FULL_PATH}/prometheus_goroutine_$(date +%Y.%m.%d_%H.%M.%S)
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/debug/pprof/goroutine?debug=1' | tee ${DIR_FULL_PATH}/prometheus_goroutine_$(date +%Y.%m.%d_%H.%M.%S).txt
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/debug/pprof/profile?seconds=10' --output ${DIR_FULL_PATH}/prometheus_profile_10_seconds_$(date +%Y.%m.%d_%H.%M.%S)
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/api/v1/query?query=topk(30%2C%20count%20by%20(__name__)(%7B__name__%3D~%22.%2B%22%7D))&timeout=5s&start='${START_DATE}'T00:00:00.000Z&end='${CURRENT_DATE}'T23:59:59.00Z&step=15s' | jq . | tee ${DIR_FULL_PATH}/prometheus_topk_count_by_name_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).json
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/api/v1/query?query=topk(30%2C%20count%20by%20(__name__%2C%20job)(%7B__name__%3D~%22.%2B%22%7D))&timeout=5s&start='${START_DATE}'T00:00:00.000Z&end='${CURRENT_DATE}'T23:59:59.00Z&step=15s' | jq . | tee ${DIR_FULL_PATH}/prometheus_topk_group_by_job_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).json
    curl -s '127.0.0.1:'${FORWARDED_PORT}'/api/v1/query?query=topk(30%2C%20count%20by%20(job)(%7B__name__%3D~%22.%2B%22%7D))&timeout=5s&start='${START_DATE}'T00:00:00.000Z&end='${CURRENT_DATE}'T23:59:59.00Z&step=15s' | jq . | tee ${DIR_FULL_PATH}/prometheus_topk_job_most_timeseries_$(hostname)-$(date +%Y.%m.%d_%H.%M.%S).json
    set +x
    
    ls -latrh ${DIR_FULL_PATH}
    
    tar -cvzf ${DIR_FULL_PATH}.tar.gz ${DIR_FULL_PATH}/
    
    exit 0
    

**Arguments:**

The script takes three positional arguments.

  1. Port number: Set to the port on which you forwarded from (e.g. 8081).
  2. Directory: Base directory for output files.
  3. Case number: Case number, used for the generated file name.



Example Usage
    
    
    ./prometheus_gather.sh 8081 . 1510679
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
