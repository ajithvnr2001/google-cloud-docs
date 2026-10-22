---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-storage/
title: Google Cloud Storage \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:30.589428+00:00
---

# Google Cloud Storage  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Cloud Storage

This document provides guidance on how to integrate Cloud Storage with the SOAR module of Google Security Operations.

This integration uses one or more open source components. You can download a copy of the source code of this integration from a [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/GoogleCloudStorage.zip).

## Use cases

In the Google SecOps SOAR platform, the Google Cloud Storage integration solves the following use cases:

  * **Incident evidence storage** : playbooks can automatically collect and store incident-related evidence like logs and malware samples in Cloud Storage buckets to provide a tamper-proof repository for evidence preservation.

  * **Threat intelligence sharing:** your security team can use Cloud Storage to securely share threat intelligence feeds like lists of malicious IP addresses and domains with other teams or organizations. Sharing feeds enables collaborative threat defense and faster response times.

  * **Malware analysis sandbox integration** : playbooks can automatically submit suspicious files from an incident to a cloud-based malware analysis sandbox. You can store the analysis results in Cloud Storage for review and further action to provide efficient and scalable malware analysis.

  * **Security configuration backup** : use the SOAR capabilities of Google SecOps to automate regular backups of critical security configurations like firewall rules and intrusion detection system signatures to Cloud Storage. Automating backups provides business continuity and faster recovery in case of accidental or malicious changes.

  * **Phishing campaign artifact storage** : use the SOAR capabilities of Google SecOps to store phishing emails, attachments, and other artifacts in Cloud Storage while investigating a phishing campaign. Artifact storage allows for centralized analysis and preservation of evidence for potential legal action.




## Before you begin

Before you configure the Cloud Storage integration in Google SecOps, complete the following prerequisite steps:

**Note:** For new deployments provisioned starting in Q4 2025, we recommend configuring all service accounts in the same project as your Google SecOps instance.

  1. Create a service account.

  2. Grant the necessary roles to your service account.

  3. Choose and configure an authentication method.




### Create a service account

