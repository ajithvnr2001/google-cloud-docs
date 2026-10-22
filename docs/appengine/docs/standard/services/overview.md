---
url: https://docs.cloud.google.com/appengine/docs/standard/services/overview/
title: Available legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:43.088431+00:00
---

# Available legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Available legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The following list shows which services are supported in second-generation runtimes:

App Engine service | Availability in Python  | Alternatives  
---|---|---  
App Identity | Available |  Migrate to [Open ID Connect (OIDC) ID tokens](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-app-identity) or [Identity Platform](https://docs.cloud.google.com/iap/docs/concepts-overview)  
Blobstore | Available |  Migrate to [Cloud Storage](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-storage)  
Capabilities | Available |  No alternatives, see the [Google Cloud Service Health dashboard](https://status.cloud.google.com) or the [Google Cloud console support page](https://console.cloud.google.com/support/) for information on service status   
Deferred | Available |  No alternatives since this API is used with App Engine Task Queues   
Images | Available |  Migrate to [Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files#serving_files_from) to serve images directly, or use a third-party content delivery network (CDN) or [image processing library](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services#images)  
Logging | Not supported |  Use [standard logging libraries](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs)  
Namespaces | Available |  No alternatives since this API is used with other App Engine services   
Datastore | Available |  Migrate to [Datastore client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries)  
Mail | Available | [Migrate to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet for outbound messaging only   
Memcache | Available |  Migrate to [Memorystore](https://docs.cloud.google.com/appengine/migration-center/standard/python/memcache-to-memorystore)  
Modules | Available |  Use environment variables and the [App Engine Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) to obtain information and modify your application's running services   
NDB | Available |  Migrate to [Cloud NDB](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb)  
Remote | Not supported |  Use Cloud Client Libraries to access resources in other projects   
Search | Available |  Migrate to [Elasticsearch](https://www.elastic.co/elasticsearch/)  
Task Queues | Available |  Migrate to [Cloud Tasks for push queues](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues) and [Pub/Sub for pull queues](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-pull-queues)  
URL Fetch | Available |  Migrate to [standard libraries for outbound requests](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-outbound-requests)  
Users | Available |  Migrate to [user authentication options](https://docs.cloud.google.com/appengine/docs/standard/authenticating-users)  
  
For more information, refer to the user guides located on the left-side navigation or see the [API reference documentation](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
