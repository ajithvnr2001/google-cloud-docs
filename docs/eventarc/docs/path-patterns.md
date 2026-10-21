---
url: https://docs.cloud.google.com/eventarc/docs/path-patterns/
title: Understand path patterns \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:51.783462+00:00
---

# Understand path patterns  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/path-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Understand path patterns Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Eventarc supports applying a path pattern when filtering. The path pattern syntax lets you define an expression that matches events. This lets you control the granularity of the Eventarc trigger you are creating, and to capture and act on certain events. For example, you can create a trigger that applies to a single event, such as a change to a specific file, or you can extend the scope of the pattern and create a trigger that applies more broadly.

## Apply a path pattern

You can apply a path pattern to filter events when you create a trigger using the Eventarc Google Cloud console page or by running a `gcloud` command.

For example, you can apply a path pattern when filtering on _resource names_ or _database instances_ (a single instance or a path).

  * Specifying a **resource name path pattern** applies when creating a trigger for **Cloud Audit Logs events** and to `resourceName` values. A resource name indicates the resource being audited through an audit log. Resource names are organized hierarchically using identifiers made up of the ID of the resource itself and the IDs of any parent resources, all separated by forward slashes, like this: `/projects/project-1/datasets/dataset-id`. The filtering done by Eventarc matches patterns based on the values of these identifiers. For more information, in this document, see Resource name format.

  * Specifying a **database instance path pattern** applies when creating a trigger for **Firebase Realtime Database events** and to `instance` or `ref` values. A database instance indicates a Firebase Realtime Database instance. You can apply a path pattern to the instance name of the database instance, or a document path for which you want to receive events when data is created, updated, or deleted in that path, or any of its children.

  * Specifying a **resource ID path pattern** applies when creating a trigger for **Cloud IoT events** and to `registry` and `device` values. You can apply a path pattern to filter changes in registries, and devices in a registry, with wildcard matching.




For details, see the instructions to [create a trigger for a specific provider, event type, and destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).

## Identify if you can apply a path pattern

To confirm if you can apply a path pattern to an attribute of an event from a provider, describe the event provider. For example:
    
    
    gcloud eventarc providers describe cloudaudit.googleapis.com --location=us-central1

The output is similar to the following and a `pathPatternSupported` value of `true` indicates that you can apply a path pattern:
    
    
    displayName: Cloud Audit Logs
    eventTypes:
    - description: An audit log is created that matches the trigger's filter criteria.
      filteringAttributes:
      - attribute: methodName
        description: The identifier of the service's operation.
        required: true
      - attribute: resourceName
        description: The complete path to a resource. Used to filter events for a specific
          resource.
        pathPatternSupported: true
      - attribute: serviceName
        description: The identifier of the Google Cloud service.
        required: true
      - attribute: type
        required: true
      type: google.cloud.audit.log.v1.written
    name: projects/project-name/locations/us-central1/providers/cloudaudit.googleapis.com

Or, for example:
    
    
    gcloud eventarc providers describe firebasedatabase.googleapis.com --location=us-central1

Where the output is similar to the following:
    
    
    displayName: Firebase Realtime Database
    eventTypes:
    - description: New data has been created in the database.
      filteringAttributes:
      - attribute: instance
        description: A single database instance.
        pathPatternSupported: true
        required: true
      - attribute: ref
        description: Pattern to match for the database instance.
        pathPatternSupported: true
        required: true
      - attribute: type
        required: true
      type: google.firebase.database.ref.v1.created
    [...]

For more information, see [`gcloud eventarc providers describe`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/providers/describe).

## Path pattern syntax

The path pattern syntax is defined as follows:

