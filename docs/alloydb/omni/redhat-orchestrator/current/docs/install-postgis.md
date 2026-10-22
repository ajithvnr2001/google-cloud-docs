---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-postgis/
title: Install PostGIS for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:55:23.796663+00:00
---

# Install PostGIS for AlloyDB Omni  |  AlloyDB Omni using the RPM orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-postgis/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Install PostGIS for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-postgis)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-postgis)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis)



To store, index, and query geospatial data in AlloyDB Omni, you can manually add the [PostGIS extension](https://postgis.net/) to your installation.

## Before you begin

[Install AlloyDB Omni using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

## Add PostGIS to your AlloyDB Omni installation

To add the PostGIS extension to your AlloyDB Omni cluster, follow these steps manually on all database nodes including read pool nodes in your cluster: 

  1. Initialize Red Hat Subscription Manager on the VM where you installed the AlloyDB Omni server:
         
         sudo dnf install -y subscription-manager
         sudo subscription-manager register --username "RHSM_USER" --password "RHSM_PASS" --auto-attach --force
         

Replace the following:

     * `RHSM_USER`: the Red Hat Subscription Manager user.
     * `RHSM_PASS`: the Red Hat Subscription Manager password.
  2. Enable the CodeReady Builder repository:
         
         sudo subscription-manager repos --enable="codeready-builder-for-rhel-9-$ARCH-rpms"
         

Replace `ARCH` with the RHEL architecture that you want to use—for example, `x86_64`.

  3. Add the PostgreSQL Yum repository:
         
         sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
         

  4. Install the PostGIS extension:
         
         sudo dnf install -y postgis35_18
         

  5. Create required symlinks so the extensions are in the expected paths:
         
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
         

  6. Connect to your database and run the `CREATE EXTENSION` command to enable PostGIS:

For instructions on connecting to your instance, see [Connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/connect).

**Note:** You only need to enable the extension once on the primary database instance. 
         
         CREATE EXTENSION IF NOT EXISTS POSTGIS;
         

  7. Confirm that PostGIS is installed and enabled:
         
         SELECT postgis_full_version();
         

The output is similar to the following:
         
         postgres=# SELECT postgis_full_version();
         postgis_full_version
         --------------------------------------------------------------------------------------------------------------------------------
         POSTGIS="3.3.2 4975da8" [EXTENSION] PGSQL="150" GEOS="3.11.1-CAPI-1.18.1" PROJ="9.1.1" LIBXML="2.9.14" LIBJSON="0.16" LIBPROTOBUF="1.4.1" WAGYU="0.5.0 (Internal)"
         (1 row)
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
