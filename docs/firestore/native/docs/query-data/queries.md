---
url: https://docs.cloud.google.com/firestore/native/docs/query-data/queries/
title: Query and filter data \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:00.056680+00:00
---

# Query and filter data  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/query-data/queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query and filter data

Firestore provides powerful query functionality for specifying which documents you want to retrieve from a collection or collection group. These queries can also be used with either `get()` or `addSnapshotListener()`, as described in [Get Data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data) and [Get Realtime Updates](https://docs.cloud.google.com/firestore/native/docs/query-data/listen).

**Note:** While the code samples cover multiple languages, the text explaining the samples refers to the Web method names.

## Example data

To get started, write some data about cities so we can look at different ways to read it back:

### Web version 9
    
    
    import { collection, doc, setDoc } from "firebase/firestore"; 
    
    const citiesRef = collection(db, "cities");
    
    await setDoc(doc(citiesRef, "SF"), {
        name: "San Francisco", state: "CA", country: "USA",
        capital: false, population: 860000,
        regions: ["west_coast", "norcal"] });
    await setDoc(doc(citiesRef, "LA"), {
        name: "Los Angeles", state: "CA", country: "USA",
        capital: false, population: 3900000,
        regions: ["west_coast", "socal"] });
    await setDoc(doc(citiesRef, "DC"), {
        name: "Washington, D.C.", state: null, country: "USA",
        capital: true, population: 680000,
        regions: ["east_coast"] });
    await setDoc(doc(citiesRef, "TOK"), {
        name: "Tokyo", state: null, country: "Japan",
        capital: true, population: 9000000,
        regions: ["kanto", "honshu"] });
    await setDoc(doc(citiesRef, "BJ"), {
        name: "Beijing", state: null, country: "China",
        capital: true, population: 21500000,
        regions: ["jingjinji", "hebei"] });
    
    [example_data.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/example_data.js#L8-L31)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var citiesRef = db.collection("cities");
    
    citiesRef.doc("SF").set({
        name: "San Francisco", state: "CA", country: "USA",
        capital: false, population: 860000,
        regions: ["west_coast", "norcal"] });
    citiesRef.doc("LA").set({
        name: "Los Angeles", state: "CA", country: "USA",
        capital: false, population: 3900000,
        regions: ["west_coast", "socal"] });
    citiesRef.doc("DC").set({
        name: "Washington, D.C.", state: null, country: "USA",
        capital: true, population: 680000,
        regions: ["east_coast"] });
    citiesRef.doc("TOK").set({
        name: "Tokyo", state: null, country: "Japan",
        capital: true, population: 9000000,
        regions: ["kanto", "honshu"] });
    citiesRef.doc("BJ").set({
        name: "Beijing", state: null, country: "China",
        capital: true, population: 21500000,
        regions: ["jingjinji", "hebei"] });
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L403-L424)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let citiesRef = db.collection("cities")
    
    citiesRef.document("SF").setData([
      "name": "San Francisco",
      "state": "CA",
      "country": "USA",
      "capital": false,
      "population": 860000,
      "regions": ["west_coast", "norcal"]
    ])
    citiesRef.document("LA").setData([
      "name": "Los Angeles",
      "state": "CA",
      "country": "USA",
      "capital": false,
      "population": 3900000,
      "regions": ["west_coast", "socal"]
    ])
    citiesRef.document("DC").setData([
      "name": "Washington D.C.",
      "country": "USA",
      "capital": true,
      "population": 680000,
      "regions": ["east_coast"]
    ])
    citiesRef.document("TOK").setData([
      "name": "Tokyo",
      "country": "Japan",
      "capital": true,
      "population": 9000000,
      "regions": ["kanto", "honshu"]
    ])
    citiesRef.document("BJ").setData([
      "name": "Beijing",
      "country": "China",
      "capital": true,
      "population": 21500000,
      "regions": ["jingjinji", "hebei"]
    ])
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L642-L680)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRCollectionReference *citiesRef = [self.db collectionWithPath:@"cities"];
    [[citiesRef documentWithPath:@"SF"] setData:@{
      @"name": @"San Francisco",
      @"state": @"CA",
      @"country": @"USA",
      @"capital": @(NO),
      @"population": @860000,
      @"regions": @[@"west_coast", @"norcal"]
    }];
    [[citiesRef documentWithPath:@"LA"] setData:@{
      @"name": @"Los Angeles",
      @"state": @"CA",
      @"country": @"USA",
      @"capital": @(NO),
      @"population": @3900000,
      @"regions": @[@"west_coast", @"socal"]
    }];
    [[citiesRef documentWithPath:@"DC"] setData:@{
      @"name": @"Washington D.C.",
      @"country": @"USA",
      @"capital": @(YES),
      @"population": @680000,
      @"regions": @[@"east_coast"]
    }];
    [[citiesRef documentWithPath:@"TOK"] setData:@{
      @"name": @"Tokyo",
      @"country": @"Japan",
      @"capital": @(YES),
      @"population": @9000000,
      @"regions": @[@"kanto", @"honshu"]
    }];
    [[citiesRef documentWithPath:@"BJ"] setData:@{
      @"name": @"Beijing",
      @"country": @"China",
      @"capital": @(YES),
      @"population": @21500000,
      @"regions": @[@"jingjinji", @"hebei"]
    }];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L566-L603)

##### Kotlin  
Android
    
    
    val cities = db.collection("cities")
    
    val data1 = hashMapOf(
        "name" to "San Francisco",
        "state" to "CA",
        "country" to "USA",
        "capital" to false,
        "population" to 860000,
        "regions" to listOf("west_coast", "norcal"),
    )
    cities.document("SF").set(data1)
    
    val data2 = hashMapOf(
        "name" to "Los Angeles",
        "state" to "CA",
        "country" to "USA",
        "capital" to false,
        "population" to 3900000,
        "regions" to listOf("west_coast", "socal"),
    )
    cities.document("LA").set(data2)
    
    val data3 = hashMapOf(
        "name" to "Washington D.C.",
        "state" to null,
        "country" to "USA",
        "capital" to true,
        "population" to 680000,
        "regions" to listOf("east_coast"),
    )
    cities.document("DC").set(data3)
    
    val data4 = hashMapOf(
        "name" to "Tokyo",
        "state" to null,
        "country" to "Japan",
        "capital" to true,
        "population" to 9000000,
        "regions" to listOf("kanto", "honshu"),
    )
    cities.document("TOK").set(data4)
    
    val data5 = hashMapOf(
        "name" to "Beijing",
        "state" to null,
        "country" to "China",
        "capital" to true,
        "population" to 21500000,
        "regions" to listOf("jingjinji", "hebei"),
    )
    cities.document("BJ").set(data5)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L722-L772)

##### Java  
Android
    
    
    CollectionReference cities = db.collection("cities");
    
    Map<String, Object> data1 = new HashMap<>();
    data1.put("name", "San Francisco");
    data1.put("state", "CA");
    data1.put("country", "USA");
    data1.put("capital", false);
    data1.put("population", 860000);
    data1.put("regions", Arrays.asList("west_coast", "norcal"));
    cities.document("SF").set(data1);
    
    Map<String, Object> data2 = new HashMap<>();
    data2.put("name", "Los Angeles");
    data2.put("state", "CA");
    data2.put("country", "USA");
    data2.put("capital", false);
    data2.put("population", 3900000);
    data2.put("regions", Arrays.asList("west_coast", "socal"));
    cities.document("LA").set(data2);
    
    Map<String, Object> data3 = new HashMap<>();
    data3.put("name", "Washington D.C.");
    data3.put("state", null);
    data3.put("country", "USA");
    data3.put("capital", true);
    data3.put("population", 680000);
    data3.put("regions", Arrays.asList("east_coast"));
    cities.document("DC").set(data3);
    
    Map<String, Object> data4 = new HashMap<>();
    data4.put("name", "Tokyo");
    data4.put("state", null);
    data4.put("country", "Japan");
    data4.put("capital", true);
    data4.put("population", 9000000);
    data4.put("regions", Arrays.asList("kanto", "honshu"));
    cities.document("TOK").set(data4);
    
    Map<String, Object> data5 = new HashMap<>();
    data5.put("name", "Beijing");
    data5.put("state", null);
    data5.put("country", "China");
    data5.put("capital", true);
    data5.put("population", 21500000);
    data5.put("regions", Arrays.asList("jingjinji", "hebei"));
    cities.document("BJ").set(data5);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L931-L976)

### Dart
    
    
    final cities = db.collection("cities");
    final data1 = <String, dynamic>{
      "name": "San Francisco",
      "state": "CA",
      "country": "USA",
      "capital": false,
      "population": 860000,
      "regions": ["west_coast", "norcal"]
    };
    cities.doc("SF").set(data1);
    
    final data2 = <String, dynamic>{
      "name": "Los Angeles",
      "state": "CA",
      "country": "USA",
      "capital": false,
      "population": 3900000,
      "regions": ["west_coast", "socal"],
    };
    cities.doc("LA").set(data2);
    
    final data3 = <String, dynamic>{
      "name": "Washington D.C.",
      "state": null,
      "country": "USA",
      "capital": true,
      "population": 680000,
      "regions": ["east_coast"]
    };
    cities.doc("DC").set(data3);
    
    final data4 = <String, dynamic>{
      "name": "Tokyo",
      "state": null,
      "country": "Japan",
      "capital": true,
      "population": 9000000,
      "regions": ["kanto", "honshu"]
    };
    cities.doc("TOK").set(data4);
    
    final data5 = <String, dynamic>{
      "name": "Beijing",
      "state": null,
      "country": "China",
      "capital": true,
      "population": 21500000,
      "regions": ["jingjinji", "hebei"],
    };
    cities.doc("BJ").set(data5);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L619-L668)

##### Java
    
    
    CollectionReference cities = db.collection("cities");
    List<ApiFuture<WriteResult>> futures = new ArrayList<>();
    futures.add(
        cities
            .document("SF")
            .set(
                new City(
                    "San Francisco",
                    "CA",
                    "USA",
                    false,
                    860000L,
                    Arrays.asList("west_coast", "norcal"))));
    futures.add(
        cities
            .document("LA")
            .set(
                new City(
                    "Los Angeles",
                    "CA",
                    "USA",
                    false,
                    3900000L,
                    Arrays.asList("west_coast", "socal"))));
    futures.add(
        cities
            .document("DC")
            .set(
                new City(
                    "Washington D.C.", null, "USA", true, 680000L, Arrays.asList("east_coast"))));
    futures.add(
        cities
            .document("TOK")
            .set(
                new City(
                    "Tokyo", null, "Japan", true, 9000000L, Arrays.asList("kanto", "honshu"))));
    futures.add(
        cities
            .document("BJ")
            .set(
                new City(
                    "Beijing",
                    null,
                    "China",
                    true,
                    21500000L,
                    Arrays.asList("jingjinji", "hebei"))));
    // (optional) block on documents successfully added
    ApiFutures.allAsList(futures).get();
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L55-L103)

##### Python
    
    
    class City:
        def __init__(self, name, state, country, capital=False, population=0, regions=[]):
            self.name = name
            self.state = state
            self.country = country
            self.capital = capital
            self.population = population
            self.regions = regions
    
        @staticmethod
        def from_dict(source):
            # ...
    
        def to_dict(self):
            # ...
    
        def __repr__(self):
            return f"City(\
                    name={self.name}, \
                    country={self.country}, \
                    population={self.population}, \
                    capital={self.capital}, \
                    regions={self.regions}\
                )"
    
    
    cities_ref = db.collection("cities")
    cities_ref.document("BJ").set(
        City("Beijing", None, "China", True, 21500000, ["hebei"]).to_dict()
    )
    cities_ref.document("SF").set(
        City(
            "San Francisco", "CA", "USA", False, 860000, ["west_coast", "norcal"]
        ).to_dict()
    )
    cities_ref.document("LA").set(
        City(
            "Los Angeles", "CA", "USA", False, 3900000, ["west_coast", "socal"]
        ).to_dict()
    )
    cities_ref.document("DC").set(
        City("Washington D.C.", None, "USA", True, 680000, ["east_coast"]).to_dict()
    )
    cities_ref.document("TOK").set(
        City("Tokyo", None, "Japan", True, 9000000, ["kanto", "honshu"]).to_dict()
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L152-L171)

##### Python  
(Async)
    
    
    class City:
        def __init__(self, name, state, country, capital=False, population=0, regions=[]):
            self.name = name
            self.state = state
            self.country = country
            self.capital = capital
            self.population = population
            self.regions = regions
    
        @staticmethod
        def from_dict(source):
            # ...
    
        def to_dict(self):
            # ...
    
        def __repr__(self):
            return f"City(\
                    name={self.name}, \
                    country={self.country}, \
                    population={self.population}, \
                    capital={self.capital}, \
                    regions={self.regions}\
                )"
    
    
    cities_ref = db.collection("cities")
    await cities_ref.document("BJ").set(
        City("Beijing", None, "China", True, 21500000, ["hebei"]).to_dict()
    )
    await cities_ref.document("SF").set(
        City(
            "San Francisco", "CA", "USA", False, 860000, ["west_coast", "norcal"]
        ).to_dict()
    )
    await cities_ref.document("LA").set(
        City(
            "Los Angeles", "CA", "USA", False, 3900000, ["west_coast", "socal"]
        ).to_dict()
    )
    await cities_ref.document("DC").set(
        City("Washington D.C.", None, "USA", True, 680000, ["east_coast"]).to_dict()
    )
    await cities_ref.document("TOK").set(
        City("Tokyo", None, "Japan", True, 9000000, ["kanto", "honshu"]).to_dict()
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L148-L167)

##### C++
    
    
    CollectionReference cities = db->Collection("cities");
    
    cities.Document("SF").Set({
        {"name", FieldValue::String("San Francisco")},
        {"state", FieldValue::String("CA")},
        {"country", FieldValue::String("USA")},
        {"capital", FieldValue::Boolean(false)},
        {"population", FieldValue::Integer(860000)},
        {"regions", FieldValue::Array({FieldValue::String("west_coast"),
                                       FieldValue::String("norcal")})},
    });
    
    cities.Document("LA").Set({
        {"name", FieldValue::String("Los Angeles")},
        {"state", FieldValue::String("CA")},
        {"country", FieldValue::String("USA")},
        {"capital", FieldValue::Boolean(false)},
        {"population", FieldValue::Integer(3900000)},
        {"regions", FieldValue::Array({FieldValue::String("west_coast"),
                                       FieldValue::String("socal")})},
    });
    
    cities.Document("DC").Set({
        {"name", FieldValue::String("Washington D.C.")},
        {"state", FieldValue::Null()},
        {"country", FieldValue::String("USA")},
        {"capital", FieldValue::Boolean(true)},
        {"population", FieldValue::Integer(680000)},
        {"regions",
         FieldValue::Array({FieldValue::String("east_coast")})},
    });
    
    cities.Document("TOK").Set({
        {"name", FieldValue::String("Tokyo")},
        {"state", FieldValue::Null()},
        {"country", FieldValue::String("Japan")},
        {"capital", FieldValue::Boolean(true)},
        {"population", FieldValue::Integer(9000000)},
        {"regions", FieldValue::Array({FieldValue::String("kanto"),
                                       FieldValue::String("honshu")})},
    });
    
    cities.Document("BJ").Set({
        {"name", FieldValue::String("Beijing")},
        {"state", FieldValue::Null()},
        {"country", FieldValue::String("China")},
        {"capital", FieldValue::Boolean(true)},
        {"population", FieldValue::Integer(21500000)},
        {"regions", FieldValue::Array({FieldValue::String("jingjinji"),
                                       FieldValue::String("hebei")})},
    });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L429-L479)

