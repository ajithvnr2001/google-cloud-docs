---
url: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value/
title: Class Value (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:05.224852+00:00
---

# Class Value (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class Value (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) class represents a type-safe, nullable Spanner value. 

It is conceptually similar to a `std::any` except the only allowed types are those supported by Spanner, and a "null" value (similar to a `std::any` without a value) still has an associated type. The supported types are shown in the following table along with how they map to the Spanner types (<https://cloud.google.com/spanner/docs/data-types>):

Spanner Type | C++ Type `T`  
---|---  
BOOL | `bool`  
INT64 | `std::int64_t`  
FLOAT32 | `float`  
FLOAT64 | `double`  
STRING | `std::string`  
BYTES | [`google::cloud::spanner::Bytes`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Bytes)  
JSON | [`google::cloud::spanner::Json`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Json)  
JSONB | [`google::cloud::spanner::JsonB`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1JsonB)  
NUMERIC | [`google::cloud::spanner::Numeric`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner)  
NUMERIC(PG) | [`google::cloud::spanner::PgNumeric`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner)  
OID(PG) | [`google::cloud::spanner::PgOid`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1PgOid)  
TIMESTAMP | [`google::cloud::spanner::Timestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp)  
DATE | `absl::CivilDay`  
INTERVAL | [`google::cloud::spanner::Interval`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Interval)  
UUID | [`google::cloud::spanner::Uuid`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Uuid)  
ENUM | [`google::cloud::spanner::ProtoEnum`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ProtoEnum)`<E>`  
PROTO | [`google::cloud::spanner::ProtoMessage`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ProtoMessage)`<M>`  
ARRAY | `std::vector<T>` // [1]  
STRUCT | `std::tuple<Ts...>`  
  
[1] The type `T` may be any of the other supported types, except for ARRAY/`std::vector`.

[Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) is a regular C++ value type with support for copy, move, equality, etc. A default-constructed [Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) represents an empty value with no type.

**Note:** There is also a C++ type of [`CommitTimestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1CommitTimestamp) that corresponds to a Cloud Spanner TIMESTAMP object for setting the commit timestamp on a column with the `allow_commit_timestamp` set to `true` in the schema. 

###### See Also

<https://cloud.google.com/spanner/docs/commit-timestamp> Callers may create instances by passing any of the supported values (shown in the table above) to the constructor. "Null" values are created using the `MakeNullValue<T>()` factory function or by passing an empty `std::optional<T>` to the [Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) constructor..

###### Example

Using a non-null value. 
    
    
    std::string msg = "hello";
    spanner::Value v(msg);
    StatusOr<std::string> copy = v.get<std::string>();
    if (copy) {
      std::cout << *copy;  // prints "hello"
    }
    

###### Example

Using a null value. 
    
    
    spanner::Value v = spanner::MakeNullValue<std::int64_t>();
    StatusOr<std::int64_t> i = v.get<std::int64_t>();
    assert(!i.ok());  // Can't get the value because v is null
    StatusOr < std::optional<std::int64_t> j =
        v.get<std::optional<std::int64_t>>();
    assert(j.ok());  // OK because an empty option can represent the null
    assert(!j->has_value());  // v held no value.
    

###### Nullness

All of the supported types (above) are "nullable". A null is created in one of two ways:

  1. Passing an `std::optional<T>()` with no value to [`Value`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value)'s constructor.
  2. Using the `MakeNullValue<T>()` helper function (defined below).



Nulls can be retrieved from a [`Value::get`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value#classgoogle_1_1cloud_1_1spanner_1_1Value_1ab39e0fe676f40daad5a93ce88a711fe9)`<T>` by specifying the type `T` as an `std::optional<U>`. The returned optional will either be empty (indicating null) or it will contain the actual value. See the documentation for [`Value::get`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value#classgoogle_1_1cloud_1_1spanner_1_1Value_1ab39e0fe676f40daad5a93ce88a711fe9)`<T>` below for more details.

###### Spanner Arrays

Spanner arrays are represented in C++ as a `std::vector<T>`, where the type `T` may be any of the other allowed Spanner types, such as `bool`, `std::int64_t`, etc. The only exception is that arrays may not directly contain another array; to achieve a similar result you could create an array of a 1-element struct holding an array. The following examples show usage of arrays.
    
    
    std::vector<std::int64_t> vec = {1, 2, 3, 4, 5};
    spanner::Value v(vec);
    auto copy = *v.get<std::vector<std::int64_t>>();
    assert(vec == copy);
    

###### Spanner Structs

Spanner structs are represented in C++ as instances of `std::tuple` holding zero or more of the allowed Spanner types, such as `bool`, `std::int64_t`, `std::vector`, and even other `std::tuple` objects. Each tuple element corresponds to a single field in a Spanner STRUCT.

Spanner STRUCT fields may optionally contain a string indicating the field's name. Fields names may be empty, unique, or repeated. A named field may be specified as a tuple element of type `std::pair<std::string, T>`, where the pair's `.first` member indicates the field's name, and the `.second` member is any valid Spanner type `T`.
    
    
    using Struct = std::tuple<bool, std::pair<std::string, std::int64_t>>;
    Struct s  = {true, {"Foo", 42}};
    spanner::Value v(s);
    assert(s == *v.get<Struct>());
    

**Note:** While a STRUCT's (optional) field names are not part of its C++ type, they are part of its Spanner STRUCT type. Array's (i.e., `std::vector`) must contain a single element type, therefore it is an error to construct a `std::vector` of `std::tuple` objects with differently named fields. 

## Constructors 

### Value()

Constructs a [`Value`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) that holds nothing. 

All calls to `get<T>()` will return an error. 

### Value(Value const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `Value const &`   
  
  
### Value(Value &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `Value &&`   
  
  
### Value(bool)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `bool`   
  
  
### Value(std::int64_t)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `std::int64_t`   
  
  
### Value(float)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `float`   
  
  
### Value(double)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `double`   
  
  
### Value(std::string)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `std::string`   
  
  
### Value(Bytes)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `Bytes`   
  
  
### Value(Json)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `Json`   
  
  
### Value(JsonB)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `JsonB`   
  
  
### Value(Numeric)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `Numeric`   
  
  
### Value(PgNumeric)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `PgNumeric`   
  
  
### Value(PgOid)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `PgOid`   
  
  
### Value(Timestamp)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `Timestamp`   
  
  
### Value(CommitTimestamp)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `CommitTimestamp`   
  
  
### Value(absl::CivilDay)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `absl::CivilDay`   
  
  
### Value(Interval)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `Interval`   
  
  
### Value(Uuid)

Constructs an instance with the specified type and value. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `Uuid`   
  
  
### Value(ProtoEnum< E >)

Constructs an instance with the specified type and value. 

**Parameters**  
---  
**Name** | **Description**  
`v` |  `ProtoEnum< E >`   
  
`typename E` |  ``   
  
  
### Value(ProtoMessage< M >)

Constructs an instance with the specified type and value. 

**Parameters**  
---  
**Name** | **Description**  
`v` |  `ProtoMessage< M >`   
  
`typename M` |  ``   
  
  
### Value(int)

Constructs an instance from common C++ literal types that closely, though not exactly, match supported Spanner types. 

An integer literal in C++ is of type `int`, which is not exactly an allowed Spanner type. This will be allowed but it will be implicitly up converted to a `std::int64_t`. Similarly, a C++ string literal will be implicitly converted to a `std::string`. For example:
    
    
    spanner::Value v1(42);
    assert(42 == *v1.get<std::int64_t>());
    
    spanner::Value v2("hello");
    assert("hello" == *v2.get<std::string>());
    

**Parameter**  
---  
**Name** | **Description**  
`v` |  `int`   
  
  
### Value(char const *)

Constructs an instance from common C++ literal types that closely, though not exactly, match supported Spanner types. 

An integer literal in C++ is of type `int`, which is not exactly an allowed Spanner type. This will be allowed but it will be implicitly up converted to a `std::int64_t`. Similarly, a C++ string literal will be implicitly converted to a `std::string`. For example:
    
    
    spanner::Value v1(42);
    assert(42 == *v1.get<std::int64_t>());
    
    spanner::Value v2("hello");
    assert("hello" == *v2.get<std::string>());
    

**Parameter**  
---  
**Name** | **Description**  
`v` |  `char const *`   
  
  
### Value(std::optional< T >)

Constructs a non-null instance if `opt` has a value, otherwise constructs a null instance with the specified type `T`. 

**Parameters**  
---  
**Name** | **Description**  
`opt` |  `std::optional< T >`   
  
`typename T` |  ``   
  
  
### Value(std::vector< T >)

Constructs an instance from a Spanner ARRAY of the specified type and values. 

The type `T` may be any valid type shown above, except vectors of vectors are not allowed.

**Warning:** If `T` is a `std::tuple` with field names (i.e., at least one of its element types is a `std::pair<std::string, T>`) then, all of the vector's elements must have exactly the same field names. Any mismatch in in field names results in undefined behavior. 

**Parameters**  
---  
**Name** | **Description**  
`v` |  `std::vector< T >`   
  
`typename T` |  ``   
  
  
### Value(std::tuple< Ts... >)

Constructs an instance from a Spanner STRUCT with a type and values matching the given `std::tuple`. 

Any STRUCT field may optionally have a name, which is specified as `std::pair<std::string, T>`. 

**Parameters**  
---  
**Name** | **Description**  
`tup` |  `std::tuple< Ts... >`   
  
`typename...` |  ``   
  
  
## Operators 

### operator=(Value const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `Value const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Value &` |   
  
### operator=(Value &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `Value &&`   
  
**Returns**  
---  
**Type** | **Description**  
`Value &` |   
  
## Functions 

### get() const &

Returns the contained value wrapped in a [`google::cloud::StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>`. 

Returns a non-OK status IFF:

  * The contained value is "null", and `T` is not an `std::optional`.
  * There is an error converting the contained value to `T`.



###### Example
    
    
    spanner::Value v{3.14};
    StatusOr<double> d = v.get<double>();
    if (d) {
      std::cout << "d=" << *d;
    }
    
    // Now using a "null" std::int64_t
    v = spanner::MakeNullValue<std::int64_t>();
    StatusOr<std::int64_t> i = v.get<std::int64_t>();
    if (!i) {
      std::cerr << "Could not get integer: " << i.status();
    }
    StatusOr<std::optional<std::int64_t>> j =
        v.get<std::optional<std::int64_t>>();
    assert(j.ok());  // Since we know the types match in this example
    assert(!v->has_value());  // Since we know v was null in this example
    

**Parameter**  
---  
**Name** | **Description**  
`typename T` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< T >` |   
  
### get() &&

Returns the contained value wrapped in a [`google::cloud::StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>`. 

Returns a non-OK status IFF:

  * The contained value is "null", and `T` is not an `std::optional`.
  * There is an error converting the contained value to `T`.



###### Example
    
    
    spanner::Value v{3.14};
    StatusOr<double> d = v.get<double>();
    if (d) {
      std::cout << "d=" << *d;
    }
    
    // Now using a "null" std::int64_t
    v = spanner::MakeNullValue<std::int64_t>();
    StatusOr<std::int64_t> i = v.get<std::int64_t>();
    if (!i) {
      std::cerr << "Could not get integer: " << i.status();
    }
    StatusOr<std::optional<std::int64_t>> j =
        v.get<std::optional<std::int64_t>>();
    assert(j.ok());  // Since we know the types match in this example
    assert(!v->has_value());  // Since we know v was null in this example
    

**Parameter**  
---  
**Name** | **Description**  
`typename T` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< T >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
