---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/blobstore/
title: Package google.golang.org/appengine/v2/blobstore (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:47.788294+00:00
---

# Package google.golang.org/appengine/v2/blobstore (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/blobstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/blobstore (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/blobstore). 

Package blobstore provides a client for App Engine's persistent blob storage service.

## Functions 

### func BlobKeyForFile 
    
    
    func BlobKeyForFile(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), filename [string](https://pkg.go.dev/builtin#string)) ([appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey), [error](https://pkg.go.dev/builtin#error))

BlobKeyForFile returns a BlobKey for a Google Storage file. The filename should be of the form "/gs/bucket_name/object_name".

### func Delete 
    
    
    func Delete(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), blobKey [appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a blob.

### func DeleteMulti 
    
    
    func DeleteMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), blobKey [][appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey)) [error](https://pkg.go.dev/builtin#error)

DeleteMulti deletes multiple blobs.

### func ParseUpload 
    
    
    func ParseUpload(req *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request)) (blobs map[[string](https://pkg.go.dev/builtin#string)][]*BlobInfo, other [url](https://pkg.go.dev/net/url).[Values](https://pkg.go.dev/net/url#Values), err [error](https://pkg.go.dev/builtin#error))

ParseUpload parses the synthetic POST request that your app gets from App Engine after a user's successful upload of blobs. Given the request, ParseUpload returns a map of the blobs received (keyed by HTML form element name) and other non-blob POST parameters.

### func Send 
    
    
    func Send(response [http](https://pkg.go.dev/net/http).[ResponseWriter](https://pkg.go.dev/net/http#ResponseWriter), blobKey [appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey))

Send sets the headers on response to instruct App Engine to send a blob as the response body. This is more efficient than reading and writing it out manually and isn't subject to normal response size limits.

### func UploadURL 
    
    
    func UploadURL(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), successPath [string](https://pkg.go.dev/builtin#string), opts *UploadURLOptions) (*[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL), [error](https://pkg.go.dev/builtin#error))

UploadURL creates an upload URL for the form that the user will fill out, passing the application path to load when the POST of the form is completed. These URLs expire and should not be reused. The opts parameter may be nil.

## BlobInfo
    
    
    type BlobInfo struct {
    	BlobKey      appengine.BlobKey
    	ContentType  [string](https://pkg.go.dev/builtin#string)    `datastore:"content_type"`
    	CreationTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) `datastore:"creation"`
    	Filename     [string](https://pkg.go.dev/builtin#string)    `datastore:"filename"`
    	Size         [int64](https://pkg.go.dev/builtin#int64)     `datastore:"size"`
    	MD5          [string](https://pkg.go.dev/builtin#string)    `datastore:"md5_hash"`
    
    	// ObjectName is the Google Cloud Storage name for this blob.
    	ObjectName [string](https://pkg.go.dev/builtin#string) `datastore:"gs_object_name"`
    }

BlobInfo is the blob metadata that is stored in the datastore. Filename may be empty.

### func Stat 
    
    
    func Stat(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), blobKey [appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey)) (*BlobInfo, [error](https://pkg.go.dev/builtin#error))

Stat returns the BlobInfo for a provided blobKey. If no blob was found for that key, Stat returns datastore.ErrNoSuchEntity.

## Reader
    
    
    type Reader interface {
    	[io](https://pkg.go.dev/io).[Reader](https://pkg.go.dev/io#Reader)
    	[io](https://pkg.go.dev/io).[ReaderAt](https://pkg.go.dev/io#ReaderAt)
    	[io](https://pkg.go.dev/io).[Seeker](https://pkg.go.dev/io#Seeker)
    }

Reader is a blob reader.

### func NewReader 
    
    
    func NewReader(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), blobKey [appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey)) Reader

NewReader returns a reader for a blob. It always succeeds; if the blob does not exist then an error will be reported upon first read.

## UploadURLOptions
    
    
    type UploadURLOptions struct {
    	MaxUploadBytes        [int64](https://pkg.go.dev/builtin#int64) // optional
    	MaxUploadBytesPerBlob [int64](https://pkg.go.dev/builtin#int64) // optional
    
    	// StorageBucket specifies the Google Cloud Storage bucket in which
    	// to store the blob.
    	// This is required if you use Cloud Storage instead of Blobstore.
    	// Your application must have permission to write to the bucket.
    	// You may optionally specify a bucket name and path in the format
    	// "bucket_name/path", in which case the included path will be the
    	// prefix of the uploaded object's name.
    	StorageBucket [string](https://pkg.go.dev/builtin#string)
    }

UploadURLOptions are the options to create an upload URL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
