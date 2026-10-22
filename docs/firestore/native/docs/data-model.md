---
url: https://docs.cloud.google.com/firestore/native/docs/data-model/
title: Data model \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:26.076491+00:00
---

# Data model  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/data-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data model

Firestore is a NoSQL, document-oriented database. Unlike a SQL database, there are no tables or rows. Instead, you store data in _documents_ , which are organized into _collections_.

Each _document_ contains a set of key-value pairs. Firestore is optimized for storing large collections of small documents.

All documents must be stored in collections. Documents can contain _subcollections_ and nested objects, both of which can include primitive fields like strings or complex objects like lists.

Collections and documents are created implicitly in Firestore. Simply assign data to a document within a collection. If either the collection or document does not exist, Firestore creates it.

## Documents

In Firestore, the unit of storage is the document. A document is a lightweight record that contains fields, which map to values. Each document is identified by a name.

A document representing a user `alovelace` might look like this:

  * class alovelace

`first : "Ada"`  
`last : "Lovelace"`  
`born : 1815`  



**Note:** Firestore supports a variety of data types for values: boolean, number, string, geo point, binary blob, and timestamp. You can also use arrays or nested objects, called maps, to structure data within a document.

Complex, nested objects in a document are called maps. For example, you could structure the user's name from the example above with a map, like this:

  * class alovelace

`name :`  
`first : "Ada"`  
`last : "Lovelace"`  
`born : 1815`  





You may notice that documents look a lot like JSON. In fact, they basically are. There are some differences (for example, documents support extra data types and are limited to the [document size limit](https://docs.cloud.google.com/firestore/quotas#collections_documents_and_fields)), but in general, you can treat documents as lightweight JSON records.

## Collections

![](https://docs.cloud.google.com/static/firestore/native/docs/images/structure-data.png)

Documents live in collections, which are simply containers for documents. For example, you could have a `users` collection to contain your various users, each represented by a document:

  * collections_bookmark users

    * class alovelace

`first : "Ada"`  
`last : "Lovelace"`  
`born : 1815`  


    * class aturing

`first : "Alan"`  
`last : "Turing"`  
`born : 1912`  





Firestore is schemaless, so you have complete freedom over what fields you put in each document and what data types you store in those fields. Documents within the same collection can all contain different fields or store different types of data in those fields. However, it's a good idea to use the same fields and data types across multiple documents, so that you can query the documents more easily.

A collection contains documents and nothing else. It can't directly contain raw fields with values, and it can't contain other collections. (See Hierarchical Data for an explanation of how to structure more complex data in Firestore.)

The names of documents within a collection are unique. You can provide your own keys, such as user IDs, or you can let Firestore create random IDs for you automatically.

You do not need to "create" or "delete" collections. After you create the first document in a collection, the collection exists. If you delete all of the documents in a collection, it no longer exists.

## References

Every document in Firestore is uniquely identified by its location within the database. The previous example showed a document `alovelace` within the collection `users`. To refer to this location in your code, you can create a _reference_ to it.

### Web version 9
    
    
    import { doc } from "firebase/firestore";
    
    const alovelaceDocumentRef = doc(db, 'users', 'alovelace');
    
    [doc_reference.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/doc_reference.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var alovelaceDocumentRef = db.collection('users').doc('alovelace');
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L195-L195)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let alovelaceDocumentRef = db.collection("users").document("alovelace")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L241-L241)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRDocumentReference *alovelaceDocumentRef =
        [[self.db collectionWithPath:@"users"] documentWithPath:@"alovelace"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L170-L171)

##### Kotlin  
Android
    
    
    val alovelaceDocumentRef = db.collection("users").document("alovelace")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L214-L214)

##### Java  
Android
    
    
    DocumentReference alovelaceDocumentRef = db.collection("users").document("alovelace");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L260-L260)

### Dart
    
    
    final alovelaceDocumentRef = db.collection("users").doc("alovelace");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L85-L85)

##### Java
    
    
    // Reference to a document with id "alovelace" in the collection "users"
    DocumentReference document = db.collection("users").document("alovelace");
    
    [References.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L52-L53)

##### Python
    
    
    a_lovelace_ref = db.collection("users").document("alovelace")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L280-L280)

##### Python  
(Async)
    
    
    a_lovelace_ref = db.collection("users").document("alovelace")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L275-L275)

##### C++
    
    
    DocumentReference alovelace_document_reference =
        db->Collection("users").Document("alovelace");
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L45-L46)

##### Node.js
    
    
    const alovelaceDocumentRef = db.collection('users').doc('alovelace');
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L132-L132)

