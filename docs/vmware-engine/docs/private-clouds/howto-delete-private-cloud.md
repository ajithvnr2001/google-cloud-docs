---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud/
title: Delete a private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:32.743738+00:00
---

# Delete a private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete a private cloud

A private cloud consists of one or more vSphere clusters. Deleting a private cloud deletes the entire private cloud. All components of the private cloud are deleted, including all of the private cloud nodes.

The components of a private cloud include the following:

  * Nodes
  * Virtual machines
  * Management VLANs and subnets
  * Workload subnets
  * All user data stored on the private cloud
  * All External access rules



Deleting a private cloud occurs in two stages: soft deletion and permanent deletion. The following happens in each stage:

  1. **Soft deletion** : The private cloud enters a seven-day soft-deletion state. During this stage, the following happens: 
     * Your billing stops immediately.
     * All connectivity to NSX segments and workloads are severed.
     * Access to the private cloud's user interface and API are disabled.
     * External IP addresses are disabled.
     * The private cloud's configuration and data are preserved and your VMs continue to run.
     * You can restore the private cloud to its previous state.
  2. **Permanent deletion** : After seven days, the private cloud and its resources are permanently deleted. If you want to permanently delete a private cloud that's in the soft-deletion state before the seven-day period ends, you can use Privileged Access Manager or contact [support](https://docs.cloud.google.com/support).



## Before you begin

If you want to keep any of the data, back up the data to another private cloud, Google Cloud storage, or on-premises storage or other storage.

### gcloud and API requirements

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

## Delete a private cloud

If you want your workload network IP CIDRs to be available right away, shut down all your VMs in your private cloud before starting the private cloud deletion.

###  Console 

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to delete the private cloud.

  3. Select the private cloud you want to delete.

  4. On the summary page, click **Delete this Private Cloud**.

  5. On the confirmation page, you're prompted to verify all of the results of the delete action. Read these carefully and continue with the deletion only if you're ready to accept the results. When you are ready to accept the results, select all of the checkboxes.

  6. Enter a number of hours to wait before running the deletion (1‑8 hours). Within that period, you can cancel the deletion by clicking **Cancel**.

  7. To verify that you know which private cloud you are deleting, enter the name of the private cloud to delete.

  8. Click **Delete** to mark the private cloud for deletion.




The deletion process starts after the specified delay, in hours, and runs to completion.

###  gcloud 

To delete a private cloud using the Google Cloud CLI, use the [`gcloud vmware private-clouds delete`command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete).
    
    
      gcloud vmware private-clouds delete PRIVATE_CLOUD_ID \
         --location=ZONE [--delay-hours=HOURS]

Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request
  * `ZONE`: the zone for this private cloud
  * `HOURS`: the numbers of hours to delay this request. By default, this is set to 3 hours, but you can set this from 0 to 8 hours. Setting this value to 0 means the deletion request will start immediately.



###  API 

To delete a private cloud using the VMware Engine API, make a `DELETE` request:
    
    
    curl -X DELETE -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds?privateCloudId=PRIVATE_CLOUD_ID&mps;delayHours=HOUR

