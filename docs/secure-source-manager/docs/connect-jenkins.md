---
url: https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins/
title: Connect to Jenkins \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:06.070093+00:00
---

# Connect to Jenkins  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Connect to Jenkins Stay organized with collections  Save and categorize content based on your preferences. 

You can start automatic builds with [Jenkins](https://www.jenkins.io/) triggers and Secure Source Manager webhooks.

## Required roles

To get the permissions that you need to create Jenkins build triggers, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Repo Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) on your repository
  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Set up a webhook trigger

Jenkins uses build trigger plugins to enable CI/CD automation. You can configure triggers to listen for incoming events, such as when a new commit is pushed to a repository or when a pull request is initiated, and then automatically execute a build when new events come in. You can also configure triggers to build code on any changes to your source repository or only on changes that match certain criteria.

**To set up a generic Jenkins webhook Trigger:**

  1. Install the Jenkins [**Git Plugin**](https://plugins.jenkins.io/git/), [**SSH Credential Plugin**](https://plugins.jenkins.io/ssh-credentials/) and [**Generic Webhook Trigger Plugin**](https://plugins.jenkins.io/generic-webhook-trigger/) on your Jenkins server.

  2. Generate a valid SSH key pair in your Jenkins server. Secure Source Manager only supports RSA type keys.

  3. Add the Secure Source Manager instance domain to the Jenkins server SSH `known_hosts` file by running the following command:
         
         ssh -t git@INSTANCE_ID-INSTANCE_PROJECT_NUMBER-ssh.us-central1.sourcemanager.dev
         

Where:

     * INSTANCE_ID is the name of your Secure Source Manager instance.
     * INSTANCE_PROJECT_NUMBER is the project number of your Secure Source Manager instance. See [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for information on where to find your project number.

For example, the following command adds the instance domain for an instance named `prod-test-instance` with a project number of `123456789`.
    
    ssh -t git@prod-test-instance-123456789-ssh.us-central1.sourcemanager.dev
    

Reply `yes` to add the instance domain to the list of known hosts.

  4. In the Jenkins **Manage Credentials** page:

     1. Select **SSH username with private key**.
     2. Paste in your Jenkins server SSH private key.
     3. In the **Kind** drop-down, fill in the other fields as required.
  5. Click **Create**.

  6. In the Jenkins web interface, create a new Jenkins job.

  7. In the Jenkins job's configuration page, under the **Source Code Management** section, select **Git**.

  8. In the **Git** section, paste the Secure Source Manager repository SSH URL as the Repository URL, enter your build branches (e.g. `*/main`), and then select the saved private SSH key credential that you added previously in the **Manage Credentials** page.

  9. In the **Build Triggers** section, select **Generic Webhook Trigger**.

Optionally, you can add a token so that the job is only triggered if that token is supplied when invoking. To add a token, under the **Generic Webhook Trigger** section, you can input a token in the **Token** field.

  10. In the **Build** section, provide a build script you would like to have for this Jenkins job. For example, you can execute `cat README.md` to print the content of README.md.

  11. Click **Save** to create the Jenkins job.




## Set up a service account and grant required permissions

  1. If you don't already have a service account that you want to use, [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).

Ensure you have the `iam.serviceAccounts.actAs` permission on the service account. This permission is part of the Service Account User (`roles/iam.serviceAccountUser`) role.

  2. In the Secure Source Manager web interface, click the more_vert **more options** menu.

  3. Click **Service account SSH keys**. The **Service account SSH keys** page opens, and a list of any existing keys you've added is displayed.

  4. Click **Add key**.

  5. In the **Add SSH key** page, enter the following values for your key:

     1. **Service account** : the service account email for the service account you want to use the SSH key with in the format `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`

Where

        * `SA_NAME` is the service account name.
        * `PROJECT_ID` is the project ID of the project the service account was created in.
     2. **SSH Public Key** : Your Jenkins public SSH key.




### Grant the Secure Source Manager service agent permissions

If the service account is not in the same project as your Secure Source Manager instance you must also grant the Secure Source Manager [service agent](https://docs.cloud.google.com/iam/docs/service-agents) the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) role or `iam.serviceAccounts.signJwt` permission.

If your service account is in the same project as your Secure Source Manager instance, skip to Grant the service account a repository role.

  1. Run the following command to get the existing IAM policy for your service account:
         
         gcloud iam service-accounts get-iam-policy SERVICE_ACCOUNT \
             --format json
         

Where SERVICE_ACCOUNT is the service account you want to use. The account should be formatted either as a numeric service account ID or as an email, like this: `123456789876543212345` or `my-iam-account@somedomain.com`.

The output includes any existing bindings, or, if none exist, the `etag` value similar to the following:
         
         {
         "etag": "BwUjHYKJUiQ="
         }
         

**Important:** keep the `etag` value from the `get-iam-policy` response to ensure that you don't overwrite someone else's policy changes. If you want to overwrite all other changes, you can remove the `etag` value.
  2. Copy the output into a new file named `policy.json`.

  3. To grant the Secure Source Manager service agent the Service Account Token Creator (`roles/iam.ServiceAccountTokenCreator`) role, modify the `policy.json` to add the following:
         
         {
             "role": "roles/iam.serviceAccountTokenCreator",
             "members": [
                 "serviceAccount:service-INSTANCE_PROJECT_NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com"
             ]
         }
         

Where `INSTANCE_PROJECT_NUMBER` is the project number of your Secure Source Manager instance.

  4. Run the following command to replace the existing IAM policy for the service account:
         
         gcloud iam service-accounts set-iam-policy SERVICE_ACCOUNT POLICY_FILE
         

Replace the following:

     * SERVICE_ACCOUNT with the service account ID or email.
     * POLICY_FILE with the location and name of the JSON formatted file including the new policy.



### Grant the service account a repository role

  1. In the Secure Source Manager web interface, navigate to the repository you want to give the service account permissions in.
  2. Click the **Permissions** tab.
  3. Click **Add Users**.
  4. In the **Add principal** field, enter the service account email address.
  5. In the **Role** drop-down menu, select **Secure Source Manager Repository Reader**.
  6. Assign the service account the `securesourcemanager.instanceAccessor` role by running the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:SA_EMAIL \
             --role=roles/securesourcemanager.instanceAccessor
         

Replace the following:

     * `PROJECT_ID` with the Secure Source Manager instance project ID.
     * `SA_EMAIL` with the service account email.



## Set up a webhook

  1. In the Secure Source Manager web interface, navigate to the repository you want to create a webhook for.
  2. Click **Settings**.
  3. Click **Webhooks** , and then click **Add webhook**.
  4. In the **Hook ID** field, enter an ID for the webhook.

**Note:** Hook IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lower case letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the webhook.
  5. In the **Target URL** field, enter the Jenkins Trigger URL.

  6. If you used the optional token when configuring your Jenkins trigger, then the Jenkins trigger URL will contain that token at the end. To prevent leaking the token, remove it from the end of the target URL and copy to the **Sensitive Query String** field.

To locate your token in your trigger URL, look for the text starting with `token=`

For example, if your URL resembles the following: `https://jenkins-server.com/generic-webhook-trigger/invoke?token=jenkins-job1`

Copy and remove the portion starting with the question mark `?token=jenkins-job1` portion from the **Target URL** field. Then remove the initial question mark, move the remaining portion `token=jenkins-job1` to the **Sensitive Query String** field.

  7. In the **Trigger on** section, select one of the following:

     * **Push** : to trigger on a push to the repository.
     * **Pull request state changed** : to trigger on a change in the pull request state.
  8. If you selected **Push** , then you can enter an allowlist for push events in the **Branch filter** field.

The **Branch filter** field uses the glob pattern and only operations on the matched branches will cause a build trigger. If the field is empty or `*`, then push events for all branches are reported.

  9. Click **Add webhook**.

  10. The webhook is displayed in the **Webhooks** page.

**Note:** When you add or edit a webhook, the length of the `Sensitive Query String` might be inconsistent with the entered one, which is expected as placeholder strings are used to ensure security.



#### Test your webhook

  1. In the Secure Source Manager **Webhooks** page, click the webhook you want to test.
  2. Go to the bottom of the page and click **Test delivery**.

A fake event is added to the delivery queue. It might take a few seconds before it shows up in the delivery history.

  3. You can also use a `git` command to push or merge a pull request to test the webhook.

  4. In the Jenkins project, view the build triggered by the test event in **Build History**.

  5. You can also view the **Request** and **Response** to the test delivery in the **Recent deliveries** section of the Secure Source Manager webhook page after you send your first test delivery.




## What's next

  * Explore the [Jenkins documentation](https://www.jenkins.io/doc/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