##### Node.js
    
    
    const citiesRef = db.collection('cities');
    
    await citiesRef.doc('SF').set({
      name: 'San Francisco', state: 'CA', country: 'USA',
      capital: false, population: 860000,
      regions: ['west_coast', 'norcal']
    });
    await citiesRef.doc('LA').set({
      name: 'Los Angeles', state: 'CA', country: 'USA',
      capital: false, population: 3900000,
      regions: ['west_coast', 'socal']
    });
    await citiesRef.doc('DC').set({
      name: 'Washington, D.C.', state: null, country: 'USA',
      capital: true, population: 680000,
      regions: ['east_coast']
    });
    await citiesRef.doc('TOK').set({
      name: 'Tokyo', state: null, country: 'Japan',
      capital: true, population: 9000000,
      regions: ['kanto', 'honshu']
    });
    await citiesRef.doc('BJ').set({
      name: 'Beijing', state: null, country: 'China',
      capital: true, population: 21500000,
      regions: ['jingjinji', 'hebei']
    });
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L451-L477)

##### Go
    
    
    cities := []struct {
    	id string
    	c  City
    }{
    	{
    		id: "SF",
    		c: City{Name: "San Francisco", State: "CA", Country: "USA",
    			Capital: false, Population: 860000,
    			Regions: []string{"west_coast", "norcal"}},
    	},
    	{
    		id: "LA",
    		c: City{Name: "Los Angeles", State: "CA", Country: "USA",
    			Capital: false, Population: 3900000,
    			Regions: []string{"west_coast", "socal"}},
    	},
    	{
    		id: "DC",
    		c: City{Name: "Washington D.C.", Country: "USA",
    			Capital: true, Population: 680000,
    			Regions: []string{"east_coast"}},
    	},
    	{
    		id: "TOK",
    		c: City{Name: "Tokyo", Country: "Japan",
    			Capital: true, Population: 9000000,
    			Regions: []string{"kanto", "honshu"}},
    	},
    	{
    		id: "BJ",
    		c: City{Name: "Beijing", Country: "China",
    			Capital: true, Population: 21500000,
    			Regions: []string{"jingjinji", "hebei"}},
    	},
    }
    for _, c := range cities {
    	if _, err := client.Collection("cities").Doc(c.id).Set(ctx, c.c); err != nil {
    		return err
    	}
    }
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L29-L68)

##### PHP
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $citiesRef->document('SF')->set([
        'name' => 'San Francisco',
        'state' => 'CA',
        'country' => 'USA',
        'capital' => false,
        'population' => 860000,
        'density' => 18000,
        'regions' => ['west_coast', 'norcal']
    ]);
    $citiesRef->document('LA')->set([
        'name' => 'Los Angeles',
        'state' => 'CA',
        'country' => 'USA',
        'capital' => false,
        'population' => 3900000,
        'density' => 8000,
        'regions' => ['west_coast', 'socal']
    ]);
    $citiesRef->document('DC')->set([
        'name' => 'Washington D.C.',
        'state' => null,
        'country' => 'USA',
        'capital' => true,
        'population' => 680000,
        'density' => 11000,
        'regions' => ['east_coast']
    ]);
    $citiesRef->document('TOK')->set([
        'name' => 'Tokyo',
        'state' => null,
        'country' => 'Japan',
        'capital' => true,
        'population' => 9000000,
        'density' => 16000,
        'regions' => ['kanto', 'honshu']
    ]);
    $citiesRef->document('BJ')->set([
        'name' => 'Beijing',
        'state' => null,
        'country' => 'China',
        'capital' => true,
        'population' => 21500000,
        'density' => 3500,
        'regions' => ['jingjinji', 'hebei']
    ]);
    printf('Added example cities data to the cities collection.' . PHP_EOL);
    
    [query_filter_dataset.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_dataset.php#L40-L86)

##### Unity
    
    
    CollectionReference citiesRef = db.Collection("cities");
    citiesRef.Document("SF").SetAsync(new Dictionary<string, object>(){
        { "Name", "San Francisco" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 860000 },
        { "Regions", new ArrayList{"west_coast", "norcal"} }
    });
    citiesRef.Document("LA").SetAsync(new Dictionary<string, object>(){
        { "Name", "Los Angeles" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 3900000 },
        { "Regions", new ArrayList{"west_coast", "socal"} }
    });
    citiesRef.Document("DC").SetAsync(new Dictionary<string, object>(){
        { "Name", "Washington D.C." },
        { "State", null },
        { "Country", "USA" },
        { "Capital", true },
        { "Population", 680000 },
        { "Regions", new ArrayList{"east_coast"} }
    });
    citiesRef.Document("TOK").SetAsync(new Dictionary<string, object>(){
        { "Name", "Tokyo" },
        { "State", null },
        { "Country", "Japan" },
        { "Capital", true },
        { "Population", 9000000 },
        { "Regions", new ArrayList{"kanto", "honshu"} }
    });
    citiesRef.Document("BJ").SetAsync(new Dictionary<string, object>(){
        { "Name", "Beijing" },
        { "State", null },
        { "Country", "China" },
        { "Capital", true },
        { "Population", 21500000 },
        { "Regions", new ArrayList{"jingjinji", "hebei"} }
    });

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    await citiesRef.Document("SF").SetAsync(new Dictionary<string, object>
    {
        { "Name", "San Francisco" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 860000 },
        { "Density", 18000 },
        { "Regions", new[] {"west_coast", "norcal"} }
    });
    await citiesRef.Document("LA").SetAsync(new Dictionary<string, object>
    {
        { "Name", "Los Angeles" },
        { "State", "CA" },
        { "Country", "USA" },
        { "Capital", false },
        { "Population", 3900000 },
        { "Density", 8300 },
        { "Regions", new[] {"west_coast", "socal"} }
    });
    await citiesRef.Document("DC").SetAsync(new Dictionary<string, object>
    {
        { "Name", "Washington D.C." },
        { "State", null },
        { "Country", "USA" },
        { "Capital", true },
        { "Population", 680000 },
        { "Density", 11300 },
        { "Regions", new[] {"east_coast"} }
    });
    await citiesRef.Document("TOK").SetAsync(new Dictionary<string, object>
    {
        { "Name", "Tokyo" },
        { "State", null },
        { "Country", "Japan" },
        { "Capital", true },
        { "Population", 9000000 },
        { "Density", 16000 },
        { "Regions", new[] {"kanto", "honshu"} }
    });
    await citiesRef.Document("BJ").SetAsync(new Dictionary<string, object>
    {
        { "Name", "Beijing" },
        { "State", null },
        { "Country", "China" },
        { "Capital", true },
        { "Population", 21500000 },
        { "Density", 3500 },
        { "Regions", new[] {"jingjinji", "hebei"} }
    });
    Console.WriteLine("Added example cities data to the cities collection.");
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L54-L105)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    cities_ref.doc("SF").set(
      {
        name:       "San Francisco",
        state:      "CA",
        country:    "USA",
        capital:    false,
        density:    18_000,
        population: 860_000,
        regions:    ["west_coast", "norcal"]
      }
    )
    cities_ref.doc("LA").set(
      {
        name:       "Los Angeles",
        state:      "CA",
        country:    "USA",
        capital:    false,
        density:    8_300,
        population: 3_900_000,
        regions:    ["west_coast", "socal"]
      }
    )
    cities_ref.doc("DC").set(
      {
        name:       "Washington D.C.",
        state:      nil,
        country:    "USA",
        capital:    true,
        density:    11_300,
        population: 680_000,
        regions:    ["east_coast"]
      }
    )
    cities_ref.doc("TOK").set(
      {
        name:       "Tokyo",
        state:      nil,
        country:    "Japan",
        capital:    true,
        density:    16_000,
        population: 9_000_000,
        regions:    ["kanto", "honshu"]
      }
    )
    cities_ref.doc("BJ").set(
      {
        name:       "Beijing",
        state:      nil,
        country:    "China",
        capital:    true,
        density:    3_500,
        population: 21_500_000,
        regions:    ["jingjinji", "hebei"]
      }
    )
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L23-L78)

## Simple queries

The following query returns all cities with state `CA`:

### Web version 9
    
    
    // Create a reference to the cities collection
    import { collection, query, where } from "firebase/firestore";
    const citiesRef = collection(db, "cities");
    
    // Create a query against the collection.
    const q = query(citiesRef, where("state", "==", "CA"));
    
    [simple_queries.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/simple_queries.js#L8-L13)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    // Create a reference to the cities collection
    var citiesRef = db.collection("cities");
    
    // Create a query against the collection.
    var query = citiesRef.where("state", "==", "CA");
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L841-L845)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    // Create a reference to the cities collection
    let citiesRef = db.collection("cities")
    
    // Create a query against the collection.
    let query = citiesRef.whereField("state", isEqualTo: "CA")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L941-L945)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    // Create a reference to the cities collection
    FIRCollectionReference *citiesRef = [self.db collectionWithPath:@"cities"];
    // Create a query against the collection.
    FIRQuery *query = [citiesRef queryWhereField:@"state" isEqualTo:@"CA"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L867-L870)

##### Kotlin  
Android
    
    
    // Create a reference to the cities collection
    val citiesRef = db.collection("cities")
    
    // Create a query against the collection.
    val query = citiesRef.whereEqualTo("state", "CA")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L844-L848)

##### Java  
Android
    
    
    // Create a reference to the cities collection
    CollectionReference citiesRef = db.collection("cities");
    
    // Create a query against the collection.
    Query query = citiesRef.whereEqualTo("state", "CA");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1038-L1042)

### Dart
    
    
    // Create a reference to the cities collection
    final citiesRef = db.collection("cities");
    
    // Create a query against the collection.
    final query = citiesRef.where("state", isEqualTo: "CA");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L674-L678)

##### Java
    
    
    // Create a reference to the cities collection
    CollectionReference cities = db.collection("cities");
    // Create a query against the collection.
    Query query = cities.whereEqualTo("state", "CA");
    // retrieve  query results asynchronously using query.get()
    ApiFuture<QuerySnapshot> querySnapshot = query.get();
    
    for (DocumentSnapshot document : querySnapshot.get().getDocuments()) {
      System.out.println(document.getId());
    }
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L135-L144)

##### Python
    
    
    # Create a reference to the cities collection
    cities_ref = db.collection("cities")
    
    # Create a query against the collection
    query_ref = cities_ref.where(filter=FieldFilter("state", "==", "CA"))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L457-L461)

##### Python  
(Async)
    
    
    # Create a reference to the cities collection
    cities_ref = db.collection("cities")
    
    # Create a query against the collection
    query_ref = cities_ref.where(filter=FieldFilter("state", "==", "CA"))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L451-L455)

##### C++
    
    
    CollectionReference cities_ref = db->Collection("cities");
    // Create a query against the collection.
    Query query_ca =
        cities_ref.WhereEqualTo("state", FieldValue::String("CA"));
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L804-L807)

##### Node.js
    
    
    // Create a reference to the cities collection
    const citiesRef = db.collection('cities');
    
    // Create a query against the collection
    const queryRef = citiesRef.where('state', '==', 'CA');
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L571-L575)

##### Go
    
    
    query := client.Collection("cities").Where("state", "==", "CA")
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L82-L82)

##### PHP
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $query = $citiesRef->where('state', '=', 'CA');
    $snapshot = $query->documents();
    foreach ($snapshot as $document) {
        printf('Document %s returned by query state=CA' . PHP_EOL, $document->id());
    }
    
    [query_filter_eq_string.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_eq_string.php#L40-L45)

##### Unity
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereEqualTo("State", "CA");
    query.GetSnapshotAsync().ContinueWithOnMainThread((querySnapshotTask) =>
    {
        foreach (DocumentSnapshot documentSnapshot in querySnapshotTask.Result.Documents)
        {
            Debug.Log(String.Format("Document {0} returned by query State=CA", documentSnapshot.Id));
        } 
    });

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereEqualTo("State", "CA");
    QuerySnapshot querySnapshot = await query.GetSnapshotAsync();
    foreach (DocumentSnapshot documentSnapshot in querySnapshot.Documents)
    {
        Console.WriteLine("Document {0} returned by query State=CA", documentSnapshot.Id);
    }
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L138-L144)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    
    query = cities_ref.where "state", "=", "CA"
    
    query.get do |city|
      puts "Document #{city.document_id} returned by query state=CA."
    end
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L89-L95)

The following query returns all the capital cities:

### Web version 9
    
    
    import { collection, query, where } from "firebase/firestore";
    const citiesRef = collection(db, "cities");
    
    const q = query(citiesRef, where("capital", "==", true));
    
    [simple_queries_again.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/simple_queries_again.js#L8-L11)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var citiesRef = db.collection("cities");
    
    var query = citiesRef.where("capital", "==", true);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L851-L853)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let capitalCities = db.collection("cities").whereField("capital", isEqualTo: true)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L967-L967)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRQuery *capitalCities =
        [[self.db collectionWithPath:@"cities"] queryWhereField:@"capital" isEqualTo:@YES];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L889-L890)

##### Kotlin  
Android
    
    
    val capitalCities = db.collection("cities").whereEqualTo("capital", true)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L852-L852)

##### Java  
Android
    
    
    Query capitalCities = db.collection("cities").whereEqualTo("capital", true);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1046-L1046)

### Dart
    
    
    final capitalcities =
        db.collection("cities").where("capital", isEqualTo: true);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L684-L685)

##### Java
    
    
    // Create a reference to the cities collection
    CollectionReference cities = db.collection("cities");
    // Create a query against the collection.
    Query query = cities.whereEqualTo("capital", true);
    // retrieve  query results asynchronously using query.get()
    ApiFuture<QuerySnapshot> querySnapshot = query.get();
    
    for (DocumentSnapshot document : querySnapshot.get().getDocuments()) {
      System.out.println(document.getId());
    }
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L114-L123)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(filter=FieldFilter("capital", "==", True))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L470-L472)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(filter=FieldFilter("capital", "==", True))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L464-L466)

##### C++
    
    
    Query capital_cities = db->Collection("cities").WhereEqualTo(
        "capital", FieldValue::Boolean(true));
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L812-L813)

##### Node.js
    
    
    // Create a reference to the cities collection
    const citiesRef = db.collection('cities');
    
    // Create a query against the collection
    const allCapitalsRes = citiesRef.where('capital', '==', true);
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L586-L590)

##### Go
    
    
    query := client.Collection("cities").Where("capital", "==", true)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L75-L75)

##### PHP
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $query = $citiesRef->where('capital', '=', true);
    $snapshot = $query->documents();
    foreach ($snapshot as $document) {
        printf('Document %s returned by query capital=true' . PHP_EOL, $document->id());
    }
    
    [query_filter_eq_boolean.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_eq_boolean.php#L40-L45)

##### Unity
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereEqualTo("Capital", true);
    query.GetSnapshotAsync().ContinueWithOnMainThread((querySnapshotTask) =>
    {
        foreach (DocumentSnapshot documentSnapshot in querySnapshotTask.Result.Documents)
        {
            Debug.Log(String.Format("Document {0} returned by query Capital=true", documentSnapshot.Id));
        } 
    });

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereEqualTo("Capital", true);
    QuerySnapshot querySnapshot = await query.GetSnapshotAsync();
    foreach (DocumentSnapshot documentSnapshot in querySnapshot.Documents)
    {
        Console.WriteLine("Document {0} returned by query Capital=true", documentSnapshot.Id);
    }
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L152-L158)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    
    query = cities_ref.where "capital", "=", true
    
    query.get do |city|
      puts "Document #{city.document_id} returned by query capital=true."
    end
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L105-L111)