Replace the following:

  * `TOKEN`: the authorization token for this request.
  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_ID`: the private cloud ID for the private cloud
  * `HOUR`: the number of hours to delay this request; the default is 3. You can set an hour between 0 to 8. Setting this value to 0 starts the deletion request immediately.



###  Python 

Deleting a private cloud with the Google Cloud VMware Engine library is a one-step process compared to using the Google Cloud console. Be very careful when calling private cloud deletion methods.
    
    
    from google.api_core import operation
    from google.cloud import vmwareengine_v1
    
    
    def delete_private_cloud_by_full_name(cloud_name: str) -> operation.Operation:
        """
        Deletes VMware Private Cloud.
    
        Args:
            cloud_name: identifier of the Private Cloud you want to delete.
                Expected format:
                projects/{project_name}/locations/{zone}/privateClouds/{cloud}
    
        Returns:
            An Operation object related to started private cloud deletion operation.
        """
        client = vmwareengine_v1.VmwareEngineClient()
        request = vmwareengine_v1.DeletePrivateCloudRequest()
        request.force = True
        request.delay_hours = 3
        request.name = cloud_name
        return client.delete_private_cloud(request)
    
    
    def delete_private_cloud(
        project_id: str, zone: str, cloud_name: str
    ) -> operation.Operation:
        """
        Deletes VMWare Private Cloud.
    
        Args:
            project_id: name of the project hosting the private cloud.
            zone: zone in which the private cloud is located in.
            cloud_name: name of the private cloud to be deleted.
    
        Returns:
            An Operation object related to started private cloud deletion operation.
        """
        return delete_private_cloud_by_full_name(
            f"projects/{project_id}/locations/{zone}/privateClouds/{cloud_name}"
        )
    
    

## Accelerate private cloud deletion using Privileged Access Manager

You can use Privileged Access Manager to get short-lived privileged access to permanently delete a private cloud that is in a soft-deleted state, rather than waiting for the seven-day soft-deletion period to end. To learn more about Privileged Access Manager, see [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview).

To use Privileged Access Manager to accelerate private cloud deletion, you need an _entitlement_ , which defines the roles you can request, the users who can request them, and the users who can approve the requests. For more information, see [Create entitlements in Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-create-entitlements).

The entitlement must grant a role that includes permissions to delete immediately a Google Cloud VMware Engine private cloud, such as `vmwareengine.privateClouds.deleteNow`. For example, the `roles/vmwareengine.vmwareenginePrivilegedUser` role includes this permission.

To request, approve, and revoke grants that provide temporary access, see [Request and manage grants](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access). When requesting a grant, you must provide a justification, and the grant must be approved by a designated approver. Grants are valid for a specified duration.

After you have an active grant with the required permissions, you can permanently delete a private cloud in a soft-deleted state. This action permanently removes the private cloud and its resources.

###  Console 

  1. In the Google Cloud console, go to the **Private clouds** page.
  2. Select the private cloud to permanently delete. The private cloud must be in a `Temporarily deleted` state.
  3. On the summary page, click **Permanently Delete**.
  4. To confirm the private cloud you are deleting, enter its name.
  5. Click **Delete** to permanently delete the private cloud.



###  gcloud 

To permanently delete a private cloud in a `soft-deleted` state using the Google Cloud CLI, use the [`gcloud vmware private-clouds delete-now` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete-now).
    
    
      gcloud vmware private-clouds delete-now PRIVATE_CLOUD_ID \
         --location=ZONE

Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request
  * `ZONE`: the zone for this private cloud



###  API 

To permanently delete a private cloud in a `soft-deleted` state using the VMware Engine API, make a `POST` request:
    
    
    curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID:privateCloudDeletionNow

Replace the following:

  * `TOKEN`: the authorization token for this request.
  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_ID`: the private cloud ID for the private cloud



## Cancel deletion of a private cloud

You can cancel the deletion of a private cloud within the soft-deletion period. Use the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Private clouds** page.



[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  1. Select the private cloud that you have marked for deletion.
  2. On the summary page, click **Cancel deletion** to cancel the deletion of the private cloud.



###  gcloud 

To cancel deletion of a private cloud using the Google Cloud CLI, use the [`gcloud vmware private-clouds undelete` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/undelete):
    
    
      gcloud vmware private-clouds undelete PRIVATE_CLOUD_ID \
         --location=ZONE

Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request
  * `ZONE`: the zone for this private cloud



###  API 

To cancel deletion of a private cloud using the VMware Engine API, make a `POST` request:
    
    
    curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds?privateCloudId=PRIVATE_CLOUD_ID:undelete

Replace the following:

  * `TOKEN`: the authorization token for this request.
  * `PROJECT_ID`: the project ID for this request
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request



###  Python 
    
    
    from google.api_core import operation
    from google.cloud import vmwareengine_v1
    
    
    def cancel_private_cloud_deletion_by_full_name(cloud_name: str) -> operation.Operation:
        """
        Cancels in progress deletion of VMware Private Cloud.
    
        Args:
            cloud_name: identifier of the Private Cloud you want to cancel deletion for.
                Expected format:
                projects/{project_name}/locations/{zone}/privateClouds/{cloud}
    
        Returns:
            An Operation object related to canceling private cloud deletion operation.
        """
        client = vmwareengine_v1.VmwareEngineClient()
        request = vmwareengine_v1.UndeletePrivateCloudRequest()
        request.name = cloud_name
        return client.undelete_private_cloud(request)
    
    
    def cancel_private_cloud_deletion(
        project_id: str, zone: str, cloud_name: str
    ) -> operation.Operation:
        """
        Cancels in progress deletion of VMWare Private Cloud.
    
        Args:
            project_id: name of the project hosting the private cloud.
            zone: zone in which the private cloud is located in.
            cloud_name: name of the private cloud to cancel deletion for.
    
        Returns:
            An Operation object related to canceling private cloud deletion operation.
        """
        return cancel_private_cloud_deletion_by_full_name(
            f"projects/{project_id}/locations/{zone}/privateClouds/{cloud_name}"
        )
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
