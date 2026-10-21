---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/toolbox/
title: Debugging node issues \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:12.557297+00:00
---

# Debugging node issues  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/toolbox/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Debugging node issues Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/toolbox)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/toolbox)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page explains how to debug node issues on Google Distributed Cloud using a suite of preinstalled debugging tools.

## Overview

Each Google Distributed Cloud cluster you create is composed of several nodes. Each node includes a distribution of [CoreOS' `toolbox`](https://github.com/coreos/toolbox), a shell script that unpacks and runs a debugging container, `debug-toolbox`. `debug-toolbox` is a container image that includes several useful debugging tools.

If you encounter issues with a specific node, you can attempt debugging by connecting to the affected node, run the `toolbox` script to unpack and run the `debug-toolbox` container, and run the tools included in the container.

### Tools included in `debug-toolbox` container

The `debug-toolbox` container runs a Debian base image that includes the following packages:

  * bash
  * curl
  * dnsutils
  * hping3
  * iperf3
  * lsof
  * netcat
  * mtr
  * procps
  * strace
  * tcpdump
  * traceroute
  * util-linux



Since these tools are included in the container, they don't require an internet connection. If you want to install additional debugging tools, you use `apt-get`, which does require an internet connection.

## Using `toolbox`

  1. [SSH into the cluster node](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ssh-cluster-node).

  2. Run the `toolbox` command:
         
         sudo toolbox

This command starts a `debug-toolbox` container.

  3. While inside the container, run one of the tools. For example, `tcpdump`.

  4. When you're finished, exit the container and close the SSH connection to the node.




## Node Problem Detector

Beginning with Google Distributed Cloud version 1.4, [Node Problem Detector](https://github.com/kubernetes/node-problem-detector), which is enabled for all the nodes in a cluster, helps in quick detection of some common node problems. Node Problem Detector keeps checking for possible problems and reports the same as events and conditions on the node. If a node misbehaves, you can check whether Node Problem Detector detected the problem by running `kubectl describe` on the node and looking for the corresponding events and conditions.

Node Problem Detector monitors generate several conditions on the node. If the reported condition is `KubeletUnhealthy` or `ContainerRuntimeUnhealthy`, a restart of the corresponding `systemd` service (kubelet or Docker) might help in making the node healthy again.

Beginning with Google Distributed Cloud version 1.5, kubelet and docker systemd service auto repair is enabled in Node Problem Detector. If Node Problem Detector detects a `KubeletUnhealthy` or `ContainerRuntimeUnhealthy` condition on the node, it tries to restart the kubelet or docker service automatically if the duration since last restart is above a certain threshold.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
