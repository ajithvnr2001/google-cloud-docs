---
url: https://docs.cloud.google.com/looker/docs/upgrading-to-openjdk-21-customer-hosted-instance/
title: Upgrading to OpenJDK 21 on customer-hosted instances \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:14.145570+00:00
---

# Upgrading to OpenJDK 21 on customer-hosted instances  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/upgrading-to-openjdk-21-customer-hosted-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Upgrading to OpenJDK 21 on customer-hosted instances Stay organized with collections  Save and categorize content based on your preferences. 

Looker uses OpenJDK for performance and memory usage improvements. Starting in Looker 26.8, Looker supports OpenJDK version 21 on customer-hosted Looker instances. This page describes how to upgrade from OpenJDK 11 to OpenJDK 21. OpenJDK 11 will be deprecated on Looker, therefore we recommend all customer-hosted instances upgrade to OpenJDK 21.

Upgrading to OpenJDK 21 from OpenJDK 11 requires downloading and installing OpenJDK 21 and then downloading and installing a new `looker` startup script.

To upgrade to OpenJDK 21, follow these steps:

  1. Stop the Looker process from shell, as the **looker** user:
         
         sudo su - looker
         cd /home/looker/looker
         ./looker stop
         

  2. If you're updating a Looker cluster, repeat the previous step to stop Looker on every node.

  3. Download and install [OpenJDK 21](https://jdk.java.net/archive/).

  4. Delete the previous version of the `looker` startup script from your `looker` directory:
         
         rm looker
         

  5. Download the new [`looker21` startup script](https://github.com/looker-open-source/customer-scripts/blob/main/startup_scripts/looker21) from the Looker public GitHub repository.

  6. Replace the old startup script with the new `looker21` script. _To run properly, the new startup script must be named`looker`_:
         
         mv <download_directory>/looker21 looker
         

  7. If you're updating a Looker cluster, repeat steps 4 through 6 on all nodes.

  8. Start up Looker on all nodes.
         
         ./looker start
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
