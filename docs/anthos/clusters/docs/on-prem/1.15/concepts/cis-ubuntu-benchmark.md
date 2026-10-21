---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cis-ubuntu-benchmark/
title: CIS Ubuntu Benchmark \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:33.917227+00:00
---

# CIS Ubuntu Benchmark  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cis-ubuntu-benchmark/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  CIS Ubuntu Benchmark Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/concepts/cis-ubuntu-benchmark)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/concepts/cis-ubuntu-benchmark)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document describes the level of compliance that Google Distributed Cloud has with the CIS Ubuntu Benchmark.

### Versions

This document refers to these versions:

Anthos version | Ubuntu version | CIS Ubuntu Benchmark version | CIS level   
---|---|---|---  
1.15 | 20.04 LTS | v1.0.0 | Level 2 Server  
  
## Access the benchmark

The CIS Ubuntu Benchmark is available on the [CIS website](https://www.cisecurity.org/benchmark/ubuntu_linux/).

## Configuration profile

In the CIS Ubuntu Benchmark document, you can read about configuration profiles. The Ubuntu images used by Google Distributed Cloud are hardened to meet the Level 2 - Server profile.

## Evaluation on Google Distributed Cloud

We use the following values to specify the status of Ubuntu recommendations in Google Distributed Cloud.

Status | Description  
---|---  
Pass | Complies with a benchmark recommendation.  
Fail | Does not comply with a benchmark recommendation.  
Equivalent control | Does not comply with the exact terms in a benchmark recommendation, but other mechanisms in Google Distributed Cloud provide equivalent security controls.  
Depends on environment | Google Distributed Cloud does not configure items related to a benchmark recommendation. Your configuration determines whether your environment complies with the recommendation.  
  
## Status of Google Distributed Cloud

The Ubuntu images used with Google Distributed Cloud are hardened to meet the CIS Level 2 - Server profile. The following table gives justifications for why Google Distributed Cloud components did not pass certain recommendations.

# | Recommendation | Scored/Not Scored | Status | Justification | Affected Components  
---|---|---|---|---|---  
1.1.2  | Ensure /tmp is configured  | Scored  | Fail  | Canonical has no plan to modify the cloud image partitions at this time.  | All cluster nodes, Admin workstation, Seesaw  
1.1.10  | Ensure separate partition exists for /var  | Scored  | Won't fix  | Canonical has no plan to modify the cloud image partitions at this time.  | All cluster nodes, Admin workstation, Seesaw  
1.1.11  | Ensure separate partition exists for /var/tmp  | Scored  | Won't fix  | Canonical has no plan to modify the cloud image partitions at this time.  | All cluster nodes, Admin workstation, Seesaw  
1.1.15  | Ensure separate partition exists for /var/log  | Scored  | Won't fix  | Canonical has no plan to modify the cloud image partitions at this time.  | All cluster nodes, Admin workstation, Seesaw  
1.1.16  | Ensure separate partition exists for /var/log/audit  | Scored  | Won't fix  | Canonical has no plan to modify the cloud image partitions at this time.  | All cluster nodes, Admin workstation, Seesaw  
1.1.17  | Ensure separate partition exists for /home  | Scored  | Won't fix  | Canonical has no plan to modify the cloud image partitions at this time.  | All cluster nodes, Admin workstation, Seesaw  
1.1.22  | Ensure sticky bit is set on all world-writable directories  | Scored  | Fail  | This could interfere with the functionality of Anthos and its services and is not enabled by default  | All cluster nodes, Admin workstation  
1.5.1  | Ensure permissions on bootloader config are configured  | Scored  | Fail  | Permissions have been left as default.  | All cluster nodes, Seesaw  
1.5.2  | Ensure bootloader password is set  | Scored  | Depends on Environment  | No root password is set on Ubuntu cloud images.  | All cluster nodes, Admin workstation, Seesaw  
1.5.3  | Ensure authentication required for single user mode  | Scored  | Depends on Environment  | No root password is set on Ubuntu cloud images.  | All cluster nodes, Admin workstation, Seesaw  
2.3.6 | Ensure RPC is not installed | Scored | Failed | rpcbind is installed on the Canonical cloud image, though it's not enabled by default. The rule is failing because it requires it to be not installed | All cluster nodes  
3.2.2  | Ensure IP forwarding is disabled  | Scored  | Fail  | IP forwarding is necessarily in order for Kubernetes (GKE) to correctly function and route traffic  | All cluster nodes, Admin workstation, Seesaw  
3.2.7 | Ensure Reverse Path Filtering is enabled | Scored | Depends on Environment | Asynchronous routing and reverse path origination is a requirement for delivering cluster load balancing | Seesaw  
3.5.3.2.1 | Ensure default deny firewall policy | Scored | Depends on Environment | It is recommended that Google Distributed Cloud be deployed on a private network with appropriate firewall protections. The required firewall rules can be found [here](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/firewall-rules). | All cluster nodes, Admin workstation, Seesaw  
3.5.3.2.2 | Ensure loopback traffic is configured | Scored | Depends on Environment | Loopback interface usage is limited given the load balancing functionality used. | Seesaw  
3.5.3.2.4  | Ensure firewall rules exist for all open ports  | Not Scored  | Depends on Environment  | It is recommended that Google Distributed Cloud be deployed on a private network with appropriate firewall protections. The required firewall rules can be found [here](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/firewall-rules).  | All cluster nodes, Admin workstation, Seesaw  
3.5.3.3.1  | Ensure IPv6 default deny firewall policy  | Scored  | Depends on Environment  | It is recommended that Google Distributed Cloud be deployed on a private network with appropriate firewall protections. The required firewall rules can be found [here](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/firewall-rules). Additionally, Anthos has no requirement for IPv6 under GA support.  | All cluster nodes, Admin workstation, Seesaw  
3.5.3.3.2  | Ensure IPv6 loopback traffic is configured  | Scored  | Depends on Environment  | Anthos has no requirement for IPv6 under GA support.  | Admin control plane, Seesaw  
4.1.1.3  | Ensure auditing for processes that start prior to auditd is enabled  | Scored  | Fail  | A known issue with our build process flags this as Failed, however this should be considered a false alarm. This will be remedied in the future.  | All cluster nodes, Seesaw  
4.1.11  | Ensure use of privileged commands is collected  | Scored  | Fail  | Some binaries are installed at runtime, so the runtime remediation is needed.  | All cluster nodes, Admin workstation, Seesaw  
4.2.1.5  | Ensure rsyslog is configured to send logs to a remote log host  | Scored  | Depends on Environment  | Google Distributed Cloud currently collects all journald logs (from system services). These can view these logs under "k8s_node"  | All cluster nodes, Admin workstation, Seesaw  
4.2.3  | Ensure permissions on all logfiles are configured  | Scored  | Fail  | This specific test is overly restrictive and unrealistic as many services may require a group to write log files. This item may be removed in a future benchmark.  | All cluster nodes, Admin workstation, Seesaw  
4.4 | Ensure logrotate assigns appropriate permissions | Scored | Failed | Complying this rule could affect the current logging functionality | All cluster nodes, Seesaw  
5.2.18  | Ensure SSH access is limited  | Scored  | Depends on Environment  | This is not configured by default. This can be configured to meet your specific requirements.  | All cluster nodes, Admin workstation, Seesaw  
5.2.20 | Ensure SSH AllowTcpForwarding is disabled | Scored | Failed | Complying this rule could affect the current ssh tunnel functionality | All cluster nodes  
5.4.1.1 | Ensure password expiration is 365 days or less | Scored | Equivalent control | VMs for Google Distributed Cloud rely on ssh key for user login, instead of using password | All cluster nodes  
6.1.10 | Ensure no world writable files exist | Scored | Fail | Permissions have been left as default. | All cluster nodes  
6.1.11 | Ensure no unowned files or directories exist | Scored | Fail | Permissions have been left as default. | All cluster nodes  
6.1.12 | Ensure no ungrouped files or directories exist | Scored | Fail | Permissions have been left as default. | All cluster nodes  
6.2.7 | Ensure users' dot files are not group or world writable | Scored | Fail | The default settings for Ubuntu permit dot file group permissions due to compatibility | Admin workstation  
  
## Configure AIDE cron job

AIDE is a file integrity checking tool that ensures compliance with CIS L1 Server benchmark 1.4 `Filesystem Integrity Checking`. In Google Distributed Cloud, the AIDE process has been causing high resource usage issues.

From 1.12, the AIDE process on nodes is disabled by default to prevent resource issues. This will affect compliance with CIS L1 Server benchmark 1.4.2: `Ensure filesystem integrity is regularly checked.`

If you want to opt in to run the AIDE cron job, complete the following steps to re-enable AIDE:

  1. Create a DaemonSet.

Here's a manifest for a DaemonSet:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
         name: enable-aide-pool1
         spec:
         selector:
           matchLabels:
             app: enable-aide-pool1
         template:
           metadata:
             labels:
               app: enable-aide-pool1
           spec:
             hostIPC: true
             hostPID: true
             nodeSelector:
               cloud.google.com/gke-nodepool: pool-1
             containers:
             - name: update-audit-rule
               image: ubuntu
               command: ["chroot", "/host", "bash", "-c"]
               args:
               - |
                 set -x
                 while true; do
                   # change daily cronjob schedule
                   minute=30;hour=5
                   sed -E "s/([0-9]+ [0-9]+)(.*run-parts --report \/etc\/cron.daily.*)/$minute $hour\2/g" -i /etc/crontab
         
                   # enable aide
                   chmod 755 /etc/cron.daily/aide
         
                   sleep 3600
                 done
               volumeMounts:
               - name: host
                 mountPath: /host
               securityContext:
                 privileged: true
             volumes:
             - name: host
               hostPath:
                 path: /
         

In the above manifest:

     * The AIDE cron job will only run on node pool `pool-1` as specified by the nodeSelector `cloud.google.com/gke-nodepool: pool-1`. You can configure the AIDE process to run on as many node pools as you wish by specifying the pools under the `nodeSelector` field. To run the same cron job schedule across different node pools, remove the `nodeSelector` field. However, to avoid host resource congestions, we recommend you maintain separate schedules.

     * The cron job is scheduled to run daily at 5:30am as specified by the configuration `minute=30;hour=5`. You can configure different schedules for the AIDE cron job as required.

  2. Copy the manifest to a file named `enable-aide.yaml`, and create the DaemonSet:



    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f enable-aide.yaml
    

where USER_CLUSTER_KUBECONFIG is the path of the [kubeconfig file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
