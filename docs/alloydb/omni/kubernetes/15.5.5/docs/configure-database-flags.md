---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/configure-database-flags/
title: Configure AlloyDB Omni database flags \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:59.994741+00:00
---

# Configure AlloyDB Omni database flags  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/configure-database-flags/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Configure AlloyDB Omni database flags Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-database-flags)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-database-flags)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/configure-database-flags)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-database-flags)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/configure-database-flags)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-database-flags)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-database-flags)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-database-flags)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/configure-database-flags)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/configure-database-flags)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/configure-database-flags)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-database-flags)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/configure-database-flags)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/configure-database-flags)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/configure-database-flags)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/configure-database-flags)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/configure-database-flags)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/configure-database-flags)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/configure-database-flags)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-database-flags)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/configure-database-flags)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/configure-database-flags)

To configure a database flag for AlloyDB Omni, you add or update [Grand Unified Configuration (GUC)](https://www.postgresql.org/docs/current/config-setting.html) parameters in the `postgresql.conf` file. 

## Add or update a GUC parameter

There are a few ways to update and add GUC parameters. This document covers the most fundamental way, which is to edit your `postgresql.conf` file. For more information, see [Setting parameters](https://www.postgresql.org/docs/current/config-setting.html) in PostgreSQL documentation.

To add or update a GUC parameter by editing the `postgresql.config` file, do the following:

  1. Locate the `postgresql.conf` configuration file for your installation of AlloyDB Omni.

  2. Use a text editor to add or update a database flag in `postgresql.conf`.

For example, to [enforce password expiration](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/manage-password-policy#enforce-password-expiration), set the following flag in the `postgresql.conf` file:
         
         password.enforce_expiration = ON
         

  3. After your database flags are added or edited, reload the `postgresql.conf` file for the changes to take effect. For example, if you [installed AlloyDB Omni using Docker](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/quickstart#install-using-docker), run the following to restart your Docker instance and reload `postgresql.conf`:
         
         docker restart CONTAINER-NAME
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