### Execute a query

After creating a query object, use the `get()` function to retrieve the results:

### Web version 9
    
    
    import { collection, query, where, getDocs } from "firebase/firestore";
    
    const q = query(collection(db, "cities"), where("capital", "==", true));
    
    const querySnapshot = await getDocs(q);
    querySnapshot.forEach((doc) => {
      // doc.data() is never undefined for query doc snapshots
      console.log(doc.id, " => ", doc.data());
    });
    
    [get_multiple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/get_multiple.js#L8-L16)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    db.collection("cities").where("capital", "==", true)
        .get()
        .then((querySnapshot) => {
            querySnapshot.forEach((doc) => {
                // doc.data() is never undefined for query doc snapshots
                console.log(doc.id, " => ", doc.data());
            });
        })
        .catch((error) => {
            console.log("Error getting documents: ", error);
        });
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L673-L683)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    do {
      let querySnapshot = try await db.collection("cities").whereField("capital", isEqualTo: true)
        .getDocuments()
      for document in querySnapshot.documents {
        print("\(document.documentID) => \(document.data())")
      }
    } catch {
      print("Error getting documents: \(error)")
    }
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L814-L822)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[[self.db collectionWithPath:@"cities"] queryWhereField:@"capital" isEqualTo:@(YES)]
        getDocumentsWithCompletion:^(FIRQuerySnapshot *snapshot, NSError *error) {
          if (error != nil) {
            NSLog(@"Error getting documents: %@", error);
          } else {
            for (FIRDocumentSnapshot *document in snapshot.documents) {
              NSLog(@"%@ => %@", document.documentID, document.data);
            }
          }
        }];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L733-L742)

##### Kotlin  
Android
    
    
    db.collection("cities")
        .whereEqualTo("capital", true)
        .get()
        .addOnSuccessListener { documents ->
            for (document in documents) {
                Log.d(TAG, "${document.id} => ${document.data}")
            }
        }
        .addOnFailureListener { exception ->
            Log.w(TAG, "Error getting documents: ", exception)
        }
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L577-L587)

##### Java  
Android
    
    
    db.collection("cities")
            .whereEqualTo("capital", true)
            .get()
            .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                @Override
                public void onComplete(@NonNull Task<QuerySnapshot> task) {
                    if (task.isSuccessful()) {
                        for (QueryDocumentSnapshot document : task.getResult()) {
                            Log.d(TAG, document.getId() + " => " + document.getData());
                        }
                    } else {
                        Log.d(TAG, "Error getting documents: ", task.getException());
                    }
                }
            });
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L742-L756)

### Dart
    
    
    db.collection("cities").where("capital", isEqualTo: true).get().then(
      (querySnapshot) {
        print("Successfully completed");
        for (var docSnapshot in querySnapshot.docs) {
          print('${docSnapshot.id} => ${docSnapshot.data()}');
        }
      },
      onError: (e) => print("Error completing: $e"),
    );
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L475-L483)

##### Java
    
    
    // asynchronously retrieve multiple documents
    ApiFuture<QuerySnapshot> future = db.collection("cities").whereEqualTo("capital", true).get();
    // future.get() blocks on response
    List<QueryDocumentSnapshot> documents = future.get().getDocuments();
    for (DocumentSnapshot document : documents) {
      System.out.println(document.getId() + " => " + document.toObject(City.class));
    }
    
    [RetrieveDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/RetrieveDataSnippets.java#L151-L157)

##### Python
    
    
    # Note: Use of CollectionRef stream() is prefered to get()
    docs = (
        db.collection("cities")
        .where(filter=FieldFilter("capital", "==", True))
        .stream()
    )
    
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L241-L249)

##### Python  
(Async)
    
    
    # Note: Use of CollectionRef stream() is prefered to get()
    docs = (
        db.collection("cities")
        .where(filter=FieldFilter("capital", "==", True))
        .stream()
    )
    
    async for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L236-L244)

##### C++
    
    
    db->Collection("cities")
        .WhereEqualTo("capital", FieldValue::Boolean(true))
        .Get()
        .OnCompletion([](const Future<QuerySnapshot>& future) {
          if (future.error() == Error::kErrorOk) {
            for (const DocumentSnapshot& document :
                 future.result()->documents()) {
              std::cout << document << std::endl;
            }
          } else {
            std::cout << "Error getting documents: " << future.error_message()
                      << std::endl;
          }
        });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L560-L573)

##### Node.js
    
    
    const citiesRef = db.collection('cities');
    const snapshot = await citiesRef.where('capital', '==', true).get();
    if (snapshot.empty) {
      console.log('No matching documents.');
      return;
    }  
    
    snapshot.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L532-L541)

##### Go
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func multipleDocs(ctx context.Context, client *firestore.Client) error {
    	fmt.Println("All capital cities:")
    	iter := client.Collection("cities").Where("capital", "==", true).Documents(ctx)
    	for {
    		doc, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Println(doc.Data())
    	}
    	return nil
    }
    
    
    [retrieve_data_query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/retrieve_data_query.go#L18-L42)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $query = $citiesRef->where('capital', '=', true);
    $documents = $query->documents();
    foreach ($documents as $document) {
        if ($document->exists()) {
            printf('Document data for document %s:' . PHP_EOL, $document->id());
            print_r($document->data());
            printf(PHP_EOL);
        } else {
            printf('Document %s does not exist!' . PHP_EOL, $document->id());
        }
    }

##### Unity
    
    
    Query capitalQuery = db.Collection("cities").WhereEqualTo("Capital", true);
    capitalQuery.GetSnapshotAsync().ContinueWithOnMainThread(task => {
      QuerySnapshot capitalQuerySnapshot = task.Result;
      foreach (DocumentSnapshot documentSnapshot in capitalQuerySnapshot.Documents) {
        Debug.Log(String.Format("Document data for {0} document:", documentSnapshot.Id));
        Dictionary<string, object> city = documentSnapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city) {
          Debug.Log(String.Format("{0}: {1}", pair.Key, pair.Value));
        }
    
        // Newline to separate entries
        Debug.Log("");
      };
    });

##### C#
    
    
    Query capitalQuery = db.Collection("cities").WhereEqualTo("Capital", true);
    QuerySnapshot capitalQuerySnapshot = await capitalQuery.GetSnapshotAsync();
    foreach (DocumentSnapshot documentSnapshot in capitalQuerySnapshot.Documents)
    {
        Console.WriteLine("Document data for {0} document:", documentSnapshot.Id);
        Dictionary<string, object> city = documentSnapshot.ToDictionary();
        foreach (KeyValuePair<string, object> pair in city)
        {
            Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
        }
        Console.WriteLine("");
    }
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/GetData/Program.cs#L153-L164)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    
    query = cities_ref.where "capital", "=", true
    
    query.get do |city|
      puts "#{city.document_id} data: #{city.data}."
    end
    
    [get_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/get_data.rb#L96-L102)

See [Get Data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data) for more information on retrieving query results. You can also [add a listener](https://docs.cloud.google.com/firestore/native/docs/query-data/listen) to a query to get the current results and listen for future updates.

## Query operators

The `where()` method takes three parameters: a field to filter on, a comparison operator, and a value. Core operations support the following comparison operators:

  * `<` less than
  * `<=` less than or equal to
  * `==` equal to
  * `>` greater than
  * `>=` greater than or equal to
  * `!=` not equal to
  * `array-contains`
  * `array-contains-any`
  * `in`
  * `not-in`

**Note:** For Apple, Android, and Java, the comparison operator is explicitly named in the method.

For example:

### Web version 9
    
    
    const stateQuery = query(citiesRef, where("state", "==", "CA"));
    const populationQuery = query(citiesRef, where("population", "<", 100000));
    const nameQuery = query(citiesRef, where("name", ">=", "San Francisco"));
    
    [example_filters.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/example_filters.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    const stateQuery = citiesRef.where("state", "==", "CA");
    const populationQuery = citiesRef.where("population", "<", 100000);
    const nameQuery = citiesRef.where("name", ">=", "San Francisco");
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L860-L862)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let stateQuery = citiesRef.whereField("state", isEqualTo: "CA")
    let populationQuery = citiesRef.whereField("population", isLessThan: 100000)
    let nameQuery = citiesRef.whereField("name", isGreaterThanOrEqualTo: "San Francisco")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L959-L961)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRQuery *stateQuery = [citiesRef queryWhereField:@"state" isEqualTo:@"CA"];
    FIRQuery *populationQuery = [citiesRef queryWhereField:@"population" isLessThan:@100000];
    FIRQuery *nameQuery = [citiesRef queryWhereField:@"name" isGreaterThanOrEqualTo:@"San Francisco"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L881-L883)

##### Kotlin  
Android
    
    
    val stateQuery = citiesRef.whereEqualTo("state", "CA")
    val populationQuery = citiesRef.whereLessThan("population", 100000)
    val nameQuery = citiesRef.whereGreaterThanOrEqualTo("name", "San Francisco")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L856-L858)

##### Java  
Android
    
    
    Query stateQuery = citiesRef.whereEqualTo("state", "CA");
    Query populationQuery = citiesRef.whereLessThan("population", 100000);
    Query nameQuery = citiesRef.whereGreaterThanOrEqualTo("name", "San Francisco");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1050-L1052)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final stateQuery = citiesRef.where("state", isEqualTo: "CA");
    final populationQuery = citiesRef.where("population", isLessThan: 100000);
    final nameQuery = citiesRef.where("name", isEqualTo: "San Francisco");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L700-L703)

##### Java
    
    
    Query stateQuery = cities.whereEqualTo("state", "CA");
    Query populationQuery = cities.whereLessThan("population", 1000000L);
    Query nameQuery = cities.whereGreaterThanOrEqualTo("name", "San Francisco");
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L159-L161)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    cities_ref.where(filter=FieldFilter("state", "==", "CA"))
    cities_ref.where(filter=FieldFilter("population", "<", 1000000))
    cities_ref.where(filter=FieldFilter("name", ">=", "San Francisco"))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L481-L485)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    cities_ref.where(filter=FieldFilter("state", "==", "CA"))
    cities_ref.where(filter=FieldFilter("population", "<", 1000000))
    cities_ref.where(filter=FieldFilter("name", ">=", "San Francisco"))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L475-L479)

##### C++
    
    
    cities_ref.WhereEqualTo("state", FieldValue::String("CA"));
    cities_ref.WhereLessThan("population", FieldValue::Integer(100000));
    cities_ref.WhereGreaterThanOrEqualTo("name",
                                         FieldValue::String("San Francisco"));
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L853-L856)

##### Node.js
    
    
    const stateQueryRes = await citiesRef.where('state', '==', 'CA').get();
    const populationQueryRes = await citiesRef.where('population', '<', 1000000).get();
    const nameQueryRes = await citiesRef.where('name', '>=', 'San Francisco').get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L594-L596)

##### Go
    
    
    countryQuery := cities.Where("state", "==", "CA")
    popQuery := cities.Where("population", "<", 1000000)
    cityQuery := cities.Where("name", ">=", "San Francisco")
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L90-L92)

##### PHP
    
    
    $stateQuery = $citiesRef->where('state', '=', 'CA');
    $populationQuery = $citiesRef->where('population', '>', 1000000);
    $nameQuery = $citiesRef->where('name', '>=', 'San Francisco');
    
    [query_filter_single_examples.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_single_examples.php#L41-L43)

##### Unity
    
    
    Query stateQuery = citiesRef.WhereEqualTo("State", "CA");
    Query populationQuery = citiesRef.WhereGreaterThan("Population", 1000000);
    Query nameQuery = citiesRef.WhereGreaterThanOrEqualTo("Name", "San Francisco");

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query stateQuery = citiesRef.WhereEqualTo("State", "CA");
    Query populationQuery = citiesRef.WhereGreaterThan("Population", 1000000);
    Query nameQuery = citiesRef.WhereGreaterThanOrEqualTo("Name", "San Francisco");
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L166-L169)

##### Ruby
    
    
    state_query      = cities_ref.where "state", "=", "CA"
    population_query = cities_ref.where "population", ">", 1_000_000
    name_query       = cities_ref.where "name", ">=", "San Francisco"
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L123-L125)

### Not equal (`!=`)

Use the not equal (`!=`) operator to return documents where the given field exists and does not match the comparison value. For example:

### Web version 9
    
    
    const notCapitalQuery = query(citiesRef, where("capital", "!=", false));
    
    [simple_query_not_equal.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/simple_query_not_equal.js#L8-L8)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where("capital", "!=", false);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L866-L866)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let notEqualQuery = citiesRef.whereField("capital", isNotEqualTo: false)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L949-L949)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    query = [citiesRef queryWhereField:@"capital" isNotEqualTo:@NO];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L873-L873)

##### Kotlin  
Android
    
    
    val notCapitalQuery = citiesRef.whereNotEqualTo("capital", false)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L862-L862)

##### Java  
Android
    
    
    Query notCapitalQuery = citiesRef.whereNotEqualTo("capital", false);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1056-L1056)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final notCapitals = citiesRef.where("capital", isNotEqualTo: true);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L709-L710)

##### Java
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Query query = citiesRef.whereNotEqualTo("capital", false);
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L578-L580)

##### Python
    
    
    // Snippet not yet available

##### C++
    
    
    cities_ref.WhereNotEqualTo("capital", FieldValue::Boolean(false));

##### Node.js
    
    
    const capitalNotFalseRes = await citiesRef.where('capital', '!=', false).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L600-L600)

##### Go
    
    
    // Snippet not yet available

##### PHP
    
    
    $stateQuery = $citiesRef->where('capital', '!=', false);
    
    [query_filter_not_eq.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_not_eq.php#L41-L41)

##### Unity
    
    
    Query query = citiesRef.WhereNotEqualTo("capital", false);
    Query query = citiesRef.WhereNotEqualTo("capital", false);

##### C#
    
    
    // Snippet not yet available

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    query = cities_ref.where "capital", "!=", false
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L239-L240)

This query returns every `city` document where the `capital` field exists with a value other than `false` or `null`. This includes `city` documents where the `capital` field value equals `true` or any non-boolean value besides `null`.

This query does not return `city` documents where the `capital` field does not exist. **Not-equal (`!=`) and `not-in` queries exclude documents where the given field does not exist**.

A field exists when it's set to any value, including an empty string (`""`), `null`, and `NaN` (not a number). Note that `null` field values do not match `!=` clauses, because `x != null` evaluates to `undefined`.

