---
url: https://docs.cloud.google.com/error-reporting/docs/setup/python/
title: Instrument Python apps for Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:24.708245+00:00
---

# Instrument Python apps for Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Instrument Python apps for Error Reporting Stay organized with collections  Save and categorize content based on your preferences. 

The [Error Reporting library for Python](https://github.com/googleapis/python-error-reporting/) lets you send error events directly from your Python applications to Error Reporting so that you can diagnose and monitor runtime crashes. Instrumenting your application with the library lets you report custom error events and capture errors even when your log buckets use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

For applications running on integrated Google Cloud services—including Cloud Run functions, [App Engine](https://docs.cloud.google.com/appengine/docs), [Compute Engine](https://docs.cloud.google.com/compute/docs), and [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)—Error Reporting can also infer error events automatically from Cloud Logging without the Error Reporting library for Python. For Error Reporting to infer error events from logs, your log entries must follow the [error formatting requirements](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages) and be stored in a non-CMEK log bucket owned by the originating project or by the destination project to which the logs were routed.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Error Reporting API , if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=clouderrorreporting.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Error Reporting API , if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=clouderrorreporting.googleapis.com)

  8. Prepare your environment for Python development. 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)




## Install the client library

The Error Reporting library for Python lets you monitor and view error events reported by Python applications running nearly anywhere.

  1. Instantiate a virtual environment and use [pip](https://pip.pypa.io/) to install the package:
         
         pip install google-cloud-error-reporting --upgrade
         

  2. Import the library and instantiate a client in order to begin reporting errors:

### Python

To authenticate to Error Reporting, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
         
         #!/usr/bin/env python
         #
         # Copyright 2022 Google, Inc.
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #    http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         
         def report_exception():
             from google.cloud import error_reporting
         
             client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
             try:
                 raise Exception("Something went wrong")
             except Exception:
                 [client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.html).[report_exception](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html#google_cloud_error_reporting_client_Client_report_exception)()
         
         
         
         
         def report_manual_error():
             from google.cloud import error_reporting
         
             client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
             [client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.html).[report](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)("An error has occurred.")
         
         
         
         
         if __name__ == "__main__":
             report_exception()
             report_manual_error()
         




For more information on installation, read the [documentation](https://cloud.google.com/python/docs/reference/clouderrorreporting/latest) for the Error Reporting library for Python. You can also report issues using the [issue tracker](https://github.com/googleapis/python-error-reporting/issues).

### Configure the client library

You can customize the behavior of Error Reporting library for Python. See [ client library documentation ](https://cloud.google.com/python/docs/reference/clouderrorreporting/latest) for configuration examples. 

## Run apps on Google Cloud

To create error groups by using [`projects.events.report`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report), your service account requires the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

Some Google Cloud services automatically grant the Error Reporting Writer role (`roles/errorreporting.writer`) to the appropriate service account. However, you must grant this role to the appropriate service account for some services.

### Cloud Run and Cloud Run functions

The default service account used by [Cloud Run](https://docs.cloud.google.com/run/docs) has the permissions of [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

The Error Reporting library for Python can be used without needing to explicitly provide credentials.

Cloud Run is configured to use Error Reporting automatically. Unhandled JavaScript exceptions will appear in Logging and be processed by Error Reporting without needing to use the Error Reporting library for Python.

**Note:** Error Reporting automatically creates an error event when a log entry contains a stack trace and the severity level of the log entry isn't set or is set to at least `ERROR`.

### App Engine flexible environment

[App Engine](https://docs.cloud.google.com/appengine/docs) grants the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`) to your default service account automatically.

The Error Reporting library for Python can be used without needing to explicitly provide credentials.

Error Reporting is automatically enabled for App Engine flexible environment applications. No additional setup is required. **Note:** Error log entries written to `stderr` are processed automatically by Error Reporting, without needing to use the Error Reporting library for Python directly.

### Google Kubernetes Engine

To use Error Reporting with Google Kubernetes Engine, do the following:

  1. Ensure that the service account to be used by your container has been granted the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

You can use either the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account.

For information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. Create your cluster and grant the cluster the `cloud-platform` [access scope](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).

For example, the following create command specifies the `cloud-platform` access scope and a service account:
         
         gcloud container clusters create CLUSTER_NAME --service-account  SERVICE_ACCT_NAME --scopes=cloud-platform
         


**Note:** After you create a cluster, you can't change its service account.

### Compute Engine

To use Error Reporting with Compute Engine VM instances, do the following:

  1. Ensure that the service account to be used by your VM instance has been granted the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

You can use either the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account.

For information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  3. Select the VM instance that you want to receive the `cloud-platform` [access scope](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).

  4. Click **Stop** , and then click **Edit**.

  5. In the **Identity and API access** section, select a service account that has the Error Reporting Writer role (`roles/errorreporting.writer`).

  6. In the **Access scopes** section, select **Allow full access to all Cloud APIs** , and then save your changes.

  7. Click **Start/Resume**.




## Example

You can manually report an error by calling the `report` method, as seen in the following example:

### Python

To authenticate to Error Reporting, set up Application Default Credentials. For more information, see Set up authentication. 
    
    
    #!/usr/bin/env python
    #
    # Copyright 2022 Google, Inc.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #    http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    
    def report_exception():
        from google.cloud import error_reporting
    
        client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
        try:
            raise Exception("Something went wrong")
        except Exception:
            [client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.html).[report_exception](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html#google_cloud_error_reporting_client_Client_report_exception)()
    
    
    
    
    def report_manual_error():
        from google.cloud import error_reporting
    
        client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
        [client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.html).[report](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)("An error has occurred.")
    
    
    
    
    if __name__ == "__main__":
        report_exception()
        report_manual_error()
    

## Run apps in a local development environment

To use the Error Reporting library for Python in a local development environment, such as running the library on your own workstation, you must provide your Error Reporting library for Python with the local application default credentials. For more information, see [Authenticate to Error Reporting](https://docs.cloud.google.com/error-reporting/docs/reference/authentication#client-libs).

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

**Note:** If the gcloud CLI prints a warning that your account doesn't have the `serviceusage.services.use` permission, then some gcloud CLI commands and client libraries might not work. Ask an administrator to grant you the Service Usage Consumer IAM role (`roles/serviceusage.serviceUsageConsumer`), then run the following command: 
         
         gcloud auth application-default set-quota-project PROJECT_ID

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/error-reporting/docs/reference/authentication#local-development). 

The [`projects.events.report` method](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report) also supports API keys. If you want to use API keys for authentication, you do not need to set up a local Application Default Credentials file. For more information, see [Create an API key](https://docs.cloud.google.com/docs/authentication/api-keys#create) in the Google Cloud authentication documentation. 

## View error groups

In the Google Cloud console, go to the **Error Reporting** page: 

[Go to **Error Reporting**](https://console.cloud.google.com/errors)

You can also find this page by using the search bar.

For more information, see [View and filter error groups](https://docs.cloud.google.com/error-reporting/docs/viewing-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
