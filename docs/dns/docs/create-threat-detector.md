---
url: https://docs.cloud.google.com/dns/docs/create-threat-detector/
title: Create a DNS threat detector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:19.862789+00:00
---

# Create a DNS threat detector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/create-threat-detector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create a DNS threat detector Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and modify a DNS threat detector to monitor VPC networks for malicious, internet-bound DNS activity.

For more information about DNS threat detection, see [DNS Armor overview](https://docs.cloud.google.com/dns/docs/threat-detection).

DNS threat monitoring can impact your billing. See [Cloud DNS Pricing](https://cloud.google.com/dns/pricing) for more information.

## Before you begin

Complete the following before you create a DNS threat detector.

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest) in your project.
  * Make sure that you have the required roles to enable a DNS threat detector.
  * If you want to use Google Cloud CLI to perform tasks, [update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) Google Cloud CLI to the latest version.



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networksecurity.dnsThreatDetectors.create`
  * `networksecurity.dnsThreatDetectors.delete`
  * `networksecurity.dnsThreatDetectors.get`
  * `networksecurity.dnsThreatDetectors.list`
  * `networksecurity.dnsThreatDetectors.update`



**Roles**

  * `roles/networksecurity.dnsThreatDetectorAdmin`



## Create DNS threat detector

To create a DNS threat detector for all of your VPC networks in a project, complete the following steps. Any new VPC networks added to the project are monitored automatically.

You can have only one DNS threat detector enabled for a project.

### Console

  1. In the Google Cloud console, go to the **Advanced threat detection** page.

[Go to Advanced threat detection](https://console.cloud.google.com/net-security/dns-armor/threat-detectors/list)

  2. Click **Create DNS threat detector**.

  3. Enter a name for your DNS threat detector.

  4. Select **All VPC networks in the project**.

  5. Click **Create**.




### gcloud
    
    
    gcloud network-security dns-threat-detectors create NAME \
      --location=global \
      --project=PROJECT_ID \
      --provider="INFOBLOX"
    

Replace the following:

  * `NAME`: the name for your DNS threat detector.
  * `PROJECT_ID`: your project ID.



### API
    
    
    POST https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/global/dnsThreatDetectors?dnsThreatDetectorId=NAME
    
    {
        "provider"  : "INFOBLOX"
    }
    

Replace the following:

  * `NAME`: the name of your DNS threat detector.
  * `PROJECT_ID`: your project ID.



## Validate a threat detector

The following are test domains you can use to verify DNS threat domains:

  * `dnst-gcp-blox.com`
  * `ftags-gcp-blox.com`
  * `dga-gcp-blox.com`



For more information, see [DNS threat events aren't generated for some abusive or bad domains](https://docs.cloud.google.com/dns/docs/troubleshooting#dns_threats_events_arent_generated_for_some_abusive_or_bad_domains).

Optionally, for more extensive testing, you can use the [Infoblox threat detection simulator](https://github.com/infobloxopen/ib-threat-detection-simulator). The tool runs local `dig` commands for a specified list of domains to simulate malicious activity and is designed for testing and demonstration purposes only. You can then verify that the expected threat logs are generated in Cloud Logging.

For step-by-step guidance on how to simulate DNS threats and view threat logs in Logs Explorer, see the [Getting started with DNS Armor's Advanced Threat Detection tutorial](https://codelabs.developers.google.com/dns-armor-getting-started#0).

**Note:** To avoid incurring future charges, make sure to delete any resources you created when following the codelab.

## Exclude a VPC network from threat monitoring

You can exclude a VPC network from threat monitoring by editing your DNS threat detector. You can also exclude the network when creating a DNS threat detector.

New VPC networks added to the project are monitored automatically.

### Console

  1. In the Google Cloud console, go to the **Advanced threat detection** page.

[Go to Advanced threat detection](https://console.cloud.google.com/net-security/dns-armor/threat-detectors/list)

  2. Click **More more_vert**, and select **Edit**.

  3. In the **Scope** section, select **All VPC networks in the project except excluded networks**.

  4. Select the VPC networks that you don't want to monitor.

  5. Click **Save**.




### gcloud
    
    
    gcloud network-security dns-threat-detectors update NAME  \
      --add-excluded-networks=LIST_OF_NETWORKS \
      --provider="INFOBLOX" \
      --location=global
    

Replace the following:

  * `NAME`: the name of your DNS threat detector.
  * `LIST_OF_NETWORKS`: the list of VPC networks you want to exclude.
  * `PROJECT_ID`: your project ID.



### API
    
    
    PATCH https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/global/dnsThreatDetectors/NAME
    
    {
        "name"                  : "NAME",
        "excluded_networks"     : [ "LIST_OF_NETWORKs" ],
        "provider"              : "INFOBLOX"
    }
    

Replace the following:

  * `NAME`: the name of your DNS threat detector.
  * `PROJECT_ID`: your project ID.
  * `LIST_OF_NETWORKS`: a comma-delimited list of VPC networks you want to exclude. Each network must be in quotes.



## Remove your DNS threat detector

You can delete your DNS threat detector.

### Console

  1. In the Google Cloud console, go to the **Advanced threat detection** page.

[Go to Advanced threat detection](https://console.cloud.google.com/net-security/dns-armor/threat-detectors/list)

  2. Click **More more_vert**, and select **Delete**.




### gcloud
    
    
    gcloud network-security dns-threat-detectors delete NAME \
      --project=PROJECT_ID \
      --location=global
    

Replace the following:

  * `NAME`: the name of your DNS threat detector.
  * `PROJECT_ID`: your project ID.



### API
    
    
    DELETE https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/global/dnsThreatDetectors/NAME
    
    {
        "name"          : "NAME",
    }
    

Replace the following:

  * `NAME`: the name of your DNS threat detector.
  * `PROJECT_ID`: your project ID.



## Add labels

You can add labels to your DNS threat detector after it has been created.

### Console

  1. In the Google Cloud console, go to the **Advanced threat detection** page.

[Go to Advanced threat detection](https://console.cloud.google.com/net-security/dns-armor/threat-detectors/list)

  2. Click **More more_vert**, and select **Labels**.

  3. Enter or select labels for your DNS threat detector.




## What's next

  * To view any threats detected, see [View threats](https://docs.cloud.google.com/dns/docs/view-threat-logs).
  * For more information about logging, see [Use logging and monitoring](https://docs.cloud.google.com/dns/docs/monitoring).
  * To find solutions for common issues that you might encounter with your DNS threat detector, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting#threat-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
