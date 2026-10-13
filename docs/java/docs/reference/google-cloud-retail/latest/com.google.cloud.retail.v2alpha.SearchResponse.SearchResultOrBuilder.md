---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.SearchResponse.SearchResultOrBuilder
title: Interface SearchResponse.SearchResultOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:58.102127+00:00
---

# Interface SearchResponse.SearchResultOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.SearchResponse.SearchResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchResponse.SearchResultOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public static interface SearchResponse.SearchResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMatchingVariantFields(String key)
    
    
    public abstract boolean containsMatchingVariantFields(String key)

If a variant Product matches the search query, this map indicates which Product fields are matched. The key is the Product.name, the value is a field mask of the matched Product fields. If matched attributes cannot be determined, this map will be empty.

For example, a key "sku1" with field mask "products.color_info" indicates there is a match between "sku1" ColorInfo and the query.

`map<string, .google.protobuf.FieldMask> matching_variant_fields = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsModelScores(String key)
    
    
    public abstract boolean containsModelScores(String key)

Google provided available scores.

`map<string, .google.cloud.retail.v2alpha.DoubleList> model_scores = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsVariantRollupValues(String key)
    
    
    public abstract boolean containsVariantRollupValues(String key)

The rollup matching variant Product attributes. The key is one of the SearchRequest.variant_rollup_keys. The values are the merged and de-duplicated Product attributes. Notice that the rollup values are respect filter. For example, when filtering by "colorFamilies:ANY(\"red\")" and rollup "colorFamilies", only "red" is returned.

For textual and numerical attributes, the rollup values is a list of string or double values with type google.protobuf.ListValue. For example, if there are two variants with colors "red" and "blue", the rollup values are

{ key: "colorFamilies" value { list_value { values { string_value: "red" } values { string_value: "blue" } } } }

For FulfillmentInfo, the rollup values is a double value with type google.protobuf.Value. For example, `{key: "pickupInStore.store1" value { number_value: 10 }}` means a there are 10 variants in this product are available in the store "store1".

`map<string, .google.protobuf.Value> variant_rollup_values = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getId()
    
    
    public abstract String getId()

Product.id of the searched Product.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Product.id of the searched Product.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getMatchingVariantCount()
    
    
    public abstract int getMatchingVariantCount()

The count of matched variant Products.

`int32 matching_variant_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The matchingVariantCount.  
  
### getMatchingVariantFields() (deprecated)
    
    
    public abstract Map<String,FieldMask> getMatchingVariantFields()

Use [#getMatchingVariantFieldsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.SearchResponse.SearchResultOrBuilder#com_google_cloud_retail_v2alpha_SearchResponse_SearchResultOrBuilder_getMatchingVariantFieldsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)>` |   
  
### getMatchingVariantFieldsCount()
    
    
    public abstract int getMatchingVariantFieldsCount()

If a variant Product matches the search query, this map indicates which Product fields are matched. The key is the Product.name, the value is a field mask of the matched Product fields. If matched attributes cannot be determined, this map will be empty.

For example, a key "sku1" with field mask "products.color_info" indicates there is a match between "sku1" ColorInfo and the query.

`map<string, .google.protobuf.FieldMask> matching_variant_fields = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMatchingVariantFieldsMap()
    
    
    public abstract Map<String,FieldMask> getMatchingVariantFieldsMap()

If a variant Product matches the search query, this map indicates which Product fields are matched. The key is the Product.name, the value is a field mask of the matched Product fields. If matched attributes cannot be determined, this map will be empty.

For example, a key "sku1" with field mask "products.color_info" indicates there is a match between "sku1" ColorInfo and the query.

`map<string, .google.protobuf.FieldMask> matching_variant_fields = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)>` |   
  
### getMatchingVariantFieldsOrDefault(String key, FieldMask defaultValue)
    
    
    public abstract FieldMask getMatchingVariantFieldsOrDefault(String key, FieldMask defaultValue)

If a variant Product matches the search query, this map indicates which Product fields are matched. The key is the Product.name, the value is a field mask of the matched Product fields. If matched attributes cannot be determined, this map will be empty.

For example, a key "sku1" with field mask "products.color_info" indicates there is a match between "sku1" ColorInfo and the query.

`map<string, .google.protobuf.FieldMask> matching_variant_fields = 4;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` |   
  
### getMatchingVariantFieldsOrThrow(String key)
    
    
    public abstract FieldMask getMatchingVariantFieldsOrThrow(String key)

If a variant Product matches the search query, this map indicates which Product fields are matched. The key is the Product.name, the value is a field mask of the matched Product fields. If matched attributes cannot be determined, this map will be empty.

For example, a key "sku1" with field mask "products.color_info" indicates there is a match between "sku1" ColorInfo and the query.

`map<string, .google.protobuf.FieldMask> matching_variant_fields = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` |   
  
### getModelScores() (deprecated)
    
    
    public abstract Map<String,DoubleList> getModelScores()

Use [#getModelScoresMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.SearchResponse.SearchResultOrBuilder#com_google_cloud_retail_v2alpha_SearchResponse_SearchResultOrBuilder_getModelScoresMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[DoubleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.DoubleList)>` |   
  
