---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-secret-manager/
title: Configure Secret Manager for your environment \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:07.269212+00:00
---

# Configure Secret Manager for your environment  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-secret-manager/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure Secret Manager for your environment Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/configure-secret-manager "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-secret-manager "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page shows how to use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) to securely store Airflow connections and secrets.

## Before you begin

  * To use Secret Manager, your Managed Airflow environment must use Airflow 1.10.10 or later and Python 3.6 or later.
  * Python 2 is not supported.



## Configure Secret Manager for your environment

This section explains how to configure Secret Manager so that you can use secrets with your Managed Airflow environment.

### Enable the Secret Manager API

###  Console 

Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

###  gcloud 

Enable the Secret Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable secretmanager.googleapis.com

### Configure access control

You must configure access control so that Airflow can access secrets stored in Secret Manager.

To do so, the service account that accesses secrets must have a role with the `secretmanager.versions.access` permission. For example, the **Secret Manager Secret Accessor** role includes this permission.

You can grant this role at the [Secret, Project, Folder, or Org level](https://docs.cloud.google.com/secret-manager/docs/access-control#least-privilege).

Use one of the following options:

  * (Recommended) [Grant this role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) to the [service account of your environment](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account).

  * Override the service account under which Airflow accesses Secret Manager.

**Caution:** This method is less advisable, because it requires storing service account credentials in a file, which increases the risk that they might be compromised.
    1. [Grant this role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) to a service account.
    2. Set the `gcp_key_path` parameter of the `backend_kwargs` Airflow configuration option to point to a JSON file with the service account credentials.



### Enable DAG serialization

In general, you should only use the Secret Manager backend from within the `execute()` methods of your operators, or with the [Jinja templates](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#templating-with-jinja). For example, you can retrieve variables using `var.value.example_var`.

The Airflow web server runs under a different service account with limited permissions, so it cannot access secrets in Secret Manager. If your DAG code accesses secrets during DAG processing (not just from tasks) and it is not possible to adjust it to access secrets from within the `execute()` methods, then [enable DAG serialization](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization). After you do so, the Airflow web server takes processed DAGs and does not need access to secrets.

### Enable and configure the Secret Manager backend

  1. [Override](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value  
---|---|---  
`secrets` | `backend` | `airflow.providers.google.cloud.secrets.secret_manager.CloudSecretManagerBackend`  
**Caution:** Do not use `airflow.contrib.secrets.gcp_secrets_manager.CloudSecretsManagerBackend` because this value does not allow you to view logs in the Airflow UI.
  2. Add optional settings by [overriding](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value  
---|---|---  
`secrets` |  `backend_kwargs` |  See the following description.  
  
The `backend_kwargs` value is the JSON representation of the [`backend_kwargs` object](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/secrets-backends/google-cloud-secret-manager-backend.html#backend-parameters) with the following fields:

     * `connections_prefix`: prefix of the secret name to read in order to get Connections. The default is `airflow-connections`.
     * `variables_prefix`: prefix of the secret name to read in order to get Variables. The default is: `airflow-variables`.
     * `gcp_key_path`: path to the Google Cloud Credential JSON file (if not provided, the default service account is used).
     * `gcp_keyfile_dict`: Google Cloud Credential JSON dictionary. Mutually exclusive with `gcp_key_path`.
     * `sep`: separator used to concatenate `connections_prefix` and `conn_id`. The default is `-`.
     * `project_id`: Google Cloud Project Id where secrets are stored.

For example, the value of `backend_kwargs` can be: `{"project_id": "<project id>", "connections_prefix":"example-connections", "variables_prefix":"example-variables", "sep":"-"}`.

**Note:** The `Keyfile Secret Name (in GCP Secret Manager)` option in Airflow connection is supported only when Secret Manager and Managed Airflow are in the same Google Cloud project.



### Add connections and variables in Secret Manager

Create secrets by following steps outlined in [Creating secrets and versions](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

#### Variables

  * Must use the `[variables_prefix][sep][variable_name]` format.
  * The default value for `[variables_prefix]` is `airflow-variables`.
  * The default separator `[sep]` is `-`.



For example, if the variable name is `example-var`, then the secret name is `airflow-variables-example-var`.

**Note:** If you want to use different values for `[variables_prefix]`, `[connection_prefix]` or `[sep]`, use the optional settings as described further in the Enable and configure Secret Manager backend section.

#### Connection names

  * Must use the `[connection_prefix][sep][connection_name]` format.
  * The default value for `[connection_prefix]` is `airflow-connections`.
  * The default separator `[sep]` is `-`.



For example, if the connection name is `exampleConnection`, then the secret name is `airflow-connections-exampleConnection`.

#### Connection values

  * Must use [URI representation](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-connection-uri). For example, `postgresql://login:secret@examplehost:9000`.

  * The URI must be [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) (percent encoded). For example, a password that has a space symbol in it must be URL-encoded as follows: `postgresql://login:secret%20password@examplehost:9000`.




Airflow has a [convenience method](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-connection-uri) for generating connection URIs. An example of how to encode a complex URL with JSON extras is available in the [Airflow documentation](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/connections/mysql.html).

## Use Secret Manager with Managed Airflow

When fetching variables and connections, Managed Airflow checks Secret Manager first. If the requested variable or connection is not found, Managed Airflow then checks the environment variables and the Airflow database.

**Note:** For security reasons, variables and connections from Secret Manager are not visible in the Airflow UI.

### Read variables using Jinja templating

You can use Secret Manager to read variables with [Jinja templating](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#templating-with-jinja) for templated operator fields (resolved at the execution time).

For the `airflow-variables-secret_filename` secret:
    
    
    file_name = '{{var.value.secret_filename}}'
    

### Read variables using custom operators and callbacks

You can also use Secret Manager to read variables in custom operators or callback methods from operators. Reading variables from inside DAGs can negatively impact performance, so use Jinja templates if you want to use variables in your DAGs.

For example, for the `airflow-variables-secret_filename` secret:
    
    
    from airflow.models.variable import Variable
    file_name = Variable.get('secret_filename')
    

### Read connections

Unless you are writing a custom operator, you should rarely need to access connections directly. Most hooks get the connection name as their instantiation parameter, and should retrieve connections from the secret backend automatically when tasks are executed.

Reading connections directly may be useful when writing your own hook.

For example, for the `airflow-connections-exampleConnection` connection:
    
    
    from airflow.hooks.base_hook import BaseHook
    exampleConnection = BaseHook.get_connection('exampleConnection')
    

`BaseHook.get_connection` returns a `Connection` object. It is possible to get the URI string representation of a connection like this:
    
    
    exampleConnectionUri = BaseHook.get_connection('exampleConnection').get_uri()
    

## What's next

  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations)
  * [Access the Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
