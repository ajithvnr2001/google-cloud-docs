---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/flow-logs/
title: Manage flow logs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:50.654435+00:00
---

# Manage flow logs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/flow-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage flow logs Stay organized with collections  Save and categorize content based on your preferences. 

Use flow logs to save network traffic metadata, including 5-tuples, in Google Distributed Cloud (GDC) air-gapped to the observability stack in the form of queryable logs. Use these logs to:

  * Understand traffic flows for a particular service in an organization.
  * Understand and identify issues with the network health of a Kubernetes workload.
  * Verify Kubernetes network policies.



Flow log is a GDC feature based on the open source Hubble project: <https://github.com/cilium/hubble>. Configure flow logs using the [`FlowLog`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/networking-v1#flowlog) resource from the [Networking API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview).

## Before you begin

  * You must obtain authorization to manage or view flow logs from the GDC console. To manage flow logs, ask your Organization IAM Admin to grant you the Flow Log Admin (`flowlog-admin`) role. To only view existing flow logs, ask your Organization IAM Admin to grant you the Flow Log Viewer (`flowlog-viewer`) role.

For information about setting role bindings from the GDC console, see [Grant access to resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

  * Before querying and viewing flow logs on dashboards, you must obtain access to the monitoring instance. For more information, see [Query and view metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics).




## Create a flow log

Create a flow log to save network traffic metadata that is filtered by a given set of specifications.

**Note:** To reduce excess and undesired information in the saved logs, narrow down the filter conditions. This is important when the network traffic volume is large.

### Create flow log with protocol and endpoint filters

  1. Create a file called `example-flowlog.yaml` with the following contents:
         
         apiVersion: networking.gdc.goog/v1
         kind: FlowLog
         metadata:
           name: "FLOW_LOG_NAME"
           namespace: "platform"
         spec:
           filters:
             - l4Protocols:
                 - udp
               endpoint:
                 ports:
                   - 53
           lifetime:
             duration: "12h"
         

Replace `FLOW_LOG_NAME` with the chosen name for the flow log.

In this example, the flow log captures all UDP traffic on port 53 (such as DNS traffic). It stops recording logs 12 hours from when the object is created.

  2. Create the flow log object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f example-flowlog.yaml
         

Replace `MANAGEMENT_API_SERVER` with the zonal Management API server's kubeconfig path.

**Note:** The `FlowLog` object must be created in the `platform` namespace.
  3. Verify that the `FLOW_LOG_NAME` value was correctly reconciled, and that the logging process has started by examining the `Status` field:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER describe -n platform FLOW_LOG_NAME
         

Example status:
         
         Status:
           Clusters:
             Cluster:  org-1-infra-cluster
             Conditions:
               Last Transition Time:  2024-01-19T01:46:11Z
               Message:
               Observed Generation:   1
               Reason:                ResourcesPropagated
               Status:                True
               Type:                  Propagated
             Name:                    cilium-flowlog-config
             Namespace:               kube-system
             Node:                    org-1-infra
             Cluster:                 user-vm-1-cluster
             Conditions:
               Last Transition Time:  2024-01-19T01:46:11Z
               Message:
               Observed Generation:   1
               Reason:                ResourcesPropagated
               Status:                True
               Type:                  Propagated
             Name:                    cilium-flowlog-config
             Namespace:               kube-system
             Node:                    user-vm-1
             Cluster:                 user-vm-2-cluster
             Conditions:
               Last Transition Time:  2024-01-19T01:46:11Z
               Message:
               Observed Generation:   1
               Reason:                ResourcesPropagated
               Status:                True
               Type:                  Propagated
             Name:                    cilium-flowlog-config
             Namespace:               kube-system
             Node:                    user-vm-2
           Conditions:
             Last Transition Time:  2024-01-18T19:17:53Z
             Message:
             Observed Generation:   1
             Reason:                Active
             Status:                True
             Type:                  Logging
             Last Transition Time:  2024-01-19T01:46:11Z
             Message:
             Observed Generation:   1
             Reason:                ResourcesPropagated
             Status:                True
             Type:                  Propagated
             Last Transition Time:  2024-01-18T19:17:53Z
             Message:
             Observed Generation:   1
             Reason:                Succeeded
             Status:                True
             Type:                  Reconciled
           Start Time:              2024-01-18T19:17:53Z
           End Time:              2024-01-18T20:17:53Z
         

This example output contains the following conditions:

     * `Propagated`: the flow log configuration was sent to clusters `user-vm-1`, `user-vm-2`, and `org-1-infra`.
     * `Reconciled`: the flow log was successfully programmed on clusters `user-vm-1`, `user-vm-2`, and `org-1-infra`.
     * `Logging`: the flow log is not expired or disabled, has not encountered any error, and may produce logs if the filters match the flows.
     * The `Start Time` and `End Time` indicate the job was started at `19:17:53`, and expires at `20:17:53`.

For this flow log to be able to successfully produce log entries, all `Propagated`, `Reconciled` and `Logging` conditions must be true.




## Modify flow log

To modify an existing flow log, modify the created flow log object definition in the `example-flowlog.yaml` file and apply it again:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f example-flowlog.yaml
    

## View flow logs in monitor dashboard

  1. Open the operational log dashboard. For more information, see [Query operational logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-logs#query-operational-logs).

  2. Set the **identifier** drop-down value to `network-flow-logs`, then click **add json parser** , and supply the following value to the query: `{identifier="network-flow-logs"} | json`:

![Set identifier](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/flowlog-dashboard-set-identifier.png)

  3. Click **Run query**. This shows the saved flow log entries:

![Run query](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/flowlog-dashboard-run-query.png)

  4. Use the filters to further refine the results. For example, provide the **cluster** drop-down with a value of `user-vm-1` to only look at flows collected from the `user-vm-1` cluster:

![Refine filters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/flowlog-dashboard-more-filters.png)

  5. Browse flow log entries, expand the entry to look at the details, and add more label filters as needed using the shortcut icon. In this example, we want to further filter flows by its source IP address:

![Flow Log entry](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/flowlog-dashboard-flowlog-entry.png)

  6. Click the `+` shortcut icon to filter flows by a specific metadata field.

![Label filter shortcut](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/flowlog-dashboard-label-filter-shortcut.png)




### View results by flow log name

When multiple flow logs are created, an additional label filter can be created to view results from one or more flow logs.

To view results limited to logs produced by `FLOW_LOG_NAME`, create a label filter with the following values:

  * `Label` set to `On`. This is case sensitive.
  * `Operator` set to `~=`. This uses a regular expression matcher.
  * `Value` set to `/FLOW_LOG_NAME/`. The `FLOW_LOG_NAME` value must be surrounded by `/`.



Filter results to only see logs produced by `flowlog1`:

![Label filter by flow name](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/flowlog-dashboard-label-filter-flow-name.png)

**Note:** To see results from multiple flow logs, join the flow log names using `|`. For example, "`/flowlog1/|/flowlog2/`" includes log entries from both `flowlog1` and `flowlog2`.

## References

  * Documentation on Hubble Dynamic Exporter: <https://docs.cilium.io/en/latest/observability/hubble-exporter/#dynamic-exporter-configuration>



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
