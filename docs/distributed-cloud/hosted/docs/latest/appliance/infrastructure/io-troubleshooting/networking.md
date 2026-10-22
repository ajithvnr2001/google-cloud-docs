---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/networking/
title: Networking troubleshooting \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:32.778496+00:00
---

# Networking troubleshooting  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Networking troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

The page contains details on how to troubleshoot common networking issues.

## Network Bootstrap Troubleshooting

This section shows some of the common errors you might face when completing the network bootstrap process.

### Configuration generation error

To complete the network installation, network configuration files are installed on the bootstrapper machine. If you face a configuration generation error, check the YAML files located at `/root/cellcfg` for the failed switch configuration.

### Bootstrap stalled at phase 1 ping

If the network bootstrap process gets stalled at phase 1 ping, follow these steps to find the issue:

  1. Get the generated switch configuration location from the bootstrap log: `/tmp/network-bootstrap/ID`
  2. Find the stalled switch by looking at the switch configuration file with the IP address.
  3. Sign in to the switch and check the operation log.



### Bootstrap stalled at phase 2 ping

If the network bootstrap process gets stalled at phase 2 ping, follow these steps to find the issue:

  1. Get the generated switch configuration location from the bootstrap log: `/tmp/network-bootstrap/ID`
  2. Find the stalled switch by looking at the switch configuration file with the management IP address.
  3. Check the management switch configuration for any potential access issues in the management network.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
