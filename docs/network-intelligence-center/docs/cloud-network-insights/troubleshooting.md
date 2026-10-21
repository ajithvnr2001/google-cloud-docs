---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/troubleshooting/
title: Troubleshooting Cloud Network Insights \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:23.219918+00:00
---

# Troubleshooting Cloud Network Insights  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Troubleshooting Cloud Network Insights Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud Network Insights.

## Monitoring Points aren't active

If your Monitoring Point is not active in the Cloud Network Insights Monitoring Points list after ten minutes, check their status on the target hosts.

### Compute Engine Cloud Monitoring Points aren't active

For Compute Engine Cloud Monitoring Points, see [Troubleshooting Connectivity to AppNeta – Google CE Cloud Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro/gce-setup/gce-mp-troubleshooting-connectivity-to-appneta.html) in the AppNeta documentation.

### Microsoft Azure Monitoring Points aren't active

For Microsoft Azure Monitoring Points, see [Troubleshooting Connectivity to AppNeta – Azure Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/azure-vm-mp-intro/azure-vm-setup/azure-vm-mp-troubleshooting-connectivity-to-appneta.html) in the AppNeta documentation.

### Amazon Web Services EC2 Monitoring Points aren't active

For AWS EC2 Monitoring Points, see [Troubleshooting Connectivity to AppNeta – AWS EC2 Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/aws-ec2-mp-intro/aws-ec2-setup/aws-ec2-mp-troubleshooting-connectivity-to-appneta.html) in the AppNeta documentation.

### Container Monitoring Points aren't active

For containers, check the service status. See the following AppNeta resources:

  * [View Status – c50-Docker/Podman](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/docker-mp-intro/docker-access/docker-mp-view-monitoring-point-status.html)
  * [Troubleshooting Connectivity to AppNeta – c50-Docker/Podman](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/docker-mp-intro/docker-setup/docker-mp-troubleshooting-connectivity-to-appneta.html)
  * [Troubleshooting Connectivity to AppNeta – c50-Kubernetes (Helm)](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/kubernetes-mp-intro/kubernetes-setup/kubernetes-mp-troubleshooting-connectivity-to-appneta.html)



### Virtual machine Monitoring Points aren't active

For VMware and KVM, open the Web Admin interface to diagnose the issue. See the following AppNeta resources:

  * [Troubleshooting Connectivity to AppNeta – v35-KVM](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-kvm-mp-intro/v35-kvm-setup/v35-kvm-mp-troubleshooting-connectivity-to-appneta.html?content_ref=system+status+ntp+synchronized+should+be+yes)
  * [Troubleshooting Connectivity to AppNeta – v35-VMware](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-vmware-mp-intro/v35-vmware-setup/v35-vmware-mp-troubleshooting-connectivity-to-appneta.html)



### Monitoring Point does not display in Cloud Network Insights

On occasion when you successfully install a Monitoring Point in a Docker or Podman environment, the Monitoring Point doesn't connect to Cloud Network Insights and is not displayed in the Monitoring Points list after waiting for more than 20 minutes.

To resolve this issue, remove the Monitoring Point and create it again using host networking.

For more information about installing on Docker or Podman using host networking, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/docker-mp-intro/docker-setup/docker-mp-setup-cmp.html).

## Access is blocked by Google Workspace

If you encounter the `Access Blocked: admin_policy_enforced error`, contact a Google Workspace administrator to allow AppNeta access.

See [Configure Google Workspace](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-workspace) for instructions.

## Some metrics aren't the same in Google Cloud and AppNeta

When looking at a timeframe longer than one hour in AppNeta, some metrics' raw values are transformed into the `MAX` and `AVG` of this value. In Google Cloud, the metrics aren't transformed.

For example, in AppNeta you see the average of `rtt_avg` and the max of the `rtt_avg` for a specific timeframe. In Google Cloud, `rtt_max` and `rtt_avg` metrics are not transformed.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
