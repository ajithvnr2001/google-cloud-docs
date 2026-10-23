---
url: https://docs.cloud.google.com/storage/docs/faq/
title: Frequently asked questions \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:08.471226+00:00
---

# Frequently asked questions  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Resources ](https://docs.cloud.google.com/storage/docs/resources)



Send feedback 

#  Frequently asked questions Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Storage to store and retrieve your data globally. This frequently asked questions (FAQ) document addresses common questions about features and use cases. These use cases include availability, uploading, and downloading data. For detailed information about how to use Cloud Storage, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/introduction).

## Pricing and support

Where can I find pricing and billing information?
    

Read the [Pricing page](https://docs.cloud.google.com/storage/docs/pricing) for detailed information on pricing, including how Cloud Storage calculates bandwidth and storage usage.

Read the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs) for general information about billing in Google Cloud.

What are my support options?
    

See the Google Cloud [Customer Care page](https://docs.cloud.google.com/support-hub) for information about support options.

Does Cloud Storage offer a service level agreement (SLA)?
    

Yes. You are covered under the Cloud Storage [Service Level Agreement](https://docs.cloud.google.com/storage/sla).

Use the [SLA Financial Credit Eligibility form](https://support.google.com/cloud/contact/cloud_platform_sla) to notify Google of SLA Financial Credit eligibility.

## Getting started

Do I need to enable billing?
    If you want to create your own buckets and store data in them, you must enable billing.
Do I need to enable billing if I was granted access to someone else's bucket?
    

No, in this case another individual has already set up a Google Cloud project and either granted you access to the entire project or to one of their buckets and the objects it contains. Once you authenticate, typically with your user account, you can read or write data according to the access that you were granted.

For information about granting access to a project, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

I am just trying to download or access some data that is freely available to the public. How can I do that?
    

Simply follow the [Accessing public data guide](https://docs.cloud.google.com/storage/docs/access-public-data), which offers several methods for accessing freely available, public data that is stored in Cloud Storage. Depending on the method you use, you do not need to turn on billing, create credentials, or authenticate to Cloud Storage.

What tools and libraries are available for Cloud Storage?
    

In addition to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) and the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), Google Cloud options for interacting with Cloud Storage include the following:

  * The browser-based [Google Cloud console](https://docs.cloud.google.com/storage/docs/cloud-console) performs basic operations on buckets and objects.

  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface with Cloud Storage using [`gcloud storage` commands](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud).

  * The [Cloud Storage Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries) provide programmatic support for a number of programming languages, including Java, Python, and Ruby.




You can find additional, third-party tools and libraries by searching the Internet.

I'm developing a library or tool for Cloud Storage and I want to sell it on the Internet. Is this okay?
    

Yes!

How do I cancel my Cloud Storage account?
    

To cancel your Cloud Storage account, take the following steps:

  1. **Delete all your buckets and objects.**

**Warning:** Deleting an object or bucket is a permanent action that can't be undone. Back up any data that you want to keep before you begin deleting your buckets and objects.

For step-by-step instructions, see [Deleting Buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets).

  2. **Disable the Cloud Storage services for your project.**

For the desired project, [open the list of enabled APIs](https://console.cloud.google.com/project/_/apis/enabled) in the Google Cloud console. For each service in the list that you want to disable, click the name of the service. In the service's page, click **Disable API**.

  3. **Disable billing (optional).**

You do not incur any new Cloud Storage charges after you perform the above steps, but you can disable billing to stop receiving statements. For step-by-step instructions, see [Disable billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project). You will receive one last bill for any remaining changes incurred between the beginning of the billing cycle and when you disabled billing.

**Caution:** You cannot disable billing for individual services or APIs. If you have other services that are being billed to the same project, disabling billing also disables these services.

**Note:** You can choose to disable the Cloud Storage service without removing your Cloud Storage data, but you continue to incur relevant charges, such as storage charges for the remaining objects.

## Storage and content policy

How durable is my data in Cloud Storage?
    Cloud Storage is designed for 99.999999999% (11 9's) annual durability. For more information, see [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability).
How can I maximize the availability of my data?
    Consider storing your data in a multi-region or dual-region [bucket location](https://docs.cloud.google.com/storage/docs/locations) if high availability is a top requirement. For more considerations, see [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability). 
What kind of recovery point objective (RPO) is available?
    The [_Turbo replication_](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) feature is available for dual-region buckets at an additional charge. Turbo replication offers a shorter, more predictable [recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning), helping to reduce data loss exposure. Turbo replication is designed to asynchronously replicate 100% of newly written Cloud Storage objects to a separate region within a target of 15 minutes. This includes object uploads, rewrites, copies, and composes. 
Where is my data stored?
    Where Cloud Storage stores your data depends on the location of the bucket in which your data resides. For information on available locations and implications for choosing a location, see the [Bucket Locations](https://docs.cloud.google.com/storage/docs/locations) page. 
How do I protect myself from accidental data deletion?
    Cloud Storage offers several different options for you to protect your data from accidental deletion. See [Options for controlling data lifecycles](https://docs.cloud.google.com/storage/docs/control-data-lifecycles) for an overview of options.
Can I delete a Cloud Storage object that I accidentally uploaded to a [locked, retention-enabled bucket](https://docs.cloud.google.com/storage/docs/bucket-lock)?
    

No. You can only delete such an object after it has fulfilled its retention period.

If you have **not** locked the bucket, you can temporarily remove the retention policy, remove the object, and then reinstate the retention policy.

I believe some content hosted on your service is inappropriate, how do I report it?
    

Certain types of content are not allowed on this service; please refer to the [Terms of Services](https://docs.cloud.google.com/terms) and [Platform Policies](https://docs.cloud.google.com/terms/aup) for details. If you believe a piece of content is in violation of our policies, [report it here](https://support.google.com/legal/troubleshooter/1114905?rd=1/troubleshooter/1114905?rd=1) (select **See more products** , then **Google Cloud Storage & Cloud Bigtable**). 

## Using buckets

What is the default bucket location if I don't specify a location constraint?
    The default bucket location is within the US. If you don't specify a location constraint, then your bucket and data added to it are stored on servers in the US. 
Can I move buckets from one location to another or change the project that the bucket is associated with?
    No, you cannot change an existing bucket's location or project; a bucket remains in the location and project that you set during bucket creation. If you want to change either of these parameters, you have to [delete the bucket and recreate it](https://docs.cloud.google.com/storage/docs/moving-buckets). 
I created a bucket, but don't remember which project I created it in. How can I find it?
    

For most common Cloud Storage operations, you only need to specify the relevant bucket's name, not the project associated with the bucket. In general, you only need to specify a project identifier when creating a bucket or listing buckets in a project. For more information, see [When to specify a project](https://docs.cloud.google.com/storage/docs/projects#projectid-using).

To find which project contains a specific bucket:

  * If you are searching over a moderate number of projects and buckets, use the [Google Cloud console](https://console.cloud.google.com/), select each project, and view the buckets it contains.
  * Otherwise, [get the bucket's metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata) using the JSON API instructions. The project number associated with the bucket appears as part of the response. To get the project name, use the project number in the following terminal command: 
        
        gcloud projects list | grep PROJECT_NUMBER




## Using with other Google services

Can I use Cloud Storage to upload files to services in Google Workspace, such as [Google Drive](https://www.google.com/drive/)?
    No, Cloud Storage is not integrated with Google Workspace.
Can I use Cloud Storage with my Google Workspace account or Cloud Identity domain?
    Yes, you can use Cloud Storage with either.

## Accessing data

Can charges associated with accessing data be billed to the user who accesses the data?
    Yes. You can use the [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature to require that requesters include a billing account project in their requests. The requester's project is then billed for access charges instead of the owner of the accessed bucket.
Does Cloud Storage provide any acceleration capabilities for uploads and downloads?
    Yes. Cloud Storage allows customers to use a global DNS name for uploads and downloads. Google uses its private network to transfer data to/from the closest POP that the data is being uploaded from or downloaded to. This generally results in significantly higher performance for the transfers than what would be possible over the public Internet. This functionality is included with all Cloud Storage buckets at no additional charge.
I want to let someone download an individual object. How do I do that?
    There are several ways that you can share an individual object. You can use a [signed URL](https://docs.cloud.google.com/storage/docs/access-control/signed-urls), which gives time-limited access to anyone in possession of the signed URL. See [V4 signing with Cloud Storage tools](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers) for instructions to create a signed URL. Alternatively, you can use the [`resource.name` IAM condition](https://docs.cloud.google.com/storage/docs/access-control/iam#conditions) to selectively grant access to objects in a bucket. See [Using IAM conditions on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-iam) for instructions to apply an IAM condition.
How do I prevent race conditions for my Cloud Storage resources?
    The easiest way to avoid race conditions is to use a naming scheme that avoids more than one mutation of the same object name. Often such a design is not feasible, in which case you can use [preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) in your request. Preconditions allow the request to proceed only if the actual state of the resource matches the criteria specified in the preconditions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
