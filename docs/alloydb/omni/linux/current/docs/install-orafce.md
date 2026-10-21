---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-orafce/
title: Install orafce for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:54:31.433494+00:00
---

# Install orafce for AlloyDB Omni  |  AlloyDB Omni using RPM: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-orafce/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)



Send feedback 

#  Install orafce for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-orafce)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/install-orafce)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/install-orafce)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-orafce)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/install-orafce)

This page describes how to manually add the [orafce extension](https://github.com/orafce/orafce) to an existing AlloyDB Omni installation. The orafce extension provides functions and operators that emulate a subset of functions and packages from the Oracle database. This extension simplifies migration of applications from Oracle to PostgreSQL-compatible databases such as AlloyDB Omni. 

## Before you begin

[Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/deploy-vm) on your system. 

## Add orafce to your AlloyDB Omni installation

To add the orafce extension to your AlloyDB Omni installation, follow these steps:

  1. Add the PostgreSQL Yum Repository:
         
         sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
         

  2. Install PostgreSQL server and development packages:
         
         sudo dnf install -y "postgresql18-server"
         

  3. Install the Orafce extension:
         
         sudo dnf install -y orafce_18
         

  4. Create required symlinks so the extensions are in the expected paths:
         
         set -e
         PGVER="18"
         
         sudo mkdir -p "/usr/lib/postgresql/${PGVER}/share/extension"
         
         for file in /usr/pgsql-${PGVER}/share/extension/*; do
           target="/usr/lib/postgresql/${PGVER}/share/extension/$(basename "$file")"
           if [[ ! -e "$target" ]]; then
             sudo ln -s "$file" "$target" || (echo "Failed to link \"$file\" to \"$target\", exiting." && exit 1)
             echo "Created extension link for $(basename "$file")"
           else
             echo "Target $target already exists."
           fi
         done
         
         sudo mkdir -p "/usr/lib/postgresql/${PGVER}/lib"
         
         for file in /usr/pgsql-${PGVER}/lib/*; do
           target="/usr/lib/postgresql/${PGVER}/lib/$(basename "$file")"
           if [[ ! -e "$target" ]]; then
             sudo ln -s "$file" "$target" || (echo "Failed to link \"$file\" to \"$target\", exiting." && exit 1)
             echo "Created lib link for $(basename "$file")"
           else
             echo "Target $target already exists."
           fi
         done
         

  5. Connect to your database and run the `CREATE EXTENSION` command to enable orafce:

For instructions on connecting to your instance, see [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/run-connect). 
         
         CREATE EXTENSION IF NOT EXISTS ORAFCE;
         

  6. Confirm that orafce is installed and enabled:
         
         SELECT oracle.sysdate();
         

The output is similar to the following:
         
         postgres=# SELECT oracle.sysdate();
         sysdate
         ---------------------
         2025-12-12 16:36:30
         (1 row)
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
