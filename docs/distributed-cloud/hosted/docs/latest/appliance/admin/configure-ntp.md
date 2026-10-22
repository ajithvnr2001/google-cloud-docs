---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-ntp/
title: Configure an external NTP server \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:44.252030+00:00
---

# Configure an external NTP server  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-ntp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure an external NTP server Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure an external NTP server for Google Distributed Cloud (GDC) air-gapped appliance.

These steps are only required if you want to synchronize the appliance with external time source.

## Before you begin

To sync the appliance with an external NTP server, [configure the device and install software](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup).

## Configure the NTP relay

  1. Determine the IP address that the GDC air-gapped appliance must use to access your NTP server. You might have to adjust your firewall rules to allow the traffic.

  2. Using the root kubeconfig, edit the `ntprelay` CR in the management plane cluster and add the `upstreamServers` section.
         
         kubectl edit ntprelay bi-ntp-relay -n gpc-system
         ntprelay.system.private.gdc.goog/bi-ntp-relay edited
         kubectl get ntprelay bi-ntp-relay -n gpc-system -oyaml
         

The resulting yaml has an updated `.spec` section that includes the IP, as shown in the following example:
         
         apiVersion: system.private.gdc.goog/v1alpha1
         kind: NTPRelay
         metadata:
           creationTimestamp: "2025-05-16T08:44:21Z"
           generation: 2
           name: bi-ntp-relay
           namespace: gpc-system
           resourceVersion: "10871409"
           uid: 6cde8e65-791c-4bc6-9a8b-d5c9bf103f8b
         spec:
           upstreamServers:
           - **192.0.2.030**
         

  3. Verify the time on each node:

Wait three minutes to give time to synchronize, then run the following command in the control plane cluster using the root kubeconfig:
         
         kubectl get pods -l app.kubernetes.io/name=ntp -n ntp-system -o name | xargs -P 0 -I {} kubectl exec {} -n ntp-system -- date; echo
         

The output displays the time for each node, matching the time of your NTP server. The output looks similar to the following:
         
         Defaulted container "ntp-image" out of: ntp-image, ntp-node-exporter
         Defaulted container "ntp-image" out of: ntp-image, ntp-node-exporter
         Defaulted container "ntp-image" out of: ntp-image, ntp-node-exporter
         Thu Nov  6 19:39:34 UTC 2025
         Thu Nov  6 19:39:34 UTC 2025
         Thu Nov  6 19:39:34 UTC 2025
         




## Debug connectivity issues

If the time does not match, run the following command in the control plane cluster using the root kubeconfig to debug the connectivity to the NTP server:
    
    
    kubectl get pods -l app.kubernetes.io/name=ntp -n ntp-system -o name | xargs -I {} kubectl exec {} -n ntp-system -- sh -c "chronyc sources -v; echo; chronyc ntpdata"; echo
    

The output of a healthy connection looks like the following. The IP of the external server starts with `^*`. In the data for the source (such as `Remote address : 192.0.2.026`), `TX` is the amount of packets sent, and `RX` is the number received. If `RX` is 0, this indicates a connectivity issue. Check your firewall to see if the NTP requests are making it through:
    
    
      .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
    / .- Source state '*' = current best, '+' = combined, '-' = not combined,
    | /             'x' = may be in error, '~' = too variable, '?' = unusable.
    ||                                                 .- xxxx [ yyyy ] +/- zzzz
    ||      Reachability register (octal) -.           |  xxxx = adjusted offset,
    ||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
    ||                                \     |          |  zzzz = estimated error.
    ||                                 |    |           \
    MS Name/IP address         Stratum Poll Reach LastRx Last sample
    ===============================================================================
    **^* 192.0.2.026                   1   6    17    43   +286ns[  +36us] +/- 1160us**
    =? 192.0.2.029                 0   6     0     -     +0ns[   +0ns] +/-    0ns
    =? 192.0.2.051                 0   6     0     -     +0ns[   +0ns] +/-    0ns
    =? 192.0.2.059            0   6     0     -     +0ns[   +0ns] +/-    0ns
    
    Remote address  : 192.0.2.026 (ACC03AF1)
    Remote port     : 123
    Local address   : 192.0.2.029 (0AA800D5)
    Leap status     : Normal
    Version         : 4
    Mode            : Symmetric passive
    Stratum         : 2
    Poll interval   : 10 (1024 seconds)
    Precision       : -25 (0.000000030 seconds)
    Root delay      : 0.000381 seconds
    Root dispersion : 0.000397 seconds
    Reference ID    : ACC03BDF ()
    Reference time  : Thu Nov 06 19:36:31 2025
    Offset          : -0.000002443 seconds
    Peer delay      : 0.000202604 seconds
    Peer dispersion : 0.000000053 seconds
    Response time   : 0.000097758 seconds
    Jitter asymmetry: -0.37
    NTP tests       : 111 111 1111
    Interleaved     : No
    Authenticated   : No
    TX timestamping : Daemon
    RX timestamping : Kernel
    Total TX        : 67
    Total RX        : 67
    Total valid RX  : 67
    Total good RX   : 67
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