To create a service account, complete the following steps:

  1. In the Google Cloud console, go to **Credentials**. [Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. From the **Create credentials** menu, select **Service account**.

  3. Enter a name in the **Service account name** field and click **Create and continue**. y

  4. Skip the optional role assignment and principal access screens by clicking **Continue > Done**.




### Grant roles to your service account

To let the integration access and manage your storage buckets and objects, grant the necessary roles to your service account:

  1. In the Google Cloud console, go to [**IAM & Admin > IAM**](https://console.cloud.google.com/iam-admin/iam).

  2. Locate your service account and click **edit Edit principal**.

  3. Click **Add another role** and select the following:

     * **Storage Admin** : Provides full control of buckets and objects.

     * **Service Usage Consumer** : Required only if you use a `Quota Project ID` for billing purposes.

  4. Click **Save**.




### Choose and configure an authentication method

Workload Identity is the recommended authentication method because it uses short-lived tokens rather than static secrets.

  1. **JSON key** : Relies on a static secret key file.

  2. **Workload Identity** (recommended): Uses temporary access tokens.




#### Configure a JSON key

Use the following procedure to generate a service account key file in JSON format:

  1. Select your service account in the Google Cloud console and go to **Keys**.

  2. Click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The key file downloads to your computer.




#### Configure Workload Identity credentials

Workload Identity lets Google SecOps securely impersonate your service account. Complete the following steps to configure your Workload Identity.

##### Configure the integration instance

To trigger the identity discovery process, you must first configure the basic connection parameters in Google SecOps:

  1. Go to **Content Hub > Response Integrations**.

  2. Search for and select the **Google Cloud Storage** integration.

  3. Configure the following mandatory parameters:

     * **API Root** : Enter the base URL (such as `https://storage.googleapis.com`).

     * **Workload Identity Email** : Enter the email address of the service account you created earlier.

     * **Verify SSL** : Make sure this is enabled.

  4. Leave the **User's Service Account** (JSON) field blank.

  5. Click **Save**.




##### Identify the unique identity email

Identifying the specific identity address requires triggering a connection test because Google SecOps uses a specific internal principal to communicate with your Google Cloud resources. This step makes sure you're granting permissions to the correct backend principal.

  1. Click **Test**. The test is expected to fail.

  2. Click the close_small button next to **Test**.

  3. Search the error message for an email address beginning with `gke-init-python@...` or `soar-python@...`. Copy this unique email.




##### Grant impersonation permissions

Establishing a trust relationship requires granting authority to the unique identity to act on behalf of your service account. This final step establishes the secure bridge that lets the integration access your resources using temporary, short-lived tokens.

  1. In the Google Cloud console, go to **[IAM& Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)**.

  2. Select the target service account and go to **Permissions**.

  3. Click **Grant access**.

  4. In the **New principals** field, paste the unique identity email you copied from Google SecOps.

  5. In the **Assign roles** field, select the **`Service Account Token Creator`** (`roles/iam.serviceAccountTokenCreator`) role.

  6. Click **Save**.

**Note:** It may take several minutes for the permissions to propagate before the test succeeds.



## Integrate Cloud Storage with Google SecOps

The integration requires the following parameters:

Parameters | Description  
---|---  
`Service Account` | _Optional_ The full content of the service account JSON key file. **Important:** To authenticate, you must provide either this field or `Workload Identity Email`. Don't populate this field if you intend to authenticate using a Workload Identity. Providing both causes authentication conflicts.   
`Workload Identity Email` | _Optional._ The client email address of the service account used for Workload Identity impersonation. **Important:** Don't populate this field if you intend to authenticate using a JSON key. Providing both causes authentication conflicts. To prevent `Permission Denied` errors, grant the **Service Account Token Creator** role to the Google SecOps instance service account on the email provided in this field.  
`Project ID` | _Optional_ The project ID to use for the Cloud Storage integration. If you set no value for this parameter, the project ID is retrieved from the JSON file content provided in the `Service Account` parameter.  
`Quota Project ID` | _Optional_ The Google Cloud project ID that you use for Google Cloud APIs and billing. This parameter requires you to grant the `Service Usage Consumer` role to your service account. If no value is provided, the project ID is retrieved from the JSON file content provided in the `Service Account` parameter.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Download an Object From a Bucket

Use this action to download a specific object (file) from a Cloud Storage bucket.

This action doesn't run on entities.

#### Action inputs

The Download an Object From a Bucket action requires the following parameters:

Parameters | Description  
---|---  
`Bucket Name` | _Required_ The name of the Cloud Storage bucket containing the object to download.   
`Object Name` | _Required_ The full name of the object to download.If the object is located within a folder in the bucket, include the folder path, such as `folderA/mydocument.pdf`.  
`Download Path` | _Required_ The absolute path for the downloaded object that leads to an existing directory, for example, `/tmp/downloads/`.   
  
#### Action outputs

The Download an Object From a Bucket action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the Download an Object From a Bucket action:
    
    
    {
    "object_name": "123.txt"
    "download_path": "/usr/bin/share/download.txt"
    }
    

##### Output messages

On a Case Wall, the Download an Object From a Bucket action provides the following output messages:

Output message | Message description  
---|---  
`OBJECT_NAME successfully downloaded to  DESTINATION_PATH.` `Action wasn't able to download OBJECT_NAME. Reason: Bucket BUCKET_NAME not found.` `Action wasn't able to download  OBJECT_NAME. Reason: No such object.` | Action succeeded.  
`Error executing action "Download an Object From a Bucket". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Download an Object From a Bucket action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get a Bucket's Access Control List

Use the Get a Bucket's Access Control List action to retrieve and display ACLs for the specified Cloud Storage buckets.

This action doesn't run on entities.

#### Action inputs

The Get a Bucket's Access Control List action requires the following parameters:

Parameters | Description  
---|---  
`Bucket Name` | _Required_ The name of the Cloud Storage bucket that you want to retrieve the ACL for. To retrieve ACLs for multiple buckets, enter the bucket names as a comma-separated string, such as `bucket1,bucket2,bucket3`.  
  
#### Action outputs

The Get a Bucket's Access Control List action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### JSON result
    
    
    [
      {"BucketName": "ziv",
       "BucketACLs": [
                      {"Entity": "project-owners-ID",
                       "Role": "OWNER"}
                     ]
      }
    ]
    

##### Output messages

On a Case Wall, the Get a Bucket's Access Control List action provides the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved the access control list (ACL) for the Cloud Storage buckets  BUCKET_NAMES` `Action wasn't able to return the access control list(ACL) for the Cloud Storage buckets  BUCKET_NAMES. Reason: Cannot get legacy ACL for a bucket that has uniform bucket-level access. Read more at https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access` `Action wasn't able to return the access control list(ACL) for the Cloud Storage buckets  BUCKET_NAMES.` | Action succeeded.  
`Error executing action "Get a Bucket's Access Control List". Reason:  ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Get a Bucket's Access Control List action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Bucket Objects

Use the List Bucket Objects action to list objects that are stored in the Cloud Storage bucket.

This action doesn't run on entities.

#### Action inputs

The List Bucket Objects action requires the following parameters:

Parameters | Description  
---|---  
`Bucket Name` | _Required_ The name of the bucket to retrieve objects from.  
`Max Objects to Return` | _Optional_ The number of objects to return.By default, the action returns 50 objects for every action execution.  
`Retrieves the Access Control List of an object` | _Optional_ If selected, the action retrieves the object ACL. Not selected by default.  
  
#### Action outputs

The List Bucket Objects action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following examples describe the JSON result outputs received when using the List Bucket Objects action:

  * If the `Retrieves the Access Control List of an object` parameter is not selected:
        
        {
            "Objects": [
                {
                    "ObjectName": "test.txt",
                "Bucket":
                "ContentType":
                    "TimeCreated": " ",
                    "TimeUpdated": " ",
                    "Size": 18,
                    "MD5": "7CjVfQ+Oz/C0pI08IKRdvQ==",
                    "Owner": "",
                    "CR32c": "RQEqxA==",
                    "id": "siemplify-tip/test.txt/1604926667310271"
                }
            ]
        }
        

  * If the `Retrieves the Access Control List of an object` parameter is selected:
        
        {
            "Objects": [
                {
                    "ObjectName": "test.txt",
                "Bucket": "BUCKET_NAME",
                "ContentType": "text/plain"
                    "TimeCreated": " ",
                    "TimeUpdated": " ",
                    "Size": 18,
                    "MD5": "7CjVfQ+Oz/C0pI08IKRdvQ==",
                    "Owner": "",
                    "CR32c": "RQEqxA==",
                    "id": "BUCKET_NAME/test.txt/1604926667310271",
                    "ObjectACL": [
                        {
                            "entity": "user@example.com",
                            "role": "OWNER"
                        }]
                },
            ]
        }
        




##### Output messages

On a Case Wall, the List Bucket Objects action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned objects of the BUCKET_NAME bucket in Google Cloud Storage.` `Action wasn't able to return objects of the BUCKET_NAME bucket in Google Cloud Storage.` | Action succeeded.  
`Error executing action "List Bucket Objects". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the List Bucket Objects action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Buckets

Use the List Buckets action to retrieve a list of buckets from Cloud Storage.

This action doesn't run on entities.

#### Action inputs

The List Buckets action requires the following parameters:

Parameters | Description  
---|---  
`Max Results` | _Optional_ The maximum number of buckets to return. By default, the action returns 50 buckets.  
  
#### Action outputs

The List Buckets action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the List Buckets action:
    
    
    {
        "Buckets": [
            {
                "CreationDate": "2020-11-09T12:57:03.981Z",
                "ModificationDate": "2020-11-09T12:57:03.981Z",
                "Name": "testexample",
                "Owner": "testexample"
            }]
    }
    

##### Output messages

On a Case Wall, the List Buckets action provides the following output messages:

Output message | Message description  
---|---  
`Successfully listed available buckets in Google Cloud Storage. ` `Action wasn't able to list available buckets in Google Cloud Storage. ` | Action succeeded.  
`Error executing action "List Buckets". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the List Buckets action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the Ping action to test connectivity to Cloud Storage.

This action doesn't run on entities.

#### Action inputs

None.

#### Action outputs

The action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the Ping action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Cloud Storage server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Google Cloud Storage server! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Ping action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Public Access From Bucket

Use the Remove Public Access From Bucket action to remove public access from the Cloud Storage bucket.

This action requires you to grant the `Storage Admin` role to the service account that you use in the integration.

This action doesn't run on entities.

#### Action inputs

The Remove Public Access From Bucket action requires the following parameters:

Parameters | Description  
---|---  
`Resource Name` | _Required_ The resource name of the bucket.  
`Prevent Public Access From Bucket` | _Required_ If selected, the action configures the bucket to prevent possible public access.  
  
#### Action outputs

The Remove Public Access From Bucket action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the Remove Public Access From Bucket action provides the following output messages:

Output message | Message description  
---|---  
`Successfully removed public access from bucket using Google Cloud Storage: RESOURCE_NAME ` | Action succeeded.  
`Error executing action "Remove Public Access From Bucket". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Remove Public Access From Bucket action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update an ACL entry on Bucket

Use the Update an ACL entry on Bucket action to update an ACL entry in the specified Cloud Storage bucket.

#### Action inputs

The Update an ACL entry on Bucket action requires the following parameters:

Parameters | Description  
---|---  
`Bucket Name` | _Required_ The name of the bucket to modify the ACL for.  
`Entity` | _Required_ The entity that holds the permission.Possible values are as follows:

  * `user-userId`
  * `user-emailAddress`
  * `group-groupId`
  * `group-emailAddress`
  * `allUsers`
  * `allAuthenticatedUsers`

For more information about entities, see [Resource representations](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls#resource).  
`Role` | _Required_ The access permission that is required for the entity.Possible values are as follows:

  * `OWNER`
  * `READER`
  * `WRITER`

  
  
#### Action outputs

The Update an ACL entry on Bucket action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the Update an ACL entry on Bucket action provides the following output messages:

Output message | Message description  
---|---  
`Action wasn't able to update the ACL entity: ENTITY to role: ROLE in bucket BUCKET_NAME. Reason: OWNERs are WRITERs.` `Action wasn't able to update the ACL entity: ENTITY to role: ROLE in bucket BUCKET_NAME. Reason: OWNERs are WRITERs.` | Action succeeded. The existing role mismatches the `Role` parameter value. Check the `Role` parameter value.  
`Successfully updated ACL entity: ENTITY to role: ROLE in bucket BUCKET_NAME.` | Action succeeded.  
`Error executing action "Update an ACL entry on Bucket". Reason: Entity ENTITY does not exist in the ACL of bucket BUCKET_NAME.` `Action wasn't able to update the ACL entity: ENTITY to role: ROLE in bucket BUCKET_NAME. The entity holding the permission can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.` `Error executing action "Update an ACL entry on Bucket". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Update an ACL entry on Bucket action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Upload an Object To a Bucket

Use the Upload an Object To a Bucket action to upload an object to the Cloud Storage bucket.

This action doesn't run on entities.

#### Action inputs

The Upload an Object To a Bucket action requires the following parameters:

Parameters | Description  
---|---  
`Bucket Name` | _Required_ The name of the bucket to upload an object to.  
`Source File Path` | _Required_ The absolute path to the file to upload, such as `/local/path/to/filename`.  
`Object Name` | _Required_ The name of the uploaded object in the bucket.  
  
#### Action outputs

The Upload an Object To a Bucket action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result
    
    
    {
       "object_id":"BUCKET_NAME/errorlog.txt/1610616919132517",
       "Object_name":"errorlog.txt",
       "md5_hash":"PTdL8D6pBwIKyMfIXR/H9A==",
       "object_path":"/b/BUCKET_NAME/o/errorlog.txt"
    }
    

##### Output messages

On a Case Wall, the Upload an Object To a Bucket action provides the following output messages:

Output message | Message description  
---|---  
`Successfully uploaded  SOURCE_PATH to bucket:  BUCKET_NAME.` `Action wasn't able to upload  SOURCE_PATH to Google Cloud Storage. Reason:No such file or directory: SOURCE_PATH.` | Action succeeded.  
`Error executing action "Upload an Object To a Bucket". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Upload an Object To a Bucket action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
