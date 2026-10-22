---
url: https://docs.cloud.google.com/appengine/migration-center/standard/java/migrate-datastore/
title: Migrate from App Engine Datastore to Firestore in Datastore mode \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:49.131362+00:00
---

# Migrate from App Engine Datastore to Firestore in Datastore mode  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/java/migrate-datastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from App Engine Datastore to Firestore in Datastore mode Stay organized with collections  Save and categorize content based on your preferences. 

This guide demonstrates how to migrate from App Engine Datastore to [Firestore in Datastore mode](https://docs.cloud.google.com/datastore/docs) (also referred to as Datastore).

Firestore in Datastore mode is similar to App Engine Datastore in that both refer to the same underlying Datastore service. While App Engine Datastore is accessible only through the App Engine legacy bundled services, Firestore in Datastore mode is a standalone Google Cloud product that is accessed through the Cloud Client Libraries.

Firestore in Datastore mode also offers a free tier and enables you to manage a highly scalable NoSQL document database and gives you the flexibility in the future to migrate to Cloud Run or another Google Cloud app hosting platform.

## Before you begin

  1. Review the [different Firestore database modes](https://docs.cloud.google.com/datastore/docs/firestore-or-datastore#choosing_a_database_mode) to ensure you understand the best use case for your app. Note that this guide covers how to migrate to Datastore mode.

  2. Review and understand Firestore in Datastore mode [pricing](https://cloud.google.com/datastore/pricing) and [quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas#Datastore).

Firestore in Datastore mode offers free usage with daily limits, and unlimited storage, read, and write operations for paid accounts. While App Engine apps are disabled, they won't get any traffic to incur charges, however Datastore usage may be billable if it exceeds the [free quota limits](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits).

  3. Enable the following APIs in the project containing your app:

     * Artifact Registry API to store and manage your build artifacts
     * Cloud Build API to continuously build, test, and deploy your application.
     * Cloud Datastore API to migrate from App Engine bundled Datastore to Firestore in Datastore mode.

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,datastore.googleapis.com)

  4. Have an existing App Engine app running Java 8 or 11 that is connected to the App Engine Datastore service.




## Process overview

At a high level, the process to migrate to Firestore in Datastore mode from App Engine Datastore consists of the following steps:

  1. Update configuration files
  2. Update your Java app
     1. Update the import statements
     2. Modify how the app accesses the Datastore service
     3. Obtain a Datastore generated key
     4. Modify entity creation
  3. Commit your transaction
  4. Query results



## Update configuration files

Update your configuration files to use the [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries).

Update the `pom.xml` file of your baseline Java app:

  1. Remove the App Engine SDK `appengine-api-1.0-sdk` imports, like the following:
         
         <dependency>
           <groupId>com.google.appengine</groupId>
           <artifactId>appengine-api-1.0-sdk</artifactId>
           <version>2.0.4</version>
         </dependency>
         

  2. Add the `Datastore` client, like the following:
         
         <dependency>
           <groupId>com.google.cloud</groupId>
           <artifactId>google-cloud-datastore</artifactId>
           <!-- Use latest version -->
           <version>2.2.9</version>
         </dependency>
         




## Update your Java app

### Update import statements

Modify your application files by updating the import and initialization lines:

  1. Remove the following App Engine import statements for App Engine Datastore `com.google.appengine.api.datastore.*`:
         
         import com.google.appengine.api.datastore.[DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService.html);
           import com.google.appengine.api.datastore.[DatastoreServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceFactory.html);
           import com.google.appengine.api.datastore.[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity.html);
           import com.google.appengine.api.datastore.[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html);
           import com.google.appengine.api.datastore.[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.html);
         

  2. Add the following Firestore in Datastore mode `com.google.cloud.datastore.*` imports:
         
         import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
           import com.google.cloud.datastore.[Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html);
           import com.google.cloud.datastore.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html);
           import com.google.cloud.datastore.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Entity.html);
           import com.google.cloud.datastore.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key.html);
           import com.google.cloud.datastore.[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity.html);
           import com.google.cloud.datastore.[KeyFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.KeyFactory.html);
           import com.google.cloud.datastore.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html);
           import com.google.cloud.datastore.[QueryResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.QueryResults.html);
           import com.google.cloud.datastore.[StructuredQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.html);
         




### Modify how your app accesses the Datastore service

