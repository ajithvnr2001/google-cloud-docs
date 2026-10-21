---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle/
title: Schema lifecycle management \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:09:22.617938+00:00
---

# Schema lifecycle management  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Schema lifecycle management Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

As your applications and their data requirements change, the structure of your Kafka messages also needs to adapt. Effective schema lifecycle management is crucial for handling these changes smoothly and maintaining data integrity. This process involves not just changing schemas, but also systematically controlling the kinds of changes that are safe, or sufficiently compatible, for the applications that depend on them.

Managed Service for Apache Kafka schema registry supports the full lifecycle of schema management and includes the following features:

  * Define and enforce compatibility rules (compatibility type) to manage schema evolution when new schema versions are introduced. These rules ensure that producers and consumers continue to operate correctly.

  * Configure operational controls (schema modes) to manage the mutability of schemas at different levels, safeguarding your data processing pipelines.

  * Manage schema references to promote reusability and consistency across your schemas.




## How schema evolution works

  1. You modify your schema definition. For example—add an optional field to your `.proto` or `.avsc` file.

  2. A producer configured with `auto.register.schemas=true` sends a message using the new schema, or you explicitly attempt to register the new schema using the API or client libraries.

  3. When a registration request for a new version reaches the schema registry, it retrieves the configured compatibility rule for the target subject. It compares the proposed new schema against the required previous version(s) according to that rule.

  4. If the schema version is compatible, the new schema is successfully registered as the next version under the subject, assigned a new version number, and potentially a new `schema_id` if the definition is unique.

  5. The producer (if applicable) receives the `schema_id` to include with messages.

  6. If the schema version is incompatible, the registration attempt fails, and an error is returned.




## About compatibility type

Schema compatibility lets you define how the schema registry handles compatibility checks between different schema versions. You can apply these configurations at various levels within the schema registry hierarchy, as indicated by the following resource pattern options:

  * **Registry-level:** Sets default configuration for the entire schema registry.

    * Path: `projects/project/locations/location/schemaRegistries/schema_registry/config`
  * **Subject-level within default context:** Sets specific configuration for a subject within the registry's default context.

    * Path: `projects/project/locations/location/schemaRegistries/schema_registry/config/subject`
  * **Subject-level within a specific context:** Sets specific configuration for a subject within a named context.

    * Path: `projects/project/locations/location/schemaRegistries/schema_registry/contexts/context/config/subject`



Configurations set at subject level override those set at the registry level. If a setting is not specified at the subject level, it inherits the value from the registry level. If not explicitly set at the registry level, the default is `Backward`.

The following available types determine how the schema registry compares a new schema version against previous ones:

  * **`None`:** No compatibility checks are performed. Allows any change, but carries a high risk of breaking clients.

  * **`Backward` (Default):** Consumer applications using the new schema can decode data produced with only the previously registered schema. This allows adding optional fields and deleting fields. Consumers must be upgraded before producers.

  * **`Backward_transitive`:** Consumer applications using the new schema can decode data produced with _all_ previous schema versions in that subject. This setting is stricter than `Backward`.

  * **`Forward`:** Data produced using the new schema must be readable by clients using the previous registered schema. Producers must be upgraded first, but consumers using the new schema might not be able to read data produced with even older schemas. This setting allows deleting optional fields and adding fields.

  * **`Forward_transitive`:** Data produced using the new schema must be readable by using _all_ previous schema versions. This setting is stricter than `Forward`.

  * **`Full`:** The new schema is both backwards- and forwards-compatible with the previously registered schema version. Clients can be upgraded in any order relative to the producer using the new schema. Allows adding or deleting optional fields.

  * **`Full_transitive`:** The new schema is both backwards- and forwards- compatible with all previous schema versions in that subject. This setting is stricter than `Full`.




### Example for compatibility type

Assume you have a schema registry with `Backward` compatibility type. You also create several subjects within this registry, and they inherit the registry's `Backward` compatibility.

For a specific subject named `user-events`, you need stricter compatibility rules. You update the schema compatibility level for the `user-events` subject to `Full`.

