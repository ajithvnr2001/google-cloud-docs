---
url: https://docs.cloud.google.com/storage/docs/collaboration/
title: Sharing and collaboration \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:41.453293+00:00
---

# Sharing and collaboration  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/collaboration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Sharing and collaboration Stay organized with collections  Save and categorize content based on your preferences. 

This document provides common data sharing and collaboration scenarios. It includes how to configure your project and bucket [Identity and Access Management (IAM) policies](https://docs.cloud.google.com/storage/docs/access-control/iam) to implement the scenarios.

## Storage and maintenance of private data

In this scenario, a company's marketing analyst wants to use Cloud Storage to back up confidential revenue forecasts and sales projection data. The data must be accessible only by the marketing analyst. The company's IT department oversees and manages the company's Cloud Storage account. Their primary management responsibilities include creating and sharing buckets so that various departments throughout the company have access to Cloud Storage.

To meet the confidentiality and privacy needs of the marketing analyst, the bucket and object permissions must allow the IT staff to maintain the bucket in which the spreadsheets are stored, but also ensure that the IT staff cannot view/download the data that is stored in the bucket. To accomplish this, you create a bucket named `finance-marketing` and grant the following [_roles_](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for the listed _resources_ to the specified _principals_ :

Role | Resource | Principal | Description  
---|---|---|---  
**Storage Legacy Bucket Owner** | The bucket `finance-marketing` | IT staff | Giving the IT staff the **Storage Legacy Bucket Owner** role for the bucket allows them to perform common bucket management tasks, such as deleting objects and changing the IAM policy on the bucket. It also allows the IT staff to list the contents of the `finance-marketing` bucket, but not view or download any of the contents.  
**Storage Object User** | The bucket `finance-marketing` | Marketing analyst | Giving the marketing analyst the **Storage Object User** role for the bucket allows her to upload, view, update, and delete objects in the bucket.  
  
With these roles, nobody except the marketing analyst can view or download the objects that are in the bucket. The IT staff can still list the contents of the `finance-marketing` bucket, and they can delete and replace the files that are stored in the bucket should the need arise.

**Caution:** Because the IT staff has permission to manage the bucket, it is possible for them to grant themselves or others permission to view objects in the bucket. To mitigate this, you can view [audit logs](https://docs.cloud.google.com/logging/docs/audit) in order to track changes made to bucket and project permissions.

### Implement this scenario

**Your actions**

You should take the following actions to implement the scenario:

  1. Create a bucket named `finance-marketing`. For step-by-step instructions, see [Creating a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  2. Give each IT staff member the **Storage Legacy Bucket Owner** role for the bucket. For step-by-step instructions, see [Adding a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).




**IT staff actions**

The IT staff should take the following actions to implement the scenario:

  1. Give the marketing analyst the **Storage Object User** for the bucket. For step-by-step instructions, see [Adding a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).



## Vendor drop box

In this scenario, a construction company works with several architectural design firms that deliver building plans for various projects. The construction company wants to set up a drop box for the vendor firms so they can upload architectural plans at various project milestones. The drop box must ensure the privacy of the construction company's clients, which means the drop box cannot allow the vendors to see each other's work. To accomplish this, you create a separate bucket for each architectural firm and grant the following [_roles_](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for the listed _resources_ to the specified _principals_ :

Role | Resource | Principal | Description  
---|---|---|---  
**Owner** | Overall project | Construction company manager | Giving the construction company manager the **Owner** role at the project level enables her to create buckets for each vendor.  
**Storage Object Viewer** | Overall project | Construction company manager | The **Storage Object Viewer** allows the construction company manager to download the objects that the vendors are uploading.  
**Storage Legacy Bucket Owner** | Each vendor bucket | Construction company manager | The **Storage Legacy Bucket Owner** role allows the construction company manager to list the contents of each bucket as well as delete objects at the end of each project milestone.  
**Storage Object Admin** | Each vendor bucket | The vendor associated with the bucket | Giving each vendor the **Storage Object Admin** for their own bucket gives them complete control over the objects in their bucket, including the ability to upload objects, list objects in the bucket, and control who has access to each object. It does not allow them to change or view metadata such as roles on the bucket as a whole, nor does it allow them to list or view other buckets in the project, thus preserving privacy between vendors.  
  
### Implement this scenario

**Your actions**

You should take the following actions to implement the scenario:

  1. Give the construction company manager the **Owner** role on the project as well as the **Storage Object Viewer** role on the project. For step-by-step instructions, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).



**Construction company manager actions**

The construction company manager should take the following actions to implement the scenario:

  1. Create a separate bucket for each vendor. For step-by-step instructions, see [Creating a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

Since the construction manager has the **Owner** role, she automatically gets the **Storage Legacy Bucket Owner** role for each bucket she creates.

  2. Give each vendor the **Storage Object Admin** for their respective bucket. For step-by-step instructions, see [Adding a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

  3. If any vendor intends to use the Google Cloud console, give them a link to their bucket, which has the format:

`https://console.cloud.google.com/storage/browser/BUCKET_NAME`

where `BUCKET_NAME` is the name of the vendor's bucket.




**Vendor actions**

Each vendor should take the following actions to implement the scenario:

  1. Upload objects to the assigned bucket. The easiest way to accomplish this is through the Google Cloud console. Other methods, such as the Google Cloud CLI, require additional setup prior to use. For step-by-step instructions, see [Uploading an object](https://docs.cloud.google.com/storage/docs/uploading-objects).

**Note:** Based on the permissions set in this scenario, vendors are required to sign in using one of the emails associated with the bucket assigned to them.



## Authenticated browser downloads

In this scenario, a client wants to make files available to specific individuals through simple browser downloads. You can do this using the [Cloud Storage cookie-based authentication](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth). To download objects, users must authenticate by signing in to a valid account, which includes Google Workspace, Cloud Identity, Gmail, and [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). The following authenticated users are able to download the object:

  * Users who have `READ` or `FULL_CONTROL` permission on the [access control list (ACL)](https://docs.cloud.google.com/storage/docs/access-control/lists) of the object itself.

  * Users with `storage.objects.get` permission in the [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) policy for the bucket or project that contains the object.




All other users get a `403 Forbidden (access denied)` error.

To use the feature, grant a user permission to access an object, then give the user a special URL to the object. When the user clicks the URL, Cloud Storage prompts them to sign in to their account (if they are not already logged in) and the object is downloaded to their computer.

### Implement this scenario

You can implement cookie-based authentication in four general steps:

  1. **Create a bucket.** For step-by-step instructions, see [Creating a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

Assuming you create a bucket in a project you own, you automatically gain permissions that allow you to upload objects to the bucket and change who has access to the bucket.

**Note:** If you already have a bucket that you want to use, keep in mind that you're serving secure content from the bucket in this scenario. As a best practice, make sure anonymous users don't have bucket or project-level roles that give access to the objects.
  2. **Upload the object you want to share.** For step-by-step instructions, see [Uploading an object](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. **Give users access to the object.** A common way to do this is to modify the bucket's IAM policy to give specific users the **Storage Object Viewer** role, which applies to all objects in the bucket. For step-by-step instructions, see [Adding a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

  4. **Provide users with a special URL to the object.**

Authenticated browser downloads access Cloud Storage through a [specific URL endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth). Use the following URL:

`https://storage.cloud.google.com/BUCKET_NAME/OBJECT_NAME`

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the desired object. For example, `my-bucket`.
     * `OBJECT_NAME` is the name of the desired object. For example, `pets/dog.png`.

Since only users with appropriate access permissions can view it, it doesn't matter how you make this URL available. You can send it to them directly, or you can post it on a web page.




## Use a group to control access

In this scenario, you want to make objects available to specific users, such as users invited to try out new software. In addition, you want to invite many users, but you do not want to set permissions for each user individually. At the same time, you don't want to make the objects publicly readable and send invited customers links to access the objects, because there is a risk the links may be sent to users who are not invited.

One way to handle this scenario is through the use of [Google Groups](https://groups.google.com/). You can create a group and add only invited users to the group. Then, you can give the group as a whole access to the objects:

Role | Resource | Principal | Description  
---|---|---|---  
**Storage Object Viewer** | Your bucket | Google Group | Giving the Google Group the **Storage Object Viewer** role for the bucket allows any customer who is part of the Google Group to view objects in the bucket. No one outside of the group has access to the objects.  
**Note:** When using groups to manage access to your resources, you should be aware of [Group policies and limits](https://support.google.com/a/answer/6099642?hl=en) that determine how many members can be in the group. If you need to invite more users than can be added to a group, you can create a service that authenticates users and redirects them to a URL signed by a [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [Signed URLs (query string authentication)](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

### Implement this scenario

  1. Create a Google Group and add customers to it. For step-by-step instructions see [Create a group](https://support.google.com/groups/answer/2464926?hl=en).

  2. Create a bucket. For step-by-step instructions, see [Creating a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  3. Upload objects to your bucket. For step-by-step instructions, see [Uploading an object](https://docs.cloud.google.com/storage/docs/uploading-objects).

  4. Give the Google Group access to the objects.

     * You can use the IAM role **storage.objectViewer** to give viewing access to all objects in your bucket. For step-by-step instructions, see [Adding a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

     * If you want to only give access to some of the objects in the bucket, set the **Reader** ACL on those individual objects. For step-by-step instructions, see [Setting ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#set-an-acl).

  5. Share the appropriate [request endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints) with the group, so that they know where to go to access the objects.

For example, when using the Google Cloud console, the URL `https://console.cloud.google.com/storage/browser/BUCKET_NAME` takes you to the list of objects in the bucket `BUCKET_NAME`.




## Use managed folders to control access

In this scenario, you have multiple customers that each own a unique website containing custom images. You want customers to be able to upload images to their website only, but not to other websites. When a customer cancels their account, you want to disable public access to the images on their website, but avoid deleting the images in case the customer wants to reactivate their account.

One way to handle this scenario is through the use of [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders). You can create multiple managed folders within a bucket and use IAM to control access to individual managed folders for both your customers and their end users.

### Implement this scenario

  1. [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  2. [Create a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders) in the bucket for each customer website.

  3. For each managed folder, [set an IAM policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders#managed-folder-set-policy) that grants a customer the Storage Object User (`roles/storage.objectUser`) role, so the customer can upload objects to the managed folder and remove objects from the managed folder.

  4. For all managed folders, [set an IAM policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders#managed-folder-set-policy) that grants the Storage Object Viewer (`roles/storage.objectViewer`) role to the principal `allUsers`, so the image objects in the managed folders can be viewable to the public.

Alternatively, you can grant a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that gives `allUsers` the `storage.objects.get` IAM permission.

  5. When a customer cancels their account, [remove the IAM policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders#managed-folder-remove) that grants the customer the Storage Object User (`roles/storage.objectUser`) role for the associated managed folder. To disable public access to the objects within that managed folder, remove the IAM policy that grants the Storage Object Viewer (`roles/storage.objectViewer`) role to `allUsers`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