##### Go
    
    
    import (
    	"cloud.google.com/go/firestore"
    )
    
    func createDocReference(client *firestore.Client) {
    
    	alovelaceRef := client.Collection("users").Doc("alovelace")
    
    	_ = alovelaceRef
    }
    
    
    [retrieve_data_reference_document.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/retrieve_data_reference_document.go#L18-L29)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $document = $db->collection('samples/php/users')->document('alovelace');

##### Unity
    
    
    DocumentReference documentRef = db.Collection("users").Document("alovelace");

##### C#

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference documentRef = db.Collection("users").Document("alovelace");

##### Ruby
    
    
    document_ref = firestore.col("users").doc("alovelace")
    
    [data_model.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/data_model.rb#L22-L22)

A reference is a lightweight object that just points to a location in your database. You can create a reference whether or not data exists there, and creating a reference does not perform any network operations.

You can also create references to _collections_ :

### Web version 9
    
    
    import { collection } from "firebase/firestore";
    
    const usersCollectionRef = collection(db, 'users');
    
    [collection_reference.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/collection_reference.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var usersCollectionRef = db.collection('users');
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L201-L201)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let usersCollectionRef = db.collection("users")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L246-L246)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRCollectionReference *usersCollectionRef = [self.db collectionWithPath:@"users"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L175-L175)

##### Kotlin  
Android
    
    
    val usersCollectionRef = db.collection("users")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L220-L220)

##### Java  
Android
    
    
    CollectionReference usersCollectionRef = db.collection("users");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L266-L266)

### Dart
    
    
    final usersCollectionRef = db.collection("users");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L89-L89)

##### Java
    
    
    // Reference to the collection "users"
    CollectionReference collection = db.collection("users");
    
    [References.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L39-L40)

##### Python
    
    
    users_ref = db.collection("users")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L288-L288)

##### Python  
(Async)
    
    
    users_ref = db.collection("users")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L283-L283)

##### C++
    
    
    CollectionReference users_collection_reference = db->Collection("users");
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L50-L50)

##### Node.js
    
    
    const usersCollectionRef = db.collection('users');
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L136-L136)

##### Go
    
    
    import (
    	"cloud.google.com/go/firestore"
    )
    
    func createCollectionReference(client *firestore.Client) {
    	usersRef := client.Collection("users")
    
    	_ = usersRef
    }
    
    
    [retrieve_data_reference_collection.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/retrieve_data_reference_collection.go#L18-L28)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $collection = $db->collection('samples/php/users');

##### Unity
    
    
    CollectionReference collectionRef = db.Collection("users");

##### C#

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    CollectionReference collectionRef = db.Collection("users");

##### Ruby
    
    
    collection_ref = firestore.col "users"
    
    [data_model.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/data_model.rb#L31-L31)

**Note:** _Collection references_ and _document references_ are two distinct types of references and let you perform different operations. For example, you could use a collection reference for querying the documents in the collection, and you could use a document reference to read or write an individual document.

For convenience, you can also create references by specifying the path to a document or collection as a string, with path components separated by a forward slash (`/`). For example, to create a reference to the `alovelace` document:

### Web version 9
    
    
    import { doc } from "firebase/firestore"; 
    
    const alovelaceDocumentRef = doc(db, 'users/alovelace');
    
    [doc_reference_alternative.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/doc_reference_alternative.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var alovelaceDocumentRef = db.doc('users/alovelace');
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L207-L207)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let aLovelaceDocumentReference = db.document("users/alovelace")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L258-L258)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRDocumentReference *aLovelaceDocumentReference =
        [self.db documentWithPath:@"users/alovelace"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L186-L187)

##### Kotlin  
Android
    
    
    val alovelaceDocumentRef = db.document("users/alovelace")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L234-L234)

##### Java  
Android
    
    
    DocumentReference alovelaceDocumentRef = db.document("users/alovelace");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L280-L280)

### Dart
    
    
    final aLovelaceDocRef = db.doc("users/alovelace");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L93-L93)

##### Java
    
    
    // Reference to a document with id "alovelace" in the collection "users"
    DocumentReference document = db.document("users/alovelace");
    
    [References.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L65-L66)

##### Python
    
    
    a_lovelace_ref = db.document("users/alovelace")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L296-L296)

##### Python  
(Async)
    
    
    a_lovelace_ref = db.document("users/alovelace")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L291-L291)

##### C++
    
    
    DocumentReference alovelace_document = db->Document("users/alovelace");
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L62-L62)

##### Node.js
    
    
    const alovelaceDocumentRef = db.doc('users/alovelace');
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L142-L142)

