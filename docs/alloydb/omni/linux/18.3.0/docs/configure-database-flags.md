---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/configure-database-flags/
title: Configure AlloyDB Omni database parameters \u00a0|\u00a0 AlloyDB Omni using RPM: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:26.152063+00:00
---

# Configure AlloyDB Omni database parameters  |  AlloyDB Omni using RPM: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/configure-database-flags/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)



Send feedback 

#  Configure AlloyDB Omni database parameters Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/configure-database-flags)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/configure-database-flags)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/configure-database-flags)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-database-flags)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/configure-database-flags)

To configure a database parameter for AlloyDB Omni, you can update [Grand Unified Configuration (GUC) parameters](https://www.postgresql.org/docs/current/config-setting.html) in either of the following: 

  * The `postgresql.conf` file for environments running AlloyDB Omni on a VM.



## Update a parameter in AlloyDB Omni using RPM

In an AlloyDB Omni using RPM installation, you can update a parameter by editing the `postgresql.conf` file as follows:

  1. Locate the `postgresql.conf` configuration file for your installation of AlloyDB Omni.

  2. Use a text editor to add or update a database flag in `postgresql.conf`.

For example, to [enforce password expiration](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/manage-password-policy#enforce-password-expiration), set the following flag in the `postgresql.conf` file:
         
         password.enforce_expiration = ON
         

  3. After your database flags are added or edited, reload the `postgresql.conf` file for the changes to take effect by restarting the AlloyDB Omni service:
         
         sudo systemctl restart alloydbomni18




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
