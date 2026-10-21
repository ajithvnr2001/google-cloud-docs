---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-database-flags/
title: Configure AlloyDB Omni database parameters \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:28:31.318108+00:00
---

# Configure AlloyDB Omni database parameters  |  AlloyDB Omni using the container orchestrator: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-database-flags/

This page documents AlloyDB Omni version **17.7.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/overview)



Send feedback 

#  Configure AlloyDB Omni database parameters Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

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

To configure a database parameter for AlloyDB Omni, you can update [Grand Unified Configuration (GUC) parameters](https://www.postgresql.org/docs/current/config-setting.html) in either of the following: 

  * The `postgresql.conf` file for environments running AlloyDB Omni on a VM.

  * The database cluster manifest for environments running AlloyDB Omni on [a Kubernetes cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/deploy-kubernetes).




## Update a parameter in containerized AlloyDB Omni

In an AlloyDB Omni running on a VM, you can update a parameter by editing the `postgresql.conf` file as follows:

  1. Locate the `postgresql.conf` configuration file for your installation of AlloyDB Omni.

  2. Use a text editor to add or update a database flag in `postgresql.conf`.

For example, to [enforce password expiration](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage-password-policy#enforce-password-expiration), set the following flag in the `postgresql.conf` file:
         
         password.enforce_expiration = ON
         

  3. After your database flags are added or edited, reload the `postgresql.conf` file for the changes to take effect. For example, if you [installed AlloyDB Omni using Docker](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/quickstart#install-using-docker), run the following to restart your Docker instance and reload `postgresql.conf`:
         
         docker restart CONTAINER-NAME




For more information, see [Setting parameters](https://www.postgresql.org/docs/current/config-setting.html) in PostgreSQL documentation.

## Update a parameter in AlloyDB Omni on a Kubernetes cluster

You can configure database parameters using the `parameters` field in the `primarySpec` section of your database cluster manifest:
    
    
    spec:
      primarySpec:
        parameters:
          "PARAMETER_NAME": "PARAMETER_VALUE"
          ...
    

Replace the following:

  * `PARAMETER_NAME`: the name of the parameter—for example, `autovacuum`.
  * `PARAMETER_VALUE`: the value of the parameter—for example, `off`.

**Note:** Repeat the `PARAMETER_NAME": "PARAMETER_VALUE` line of code for each name-value pair that you have.

Some parameters require you to restart your cluster for the changes to take effect. You can obtain a list of parameters that require a restart from `pg_catalog.pg_settings`. Any parameter with `pg_catalog.pg_settings.context = 'postmaster'` requires a restart.

To update database parameters, run the following command:
    
    
    kubectl patch dbclusters.alloydbomni.dbadmin.goog dbcluster-sample -p '{"spec":{"primarySpec":{"parameters": {"PARAMETER_NAME": "PARAMETER_VALUE"}}}}' --type=merge

**Note:** For parameters that require a restart, updating parameters restarts the database automatically.

Parameter settings are located in the `status` part of the `currentParameters` field.

To view database parameters, run the following:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog dbcluster-sample -o jsonpath={.status.primary.currentParameters}

The output looks similar to the following:
    
    
    {"autovacuum":"off","max_connections":"3000"}
    

If AlloyDB Omni cannot apply the parameters that you request in the database cluster manifest, then the values for the `currentParameters` field can differ from the values in the `parameters` field of your manifest. For example, you apply a non-existent parameter or you set a string value to an integer parameter.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
