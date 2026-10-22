---
url: https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-web-server/
title: Troubleshooting Airflow web server issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:32.677955+00:00
---

# Troubleshooting Airflow web server issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-web-server/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Troubleshooting Airflow web server issues Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-web-server "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-web-server "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page provides troubleshooting steps and information for common Airflow web server issues.

The Airflow web server is an Airflow component that provides a user interface for managing Airflow DAGs and tasks. This page describes troubleshooting steps for various issues with accessing the Airflow web server of your environment or for web server-related warnings visible in Airflow logs.

## Can't access Airflow UI when network access controls are enabled

**Symptom** : After web server access controls are configured, it's not possible to access Airflow UI. Usually, the error code displayed in this situation is 403.

**Information about the issue** : Managed Airflow supports [web server network access controls](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface#network-access-controls), which lets you specify IP ranges that are allowed to connect to the web server.

Problems with accessing Airflow UI usually result in error 403. To check if the error is related to web server network access controls, do the following:

  1. In the list of environments, click the name of your environment. The **Environment details** page opens.
  2. Go to the **Environment configuration** tab.
  3. Check if the **Web server access control** item is set to **All IP addresses have access (default)**.
  4. If a value different than **All IP addresses have access (default)** is configured, then network access control is enabled and the visibility of the Airflow UI is limited to the provided IPv4 and IPv6 address ranges. In this case, the problem might be related to web server network access controls.



In most cases, the cause of the issue is the mismatch between the intended IP that you specified and the IP that is actually resolved to connect to the Airflow UI. To troubleshoot the problem, do the following:

  1. In the list of environments, click the name of your environment. The **Environment details** page opens.

  2. Go to the **Environment configuration** tab.

  3. Find the **Web server access control** item and click **Edit**.

  4. In the **Web server network access control** dialog, select **Allow access from all IP addresses**.

  5. Access the Airflow UI multiple times and verify that it works without any issues:

     * If you don't experience problems, continue to the next step.

     * If you experience a problem at this point, it means that the issue might be related to your IAM permissions configuration. For more information about the IAM permissions for Managed Airflow, see [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control).

  6. In the **Web server network access control** dialog, select **Allow access only from specific IP addresses**.

  7. Add the `0.0.0.0/0` IP range, then access the Airflow UI multiple times and verify that it works without issues:

     * If you don't experience problems, then the IP that you're connecting with is an IPv4 address.

     * If you experience a problem at this point, it means the IP you're connecting with is an IPv6 address.

  8. Delete the `0.0.0.0/0` IP range, and add the `::/0` IP range.

     * If you don't experience problems, then the IP that you're connecting with is an IPv6 address.

     * If you experience a problem at this point, it means the IP you're connecting with is an IPv4 address.

  9. Now you determined if your resolved address is IPv4 or IPv6.

  10. Depending on the address type, narrow down the `::/0` or `0.0.0.0/0` ranges to more specific ones, to verify the broadest range when the access stops working:

     * You can start with the wide subnet mask (such as `192.0.2.0/8`) that includes the address that you assume to be your IP address. 

     * To determine your IP address, you can use a third-party service that provides your external IP address when you visit its page. You can search for such services by the "what is my IP address" search query). 




## Configuration values aren't displayed on the configuration page

Some Airflow configuration parameters of Airflow are hidden on the configuration page to prevent access to potentially sensitive information. For example, credentials to access the Airflow database are not displayed.

**Warning:**

If you configure Airflow to display these parameters, then **any Airflow user with`Admin` and `Op` permission will be able to access this information.** By default, Airflow assigns the `Op` role to new Airflow users.

To prevent Airflow users with the `Op` role from accessing the configuration page:

  1. Go to the **Security** > **List Roles** configuration page in the Airflow UI.
  2. Revoke the **can read Configurations** and **menu access on Configurations** permissions from the `Op` role.



To display hidden fields, [override](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the following Airflow configuration option. We recommend to revert the changes after you obtain the required values.

Section | Key | Value | Notes  
---|---|---|---  
`webserver` |  `expose_config` |  `True` |  The default value is `non-sensitive-only`. Set to `False` to hide all configuration parameters.  
  
## DAG crashes the Airflow web server or causes it to return a '502 gateway timeout' error

Web server failures can occur for several different reasons. Check the **airflow-webserver** logs in [Cloud Logging](https://docs.cloud.google.com/composer/docs/composer-1/view-logs#streaming) to determine the cause of the `502 gateway timeout` error.

### Heavy load computation

This section applies only to Managed Airflow (Legacy Gen 1).

Unlike the worker and scheduler nodes, whose machine types can be customized to have greater CPU and memory capacity, the web server uses a fixed machine type, which can lead to DAG parsing failures if the parse-time computation is too heavy.

Note that the web server has [2 vCPUs and 2 GB of memory](https://cloud.google.com/composer/pricing#environment_sizing). The default value for `core-dagbag_import_timeout` is 30 seconds. This timeout value defines the upper limit for how long Airflow spends loading a Python module in the `/dags` folder.

### Incorrect permissions

This section applies only to Managed Airflow (Legacy Gen 1).

The web server does not run under the same service account as the workers and scheduler. As such, the workers and scheduler might be able to access user-managed resources that the web server cannot access.

We recommend that you avoid accessing non-public resources during DAG parsing. Sometimes, this is unavoidable, and you will need to grant permissions to the web server's service account. The service account name is derived from your web server domain. For example, if the domain is `example-tp.appspot.com`, the service account is `example-tp@appspot.gserviceaccount.com`.

### DAG errors

This section applies only to Managed Airflow (Legacy Gen 1).

The web server runs on App Engine and is separate from your environment's GKE cluster. The web server parses the DAG definition files, and a `502 gateway timeout` can occur if there are errors in the DAG. Airflow works normally without a functional web server if the problematic DAG is not breaking any processes running in GKE. In this case, you can use `gcloud composer environments run` to retrieve details from your environment and as a workaround if the web server becomes unavailable.

In other cases, you can run DAG parsing in GKE and look for DAGs that throw fatal Python exceptions or that time out (default 30 seconds). To troubleshoot, connect to a remote shell in an Airflow worker container and test for syntax errors. For more information, see [Testing DAGs](https://docs.cloud.google.com/composer/docs/composer-1/test-dags).

## What's next

  * [Access Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface)
  * [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
