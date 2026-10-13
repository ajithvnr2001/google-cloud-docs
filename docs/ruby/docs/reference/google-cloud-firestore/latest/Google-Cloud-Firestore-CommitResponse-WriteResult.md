---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-CommitResponse-WriteResult/
title: Cloud Firestore API - Class Google::Cloud::Firestore::CommitResponse::WriteResult (v3.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:06.961893+00:00
---

# Cloud Firestore API - Class Google::Cloud::Firestore::CommitResponse::WriteResult (v3.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-CommitResponse-WriteResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore API - Class Google::Cloud::Firestore::CommitResponse::WriteResult (v3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.1  3.0.0  2.16.1  2.15.1  2.14.0  2.13.1  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.2  2.6.6 

Reference documentation and code samples for the Cloud Firestore API class Google::Cloud::Firestore::CommitResponse::WriteResult.

## WriteResult

Represents the result of applying a write.

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    commit_response = firestore.batch do |b|
      # Set the data for NYC
      b.set("cities/NYC", { name: "New York City" })
    
      # Update the population for SF
      b.update("cities/SF", { population: 1000000 })
    
      # Delete LA
      b.delete("cities/LA")
    end
    
    puts commit_response.commit_time
    commit_response.write_results.each do |write_result|
      puts write_result.update_time
    end

## Methods 

### #update_time
    
    
    def update_time() -> Time

The last update time of the document after applying the write. Not set after a +delete+.

If the write did not actually change the document, this will be the previous update_time.

**Returns**

  * (Time) — The last update time. 



### #update_time=
    
    
    def update_time=(value) -> Time

The last update time of the document after applying the write. Not set after a +delete+.

If the write did not actually change the document, this will be the previous update_time.

**Parameter**

  * **value** (Time) — The last update time. 



**Returns**

  * (Time) — The last update time. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
