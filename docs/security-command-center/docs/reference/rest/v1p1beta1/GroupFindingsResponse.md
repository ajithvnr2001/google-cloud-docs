---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/GroupFindingsResponse/
title: GroupFindingsResponse \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:50.241136+00:00
---

# GroupFindingsResponse  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/GroupFindingsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  GroupFindingsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for group by findings.

JSON representation  
---  
      
    
    {
      "groupByResults": [
        {
          object ([GroupResult](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/GroupResult))
        }
      ],
      "readTime": string,
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`groupByResults[]` |  `object (`[GroupResult](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/GroupResult)`)` Group results. There exists an element for each existing unique combination of property/values. The element contains a count for the number of times those specific property/values appear.  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time used for executing the groupBy request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results.  
`totalSize` |  `integer` The total number of results matching the query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-02 UTC."],[],[]] 
