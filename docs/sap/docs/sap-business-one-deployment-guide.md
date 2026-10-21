---
url: https://docs.cloud.google.com/sap/docs/sap-business-one-deployment-guide/
title: Deploying SAP Business One on SAP HANA in Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:45.508897+00:00
---

# Deploying SAP Business One on SAP HANA in Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-business-one-deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deploying SAP Business One on SAP HANA in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

You deploy _SAP Business One, version for SAP HANA_ on Google Cloud by first deploying SAP HANA on a Compute Engine virtual machine (VM) and then installing SAP Business One.

For information about software versions and resource requirements for SAP Business One on Google Cloud, see the [SAP Business One planning guide](https://docs.cloud.google.com/sap/docs/sap-business-one-planning-guide).

## High-level steps for deploying SAP Business One

  1. Create a VM and install SAP HANA by following the instructions in the [SAP HANA deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide).

  2. Confirm that the following Linux packages are installed on the target VM:

     * `python-crypto`
     * `samba`
     * `samba-client`
  3. Install _SAP Business One, version for SAP HANA_ by following the instructions that are provided by SAP in the _SAP Business One Administrator's Guide, version for SAP HANA_. You can find the guide in [the SAP Help Portal](https://help.sap.com/viewer/p/SAP_BUSINESS_ONE_VERSION_FOR_SAP_HANA) after selecting your version from the drop down menu at the top of the page.




## What's next

  * For information about SAP HANA on Google Cloud, see: 
    * [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide)
    * [SAP HANA deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide)
  * For information about administering and operating SAP Business One, see the SAP documentation in the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_BUSINESS_ONE_VERSION_FOR_SAP_HANA).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
