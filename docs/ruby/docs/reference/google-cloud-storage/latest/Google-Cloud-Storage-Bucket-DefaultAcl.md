---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl/
title: Cloud Storage API - Class Google::Cloud::Storage::Bucket::DefaultAcl (v1.62.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:09.274034+00:00
---

# Cloud Storage API - Class Google::Cloud::Storage::Bucket::DefaultAcl (v1.62.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Storage API - Class Google::Cloud::Storage::Bucket::DefaultAcl (v1.62.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.62.1 (latest)  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.1  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.1  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.2  1.35.0 

Reference documentation and code samples for the Cloud Storage API class Google::Cloud::Storage::Bucket::DefaultAcl.

## Bucket Default Access Control List

Represents a Bucket's Default Access Control List.

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.readers.each { |reader| puts reader }

## Methods 

### #add_owner
    
    
    def add_owner(entity)

Grants default owner permission to files in the bucket.

**Parameter**

  * **entity** (String) — 

The entity holding the permission, in one of the following forms:

    * user-userId
    * user-email
    * group-groupId
    * group-email
    * domain-domain
    * project-team-projectId
    * allUsers
    * allAuthenticatedUsers



**Examples**

Grant access to a user by prepending `"user-"` to an email:
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    email = "heidi@example.net"
    bucket.default_acl.add_owner "user-#{email}"

Grant access to a group by prepending `"group-"` to email:
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    email = "authors@example.net"
    bucket.default_acl.add_owner "group-#{email}"

### #add_reader
    
    
    def add_reader(entity)

Grants default reader permission to files in the bucket.

**Parameter**

  * **entity** (String) — 

The entity holding the permission, in one of the following forms:

    * user-userId
    * user-email
    * group-groupId
    * group-email
    * domain-domain
    * project-team-projectId
    * allUsers
    * allAuthenticatedUsers



**Examples**

Grant access to a user by prepending `"user-"` to an email:
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    email = "heidi@example.net"
    bucket.default_acl.add_reader "user-#{email}"

Grant access to a group by prepending `"group-"` to email:
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    email = "authors@example.net"
    bucket.default_acl.add_reader "group-#{email}"

### #auth!
    
    
    def auth!(if_metageneration_match: nil)

**Aliases**

  * [#authenticatedRead!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_authenticatedRead!_instance_)
  * [#auth_read!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_auth_read!_instance_)
  * [#authenticated!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_authenticated!_instance_)
  * [#authenticated_read!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_authenticated_read!_instance_)



Convenience method to apply the default `authenticatedRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.auth!

### #auth_read!
    
    
    def auth_read!(if_metageneration_match: nil)

**Alias Of** : [#auth!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_auth!_instance_)

Convenience method to apply the default `authenticatedRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.auth!

### #authenticated!
    
    
    def authenticated!(if_metageneration_match: nil)

**Alias Of** : [#auth!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_auth!_instance_)

Convenience method to apply the default `authenticatedRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.auth!

### #authenticatedRead!
    
    
    def authenticatedRead!(if_metageneration_match: nil)

**Alias Of** : [#auth!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_auth!_instance_)

Convenience method to apply the default `authenticatedRead` predefined ACL rule to files in the bucket. rubocop:disable Naming/MethodName

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.auth!

### #authenticated_read!
    
    
    def authenticated_read!(if_metageneration_match: nil)

**Alias Of** : [#auth!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_auth!_instance_)

Convenience method to apply the default `authenticatedRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.auth!

### #bucketOwnerFullControl!
    
    
    def bucketOwnerFullControl!(if_metageneration_match: nil)

**Alias Of** : [#owner_full!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_owner_full!_instance_)

Convenience method to apply the default `bucketOwnerFullControl` predefined ACL rule to files in the bucket. rubocop:disable Naming/MethodName

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.owner_full!

### #bucketOwnerRead!
    
    
    def bucketOwnerRead!(if_metageneration_match: nil)

**Alias Of** : [#owner_read!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_owner_read!_instance_)

Convenience method to apply the default `bucketOwnerRead` predefined ACL rule to files in the bucket. rubocop:disable Naming/MethodName

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.owner_read!

### #delete
    
    
    def delete(entity)

Permanently deletes the entity from the bucket's default access control list for files.

**Parameter**

  * **entity** (String) — 

The entity holding the permission, in one of the following forms:

    * user-userId
    * user-email
    * group-groupId
    * group-email
    * domain-domain
    * project-team-projectId
    * allUsers
    * allAuthenticatedUsers



**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    email = "heidi@example.net"
    bucket.default_acl.delete "user-#{email}"

### #owner_full!
    
    
    def owner_full!(if_metageneration_match: nil)

**Aliases**

  * [#bucketOwnerFullControl!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_bucketOwnerFullControl!_instance_)



Convenience method to apply the default `bucketOwnerFullControl` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.owner_full!

### #owner_read!
    
    
    def owner_read!(if_metageneration_match: nil)

**Aliases**

  * [#bucketOwnerRead!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_bucketOwnerRead!_instance_)



Convenience method to apply the default `bucketOwnerRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.owner_read!

### #owners
    
    
    def owners() -> Array<String>

Lists the default owners for files in the bucket.

**Returns**

  * (Array<String>) 



**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.owners.each { |owner| puts owner }

### #private!
    
    
    def private!(if_metageneration_match: nil)

Convenience method to apply the default `private` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.private!

### #projectPrivate!
    
    
    def projectPrivate!(if_metageneration_match: nil)

**Alias Of** : [#project_private!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_project_private!_instance_)

Convenience method to apply the default `projectPrivate` predefined ACL rule to files in the bucket. rubocop:disable Naming/MethodName

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.project_private!

### #project_private!
    
    
    def project_private!(if_metageneration_match: nil)

**Aliases**

  * [#projectPrivate!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_projectPrivate!_instance_)



Convenience method to apply the default `projectPrivate` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.project_private!

### #public!
    
    
    def public!(if_metageneration_match: nil)

**Aliases**

  * [#publicRead!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_publicRead!_instance_)
  * [#public_read!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_public_read!_instance_)



Convenience method to apply the default `publicRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.public!

### #publicRead!
    
    
    def publicRead!(if_metageneration_match: nil)

**Alias Of** : [#public!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_public!_instance_)

Convenience method to apply the default `publicRead` predefined ACL rule to files in the bucket. rubocop:disable Naming/MethodName

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.public!

### #public_read!
    
    
    def public_read!(if_metageneration_match: nil)

**Alias Of** : [#public!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_public!_instance_)

Convenience method to apply the default `publicRead` predefined ACL rule to files in the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.public!

### #readers
    
    
    def readers() -> Array<String>

Lists the default readers for files in the bucket.

**Returns**

  * (Array<String>) 



**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.readers.each { |reader| puts reader }

### #refresh!
    
    
    def refresh!()

**Alias Of** : [#reload!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_reload!_instance_)

Reloads all Default Access Control List data for the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.reload!

### #reload!
    
    
    def reload!()

**Aliases**

  * [#refresh!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-DefaultAcl#Google__Cloud__Storage__Bucket__DefaultAcl_refresh!_instance_)



Reloads all Default Access Control List data for the bucket.

**Example**
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    
    bucket.default_acl.reload!

### #user_project
    
    
    def user_project()

A boolean value or a project ID string to indicate the project to be billed for operations on the bucket and its files. If this attribute is set to `true`, transit costs for operations on the bucket will be billed to the current project for this client. (See [Project#project](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project#Google__Cloud__Storage__Project_project_instance_ "Google::Cloud::Storage::Project#project \(method\)") for the ID of the current project.) If this attribute is set to a project ID, and that project is authorized for the currently authenticated service account, transit costs will be billed to that project. This attribute is required with requester pays-enabled buckets. The default is `nil`.

In general, this attribute should be set when first retrieving the owning bucket by providing the `user_project` option to [Project#bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project#Google__Cloud__Storage__Project_bucket_instance_ "Google::Cloud::Storage::Project#bucket \(method\)").

See also [#requester_pays=](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket#Google__Cloud__Storage__Bucket_requester_pays__instance_ "Google::Cloud::Storage::Bucket#requester_pays= \(method\)") and [#requester_pays](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket#Google__Cloud__Storage__Bucket_requester_pays_instance_ "Google::Cloud::Storage::Bucket#requester_pays \(method\)").

### #user_project=
    
    
    def user_project=(value)

A boolean value or a project ID string to indicate the project to be billed for operations on the bucket and its files. If this attribute is set to `true`, transit costs for operations on the bucket will be billed to the current project for this client. (See [Project#project](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project#Google__Cloud__Storage__Project_project_instance_ "Google::Cloud::Storage::Project#project \(method\)") for the ID of the current project.) If this attribute is set to a project ID, and that project is authorized for the currently authenticated service account, transit costs will be billed to that project. This attribute is required with requester pays-enabled buckets. The default is `nil`.

In general, this attribute should be set when first retrieving the owning bucket by providing the `user_project` option to [Project#bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project#Google__Cloud__Storage__Project_bucket_instance_ "Google::Cloud::Storage::Project#bucket \(method\)").

See also [#requester_pays=](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket#Google__Cloud__Storage__Bucket_requester_pays__instance_ "Google::Cloud::Storage::Bucket#requester_pays= \(method\)") and [#requester_pays](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket#Google__Cloud__Storage__Bucket_requester_pays_instance_ "Google::Cloud::Storage::Bucket#requester_pays \(method\)").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