### getModelScoresCount()
    
    
    public abstract int getModelScoresCount()

Google provided available scores.

`map<string, .google.cloud.retail.v2alpha.DoubleList> model_scores = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getModelScoresMap()
    
    
    public abstract Map<String,DoubleList> getModelScoresMap()

Google provided available scores.

`map<string, .google.cloud.retail.v2alpha.DoubleList> model_scores = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[DoubleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.DoubleList)>` |   
  
### getModelScoresOrDefault(String key, DoubleList defaultValue)
    
    
    public abstract DoubleList getModelScoresOrDefault(String key, DoubleList defaultValue)

Google provided available scores.

`map<string, .google.cloud.retail.v2alpha.DoubleList> model_scores = 8;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[DoubleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.DoubleList)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DoubleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.DoubleList)` |   
  
### getModelScoresOrThrow(String key)
    
    
    public abstract DoubleList getModelScoresOrThrow(String key)

Google provided available scores.

`map<string, .google.cloud.retail.v2alpha.DoubleList> model_scores = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DoubleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.DoubleList)` |   
  
### getPersonalLabels(int index)
    
    
    public abstract String getPersonalLabels(int index)

Specifies previous events related to this product for this user based on UserEvent with same SearchRequest.visitor_id or UserInfo.user_id.

This is set only when SearchRequest.PersonalizationSpec.mode is SearchRequest.PersonalizationSpec.Mode.AUTO.

Possible values:

  * `purchased`: Indicates that this product has been purchased before.



`repeated string personal_labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The personalLabels at the given index.  
  
### getPersonalLabelsBytes(int index)
    
    
    public abstract ByteString getPersonalLabelsBytes(int index)

Specifies previous events related to this product for this user based on UserEvent with same SearchRequest.visitor_id or UserInfo.user_id.

This is set only when SearchRequest.PersonalizationSpec.mode is SearchRequest.PersonalizationSpec.Mode.AUTO.

Possible values:

  * `purchased`: Indicates that this product has been purchased before.



`repeated string personal_labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the personalLabels at the given index.  
  
### getPersonalLabelsCount()
    
    
    public abstract int getPersonalLabelsCount()

Specifies previous events related to this product for this user based on UserEvent with same SearchRequest.visitor_id or UserInfo.user_id.

This is set only when SearchRequest.PersonalizationSpec.mode is SearchRequest.PersonalizationSpec.Mode.AUTO.

Possible values:

  * `purchased`: Indicates that this product has been purchased before.



`repeated string personal_labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of personalLabels.  
  
### getPersonalLabelsList()
    
    
    public abstract List<String> getPersonalLabelsList()

Specifies previous events related to this product for this user based on UserEvent with same SearchRequest.visitor_id or UserInfo.user_id.

This is set only when SearchRequest.PersonalizationSpec.mode is SearchRequest.PersonalizationSpec.Mode.AUTO.

Possible values:

  * `purchased`: Indicates that this product has been purchased before.



`repeated string personal_labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the personalLabels.  
  
### getProduct()
    
    
    public abstract Product getProduct()

The product data snippet in the search response. Only Product.name is guaranteed to be populated.

Product.variants contains the product variants that match the search query. If there are multiple product variants matching the query, top 5 most relevant product variants are returned and ordered by relevancy.

If relevancy can be deternmined, use matching_variant_fields to look up matched product variants fields. If relevancy cannot be determined, e.g. when searching "shoe" all products in a shoe product can be a match, 5 product variants are returned but order is meaningless.

`.google.cloud.retail.v2alpha.Product product = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Product)` | The product.  
  
### getProductOrBuilder()
    
    
    public abstract ProductOrBuilder getProductOrBuilder()

The product data snippet in the search response. Only Product.name is guaranteed to be populated.

Product.variants contains the product variants that match the search query. If there are multiple product variants matching the query, top 5 most relevant product variants are returned and ordered by relevancy.

If relevancy can be deternmined, use matching_variant_fields to look up matched product variants fields. If relevancy cannot be determined, e.g. when searching "shoe" all products in a shoe product can be a match, 5 product variants are returned but order is meaningless.

`.google.cloud.retail.v2alpha.Product product = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ProductOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ProductOrBuilder)` |   
  
### getVariantRollupValues() (deprecated)
    
    
    public abstract Map<String,Value> getVariantRollupValues()

Use [#getVariantRollupValuesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.SearchResponse.SearchResultOrBuilder#com_google_cloud_retail_v2alpha_SearchResponse_SearchResultOrBuilder_getVariantRollupValuesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getVariantRollupValuesCount()
    
    
    public abstract int getVariantRollupValuesCount()

The rollup matching variant Product attributes. The key is one of the SearchRequest.variant_rollup_keys. The values are the merged and de-duplicated Product attributes. Notice that the rollup values are respect filter. For example, when filtering by "colorFamilies:ANY(\"red\")" and rollup "colorFamilies", only "red" is returned.

For textual and numerical attributes, the rollup values is a list of string or double values with type google.protobuf.ListValue. For example, if there are two variants with colors "red" and "blue", the rollup values are

{ key: "colorFamilies" value { list_value { values { string_value: "red" } values { string_value: "blue" } } } }

For FulfillmentInfo, the rollup values is a double value with type google.protobuf.Value. For example, `{key: "pickupInStore.store1" value { number_value: 10 }}` means a there are 10 variants in this product are available in the store "store1".

`map<string, .google.protobuf.Value> variant_rollup_values = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVariantRollupValuesMap()
    
    
    public abstract Map<String,Value> getVariantRollupValuesMap()

