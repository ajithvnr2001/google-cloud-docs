---
url: https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/
title: @google-cloud/precise-date \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:05.178141+00:00
---

# @google-cloud/precise-date  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  @google-cloud/precise-date Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  4.0.0  3.0.1  2.0.4 

> A simple utility for precise-dateing functions and classes.

### Installing the package

It's unlikely you will need to install this package directly, as it will be installed as a dependency when you install other `@google-cloud` packages.
    
    
    $ npm install --save @google-cloud/precise-date
    

### Using the package

`PreciseDate` extends the native `Date` object, so you can use it in place of that or when you need nanosecond precision.
    
    
    const {PreciseDate} = require('[@google-cloud/precise-date](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/overview.html)');
    const date = new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)('1547253035381101032');
    
    date.[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)();
    // => 2019-01-12T00:30:35.381101032Z
    
    date.toFullTimeString();
    // => '1547253035381101032'
    

## API

### PreciseDate([time])

Returns a new `date` instance.

#### time

Type: `string` [`BigInt`](https://github.com/tc39/proposal-bigint) `Object<string, number>` `[number, number]`
    
    
    // from a full ISO string
    date = new PreciseDate('2019-02-08T10:34:29.481145231Z');
    
    // from a string representing nanoseconds
    date = new PreciseDate('1549622069481320032');
    
    // from a BigInt representing nanoseconds (requires Node >= 10.7)
    date = new PreciseDate(1549622069481320032n);
    
    // from an object containing `seconds` and `nanos` values
    date = new PreciseDate({seconds: 1549622069, nanos: 481320032});
    
    // from a tuple representing [seconds, nanos]
    date = new PreciseDate([1549622069, 481320032]);
    

#### PreciseDate.parseFull(time)

Similar to [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse), but this accepts the same nanosecond time options as the `PreciseDate` constructor and returns a string representing the nanoseconds in the specified date according to universal time.
    
    
    PreciseDate.parseFull('2019-02-08T10:34:29.481145231Z');
    // => '1549622069481145231'
    

#### PreciseDate.fullUTCString(...dateFields)

Similar to [`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC), but also accepts microsecond and nanosecond parameters. Returns a string that represents the number of nanoseconds since January 1, 1970, 00:00:00 UTC.

##### dateFields

Type: `...number`
    
    
    PreciseDate.fullUTCString(2019, 1, 8, 10, 34, 29, 481, 145, 231);
    // => '1549622069481145231'
    

#### PreciseDate.fullUTC(...dateFields)

Like `PreciseDate.fullUTCString()` but returns a native [`BigInt`](https://github.com/tc39/proposal-bigint) instead of a string. **Requires Node >= 10.7.**

##### dateFields

Type: `...number`
    
    
    PreciseDate.fullUTC(2019, 1, 8, 10, 34, 29, 481, 145, 231);
    // => 1549622069481145231n
    

### date

`PreciseDate` instance.

#### date.getFullTimeString()

Returns a string of the specified date represented in nanoseconds according to universal time.

#### date.getFullTime()

Like `date.getFullTimeString()` but returns a native [`BigInt`](https://github.com/tc39/proposal-bigint) instead of a string. **Requires Node >= 10.7.**

#### date.getMicroseconds()

Returns the microseconds in the specified date according to universal time.

#### date.getNanoseconds()

Returns the nanoseconds in the specified date according to universal time.

#### date.setMicroseconds(microseconds)

Sets the microseconds for a specified date according to universal time. Returns a string representing the nanoseconds in the specified date according to universal time.

##### microseconds

Type: `number`

#### date.setNanoseconds(nanoseconds)

Sets the nanoseconds for a specified date according to universal time. Returns a string representing the nanoseconds in the specified date according to universal time.

##### nanoseconds

Type: `number`

#### date.setFullTime(time)

Sets the time to the number of supplied nanoseconds since January 1, 1970, 00:00:00 UTC. Returns a string representing the nanoseconds in the specified date according to universal time (effectively, the value of the argument).

##### time

Type: `number` `string` [`BigInt`](https://github.com/tc39/proposal-bigint)

#### date.toStruct()

Returns an object representing the specified date according to universal time. Refer to [`google.protobuf.Timestamp`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp|google.protobuf.Timestamp) for more information about this format.
    
    
    const {seconds, nanos} = date.toStruct();
    

#### date.toTuple()

Like `date.toStruct()` but returns the `seconds` and `nanos` as a tuple.
    
    
    const [seconds, nanos] = date.toTuple();
    

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googlecloudplatform/google-cloud-node/blob/master/.github/CONTRIBUTING.md).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googlecloudplatform/google-cloud-node/blob/master/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
