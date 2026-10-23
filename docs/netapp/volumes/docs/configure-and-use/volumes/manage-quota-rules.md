---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules/
title: Manage quota rules \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:08.121149+00:00
---

# Manage quota rules  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage quota rules Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to manage your quota rules.

Quota rules enable you to limit the storage space within a volume for specific users and groups. For more information, see [Volume user and group quotas](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#volume-user-group-quotas).

For more information about managing quotas in ONTAP-mode, see [Use quotas to restrict or track resource usage](https://docs.netapp.com/us-en/ontap/volumes/quota-rules-policies-enforced-quotas-concept.html). For more information about how to submit ONTAP commands to the storage pool, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview).

For more information about instructions to manage your quota rules, see the following:

  * [Create a quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#create_a_quota_rule)

  * [Edit a quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#edit_a_quota_rule)

  * [Delete a quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#delete_a_quota_rule)




## Create a quota rule

The following sections provide instructions for how to [Create an individual user or group quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#create_an_individual_user_or_group_quota_rule), [Create a default user quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#create_a_default_user_quota_rule), and [Create a default group quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#create_a_default_group_quota_rule).

### Create an individual user or group quota rule

Use the following instructions to create an individual user or group quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to add a quota rule to.

  4. Click the **Quota rules** tab.

  5. Click **Create quota rule**.

  6. The **Create a quota rule** page appears. Under **Quota rule details** , complete the following steps:

     1. Enter a name for the quota rule in the **Name** field. The name must be unique for each volume.

     2. Optional: enter a description for the quota rule in the **Description** field.

  7. Select the quota rule type.

     * **Individual user quota**

     * **Individual group quota**

  8. Specify the target UID, or SID, or GID for the user or group in the **Target** field.

  9. Enter the usage limit for users or groups in MiB in the **Limit** field.

  10. Optional: under the **Labels** section, click **Add label** to enter relevant labels for your quota rule.

  11. Click **Create**.

The **Quota rules** tab displays your new quota rule.




### gcloud

Create an individual user or group quota rule:
    
    
      gcloud netapp volumes quota-rules create RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --type=RULE_TYPE \
       --target=TARGET_ID \
       --disk-limit-mib=LIMIT

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.

  * `RULE_TYPE`: the quota rule type: INDIVIDUAL_USER_QUOTA or INDIVIDUAL_GROUP_QUOTA.

  * `TARGET_ID`: the UID, or SID, or GID number.

  * `LIMIT`: the usage limit for users or groups in MiB.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

### Create a default user quota rule

Use the following instructions to create a default user quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to add a quota rule to.

  4. Click the **Quota rules** tab.

  5. In the **Default user quota** pane, click **Create quota rule**.

  6. The **Create a default user quota rule** page appears. Under **Quota rule details** , complete the following steps:

     1. Enter a name for the quota rule in the **Name** field. The name must be unique for each volume.

     2. Optional: enter a description for the quota rule in the **Description** field.

  7. Enter the usage limit for users in MiB in the **Limit** field.

  8. Optional: under the **Labels** section, click **Add label** to enter relevant labels for your quota rule.

  9. Click **Create**.

The **Default user quota** pane displays your new quota rule.




### gcloud

Create a default user quota rule:
    
    
      gcloud netapp volumes quota-rules create RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --type=RULE_TYPE \
       --disk-limit-mib=LIMIT

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.

  * `RULE_TYPE`: the quota rule type: DEFAULT_USER_QUOTA.

  * `LIMIT`: the usage limit for users in MiB.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

### Create a default group quota rule

Use the following instructions to create a default group quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to add a quota rule to.

  4. Click the **Quota rules** tab.

  5. In the **Default group quota** pane, click **Create quota rule**.

  6. The **Create a default group quota rule** page appears. Under **Quota rule details** , complete the following steps:

     1. Enter a name for the quota rule in the **Name** field. The name must be unique for each volume.

     2. Optional: enter a description for the quota rule in the **Description** field.

  7. Enter the usage limit for groups in MiB in the **Limit** field.

  8. Optional: under the **Labels** section, click **Add label** to enter relevant labels for your quota rule.

  9. Click **Create**.

The **Default group quota** pane displays your new quota rule.




### gcloud

Create a default group quota rule:
    
    
      gcloud netapp volumes quota-rules create RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --type=RULE_TYPE \
       --disk-limit-mib=LIMIT

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.

  * `RULE_TYPE`: the quota rule type: DEFAULT_GROUP_QUOTA.

  * `LIMIT`: the usage limit for users in MiB.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

## Edit a quota rule

The following sections provide instructions for how to [Edit an individual user or group quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#edit_an_individual_user_or_group_quota_rule) and [Edit a default user or group quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#edit_a_default_user_or_group_quota_rule).

### Edit an individual user or group quota rule

Use the following instructions to edit an individual user or group quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to edit a quota rule for.

  4. Click the **Quota rules** tab.

  5. From the list of quota rules, select the quota rule you want to edit.

  6. Click more_vert **Show more** icon on the quota rule and click **Edit**.

  7. Make the required changes to the quota rule.

  8. Click **Save**.




### gcloud

Update an individual user or group quota rule:
    
    
      gcloud netapp volumes quota-rules update RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --disk-limit-mib=LIMIT

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.

  * `LIMIT`: the usage limit for users or groups in MiB.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

### Edit a default user or group quota rule

Use the following instructions to edit a default user or group quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to edit a quota rule for.

  4. Click the **Quota rules** tab.

  5. Click more_vert **Show more** icon next to the **Default user quota** or the **Default group quota** pane and click **Edit**.

  6. Make the required changes to the quota rule.

  7. Click **Save**.




### gcloud

Update a default user or group quota rule:
    
    
      gcloud netapp volumes quota-rules update RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --disk-limit-mib=LIMIT

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.

  * `LIMIT`: the usage limit for users or groups in MiB.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

## Delete a quota rule

The following sections provide instructions for how to [Delete an individual user or group quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#delete_an_individual_user_or_group_quota_rule) and [Delete a default user or group quota rule](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules#delete_a_default_user_or_group_quota_rule).

### Delete an individual user or group quota rule

Use the following instructions to delete an individual user or group quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to delete a quota rule from.

  4. Click the **Quota rules** tab.

  5. From the list of quota rules, select the quota rule you want to delete.

  6. Click more_vert **Show more** icon on the quota rule and click **Delete**.

  7. A confirmation dialog appears. Read through the warnings.

  8. Enter the name of the quota rule in the **Quota rule name** field.

  9. Click **Delete quota rule**.




### gcloud

Delete an individual user or group quota rule:
    
    
      gcloud netapp volumes quota-rules delete RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

### Delete a default user or group quota rule

Use the following instructions to delete a default user or group quota rule using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to delete a quota rule from.

  4. Click the **Quota rules** tab.

  5. From the list of quota rules, select the quota rule you want to delete.

  6. Click more_vert **Show more** icon next to the **Default user quota** or the **Default group quota** pane and click **Delete**.

  7. A confirmation dialog appears. Read through the warnings.

  8. Enter the name of the quota rule in the **Quota rule name** field.

  9. Click **Delete quota rule**.




### gcloud

Delete a default user or group quota rule:
    
    
      gcloud netapp volumes quota-rules delete RULE_NAME \
       --volume=VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION

Replace the following information:

  * `RULE_NAME`: the name of the rule.

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.




For more information about additional optional flags, see see [Google Cloud SDK documentation on quota-rules](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules).

## What's next

[Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