**Warning:** A `!=` query clause might match many documents in a collection. To control the number of results returned, use a [limit clause](https://docs.cloud.google.com/firestore/native/docs/query-data/order-limit-data) or [paginate your query](https://docs.cloud.google.com/firestore/native/docs/query-data/query-cursors#paginate_a_query).

#### Standard edition limitations

Note the following limitations for `!=` queries. These limitations apply only to Standard edition:

  * Only documents where the given field exists can match the query.
  * You can't combine `not-in` and `!=` in a compound query.



### Array membership

You can use the `array-contains` operator to filter based on array values. For example:

### Web version 9
    
    
    import { query, where } from "firebase/firestore";  
    const q = query(citiesRef, where("regions", "array-contains", "west_coast"));
    
    [array_contains_filter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/array_contains_filter.js#L8-L9)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where("regions", "array-contains", "west_coast");
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L873-L873)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef
      .whereField("regions", arrayContains: "west_coast")
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L976-L977)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [citiesRef queryWhereField:@"state" arrayContains:@"west_coast"];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L898-L898)

##### Kotlin  
Android
    
    
    val citiesRef = db.collection("cities")
    
    citiesRef.whereArrayContains("regions", "west_coast")
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L868-L870)

##### Java  
Android
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    citiesRef.whereArrayContains("regions", "west_coast");
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1062-L1064)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final westCoastcities =
        citiesRef.where("regions", arrayContains: "west_coast");
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L716-L718)

##### Java
    
    
    CollectionReference citiesRef = db.collection("cities");
    Query westCoastQuery = citiesRef.whereArrayContains("regions", "west_coast");
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L177-L178)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter("regions", "array_contains", "west_coast")
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L256-L260)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter("regions", "array_contains", "west_coast")
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L251-L255)

##### C++
    
    
    CollectionReference cities_ref = db->Collection("cities");
    
    cities_ref.WhereArrayContains("region", FieldValue::String("west_coast"));
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L872-L874)

##### Node.js
    
    
    const westCoastCities = citiesRef.where('regions', 'array-contains',
      'west_coast').get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L613-L614)

##### Go
    
    
    query := cities.Where("regions", "array-contains", "west_coast").Documents(ctx)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L284-L284)

##### PHP
    
    
    $containsQuery = $citiesRef->where('regions', 'array-contains', 'west_coast');
    
    [query_filter_array_contains.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_array_contains.php#L41-L41)

##### Unity
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query arrayContainsQuery = citiesRef.WhereArrayContains("region", "west_coast");

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereArrayContains("Regions", "west_coast");
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L192-L193)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    cities = cities_ref.where "regions", "array-contains", "west_coast"
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L281-L282)

This query returns every `city` document where the `regions` field is an array that contains `west_coast`. If the array has multiple instances of the value you query on, the document is included in the results only once.

You can use at most one `array-contains` clause per disjunction (`or` group). You can't combine `array-contains` with `array-contains-any` in the same disjunction.

### `in`, `not-in`, and `array-contains-any`

Use the `in` operator to combine up to 30 equality (`==`) clauses on the same field with a logical `OR`. An `in` query returns documents where the given field matches any of the comparison values. For example:

### Web version 9
    
    
    import { query, where } from "firebase/firestore";
    
    const q = query(citiesRef, where('country', 'in', ['USA', 'Japan']));
    
    [in_filter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/in_filter.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where('country', 'in', ['USA', 'Japan']);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L888-L888)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let citiesRef = db.collection("cities")
    
    citiesRef.whereField("country", in: ["USA", "Japan"])
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1083-L1085)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRCollectionReference *citiesRef = [self.db collectionWithPath:@"cities"];
    
    [citiesRef queryWhereField:@"country" in:@[@"USA", @"Japan"]];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L985-L987)

##### Kotlin  
Android
    
    
    val citiesRef = db.collection("cities")
    
    citiesRef.whereIn("country", listOf("USA", "Japan"))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L884-L886)

##### Java  
Android
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    citiesRef.whereIn("country", Arrays.asList("USA", "Japan"));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1078-L1080)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final cities = citiesRef.where("country", whereIn: ["USA", "Japan"]);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L724-L725)

##### Java
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Query query = citiesRef.whereIn("country", Arrays.asList("USA", "Japan"));
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L558-L560)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(filter=FieldFilter("country", "in", ["USA", "Japan"]))
    return query
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L908-L911)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(filter=FieldFilter("country", "in", ["USA", "Japan"]))
    return query
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L761-L764)

##### C++
    
    
    CollectionReference cities_ref = db->Collection("cities");
    
    cities_ref.WhereIn("country", std::vector<FieldValue> {
      FieldValue::String("USA"),
      FieldValue::String("Japan")
    });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L886-L891)

##### Node.js
    
    
    const usaOrJapan = await citiesRef.where('country', 'in', ['USA', 'Japan']).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L633-L633)

##### Go
    
    
    cities := client.Collection("cities")
    query := cities.Where("country", "in", []string{"USA", "Japan"}).Documents(ctx)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L263-L264)

##### PHP
    
    
    $rangeQuery = $citiesRef->where('country', 'in', ['USA', 'Japan']);
    
    [query_filter_in.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_in.php#L41-L41)

##### Unity
    
    
    CollectionReference citiesRef = db.Collection("cities");
    List countriesList = new List<object>() {"USA", "Japan"};
    
    Query whereInQuery = citiesRef.WhereIn("country", countriesList);

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereIn("Country", new[] { "USA", "Japan" });
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L220-L221)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    usr_or_japan = cities_ref.where "country", "in", ["USA", "Japan"]
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L211-L212)

This query returns every `city` document where the `country` field is set to `USA` or `Japan`. From the example data, this includes the `SF`, `LA`, `DC`, and `TOK` documents.

#### `not-in`

Use the `not-in` operator to combine up to 10 not equal (`!=`) clauses on the same field with a logical `AND`. A `not-in` query returns documents where the given field exists, is not `null`, and does not match any of the comparison values. For example:

### Web version 9
    
    
    import { query, where } from "firebase/firestore";
    
    const q = query(citiesRef, where('country', 'not-in', ['USA', 'Japan']));
    
    [not_in_filter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/not_in_filter.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where('country', 'not-in', ['USA', 'Japan']);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L892-L892)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef.whereField("country", notIn: ["USA", "Japan"])
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1093-L1093)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [citiesRef queryWhereField:@"country" notIn:@[@"USA", @"Japan"]];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L995-L995)

##### Kotlin  
Android
    
    
    citiesRef.whereNotIn("country", listOf("USA", "Japan"))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/fe812e0c289c579a281d86a1c54be5c798fe6a4c/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L855-L855)

##### Java  
Android
    
    
    citiesRef.whereNotIn("country", Arrays.asList("USA", "Japan"));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/fe812e0c289c579a281d86a1c54be5c798fe6a4c/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1056-L1056)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final cities = citiesRef.where("country", whereNotIn: ["USA", "Japan"]);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L731-L732)

##### Java
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Query query = citiesRef.whereNotIn("country", Arrays.asList("USA", "Japan"));
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L587-L589)

##### Python
    
    
    // Snippet not yet available

##### C++
    
    
    cities_ref.WhereNotIn("country", std::vector<FieldValue> {
      FieldValue::String("USA"),
      FieldValue::String("Japan")
    });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L895-L898)

##### Node.js
    
    
    const notUsaOrJapan = await citiesRef.where('country', 'not-in', ['USA', 'Japan']).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L637-L637)

##### Go
    
    
    // Snippet not yet available

##### PHP
    
    
    $stateQuery = $citiesRef->where(
        'country',
        \Google\Cloud\Firestore\V1\StructuredQuery\FieldFilter\Operator::NOT_IN,
        ['USA', 'Japan']
    );
    
    [query_filter_not_in.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_not_in.php#L41-L45)

##### Unity
    
    
    Query query = citiesRef.WhereNotIn(new FieldPath("country"), new List<string>{"USA", "Japan"});
    Query query = citiesRef.WhereNotIn("country", new List<object>(){"USA", "Japan"});

##### C#
    
    
    // Snippet not yet available

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    usr_or_japan = cities_ref.where "country", "not_in", ["USA", "Japan"]
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L253-L254)

This query returns every `city` document where the `country` field exists and is not set to `USA`, `Japan`, or `null`. From the example data, this includes the `London` and `Hong Kong` documents.

**`not-in` queries exclude documents where the given field does not exist.** A field exists when it's set to any value, including an empty string (`""`), `null`, and `NaN` (not a number). Note that `x != null` evaluates to `undefined`. A `not-in` query with `null` as one of the comparison values does not match any documents.

**Warning:** A `not-in` query clause might match many documents in a collection. To control the number of results returned, use a [limit clause](https://docs.cloud.google.com/firestore/native/docs/query-data/order-limit-data) or [paginate your query](https://docs.cloud.google.com/firestore/native/docs/query-data/query-cursors#paginate_a_query).

#### `array-contains-any`

Use the `array-contains-any` operator to combine up to 30 `array-contains` clauses on the same field with a logical `OR`. An `array-contains-any` query returns documents where the given field is an array that contains one or more of the comparison values:

### Web version 9
    
    
    import { query, where } from "firebase/firestore";  
    
    const q = query(citiesRef, 
      where('regions', 'array-contains-any', [['west_coast'], ['east_coast']]));
    
    [array_contains_any_filter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/array_contains_any_filter.js#L8-L11)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where('regions', 'array-contains-any',
        [['west_coast'], ['east_coast']]);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L880-L881)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let citiesRef = db.collection("cities")
    citiesRef.whereField("regions", arrayContainsAny: ["west_coast", "east_coast"])
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1076-L1077)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRCollectionReference *citiesRef = [self.db collectionWithPath:@"cities"];
    
    [citiesRef queryWhereField:@"regions" arrayContainsAny:@[@"west_coast", @"east_coast"]];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L977-L979)

##### Kotlin  
Android
    
    
    val citiesRef = db.collection("cities")
    
    citiesRef.whereArrayContainsAny("regions", listOf("west_coast", "east_coast"))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L876-L878)

##### Java  
Android
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    citiesRef.whereArrayContainsAny("regions", Arrays.asList("west_coast", "east_coast"));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1070-L1072)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final cities = citiesRef
        .where("regions", arrayContainsAny: ["west_coast", "east_coast"]);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L738-L740)

##### Java
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Query query =
        citiesRef.whereArrayContainsAny("regions", Arrays.asList("west_coast", "east_coast"));
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L548-L551)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter(
            "regions", "array_contains_any", ["west_coast", "east_coast"]
        )
    )
    return query
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L895-L902)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter(
            "regions", "array_contains_any", ["west_coast", "east_coast"]
        )
    )
    return query
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L748-L755)

##### C++
    
    
    CollectionReference cities_ref = db->Collection("cities");
    
    cities_ref.WhereArrayContainsAny("region", std::vector<FieldValue> {
      FieldValue::String("west_coast"),
      FieldValue::String("east_coast")
    });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L909-L914)

##### Node.js
    
    
    const coastalCities = await citiesRef.where('regions', 'array-contains-any',
        ['west_coast', 'east_coast']).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L623-L624)

##### Go
    
    
    cities := client.Collection("cities")
    query := cities.Where("regions", "array-contains-any", []string{"west_coast", "east_coast"}).Documents(ctx)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L293-L294)

##### PHP
    
    
    $containsQuery = $citiesRef->where('regions', 'array-contains-any', ['west_coast', 'east_coast']);
    
    [query_filter_array_contains_any.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_array_contains_any.php#L41-L41)

##### Unity
    
    
    Query query = citiesRef.WhereArrayContainsAny(
                             "regions",
                             new List<object>()
                             {
                                new List<object>(){"west_coast"},
                                new List<object>(){"east_coast"}});

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereArrayContainsAny("Regions", new[] { "west_coast", "east_coast" });
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L206-L207)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    costal_cities = cities_ref.where "regions", "array-contains-any", ["west_coast", "east_coast"]
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L267-L268)

This query returns every city document where the `regions` field is an array that contains `west_coast` or `east_coast`. From the example data, this includes the `SF`, `LA`, and `DC` documents.

Results from `array-contains-any` are de-duped. Even if a document's array field matches more than one of the comparison values, the result set includes that document only once.

`array-contains-any` always filters by the array data type. For example, the query above would not return a city document where instead of an array, the `regions` field is the string `west_coast`.

You can use an array value as a comparison value for `in`, but unlike `array-contains-any`, the clause matches for an exact match of array length, order, and values. For example:

### Web version 9
    
    
    import { query, where } from "firebase/firestore";  
    
    const q = query(citiesRef, where('regions', 'in', [['west_coast'], ['east_coast']]));
    
    [in_filter_with_array.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/in_filter_with_array.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where('regions', 'in',
        [['west_coast'], ['east_coast']]);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L896-L897)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef.whereField("regions", in: [["west_coast"], ["east_coast"]])
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1089-L1089)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [citiesRef queryWhereField:@"regions" in:@[@[@"west_coast"], @[@"east_coast"]]];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L991-L991)

##### Kotlin  
Android
    
    
    citiesRef.whereIn("regions", listOf(arrayOf("west_coast"), arrayOf("east_coast")))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L894-L894)

##### Java  
Android
    
    
    citiesRef.whereIn("regions", Arrays.asList(new String[]{"west_coast"}, new String[]{"east_coast"}));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1088-L1088)

### Dart
    
    
    final citiesRef = db.collection("cities");
    final cities = citiesRef.where("regions", whereIn: [
      ["west_coast"],
      ["east_coast"]
    ]);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L746-L750)

##### Java
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Query query =
        citiesRef.whereIn(
            "regions", Arrays.asList(Arrays.asList("west_coast"), Arrays.asList("east_coast")));
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L567-L571)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter("regions", "in", [["west_coast"], ["east_coast"]])
    )
    return query
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L917-L922)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter("regions", "in", [["west_coast"], ["east_coast"]])
    )
    return query
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L770-L775)

##### C++
    
    
    cities_ref.WhereIn("region", std::vector<FieldValue> {
      FieldValue::String("west_coast"),
      FieldValue::String("east_coast")
    });
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L918-L921)

##### Node.js
    
    
    const exactlyOneCoast = await citiesRef.where('regions', 'in',
        [['west_coast', 'east_coast']]).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L641-L642)

##### Go
    
    
    cities := client.Collection("cities")
    query := cities.Where("regions", "in", [][]string{{"west_coast"}, {"east_coast"}}).Documents(ctx)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L273-L274)

##### PHP
    
    
    $rangeQuery = $citiesRef->where('regions', 'in', [['west_coast'], ['east_coast']]);
    
    [query_filter_in_with_array.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_in_with_array.php#L41-L41)

##### Unity
    
    
    Query query = citiesRef.WhereIn(new FieldPath("regions"), new List<string>{"west_coast", "east_coast"});

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereIn("Regions",
        new[] { new[] { "west_coast" }, new[] { "east_coast" } });
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L234-L236)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    exactly_one_cost = cities_ref.where "regions", "in", [["west_coast"], ["east_coast"]]
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L225-L226)

This query returns every city document where the `regions` field is an array that contains exactly one element of either `west_coast` or `east_coast`. From the example data, only the `DC` document qualifies with its `regions` field of `["east_coast"]`. The `SF` document, however, does not match because its `regions` field is `["west_coast", "norcal"]`.

#### Standard edition limitations

Note the following limitations for `in`, `not-in`, and `array-contains-any`. These limitations apply only to Standard edition:

  * Firestore provides support for logical `OR` queries through the `or`, `in`, and `array-contains-any` operators. These queries are limited to 30 disjunctions based on the query's disjunctive normal form. This limit is fixed and cannot be adjusted.
  * You can use at most one `array-contains` clause per disjunction (`or` group). You can't combine `array-contains` with `array-contains-any` in the same disjunction.
  * You can't combine `not-in` with not equals `!=`.
  * `not-in` supports up to 10 comparison values.



