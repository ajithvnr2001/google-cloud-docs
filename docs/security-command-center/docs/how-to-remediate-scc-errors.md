---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors/
title: Remediating Security Command Center errors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:23.793462+00:00
---

# Remediating Security Command Center errors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Remediating Security Command Center errors Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides a list of reference guides and techniques for remediating SCC errors.

## Before you begin

You need adequate Identity and Access Management (IAM) roles to view or edit findings, and to access or modify Google Cloud resources. If you encounter permission errors when accessing Security Command Center in the Google Cloud console, ask your administrator for assistance. To learn about roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). To resolve resource errors, read documentation for affected products.

## Review findings in the Google Cloud console

[SCC errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors) are configuration errors that prevent Security Command Center from working as expected. The `Security Command Center` source generates these findings.

As long as Security Command Center is [set up for your organization](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation) or [project](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview), it generates error findings as it detects them. You can view SCC errors in the Google Cloud console.

Use the following procedure to review findings in the Google Cloud console:

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Security Command Center**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



## Deactivation of SCC errors after remediation

After you remediate an `SCC error` finding, Security Command Center automatically sets the state of the finding to `INACTIVE` during the next scan. How long it takes for Security Command Center to set the state of a remediated finding to `INACTIVE` depends on when you fix the finding and the schedule of the scan that detects the error.

For information about the scan frequency for an `SCC error` finding, see the summary of the finding in [Error detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#error_detectors).

## Remediate SCC errors

This section includes remediation instructions for all SCC errors.

**Caution** : If done improperly, modifying the configuration of your resources can negatively affect your production environment. Also, enabling some suggested Google Cloud services can increase your cloud costs. Understand the impact of all remediation steps before making changes. 

### `API disabled`

**Category name in the API** : `API_DISABLED`

One of the following services is disabled for the project:

  * [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
  * [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)



The disabled service can't generate findings.

To remediate this finding, follow these steps:

  1. Review the finding to determine which API is disabled.
  2. Enable the API:

     * Enable the Container Threat Detection API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containerthreatdetection.googleapis.com)

     * Enable the Web Security Scanner API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=websecurityscanner.googleapis.com)




read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#api_disabled).

### `APS no resource value configs match any resources`

**Category name in the API** : `APS_NO_RESOURCE_VALUE_CONFIGS_MATCH_ANY_RESOURCES`

[Resource value configurations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-value-configurations) are defined for attack path simulations, but they don't match any resource instances in your environment. The simulations are using the default high-value resource set instead.

Resource value configurations might not match any resources for the following reasons, which are identified in the finding description in Google Cloud console:

  * None of the resource value configurations match any resource instances.
  * One or more resource value configurations that specify `NONE` override every other valid configuration.
  * All the defined resource value configurations specify a value of `NONE`.



To remediate this finding, follow these steps:

  1. Go to the **Attack path simulation** page in Security Command Center **Settings** :

