---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters/
title: Configure database parameters \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:24.316635+00:00
---

# Configure database parameters  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Configure database parameters Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/configure-database-parameters)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/configure-database-parameters)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-database-parameters)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters)

This page describes how to configure database parameters using the AlloyDB Omni RPM orchestrator. 

Database parameters, also known as Grand Unified Configuration (GUC) parameters, let you tune the performance and behavior of your AlloyDB Omni database cluster. For more information, see [Setting parameters](https://www.postgresql.org/docs/18/config-setting.html) in the PostgreSQL documentation.

## Before you begin

Before you configure database parameters, make sure that you have:

  1. [Installed](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-orchestrator) the AlloyDB Omni orchestrator.
  2. Provisioned and [created](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster) your AlloyDB Omni cluster.



## Configure database parameters

To configure database parameters, you use the `parameters` field within the `primarySpec` section of your `DBCluster` resource specification.

### Update the resource specification

Add or modify the required parameters and their values in your `DBCluster` resource specification. You can do this to configure parameters during cluster creation or to update parameters after the cluster is created.

**Note:** The `parameters` block specifies the full map of database (GUC) parameters for your cluster. When updating this section, include all parameters that you want to maintain. Copying and pasting only new parameters without including existing ones overwrites and removes the omitted parameters. 

The following snippet shows examples of GUC parameters. You can configure other supported database parameters similarly:
    
    
    DBCluster:
      metadata:
        name: CLUSTER_NAME
      spec:
        primarySpec:
          # ... other settings ...
          **parameters :
            # ... existing parameters ...
            max_wal_size: "MAX_WAL_SIZE"
            max_connections: "MAX_CONNECTIONS_LIMIT"
            huge_pages: "HUGE_PAGES"
            log_statement: "LOG_STATEMENT"
            # ... other parameters ...**
    

Replace the following:

  * `CLUSTER_NAME`: the name of your database cluster.
  * `MAX_WAL_SIZE`: an example parameter controlling the maximum size the WAL can grow to between automatic WAL checkpoints, for example `2GB`.
  * `MAX_CONNECTIONS_LIMIT`: an example parameter controlling the maximum number of concurrent connections allowed to the database server, for example, `200`. Minimum supported value is `50`.
  * `HUGE_PAGES`: an example parameter controlling the use of huge pages, for example `on`.
  * `LOG_STATEMENT`: an example parameter controlling which SQL statements are logged, for example `all`.



## Apply the configuration

Apply the changes using your preferred orchestrator interface.

###  Ansible 

If you're managing your AlloyDB Omni RPM orchestrator infrastructure directly using Ansible, it triggers updates by running the appropriate playbook and passing the selected `update_action` as an extra variable.

Sample file for `update.yml`:
    
    
    ---
    - hosts: localhost
      vars:
        update_action: "update_resource_spec"
        ansible_user: your_ssh_user
        ansible_ssh_private_key_file: ~/path/to/private-key
      roles:
        - role: google.alloydbomni_orchestrator.update
    

Run the Ansible command:
    
    
    ansible-playbook -i DEPLOYMENT_SPECIFICATION update.yml -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.




###  `alloydbctl`
    
    
    alloydbctl apply -d DEPLOYMENT_SPECIFICATION -r DBCLUSTER_SPECIFICATION

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.




**Note:** Some database parameters require a restart of the database service to take effect. The AlloyDB Omni cluster manager automatically handles these restarts when you apply the changes.

## Verify parameter changes

After applying the configuration, you can verify that the parameters are updated using the `SHOW` command in `psql`:
    
    
    SHOW PARAMETER_NAME;

Replace `PARAMETER_NAME` with the name of the parameter that you configured.

## Audit database parameters using the web UI

You can audit active database flags and identify customized parameters that differ from default engine values using the **Database flags** page in the AlloyDB Omni web user interface.

To audit database parameters in the web UI, complete the following steps:

  1. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/connect-web-ui) and select your cluster.
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