In this situation, the following rules apply:

  * Any new schema version registered under the `user-events` subject have to be both backwards- and forwards-compatible with the previously registered schema version for that subject.

  * Other subjects in the schema registry still adhere to the registry-level `Backward` compatibility setting unless their compatibility has been explicitly configured.




If you were to later change the schema registry's compatibility level to `Forward`, this change would affect the default compatibility for any _new_ subjects created within the registry. However, the `user-events` subject would retain its explicitly set `Full` compatibility, as subject-level configurations override registry-level configurations.

This demonstrates how you can have a default compatibility level for the entire registry while also having the flexibility to define specific compatibility requirements for individual subjects based on your application needs.

For more information, see [Update compatibility type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-compatibility-type).

### Compatibility Mode Best practices

  * Don't use `None` as a compatibility type strategy because you run the risk of breaking clients with schema changes.

  * Choose a forward-based strategy such as `Forward` or `Forward-transitive` if you want to update producers first. Choose a backward-based strategy such as `Backward` or `Backward-transitive` if you want to update consumers first.

  * Choose a transitive strategy if you want to maintain compatibility with multiple previous schema versions. If you want to maximize compatibility and minimize the risk of breaking clients when updating schema versions, use the `Full-transitive` strategy.




## About schema references

Schema references allow you to define common structures once and refer to them from multiple schemas. For example an `Address` schema might be used as part of both a `Customer` and a `Supplier` schema.

This approach promotes reusability and consistency across your schemas. Additionally, using schema references creates clear dependencies, explicitly tracking which schemas rely on others. This improves the maintainability of your schema architecture.

When one schema needs to use another common schema, it includes a reference to that common schema. This relationship is formally defined by a `SchemaReference` structure.

A `SchemaReference` has the following components:

  * `name` (string): the fully qualified name of the schema being referenced for Avro formats or the filename of an imported type for Protobuf formats, as used within the schema definition itself.

  * `subject` (string): the name of the subject under which the referenced schema is registered in the schema registry.

  * `version` (int32): the specific version number of the referenced schema.




A schema that uses other schemas declares these dependencies in a `references` field. This field holds a list of `SchemaReference` objects.

### Example for schema references

Assume you need to define schemas for both `Customer` data and `Supplier` data, and both need to include an address. With schema references, you can define the address structure once and reuse it.

To follow this example, see [Create a subject](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one).

  1. Create a subject named `address_schema`, and register the definition for a standard address. When you create a subject for the first time, you are also creating version 1 of the schema for that subject.

###  Avro 

Create and store this as subject `address_schema_avro` version 1.
         
         {
           "type": "record",
           "name": "Address",
           "namespace": "com.example.common",
           "fields": [
             {"name": "street", "type": "string"},
             {"name": "city", "type": "string"},
             {"name": "zipCode", "type": "string"},
             {"name": "country", "type": "string", "default": "USA"}
           ]
         }
         

###  Protobuf 

Create and store this as subject `address_schema_proto` version 1.
         
         syntax = "proto3";
         
         package com.example.common;
         
         message Address {
           string street = 1;
           string city = 2;
           string zip_code = 3;
           string country = 4;
         }
         

  2. Create the `customer_schema` schema. Instead of repeating the address fields, you reference the `address_schema` schema.

###  Avro 

The `billingAddress` field's type `com.example.common.Address` refers to the `Address` schema defined in the previous step.
         
         {
           "type": "record",
           "name": "Customer",
           "namespace": "com.example.crm",
           "fields": [
             {"name": "customerId", "type": "long"},
             {"name": "customerName", "type": "string"},
             // This field's type refers to the Address schema
             {"name": "billingAddress", "type": "com.example.common.Address"}
           ]
         }
         

When registering `customer_schema_avro`, its metadata would include a schema reference:
         
         // Conceptual metadata for customer_schema_avro
         "references": [
           {
             "name": "com.example.common.Address",
             "subject": "address_schema_avro",
             "version": 1
           }
         ]
         

###  Protobuf 

The `customer.proto` file imports `address.proto` and uses `com.example.common.Address` for the `billing_address` field.
         
         syntax = "proto3";
         package com.example.crm;
         import "address.proto";
         
         message Customer {
           int64 customer_id = 1;
           string customer_name = 2;
           // This field's type refers to the imported Address message
           com.example.common.Address billing_address = 3;
         }
         