Firestore in Datastore mode uses the `Datastore` class instead of `DatastoreService`. To modify how your app access the Datastore service:

  1. Find the lines that use the `DatastoreServiceFactory.getDatastoreService()` method, like the following:
         
         // Initialize a client
         DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
         

  2. Replace the `DatastoreServiceFactory.getDatastoreService()` with [`DatastoreOptions.getDefaultInstance().getService()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions#com_google_cloud_datastore_DatastoreOptions_getDefaultInstance__) method, like the following:
         
         // Initialize a client
         Datastore datastore = DatastoreOptions.getDefaultInstance().getService();
         




### Obtain a Datastore generated key

After you initialize a client, get your key by creating a new `KeyFactory` of the appropriate `Kind`, then have Datastore generate one for you. To obtain a Datastore generated key:

  1. Create a [`newKeyFactory`](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore#com_google_cloud_datastore_Datastore_newKeyFactory__).

  2. Call the `setKind()` method to determine the [`kind`](https://docs.cloud.google.com/datastore/docs/concepts/entities#kinds_and_identifiers) of entity used for query categorizations.

  3. Append the `newKey()` method to generate a Datastore key:
         
         //Prepare a new entity
         String kind = "visit";
         Key key = datastore.allocateId(datastore.newKeyFactory().setKind(kind).newKey());
         




### Modify entity creation

After obtaining a Datastore key, create entities using the following methods:

  1. Use [`Entity.newBuilder`](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/2.14.1/com.google.cloud.datastore.Entity.Builder), and pass the key generated by the Datastore.

Find the lines that use the [`Entity`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity#com_google_appengine_api_datastore_Entity_Entity_com_google_appengine_api_datastore_Key_) constructor call, like the following:
         
         Entity visit = new Entity(kind);
         

Replace the `Entity` constructor call with the `Entity.newBuilder` constructor call, like the following:
         
         Entity visit = Entity.newBuilder(key);
         

  2. Use the [`set`](https://docs.cloud.google.com/datastore/docs/samples/datastore-basic-entity) method to set properties on entities.

The first parameter is the intended property, and the second is the value. In the case of the `timestamp` property, the value is a `Timestamp` instead of an `Instant.toString()`.

Find the lines that use the [`setProperty`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity#com_google_appengine_api_datastore_Entity_setPropertiesFrom_com_google_appengine_api_datastore_Entity_) method, like the following:
         
         visit.setProperty("user_ip", userIp);
         visit.setProperty("timestamp", Instant.now().toString());
         

Replace the `setProperty` method with the `set` method, like the following:
         
         Entity visit = Entity.newBuilder(key).set("user_ip", userIp).set("timestamp", Timestamp.now()).build();
         




## Commit your transaction

The Firestore in Datastore mode client library uses the [`add()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreWriter#methods) method to commit a transaction. To commit your transaction:

  1. Find lines that use the [`put()`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PutContext) method, like the following:
         
         // Save the entity
         datastore.put(visit);
         

  2. Replace the `put()` method with the `add()` method, like the following:
         
         // Save the entity
         datastore.add(visit);
         




## Query Results

Queries retrieve [`entities`](https://docs.cloud.google.com/appengine/docs/legacy/standard/java/datastore/entities) that meet a specified set of conditions. You can use the following methods to display results:

  * The [`OrderBy`](https://docs.cloud.google.com/datastore/docs/concepts/queries#query_interface) method displays the results in ascending or descending order.

  * The [`Limit`](https://docs.cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets) method limits the maximum number of results fetched using in the same builder.




Querying uses a builder pattern method with the `kind` variable. The `kind` variable is set to `Visit` from the Obtain a Datastore generated key step.

To retrieve the first 10 results:

  1. Find lines that use the [`addSort()`](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/queries?tab=java#sort_orders) method, like the following:
         
         // Retrieve the last 10 visits from the datastore, ordered by timestamp.
           Query query = new Query(kind).addSort("timestamp", Query.SortDirection.DESCENDING);
           List<Entity> results = datastore.prepare(query).asList(FetchOptions.Builder.withLimit(10));
         

  2. Replace the `addSort()` method with the [`setOrderBy()`](https://docs.cloud.google.com/datastore/docs/concepts/queries#sort_orders) method and append the [`setLimit()`](https://docs.cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets) method, like the following:
         
         // Retrieve the last 10 visits from the datastore, ordered by timestamp.
         Query<Entity> query = Query.newEntityQueryBuilder()
                                 .setKind(kind)
                                 .setOrderBy(StructuredQuery.OrderBy.desc("timestamp"))
                                 .setLimit(10)
                                 .build();
         

  3. Once the query is ready, execute the code using [`datastore.run()`](https://docs.cloud.google.com/datastore/docs/concepts/queries#query_interface), and collect the results in a `QueryResultsEntity` collection.

The resulting `QueryResults` object is an iterator with a `hasNext()` function.

  4. Check if the result set has a `next` object for processing, instead of looping through the results list. For example:
         
         QueryResults<Entity> results = datastore.run(query);
         
               resp.setContentType("text/plain");
               PrintWriter out = resp.getWriter();
               out.print("Last 10 visits:\n");
               while (results.hasNext()) {
                   Entity entity = results.next();
                   out.format(
                           "Time: %s Addr: %s\n", entity.getTimestamp("timestamp"), entity.getString("user_ip"));
               }
         




## Examples

To see an example of how to migrate a Java 8 app to Firestore in Datastore mode, compare the [App Engine Datastore for Java 8 code sample](https://github.com/google/appengine-java-migration-samples/tree/main/baseline) and the [Firestore in Datastore mode code sample](https://github.com/google/appengine-java-migration-samples/tree/main/java17-and-cloud-run/finish) in GitHub.

## What’s next

  * Learn how to [Use Firestore in Datastore mode](https://docs.cloud.google.com/appengine/docs/standard/using-firestore-in-datastore-mode?tab=java).
  * See [Firestore in Datastore mode documentation](https://docs.cloud.google.com/datastore/docs) for more details.
  * Learn how to [Migrate off of legacy bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services?tab=java#top) for Java.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