##### Go
    
    
    import (
    	"cloud.google.com/go/firestore"
    )
    
    func createDocReferenceFromString(client *firestore.Client) {
    	// Reference to a document with id "alovelace" in the collection "users"
    	alovelaceRef := client.Doc("users/alovelace")
    
    	_ = alovelaceRef
    }
    
    
    [retrieve_data_reference_document_path.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/retrieve_data_reference_document_path.go#L18-L29)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $document = $db->document('users/alovelace');

##### Unity
    
    
    DocumentReference documentRef = db.Document("users/alovelace");

##### C#

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference documentRef = db.Document("users/alovelace");

##### Ruby
    
    
    document_path_ref = firestore.doc "users/alovelace"
    
    [data_model.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/data_model.rb#L40-L40)

## Hierarchical Data

To understand how hierarchical data structures work in Firestore, consider an example chat app with messages and chat rooms.

You can create a collection called `rooms` to store different chat rooms:

  * collections_bookmark rooms

    * class roomA

`name : "my chat room"`  


    * class roomB

`...`  





Now that you have chat rooms, decide how to store your messages. You might not want to store them in the chat room's document. Documents in Firestore should be lightweight, and a chat room could contain a large number of messages. However, you can create additional collections within your chat room's document, as subcollections.

### Subcollections

The best way to store messages in this scenario is by using subcollections. A subcollection is a collection associated with a specific document.

**Note:** You can query across subcollections with the same collection ID by using [Collection Group Queries](https://docs.cloud.google.com/firestore/native/docs/query-data/queries#collection-group-query).

You can create a subcollection called `messages` for every room document in your `rooms` collection:

  * collections_bookmark rooms

    * class roomA

`name : "my chat room"`  


      * collections_bookmark messages

        * class message1

`from : "alex"`  
`msg : "Hello World!"`  


        * class message2

`...`  


    * class roomB

`...`  





In this example, you would create a reference to a message in the subcollection with the following code:

### Web version 9
    
    
    import { doc } from "firebase/firestore"; 
    
    const messageRef = doc(db, "rooms", "roomA", "messages", "message1");
    
    [subcollection_reference.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/subcollection_reference.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var messageRef = db.collection('rooms').doc('roomA')
                    .collection('messages').doc('message1');
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L213-L214)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let messageRef = db
      .collection("rooms").document("roomA")
      .collection("messages").document("message1")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L251-L253)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRDocumentReference *messageRef =
        [[[[self.db collectionWithPath:@"rooms"] documentWithPath:@"roomA"]
        collectionWithPath:@"messages"] documentWithPath:@"message1"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L179-L181)

##### Kotlin  
Android
    
    
    val messageRef = db
        .collection("rooms").document("roomA")
        .collection("messages").document("message1")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L226-L228)

##### Java  
Android
    
    
    DocumentReference messageRef = db
            .collection("rooms").document("roomA")
            .collection("messages").document("message1");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L272-L274)

### Dart
    
    
    final messageRef = db
        .collection("rooms")
        .doc("roomA")
        .collection("messages")
        .doc("message1");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L99-L103)

##### Java
    
    
    // Reference to a document in subcollection "messages"
    DocumentReference document =
        db.collection("rooms").document("roomA").collection("messages").document("message1");
    
    [References.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L78-L80)

##### Python
    
    
    room_a_ref = db.collection("rooms").document("roomA")
    message_ref = room_a_ref.collection("messages").document("message1")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L305-L306)

##### Python  
(Async)
    
    
    room_a_ref = db.collection("rooms").document("roomA")
    message_ref = room_a_ref.collection("messages").document("message1")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L300-L301)

##### C++
    
    
    DocumentReference message_reference = db->Collection("rooms")
        .Document("roomA")
        .Collection("messages")
        .Document("message1");
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L55-L58)

##### Node.js
    
    
    const messageRef = db.collection('rooms').doc('roomA')
      .collection('messages').doc('message1');
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L146-L147)

##### Go
    
    
    import (
    	"cloud.google.com/go/firestore"
    )
    
    func createSubcollectionReference(client *firestore.Client) {
    	messageRef := client.Collection("rooms").Doc("roomA").
    		Collection("messages").Doc("message1")
    
    	_ = messageRef
    }
    
    
    [retrieve_data_reference_subcollection.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/retrieve_data_reference_subcollection.go#L18-L29)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $document = $db
        ->collection('rooms')
        ->document('roomA')
        ->collection('messages')
        ->document('message1');

##### Unity
    
    
    DocumentReference documentRef = db
    	.Collection("Rooms").Document("RoomA")
    	.Collection("Messages").Document("Message1");

##### C#

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference documentRef = db
        .Collection("Rooms").Document("RoomA")
        .Collection("Messages").Document("Message1");

##### Ruby
    
    
    message_ref = firestore.col("rooms").doc("roomA").col("messages").doc("message1")
    
    [data_model.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/data_model.rb#L49-L49)

Notice the alternating pattern of collections and documents. Your collections and documents must always follow this pattern. You cannot reference a collection in a collection or a document in a document.

Subcollections allow you to structure data hierarchically, making data easier to access. To get all messages in `roomA`, you can create a collection reference to the subcollection `messages` and interact with it like you would any other collection reference.

Documents in subcollections can contain subcollections as well, allowing you to further nest data. You can nest data up to 100 levels deep.

**Warning:** Deleting a document does not delete its subcollections!  
  
When you delete a document that has subcollections, those subcollections are not deleted. For example, there may be a document located at `coll/doc/subcoll/subdoc` even though the document `coll/doc` no longer exists. If you want to delete documents in subcollections when deleting a parent document, you must do so manually, as shown in [Delete Collections](https://docs.cloud.google.com/firestore/native/docs/manage-data/delete-data#collections).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
