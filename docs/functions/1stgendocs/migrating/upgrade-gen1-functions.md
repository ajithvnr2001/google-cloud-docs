---
url: https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions/
title: Upgrade 1st gen functions to Cloud Run functions \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:27.507517+00:00
---

# Upgrade 1st gen functions to Cloud Run functions  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade 1st gen functions to Cloud Run functions

This guide describes how to upgrade your 1st gen HTTP and Pub/Sub functions to Cloud Run functions. By following the steps in this guide, your 1st gen function will be upgraded to a Cloud Run function running exclusively as a Cloud Run service, managed through the Cloud Run API. You can optionally use the `skip-detach` flag to upgrade your 1st gen function to a Cloud Run function that can be managed with either the Cloud Run Admin API or the Cloud Functions v2 API.

## Limitations

  * The upgrade tool only supports upgrading 1st gen HTTP and Pub/Sub-triggered functions (`google.pubsub.topic.publish`) in an `ACTIVE` state (meaning that the function is successfully deployed and waiting for traffic).
  * You cannot upgrade functions that are in a project that has a domain-scoped ID (that is, an ID that contains a colon :).
  * If your function is running on a decommissioned runtime, you must redeploy it on a [supported runtime](https://docs.cloud.google.com/functions/docs/runtime-support#support_schedule) before you can upgrade it.
  * The name of the function you want to upgrade must not collide with an existing Cloud Run service name in the project.



## Overview of the upgrade process

Here is a high level overview of the upgrade process:

![Overview of upgrading a 1st gen function to Cloud Run.](https://docs.cloud.google.com/static/functions/img/gen1-migration-process.svg)**Figure 1.** An overview of the steps by which a 1st gen function is upgraded to Cloud Run.

The details of this process are described in the following sections.

### Start Upgrade overview

  * When you start the upgrade (using either the Google Cloud CLI or the Google Cloud console), the upgrade tool creates a temporary 2nd gen function that is a copy of your original 1st gen function. Once you start the migration process, don't delete the function source code from Cloud Storage or the function container from Artifact Registry. This 2nd gen function: 
    * Acts as a bridge between the original 1st gen function and the final fully upgraded function.
    * Has the same name, code, and configuration as the original 1st gen function. 
      * If upgrading an HTTP function, has the same `cloudfunctions.net` URL as the original 1st gen function, and also has a `run.app` Cloud Run URL. 
        * After starting the upgrade, both your 1st gen function and your 2nd gen function copy are assigned to the same `cloudfunctions.net` URL. When sending requests to the `cloudfunctions.net` URL, traffic continues to be routed to the 1st gen function. The 2nd gen function copy also has a Cloud Run `run.app` URL. The 2nd gen function URLs won't receive traffic until you redirect traffic in the next step.
      * If upgrading a Pub/Sub function, uses the same Pub/Sub topic as the 1st gen function, but doesn't have a subscription yet.
    * Note that if you didn't pin your dependencies to a specific version, the newly created 2nd gen function copy may use a newer dependency version.
  * The 1st gen function continues to be listed in the 1st gen [Google Cloud console](https://console.cloud.google.com/functions/list), and its temporary 2nd gen copy appears for the first time in the [Cloud Run console](https://console.cloud.google.com/run).



Example: This table shows the state of HTTP functions during the initial upgrade step.

Functions | Serving Traffic? | Visible in Console?  
---|---|---  
Original 1st gen function | Yes, from `cloudfunctions.net` URL | Yes, 1st gen console.  
New 2nd gen copy | No. This function has both `cloudfunctions.net` and `run.app` URLs, but they won't serve traffic until the redirection step. | Yes, Cloud Run console.  
  
### Redirect traffic overview

  * When you redirect traffic, the result depends on whether the function you're upgrading is an HTTP function or a Pub/Sub function: 
    * If you are upgrading an HTTP function, traffic directed at the `cloudfunctions.net` URL goes to the 2nd gen function. Your 1st gen function continues to exist, but it doesn't receive any traffic.
    * If you are upgrading a Pub/Sub function, the 2nd gen function trigger uses the same Pub/Sub topic, but creates a new subscription that sends a message to the Cloud Run function. The old subscription is deleted.
  * The 1st gen function disappears from the 1st gen console.
  * If you run the `gcloud functions describe` command, you can see that the function's environment is now 2nd gen.
  * Note that there are risks during this transition phase, especially for Pub/Sub functions: 
    * **Duplicate messages** : A new subscription is created before the old subscription is deleted. The same Pub/Sub message may be sent to both your old function and the new function during this transition time.
    * **Losing messages** : If you are upgrading a Pub/Sub function and the new function fails to handle messages after traffic is redirected, you risk losing Pub/Sub messages. This is especially true if the function has retry disabled; see Upgrade Pub/Sub for details.



Example: This table shows the state of HTTP functions during the traffic redirection step.

Functions | Serving Traffic? | Visible in Console?  
---|---|---  
Original 1st gen function | No. | No longer visible in 1st gen console, but still exists.  
New 2nd gen copy | Yes, from `cloudfunctions.net` URL as well as from `run.app` Cloud Run URL. | Yes, Cloud Run console.  
  
### Rollback traffic overview

  * When you roll back traffic, the upgrade tool rolls back all traffic from the 2nd gen function copy to the original 1st gen function, which is now serving all traffic. The 2nd gen function is still available for testing.
  * If you are rolling back a Pub/Sub function, the 1st gen function subscription is created again, and the 2nd gen function subscription is deleted.
  * If you want to proceed with the upgrade after rolling back traffic, you must first redirect traffic again to the new 2nd gen function to continue.



Example: This table shows the state of HTTP functions if you roll back traffic.

Functions | Serving Traffic? | Visible in Console?  
---|---|---  
Original 1st gen function | Yes. | Yes, 1st gen console.  
New 2nd gen copy | No. | No longer visible in Cloud Run console, but still exists.  
  
### Abort overview

You can abort the upgrade any time before you commit. Once you commit, the upgrade becomes irreversible.

Example: This table shows the state of HTTP functions if you abort the upgrade.

Functions | Serving Traffic? | Visible in Console?  
---|---|---  
Original 1st gen function | Yes. | Yes, 1st gen console.  
2nd gen copy | No. | No longer visible in Cloud Run console, no longer exists.  
  
### Commit overview (irreversible)

  * Committing the upgrade completes the upgrade process for the 1st gen function. This action is irreversible.
  * The temporary 2nd gen function is converted into a full-fledged Cloud Run function using the Cloud Run Admin API. 
    * This is the equivalent of running the [`detach` command](https://docs.cloud.google.com/functions/docs/managing#detach) on a 2nd gen function. The `detach` command detaches a Cloud Functions v2 function from its existing API environment.
    * Going forward, you can only interact with the upgraded function using the Cloud Run Admin API and Cloud Run tools.
  * The 1st gen function is deleted, and all traffic is served to the upgraded Cloud Run function.



Example: This table shows the state of HTTP functions after you commit the upgrade:

Functions | Serving Traffic? | Visible in Console?  
---|---|---  
New Cloud Run function based on Cloud Run Admin API. | Yes, from `cloudfunctions.net` URL as well as from `run.app` Cloud Run URL. | Yes, Cloud Run console.  
Original 1st gen function | No. | No, no longer exists.  
2nd gen copy | No. | No, no longer exists.  
**Note:** As described in Skip detach, you can optionally use the `skip-detach` flag to delete the 1st gen function, but without detaching the resulting 2nd gen function. The result is a fully functional 2nd gen function.

### Pre-commit tasks

You can use the following features to modify the outcome of the migration process:

  * **Override parameters:** Update function and redeploy before committing.
  * **Skip detach:** Use the `skip-detach` flag to skip the detach step and leave the function as a 2nd gen function.



#### Override parameters

Prior to committing your upgrade, make sure that you are using the latest version of your chosen [runtime](https://docs.cloud.google.com/functions/docs/runtime-support#support_schedule), and update your `max-instances` setting if your current setting is not suitable for Cloud Run.

For example:
    
    
    gcloud functions upgrade FUNCTION \
      --region=REGION \
      --setup-config \
      --runtime=RUNTIME \
      --max-instances=MAX_INSTANCES
    

Replace the following:

  * FUNCTION: the name of your function.
  * REGION: your region.
  * RUNTIME: your runtime.
  * MAX_INSTANCES: the maximum number of instances for your new Cloud Run function.



#### Skip detach

By default, the commit operation "detaches" the function and converts it into a full-fledged Cloud Run function based on the Cloud Run Admin API. However, you can alternatively use the `skip-detach` flag to delete the 1st gen function, but without detaching the resulting 2nd gen function. The result is a fully functional 2nd gen function that can be managed with the Cloud Functions v2 API as well as the Cloud Run Admin API.

To skip detach, use this command:
    
    
    gcloud functions upgrade FUNCTION_NAME --commit --skip-detach
    

## Testing tips

Testing is an essential part of the upgrade process.

We recommend that you become familiar with the upgrade tool by testing it on non-production functions. Once you have mastered the process and are seeing consistent success, you can start upgrading production functions.

Here are some of the tools and techniques you can use to test your functions during an upgrade:

  * Whenever your functions change state, use the Google Cloud CLI `describe` commands to verify that the function exists, and that its environment and version are as expected. Depending on the current state of the function being upgraded, use one of the following

    * Cloud Run:
          
          gcloud run services describe FUNCTION_NAME --format yaml
          

    * Cloud Functions:
          
          gcloud functions describe --region REGION_NAME FUNCTION_NAME
          

  * Use the Logging page in the 1st gen and Cloud Run consoles to see the details of function traffic.

  * Use the Cloud Run console to view and test the 2nd gen function copy as it progresses through the upgrade process:

    * Use the **Triggers** tab to test the 2nd gen function copy after starting the upgrade.
    * Use the **YAML** tab to view details about the function, including its Cloud Run `run.app` URL.



## Before you begin

Before you begin the upgrade, ensure you meet these prerequisites:

  * You have enabled the Cloud Run API:
        
        gcloud services enable run.googleapis.com

  * You have an existing 1st gen HTTP or Pub/Sub function.

  * Your 1st gen function is using a [supported runtime version](https://docs.cloud.google.com/functions/docs/runtime-support#support_schedule). If not, [redeploy your function](https://docs.cloud.google.com/functions/1stgendocs/deploy) with a supported version of your chosen runtime.

  * Your 1st gen function's [`max-instances` setting](https://docs.cloud.google.com/functions/1stgendocs/configuring/max-instances) doesn't exceed your quota on [Cloud Run](https://docs.cloud.google.com/run/docs/configuring/max-instances-limits).

  * You have the required IAM roles:

    * You must have `roles/iam.serviceAccountUser` set on the function's service account.
    * You must have the `roles/cloudfunctions.admin` role or an equivalent role on the project to perform the upgrade.
    * For a Pub/Sub function with a `no-retry` setting, you have the `roles/serviceusage.consumer` role or a custom role with the

and `pubsub.topic.setIAMPermissions` role.

    * To commit a Pub/Sub function upgrade, you must have the role [`roles/pubsub.admin`](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin). The role `roles/pubsub.admin` is a project-level role that grants administrative access to all Pub/Sub resources within a project.

You can view your function's IAM policies as follows:
    
    gcloud functions get-iam-policy FUNCTION_NAME

  * You have `roles/cloudfunctions.admin` granted on the function's service account. To grant the `roles/cloudfunctions.admin` role, use the `gcloud functions add-iam-policy-binding` command, for example:
        
        gcloud functions add-iam-policy-binding FUNCTION_NAME \
           --region=REGION \
           --member=serviceAccount:SERVICE_ACCOUNT \
           --role="roles/cloudfunctions.admin"
        

If you get errors when you try to run this command, make sure that your function adheres to your organization's policies. For example, your organization may not allow unauthenticated HTTP functions.




To learn more about members and roles, see [Add principals and granting roles](https://docs.cloud.google.com/securing/managing-access-iam#adding_principals_and_granting_roles).

## Upgrade HTTP functions

This section describes how to upgrade a 1st gen HTTP function to a Cloud Run function. To learn how to upgrade a 1st gen Pub/Sub function, see the later section.

After you have redirected traffic and committed the upgrade as described in the following sections, the `cloudfunctions.net` URL associated with the original 1st gen HTTP function will continue to work and will route traffic to the new Cloud Run function.

### Start HTTP function upgrade

This step creates a 2nd gen copy of your 1st gen function.

###  Console 

  1. In the Google Cloud console, go to the Functions (1st gen) page:

[Go to Functions (1st gen)](https://console.cloud.google.com/functions/list)

  2. Find the 1st gen function you want to upgrade, and confirm that its status in the **Upgrade status** column is **Ready to upgrade**.

  3. Click the function name to display its details page.

  4. On the function details page, click **Upgrade** under **Upgrade eligible**.

  5. Follow the prompts to start the upgrade process.




After you complete this step, the **Upgrade in progress** panel appears, prompting you to click the **Go to Cloud Run** link to continue the upgrade process.

###  gcloud 

Run the `gcloud functions upgrade` command with the `--setup-config` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --setup-config
    

Replace FUNCTION_NAME with the name of your 1st gen function.

After starting the upgrade:

  * The 1st gen function continues to serve traffic to its original URL. You can view this URL by going to the function's detail page in the [Functions (1st gen) console](https://console.cloud.google.com/functions/list) and opening the **Trigger** tab.
  * A temporary 2nd gen function that is a copy of the 1st gen function is created. It has the same `cloudfunctions.net` URL as the 1st gen function, as well as a new Cloud Run `run.app` URL. You can view both of these URLs by going to the function's detail page in the [Cloud Run console](https://console.cloud.google.com/run) and opening the YAML tab. Alternatively, you can use this command:
        
        gcloud run services describe YOUR_SERVICE_NAME \
            --region YOUR_REGION \
            --format="value(status.url)"

  * You can verify that the 2nd gen copy of your 1st gen function exists:
        
        gcloud run services describe FUNCTION_NAME --format yaml
        

  * You can verify the 1st gen function environment, where the output should show the function environment as `1st gen`:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        




#### Troubleshoot start upgrade step

The upgrade fails under these conditions:

  * A function with the same name already exists in the same region and project.
  * The 1st gen function uses a [decommissioned runtime](https://docs.cloud.google.com/functions/docs/runtime-support), so it is not eligible for upgrade until you redeploy it with a supported runtime.
  * The caller lacks the [`cloudfunctions.functions.generationUpgrade`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.functions.generationUpgrade) permission. Note that the caller needs the `roles/cloudfunctions.admin` role or an equivalent role on the project.



### Redirect traffic for HTTP function

At this point, you should test the URL for both the original function and its copy. Make sure they work as expected before proceeding. If you encounter problems, abort the upgrade to return to a clean state, where you can address any underlying issues in the 1st gen function.

The redirect step redirects traffic from the 1st gen Cloud Functions URL to the 2nd gen function copy.

###  Console 

  1. From the **Upgrade in progress** panel in the Cloud Run functions details page, click **Go to Cloud Run**.
  2. Click **Test function** to test your function (optional, but highly recommended).
  3. When you are ready, click **Redirect traffic**.



###  gcloud 

Run the `gcloud functions upgrade` command with the `--redirect-traffic` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --redirect-traffic
    

After redirecting traffic, the 2nd gen function copy serves traffic to both the functions URL (`cloudfunctions.net`) and the Cloud Run URL (`run.app`).

#### Test your HTTP function after redirection

  * Verify the function environment:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        

The output shows the environment as `2nd gen`.

  * Use the console logging tool to compare your 2nd gen function copy with the original 1st gen function.




#### Troubleshoot redirection

The redirection fails under these conditions:

  * You did not run the previous step (`--setup-config`).



### Roll back traffic for HTTP function

If you are not ready to commit your upgrade, you can roll traffic back to the 1st gen function.

###  Console 

From the **Upgrade in progress** panel in the Cloud Run functions details page in the [Cloud Run console](https://console.cloud.google.com/run), click **Rollback traffic**.

###  gcloud 

Run the `gcloud functions upgrade` command with the `--rollback-traffic` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --rollback-traffic
    

After rolling back traffic:

  * The 1st gen function serves traffic to the `cloudfunctions.net` URL.
  * The 2nd gen function copy remains available and you can trigger it using its `run.app` URL.



You can verify the function environment as follows. The output should show the function environment as `1st gen`:
    
    
    gcloud functions describe --region REGION_NAME FUNCTION_NAME
    

The rollback fails if you have not redirected traffic to the 2nd gen function.

### Commit the upgrade for HTTP function

This step finalizes the upgrade, after which you can no longer abort the process. Before performing this step, make sure that you have thoroughly tested your functions.

###  Console 

From the **Upgrade in progress** panel in the Cloud Run functions details page in the [Cloud Run console](https://console.cloud.google.com/run), click **Commit upgrade**.

###  gcloud 

Run the `gcloud functions upgrade` command with the `--commit` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --commit
    

After committing the upgrade:

  * The 1st gen function is deleted, and the 2nd gen function copy is [detached](https://docs.cloud.google.com/functions/docs/managing#detach) to become a full-fledged Cloud Run function.
  * The Cloud Run function retains the `cloudfunctions.net` URL along with the new `run.app` URL.
  * You can verify that the 1st gen function no longer exists:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        

  * You can verify the Cloud Run service details: 
        
        gcloud run services describe FUNCTION_NAME --format yaml
        




The output shows a new generation created and the `Goog-managed-by` label has an empty value.

The commit fails when traffic has not been redirected to the Cloud Run function.

Note that if an upgrade commit fails in a rollback-safe state (`COMMIT_FUNCTION_UPGRADE_ERROR_ROLLBACK_SAFE`), you can recover by retrying `--commit`, rolling back traffic (`--rollback-traffic`), or aborting (`--abort`).

## Upgrade Pub/Sub functions

This section describes how to upgrade a 1st gen Pub/Sub function to a Cloud Run function.

The process of upgrading a 1st gen Pub/Sub function follows the same basic pattern as upgrading an HTTP function, but there are a few additional considerations:

  * Disabling retry on failure is not a supported feature on Cloud Run, but it is the default setting on 1st gen. So you may have functions of both types. What the upgrade tool does depends on this setting:

    * If your 1st gen function has retry disabled (the default 1st gen setting), the upgrade tool creates an Eventarc Pub/Sub trigger along with a [dead letter queue](https://docs.cloud.google.com/pubsub/docs/handling-failures#how_dead_letter_topics_work) (DLQ). The upgrade tool sets Identity and Access Management (IAM) policy for subscriptions and their topics. When the upgrade is complete, the dead letter queue topic stores the undelivered messages, which you can retrieve by creating a new subscription to the dead letter queue. If you want to use a customer-managed encryption key (CMEK) for the DLQ topic, you can [update CMEK for the topic](https://docs.cloud.google.com/pubsub/docs/encryption#update_cmek_for_a_topic) after the migration.
    * If your 1st gen function has retry enabled, the upgrade tool creates an Eventarc Pub/Sub trigger with default settings.



### Start the upgrade for Pub/Sub function

This step creates a 2nd gen copy of your 1st gen function.

###  Console 

  1. In the Google Cloud console, go to the Cloud Functions (1st gen) page:

[Go to Functions (1st gen)](https://console.cloud.google.com/functions/list)

  2. Find the 1st gen function you want to upgrade, and confirm that its status in the **Upgrade status** column is **Ready to upgrade**.

  3. Click the function name to display its details page.

  4. On the function details page, click **Upgrade** under **Upgrade eligible**.




When this phase completes, the **Upgrade in progress** panel appears, prompting you to click the link **Go to Cloud Run** to continue the upgrade process.

###  gcloud 

Run the `gcloud functions upgrade` command with the `--setup-config` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --setup-config
    

Replace FUNCTION_NAME with the name of your 1st gen function.

Optionally, specify a service account for the trigger:
    
    
    gcloud functions upgrade FUNCTION_NAME --setup-config --trigger-service-account=CUSTOM_SA_EMAIL

Replace CUSTOM_SA_EMAIL with the email of your custom service account.

If the trigger service account (default Compute Engine service account or specified custom service account) lacks the `run.route.invoke` permission, the system prompts you to bind the `roles/run.invoker` role.

After starting the upgrade:

  * The 1st gen function continues to serve traffic to its original URL.
  * A 2nd gen copy of your 1st gen function is created. You can trigger it using its Cloud Run URL.
  * The 1st gen function continues to serve traffic to its `cloudfunctions.net` URL.



#### Test your Pub/Sub function after start upgrade step

  * You can verify that the 2nd gen copy of your 1st gen function exists:
        
        gcloud run services describe FUNCTION_NAME --format yaml
        

  * You can verify the 1st gen function environment, where the output should show the function environment as `1st gen`:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        

  * Publish a message to the destination topic to trigger the 1st gen function.

  * To test the new function, add a Pub/Sub trigger to it and confirm that the function responds to the trigger as expected:

    1. Select the function in the Cloud Run console and open the **Triggers** tab.
    2. Click **Add Trigger** and in the **Eventarc trigger** panel, select a topic to trigger the function. By default, the function is triggered when a message is published to the topic.
    3. In the **Upgrade in Progress** panel, click **Test function**.
    4. In the Cloud Code for Cloud Shell window that opens, publish a message to the topic you added in the **Triggers** tab.
    5. In the Cloud Run console, go to **Observability > Logs** to confirm that your function published the message. Alternatively, you can use the command line in Cloud Code for Cloud Shell to view logging output.

For example, suppose you have a basic Hello World function that publishes a greeting. After specifying the new trigger, you can test it in Cloud Code for Cloud Shell as follows:
    
    gcloud pubsub topics publish YOUR_TOPIC_NAME --message YOUR_NAME
    gcloud functions logs read --region YOUR_REGION --limit 50
    




#### Troubleshoot Pub/Sub start upgrade step

The upgrade fails under these conditions:

  * A Cloud Run function with the same name already exists in the same region and project.
  * You attempted to upgrade a 2nd gen function.
  * The 1st gen function is already undergoing the upgrade process.
  * The 1st gen function does not exist.
  * The 1st gen function is in an error state.
  * The 1st gen function is neither an HTTP nor a Pub/Sub function.
  * The caller lacks the [`cloudfunctions.functions.generationUpgrade`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.functions.generationUpgrade) permission. Note that the caller needs the `roles/cloudfunctions.admin` role or an equivalent role on the project.



### Redirect traffic for Pub/Sub function

This step redirects traffic from the 1st gen Cloud Functions URL to the 2nd gen function copy.

###  Console 

  1. From the **Upgrade in progress** panel in the Cloud Run functions details page, click **Go to Cloud Run**.
  2. Click **Test function** to test your function (optional, but highly recommended).
  3. When you are ready, click **Redirect traffic**.



###  gcloud 

Run the `gcloud functions upgrade` command with the `--redirect-traffic` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --redirect-traffic
    

After redirecting traffic, the 2nd gen function serves traffic to both the Cloud Functions URL and the Cloud Run URL.

#### Test Pub/Sub after redirecting traffic

  * You can verify the function environment:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        

The output shows the environment as `2nd gen`.

    * The `eventTrigger.retryPolicy` matches the retry policy specified during function creation.
    * The `eventTrigger.serviceAccountEmail` is either the default Compute Engine service account or the specified custom service account.
    * Publishing a message to the destination topic now triggers the 2nd gen function copy.



#### Troubleshoot Pub/Sub for redirection

The redirection fails under these conditions:

  * You did not run the previous step (`--setup-config`).
  * The Cloud Run function was manually deleted.



### Roll back traffic for Pub/Sub function

This step reverts traffic back to the 1st gen function.

###  Console 

From the **Upgrade in progress** panel in the Cloud Run functions details page, click **Rollback traffic**.

###  gcloud 

Run the `gcloud functions upgrade` command with the `--rollback-traffic` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --rollback-traffic
    

After rolling back traffic:

  * The function reverts to the state it was in immediately after the initial upgrade step.
  * The 1st gen function serves traffic to the `cloudfunctions.net` URL.
  * The 2nd gen copy remains available and you can trigger it using its Cloud Run URL.

  * You can verify the function environment:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        

The output should show the function environment as `1st gen`.

  * Publishing a message to the destination topic triggers the 1st generation function.




The rollback fails if you have not redirected traffic to the Cloud Run function.

### Commit the upgrade for Pub/Sub function

This step finalizes the upgrade, after which you can no longer abort the process. This step is not reversible. Before performing this step, make sure that you have thoroughly tested your functions.

###  Console 

From the **Upgrade in progress** panel in the Cloud Run functions details page, click **Commit upgrade**.

###  gcloud 

Run the `gcloud functions upgrade` command with the `--commit` flag:
    
    
    gcloud functions upgrade FUNCTION_NAME --commit
    

After committing the upgrade:

  * The 1st gen function is deleted.
  * The Cloud Run function retains the `cloudfunctions.net` URL.
  * You can verify that the function no longer appears in the list: 
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        

  * You can verify the Cloud Run service details: 
        
        gcloud run services describe FUNCTION_NAME --format yaml
        

    * The output shows that a new generation has been created. The `Goog-managed-by` label should have an empty value.
  * If you created the 1st gen function without checking **Retry on Failures** , the Pub/Sub subscription for the trigger has a [dead letter queue](https://docs.cloud.google.com/pubsub/docs/handling-failures#how_dead_letter_topics_work) (DLQ).
  * Publishing a message to the destination topic now triggers the Cloud Run function.



The commit fails under these conditions:

  * Traffic has not been redirected to the Cloud Run function.
  * The Cloud Run function was manually deleted.



Note that if an upgrade commit fails in a rollback-safe state (`COMMIT_FUNCTION_UPGRADE_ERROR_ROLLBACK_SAFE`), you can recover by retrying `--commit`, rolling back traffic (`--rollback-traffic`), or aborting (`--abort`).

## Abort the upgrade

**Note:** You can only use this feature for function upgrades you haven't committed yet. Once you commit a function upgrade, it is irreversible.

This action cancels the upgrade process. The new 2nd gen function copy is deleted, and the 1st gen function continues to serve traffic to the original `cloudfunctions.net` URL. You can perform this action at any time during the upgrade process before you commit the upgrade.

If you are using the Google Cloud console to perform the upgrade, the UI only lets you abort the process immediately after the initial upgrade operation. The **Abort** button is located in the upper left corner of the Functions (1st gen) console. If you are using the Google Cloud CLI, you can abort the upgrade any time before you commit the upgrade, after which the process becomes irreversible.

You can use the Google Cloud CLI to abort a function upgrade even if you used the Google Cloud console to perform the upgrade process:
    
    
    gcloud functions upgrade FUNCTION_NAME --abort
    

After aborting the upgrade:

  * The 2nd gen function copy is deleted.
  * The 1st gen function serves traffic to the `cloudfunctions.net` URL.
  * In the [Google Cloud console](https://console.cloud.google.com/functions/list), the function's upgrade status changes from **Configuration copied** back to **Ready to Upgrade**.
  * You can verify the Cloud Run service no longer appears in the list:
        
        gcloud run services list

  * You can verify the function environment:
        
        gcloud functions describe --region REGION_NAME FUNCTION_NAME
        




The output shows the function environment as `1st gen`.

The abort operation fails if you have already committed the upgrade.

## Check converted IAM policies

During the upgrade process, the tool performs a best-effort conversion of roles and permissions between 1st gen Cloud Functions and the new Cloud Run functions.

The upgrade process converts 1st gen Cloud Functions IAM roles to equivalent Cloud Run roles.

**Conversion rules:**

  * `roles/cloudfunctions.invoker` converts to `roles/run.invoker`.
  * `roles/cloudfunctions.developer` converts to `roles/run.sourceDeveloper`.
  * `roles/cloudfunctions.viewer` converts to `roles/run.sourceViewer`.
  * `roles/cloudfunctions.admin` converts to `roles/run.admin` and `roles/run.sourceDeveloper`.



The IAM policy upgrade fails if the caller lacks `projects.getIamPolicy` or `run.setIamPolicy` permissions. The caller needs the `roles/cloudfunctions.admin` role or an equivalent role on the project.

### Verify IAM policy upgrade

To verify that your IAM policies are being properly upgraded, check them at every stage of the upgrade process to confirm that they have the expected values:

  1. Start the upgrade process for your function:
         
         gcloud functions upgrade FUNCTION_NAME --setup-config
         

The output displays a warning message if custom role bindings are detected.

  2. Validate the IAM policies set on the 1st gen function are converted and upgraded to the Cloud Run function:
         
         gcloud functions get-iam-policy FUNCTION_NAME
         gcloud run services get-iam-policy FUNCTION_NAME
         

  3. Validate the Cloud Run functions invoker role binding at the project level is converted and upgraded to the Cloud Run function:
         
         gcloud projects get-iam-policy PROJECT_ID | grep "roles/cloudfunctions.invoker"
         gcloud run services get-iam-policy FUNCTION_NAME
         




## What's next

  * Learn more about [Cloud Run functions](https://docs.cloud.google.com/run/docs/functions/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
