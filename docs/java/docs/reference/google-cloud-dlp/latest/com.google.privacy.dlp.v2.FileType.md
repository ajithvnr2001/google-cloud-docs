---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType
title: Enum FileType (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:58.233464+00:00
---

# Enum FileType (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum FileType (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.7  3.5.0  3.4.0  3.3.2  3.2.1  3.1.4 
    
    
    public enum FileType extends Enum<FileType> implements ProtocolMessageEnum

Definitions of file type groups to scan. New types will be added to this list.

Protobuf enum `google.privacy.dlp.v2.FileType`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`AVRO` |  Included file extensions: avro `AVRO = 7;`  
`AVRO_VALUE` |  Included file extensions: avro `AVRO = 7;`  
`BINARY_FILE` |  Includes all file extensions not covered by another entry. Binary scanning attempts to convert the content of the file to utf_8 to scan the file. If you wish to avoid this fall back, specify one or more of the other file types in your storage scan. `BINARY_FILE = 1;`  
`BINARY_FILE_VALUE` |  Includes all file extensions not covered by another entry. Binary scanning attempts to convert the content of the file to utf_8 to scan the file. If you wish to avoid this fall back, specify one or more of the other file types in your storage scan. `BINARY_FILE = 1;`  
`CSV` |  Included file extensions: csv `CSV = 8;`  
`CSV_VALUE` |  Included file extensions: csv `CSV = 8;`  
`EXCEL` |  Microsoft Excel files larger than 30 MB will be scanned as binary files. Included file extensions: xlsx, xlsm, xltx, xltm. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on Excel files. `EXCEL = 12;`  
`EXCEL_VALUE` |  Microsoft Excel files larger than 30 MB will be scanned as binary files. Included file extensions: xlsx, xlsm, xltx, xltm. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on Excel files. `EXCEL = 12;`  
`FILE_TYPE_UNSPECIFIED` |  Includes all files. `FILE_TYPE_UNSPECIFIED = 0;`  
`FILE_TYPE_UNSPECIFIED_VALUE` |  Includes all files. `FILE_TYPE_UNSPECIFIED = 0;`  
`IMAGE` |  Included file extensions: bmp, gif, jpg, jpeg, jpe, png. Setting bytes_limit_per_file or bytes_limit_per_file_percent has no effect on image files. Image inspection is restricted to the `global`, `us`, `asia`, and `europe` regions. `IMAGE = 3;`  
`IMAGE_VALUE` |  Included file extensions: bmp, gif, jpg, jpeg, jpe, png. Setting bytes_limit_per_file or bytes_limit_per_file_percent has no effect on image files. Image inspection is restricted to the `global`, `us`, `asia`, and `europe` regions. `IMAGE = 3;`  
`PDF` |  PDF files larger than 30 MB will be scanned as binary files. Included file extensions: pdf. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on PDF files. `PDF = 6;`  
`PDF_VALUE` |  PDF files larger than 30 MB will be scanned as binary files. Included file extensions: pdf. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on PDF files. `PDF = 6;`  
`POWERPOINT` |  Microsoft PowerPoint files larger than 30 MB will be scanned as binary files. Included file extensions: pptx, pptm, potx, potm, pot. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on PowerPoint files. `POWERPOINT = 11;`  
`POWERPOINT_VALUE` |  Microsoft PowerPoint files larger than 30 MB will be scanned as binary files. Included file extensions: pptx, pptm, potx, potm, pot. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on PowerPoint files. `POWERPOINT = 11;`  
`TEXT_FILE` |  Included file extensions: asc,asp, aspx, brf, c, cc,cfm, cgi, cpp, csv, cxx, c++, cs, css, dart, dat, dot, eml,, epbub, ged, go, h, hh, hpp, hxx, h++, hs, html, htm, mkd, markdown, m, ml, mli, perl, pl, plist, pm, php, phtml, pht, properties, py, pyw, rb, rbw, rs, rss, rc, scala, sh, sql, swift, tex, shtml, shtm, xhtml, lhs, ics, ini, java, js, json, jsonl, kix, kml, ocaml, md, txt, text, tsv, vb, vcard, vcs, wml, xcodeproj, xml, xsl, xsd, yml, yaml. `TEXT_FILE = 2;`  
`TEXT_FILE_VALUE` |  Included file extensions: asc,asp, aspx, brf, c, cc,cfm, cgi, cpp, csv, cxx, c++, cs, css, dart, dat, dot, eml,, epbub, ged, go, h, hh, hpp, hxx, h++, hs, html, htm, mkd, markdown, m, ml, mli, perl, pl, plist, pm, php, phtml, pht, properties, py, pyw, rb, rbw, rs, rss, rc, scala, sh, sql, swift, tex, shtml, shtm, xhtml, lhs, ics, ini, java, js, json, jsonl, kix, kml, ocaml, md, txt, text, tsv, vb, vcard, vcs, wml, xcodeproj, xml, xsl, xsd, yml, yaml. `TEXT_FILE = 2;`  
`TSV` |  Included file extensions: tsv `TSV = 9;`  
`TSV_VALUE` |  Included file extensions: tsv `TSV = 9;`  
`UNRECOGNIZED` |   
`WORD` |  Microsoft Word files larger than 30 MB will be scanned as binary files. Included file extensions: docx, dotx, docm, dotm. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on Word files. `WORD = 5;`  
`WORD_VALUE` |  Microsoft Word files larger than 30 MB will be scanned as binary files. Included file extensions: docx, dotx, docm, dotm. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on Word files. `WORD = 5;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType#com_google_privacy_dlp_v2_FileType_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