## Compound (`AND`) queries

You can combine constraints with a logical `AND` by chaining multiple equality operators (`==` or `array-contains`). However, you must create a [composite index](https://docs.cloud.google.com/firestore/native/docs/query-data/indexing) to combine equality operators with the inequality operators, `<`, `<=`, `>`, and `!=`.

### Web version 9
    
    
    import { query, where } from "firebase/firestore";  
    
    const q1 = query(citiesRef, where("state", "==", "CO"), where("name", "==", "Denver"));
    const q2 = query(citiesRef, where("state", "==", "CA"), where("population", "<", 1000000));
    
    [chain_filters.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/chain_filters.js#L8-L11)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    const q1 = citiesRef.where("state", "==", "CO").where("name", "==", "Denver");
    const q2 = citiesRef.where("state", "==", "CA").where("population", "<", 1000000);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L904-L905)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef
      .whereField("state", isEqualTo: "CO")
      .whereField("name", isEqualTo: "Denver")
    citiesRef
      .whereField("state", isEqualTo: "CA")
      .whereField("population", isLessThan: 1000000)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L985-L990)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[citiesRef queryWhereField:@"state" isEqualTo:@"CO"]
        queryWhereField:@"name" isGreaterThanOrEqualTo:@"Denver"];
    [[citiesRef queryWhereField:@"state" isEqualTo:@"CA"]
        queryWhereField:@"population" isLessThan:@1000000];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L905-L908)

##### Kotlin  
Android
    
    
    citiesRef.whereEqualTo("state", "CO").whereEqualTo("name", "Denver")
    citiesRef.whereEqualTo("state", "CA").whereLessThan("population", 1000000)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L902-L903)

##### Java  
Android
    
    
    citiesRef.whereEqualTo("state", "CO").whereEqualTo("name", "Denver");
    citiesRef.whereEqualTo("state", "CA").whereLessThan("population", 1000000);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1096-L1097)

### Dart
    
    
    final citiesRef = db.collection("cities");
    citiesRef
        .where("state", isEqualTo: "CO")
        .where("name", isEqualTo: "Denver");
    citiesRef
        .where("state", isEqualTo: "CA")
        .where("population", isLessThan: 1000000);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L756-L762)

##### Java
    
    
    Query chainedQuery1 = cities.whereEqualTo("state", "CO").whereEqualTo("name", "Denver");
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L194-L194)

##### Python
    
    
    cities_ref = db.collection("cities")
    
    denver_query = cities_ref.where(filter=FieldFilter("state", "==", "CO")).where(
        filter=FieldFilter("name", "==", "Denver")
    )
    large_us_cities_query = cities_ref.where(
        filter=FieldFilter("state", "==", "CA")
    ).where(filter=FieldFilter("population", ">", 1000000))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L494-L501)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    
    denver_query = cities_ref.where(filter=FieldFilter("state", "==", "CO")).where(
        filter=FieldFilter("name", "==", "Denver")
    )
    large_us_cities_query = cities_ref.where(
        filter=FieldFilter("state", "==", "CA")
    ).where(filter=FieldFilter("population", ">", 1000000))
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L486-L493)

##### C++
    
    
    cities_ref.WhereEqualTo("state", FieldValue::String("CO"))
        .WhereEqualTo("name", FieldValue::String("Denver"));
    cities_ref.WhereEqualTo("state", FieldValue::String("CA"))
        .WhereLessThan("population", FieldValue::Integer(1000000));
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1013-L1016)

##### Node.js
    
    
    citiesRef.where('state', '==', 'CO').where('name', '==', 'Denver');
    citiesRef.where('state', '==', 'CA').where('population', '<', 1000000);
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L719-L719)

##### Go
    
    
    denverQuery := cities.Where("name", "==", "Denver").Where("state", "==", "CO")
    caliQuery := cities.Where("state", "==", "CA").Where("population", "<=", 1000000)
    query := cities.Where("country", "==", "USA").Where("population", ">", 5000000)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query.go#L115-L115)

##### PHP
    
    
    $chainedQuery = $citiesRef
        ->where('state', '=', 'CA')
        ->where('name', '=', 'San Francisco');
    
    [query_filter_compound_multi_eq.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_filter_compound_multi_eq.php#L41-L43)

##### Unity
    
    
    Query chainedQuery = citiesRef
        .WhereEqualTo("State", "CA")
        .WhereEqualTo("Name", "San Francisco");

##### C#
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query chainedQuery = citiesRef
        .WhereEqualTo("State", "CA")
        .WhereEqualTo("Name", "San Francisco");
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L275-L278)

##### Ruby
    
    
    chained_query = cities_ref.where("state", "=", "CA").where("name", "=", "San Francisco")
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L145-L145)

## `OR` queries

You can combine constraints with a logical `OR`. For example:

### Web version 9
    
    
    const q = query(citiesRef,
      or(where('capital', '==', true),
         where('population', '>=', 1000000)
      )
    );
      

### Web version 8

Not available.

##### Swift
    
    
    let query = db.collection("cities").whereFilter(Filter.orFilter([
                    Filter.whereField("capital", isEqualTo: true),
                    Filter.whereField("population", isGreaterThanOrEqualTo: 1000000);
                ]))
      

##### Objective-C
    
    
      FIRCollectionReference *collection = [self.db collectionWithPath:@"cities"];
      FIRQuery *query = [collection queryWhereFilter:[FIRFilter orFilterWithFilters:@[
          [FIRFilter filterWhereField:@"capital" isEqualTo:@YES],
          [FIRFilter filterWhereField:@"population" isGreaterThanOrEqualTo:@1000000]
      ]]];
      

##### Kotlin  
Android
    
    
    val query = collection.where(Filter.or(
            Filter.equalTo("capital", true),
            Filter.greaterThanOrEqualTo("population", 1000000)
    ))
      

##### Java  
Android
    
    
    Query query = collection.where(Filter.or(
            Filter.equalTo("capital", true),
            Filter.greaterThanOrEqualTo("population", 1000000)
    ));
      

### Dart
    
    
    var query = db.collection("cities").where(
          Filter.or(
            Filter("capital", isEqualTo: true),
            Filter("population", isGreaterThan: 1000000),
          ),
        );
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L845-L850)

##### Java

Snippet not available.

##### Python
    
    
    from google.cloud.firestore_v1.base_query import FieldFilter, Or
    
    col_ref = client.collection("cities")
    # Execute the query
    query = col_ref.where(
        filter=Or(
            [
                FieldFilter("capital", "==", True),
                FieldFilter("population", ">", 1_000_000),
            ]
        )
    )
    docs = query.stream()
    
    [query_filter_or.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/query_filter_or.py#L18-L30)

##### Python  
(Async)

Snippet not available.

##### C++

Snippet not available.

##### Node.js
    
    
    const bigCities = await citiesRef
      .where(
        Filter.or(
          Filter.where('capital', '==', true),
          Filter.where('population', '>=', 1000000)
        )
      )
      .get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L659-L666)

##### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	firestore "cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func queryFilterOr(w io.Writer, projectId string) error {
    	// Instantiate a client
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, projectId)
    	if err != nil {
    		return err
    	}
    	// always be sure to close the client to release resources
    	defer client.Close()
    
    	q1 := firestore.[PropertyFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PropertyFilter){
    		Path:     "birthYear",
    		Operator: "==",
    		Value:    1906,
    	}
    
    	q2 := firestore.[PropertyFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PropertyFilter){
    		Path:     "birthYear",
    		Operator: "==",
    		Value:    1815,
    	}
    
    	orFilter := firestore.[OrFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_OrFilter){
    		Filters: []firestore.[EntityFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_EntityFilter){q1, q2},
    	}
    
    	orQuery := client.Collection("users").[WhereEntity](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Query_WhereEntity)(orFilter)
    	it := orQuery.Documents(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprint(w, "Individual documents:\n")
    	for {
    		doc, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("documents iterator: %w", err)
    		}
    		fmt.Fprintf(w, "%s: %s", doc.[Ref](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_Ref).ID, doc.Data()["birthYear"])
    	}
    
    	return nil
    }
    
    
    [query_filter_or.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/query_filter_or.go#L18-L73)

##### PHP

Snippet not available.

##### Unity
    
    
    Query query = citiesRef.Where(Filter.Or(
            Filter.EqualTo("State", "CA"),
            Filter.GreaterThanOrEqualTo("population", 1000000)
    ));
    query.GetSnapshotAsync().ContinueWithOnMainThread((querySnapshotTask) =>
    {
        foreach (DocumentSnapshot documentSnapshot in querySnapshotTask.Result.Documents)
        {
            Debug.Log(String.Format("Document {0} returned by query State=CA or population >= {1}", documentSnapshot.Id, 1000000));
        } 
    });

##### C#

Snippet not available.

##### Ruby

Snippet not available.

Firestore uses your composite indexes to serve `OR` queries. If your indexes do not support the query, Firestore [suggests additional indexes for your database](https://docs.cloud.google.com/firestore/native/docs/query-data/indexing#create_a_missing_index_through_an_error_message).

You can combine `OR` queries with compound queries to filter on combinations of `OR` and `AND` operations. For example:

### Web version 9
    
    
    const q = query(collection(db, "cities"), and(
      where('state', '==', 'CA'),   
      or(
        where('capital', '==', true),
        where('population', '>=', 1000000)
      )
    ));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore-next/test.firestore.js#L1125-L1131)

### Web version 8

Not available.

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let query = db.collection("cities").whereFilter(Filter.andFilter([
      Filter.whereField("state", isEqualTo: "CA"),
      Filter.orFilter([
        Filter.whereField("capital", isEqualTo: true),
        Filter.whereField("population", isGreaterOrEqualTo: 1000000)
      ])
    ]))
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1372-L1378)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRCollectionReference *collection = [self.db collectionWithPath:@"cities"];
    FIRQuery *query = [collection queryWhereFilter:[FIRFilter andFilterWithFilters:@[
      [FIRFilter filterWhereField:@"state" isEqualTo:@"CA"],
      [FIRFilter orFilterWithFilters:@[
        [FIRFilter filterWhereField:@"capital" isEqualTo:@YES],
        [FIRFilter filterWhereField:@"population" isGreaterThanOrEqualTo:@1000000]
      ]]
    ]]];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L1296-L1303)

##### Kotlin  
Android
    
    
    val query = collection.where(Filter.and(
        Filter.equalTo("state", "CA"),
        Filter.or(
            Filter.equalTo("capital", true),
            Filter.greaterThanOrEqualTo("population", 1000000)
        )
    ))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1149-L1155)

##### Java  
Android
    
    
    Query query = collection.where(Filter.and(
        Filter.equalTo("state", "CA"),
        Filter.or(
            Filter.equalTo("capital", true),
            Filter.greaterThanOrEqualTo("population", 1000000)
        )
    ));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1377-L1383)

### Dart
    
    
    var query = db.collection("cities").where(
          Filter.and(
            Filter("state", isEqualTo: "CA"),
            Filter.or(
              Filter("capital", isEqualTo: true),
              Filter("population", isGreaterThan: 1000000),
            ),
          ),
        );
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L856-L864)

##### Java

Snippet not available.

##### Python

Snippet not available.

##### Python  
(Async)

Snippet not available.

##### C++

Snippet not available.

##### Node.js
    
    
    const bigCitiesInCalifornia = await citiesRef
      .where('state', '==', 'CA')
      .where(
        Filter.or(
          Filter.where('capital', '==', true),
          Filter.where('population', '>=', 1000000)
        )
      )
      .get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L670-L678)

##### Go

Snippet not available.

##### PHP

Snippet not available.

##### Unity
    
    
    Query query = citiesRef.Where(Filter.And(
        Filter.EqualTo("state", "CA"),
        Filter.Or(
            Filter.EqualTo("capital", true),
            Filter.GreaterThanOrEqualTo("population", 1000000)
        )
    ));

##### C#

Snippet not available.

##### Ruby

Snippet not available.

### Standard edition limitations

Note the following limitations for `or` queries. These limitations apply only to Standard edition:

  * Firestore limits a query to a maximum of 30 disjunctions based on the query's disjunctive normal form. This limit is fixed and cannot be adjusted. You are more likely to reach this limit when performing an `AND` of multiple `OR` groups.

  * You can't combine `not-in` with `in`, `array-contains-any`, or `or` in the same query.




For a full description of limitations, see Query limitations.

## Collection group queries

A collection group consists of all collections with the same ID. By default, queries retrieve results from a single collection in your database. Use a collection group query to retrieve documents from a collection group instead of from a single collection.

For example, you can create a `landmarks` collection group by adding a landmarks subcollection to each city:

