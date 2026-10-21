---
url: https://docs.cloud.google.com/dataflow/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:19.562886+00:00
---

# Security bulletins  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dataflow/docs/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Dataflow.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/feeds/dataflow-security-bulletins.xml`



## GCP-2024-040

**Published** : 2024-07-03

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. Dataflow jobs might create VMs that use an OS image with versions of OpenSSH that are vulnerable to CVE-2024-6387. The vulnerability could enable attackers to gain root access to Dataflow worker VMs. **Dataflow worker VMs with public IP addresses and SSH exposed to the internet should be treated with the highest priority for mitigation.**

#### What should I do?

A patched Dataflow VM image that includes an updated OpenSSH is available. We recommend working through the following steps to check your pipelines' exposure, and then applying the mitigations described, as necessary.

#### Disallow SSH to Dataflow worker VMs

_This action is the most effective mitigation against current and future vulnerabilities in SSH._ [SSH access](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#ssh_access_to_worker_vms) to Dataflow worker VMs is not required for Dataflow to function or for debugging most Dataflow issues.  Use the following Google Cloud CLI command to disable SSH for Dataflow VMs:
    
    
    gcloud compute firewall-rules create block-ssh-dataflow \
       --network=NETWORK \
       --action=DENY --priority=500 \
       --rules=tcp:22 \
       --target-tags=dataflow

To revert this action, use the `[gcloud compute firewall-rules delete block-ssh-dataflow](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/delete)` command.

#### Update or restart long-running streaming pipelines

_This action addresses the specific vulnerability mentioned in this bulletin._ Any Dataflow jobs that were started after 2024-07-04 22:00 PDT use the patched VM image. For streaming pipelines launched before this date, to use the patched VM image, you must either manually [update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline) the job or restart the job. 

#### Identify which Dataflow jobs have worker VMs with public IP addresses

_Unless access is blocked by firewalls, the SSH ports of Dataflow worker VMs with public IP addresses are open to the internet._ To get a list of Dataflow jobs that started VMs with external IP addresses, use the following gcloud CLI command:
    
    
    gcloud --project PROJECT_ID compute instances list \
       --filter "EXTERNAL_IP!='' AND STATUS='RUNNING' \
                  AND description ~ 'Created for Dataflow job'" \
       --format="list (description)" | sort -u

To inspect the list of all VMs with external IP addresses in your project, use the following gcloud CLI command:
    
    
    gcloud --project PROJECT_ID compute instances list \
       --filter "EXTERNAL_IP!='' AND STATUS='RUNNING'"

#### Disable public IPs in your Dataflow jobs

_This step ensures that the SSH ports aren't open to the public internet. Unless access is blocked by a firewall, this configuration leaves the ports open to other users with access to this network._ Dataflow pipelines that don't access the public internet don't need to use public IP addresses. If you identify any pipelines that are using public IP addresses but don't need public internet access, turn off external IP addresses for these pipelines. For instructions, see [Turn off external IP address](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#turn_off_external_ip_address).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2024-6387 exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to Dataflow worker VMs. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. | Medium | [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
