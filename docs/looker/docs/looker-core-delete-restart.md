---
url: https://docs.cloud.google.com/looker/docs/looker-core-delete-restart/
title: Delete or restart a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:57:20.445035+00:00
---

# Delete or restart a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-delete-restart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Delete or restart a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Instance deletion is permanent and unrecoverable.

You can delete or restart a Looker (Google Cloud core) instance.

## Required role

To get the permissions that you need to delete or restart a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a Looker (Google Cloud core) instance

Instance deletion is permanent and unrecoverable.

Deleting a Looker (Google Cloud core) instance that is [associated with a Data Studio Pro subscription](https://docs.cloud.google.com/looker/docs/looker-core-lsp) immediately converts any in-use complimentary Data Studio Pro licenses to paid licenses.

To delete a Looker (Google Cloud core) instance, select one of the following options:

### console

  1. On the **Instances** page, click the three-dot menu beside the instance.
  2. Select **Delete Instance**. If the instance is currently being modified, you will not be able to delete it.
  3. In the pop-up, confirm that you want to delete your instance by typing the instance name in the provided field and clicking **DELETE**.



You can also delete an instance from its configuration page by clicking **DELETE** in the instance configuration page icon bar.

###  gcloud 
    
    
    gcloud looker instances delete INSTANCE_NAME --region=REGION --async
    

Replace the following:

  * INSTANCE_NAME: the [name](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) of the Looker (Google Cloud core) instance
  * REGION: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in



## Restart a Looker (Google Cloud core) instance

Restarting a Looker (Google Cloud core) instance stops any in-process Looker processes on the instance — including running queries, schedules, and alerts — and then restarts the instance. Once the restart has been completed, the instance will automatically resume its normal operations. Any queries that were running at the time of restart won't be completed unless you reinitiate them. Schedules and alerts will run on their specified cadence, but any jobs that were scheduled or that were being executed during the restart won't be completed.

If the instance is currently being modified, wait for it to complete its updates before you attempt a restart.

To restart a Looker (Google Cloud core) instance, select one of the following options:

### console

  1. On the **Instances** page, click the name of the instance to view its configuration settings.
  2. Click **RESTART** in the instance configuration page icon bar.



###  gcloud 
    
    
    gcloud looker instances restart INSTANCE_NAME --region=REGION --async
    

Replace the following:

  * INSTANCE_NAME: the [name](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) of the Looker (Google Cloud core) instance
  * REGION: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in



**Note:** If your `gcp.restrictTLSCipherSuites` organization policy constraint doesn't include any cipher suites that are in the [MODERN SSL policy profile](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy), Looker will return an error, and the instance restart will fail. Update the policy to resolve the error and restart the instance. See the [Restrict TLS cipher suites](https://docs.cloud.google.com/looker/docs/looker-core-tls-cipher-suites#policy_violations) documentation page for more information.

## What's next

  * [Create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)
  * [Back up and restore a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-backup-restore)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
