---
url: https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/gceimages/
title: Class GCEImages (5.0.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:46.893286+00:00
---

# Class GCEImages (5.0.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/gceimages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class GCEImages (5.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 5.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/gceimages/)
  * [ 4.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/4.0.1/gce-images/gceimages/)
  * [ 3.0.4 ](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/3.0.4/gce-images/gceimages/)



## Package

[gce-images](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/overview.html)

## Constructors 

### (constructor)(config)
    
    
    constructor(config?: GCEImagesConfig | AuthOptions);

Constructs a new instance of the `GCEImages` class

**Parameter**  
---  
**Name** | **Description**  
`config` |  `[GCEImagesConfig](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/overview.html) | AuthOptions`   
  
  
## Properties 

### OS_TO_URL
    
    
    OS_TO_URL: {
            [index: string]: string;
        };

### OS_URLS
    
    
    OS_URLS: OSUrls;

## Methods 

### _filterDeprecated(image)
    
    
    _filterDeprecated(image: Image): boolean;

**Parameter**  
---  
**Name** | **Description**  
`image` |  `[Image_2](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/image_2)`   
  
**Returns**  
---  
**Type** | **Description**  
`boolean` |   
  
### _getAllByOS(options)
    
    
    _getAllByOS(options: GetOptions & {
            osNames: string[];
        }): Promise<Image[]>;

**Parameter**  
---  
**Name** | **Description**  
`options` |  `[GetOptions](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getoptions) & { osNames: string[]; }`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[Image](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/image_2)[]>` |   
  
### _parseArguments(options, callback)
    
    
    _parseArguments<O, C>(options: any, callback: any): ParsedArguments<O, C>;

**Parameters**  
---  
**Name** | **Description**  
`options` |  `any`   
  
`callback` |  `any`   
  
**Returns**  
---  
**Type** | **Description**  
`ParsedArguments<O, C>` |   
**Type Parameters**  
---  
**Name** | **Description**  
`O` |   
`C` |   
  
### _parseOsInput(os)
    
    
    _parseOsInput(os: string): {
            name: string;
            version: string;
            url: string;
        };

**Parameter**  
---  
**Name** | **Description**  
`os` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`{ name: string; version: string; url: string; }` |   
  
### _sortNewestFirst(imageA, imageB)
    
    
    _sortNewestFirst(imageA: Image, imageB: Image): 0 | 1 | -1;

**Parameters**  
---  
**Name** | **Description**  
`imageA` |  `[Image_2](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/image_2)`   
  
`imageB` |  `[Image_2](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/image_2)`   
  
**Returns**  
---  
**Type** | **Description**  
`0 | 1 | -1` |   
  
### getAll(cb)
    
    
    getAll(cb: GetAllCallback): void;

Get all available images.

**Parameter**  
---  
**Name** | **Description**  
`cb` |  `[GetAllCallback](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getallcallback)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` | {Promise} if callback is omitted.  
  
### getAll(opts)
    
    
    getAll(opts?: GetOptions | string): Promise<Image[] | ImagesMap>;

**Parameter**  
---  
**Name** | **Description**  
`opts` |  `[GetOptions](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getoptions) | string`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[Image](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/image_2)[] | [ImagesMap](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/imagesmap)>` |   
  
### getAll(opts, cb)
    
    
    getAll(opts: GetOptions | string, cb: GetAllCallback): void;

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `[GetOptions](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getoptions) | string`   
  
`cb` |  `[GetAllCallback](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getallcallback)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getLatest(cb)
    
    
    getLatest(cb: GetLatestCallback): void;

Get all available images, but only return the newest one.

**Parameter**  
---  
**Name** | **Description**  
`cb` |  `[GetLatestCallback](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getlatestcallback)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` | {Promise} if callback is omitted.  
  
### getLatest(opts)
    
    
    getLatest(opts?: GetOptions | string): Promise<Image | ImageMap>;

**Parameter**  
---  
**Name** | **Description**  
`opts` |  `[GetOptions](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getoptions) | string`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[Image](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/image_2) | [ImageMap](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/imagemap)>` |   
  
### getLatest(opts, cb)
    
    
    getLatest(opts: GetOptions | string, cb: GetLatestCallback): void;

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `[GetOptions](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getoptions) | string`   
  
`cb` |  `[GetLatestCallback](https://docs.cloud.google.com/nodejs/docs/reference/gce-images/latest/gce-images/getlatestcallback)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProjectId()
    
    
    getProjectId(): Promise<string>;

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