[Go to Settings](https://console.cloud.google.com/security/command-center/config/attack-path-simulation)

  2. Select your organization. The **Attack path simulation** page opens with the existing configurations displayed.

  3. In the **Resource value** column of the **Resource value configurations** list, check for values of `None`.

  4. For any configuration that specified `None`, do the following:

     1. Click the name of any resource value configuration to display the configuration specifications.
     2. If necessary, [edit the resource attribute specifications](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#edit_a_configuration) to reduce the number of resource instances that match the configuration.
  5. If the problem is not caused by an overly broad `None` specification, do the following:

     1. Click the names of each configuration that specifies a value of `HIGH`, `MEDIUM`, or `LOW` to display the resource attribute specifications.
     2. Review and, necessary, edit the configuration to correct the scope, resource type, tag, or label specification to match the intended resources.
  6. If necessary, [create a new resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_configuration).




Your changes are applied to the next attack path simulation.

read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#aps_no_rvcs_match_resources).

### `APS resource value assignment limit exceeded`

**Category name in the API** : `APS_RESOURCE_VALUE_ASSIGNMENT_LIMIT_EXCEEDED`

In the last [attack path simulation](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations), the number of high-value resource instances, as identified by the [Resource value configurations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-value-configurations), exceeded the limit of 1,000 resource instances in a high-value resource set. As a result, Security Command Center excluded the excess number of instances from the high-value resource set.

To remediate this finding, you can try the following actions:

  * Use [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) or [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) to reduce the number of matches for a given resource type or within a specified scope. The tags or labels have to be applied to the resources instances before they can be matched by a resource value configuration.
  * Create a resource value configuration that assigns a [resource value](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-values) of `NONE` to a subset of the resources that are specified in another configuration.

Specifying a value of `NONE` overrides any other configurations and excludes the resource instances from your high-value resource set.

  * Reduce the [scope resource attribute](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-attributes) specification in the resource value configuration.

  * Delete resource value configurations that assign a value of `LOW`.




For instructions on creating, editing, or deleting a resource value configuration, see [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#edit_a_configuration).

read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#aps_value_assignment_limit_exceeded).

### `CIEM service account missing permissions`

**Category name in the API** : `CIEM_SERVICE_ACCOUNT_MISSING_PERMISSIONS`

The service account that is used by the CIEM service is missing permissions. CIEM cannot generate one or more finding categories.

To remediate this finding, restore the required IAM roles on the CIEM service account:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Select your organization's CIEM service account. The service account's identifier is an email address with the following format:
         
         service-org-ORGANIZATION_ID@gcp-sa-ciem.iam.gserviceaccount.com
         

Replace `ORGANIZATION_ID` with your organization's numerical ID.

If you don't see the service account listed, click **GRANT ACCESS** at the top of the page and enter the service account as a new principal.

  3. Grant the CIEM Service Agent role (`roles/ciem.serviceAgent`) to the service account. If you use custom roles, make sure they include the following permissions:

     * `cloudasset.assets.exportResource`
     * `cloudasset.assets.exportIamPolicy`
  4. Click **Save**.




### `CIEM AWS CloudTrail configuration error`

**Category name in the API** : `AWS_CLOUDTRAIL_CONFIGURATION_ERROR`

Either all or some CIEM AWS findings aren't being sent to Security Command Center. The AWS CloudTrail feed failed and is unable to successfully fetch data due to a configuration error.

There are three possible causes for this finding:

  * **Missing AWS CloudTrail feed**

To fix this issue, create and configure a feed in Security Operations console to ingest AWS CloudTrail logs. Set the **Ingestion label** key-value pair to `CIEM` and `TRUE`.

For instructions on creating a feed, see [Create the feed](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle#create_the_feed) in the Google SecOps documentation.

  * **Errors in feed configuration**

Make sure you have configured the feed correctly.

To configure a feed, see [Configure feed in Google Security Operations to ingest AWS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle#configure_feed_in_to_ingest_aws_logs) in the Google SecOps documentation.

  * **Incomplete AWS CloudTrail configuration**

To fix this issue, set up the S3 bucket in your AWS CloudTrail configuration to log both **data events** and **management events** from all AWS accounts where you intend to use CIEM.

To set up CloudTrail, see [Configure AWS CloudTrail (or other service)](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle#configure_aws_cloudtrail_or_other_service) in the Google SecOps documentation.




### `External Exposure VPC Service Controls Restriction`

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Category name in the API** : `EXTERNAL_EXPOSURE_VPC_SC_RESTRICTION`

External Exposure cannot perform scans or generate findings for a project because the project is protected by a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview). You must grant the External Exposure service agent inbound access to the service perimeter.

Depending on the resource level where the service is enabled, the service account identifier uses one of the following email address formats: 

  * For organizations or folders:
        
        service-RESOURCE_KEYWORD-RESOURCE_ID@gcp-sa-ee-hpsa.iam.gserviceaccount.com
        

  * For projects:
        
        service-project-PROJECT_NUMBER@gcp-sa-ee.iam.gserviceaccount.com
        




Replace the following:

  * `RESOURCE_KEYWORD`: the keyword `org` or `folder`
  * `RESOURCE_ID`: the organization ID or folder ID 
  * `PROJECT_NUMBER`: the project number 



If you have both organization-level and project-level service accounts, apply the remediation to both of them. 

To remediate this finding, add an ingress rule to the blocking service perimeter:

  1. In the Google Cloud console, go to the **VPC Service Controls** page.
  2. Select the blocking access policy and the service perimeter.
  3. Click **Edit** and then **Ingress policy**.
  4. Click **Add ingress rule** and configure the **From** block: 
     1. For **Identity** , select **Selected identities & groups**.
     2. Enter the email address of the External Exposure service account.
     3. For **Source** , select **All sources**.
  5. Configure the rule's **To** block: 
     1. For **Project** , select **All projects** , or select the specific project listed in the finding.
     2. For **Operations or IAM roles** , select **All operations**.
  6. Click **Save**.



### `GKE service account missing permissions`

**Category name in the API** : `GKE_SERVICE_ACCOUNT_MISSING_PERMISSIONS`

Container Threat Detection can't generate findings for a Google Kubernetes Engine cluster, because the [ GKE default service account](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization) on the cluster is missing permissions. This prevents Container Threat Detection from being successfully enabled on the cluster.

To remediate this finding, [restore the GKE default service account](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#restore_service_account), and confirm that the service account has the **Kubernetes Engine Service Agent** (`roles/container.serviceAgent`) role.

read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#gke_cluster_service_account_has_been_deleted).

### `KTD blocked by admission controller`

**Category name in the API** : `KTD_BLOCKED_BY_ADMISSION_CONTROLLER`

Container Threat Detection can't be enabled on a cluster because a third-party admission controller is preventing the deployment of the required [Kubernetes DaemonSet object](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection).

To remediate this finding, make sure that the admission controllers that are running on the cluster allow Container Threat Detection to create the required Kubernetes objects.

#### Check the admission controller

Check to see if the admission controller in your cluster is denying the deployment of the Container Threat Detection DaemonSet object.

  1. In the finding description in finding details in the Google Cloud console, review the included error message from Kubernetes. The Kubernetes error message should be similar to the following message:
         
         generic::failed_precondition: incompatible admission webhook:
         admission webhook "example.webhook.sh" denied the request:
         [example-constraint] you must provide labels: {"example-required-label"}.
         

  2. In the Admin Activity Cloud Audit Logs for the project that contains your cluster, look for the error message shown in the **Description** field of the finding details.

  3. If your admission controller is working, but is denying the deployment of the Container Threat Detection DaemonSet object, configure your admission controller to allow the [service agent for Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#required_permissions) to manage objects in the `kube-system` namespace.

The service agent for Container Threat Detection must be able to manage specific Kubernetes objects.




For more information about using admission controllers with Container Threat Detection, see [PodSecurityPolicy and Admission Controllers](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#podsecuritypolicy_and_admission_controllers).

#### Confirm the fix

After you fix the error, Security Command Center automatically attempts to enable Container Threat Detection. After waiting for enablement to complete, you can check if Container Threat Detection is active by using the following steps:

  1. Go to Kubernetes Engine **Workloads** page in the console.

[Go to Kubernetes workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. If necessary, select **Show system workloads**.

  3. On the **Workloads** page, filter the workloads first by the cluster name.

  4. Look for the `container-watcher` workload. If `container-watcher` is present and its status shows `OK`, Container Threat Detection is active.




### `KTD image pull failure`

**Category name in the API** : `KTD_IMAGE_PULL_FAILURE`

Container Threat Detection can't be enabled on the cluster because a required container image can't be pulled (downloaded) from `gcr.io`, the [Container Registry](https://docs.cloud.google.com/container-registry/docs/overview) image host.

The pulling or downloading of a container image can fail for any of multiple possible reasons.

Check the following:

  * Make sure that your VPC network, DNS, or firewall settings are not blocking network access from the cluster to the `gcr.io` image host.
  * If the cluster is private, make sure that [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) is enabled to allow access to the `gcr.io` image host.
  * If the network settings and Private Google Access are not the cause of the failure, see the GKE troubleshooting documentation for [`ImagePullBackOff` and `ErrImagePull`](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls) errors.



read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#ktd_image_pull_failure).

### `KTD service account missing permissions`

**Category name in the API** : `KTD_SERVICE_ACCOUNT_MISSING_PERMISSIONS`

The Container Threat Detection service account that is identified in the finding details in the Google Cloud console is missing required permissions. Either all or some Container Threat Detection findings are not being sent to Security Command Center.

To remediate this finding, follow these steps:

  1. Grant the [Container Threat Detection Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerthreatdetection#containerthreatdetection.serviceAgent) role (`roles/containerthreatdetection.serviceAgent`) to the service account. For more information, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

Alternatively, if you want to use a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role), make sure it has the [permissions in the Container Threat Detection Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerthreatdetection#containerthreatdetection.serviceAgent) role.

  2. Make sure that there are no IAM [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) preventing the service account from using any of the permissions in the Container Threat Detection Service Agent role. If there is a deny policy blocking access, add the service account as an [exception principal](https://docs.cloud.google.com/iam/docs/deny-overview#deny-rules) in the deny policy.




For more information about the Container Threat Detection service account and the role and permissions it requires, see [Required IAM permissions](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#required_permissions)

read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#container_threat_detection_service_account_missing_permissions).

### `Misconfigured Cloud Logging Export`

**Category name in the API** : `MISCONFIGURED_CLOUD_LOGGING_EXPORT`

The project configured for [continuous export to Cloud Logging](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging) is unavailable. As a result, Security Command Center can't send findings to Logging.

To remediate this finding, do one of the following:

  * If the project recovery period has not elapsed, [restore the missing project](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects#restoring_a_project).

**Note:** You can verify the number of days left in the recovery period by using the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) Google Cloud CLI method.
  * If the project has been permanently deleted, [configure a new or existing project for Logging exports](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging).




read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#misconfigured_cloud_logging_export).

### `VPC Service Controls Restriction`

**Category name in the API** : `VPC_SC_RESTRICTION`

Security Health Analytics can't produce certain findings for a project, because the project is protected by a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview). You must grant the Security Command Center service account inbound access to the service perimeter.

The service account's identifier is an email address with the following format: 
    
    
    service-RESOURCE_KEYWORD-RESOURCE_ID@security-center-api.iam.gserviceaccount.com
    

Replace the following:

  * `RESOURCE_KEYWORD`: the keyword `org` or `project`, depending on what resource owns the service account 
  * `RESOURCE_ID`: one of the following:

    * The organization ID if the service account is owned by the organization 
    * The [ project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) if the service account is owned by a project 



If you have both organization-level and project-level service accounts, apply the remediation to both of them. 

To remediate this finding, follow these steps.

#### Step 1: Determine which service perimeter is blocking Security Health Analytics

  1. Get the VPC Service Controls unique ID and the project ID associated with the finding:

     1. To view the finding's details, click its category name.
     2. In the **Description** field, copy the VPC Service Controls unique ID—for example, `5e4GI409D6BTWfOp_6C-uSwmTpOQWcmW82sfZW9VIdRhGO5pXyCJPQ`.
     3. In the **Resource path** field, copy the project's ID.
  2. Obtain the access policy ID and the service perimeter's name:

     1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

     2. On the toolbar, select the project associated with the finding.

     3. In the search box, enter the error's unique ID.

![Search by error UID](https://docs.cloud.google.com/static/security-command-center/images/search-error-id.png)

If the error doesn't appear in the query results, extend the timeline in the **Histogram** , and then rerun the query.

     4. Click the error that appears.

     5. Click **Expand nested fields**.

     6. Copy the value of the `servicePerimeterName` field. The value has the following format:
            
            accessPolicies/ACCESS_POLICY/servicePerimeters/SERVICE_PERIMETER
            

In this example, the service perimeter's full resource name is `accessPolicies/540107806624/servicePerimeters/vpc_sc_misconfigured`.

        * `ACCESS_POLICY` is the access policy ID—for example, `540107806624`.
        * `SERVICE_PERIMETER` is the service perimeter's name—for example, `vpc_sc_misconfigured`.

![Service perimeter's full resource name](https://docs.cloud.google.com/static/security-command-center/images/service-perimeter-name.png)

     7. To get the display name that corresponds to the access policy ID, use the gcloud CLI.

If you can't make organization-level queries, ask your administrator to perform this step.
            
            gcloud access-context-manager policies list \
                --organization ORGANIZATION_ID
            

Replace `ORGANIZATION_ID` with your organization's numerical ID.

You get an output similar to the following:
            
            NAME          ORGANIZATION  SCOPES                 TITLE           ETAG
            540107806624  549441802605                         default policy  2a9a7e30cbc14371
            352948212018  549441802605  projects/393598488212  another_policy  d7b47a9ecebd4659
            

The display name is the title that corresponds to the access policy ID. Take note of the access policy's display name and the service perimeter's name. You need them in the next section.




#### Step 2: Create ingress and egress rules that grant access

This section requires you to have organization-level access to VPC Service Controls. If you don't have organization-level access, ask your administrator to perform these steps.

In the following steps, you create ingress and egress rules on the service perimeter that you identified in step 1.

**Note:** If you were unable to identify the restricted service perimeter in step 1, we recommend performing the following steps for each service perimeter in your organization that restricts access to the project and to the services that Security Health Analytics calls. You can check each service perimeter's settings through the Google Cloud console or through the [Google Cloud CLI](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#formatted-list).

### Console

#### Navigate to the service perimeter

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter?supportedpurview=organizationId)

  2. Select your organization.
  3. In the drop-down list, select the access policy that contains the service perimeter that you want to grant access to.

The service perimeters associated with the access policy appear in the list.

  4. Click the name of the service perimeter that you want to update.

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
         
         accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Click edit **Edit**.



#### Add an egress rule

  1. Click **Egress policy**.
  2. Click **Add an egress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent). This address has the following format: 
            
            service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **All projects** , or select the project specified in the finding. 
     2. For **Operations or IAM roles** , select **Select operations**. 
     3. Click **Add operations** , and then add the following operations:

        * Add the **bigquery.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **binaryauthorization.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudkms.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **logging.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **monitoring.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudresourcemanager.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **storage.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **compute.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **iam.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **container.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.



#### Add an ingress rule

  1. Click **Ingress policy**.
  2. Click **Add an ingress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent). This address has the following format: 
            
            service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **All projects** , or select the project specified in the finding. 
     2. For **Operations or IAM roles** , select **Select operations**. 
     3. Click **Add operations** , and then add the following operations:

        * Add the **bigquery.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **binaryauthorization.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudkms.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **logging.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **monitoring.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudresourcemanager.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **storage.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **compute.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **iam.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **container.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
  5. Click **Save**.



### gcloud

**Warning:** The `--set-ingress-policies` and `--set-egress-policies` flags replace all existing ingress or egress policies in the perimeter. If you have existing policies, you must retrieve them first, add the new policy to the appropriate ingress or egress YAML file, and then run the update command. 

  1. If a quota project isn't already set, then set it. Choose a project that has the Access Context Manager API enabled. 
         
         gcloud config set billing/quota_project QUOTA_PROJECT_ID

Replace `QUOTA_PROJECT_ID` with the ID of the project that you want to use for billing and quota. 

  2. Create a file named `egress-rule.yaml` with the following contents:
         
         - egressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com
           egressTo:
             operations:
             - serviceName: bigquery.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: binaryauthorization.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudkms.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: logging.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: monitoring.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudresourcemanager.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: storage.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: iam.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: container.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - '*'

Alternatively, you can use `operations` to specify services for which VPC Service Controls violations appear and `resources` to specify the project that appeared in the finding. 

Replace `ORGANIZATION_ID` with your organization ID.

  3. Create a file named `ingress-rule.yaml` with the following contents:
         
         - ingressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: bigquery.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: binaryauthorization.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudkms.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: logging.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: monitoring.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudresourcemanager.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: storage.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: iam.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: container.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - '*'

Alternatively, you can use `operations` to specify services for which VPC Service Controls violations appear and `resources` to specify the project that appeared in the finding. 

Replace `ORGANIZATION_ID` with your organization ID.

  4. Add the egress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-egress-policies=egress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Add the ingress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=ingress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME




For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). 

#### Services that Security Health Analytics calls

To function correctly, Security Health Analytics requires access to the Google Cloud APIs of the services that it scans, as well as core infrastructure services. Depending on your configuration, you might need to allow ingress or egress for the following services in your VPC Service Controls perimeters:

  * BigQuery API (`bigquery.googleapis.com`)
  * Binary Authorization API (`binaryauthorization.googleapis.com`)
  * Cloud Key Management Service API (`cloudkms.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)
  * Cloud Monitoring API (`monitoring.googleapis.com`)
  * Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)
  * Identity and Access Management API (`iam.googleapis.com`)
  * Kubernetes Engine API (`container.googleapis.com`)



If you use custom modules or scan other services, you might need to allow access to additional APIs.

read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#vpc_service_controls_restriction).

### `Security Command Center service account missing permissions`

**Category name in the API** : `SCC_SERVICE_ACCOUNT_MISSING_PERMISSIONS`

Security Command Center's [service agent](https://docs.cloud.google.com/iam/docs/service-agents) is missing the permissions needed to function properly.

The service account's identifier is an email address with the following format: 
    
    
    service-RESOURCE_KEYWORD-RESOURCE_ID@security-center-api.iam.gserviceaccount.com
    

Replace the following:

  * `RESOURCE_KEYWORD`: the keyword `org` or `project`, depending on what resource owns the service account 
  * `RESOURCE_ID`: one of the following:

    * The organization ID if the service account is owned by the organization 
    * The [ project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) if the service account is owned by a project 



If you have both organization-level and project-level service accounts, apply the remediation to both of them. 

To remediate this finding, follow these steps:

  1. Grant the Security Center Service Agent (`roles/securitycenter.serviceAgent`) role to the service account.

For more information, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

Alternatively, if you want to use a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role), make sure it has the permissions in the [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) role.

  2. Make sure that there are no IAM [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) preventing the service account from using any of the permissions in the required roles. If there is a deny policy blocking access, add the service account as an [exception principal](https://docs.cloud.google.com/iam/docs/deny-overview#deny-rules) in the deny policy.




read_more Learn about this finding type's [supported assets and scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#security_command_center_service_account_missing_permissions).

## What's next

Learn about [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
