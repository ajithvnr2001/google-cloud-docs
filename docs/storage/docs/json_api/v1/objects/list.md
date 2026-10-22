---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list/
title: Objects: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:50.253277+00:00
---

# Objects: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: list Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of objects matching the criteria, ordered in the list lexicographically by name.

In [buckets with a flat namespace](https://docs.cloud.google.com/storage/docs/objects#flat-namespace), the use of the `delimiter` parameter in conjunction with the `prefix` filter allows the `list` method to operate like a directory listing. For example, consider a bucket that contains the objects "a/b", "a/c", "d", "e", "e/f", and "e/g/h":

  * If `delimiter` is set to "/" and `prefix` is not set, then an object listing of the bucket returns object metadata for objects "d" and "e". It also returns "a/" and "e/" in the `prefixes[]` list.
  * If `delimiter` is set to "/" and `prefix` is set to "e/", then an object listing of the bucket returns object metadata for object "e/f". It also returns "g/" in the `prefixes[]` list.



## Required permissions

The authenticated user must have the `storage.objects.list` IAM permission to use this method. To return object ACLs, the authenticated user must also have the `storage.objects.getIamPolicy` permission.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/o

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which to look for objects.   
**Optional query parameters**  
`filter` | `string` |  Filter results to include only objects to which the specified [context](https://docs.cloud.google.com/storage/docs/object-contexts) is attached. For information about the syntax that is supported, see [Filter by object context](https://docs.cloud.google.com/storage/docs/listing-objects#filter-by-object-contexts).   
`delimiter` | `string` |  Returns results in a directory-like mode, with `/` being a common value for the delimiter. 

  * `items[]` contains object metadata for objects whose names do not contain `delimiter`, or whose names only have instances of `delimiter` in their `prefix`.
  * `prefixes[]` contains truncated object names for objects whose names contain `delimiter` after any `prefix`, and can also contain empty folders and managed folders when `includeFoldersAsPrefixes` is `true`. Object names are truncated beyond the first applicable instance of the delimiter, mimicking a directory. If multiple objects have the same truncated name, duplicates are omitted. Truncated object names in `prefixes[]` always end with `/`.

`delimiter` must be either excluded or set to `/` in requests that use the `matchGlob` parameter, and `delimiter` must be set to `/` in requests that use the `includeFoldersAsPrefixes` parameter, which returns managed folders.  
`endOffset` | `string` |  Filter results to objects whose names are lexicographically before `endOffset`. If `startOffset` is also set, the objects listed have names between `startOffset` (inclusive) and `endOffset` (exclusive).   
`includeFoldersAsPrefixes` | `boolean` |  If true, includes empty [ folders](https://docs.cloud.google.com/storage/docs/folders-overview) and [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) in results, within `prefixes[]`. If this parameter is used, `delimiter` must be set to `/`.   
`includeTrailingDelimiter` | `boolean` |  If true, objects that end in exactly one instance of `delimiter` have their metadata included in `items[]` in addition to the relevant part of the object name appearing in `prefixes[]`.   
`maxResults` | `integer` |  Maximum combined number of entries in `items[]` and `prefixes[]` to return in a single page of responses. The service may return fewer results than `maxResults` so the presence of `nextPageToken` should always be checked. The recommended upper value for `maxResults` is 1000 objects in a single response.   
`matchGlob` | `string` |  A [glob pattern](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-object-glob) used to filter results (for example, `foo*bar`). The value must be UTF-8 encoded and has a maximum size of 1024 bytes. Objects that match the glob are returned in `items[]`. When `delimiter` is used in conjunction with `matchGlob`, it must be set to `/`. Object prefixes that contain the delimiter and match the glob are returned in `prefixes[]`. If `delimiter` is not set, the `prefixes[]` field is empty in the response. See List prefixes only for information on how to list only object prefixes.  
`pageToken` | `string` |  A previously-returned page token representing part of the larger set of results to view.   
  
The `pageToken` is an encoded field that marks the name and generation of the last object in the returned list. In a subsequent request using the `pageToken`, items that come after the `pageToken` are shown (up to `maxResults`).   
  
If you start a listing and then create an object in the bucket before using a `pageToken` to continue listing, you do not see the new object in subsequent listing results if it is in part of the object namespace already listed.   
`prefix` | `string` |  Filter results to include only objects whose names begin with this prefix. When `prefix` is set, the names of the objects returned in the response are relative to the root of the bucket.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`.   
  
Acceptable values are: 

  * `full`: Include all properties. 
  * `noAcl`: Omit the `owner`, `acl` property. 

  
`startOffset` | `string` |  Filter results to objects whose names are lexicographically equal to or after `startOffset`. If `endOffset` is also set, the objects listed have names between `startOffset` (inclusive) and `endOffset` (exclusive).   
`softDeleted` | `boolean` |  If `true`, only returns [soft-deleted objects](https://docs.cloud.google.com/storage/docs/soft-delete) as part of the objects list response. Soft-deleted objects are returned as distinct results in order of increasing generation number. The `softDeleted` parameter can only be used successfully if the bucket has a soft delete policy. Otherwise, the request fails with a `400 Bad Request` error with the reason `invalidArgument`. If `true`, `versions` cannot be set to `true`.   
`versions` | `boolean` |  If `true`, lists all versions of an object as distinct results in order of increasing generation number. The default value for `versions` is `false`. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).   
  
### Request body

Do not supply a request body with this method.

## List objects and prefixes using glob

When the `matchGlob` query parameter is set to a glob pattern, the objects list operation only returns objects that match the glob pattern in `items[]`. When `delimiter` is set to `/` in conjunction with `matchGlob`, the objects list operation additionally filters results for object prefixes, where prefixes that match the given glob are returned in `prefixes[]`. To learn how to list prefixes only, see List prefixes only.

Cloud Storage supports the following syntax for glob patterns:

Syntax | Description | Notes  
---|---|---  
`?` | Match any single character, excluding `/`. |   
`*` | Match zero or more characters, excluding `/`. |   
`**` | Match zero or more characters, including `/`. |   
`**/` | Match zero or more characters that end in `/`. As a special case, if at a directory boundary, can match zero characters even if the trailing slash is not present. For example, the glob pattern `foo/**/bar` can be used to match `foo/bar` and `foo/baz/bar`. | A directory boundary exists at the beginning of the pattern and immediately after each slash (`/`).  
`[abc]` | Match exactly one of the characters between the brackets. |   
`[a-z]` | Match exactly one character that is in the inclusive range `a` to `z`. | Within a single character class, multiple ranges and characters can be used. For example, `[0-9XYZa-z]` is the union of `[0-9]`, `[XYZ]`, and `[a-z]`.  
`[!abc]` or `[^abc]` | Match exactly one character that is not in the character class defined by `[abc]`. | Within a single character class, multiple ranges and characters can be used. For example, `[!0-9XYZa-z]` is the intersection of `[!0-9]`, `[!XYZ]`, and `[!a-z]`.  
`{abc,xyz}` | Match one of `abc` or `xyz`. |   
`{foo,{a,b}{x,y},bar}` | Match one of `foo`, `ax`, `ay`, `bx`, `by`, or `bar`. |   
`{foo*,*bar}` | Match anything prefixed with `foo` or suffixed with `bar`. | Excludes `/` characters.  
`\?` | Match the character after the backslash without interpreting it as a special character. Special characters are `?`, `*`, `\`, `[`, `]`, `{`, and `}`. |   
**Note:** Brace expansions (`{}`) cannot contain slashes (`/`) or double asterisks (`**`). 

For example, to filter for the object `foo/bar/dog.jpeg`, `matchGlob` should be set to `foo/bar/*?`. 

### List prefixes only

To use `matchGlob` to filter for prefixes, `delimiter` must be set to `/`. Object prefixes always end with `/`, so glob patterns that match a trailing `/` (for example, `**/`) can be used to filter results to object prefixes only. Glob patterns that match a trailing `?` (for example, `**?`) can be used to filter results to objects only.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "storage#objects",
      "nextPageToken": string,
      "prefixes": [
        string
      ],
      "items": [
        [objects Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource)
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For lists of objects, this is always `"storage#objects"`. |   
`nextPageToken` | `string` | The continuation token. Provide this value as the `pageToken` of a subsequent request in order to return the next page of results. Note that the next page may be empty. If this is the last page of results, then no continuation token is returned. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results. |   
`prefixes[]` | `list` | Object name prefixes for objects that matched the listing request but were excluded from `items[]` because of a delimiter. Values in this list are object names up to and including the requested delimiter. Duplicate entries are omitted from this list. If `matchGlob` was used in the request, only prefixes matching the glob pattern are returned. |   
`items[]` | `list` | The list of [objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects), ordered lexicographically by name. If `matchGlob` was used in the request, only objects matching the glob pattern are returned. |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