When registering `customer_schema_proto`, its metadata would include a schema reference:
         
         // Conceptual metadata for customer_schema_proto
         "references": [
           {
             "name": "address.proto",
             "subject": "address_schema_proto",
             "version": 1
           }
         ]
         

  3. Similarly, for your `Supplier` schema, you would add a schema reference pointing to the same common `Address` schema.




## About schema mode

Schema mode defines the operational state of a schema registry or a specific subject, and controls the types of modifications allowed. The schema mode can be applied to a registry or a specific subject within a schema registry. The following are the paths for the schema mode resources:

  * **Registry-level mode:** applies to the entire schema registry.

    * Path: `projects/project/locations/location/schemaRegistry/schema_registry/mode`
  * **Registry-level subject mode:** applies to a specific subject within the entire schema registry.

    * Path: `projects/project/locations/location/schemaRegistries/schema_registry/mode/subject`



The following modes are supported:

  * `Readonly`: in this mode, the schema registry or the specified subject or subjects cannot be updated. Modifications, such as updating configurations or adding new schema versions, are prevented.

  * `Readwrite`: this mode allows limited write operations on the schema registry or the specified subject or subjects. It enables modifications like updating configurations and adding new schema versions. This is the default mode for both new schema registries and new subjects.




When determining whether a modification is allowed for a specific subject, the mode set at the subject level takes precedence over the mode set at the schema registry level.

For example, if a schema registry is in `Readonly` mode, but a specific subject within it is in `Readwrite` mode, modifications to that specific subject is allowed. However, the creation of new subjects is restricted by the registry-level `Readonly` mode.

### Example for schema mode

Consider a schema registry with mode set to `Readwrite`. This configuration means you can add new subjects to the registry and new schema versions to existing subjects.

Assume that you have a subject named `production-config` that you want to protect from accidental changes. You set the mode for the `production-config` subject to `Readonly`. As a result, the following conditions apply to the `production-config` subject:

  * You cannot add new schema versions to the subject.

  * You cannot update the configuration (like compatibility type) for the subject.

  * Other subjects in the registry that don't have their own mode explicitly set remain in `Readwrite` mode, so you can still modify them.

  * You can continue to create subjects in the registry because the registry itself is still in `Readwrite` mode.




Later, you might decide to put the entire schema registry into a maintenance state by setting the registry-level mode to `Readonly`. However, you have another subject, `staging-config`, which needs to remain modifiable for ongoing testing. You explicitly set the mode for the `staging-config` subject to `Readwrite`. As a result, the following conditions apply to the `staging-config` subject:

  * The schema registry is now `Readonly`. You cannot create new subjects.

  * Most existing subjects such as those without a specific mode override also become `Readonly` by inheritance. You cannot add new schema versions to them or update their configurations.

  * The `production-config` subject remains `Readonly` as explicitly set.

  * The `staging-config` subject remains in `Readwrite` mode because its subject-level setting overrides the registry-level `Readonly` mode. You can continue to add schema versions and update configurations for `staging-config`.




This hierarchical approach provides flexibility in managing schema modifications at different levels of granularity.

For more information about how to update the schema mode, see [Update schema mode](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/update-schema-mode).

## Recommended configuration to use schema registry in production

To secure your schemas in a production environment, apply the following configurations:

  * Prevent the registration of new schemas by setting `mode=READONLY` for the entire schema registry or for the specific production topics.

  * Prevent Kafka clients from creating new schema versions by ensuring that they lack the `create version` permission. 

  * In your Kafka client serializers, set `auto.register.schemas=false`. For Kafka Connect, configure this setting for the key and value serializers as needed:

    * `key.serializer.auto.register.schemas=false`
    * `value.serializer.auto.register.schemas=false`
  * (Optional) To force clients to use the most recent schema for a subject, set `use.latest.version=true` in the serializer or deserializer. This setting directs the client to use the latest schema version registered for the subject, rather than the version that matches the specific message.




## What's next

  * [Create a schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-schema-registry)

  * [Create a subject](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/create-subject-version-one)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
