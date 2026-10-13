---
url: https://cloud.google.com/apis/design/resource_names/
title: AIP-122: Resource names
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:02.028254+00:00
---

# AIP-122: Resource names

> Source: https://cloud.google.com/apis/design/resource_names/

  * AIPs by Scope
  * [General](https://cloud.google.com/general)
  * [Google Cloud Platform](https://cloud.google.com/cloud)
  * [Auth](https://cloud.google.com/auth)
  * [Client libraries](https://cloud.google.com/client-libraries)
  * [Workspace](https://cloud.google.com/apps)
  * [Actions on Google](https://cloud.google.com/aog)
  * AIPs
  * [ 1 AIP Purpose and Guidelines ](https://cloud.google.com/1)
  * [ 2 AIP Numbering ](https://cloud.google.com/2)
  * [ 3 AIP Versioning ](https://cloud.google.com/3)
  * [ 8 AIP Style and Guidance ](https://cloud.google.com/8)
  * [ 9 Glossary ](https://cloud.google.com/9)
  * [ 100 API Design Review FAQ ](https://cloud.google.com/100)
  * [ 111 Planes ](https://cloud.google.com/111)
  * [ 121 Resource-oriented design ](https://cloud.google.com/121)
  * [ 122 Resource names ](https://cloud.google.com/122)
  * [ 123 Resource types ](https://cloud.google.com/123)
  * [ 124 Resource association ](https://cloud.google.com/124)
  * [ 126 Enumerations ](https://cloud.google.com/126)
  * [ 127 HTTP and gRPC Transcoding ](https://cloud.google.com/127)
  * [ 128 Declarative-friendly interfaces ](https://cloud.google.com/128)
  * [ 129 Server-Modified Values and Defaults ](https://cloud.google.com/129)
  * [ 130 Methods ](https://cloud.google.com/130)
  * [ 131 Standard methods: Get ](https://cloud.google.com/131)
  * [ 132 Standard methods: List ](https://cloud.google.com/132)
  * [ 133 Standard methods: Create ](https://cloud.google.com/133)
  * [ 134 Standard methods: Update ](https://cloud.google.com/134)
  * [ 135 Standard methods: Delete ](https://cloud.google.com/135)
  * [ 136 Custom methods ](https://cloud.google.com/136)
  * [ 140 Field names ](https://cloud.google.com/140)
  * [ 141 Quantities ](https://cloud.google.com/141)
  * [ 142 Time and duration ](https://cloud.google.com/142)
  * [ 143 Standardized codes ](https://cloud.google.com/143)
  * [ 144 Repeated fields ](https://cloud.google.com/144)
  * [ 145 Ranges ](https://cloud.google.com/145)
  * [ 146 Generic fields ](https://cloud.google.com/146)
  * [ 147 Sensitive fields ](https://cloud.google.com/147)
  * [ 148 Standard fields ](https://cloud.google.com/148)
  * [ 149 Unset field values ](https://cloud.google.com/149)
  * [ 151 Long-running operations ](https://cloud.google.com/151)
  * [ 152 Jobs ](https://cloud.google.com/152)
  * [ 153 Import and export ](https://cloud.google.com/153)
  * [ 154 Resource freshness validation ](https://cloud.google.com/154)
  * [ 155 Request identification ](https://cloud.google.com/155)
  * [ 156 Singleton resources ](https://cloud.google.com/156)
  * [ 157 Partial responses ](https://cloud.google.com/157)
  * [ 158 Pagination ](https://cloud.google.com/158)
  * [ 159 Reading across collections ](https://cloud.google.com/159)
  * [ 160 Filtering ](https://cloud.google.com/160)
  * [ 161 Field masks ](https://cloud.google.com/161)
  * [ 162 Resource Revisions ](https://cloud.google.com/162)
  * [ 163 Change validation ](https://cloud.google.com/163)
  * [ 164 Soft delete ](https://cloud.google.com/164)
  * [ 165 Criteria-based delete ](https://cloud.google.com/165)
  * [ 180 Backwards compatibility ](https://cloud.google.com/180)
  * [ 181 Stability levels ](https://cloud.google.com/181)
  * [ 182 External software dependencies ](https://cloud.google.com/182)
  * [ 184 API version identifiers ](https://cloud.google.com/184)
  * [ 185 API Versioning ](https://cloud.google.com/185)
  * [ 190 Naming conventions ](https://cloud.google.com/190)
  * [ 191 File and directory structure ](https://cloud.google.com/191)
  * [ 192 Documentation ](https://cloud.google.com/192)
  * [ 193 Errors ](https://cloud.google.com/193)
  * [ 194 Automatic retry configuration ](https://cloud.google.com/194)
  * [ 200 Precedent ](https://cloud.google.com/200)
  * [ 202 Fields ](https://cloud.google.com/202)
  * [ 203 Field behavior documentation ](https://cloud.google.com/203)
  * [ 205 Beta-blocking changes ](https://cloud.google.com/205)
  * [ 210 Unicode ](https://cloud.google.com/210)
  * [ 211 Authorization checks ](https://cloud.google.com/211)
  * [ 213 Common components ](https://cloud.google.com/213)
  * [ 214 Resource expiration ](https://cloud.google.com/214)
  * [ 215 API-specific protos ](https://cloud.google.com/215)
  * [ 216 States ](https://cloud.google.com/216)
  * [ 217 Unreachable resources ](https://cloud.google.com/217)
  * [ 231 Batch methods: Get ](https://cloud.google.com/231)
  * [ 233 Batch methods: Create ](https://cloud.google.com/233)
  * [ 234 Batch methods: Update ](https://cloud.google.com/234)
  * [ 235 Batch methods: Delete ](https://cloud.google.com/235)
  * [ 236 Policy preview ](https://cloud.google.com/236)

Resource names  
---  
Number| 122  
Permalink| [google.aip.dev/122](https://google.aip.dev/122)  
State| Approved  
Created| 2019-01-26  
Updated| 2019-01-26  
  
Contents

  * Guidance
    * Collection identifiers
    * Resource ID segments
    * Resource ID aliases
    * Full resource names
    * Resource URIs
    * Fields representing resource names
    * Fields representing a resource's parent
    * Fields representing another resource
  * Further reading
  * Rationale
    * Using names instead of IDs
    * Standardizing on name
    * Disallow embedding of resources
  * History
    * Disallowing UUIDs in user-specified IDs
  * Changelog



  * [File Bug](https://github.com/aip-dev/google.aip.dev/issues/)
  * [View source](https://github.com/aip-dev/google.aip.dev/blob/master/aip/general/0122.md)
  * [Edit this page](https://github.com/aip-dev/google.aip.dev/edit/master/aip/general/0122.md)



  1. [ API Improvement Proposals ](https://cloud.google.com/)
  2. [ General AIPs ](https://cloud.google.com/general)
  3. Resource names 



#### AIP-122

# Resource names

Most APIs expose _resources_ (their primary nouns) which users are able to create, retrieve, and manipulate. Additionally, resources are _named_ : each resource has a unique identifier that users use to reference that resource, and these names are what users should _store_ as the canonical names for the resources.

## Guidance

All resource names defined by an API **must** be unique within that API. (See the section on full resource names below for more information on referring to resources across APIs.)

Resource names are formatted according to the [URI path schema](https://datatracker.ietf.org/doc/html/rfc3986#appendix-A), but without the leading slash:
    
    
      publishers/123/books/les-miserables
      users/vhugo1802
    

  * Resource name components **should** usually alternate between collection identifiers (example: `publishers`, `books`, `users`) and resource IDs (example: `123`, `les-miserables`, `vhugo1802`).
  * Resource names **must** use the `/` character to separate individual segments of the resource name.
    * Non-terminal segments of a resource name **must not** contain a `/` character.
    * The terminal segment of a resource name **should not** contain a `/` character.
  * Resource names **should** only use characters available in DNS names, as defined by [RFC-1123](https://tools.ietf.org/html/rfc1123).
    * Additionally, resource IDs **should not** use upper-case letters.
    * If additional characters are necessary, resource names **should not** use characters that require URL-escaping, or characters outside of ASCII.
    * If Unicode characters can not be avoided, resource names **must** be stored in Normalization Form C (see [AIP-210](https://cloud.google.com/210)).
  * Resources **must** expose a `name` field that contains its resource name.
    * Resources **may** provide the resource ID as a separate field (e.g. `book_id`). This field **must** apply the [`OUTPUT_ONLY`](https://cloud.google.com/203#output-only) field behavior classification.
    * Resources **may** expose a separate, system-generated unique ID field [(`uid`)](https://cloud.google.com/148#uid). This field **must** apply the [`OUTPUT_ONLY`](https://cloud.google.com/203#output-only) field behavior classification.
    * Resources **must not** expose tuples, self-links, or other forms of resource identification.
    * All ID fields **should** be strings.



**Note:** Resource names as described here are used within the scope of a single API (or else in situations where the owning API is clear from the context), and are only required to be unique within that scope. For this reason, they are sometimes called _relative resource names_ to distinguish them from _full resource names_ (discussed below).

### Collection identifiers

The collection identifier segments in a resource name **must** be the plural form of the noun used for the resource. (For example, a collection of `Publisher` resources is called `publishers` in the resource name.)

  * Collection identifiers **must** be concise American English terms.
  * Collection identifiers **must** be in `camelCase`.
  * Collection identifiers **must** begin with a lower-cased letter and contain only ASCII letters and numbers (`/[a-z][a-zA-Z0-9]*/`).
  * Collection identifiers **must** be plural.
    * In situations where there is no plural word ("info"), or where the singular and plural terms are the same ("moose"), the non-pluralized (singular) form is correct. Collection segments **must not** "coin" words by adding "s" in such cases (e.g, avoid "infos").
  * Within any given single resource name, collection identifiers **must** be unique. (e.g. `people/xyz/people/abc` is invalid)



#### Nested collections

If a resource name contains multiple levels of a hierarchy, and a parent collection's name is used as a prefix for the child resource's name, the child collection's name **may** omit the prefix. For example, given a collection of `UserEvent` resources that would normally be nested underneath `users`:
    
    
    users/vhugo1802/userEvents/birthday-dinner-226
    

An API **should** use the less-redundant form:
    
    
    users/vhugo1802/events/birthday-dinner-226
    

In this situation, the _message_ and _resource type_ are still called `UserEvent`; only the collection and resource identifiers in the pattern(s) are shortened. Since the _resource type_ is not shortened, the `singular` and `plural` are similarly _not shortened_.
    
    
    message UserEvent {
      option (google.api.resource) = {
        type: "example.googleapis.com/UserEvent"
        // Only the collection & resource identfiers in the `pattern` are shortened.    
        pattern: "projects/{project}/users/{user}/events/{event}"
        singular: "userEvent"
        plural: "userEvents"
      };
    
      string name = 1;
    }
    

**Note:** APIs wishing to do this **must** follow this format consistently throughout all of its `pattern` entries defined and anywhere else the resource is referenced in the API, or else not at all.

### Resource ID segments

A resource ID segment identifies the resource within its parent collection. In the resource name `publishers/123/books/les-miserables`, `123` is the resource ID for the publisher, and `les-miserables` is the resource ID for the book.

  * If resource IDs are user-specified, the API **must** document allowed formats. User-specified resource IDs **should** conform to [RFC-1034](https://tools.ietf.org/html/rfc1034); which restricts to letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum.
    * Additionally, user-specified resource IDs **should** restrict letters to lower-case (`^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`).
    * Characters outside of ASCII **should not** be permitted; however, if Unicode characters are necessary, APIs **must** follow guidance in [AIP-210](https://cloud.google.com/210).
  * If resource IDs are not user-settable, the API **should** document the basic format, and any upper boundaries (for example, "at most 63 characters").
  * For more information, see the [create](https://cloud.google.com/133#user-specified-ids) standard method.



### Resource ID aliases

It is sometimes valuable to provide an alias for common lookup patterns for resource IDs. For example, an API with `users` at the top of its resource hierarchy may wish to provide `users/me` as a shortcut for retrieving information for the authenticated user.

APIs **may** provide programmatic aliases for common lookup patterns. However, all data returned from the API **must** use the canonical resource name.

### Full resource names

In most cases, resource names are used within a single API only, or else they are used in contexts where the owning API is clear (for example, `string pubsub_topic`).

However, sometimes it is necessary for services to refer to resources in an arbitrary API. In this situation, the service **should** use the _full resource name_ , a schemeless URI with the owning [API's service name](https://cloud.google.com/9#api-service-name), followed by the relative resource name:
    
    
    //library.googleapis.com/publishers/123/books/les-miserables
    //calendar.googleapis.com/users/vhugo1802
    

**Note:** The full resource name **should not** be used for cross-API references where the owning API is clear; it is only used if a field refers to resources in multiple APIs where ambiguity is possible.

### Resource URIs

The full resource name is a schemeless URI, but slightly distinct from the full URIs we use to access a resource. The latter includes the protocol (HTTPS), the API version, and the specific [service endpoint](https://cloud.google.com/9#api-service-endpoint) to target:
    
    
    https://library.googleapis.com/v1/publishers/123/books/les-miserables
    https://calendar.googleapis.com/v3/users/vhugo1802
    

The version is not included in the full resource name because the full resource name is expected to persist from version to version. Even though the API surface may change between major versions, multiple major versions of the same API are expected to use the same underlying data.

**Note:** The correlation between the full resource name and the service's endpoint is by convention. In particular, one service is able to have multiple endpoints (example use cases include regionalization, MTLS, and private access), and the full resource name does not change between these.

### Fields representing resource names

When defining a resource, the first field **should** be the resource name, which **must** be of type `string` and **must** be called `name` for the resource name. The message **should** include a `google.api.resource` annotation declaring the type (see [AIP-123](https://cloud.google.com/123) for more on this).
    
    
    // A representation of a book in the library.
    message Book {
      option (google.api.resource) = {
        type: "library.googleapis.com/Book"
        pattern: "publishers/{publisher}/books/{book}"
      };
    
      // The resource name of the book.
      // Format: publishers/{publisher}/books/{book}
      string name = 1 [(google.api.field_behavior) = IDENTIFIER];
    
      // Other fields...
    }
    

When defining a method that retrieves or acts on an already-existing resource (such as `GetBook` or `ArchiveBook`), the first field of the request message **should** be the resource name, which **must** be of type `string` and **must** be called `name` for the resource name. The field **should** also be annotated with the `google.api.resource_reference` annotation, referencing the resource type ([AIP-123](https://cloud.google.com/123)).
    
    
    // Request message for ArchiveBook
    message ArchiveBookRequest {
      // The book to archive.
      // Format: publishers/{publisher}/books/{book}
      string name = 1 [
        (google.api.field_behavior) = REQUIRED,
        (google.api.resource_reference) = {
          type: "library.googleapis.com/Book"
        }];
    
      // Other fields...
    }
    

**Note:** Fields **must not** be called `name` except for this purpose. For other use cases, either use a different term or prepend an adjective (for example: `display_name`).

### Fields representing a resource's parent

When defining a method that retrieves resources from a collection or adds a new resource to a collection (such as `ListBooks` or `CreateBook`), the first field of the request message **should** be of type `string` and **should** be called `parent` for the resource name of the collection. The `parent` field **should** also be annotated with the `google.api.resource_reference` annotation, referencing the parent's resource type ([AIP-123](https://cloud.google.com/123)).
    
    
    // Request message for ListBooks.
    message ListBooksRequest {
      // The publisher to list books from.
      // Format: publishers/{publisher_id}
      string parent = 1 [(google.api.resource_reference) = {
        type: "library.googleapis.com/Publisher"
      }];
    
      // Other fields (e.g. page_size, page_token, filter, etc.)...
    }
    

If there is more than one possible parent type, the `parent` field **should** be annotated with the `child_type` key on `google.api.resource_reference` instead:
    
    
    // Request message for ListBooks.
    message ListBooksRequest {
      // The parent to list books from.
      // Format:
      //   - publishers/{publisher_id}
      //   - authors/{author_id}
      string parent = 1 [
        (google.api.field_behavior) = REQUIRED,
        (google.api.resource_reference) = {
          child_type: "library.googleapis.com/Book"
        }];
    
      // Other fields (e.g. page_size, page_token, filter, etc.)...
    }
    

**Note:** Fields **should not** be called `parent` except for this purpose. For other use cases, use a synonymous term if possible.

### Fields representing another resource

When a field represents another resource, the field **should** be of type `string` and accept the resource name of the other resource. The field name **should** be equivalent to the corresponding message's name in snake case.

  * Field names **may** include a leading adjective if appropriate (such as `string dusty_book`).
  * Field names **should not** use the `_name` suffix unless the field would be ambiguous without it (e.g., `crypto_key_name`)
  * Fields representing another resource **should** provide the `google.api.resource_reference` annotation with the resource type being referenced.
  * If using the resource name is not possible and using the ID component alone is strictly necessary, the field **should** use an `_id` suffix (e.g. `shelf_id`).



The field **should not** be of type `message` using the `message` that implements the resource, **except** for one of following conditions:

  * The API is internal-only, has tight lifecycle relationships, and has a permission model that enables inherited access to embedded resources.
  * The embedding of the resource is done as part of the [AIP-162](https://cloud.google.com/162) revisions pattern.



Example of a resource reference:
    
    
    // A representation of a book in a library.
    message Book {
      option (google.api.resource) = {
        type: "library.googleapis.com/Book"
        pattern: "publishers/{publisher}/books/{book}"
      };
    
      // Name of the book.
      // Format is `publishers/{publisher}/books/{book}`
      string name = 1 [(google.api.field_behavior) = IDENTIFIER];
    
      // The shelf where the book currently sits.
      // Format is `shelves/{shelf}`.
      string shelf = 2 [(google.api.resource_reference) = {
        type: "library.googleapis.com/Shelf"
      }];
    
      // Other fields...
    }
    

## Further reading

  * For evolving resource names over time, see [AIP-180](https://cloud.google.com/180#changing-resource-names).
  * For resource types, see [AIP-123](https://cloud.google.com/123).



## Rationale

### Using names instead of IDs

For any large system, there are many kinds of resources. To use simple resource IDs to identify a resource, we'd actually need use a resource-specific tuple to reliably identify it, such as `(bucket, object)` or `(user, album, photo)`. This creates several issues:

  * Developers have to understand and remember such anonymous tuples.
  * Passing tuples is generally harder than passing strings.
  * Centralized infrastructures, such as logging and access control systems, don't understand specialized tuples.
  * Specialized tuples limit API design flexibility, such as providing reusable API interfaces. For example, [Long Running Operations](https://cloud.google.com/151) can work with many other API interfaces because they use flexible resource names.



### Standardizing on `name`

The concept of resource names is not a new one, and is formalized in Uniform Resource Names (URN) in conjunction with Uniform Resource Identifiers (URI) and Uniform Resource Locators (URL). Considering that the term "name" is so heavily overloaded in general, usage outside of a very well-defined meaning would be confusing for developers. So, the field name `name` is reserved in the context of AIP-compliant APIs so as to eliminate any confusion with resource names, and force other would be "name" fields to use a more specific field name.

### Disallow embedding of resources

Using a resource message directly as the type of a field within another resource is problematic for a number of reasons, which are as follows:

  * Complicates the resource lifecycle: If the dependency resource is deleted, what happens to the embedded reference in the dependent resource? Data retention and clean up operations will be significantly complicated.
  * Bypasses permissions: If every resource has its own set of permissions, a user with read permission on the dependent resource that doesn't have the same permission on the dependency resource suddenly cannot see the full resource.
  * Tightly couples resources in all aspects: Changing the requirements in the schema, permissions, or otherwise for either resource impacts the other, significantly increasing complexity of roll outs.



Referencing by name, as is recommended, eliminates all of this complexity by preventing resource data duplication, and forcing the owning service to be involved in the resolution of the reference (via Standard Methods), guaranteeing isolation of logical concerns per-resource.

## History

### Disallowing UUIDs in user-specified IDs

As part of an effort to make APIs more declarative-friendly, APIs were required to allow user-specified resource ID on creation. As part of this, a supporting field `string uid` containing a UUID was also encouraged. Guidance was then added to discourage the _user-specified resource ID_ from being a UUID or even resembling one.

Ostensibly, the fact that `uid` contained a service-generated UUID motivated this restriction on the user-specified resource ID, forcing the user-specified resource ID to be a more "meaningful" value. However, we no longer saw value in this requirement, hence its removal.

## Changelog

  * **2025-03-10** : Drop guidance disallowing UUID in user-specified ID.
  * **2024-10-15** : Add some rationale we found for use of `name` as a field and instead of IDs as an identifier.
  * **2024-06-14** : Clarify resource annotation shortening rules for nested collections.
  * **2023-09-19** : Prohibit duplicate collection identifiers.
  * **2023-09-01** : Add a clause that allows embedding for revision resource messages.
  * **2023-08-10** : Explicitly disallow embedding resource messages in a resource.
  * **2023-03-24** : Correction: full resource name contains the service name rather than the service endpoint
  * **2023-03-17** : Add `OUTPUT_ONLY` guidance for resource ID fields.
  * **2020-10-06** : Added declarative-friendly guidance, and tightened character set restrictions.
  * **2020-10-05** : Clarified when full resource names are used.
  * **2020-05-19** : Clarified that resource _IDs_ avoid capital characters, not the entire resource _name_.
  * **2020-04-27** : Tighten the restriction on valid characters.
  * **2019-12-05** : Added guidance for resource annotations.
  * **2019-08-01** : Changed the examples from "shelves" to "publishers", to present a better example of resource ownership. Also changed the final example from a Pub/Sub example to the usual Book example.
  * **2019-07-30** : Changed the nested collection brevity suggestion from "may" to "should"

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see [content licensing](https://cloud.google.com/licensing).
