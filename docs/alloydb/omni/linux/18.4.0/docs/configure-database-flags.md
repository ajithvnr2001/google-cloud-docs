---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/configure-database-flags/
title: Configure AlloyDB Omni database parameters \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:46.650868+00:00
---

# Configure AlloyDB Omni database parameters  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/configure-database-flags/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)



Send feedback 

#  Configure AlloyDB Omni database parameters Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/configure-database-flags)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/configure-database-flags)
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

For example, to [enforce password expiration](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/manage-password-policy#enforce-password-expiration), set the following flag in the `postgresql.conf` file:
         
         password.enforce_expiration = ON
         

  3. After your database flags are added or edited, reload the `postgresql.conf` file for the changes to take effect by restarting the AlloyDB Omni service:
         
         sudo systemctl restart alloydbomni18




## Audit database parameters using the web UI

You can audit active database flags and identify customized parameters that differ from default engine values using the **Database flags** page in the AlloyDB Omni web user interface.

To audit database parameters in the web UI, complete the following steps:

  1. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/connect-web-ui) and select your cluster.
  2. In the navigation menu, click **Database flags**.
  3. Use the following controls to search and filter parameters: 
     * **Search for flags** : Enter a keyword (for example, `max`) to filter parameters by name.
     * **Show modified flags** : Select this checkbox to display only parameters whose active values differ from their default engine values. Customized values are also highlighted in yellow in the **Current value** column.
     * **Collapse all** or **Expand all** : Collapse or expand the parameter category groups (such as **Google AlloyDB Options** , **Client Connection Defaults / Locale and Formatting** , **Client Connection Defaults / Other Defaults** , and **Client Connection Defaults / Shared Library Preloading**).
  4. Review the parameter table columns within each category group: 
     * **Setting** : The name of the database parameter.
     * **Type** : The data type of the parameter (for example, `INTEGER`).
     * **Current value** : The active value of the parameter on the instance (highlighted in yellow if modified from the default).
     * **Default value** : The default engine value for the parameter.
     * **Restart required** : Indicates whether modifying the parameter requires a database restart (`true` or `false`).
     * **Source** : The configuration source of the current value (for example, `default`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