The rollup matching variant Product attributes. The key is one of the SearchRequest.variant_rollup_keys. The values are the merged and de-duplicated Product attributes. Notice that the rollup values are respect filter. For example, when filtering by "colorFamilies:ANY(\"red\")" and rollup "colorFamilies", only "red" is returned.

For textual and numerical attributes, the rollup values is a list of string or double values with type google.protobuf.ListValue. For example, if there are two variants with colors "red" and "blue", the rollup values are

{ key: "colorFamilies" value { list_value { values { string_value: "red" } values { string_value: "blue" } } } }

For FulfillmentInfo, the rollup values is a double value with type google.protobuf.Value. For example, `{key: "pickupInStore.store1" value { number_value: 10 }}` means a there are 10 variants in this product are available in the store "store1".

`map<string, .google.protobuf.Value> variant_rollup_values = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getVariantRollupValuesOrDefault(String key, Value defaultValue)
    
    
    public abstract Value getVariantRollupValuesOrDefault(String key, Value defaultValue)

The rollup matching variant Product attributes. The key is one of the SearchRequest.variant_rollup_keys. The values are the merged and de-duplicated Product attributes. Notice that the rollup values are respect filter. For example, when filtering by "colorFamilies:ANY(\"red\")" and rollup "colorFamilies", only "red" is returned.

For textual and numerical attributes, the rollup values is a list of string or double values with type google.protobuf.ListValue. For example, if there are two variants with colors "red" and "blue", the rollup values are

{ key: "colorFamilies" value { list_value { values { string_value: "red" } values { string_value: "blue" } } } }

For FulfillmentInfo, the rollup values is a double value with type google.protobuf.Value. For example, `{key: "pickupInStore.store1" value { number_value: 10 }}` means a there are 10 variants in this product are available in the store "store1".

`map<string, .google.protobuf.Value> variant_rollup_values = 5;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getVariantRollupValuesOrThrow(String key)
    
    
    public abstract Value getVariantRollupValuesOrThrow(String key)

The rollup matching variant Product attributes. The key is one of the SearchRequest.variant_rollup_keys. The values are the merged and de-duplicated Product attributes. Notice that the rollup values are respect filter. For example, when filtering by "colorFamilies:ANY(\"red\")" and rollup "colorFamilies", only "red" is returned.

For textual and numerical attributes, the rollup values is a list of string or double values with type google.protobuf.ListValue. For example, if there are two variants with colors "red" and "blue", the rollup values are

{ key: "colorFamilies" value { list_value { values { string_value: "red" } values { string_value: "blue" } } } }

For FulfillmentInfo, the rollup values is a double value with type google.protobuf.Value. For example, `{key: "pickupInStore.store1" value { number_value: 10 }}` means a there are 10 variants in this product are available in the store "store1".

`map<string, .google.protobuf.Value> variant_rollup_values = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### hasProduct()
    
    
    public abstract boolean hasProduct()

The product data snippet in the search response. Only Product.name is guaranteed to be populated.

Product.variants contains the product variants that match the search query. If there are multiple product variants matching the query, top 5 most relevant product variants are returned and ordered by relevancy.

If relevancy can be deternmined, use matching_variant_fields to look up matched product variants fields. If relevancy cannot be determined, e.g. when searching "shoe" all products in a shoe product can be a match, 5 product variants are returned but order is meaningless.

`.google.cloud.retail.v2alpha.Product product = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the product field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
