---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access/
title: Verify key access \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:36.995911+00:00
---

# Verify key access  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Verify key access Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to verify key access after you create a customer-managed encryption key (CMEK) policy.

## Key access verification use cases

At any time, you can rerun key access verification to identify issues with the key:

  * **Key disablement** : if a key gets disabled, data access to volumes stops.

  * **Key destructions** : if a key is destroyed, access to data is unrestorable. You can delete volumes to free up capacity. For more information, see [Delete a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#delete_a_volume).

  * **Missing permissions** : if permissions are removed, the instructions to grant them appear. See [Grant the service permission to read a key](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access#grant_the_service_permission_to_read_a_key).




## Grant the service permission to read a key

To use a CMEK key, you must grant the service permission to read the specified key first. NetApp Volumes provides the correct Google Cloud CLI commands. To grant the required Cloud KMS key permissions to the service, you need to create a project-wide custom role with the appropriate permissions, and then a key role binding that binds the custom role to the appropriate service account. You need the Role Administrator (`roles/iam.RoleAdmin`) permissions on the project within your Google Account to create the custom role and the Cloud KMS Admin (`roles/cloudkms.admin`) permissions to grant NetApp Volumes access to the key.

Use the following instructions to grant the service permission to read a key using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **CMEK policies**.

  3. Find the CMEK policy you want to edit and click the **Show more** menu.

  4. Select **Verify key access**.

  5. If you haven't configured key access yet, the verification fails and the UI shows instructions on how to grant key access. After you run the required Google Cloud CLI commands, click **Retry** to run key verification again.

If verification is successful, a dialog appears that indicates successful verification. If verification is unsuccessful, click **Retry** to rerun the key check.




### gcloud

Run the following `kms-configs verify` command:
    
    
     gcloud netapp kms-configs verify CONFIG_NAME \
       --project=PROJECT_ID \
       --location=LOCATION

Replace the following information:

  * `CONFIG_NAME`: the name of the config.

  * `PROJECT_ID`: the unique project ID you want to grant access for.

  * `LOCATION`: the region of the config.




If key verification is successful, the command outputs the following message:
    
    
    healthy: true

If key verification fails, you have to grant access permissions to the key. Run the following command to identify the Google Cloud CLI commands to grant the service key access. You need the `cloudkms.admin` role to run the following command.
    
    
      gcloud netapp kms-configs describe CONFIG_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --format="value(instructions)"

For more information about additional optional flags, see [Google Cloud SDK documentation for Cloud Key Management Service](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/kms-configs/verify).

For more information, see [Cloud Key Management Service user documentation](https://docs.cloud.google.com/kms/docs/quickstart).

## Configure VPC Service Controls ingress rule for CMEK

If you use [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls), you must update your ingress rules to allow traffic for the relevant project, region, and service account.

### Projects in the same perimeter

Use the following template to configure the necessary permissions. This example assumes your KMS project and the project that owns your volumes are in the same perimeter. If they are in different perimeters, see the additional requirements in Projects in different perimeters.
    
    
       {
        "ingressFrom": {
          "identities": [
        "serviceAccount:n-cmek-usea4-1234567890@netapp-cmek-prod.iam.gserviceaccount.com"
           ],
           "sources": [
             {
              "resource": "projects/112233445566"
             }
           ]
       },
       "ingressTo": {
         "operations": [
           {
             "methodSelectors": [
               {
                 "method": "*"
               }
           ],
           "serviceName": "cloudkms.googleapis.com"
           }
           ],
           "resources": [
             "projects/1234567890"
           ]
       },
       "title": "CMEK for NetApp Volumes"
       }
     

Update the following fields in the template:

  * **ingressFrom.identities** : enter a comma-separated list of the service accounts used by NetApp Volumes. The service uses a unique service account for each project and location in the following format:

`serviceAccount:n-cmek-location-short-name-your-project-number@netapp-cmek-prod.iam.gserviceaccount.com`

where `location-short-name` is the short form of the region, for example, `usea4` for `us-east4`, and `your-project-number` is the project number.

You can query this service account name using the following command:
        
        gcloud netapp kms-configs describe NAME --location LOCATION --format="value(serviceAccount)"
        

Replace the following information:

    * `NAME`: the name of the CMEK policy.
    * `LOCATION`: the region of the CMEK policy.

The example in the template shows the service account name for Google project `1234567890` in `us-east4` region.

  * **ingressTo.resources** : enter the project number of the project that contains the `KMS` key. The example in the template uses `projects/1234567890`.

  * **ingressFrom.sources** : enter a comma-separated list of the backend projects used by the service. You must add one entry for each Google region where you need to host CMEK volumes. To get the backend project number for your region, contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/). In the template, `projects/112233445566` is a placeholder that you must replace with the backend project number for your region.




You can't specify individual methods for the `cloudkms.googleapis.com` service; you must use `*` to allow all methods.

### Projects in different perimeters

If your KMS project and your NetApp Volumes project are in different perimeters, or if only one of the projects is in a perimeter, you must configure additional VPC Service Controls to enable communication between the NetApp Volume backend projects, your NetApp Volumes project, and the KMS project across the service perimeter boundaries.

Complete the following steps to configure additional VPC Service Controls:

  1. Copy the preceding ingress template.

  2. Add the project number that owns your NetApp Volumes to the `ingressFrom.sources` list.

  3. Apply the ingress policy to the perimeter that contains the KMS project.

  4. Apply an egress policy to the perimeter that contains your NetApp Volumes project. Use the following template to apply an egress policy:
         
         {
            "egressFrom": {
              "identities": [
            "serviceAccount:n-cmek-usea4-1234567890@netapp-cmek-prod.iam.gserviceaccount.com"
               ],
               "sources": [
                 {
                  "resource": "projects/33445566"
                 }
               ]
           },
           "egressTo": {
             "operations": [
               {
                 "methodSelectors": [
                   {
                     "method": "*"
                   }
               ],
               "serviceName": "cloudkms.googleapis.com"
               }
               ],
               "resources": [
                 "projects/1234567890"
               ]
           },
           "title": "CMEK for NetApp Volumes"
           }
         

Update the following fields in the template:

     * **egressFrom.identities** : use the same service accounts used for `ingressFrom.identities`.

     * **egressFrom.sources** : the project number of the project that owns your NetApp Volumes. The example in the template uses `projects/33445566`.

     * **egressTo.resources** : enter the project number of the project that contains the `KMS` key. The example in the template uses `projects/1234567890`.




## What's next

[Manage CMEK policies](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/manage-cmek-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