![Path pattern syntax](https://docs.cloud.google.com/static/eventarc/images/path-patterns.svg) **Pattern** | `/?`` Segment ``(/``Segment``)*`  
---|---  
**Segment** | `CaptureGroup ``| ``Expression`  
**CaptureGroup** | `{ ``ID ``(= ``Expression``)? }`  
**Expression** | `Wildcard ``|`` MultiSegmentWildcard ``| ``NameSegment`  
**NameSegment** | `(``Character``* ``Wildcard``? ``Character``*)`  
**ID** | `[a-zA-Z0-9_]+`  
**Wildcard** | `*`  
**MultiSegmentWildcard** | `**`  
**Character****1** | `[\\w\\s\\t~@#$%&.,?:;+='[]()-]`  
  
#### Legend:

`?` | zero or one  
---|---  
`*` | zero or more  
`+` | one or more  
`|` | OR  
  
**1** Only listed ASCII characters are supported. Regular expression matching is not supported. Supported metacharacters: 

  * `\w` refers to a word; also represented as `[a-zA-Z0-9_]`
  * `\t` refers to a tab
  * `\s` refers to a whitespace character



### Expressions

An expression can be one of the following segment types and cannot be empty:

  * A single segment `Wildcard` defined as `*` matches zero or more characters in the pattern.
  * A `MultiSegmentWildcard` defined as `**` matches zero or more segments in the pattern.
  * A `NameSegment`consists of zero or one `*` and other characters. This combination lets you filter by prefix, suffix, or file extension; for example, `file-*.txt`.



Note that a path can contain many single segment wildcards, but only one multiple segment wildcard. For example, the following path is invalid: `/projects/**/buckets/**`.

### Resource regionality

Resource names can contain location identifiers. For example:

`/projects/$PROJECT_ID/**locations/$REGION** /triggers/my-trigger`

However, path pattern matching is constrained by resource regionality. For example, for Cloud Audit Logs triggers, location wildcards only match triggers from the Cloud Audit Logs region, or global triggers.

### Capture groups

A `CaptureGroup` lets you capture the content of an expression. You do this by assigning the value to a variable name in braces; for example, `buckets/{path=**}/files/{filename=file-*.txt}`. A single segment wildcard can omit `=*` in a capture group; for example, `/projects/_/buckets/{bucket}/objects/file.*`

**Note:** Capture groups have no semantic meaning; only the syntax is supported.

## Resource name format

The following table provides examples of full resource names for commonly used Google Cloud services. **It is not a complete list.** To learn more about how full resource names are formatted, see the [Resource names](https://docs.cloud.google.com/apis/design/resource_names) section of the API design guide.

Resource type | Full resource name format  
---|---  
BigQuery [datasets](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) | `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID`  
Cloud Billing [accounts](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts) | `//cloudbilling.googleapis.com/billingAccounts/BILLING_ACCOUNT_ID`  
Cloud Firestore [documents](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents)1 | `//firestore.googleapis.com/projects/PROJECT_ID/databases/DATABASE_ID/documents/DOCUMENT`  
Cloud Run [services](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services) | `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID`  
Cloud SQL [instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances) | `//sqladmin.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID`  
Cloud Storage [buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets)2 | `//storage.googleapis.com/projects/_/buckets/BUCKET_ID`  
Cloud Storage [objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects)2, 3 | `//storage.googleapis.com/projects/_/buckets/BUCKET_ID/objects/OBJECT_ID`  
Compute Engine [instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) | `//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID`  
Compute Engine [networks](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) | `//compute.googleapis.com/projects/PROJECT_ID/global/networks/NETWORK`  
Compute Engine [subnetworks](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks) | `//compute.googleapis.com/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK`  
Google Kubernetes Engine [clusters](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters) | `//container.googleapis.com/projects/PROJECT_ID/clusters/CLUSTER_ID`  
Identity-Aware Proxy [App Engine app service](https://docs.cloud.google.com/iap/docs/reference/compute-engine-apis) | `//iap.googleapis.com/projects/PROJECT_NUMBER/iap_web/appengine-PROJECT_ID/services/APP_SERVICE_ID`  
IAP [Compute Engine backend service](https://docs.cloud.google.com/iap/docs/reference/app-engine-apis) | `//iap.googleapis.com/projects/PROJECT_NUMBER/iap_web/compute/services/BACKEND_SERVICE_ID_OR_NAME`  
Pub/Sub [topics](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics) | `//pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID`  
Resource Manager [organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations) | `//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_NUMBER`  
Resource Manager [folders](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders) | `//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER`  
Resource Manager [projects](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects) | `//cloudresourcemanager.googleapis.com/projects/PROJECT_ID`  
  
1 For Cloud Firestore, don't specify a leading slash when creating a trigger (see [examples](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-firestore#create-trigger)). For more information, see [Cloud Firestore data model](https://firebase.google.com/docs/firestore/data-model).

2 For Cloud Storage, resource names contain an underscore (`_`) rather than a project ID. You _cannot_ replace the underscore with a project ID, project name, or project number.

3 For Cloud Storage, use the entire object name, including forward slashes. These characters are [part of the object name](https://docs.cloud.google.com/storage/docs/objects#naming), not path separators.

## Examples

The following examples demonstrate how you can and can't use the syntax.

### Valid patterns

Pattern | Description  
---|---  
`/projects/project-1/datasets/dataset-1` | Specific resource name.  
`/projects/project-1/regions/region-1/subnetworks/*` | Matches any subnetwork in `project-1` and `region-1`.  
`/projects/_/buckets/bucket-1/objects/*.txt` | Matches all TXT files in the bucket.  
`/projects/_/buckets/bucket-1/objects/file-*.txt` | Matches all TXT files with prefix `file-` in the bucket.  
`/projects/project-1/serviceAccounts/service-account-email-1/keys/**` | Matches any key for a specific service account email.  
`/projects/_/**/file-*.txt` | Matches any TXT file with prefix `file-` for all buckets.  
`/projects/_/buckets/bucket-*/objects/file-*.txt` | Matches all TXT files with prefix `file-` for any bucket with prefix `bucket-`.  
`/projects/_/buckets/{bucket}/objects/file.*`  
`/projects/_/buckets/{bucket=*}/objects/file.*`  
`/projects/_/buckets/*/objects/{filename=file.*}` | Three different representations of the same filter. Matches any bucket with a file named `file` of any type. The first two examples also capture the bucket and the last example captures the filename.   
`/projects/project-1/zones/zone-1/instances/**` | Matches anything in `project-1` and `zone-1`.  
`/projects/*/zones/zone-1/instances/**` | Matches anything in `zone-1` in any project.  
  
### Invalid patterns

Pattern | Description  
---|---  
`/projects/_/buckets/bucket-1/objects**/**` | Empty expression.  
`/projects**//** buckets/bucket-1/objects/file1.txt` | Empty expression.  
`/projects/_/buckets/bucket****** /objects/file1.txt` | Expression can contain only one `*`.  
`/projects/_/buckets/bucket-1/objects/**file-*.***` | Expression can contain only one `*`.  
`/projects/****** /buckets/******` | Resource path can contain only one `**`.  
`/projects/_/buckets/{**=***}/objects/file1.txt` | Missing ID in segment.  
`/projects/_/buckets/{**bucket=**}/objects/file1.txt` | Empty expression inside a capture group.  
`/projects/_/buckets/{**bucket** /objects/file1.txt` | Capture group not closed.  
  
### Pattern matching

Pattern | Resource | Matches?  
---|---|---  
`/buckets/bucket-1/objects/file1.txt` | `/buckets/bucket-1/objects/file1.txt` |   
`/buckets/bucket-1/objects/file2.txt` |   
`/buckets/bucket-1/objects/*` | `/buckets/bucket-1/objects/file3.txt` |   
`/buckets/bucket-1/objects/file4.jpg` |   
`/buckets/bucket-1/objects/files/file4.jpg` |   
`/buckets/bucket-1/objects` |   
`/buckets/bucket-1/objects/*.txt` | `/buckets/bucket-1/objects/file5.txt` |   
`/buckets/bucket-1/objects/file6.jpg` |   
`/buckets/bucket-1/objects/file-*.txt` | `/buckets/bucket-1/objects/file-777.txt` |   
`/buckets/bucket-1/objects/file-.txt` |   
`/buckets/bucket-1/objects/file.txt` |   
`/projects/_/**/{filename=file-*.txt}` | `/projects/_/objects/object-1/files/file-9.txt` |   
`/projects/_/{ob}jects/**/-+=*/file-9.txt` |   
`/projects/_/file-10.txt` |   
`/projects/_/files-1/file-1.txt/files-2/file-2.txt` |   
`/projects/_//file-1234.txt` |   
`/projects/_/files/file-5.txt/file.txt` |   
`{collection=[clients,users]}/id` | `users/id` |   
`clients/id` |   
`[clients,users]/id` |   
`{collection=clients,users}/id` | `users/id` |   
`clients/id` |   
`clients,users/id` |   
`all users/{id=.*_ +1@gmail.com}` | `all-users/aa_ +1@gmail.com` |   
`all users/bb_+1@gmail.com` |   
`all users/cc +1@gmail.com` |   
  
## What's next

  * For a list of the events supported by Eventarc, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