### Web version 9
    
    
    import { collection, addDoc } from "firebase/firestore";  
    
    const citiesRef = collection(db, 'cities');
    
    await Promise.all([
        addDoc(collection(citiesRef, 'SF', 'landmarks'), {
            name: 'Golden Gate Bridge',
            type: 'bridge'
        }),
        addDoc(collection(citiesRef, 'SF', 'landmarks'), {
            name: 'Legion of Honor',
            type: 'museum'
        }),
        addDoc(collection(citiesRef, 'LA', 'landmarks'), {
            name: 'Griffith Park',
            type: 'park'
        }),
        addDoc(collection(citiesRef, 'LA', 'landmarks'), {
            name: 'The Getty',
            type: 'museum'
        }),
        addDoc(collection(citiesRef, 'DC', 'landmarks'), {
            name: 'Lincoln Memorial',
            type: 'memorial'
        }),
        addDoc(collection(citiesRef, 'DC', 'landmarks'), {
            name: 'National Air and Space Museum',
            type: 'museum'
        }),
        addDoc(collection(citiesRef, 'TOK', 'landmarks'), {
            name: 'Ueno Park',
            type: 'park'
        }),
        addDoc(collection(citiesRef, 'TOK', 'landmarks'), {
            name: 'National Museum of Nature and Science',
            type: 'museum'
        }),
        addDoc(collection(citiesRef, 'BJ', 'landmarks'), {
            name: 'Jingshan Park',
            type: 'park'
        }),
        addDoc(collection(citiesRef, 'BJ', 'landmarks'), {
            name: 'Beijing Ancient Observatory',
            type: 'museum'
        })
    ]);
    
    [fs_collection_group_query_data_setup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/fs_collection_group_query_data_setup.js#L8-L53)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var citiesRef = db.collection('cities');
    
    var landmarks = Promise.all([
        citiesRef.doc('SF').collection('landmarks').doc().set({
            name: 'Golden Gate Bridge',
            type: 'bridge'
        }),
        citiesRef.doc('SF').collection('landmarks').doc().set({
            name: 'Legion of Honor',
            type: 'museum'
        }),
        citiesRef.doc('LA').collection('landmarks').doc().set({
            name: 'Griffith Park',
            type: 'park'
        }),
        citiesRef.doc('LA').collection('landmarks').doc().set({
            name: 'The Getty',
            type: 'museum'
        }),
        citiesRef.doc('DC').collection('landmarks').doc().set({
            name: 'Lincoln Memorial',
            type: 'memorial'
        }),
        citiesRef.doc('DC').collection('landmarks').doc().set({
            name: 'National Air and Space Museum',
            type: 'museum'
        }),
        citiesRef.doc('TOK').collection('landmarks').doc().set({
            name: 'Ueno Park',
            type: 'park'
        }),
        citiesRef.doc('TOK').collection('landmarks').doc().set({
            name: 'National Museum of Nature and Science',
            type: 'museum'
        }),
        citiesRef.doc('BJ').collection('landmarks').doc().set({
            name: 'Jingshan Park',
            type: 'park'
        }),
        citiesRef.doc('BJ').collection('landmarks').doc().set({
            name: 'Beijing Ancient Observatory',
            type: 'museum'
        })
    ]);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L1040-L1083)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    let citiesRef = db.collection("cities")
    
    var data = ["name": "Golden Gate Bridge", "type": "bridge"]
    citiesRef.document("SF").collection("landmarks").addDocument(data: data)
    
    data = ["name": "Legion of Honor", "type": "museum"]
    citiesRef.document("SF").collection("landmarks").addDocument(data: data)
    
    data = ["name": "Griffith Park", "type": "park"]
    citiesRef.document("LA").collection("landmarks").addDocument(data: data)
    
    data = ["name": "The Getty", "type": "museum"]
    citiesRef.document("LA").collection("landmarks").addDocument(data: data)
    
    data = ["name": "Lincoln Memorial", "type": "memorial"]
    citiesRef.document("DC").collection("landmarks").addDocument(data: data)
    
    data = ["name": "National Air and Space Museum", "type": "museum"]
    citiesRef.document("DC").collection("landmarks").addDocument(data: data)
    
    data = ["name": "Ueno Park", "type": "park"]
    citiesRef.document("TOK").collection("landmarks").addDocument(data: data)
    
    data = ["name": "National Museum of Nature and Science", "type": "museum"]
    citiesRef.document("TOK").collection("landmarks").addDocument(data: data)
    
    data = ["name": "Jingshan Park", "type": "park"]
    citiesRef.document("BJ").collection("landmarks").addDocument(data: data)
    
    data = ["name": "Beijing Ancient Observatory", "type": "museum"]
    citiesRef.document("BJ").collection("landmarks").addDocument(data: data)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L686-L716)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    FIRCollectionReference *citiesRef = [self.db collectionWithPath:@"cities"];
    
    NSDictionary *data = @{@"name": @"Golden Gate Bridge", @"type": @"bridge"};
    [[[citiesRef documentWithPath:@"SF"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"Legion of Honor", @"type": @"museum"};
    [[[citiesRef documentWithPath:@"SF"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"Griffith Park", @"type": @"park"};
    [[[citiesRef documentWithPath:@"LA"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"The Getty", @"type": @"museum"};
    [[[citiesRef documentWithPath:@"LA"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"Lincoln Memorial", @"type": @"memorial"};
    [[[citiesRef documentWithPath:@"DC"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"National Air and Space Museum", @"type": @"museum"};
    [[[citiesRef documentWithPath:@"DC"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"Ueno Park", @"type": @"park"};
    [[[citiesRef documentWithPath:@"TOK"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"National Museum of Nature and Science", @"type": @"museum"};
    [[[citiesRef documentWithPath:@"TOK"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"Jingshan Park", @"type": @"park"};
    [[[citiesRef documentWithPath:@"BJ"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    data = @{@"name": @"Beijing Ancient Observatory", @"type": @"museum"};
    [[[citiesRef documentWithPath:@"BJ"] collectionWithPath:@"landmarks"] addDocumentWithData:data];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L609-L639)

##### Kotlin  
Android
    
    
    val citiesRef = db.collection("cities")
    
    val ggbData = mapOf(
        "name" to "Golden Gate Bridge",
        "type" to "bridge",
    )
    citiesRef.document("SF").collection("landmarks").add(ggbData)
    
    val lohData = mapOf(
        "name" to "Legion of Honor",
        "type" to "museum",
    )
    citiesRef.document("SF").collection("landmarks").add(lohData)
    
    val gpData = mapOf(
        "name" to "Griffth Park",
        "type" to "park",
    )
    citiesRef.document("LA").collection("landmarks").add(gpData)
    
    val tgData = mapOf(
        "name" to "The Getty",
        "type" to "museum",
    )
    citiesRef.document("LA").collection("landmarks").add(tgData)
    
    val lmData = mapOf(
        "name" to "Lincoln Memorial",
        "type" to "memorial",
    )
    citiesRef.document("DC").collection("landmarks").add(lmData)
    
    val nasaData = mapOf(
        "name" to "National Air and Space Museum",
        "type" to "museum",
    )
    citiesRef.document("DC").collection("landmarks").add(nasaData)
    
    val upData = mapOf(
        "name" to "Ueno Park",
        "type" to "park",
    )
    citiesRef.document("TOK").collection("landmarks").add(upData)
    
    val nmData = mapOf(
        "name" to "National Musuem of Nature and Science",
        "type" to "museum",
    )
    citiesRef.document("TOK").collection("landmarks").add(nmData)
    
    val jpData = mapOf(
        "name" to "Jingshan Park",
        "type" to "park",
    )
    citiesRef.document("BJ").collection("landmarks").add(jpData)
    
    val baoData = mapOf(
        "name" to "Beijing Ancient Observatory",
        "type" to "musuem",
    )
    citiesRef.document("BJ").collection("landmarks").add(baoData)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L778-L838)

##### Java  
Android
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Map<String, Object> ggbData = new HashMap<>();
    ggbData.put("name", "Golden Gate Bridge");
    ggbData.put("type", "bridge");
    citiesRef.document("SF").collection("landmarks").add(ggbData);
    
    Map<String, Object> lohData = new HashMap<>();
    lohData.put("name", "Legion of Honor");
    lohData.put("type", "museum");
    citiesRef.document("SF").collection("landmarks").add(lohData);
    
    Map<String, Object> gpData = new HashMap<>();
    gpData.put("name", "Griffith Park");
    gpData.put("type", "park");
    citiesRef.document("LA").collection("landmarks").add(gpData);
    
    Map<String, Object> tgData = new HashMap<>();
    tgData.put("name", "The Getty");
    tgData.put("type", "museum");
    citiesRef.document("LA").collection("landmarks").add(tgData);
    
    Map<String, Object> lmData = new HashMap<>();
    lmData.put("name", "Lincoln Memorial");
    lmData.put("type", "memorial");
    citiesRef.document("DC").collection("landmarks").add(lmData);
    
    Map<String, Object> nasaData = new HashMap<>();
    nasaData.put("name", "National Air and Space Museum");
    nasaData.put("type", "museum");
    citiesRef.document("DC").collection("landmarks").add(nasaData);
    
    Map<String, Object> upData = new HashMap<>();
    upData.put("name", "Ueno Park");
    upData.put("type", "park");
    citiesRef.document("TOK").collection("landmarks").add(upData);
    
    Map<String, Object> nmData = new HashMap<>();
    nmData.put("name", "National Museum of Nature and Science");
    nmData.put("type", "museum");
    citiesRef.document("TOK").collection("landmarks").add(nmData);
    
    Map<String, Object> jpData = new HashMap<>();
    jpData.put("name", "Jingshan Park");
    jpData.put("type", "park");
    citiesRef.document("BJ").collection("landmarks").add(jpData);
    
    Map<String, Object> baoData = new HashMap<>();
    baoData.put("name", "Beijing Ancient Observatory");
    baoData.put("type", "museum");
    citiesRef.document("BJ").collection("landmarks").add(baoData);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L982-L1032)

### Dart
    
    
    final citiesRef = db.collection("cities");
    
    final ggbData = {"name": "Golden Gate Bridge", "type": "bridge"};
    citiesRef.doc("SF").collection("landmarks").add(ggbData);
    
    final lohData = {"name": "Legion of Honor", "type": "museum"};
    citiesRef.doc("SF").collection("landmarks").add(lohData);
    
    final gpData = {"name": "Griffth Park", "type": "park"};
    citiesRef.doc("LA").collection("landmarks").add(gpData);
    
    final tgData = {"name": "The Getty", "type": "museum"};
    citiesRef.doc("LA").collection("landmarks").add(tgData);
    
    final lmData = {"name": "Lincoln Memorial", "type": "memorial"};
    citiesRef.doc("DC").collection("landmarks").add(lmData);
    
    final nasaData = {
      "name": "National Air and Space Museum",
      "type": "museum"
    };
    citiesRef.doc("DC").collection("landmarks").add(nasaData);
    
    final upData = {"name": "Ueno Park", "type": "park"};
    citiesRef.doc("TOK").collection("landmarks").add(upData);
    
    final nmData = {
      "name": "National Musuem of Nature and Science",
      "type": "museum"
    };
    citiesRef.doc("TOK").collection("landmarks").add(nmData);
    
    final jpData = {"name": "Jingshan Park", "type": "park"};
    citiesRef.doc("BJ").collection("landmarks").add(jpData);
    
    final baoData = {"name": "Beijing Ancient Observatory", "type": "musuem"};
    citiesRef.doc("BJ").collection("landmarks").add(baoData);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L790-L826)

##### Java
    
    
    CollectionReference cities = db.collection("cities");
    
    final List<ApiFuture<WriteResult>> futures =
        Arrays.asList(
            cities
                .document("SF")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Golden Gate Bridge");
                        put("type", "bridge");
                      }
                    }),
            cities
                .document("SF")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Legion of Honor");
                        put("type", "museum");
                      }
                    }),
            cities
                .document("LA")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Griffith Park");
                        put("type", "park");
                      }
                    }),
            cities
                .document("LA")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "The Getty");
                        put("type", "museum");
                      }
                    }),
            cities
                .document("DC")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Lincoln Memorial");
                        put("type", "memorial");
                      }
                    }),
            cities
                .document("DC")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "National Air and Space Museum");
                        put("type", "museum");
                      }
                    }),
            cities
                .document("TOK")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Ueno Park");
                        put("type", "park");
                      }
                    }),
            cities
                .document("TOK")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "National Museum of Nature and Science");
                        put("type", "museum");
                      }
                    }),
            cities
                .document("BJ")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Jingshan Park");
                        put("type", "park");
                      }
                    }),
            cities
                .document("BJ")
                .collection("landmarks")
                .document()
                .set(
                    new HashMap<String, String>() {
                      {
                        put("name", "Beijing Ancient Observatory");
                        put("type", "museum");
                      }
                    }));
    final List<WriteResult> landmarks = ApiFutures.allAsList(futures).get();
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L418-L532)

##### Python
    
    
    cities = db.collection("cities")
    
    sf_landmarks = cities.document("SF").collection("landmarks")
    sf_landmarks.document().set({"name": "Golden Gate Bridge", "type": "bridge"})
    sf_landmarks.document().set({"name": "Legion of Honor", "type": "museum"})
    la_landmarks = cities.document("LA").collection("landmarks")
    la_landmarks.document().set({"name": "Griffith Park", "type": "park"})
    la_landmarks.document().set({"name": "The Getty", "type": "museum"})
    dc_landmarks = cities.document("DC").collection("landmarks")
    dc_landmarks.document().set({"name": "Lincoln Memorial", "type": "memorial"})
    dc_landmarks.document().set(
        {"name": "National Air and Space Museum", "type": "museum"}
    )
    tok_landmarks = cities.document("TOK").collection("landmarks")
    tok_landmarks.document().set({"name": "Ueno Park", "type": "park"})
    tok_landmarks.document().set(
        {"name": "National Museum of Nature and Science", "type": "museum"}
    )
    bj_landmarks = cities.document("BJ").collection("landmarks")
    bj_landmarks.document().set({"name": "Jingshan Park", "type": "park"})
    bj_landmarks.document().set(
        {"name": "Beijing Ancient Observatory", "type": "museum"}
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L857-L879)

##### Python  
(Async)
    
    
    cities = db.collection("cities")
    
    sf_landmarks = cities.document("SF").collection("landmarks")
    await sf_landmarks.document().set({"name": "Golden Gate Bridge", "type": "bridge"})
    await sf_landmarks.document().set({"name": "Legion of Honor", "type": "museum"})
    la_landmarks = cities.document("LA").collection("landmarks")
    await la_landmarks.document().set({"name": "Griffith Park", "type": "park"})
    await la_landmarks.document().set({"name": "The Getty", "type": "museum"})
    dc_landmarks = cities.document("DC").collection("landmarks")
    await dc_landmarks.document().set({"name": "Lincoln Memorial", "type": "memorial"})
    await dc_landmarks.document().set(
        {"name": "National Air and Space Museum", "type": "museum"}
    )
    tok_landmarks = cities.document("TOK").collection("landmarks")
    await tok_landmarks.document().set({"name": "Ueno Park", "type": "park"})
    await tok_landmarks.document().set(
        {"name": "National Museum of Nature and Science", "type": "museum"}
    )
    bj_landmarks = cities.document("BJ").collection("landmarks")
    await bj_landmarks.document().set({"name": "Jingshan Park", "type": "park"})
    await bj_landmarks.document().set(
        {"name": "Beijing Ancient Observatory", "type": "museum"}
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L710-L732)

##### C++
    
    
    // Get a new write batch
    WriteBatch batch = db->batch();
    
    DocumentReference sf_ref = db->Collection("cities").Document("SF");
    batch.Set(sf_ref,{{"name", FieldValue::String("Golden Gate Bridge")}, {"type", FieldValue::String("bridge")}});
    batch.Set(sf_ref,{{"name", FieldValue::String("Legion of Honor")}, {"type", FieldValue::String("museum")}});
    
    DocumentReference la_ref = db->Collection("cities").Document("LA");
    batch.Set(la_ref,{{"name", FieldValue::String("Griffith Park")}, {"type", FieldValue::String("park")}});
    batch.Set(la_ref,{{"name", FieldValue::String("The Getty")}, {"type", FieldValue::String("museum")}});
    
    DocumentReference dc_ref = db->Collection("cities").Document("DC");
    batch.Set(dc_ref,{{"name", FieldValue::String("Lincoln Memorial")}, {"type", FieldValue::String("memorial")}});
    batch.Set(dc_ref,{{"name", FieldValue::String("National Air and Space Museum")}, {"type", FieldValue::String("museum")}});
    
    DocumentReference tok_ref = db->Collection("cities").Document("TOK");
    batch.Set(tok_ref,{{"name", FieldValue::String("Ueno Park")}, {"type", FieldValue::String("park")}});
    batch.Set(tok_ref,{{"name", FieldValue::String("National Museum of Nature and Science")}, {"type", FieldValue::String("museum")}});
    
    DocumentReference bj_ref = db->Collection("cities").Document("BJ");
    batch.Set(bj_ref,{{"name", FieldValue::String("Jingshan Park")}, {"type", FieldValue::String("park")}});
    batch.Set(bj_ref,{{"name", FieldValue::String("Beijing Ancient Observatory")}, {"type", FieldValue::String("museum")}});
    
    // Commit the batch
    batch.Commit().OnCompletion([](const Future<void>& future) {
      if (future.error() == Error::kErrorOk) {
        std::cout << "Write batch success!" << std::endl;
      } else {
        std::cout << "Write batch failure: " << future.error_message() << std::endl;
      }
    });

