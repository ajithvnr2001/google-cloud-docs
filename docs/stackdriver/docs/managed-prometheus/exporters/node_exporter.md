---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/node_exporter/
title: Node Exporter \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:33.614294+00:00
---

# Node Exporter  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/node_exporter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Node Exporter Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Node Exporter. This document shows you how to do the following: 

  * Set up Node Exporter to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/prometheus/node_exporter) for Node Exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

## Prerequisites

To collect metrics from Node Exporter by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the integration, you must use `node_exporter` version 1.3.1 or later. 

For more information about available dashboards, see Install dashboards. 


These metrics are already enabled for nodes in GKE Autopilot clusters. 

## Install Node Exporter

You can use the following configuration to install Node Exporter:
    
    
    # Copyright 2022 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      namespace: gmp-public
      name: node-exporter
      labels:
        app.kubernetes.io/name: node-exporter
        app.kubernetes.io/version: 1.8.2
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: node-exporter
      updateStrategy:
        type: RollingUpdate
        rollingUpdate:
          maxUnavailable: 10%
      template:
        metadata:
          labels:
            app.kubernetes.io/name: node-exporter
            app.kubernetes.io/version: 1.8.2
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: kubernetes.io/arch
                    operator: In
                    values:
                    - arm64
                    - amd64
                  - key: kubernetes.io/os
                    operator: In
                    values:
                    - linux
          containers:
          - name: node-exporter
            image: quay.io/prometheus/node-exporter:v1.8.2
            args:
            - --web.listen-address=:8080
            - --path.sysfs=/host/sys
            - --path.rootfs=/host/root
            - --no-collector.wifi
            - --no-collector.hwmon
            - --collector.filesystem.ignored-mount-points=^/(dev|proc|sys|var/lib/docker/.+|var/lib/kubelet/pods/.+)($|/)
            - --collector.netclass.ignored-devices=^(veth.*)$
            - --collector.netdev.device-exclude=^(veth.*)$
            ports:
            - name: metrics
              containerPort: 8080
            resources:
              limits:
                memory: 180Mi
              requests:
                cpu: 102m
                memory: 180Mi
            volumeMounts:
            - mountPath: /host/sys
              mountPropagation: HostToContainer
              name: sys
              readOnly: true
            - mountPath: /host/root
              mountPropagation: HostToContainer
              name: root
              readOnly: true
          hostNetwork: true
          hostPID: true
          securityContext:
            runAsNonRoot: true
            runAsUser: 65534
          volumes:
          - hostPath:
              path: /sys
            name: sys
          - hostPath:
              path: /
            name: root
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      namespace: gmp-public
      name: node-exporter
      labels:
        app.kubernetes.io/name: node-exporter
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: node-exporter
      endpoints:
      - port: metrics
        interval: 30s
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your metrics:
    
    
    # Copyright 2022 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: monitoring.googleapis.com/v1
    kind: Rules
    metadata:
      namespace: gmp-public
      name: node-exporter-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: node-exporter-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: node-exporter
        interval: 30s
        rules:
        - alert: NodeFilesystemSpaceFillingUp
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available space left and is filling
              up.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemspacefillingup
            summary: Filesystem is predicted to run out of space within the next 24 hours.
          expr: |
            (
              node_filesystem_avail_bytes{job="node-exporter",fstype!=""} / node_filesystem_size_bytes{job="node-exporter",fstype!=""} * 100 < 15
            and
              predict_linear(node_filesystem_avail_bytes{job="node-exporter",fstype!=""}[6h], 24 * 60 * 60) < 0
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 1h
          labels:
            severity: warning
        - alert: NodeFilesystemSpaceFillingUp
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available space left and is filling
              up fast.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemspacefillingup
            summary: Filesystem is predicted to run out of space within the next 4 hours.
          expr: |
            (
              node_filesystem_avail_bytes{job="node-exporter",fstype!=""} / node_filesystem_size_bytes{job="node-exporter",fstype!=""} * 100 < 10
            and
              predict_linear(node_filesystem_avail_bytes{job="node-exporter",fstype!=""}[6h], 4*60*60) < 0
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 1h
          labels:
            severity: critical
        - alert: NodeFilesystemAlmostOutOfSpace
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available space left.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemalmostoutofspace
            summary: Filesystem has less than 5% space left.
          expr: |
            (
              node_filesystem_avail_bytes{job="node-exporter",fstype!=""} / node_filesystem_size_bytes{job="node-exporter",fstype!=""} * 100 < 5
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 30m
          labels:
            severity: warning
        - alert: NodeFilesystemAlmostOutOfSpace
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available space left.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemalmostoutofspace
            summary: Filesystem has less than 3% space left.
          expr: |
            (
              node_filesystem_avail_bytes{job="node-exporter",fstype!=""} / node_filesystem_size_bytes{job="node-exporter",fstype!=""} * 100 < 3
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 30m
          labels:
            severity: critical
        - alert: NodeFilesystemFilesFillingUp
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available inodes left and is filling
              up.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemfilesfillingup
            summary: Filesystem is predicted to run out of inodes within the next 24 hours.
          expr: |
            (
              node_filesystem_files_free{job="node-exporter",fstype!=""} / node_filesystem_files{job="node-exporter",fstype!=""} * 100 < 40
            and
              predict_linear(node_filesystem_files_free{job="node-exporter",fstype!=""}[6h], 24*60*60) < 0
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 1h
          labels:
            severity: warning
        - alert: NodeFilesystemFilesFillingUp
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available inodes left and is filling
              up fast.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemfilesfillingup
            summary: Filesystem is predicted to run out of inodes within the next 4 hours.
          expr: |
            (
              node_filesystem_files_free{job="node-exporter",fstype!=""} / node_filesystem_files{job="node-exporter",fstype!=""} * 100 < 20
            and
              predict_linear(node_filesystem_files_free{job="node-exporter",fstype!=""}[6h], 4*60*60) < 0
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 1h
          labels:
            severity: critical
        - alert: NodeFilesystemAlmostOutOfFiles
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available inodes left.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemalmostoutoffiles
            summary: Filesystem has less than 5% inodes left.
          expr: |
            (
              node_filesystem_files_free{job="node-exporter",fstype!=""} / node_filesystem_files{job="node-exporter",fstype!=""} * 100 < 5
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 1h
          labels:
            severity: warning
        - alert: NodeFilesystemAlmostOutOfFiles
          annotations:
            description: Filesystem on {{ $labels.device }} at {{ $labels.instance }}
              has only {{ printf "%.2f" $value }}% available inodes left.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefilesystemalmostoutoffiles
            summary: Filesystem has less than 3% inodes left.
          expr: |
            (
              node_filesystem_files_free{job="node-exporter",fstype!=""} / node_filesystem_files{job="node-exporter",fstype!=""} * 100 < 3
            and
              node_filesystem_readonly{job="node-exporter",fstype!=""} == 0
            )
          for: 1h
          labels:
            severity: critical
        - alert: NodeNetworkReceiveErrs
          annotations:
            description: '{{ $labels.instance }} interface {{ $labels.device }} has encountered
              {{ printf "%.0f" $value }} receive errors in the last two minutes.'
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodenetworkreceiveerrs
            summary: Network interface is reporting many receive errors.
          expr: |
            rate(node_network_receive_errs_total[2m]) / rate(node_network_receive_packets_total[2m]) > 0.01
          for: 1h
          labels:
            severity: warning
        - alert: NodeNetworkTransmitErrs
          annotations:
            description: '{{ $labels.instance }} interface {{ $labels.device }} has encountered
              {{ printf "%.0f" $value }} transmit errors in the last two minutes.'
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodenetworktransmiterrs
            summary: Network interface is reporting many transmit errors.
          expr: |
            rate(node_network_transmit_errs_total[2m]) / rate(node_network_transmit_packets_total[2m]) > 0.01
          for: 1h
          labels:
            severity: warning
        - alert: NodeHighNumberConntrackEntriesUsed
          annotations:
            description: '{{ $value | humanizePercentage }} of conntrack entries are used.'
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodehighnumberconntrackentriesused
            summary: Number of conntrack are getting close to the limit.
          expr: |
            (node_nf_conntrack_entries / node_nf_conntrack_entries_limit) > 0.75
          labels:
            severity: warning
        - alert: NodeTextFileCollectorScrapeError
          annotations:
            description: Node Exporter text file collector failed to scrape.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodetextfilecollectorscrapeerror
            summary: Node Exporter text file collector failed to scrape.
          expr: |
            node_textfile_scrape_error{job="node-exporter"} == 1
          labels:
            severity: warning
        - alert: NodeClockSkewDetected
          annotations:
            description: Clock on {{ $labels.instance }} is out of sync by more than 300s.
              Ensure NTP is configured correctly on this host.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodeclockskewdetected
            summary: Clock skew detected.
          expr: |
            (
              node_timex_offset_seconds{job="node-exporter"} > 0.05
            and
              deriv(node_timex_offset_seconds{job="node-exporter"}[5m]) >= 0
            )
            or
            (
              node_timex_offset_seconds{job="node-exporter"} < -0.05
            and
              deriv(node_timex_offset_seconds{job="node-exporter"}[5m]) <= 0
            )
          for: 10m
          labels:
            severity: warning
        - alert: NodeClockNotSynchronising
          annotations:
            description: Clock on {{ $labels.instance }} is not synchronising. Ensure
              NTP is configured on this host.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodeclocknotsynchronising
            summary: Clock not synchronising.
          expr: |
            min_over_time(node_timex_sync_status{job="node-exporter"}[5m]) == 0
            and
            node_timex_maxerror_seconds{job="node-exporter"} >= 16
          for: 10m
          labels:
            severity: warning
        - alert: NodeRAIDDegraded
          annotations:
            description: RAID array '{{ $labels.device }}' on {{ $labels.instance }} is
              in degraded state due to one or more disks failures. Number of spare drives
              is insufficient to fix issue automatically.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/noderaiddegraded
            summary: RAID Array is degraded
          expr: |
            node_md_disks_required{job="node-exporter",device=~"(/dev/)?(mmcblk.p.+|nvme.+|rbd.+|sd.+|vd.+|xvd.+|dm-.+|dasd.+)"} - ignoring (state) (node_md_disks{state="active",job="node-exporter",device=~"(/dev/)?(mmcblk.p.+|nvme.+|rbd.+|sd.+|vd.+|xvd.+|dm-.+|dasd.+)"}) > 0
          for: 15m
          labels:
            severity: critical
        - alert: NodeRAIDDiskFailure
          annotations:
            description: At least one device in RAID array on {{ $labels.instance }} failed.
              Array '{{ $labels.device }}' needs attention and possibly a disk swap.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/noderaiddiskfailure
            summary: Failed device in RAID array
          expr: |
            node_md_disks{state="failed",job="node-exporter",device=~"(/dev/)?(mmcblk.p.+|nvme.+|rbd.+|sd.+|vd.+|xvd.+|dm-.+|dasd.+)"} > 0
          labels:
            severity: warning
        - alert: NodeFileDescriptorLimit
          annotations:
            description: File descriptors limit at {{ $labels.instance }} is currently
              at {{ printf "%.2f" $value }}%.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefiledescriptorlimit
            summary: Kernel is predicted to exhaust file descriptors limit soon.
          expr: |
            (
              node_filefd_allocated{job="node-exporter"} * 100 / node_filefd_maximum{job="node-exporter"} > 70
            )
          for: 15m
          labels:
            severity: warning
        - alert: NodeFileDescriptorLimit
          annotations:
            description: File descriptors limit at {{ $labels.instance }} is currently
              at {{ printf "%.2f" $value }}%.
            runbook_url: https://runbooks.prometheus-operator.dev/runbooks/node/nodefiledescriptorlimit
            summary: Kernel is predicted to exhaust file descriptors limit soon.
          expr: |
            (
              node_filefd_allocated{job="node-exporter"} * 100 / node_filefd_maximum{job="node-exporter"} > 90
            )
          for: 15m
          labels:
            severity: critical
      - name: node-exporter.rules
        interval: 30s
        rules:
        - expr: |
            count without (cpu, mode) (
              node_cpu_seconds_total{job="node-exporter",mode="idle"}
            )
          record: instance:node_num_cpu:sum
        - expr: |
            1 - avg without (cpu) (
              sum without (mode) (rate(node_cpu_seconds_total{job="node-exporter", mode=~"idle|iowait|steal"}[5m]))
            )
          record: instance:node_cpu_utilisation:rate5m
        - expr: |
            (
              node_load1{job="node-exporter"}
            /
              instance:node_num_cpu:sum{job="node-exporter"}
            )
          record: instance:node_load1_per_cpu:ratio
        - expr: |
            1 - (
              (
                node_memory_MemAvailable_bytes{job="node-exporter"}
                or
                (
                  node_memory_Buffers_bytes{job="node-exporter"}
                  +
                  node_memory_Cached_bytes{job="node-exporter"}
                  +
                  node_memory_MemFree_bytes{job="node-exporter"}
                  +
                  node_memory_Slab_bytes{job="node-exporter"}
                )
              )
            /
              node_memory_MemTotal_bytes{job="node-exporter"}
            )
          record: instance:node_memory_utilisation:ratio
        - expr: |
            rate(node_vmstat_pgmajfault{job="node-exporter"}[5m])
          record: instance:node_vmstat_pgmajfault:rate5m
        - expr: |
            rate(node_disk_io_time_seconds_total{job="node-exporter", device=~"(/dev/)?(mmcblk.p.+|nvme.+|rbd.+|sd.+|vd.+|xvd.+|dm-.+|dasd.+)"}[5m])
          record: instance_device:node_disk_io_time_seconds:rate5m
        - expr: |
            rate(node_disk_io_time_weighted_seconds_total{job="node-exporter", device=~"(/dev/)?(mmcblk.p.+|nvme.+|rbd.+|sd.+|vd.+|xvd.+|dm-.+|dasd.+)"}[5m])
          record: instance_device:node_disk_io_time_weighted_seconds:rate5m
        - expr: |
            sum without (device) (
              rate(node_network_receive_bytes_total{job="node-exporter", device!="lo"}[5m])
            )
          record: instance:node_network_receive_bytes_excluding_lo:rate5m
        - expr: |
            sum without (device) (
              rate(node_network_transmit_bytes_total{job="node-exporter", device!="lo"}[5m])
            )
          record: instance:node_network_transmit_bytes_excluding_lo:rate5m
        - expr: |
            sum without (device) (
              rate(node_network_receive_drop_total{job="node-exporter", device!="lo"}[5m])
            )
          record: instance:node_network_receive_drop_excluding_lo:rate5m
        - expr: |
            sum without (device) (
              rate(node_network_transmit_drop_total{job="node-exporter", device!="lo"}[5m])
            )
          record: instance:node_network_transmit_drop_excluding_lo:rate5m
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

This `Rules` configuration was adapted from the rules and alerts contributed to the [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) repository. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured Node Exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="node-exporter", cluster="CLUSTER_NAME", namespace="gmp-public"}
         




## Install dashboards

Cloud Monitoring provides a library of sample dashboards for integrations. The sample library includes "Prometheus" dashboards, which you can install to view your data in the Google Cloud console.

Note that the **Kubernetes Cluster Prometheus Overview** dashboard requires [Kube State Metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics) to be installed. The **Kubernetes Pod Prometheus Overview** dashboard requires [Kube State Metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics) and [Kubelet/cAdvisor](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor) to be installed.

To install a dashboard from the sample library, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Sample Library** tab.
  3. Choose the **Other** category.
  4. (Optional) To view a static preview of a dashboard without installing it, click **Preview**.
  5. Select the dashboards you want to install, then click download **Import**.



For more information about installing dashboards, see [ Installing sample dashboards](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates#install-templates).

## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
