---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode/
title: Enable permissive mode on a backup plan \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:45.924059+00:00
---

# Enable permissive mode on a backup plan  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Enable permissive mode on a backup plan Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page explains how to enable permissive mode on a backup plan.

During backup execution, if Backup for GKE detects conditions that are likely to cause restore to fail, the backup itself fails. The reason for the failure is provided in the backup's [state_reason](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#Backup.FIELDS.state_reason) field. In the Google Cloud console, this field is termed as **Status reason**.

**Note:** You can [set up alerts](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts) to receive notifications if backups fail.

## About permissive mode

When backup failures aren't acceptable and it's not possible to address the underlying issues, you can enable _permissive mode_. Permissive mode ensures that backups complete successfully, even if GKE resources that could potentially cause restore failures are detected during the backup process. Details about the issues are provided in the backup's **Status reason** field.

We recommend using this option only if you understand the issues and can implement workarounds during the restoration process. For a list of potential error messages in the backup's **Status reason** field with recommended actions, see [Troubleshoot backup failures](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode#troubleshoot_backup_failures).

## Enable permissive mode

Use the following instructions to enable permissive mode:

### gcloud

To enable permissive mode, run the `gcloud beta container backup-restore backup-plans update` command:
    
    
    gcloud beta container backup-restore backup-plans update BACKUP_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION
        --permissive-mode
    

Replace the following:

  * `BACKUP_PLAN`: the name of the backup plan that you want to update.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the resource, for example `us-central1`. See [About resource locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).

For a full list of options, refer to the [gcloud beta container backup-restore backup-plans update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/update) documentation.




### Console

Use the following instructions to enable permissive mode in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[ Go to Google Kubernetes Engine ](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click the **Details** tab to edit the plan details.

  6. Click **Edit** to edit the section with **Backup mode**.

  7. Click the **Permissive mode** checkbox and click **Save changes**.




### Terraform

Update the existing `google_gke_backup_backup_plan` resource.
    
    
    resource "google_gke_backup_backup_plan" "NAME" {
       ...
       backup_config {
         permissive_mode = true
         ...
       }
    }
    

Replace the following:

  * `NAME`: the name of the `google_gke_backup_backup_plan` that you want to update.



For more information, see [gke_backup_backup_plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_backup_plan).

## Troubleshoot backup failures

The following table provides explanations and recommended actions for various backup failure messages displayed in the backup's **Status reason** field.

**Backup failure message** | **Message description and failure reason** | **Recommended action**  
---|---|---  
`Secret ... is an auto-generated token from ServiceAccount ... referenced in Pod specs` |  **Description** : In Kubernetes v1.23 and earlier, service accounts automatically generate a token backed by a secret. However, in later versions, Kubernetes removed this auto-generated token feature. A Pod in the cluster might have mounted the secret volume to its containers' file system.  
  
**Reason** : If Backup for GKE attempts to restore a service account along with its auto-generated secret and a Pod that mounts the secret volume, the restore appears to be successful. However, Kubernetes removes the secret, which causes the Pod to get stuck in container creation and fail to start.  |  Define the `spec.serviceAccountName` field in the Pod. This action ensures that the token is automatically mounted on `/var/run/secrets/kubernetes.io/serviceaccount` in the containers. For more information, refer to [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) documentation.  
  
When permissive mode is enabled, the secret is backed up but can't be mounted in Pods in Kubernetes v1.24+ clusters.   
  
### Common Custom Resource Definitions (CRDs) with issues and recommended actions

Here are some common CRDs that have backup issues and the actions we recommend to address the issues:

  * `capacityrequests.internal.autoscaling.k8s.io`: This CRD was used temporarily in v1.21 clusters. Run `kubectl delete crd capacityrequests.internal.autoscaling.k8s.io` to remove the CRD.
  * `scalingpolicies.scalingpolicy.kope.io`: This CRD was used to control fluentd resources, but GKE has migrated to using fluentbit. Run `kubectl delete crd scalingpolicies.scalingpolicy.kope.io` to remove the CRD.
  * `memberships.hub.gke.io`: Run `kubectl delete crd memberships.hub.gke.io` to remove the CRD if there are no membership resources. Enable permissive mode if there are membership resources.
  * `applications.app.k8s.io`: Enable permissive mode with an understanding of restore behavior.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