##### Node.js
    
    
    const citiesRef = db.collection('cities');
    
    await citiesRef.doc('SF').collection('landmarks').doc().set({
      name: 'Golden Gate Bridge',
      type: 'bridge'
    });
    await citiesRef.doc('SF').collection('landmarks').doc().set({
      name: 'Legion of Honor',
      type: 'museum'
    });
    await citiesRef.doc('LA').collection('landmarks').doc().set({
      name: 'Griffith Park',
      type: 'park'
    });
    await citiesRef.doc('LA').collection('landmarks').doc().set({
      name: 'The Getty',
      type: 'museum'
    });
    await citiesRef.doc('DC').collection('landmarks').doc().set({
      name: 'Lincoln Memorial',
      type: 'memorial'
    });
    await citiesRef.doc('DC').collection('landmarks').doc().set({
      name: 'National Air and Space Museum',
      type: 'museum'
    });
    await citiesRef.doc('TOK').collection('landmarks').doc().set({
      name: 'Ueno Park',
      type: 'park'
    });
    await citiesRef.doc('TOK').collection('landmarks').doc().set({
      name: 'National Museum of Nature and Science',
      type: 'museum'
    });
    await citiesRef.doc('BJ').collection('landmarks').doc().set({
      name: 'Jingshan Park',
      type: 'park'
    });
    await citiesRef.doc('BJ').collection('landmarks').doc().set({ 
      name: 'Beijing Ancient Observatory',
      type: 'museum'
    });
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L820-L861)

##### Go
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    )
    
    // collectionGroupSetup sets up a collection group to query.
    func collectionGroupSetup(projectID, cityCollection string) error {
    	ctx := context.Background()
    
    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	landmarks := []struct {
    		city, name, t string
    	}{
    		{"SF", "Golden Gate Bridge", "bridge"},
    		{"SF", "Legion of Honor", "museum"},
    		{"LA", "Griffith Park", "park"},
    		{"LA", "The Getty", "museum"},
    		{"DC", "Lincoln Memorial", "memorial"},
    		{"DC", "National Air and Space Museum", "museum"},
    		{"TOK", "Ueno Park", "park"},
    		{"TOK", "National Museum of Nature and Science", "museum"},
    		{"BJ", "Jingshan Park", "park"},
    		{"BJ", "Beijing Ancient Observatory", "museum"},
    	}
    
    	cities := client.Collection(cityCollection)
    	for _, l := range landmarks {
    		if _, err := cities.Doc(l.city).Collection("landmarks").[NewDoc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_CollectionRef_NewDoc)().Set(ctx, map[string]string{
    			"name": l.name,
    			"type": l.t,
    		}); err != nil {
    			return fmt.Errorf("Set: %w", err)
    		}
    	}
    
    	return nil
    }
    
    
    [collection_group_setup.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/collection_group_setup.go#L18-L62)

##### PHP
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $citiesRef->document('SF')->collection('landmarks')->newDocument()->set([
        'name' => 'Golden Gate Bridge',
        'type' => 'bridge'
    ]);
    $citiesRef->document('SF')->collection('landmarks')->newDocument()->set([
        'name' => 'Legion of Honor',
        'type' => 'museum'
    ]);
    $citiesRef->document('LA')->collection('landmarks')->newDocument()->set([
        'name' => 'Griffith Park',
        'type' => 'park'
    ]);
    $citiesRef->document('LA')->collection('landmarks')->newDocument()->set([
        'name' => 'The Getty',
        'type' => 'museum'
    ]);
    $citiesRef->document('DC')->collection('landmarks')->newDocument()->set([
        'name' => 'Lincoln Memorial',
        'type' => 'memorial'
    ]);
    $citiesRef->document('DC')->collection('landmarks')->newDocument()->set([
        'name' => 'National Air and Space Museum',
        'type' => 'museum'
    ]);
    $citiesRef->document('TOK')->collection('landmarks')->newDocument()->set([
        'name' => 'Ueno Park',
        'type' => 'park'
    ]);
    $citiesRef->document('TOK')->collection('landmarks')->newDocument()->set([
        'name' => 'National Museum of Nature and Science',
        'type' => 'museum'
    ]);
    $citiesRef->document('BJ')->collection('landmarks')->newDocument()->set([
        'name' => 'Jingshan Park',
        'type' => 'park'
    ]);
    $citiesRef->document('BJ')->collection('landmarks')->newDocument()->set([
        'name' => 'Beijing Ancient Observatory',
        'type' => 'museum'
    ]);
    print('Added example landmarks collections to the cities collection.' . PHP_EOL);
    
    [query_collection_group_dataset.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_collection_group_dataset.php#L41-L82)

##### Unity
    
    
    List<Task<DocumentReference>> futures =
        new List<Task<DocumentReference>>(){
            citiesRef
                .Document("SF")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "Golden Gate Bridge"},
                        {"type", "bridge"},
                    }
                    ),
            citiesRef
                .Document("SF")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "Legion of Honor"},
                        {"type", "museum"},
                    }
                    ),
            citiesRef
                .Document("LA")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>() 
                    {
                        {"name", "Griffith Park"},
                        {"type", "park"},
                    }
                    ),
            citiesRef
                .Document("LA")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>() 
                    {
                        {"name", "The Getty"},
                        {"type", "museum"},
                    }
                    ),
            citiesRef
                .Document("DC")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>() 
                    {
                        {"name", "Lincoln Memorial"},
                        {"type", "memorial"},
                    }
                    ),
            citiesRef
                .Document("DC")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "National Air and Space Museum"},
                        {"type", "museum"},
                    }
                    ),
            citiesRef
                .Document("TOK")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "Ueno Park"},
                        {"type", "park"},
                    }
                    ),
            citiesRef
                .Document("TOK")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "National Museum of Nature and Science"},
                        {"type", "museum"},
                    }
                    ),
            citiesRef
                .Document("BJ")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "Jingshan Park"},
                        {"type", "park"},
                    }
                    ),
            citiesRef
                .Document("BJ")
                .Collection("landmarks")
                .AddAsync(
                    new Dictionary<string, object>()
                    {
                        {"name", "Beijing Ancient Observatory"},
                        {"type", "museum"},
                    }
                    )};
    DocumentReference[] landmarks = Task.WhenAll(futures).Result;

##### C#
    
    
    // Copyright(c) 2017 Google Inc.
    //
    // Licensed under the Apache License, Version 2.0 (the "License"); you may not
    // use this file except in compliance with the License. You may obtain a copy of
    // the License at
    //
    // http://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    // WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    // License for the specific language governing permissions and limitations under
    // the License.
    
    using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
    using [Google.Cloud.Firestore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    using static Google.Cloud.Firestore.Admin.V1.Index.Types;
    
    namespace GoogleCloudSamples
    {
        public class QueryData
        {
            public static string Usage = @"Usage:
    C:\> dotnet run command YOUR_PROJECT_ID
    
    Where command is one of
        query-create-examples
        create-query-state
        create-query-capital
        simple-queries
        array-contains-query
        array-contains-any-query
        in-query
        in-query-array
        collection-group-query
        subcollection-query
        chained-query
        composite-index-chained-query
        range-query
        multiple-inequalities
    ";
            private static async Task QueryCreateExamples(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                // Note: the extra braces here are just to allow multiple citiesRef local variables.
                {
                    [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("SF").[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new Dictionary<string, object>
                    {
                        { "Name", "San Francisco" },
                        { "State", "CA" },
                        { "Country", "USA" },
                        { "Capital", false },
                        { "Population", 860000 },
                        { "Density", 18000 },
                        { "Regions", new[] {"west_coast", "norcal"} }
                    });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("LA").[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new Dictionary<string, object>
                    {
                        { "Name", "Los Angeles" },
                        { "State", "CA" },
                        { "Country", "USA" },
                        { "Capital", false },
                        { "Population", 3900000 },
                        { "Density", 8300 },
                        { "Regions", new[] {"west_coast", "socal"} }
                    });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("DC").[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new Dictionary<string, object>
                    {
                        { "Name", "Washington D.C." },
                        { "State", null },
                        { "Country", "USA" },
                        { "Capital", true },
                        { "Population", 680000 },
                        { "Density", 11300 },
                        { "Regions", new[] {"east_coast"} }
                    });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("TOK").[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new Dictionary<string, object>
                    {
                        { "Name", "Tokyo" },
                        { "State", null },
                        { "Country", "Japan" },
                        { "Capital", true },
                        { "Population", 9000000 },
                        { "Density", 16000 },
                        { "Regions", new[] {"kanto", "honshu"} }
                    });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("BJ").[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new Dictionary<string, object>
                    {
                        { "Name", "Beijing" },
                        { "State", null },
                        { "Country", "China" },
                        { "Capital", true },
                        { "Population", 21500000 },
                        { "Density", 3500 },
                        { "Regions", new[] {"jingjinji", "hebei"} }
                    });
                    Console.WriteLine("Added example cities data to the cities collection.");
                }
    
                {
                    [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("SF").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Golden Gate Bridge", Type = "bridge" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("SF").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Legion of Honor", Type = "museum" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("LA").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Griffith Park", Type = "park" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("DC").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Lincoln Memorial", Type = "memorial" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("DC").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "National Air And Space Museum", Type = "museum" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("TOK").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Ueno Park", Type = "park" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("TOK").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "National Museum of Nature and Science", Type = "museum" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("BJ").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Jingshan Park", Type = "park" });
                    await citiesRef.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)("BJ").Collection("landmarks").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)()
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(new { Name = "Beijing Ancient Observatory", Type = "museum" });
                }
            }
    
            private static async Task CreateQueryState(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef.[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("State", "CA");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query State=CA", documentSnapshot.Id);
                }
            }
    
            private static async Task CreateQueryCapital(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef.[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("Capital", true);
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query Capital=true", documentSnapshot.Id);
                }
            }
    
            private static async Task SimpleQueries(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) stateQuery = citiesRef.[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("State", "CA");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) populationQuery = citiesRef.[WhereGreaterThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereGreaterThan_Google_Cloud_Firestore_FieldPath_System_Object_)("Population", 1000000);
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) nameQuery = citiesRef.[WhereGreaterThanOrEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereGreaterThanOrEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("Name", "San Francisco");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) stateQuerySnapshot = await stateQuery.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in stateQuerySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query State=CA", documentSnapshot.Id);
                }
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) populationQuerySnapshot = await populationQuery.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in populationQuerySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query Population>1000000", documentSnapshot.Id);
                }
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) nameQuerySnapshot = await nameQuery.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in nameQuerySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query Name>=San Francisco", documentSnapshot.Id);
                }
            }
    
            private static async Task ArrayContainsQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef.[WhereArrayContains](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereArrayContains_Google_Cloud_Firestore_FieldPath_System_Object_)("Regions", "west_coast");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query 'Regions array_contains west_coast'", documentSnapshot.Id);
                }
            }
    
            private static async Task ArrayContainsAnyQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef.[WhereArrayContainsAny](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereArrayContainsAny_Google_Cloud_Firestore_FieldPath_System_Collections_IEnumerable_)("Regions", new[] { "west_coast", "east_coast" });
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query 'Regions array_contains_any {{west_coast, east_coast}}'", documentSnapshot.Id);
                }
            }
    
            private static async Task InQueryWithoutArray(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef.[WhereIn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereIn_Google_Cloud_Firestore_FieldPath_System_Collections_IEnumerable_)("Country", new[] { "USA", "Japan" });
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query 'Country in {{USA, Japan}}'", documentSnapshot.Id);
                }
            }
    
            private static async Task InQueryWithArray(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef.[WhereIn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereIn_Google_Cloud_Firestore_FieldPath_System_Collections_IEnumerable_)("Regions",
                    new[] { new[] { "west_coast" }, new[] { "east_coast" } });
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query 'Regions in {{west_coast}}, {{east_coast}}'", documentSnapshot.Id);
                }
            }
    
            private static async Task CollectionGroupQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) museums = db.[CollectionGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_CollectionGroup_System_String_)("landmarks").[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("Type", "museum");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await museums.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) document in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine($"{document.[Reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html#Google_Cloud_Firestore_DocumentSnapshot_Reference).Path}: {document.GetValue<string>("Name")}");
                }
            }
    
            private static async Task SubcollectionQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) landmarks = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities").[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Document.html)("SF").Collection("landmarks");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await landmarks.GetSnapshotAsync();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) document in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine($"{document.[Reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html#Google_Cloud_Firestore_DocumentSnapshot_Reference).Path}: {document.GetValue<string>("Name")}");
                }
            }
    
            private static async Task ChainedQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) chainedQuery = citiesRef
                    .[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("State", "CA")
                    .[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("Name", "San Francisco");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await chainedQuery.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query State=CA and Name=San Francisco", documentSnapshot.Id);
                }
            }
    
            private static async Task CompositeIndexChainedQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) chainedQuery = citiesRef
                    .[WhereEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("State", "CA")
                    .[WhereLessThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereLessThan_Google_Cloud_Firestore_FieldPath_System_Object_)("Population", 1000000);
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await chainedQuery.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query State=CA and Population<1000000", documentSnapshot.Id);
                }
            }
    
            private static async Task RangeQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) rangeQuery = citiesRef
                    .[WhereGreaterThanOrEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereGreaterThanOrEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("State", "CA")
                    .[WhereLessThanOrEqualTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereLessThanOrEqualTo_Google_Cloud_Firestore_FieldPath_System_Object_)("State", "IN");
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await rangeQuery.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot.[Documents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html#Google_Cloud_Firestore_QuerySnapshot_Documents))
                {
                    Console.WriteLine("Document {0} returned by query CA<=State<=IN", documentSnapshot.Id);
                }
            }
    
            private static async Task MultipleInequalitiesQuery(string project)
            {
                [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) db = [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(project);
                [FirestoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.FirestoreAdminClient.html) adminClient = [FirestoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.FirestoreAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.FirestoreAdminClient.html#Google_Cloud_Firestore_Admin_V1_FirestoreAdminClient_Create)();
                var index = new Google.Cloud.Firestore.Admin.V1.Index
                {
                    Fields =
                    {
                        new IndexField { FieldPath = "Density", Order = IndexField.Types.Order.Ascending },
                        new IndexField { FieldPath = "Population", Order = IndexField.Types.Order.Ascending }
                    },
                    QueryScope = QueryScope.Collection
                };
    
                // We speculatively try to create the index, and just ignore an error of it already existing.
                try
                {
                    var lro = await adminClient.[CreateIndexAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.FirestoreAdminClient.html#Google_Cloud_Firestore_Admin_V1_FirestoreAdminClient_CreateIndexAsync_Google_Cloud_Firestore_Admin_V1_CollectionGroupName_Google_Cloud_Firestore_Admin_V1_Index_Google_Api_Gax_Grpc_CallSettings_)(new [CollectionGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.CollectionGroupName.html)(db.[ProjectId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_ProjectId), db.[DatabaseId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_DatabaseId), "cities"), index);
                    await lro.PollUntilCompletedAsync();
                }
                catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) ex) when (ex.[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
                {
                    // Assume the index is okay.
                }
    
                [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) citiesRef = db.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("cities");
                [Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html) query = citiesRef
                    .[WhereGreaterThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereGreaterThan_Google_Cloud_Firestore_FieldPath_System_Object_)("Population", 1000000)
                    .[WhereLessThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_WhereLessThan_Google_Cloud_Firestore_FieldPath_System_Object_)("Density", 10000);
                [QuerySnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.QuerySnapshot.html) querySnapshot = await query.[GetSnapshotAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_GetSnapshotAsync_System_Threading_CancellationToken_)();
                foreach ([DocumentSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentSnapshot.html) documentSnapshot in querySnapshot)
                {
                    var name = documentSnapshot.GetValue<string>("Name");
                    var population = documentSnapshot.GetValue<int>("Population");
                    var density = documentSnapshot.GetValue<int>("Density");
                    Console.WriteLine($"City '{name}' returned by query. Population={population}; Density={density}");
                }
            }
    
            public static void Main(string[] args)
            {
                if (args.[Length](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Blob.html#Google_Cloud_Firestore_Blob_Length) < 2)
                {
                    Console.[Write](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Write.html)(Usage);
                    return;
                }
                string command = args[0].ToLower();
                string project = string.Join(" ",
                    new ArraySegment<string>(args, 1, args.[Length](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Blob.html#Google_Cloud_Firestore_Blob_Length) - 1));
                switch (command)
                {
                    case "query-create-examples":
                        QueryCreateExamples(project).Wait();
                        break;
    
                    case "create-query-state":
                        CreateQueryState(project).Wait();
                        break;
    
                    case "create-query-capital":
                        CreateQueryCapital(project).Wait();
                        break;
    
                    case "simple-queries":
                        SimpleQueries(project).Wait();
                        break;
    
                    case "array-contains-query":
                        ArrayContainsQuery(project).Wait();
                        break;
    
                    case "array-contains-any-query":
                        ArrayContainsAnyQuery(project).Wait();
                        break;
    
                    case "in-query":
                        InQueryWithoutArray(project).Wait();
                        break;
    
                    case "in-query-array":
                        InQueryWithArray(project).Wait();
                        break;
    
                    case "collection-group-query":
                        CollectionGroupQuery(project).Wait();
                        break;
    
                    case "subcollection-query":
                        SubcollectionQuery(project).Wait();
                        break;
    
                    case "chained-query":
                        ChainedQuery(project).Wait();
                        break;
    
                    case "composite-index-chained-query":
                        CompositeIndexChainedQuery(project).Wait();
                        break;
    
                    case "range-query":
                        RangeQuery(project).Wait();
                        break;
    
                    case "multiple-inequalities":
                        MultipleInequalitiesQuery(project).Wait();
                        break;
    
                    default:
                        Console.[Write](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Write.html)(Usage);
                        return;
                }
            }
        }
    }
    
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs)

##### Ruby
    
    
    cities_ref = firestore.col collection_path
    
    sf_landmarks = cities_ref.document("SF").collection("landmarks")
    sf_landmarks.document.set(
      {
        name: "Golden Gate Bridge",
        type: "bridge"
      }
    )
    sf_landmarks.document.set(
      {
        name: "Legion of Honor",
        type: "museum"
      }
    )
    
    la_landmarks = cities_ref.document("LA").collection("landmarks")
    la_landmarks.document.set(
      {
        name: "Griffith Park",
        type: "park"
      }
    )
    la_landmarks.document.set(
      {
        name: "The Getty",
        type: "museum"
      }
    )
    
    dc_landmarks = cities_ref.document("DC").collection("landmarks")
    dc_landmarks.document.set(
      {
        name: "Lincoln Memorial",
        type: "memorial"
      }
    )
    dc_landmarks.document.set(
      {
        name: "National Air and Space Museum",
        type: "museum"
      }
    )
    
    tok_landmarks = cities_ref.document("TOK").collection("landmarks")
    tok_landmarks.document.set(
      {
        name: "Ueno Park",
        type: "park"
      }
    )
    tok_landmarks.document.set(
      {
        name: "National Museum of Nature and Science",
        type: "museum"
      }
    )
    
    bj_landmarks = cities_ref.document("BJ").collection("landmarks")
    bj_landmarks.document.set(
      {
        name: "Jingshan Park",
        type: "park"
      }
    )
    bj_landmarks.document.set(
      {
        name: "Beijing Ancient Observatory",
        type: "museum"
      }
    )
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L295-L365)

We can use the simple and compound query described earlier to query a single city's `landmarks` subcollection, but you might also want to retrieve results from every city's `landmarks` subcollection at once.

The `landmarks` collection group consists of all collections with the ID `landmarks`, and you can query it using a collection group query. For example, this collection group query retrieves all `museum` landmarks across all cities:

### Web version 9
    
    
    import { collectionGroup, query, where, getDocs } from "firebase/firestore";  
    
    const museums = query(collectionGroup(db, 'landmarks'), where('type', '==', 'museum'));
    const querySnapshot = await getDocs(museums);
    querySnapshot.forEach((doc) => {
        console.log(doc.id, ' => ', doc.data());
    });
    
    [fs_collection_group_query.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/fs_collection_group_query.js#L8-L14)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    var museums = db.collectionGroup('landmarks').where('type', '==', 'museum');
    museums.get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            console.log(doc.id, ' => ', doc.data());
        });
    });
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L1090-L1095)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    db.collectionGroup("landmarks").whereField("type", isEqualTo: "museum").getDocuments { (snapshot, error) in
      // ...
    }
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1255-L1259)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[[self.db collectionGroupWithID:@"landmarks"] queryWhereField:@"type" isEqualTo:@"museum"]
        getDocumentsWithCompletion:^(FIRQuerySnapshot *snapshot, NSError *error) {
        // ...
    }];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L1153-L1157)

