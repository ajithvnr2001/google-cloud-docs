---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-accounts/
title: Using service account credentials \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:59.028636+00:00
---

# Using service account credentials  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using service account credentials Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Google service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to give your Knative serving services the necessary permissions to access Google Cloud services, for example [Cloud Monitoring](https://docs.cloud.google.com/monitoring). Each service account let you define a specific set of [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) permissions that you can associate with each of your services through Kubernetes Secrets.

To create a service account, you can use the following steps that are provided here for convenience. For complete details about creating and managing service accounts, see the [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

### Console

To create a service account and then download the JSON key file using the Google Cloud console:

  1. Go to the **Service Accounts** page in Google Cloud console.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click _add_ **Create Service Account**.

  3. Under **Service account details** , specify a name of your choice in **Service account name**.

  4. Optionally, modify the **Service account ID** and add a description.

  5. Click **Create and continue**.

  6. Under **Grant this service account access to a project** , from the **Select a role** drop-down list, select one or more roles for which you the permissions granted to the service account. For example, [Monitoring Metric Writer role](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc).

  7. Click **Continue** , to

  8. Optionally, you can specify users or groups who you want to associate with the service account.

  9. Click **Done** to create the service account.

  10. In the list of service accounts, next to the service account you created, click _more_vert_ **Actions > Manage keys**.

  11. Click **Add Key > Create a new key**.

  12. Under **Key type** , select **JSON**.

  13. Click **Create**.




### gcloud

See the following pages to learn how to use the gcloud CLI to:

  1. [Create service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  2. [Assign roles and permissions](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts).
  3. [Create account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).



After you create a key and download the JSON file which contains the credentials of your service account, you use that key to create a secret that you can then associate with your Knative serving services.

See [Using secrets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/using-secrets) to learn how to create and then associate secrets with your services.

## Next steps

Learn how to [manage access](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/managing-access) to your services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
