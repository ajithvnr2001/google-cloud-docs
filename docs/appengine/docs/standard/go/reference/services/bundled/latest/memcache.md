---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/memcache/
title: Package google.golang.org/appengine/v2/memcache (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:50.360692+00:00
---

# Package google.golang.org/appengine/v2/memcache (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/memcache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/memcache (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/memcache). 

Package memcache provides a client for App Engine's distributed in-memory key-value store for small chunks of arbitrary data. 

The fundamental operations get and set items, keyed by a string.
    
    
    item0, err := memcache.Get(c, "key")
    if err != nil && err != memcache.ErrCacheMiss {
        return err
    }
    if err == nil {
        fmt.Fprintf(w, "memcache hit: Key=%q Val=[% x]\n", item0.Key, item0.Value)
    } else {
        fmt.Fprintf(w, "memcache miss\n")
    }

and
    
    
    item1 := &memcache.Item{
        Key:   "foo",
        Value: []byte("bar"),
    }
    if err := memcache.Set(c, item1); err != nil {
        return err
    }

## Variables 

### ErrCacheMiss, ErrCASConflict, ErrNoStats, ErrNotStored, ErrServerError
    
    
    var (
    	// ErrCacheMiss means that an operation failed
    	// because the item wasn't present.
    	ErrCacheMiss = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("memcache: cache miss")
    	// ErrCASConflict means that a CompareAndSwap call failed due to the
    	// cached value being modified between the Get and the CompareAndSwap.
    	// If the cached value was simply evicted rather than replaced,
    	// ErrNotStored will be returned instead.
    	ErrCASConflict = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("memcache: compare-and-swap conflict")
    	// ErrNoStats means that no statistics were available.
    	ErrNoStats = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("memcache: no statistics available")
    	// ErrNotStored means that a conditional write operation (i.e. Add or
    	// CompareAndSwap) failed because the condition was not satisfied.
    	ErrNotStored = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("memcache: item not stored")
    	// ErrServerError means that a server error occurred.
    	ErrServerError = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("memcache: server error")
    )

### Gob, JSON
    
    
    var (
    	// Gob is a Codec that uses the gob package.
    	Gob = Codec{gobMarshal, gobUnmarshal}
    	// JSON is a Codec that uses the json package.
    	JSON = Codec{[json](https://pkg.go.dev/encoding/json).[Marshal](https://pkg.go.dev/encoding/json#Marshal), [json](https://pkg.go.dev/encoding/json).[Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)}
    )

## Functions 

### func Add 
    
    
    func Add(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item *Item) [error](https://pkg.go.dev/builtin#error)

Add writes the given item, if no value already exists for its key. ErrNotStored is returned if that condition is not met.

### func AddMulti 
    
    
    func AddMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item []*Item) [error](https://pkg.go.dev/builtin#error)

AddMulti is a batch version of Add. appengine.MultiError may be returned.

### func CompareAndSwap 
    
    
    func CompareAndSwap(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item *Item) [error](https://pkg.go.dev/builtin#error)

CompareAndSwap writes the given item that was previously returned by Get, if the value was neither modified or evicted between the Get and the CompareAndSwap calls. The item's Key should not change between calls but all other item fields may differ. ErrCASConflict is returned if the value was modified in between the calls. ErrNotStored is returned if the value was evicted in between the calls.

### func CompareAndSwapMulti 
    
    
    func CompareAndSwapMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item []*Item) [error](https://pkg.go.dev/builtin#error)

CompareAndSwapMulti is a batch version of CompareAndSwap. appengine.MultiError may be returned.

### func Delete 
    
    
    func Delete(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

Delete deletes the item for the given key. ErrCacheMiss is returned if the specified item can not be found. The key must be at most 250 bytes in length.

### func DeleteMulti 
    
    
    func DeleteMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [][string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

DeleteMulti is a batch version of Delete. If any keys cannot be found, an appengine.MultiError is returned. Each key must be at most 250 bytes in length.

### func Flush 
    
    
    func Flush(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [error](https://pkg.go.dev/builtin#error)

Flush flushes all items from memcache.

### func GetMulti 
    
    
    func GetMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [][string](https://pkg.go.dev/builtin#string)) (map[[string](https://pkg.go.dev/builtin#string)]*Item, [error](https://pkg.go.dev/builtin#error))

GetMulti is a batch version of Get. The returned map from keys to items may have fewer elements than the input slice, due to memcache cache misses. Each key must be at most 250 bytes in length.

### func Increment 
    
    
    func Increment(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [string](https://pkg.go.dev/builtin#string), delta [int64](https://pkg.go.dev/builtin#int64), initialValue [uint64](https://pkg.go.dev/builtin#uint64)) (newValue [uint64](https://pkg.go.dev/builtin#uint64), err [error](https://pkg.go.dev/builtin#error))

Increment atomically increments the decimal value in the given key by delta and returns the new value. The value must fit in a uint64. Overflow wraps around, and underflow is capped to zero. The provided delta may be negative. If the key doesn't exist in memcache, the provided initial value is used to atomically populate it before the delta is applied. The key must be at most 250 bytes in length.

### func IncrementExisting 
    
    
    func IncrementExisting(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [string](https://pkg.go.dev/builtin#string), delta [int64](https://pkg.go.dev/builtin#int64)) (newValue [uint64](https://pkg.go.dev/builtin#uint64), err [error](https://pkg.go.dev/builtin#error))

IncrementExisting works like Increment but assumes that the key already exists in memcache and doesn't take an initial value. IncrementExisting can save work if calculating the initial value is expensive. An error is returned if the specified item can not be found.

### func PeekMulti 
    
    
    func PeekMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [][string](https://pkg.go.dev/builtin#string)) (map[[string](https://pkg.go.dev/builtin#string)]*Item, [error](https://pkg.go.dev/builtin#error))

PeekMulti is a batch version of Peek. It is similar to GetMulti but additionally populates Item.Timestamps.

### func Set 
    
    
    func Set(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item *Item) [error](https://pkg.go.dev/builtin#error)

Set writes the given item, unconditionally.

### func SetMulti 
    
    
    func SetMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item []*Item) [error](https://pkg.go.dev/builtin#error)

SetMulti is a batch version of Set. appengine.MultiError may be returned.

## Codec
    
    
    type Codec struct {
    	Marshal   func(interface{}) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))
    	Unmarshal func([][byte](https://pkg.go.dev/builtin#byte), interface{}) [error](https://pkg.go.dev/builtin#error)
    }

Codec represents a symmetric pair of functions that implement a codec. Items stored into or retrieved from memcache using a Codec have their values marshaled or unmarshaled.

All the methods provided for Codec behave analogously to the package level function with same name.

### func (Codec) Add 
    
    
    func (cd Codec) Add(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item *Item) [error](https://pkg.go.dev/builtin#error)

Add writes the given item, if no value already exists for its key. ErrNotStored is returned if that condition is not met.

### func (Codec) AddMulti 
    
    
    func (cd Codec) AddMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), items []*Item) [error](https://pkg.go.dev/builtin#error)

AddMulti is a batch version of Add. appengine.MultiError may be returned.

### func (Codec) CompareAndSwap 
    
    
    func (cd Codec) CompareAndSwap(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item *Item) [error](https://pkg.go.dev/builtin#error)

CompareAndSwap writes the given item that was previously returned by Get, if the value was neither modified or evicted between the Get and the CompareAndSwap calls. The item's Key should not change between calls but all other item fields may differ. ErrCASConflict is returned if the value was modified in between the calls. ErrNotStored is returned if the value was evicted in between the calls.

### func (Codec) CompareAndSwapMulti 
    
    
    func (cd Codec) CompareAndSwapMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), items []*Item) [error](https://pkg.go.dev/builtin#error)

CompareAndSwapMulti is a batch version of CompareAndSwap. appengine.MultiError may be returned.

### func (Codec) Get 
    
    
    func (cd Codec) Get(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [string](https://pkg.go.dev/builtin#string), v interface{}) (*Item, [error](https://pkg.go.dev/builtin#error))

Get gets the item for the given key and decodes the obtained value into v. ErrCacheMiss is returned for a memcache cache miss. The key must be at most 250 bytes in length.

### func (Codec) Set 
    
    
    func (cd Codec) Set(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), item *Item) [error](https://pkg.go.dev/builtin#error)

Set writes the given item, unconditionally.

### func (Codec) SetMulti 
    
    
    func (cd Codec) SetMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), items []*Item) [error](https://pkg.go.dev/builtin#error)

SetMulti is a batch version of Set. appengine.MultiError may be returned.

## Item
    
    
    type Item struct {
    	// Key is the Item's key (250 bytes maximum).
    	Key [string](https://pkg.go.dev/builtin#string)
    	// Value is the Item's value.
    	Value [][byte](https://pkg.go.dev/builtin#byte)
    	// Object is the Item's value for use with a Codec.
    	Object interface{}
    	// Flags are server-opaque flags whose semantics are entirely up to the
    	// App Engine app.
    	Flags [uint32](https://pkg.go.dev/builtin#uint32)
    	// Expiration is the maximum duration that the item will stay
    	// in the cache.
    	// The zero value means the Item has no expiration time.
    	// Subsecond precision is ignored.
    	// This is not set when getting items.
    	Expiration [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
    
    	// ItemTimestamps are server values only returned when calling Peek and PeekMulti.
    	// The timestamps are nil when calling Get and GetMulti.
    	Timestamps ItemTimestamps
    	// contains filtered or unexported fields
    }

Item is the unit of memcache gets and sets.

### func Get 
    
    
    func Get(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [string](https://pkg.go.dev/builtin#string)) (*Item, [error](https://pkg.go.dev/builtin#error))

Get gets the item for the given key. ErrCacheMiss is returned for a memcache cache miss. The key must be at most 250 bytes in length.

### func Peek 
    
    
    func Peek(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [string](https://pkg.go.dev/builtin#string)) (*Item, [error](https://pkg.go.dev/builtin#error))

Peek gets the item for the given key and additionally populates Item.Timestamps. ErrCacheMiss is returned for a memcache cache miss. The key must be at most 250 bytes in length.

## ItemTimestamps
    
    
    type ItemTimestamps struct {
    	// Expiration is related to Item.Expiration but it is a Time (not a Duration),
    	// provided by the server. It is not meant to be set by the user.
    	Expiration *[time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)
    	// LastAccess is the last time the Item was accessed.
    	LastAccess *[time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)
    }

ItemTimestamps are timestamps optionally provided by the server. See Peek and PeekMulti.

## Statistics
    
    
    type Statistics struct {
    	Hits     [uint64](https://pkg.go.dev/builtin#uint64) // Counter of cache hits
    	Misses   [uint64](https://pkg.go.dev/builtin#uint64) // Counter of cache misses
    	ByteHits [uint64](https://pkg.go.dev/builtin#uint64) // Counter of bytes transferred for gets
    
    	Items [uint64](https://pkg.go.dev/builtin#uint64) // Items currently in the cache
    	Bytes [uint64](https://pkg.go.dev/builtin#uint64) // Size of all items currently in the cache
    
    	Oldest [int64](https://pkg.go.dev/builtin#int64) // Age of access of the oldest item, in seconds
    }

Statistics represents a set of statistics about the memcache cache. This may include items that have expired but have not yet been removed from the cache.

### func Stats 
    
    
    func Stats(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (*Statistics, [error](https://pkg.go.dev/builtin#error))

Stats retrieves the current memcache statistics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
