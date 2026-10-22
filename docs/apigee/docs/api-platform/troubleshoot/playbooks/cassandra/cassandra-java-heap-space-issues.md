---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-java-heap-space-issues/
title: Cassandra Java heap space issues \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:56.382549+00:00
---

# Cassandra Java heap space issues  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-java-heap-space-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra Java heap space issues Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

Cassandra heap issues may cause slowness in the Apigee hybrid proxy execution or even `Datastore` errors. Sometimes logs are an early indicator, even before the onset of symptoms. 

## Error Message

In Cassandra pod logs ([Cloud Logging](https://docs.cloud.google.com/logging)), log entries might be observed that are similar to the following: 
    
    
    WARN  [Service Thread] 2023-01-01 01:14:51,121 GCInspector.java:283 - G1 Young Generation GC in 2510ms...
    ...
    WARN  [Service Thread] 2023-01-01 01:14:51,121 GCInspector.java:283 - G1 Old Generation GC in 3100ms...
    
    
    2023-01-01 01:14:51,123 FailureDetector.java:278 - Not marking nodes down due to local pause of 45261214670 > 5000000000
    
    
    java.lang.OutOfMemoryError: Java heap space

## Cause: Insufficient Java heap size

### Diagnosis

In the `overrides.yaml` file for the Apigee hybrid installation, `maxHeapSize` is not set to a sufficient value. This could be due to [ production settings](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-production#configure-cassandra-storage-settings) not applied, or current throughputs requiring a setting higher than usual. 

### Resolution

To resolve the issue, adjust `maxHeapSize` and `memory` [ accordingly](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-production#configure-cassandra-storage-settings), and [ apply the changes](https://docs.cloud.google.com/apigee/docs/hybrid/latest/customize-services): 
    
    
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M

If the issue persists with the default production configuration, try to increase the values further. Note that you need to ensure that node capacity, [ disk throughput](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-production#use-ssd-storage-for-production-deployments) and [ network bandwidth](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cluster-overview#cassandra-network-requirements) are sufficient as well. 
    
    
      resources:
        requests:
          cpu: 7
          memory: 30Gi
      maxHeapSize: 16384M
      heapNewSize: 2400M

If the 16 GB heap setting is still not sufficient for the traffic volume, continue with [ horizontal scaling](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-scaling#scaling-cassandra-horizontally). 

## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

Apart from the usual data you might be asked to provide, collect the diagnostic data from all the Cassandra pods with the command below: 
    
    
    for p in $(kubectl -n apigee get pods -l app=apigee-cassandra --no-headers -o custom-columns=":metadata.name") ; do \
    for com in info describecluster failuredetector version status ring info gossipinfo compactionstats tpstats netstats cfstats proxyhistograms gcstats ; do kubectl \
    -n apigee exec ${p} -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD '"$com"' 2>&1 '\
    | tee /tmp/k_cassandra_nodetool_${com}_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt | head -n 40 ; echo '...' ; done; done

Compress it, and provide it in the Support case: 
    
    
    tar -cvzf /tmp/cassandra_data_$(date +%Y.%m.%d_%H.%M.%S).tar.gz /tmp/k_cassandra_nodetool*

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