##### Kotlin  
Android
    
    
    db.collectionGroup("landmarks").whereEqualTo("type", "museum").get()
        .addOnSuccessListener { queryDocumentSnapshots ->
            // ...
        }
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1026-L1033)

##### Java  
Android
    
    
    db.collectionGroup("landmarks").whereEqualTo("type", "museum").get()
            .addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
                @Override
                public void onSuccess(QuerySnapshot queryDocumentSnapshots) {
                    // ...
                }
            });
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1226-L1236)

### Dart
    
    
    db
        .collectionGroup("landmarks")
        .where("type", isEqualTo: "museum")
        .get()
        .then(
          (res) => print("Successfully completed"),
          onError: (e) => print("Error completing: $e"),
        );
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L832-L839)

##### Java
    
    
    final Query museums = db.collectionGroup("landmarks").whereEqualTo("type", "museum");
    final ApiFuture<QuerySnapshot> querySnapshot = museums.get();
    for (DocumentSnapshot document : querySnapshot.get().getDocuments()) {
      System.out.println(document.getId());
    }
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L536-L540)

##### Python
    
    
    museums = db.collection_group("landmarks").where(
        filter=FieldFilter("type", "==", "museum")
    )
    docs = museums.stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-client/snippets.py#L883-L888)

##### Python  
(Async)
    
    
    museums = db.collection_group("landmarks").where(
        filter=FieldFilter("type", "==", "museum")
    )
    docs = museums.stream()
    async for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/83a4a2befda9030e8c4e5b1d24bbc97c04329923/firestore/cloud-async-client/snippets.py#L736-L741)

##### C++
    
    
    db->CollectionGroup("landmarks")
    .WhereEqualTo("type", FieldValue::String("museum")).Get()
    .OnCompletion([](const firebase::Future<QuerySnapshot>& future) {
      if (future.error() == Error::kErrorOk) {
        for (const DocumentSnapshot& document : future.result()->documents()) {
          std::cout << document << std::endl;
        }
      } else {
        std::cout << "Error getting documents: " << future.error_message()
                  << std::endl;
      }
    });

##### Node.js
    
    
    const querySnapshot = await db.collectionGroup('landmarks').where('type', '==', 'museum').get();
    querySnapshot.forEach((doc) => {
      console.log(doc.id, ' => ', doc.data());
    });
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L865-L868)

##### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    // collectionGroupQuery runs a collection group query over the data created by
    // collectionGroupSetup.
    func collectionGroupQuery(w io.Writer, projectID string) error {
    	ctx := context.Background()
    
    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	it := client.CollectionGroup("landmarks").Where("type", "==", "museum").Documents(ctx)
    	for {
    		doc, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("documents iterator: %w", err)
    		}
    		fmt.Fprintf(w, "%s: %s", doc.[Ref](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_PipelineResult_Ref).ID, doc.Data()["name"])
    	}
    
    	return nil
    }
    
    
    [collection_group_query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/collection_group_query.go#L18-L52)

##### PHP
    
    
    $museums = $db->collectionGroup('landmarks')->where('type', '==', 'museum');
    foreach ($museums->documents() as $document) {
        printf('%s => %s' . PHP_EOL, $document->id(), $document->data()['name']);
    }
    
    [query_collection_group_filter_eq.php](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/699cf3e69716069e565cfc595cb4efb1049ab35a/firestore/src/query_collection_group_filter_eq.php#L43-L46)

##### Unity
    
    
    Query museums = db.CollectionGroup("landmarks").WhereEqualTo("type", "museum");
    museums.GetSnapshotAsync().ContinueWithOnMainThread((querySnapshotTask) =>
    {
        foreach (DocumentSnapshot documentSnapshot in querySnapshotTask.Result.Documents)
        {
            Debug.Log(String.Format("Document {0} returned by query State=CA", documentSnapshot.Id));
        } 
    });

##### C#
    
    
    Query museums = db.CollectionGroup("landmarks").WhereEqualTo("Type", "museum");
    QuerySnapshot querySnapshot = await museums.GetSnapshotAsync();
    foreach (DocumentSnapshot document in querySnapshot.Documents)
    {
        Console.WriteLine($"{document.Reference.Path}: {document.GetValue<string>("Name")}");
    }
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/6f1cae15ae479cedcc5c6f3760f94c581c985822/firestore/api/QueryData/Program.cs#L249-L254)

##### Ruby
    
    
    museums = firestore.collection_group("landmarks").where("type", "==", "museum")
    museums.get do |museum|
      puts "#{museum[:type]} name is #{museum[:name]}."
    end
    
    [query_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/ce9995ee43bde7f4792efc07782fe2a2ba6184d9/google-cloud-firestore/samples/query_data.rb#L369-L372)

Before using a collection group query, you must create an index that supports your collection group query. [You can create an index through an error message, the console, or the Firebase CLI](https://docs.cloud.google.com/firestore/native/docs/query-data/indexing).

For the web and mobile SDKs, you must also [create rules that allow your collection group queries](https://docs.cloud.google.com/firestore/native/docs/security/rules-query#secure_and_query_documents_based_on_collection_groups).

## Explain your query performance

Firestore in Native Mode allows you to measure performance of your queries on the backend and receive detailed performance statistics on backend query execution in return.

Query Explain results help you understand how your queries are executed, showing you inefficiencies and the location of likely server-side bottlenecks.

For more information, see the [guide for Query Explain](https://docs.cloud.google.com/firestore/native/docs/query-explain).

## Standard edition query limitations

The following list summarizes Firestore query limitations. These limitations apply only to Standard edition:

  * Firestore provides support for logical `OR` queries through the `or`, `in`, and `array-contains-any` operators. These queries are limited to 30 disjunctions based on the query's disjunctive normal form. This limit is fixed and cannot be adjusted.
  * You can use at most one `array-contains` clause per disjunction (`or` group). You can't combine `array-contains` with `array-contains-any` in the same disjunction.
  * You can't combine `not-in` with `in`, `array-contains-any`, or `or` in the same query.
  * Only a single `not-in` or `!=` is allowed per query.
  * `not-in` supports up to 10 comparison values.
  * The sum of filters, sort orders, and parent document path (1 for a subcollection, 0 for a root collection) in a query cannot exceed 100. This is calculated based on the disjunctive normal form of the query.
  * A query with an inequality filter on a field implies ordering by that field and filters for existence of that field.



### Limits on `OR` queries

To prevent a query from becoming too computationally expensive, Firestore Standard edition limits how many `AND` and `OR` clauses you can combine. To apply this limit, Firestore converts queries that perform logical `OR` operations (`or`, `in`, and `array-contains-any`) to [disjunctive normal form](https://en.wikipedia.org/wiki/Disjunctive_normal_form) (also known as an `OR` of `AND`s). **Firestore limits a query to a maximum of 30 disjunctions in disjunctive normal form.** This limit is fixed and cannot be adjusted.

#### Disjunctive normal form

Firestore converts queries to disjunctive normal form by applying two rules:

  * **_Flatten_**

Given conditions `A`, `B`, and `C`:

`A and (B and C) => A and B and C`

  * [**_Distributive Law_**](https://en.wikipedia.org/wiki/Distributive_property)

Given conditions `A`, `B`, `C`, and `D`:

    * `A and (B or C) => (A and B) or (A and C)`
    * `(A or B) and (C or D) => (A and C) or (A and D) or (B and C) or (B and D)`



When applying these rules to `in` and `array-contains-any` queries, remember that these operators are shorthands for `OR`. For example, `a in [1,2]` is shorthand for `a = 1 OR a = 2`.

**Warning:** Due to the multiplicative nature of conversions to disjunctive normal form, you are more likely to reach the limit when performing an `AND` of multiple `OR` groups.

The following examples show the number of disjunctions for different queries:

Query| Number of disjunctions  
---|---  
      
    
    query(collectionRef, where("a", "==", 1))
          

| 1  
      
    
    query(collectionRef, or( where("a", "==", 1), where("b", "==", 2) ))
          

| 2  
      
    
    query(collectionRef,
            or( and( where("a", "==", 1), where("c", "==", 3) ),
                and( where("a", "==", 1), where("d", "==", 4) ),
                and( where("b", "==", 2), where("c", "==", 3) ),
                and( where("b", "==", 2), where("d", "==", 4) )
            )
          )
          

| 4  
      
    
    query(collectionRef,
            and( or( where("a", "==", 1), where("b", "==", 2) ),
                 or( where("c", "==", 3), where("d", "==", 4) )
            )
          )
          

|  4 The disjunctive normal form of this query is equal to the query above.  
      
    
    query(collectionRef, where("a", "in", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) )
          

| 10  
      
    
    query(collectionRef,
            and( where("a", "in", [1, 2, 3, 4, 5]),
                 where("b", "in", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            )
          )
          

| 50 This query returns an error, because it surpasses the limit of 30 disjunctions.  
      
    
    query(collectionRef,
            or( where("a", "in", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                where("b", "in", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            )
          )
          

| 20  
      
    
    query(collectionRef,
            and( where("a", "in", [1, 2, 3, 4, 5]),
                 or( where("b", "==", 2),
                     where("c", "==", 3)
                 )
            )
          )
          

| 10  
  
## `orderBy` and existence

When you order a query by a given field, the query can return only the documents where the order-by field exists.

For example, the following query would not return any documents where the `population` field is not set, even if they otherwise meet the query filters.

##### Java
    
    
    db.collection("cities").whereEqualTo("country", “USA”).orderBy(“population”);

A related effect applies to inequalities. A query with an inequality filter on a field also implies ordering by that field. The following query does not return documents without a `population` field even if `country = USA` in that document . As a workaround, you can execute separate queries for each ordering or you can assign a value for all fields that you order by.

##### Java
    
    
    db.collection(“cities”).where(or(“country”, USA”), greaterThan(“population”, 250000));

The query above includes an implied order-by on the inequality and is equivalent to the following:

##### Java
    
    
    db.collection(“cities”).where(or(“country”, USA”), greaterThan(“population”, 250000)).orderBy(“population”);

## What's next

  * Learn how to [order and limit data in query results](https://docs.cloud.google.com/firestore/native/docs/query-data/order-limit-data).
  * Save reads when you simply want to [count results](https://docs.cloud.google.com/firestore/native/docs/query-data/aggregation-queries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
