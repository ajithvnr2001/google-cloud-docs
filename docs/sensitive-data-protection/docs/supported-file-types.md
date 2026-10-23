---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types/
title: Supported file types and scanning modes \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:38.200409+00:00
---

# Supported file types and scanning modes  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Supported file types and scanning modes Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the types of files that Sensitive Data Protection can scan and describes the scanning modes that Sensitive Data Protection uses to analyze files.

## Supported file types in inspection and de-identification operations

The following table shows the types of files that Sensitive Data Protection can inspect and transform (_de-identify_).

Sensitive Data Protection relies on file extensions and media (MIME) types to identify the types of the files to be scanned and the [scanning modes](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#scanning_modes) to apply. For example, Sensitive Data Protection scans a `.txt` file in plain text mode, even if the file is structured as a CSV file, which is normally scanned in structured parsing mode. 

File type | File extensions | Limits | Scanning mode | Transformation support  
---|---|---|---|---  
`Apache Avro` | avro | [Avro limits](https://docs.cloud.google.com/sensitive-data-protection/limits#avro-limits) | Structured parsing |   
`Comma- or tab-separated values` | csv, tsv **Note:** To scan a CSV or TSV file in structured parsing mode, make sure that the file's delimiter matches its file extension. That is, a `.csv` file must be comma-delimited, and a `.tsv` file must be tab-delimited. |  | Structured parsing |  [ De-identify content](https://docs.cloud.google.com/sensitive-data-protection/docs/examples-deid-tables)  
`PDF` | pdf | [PDF limits](https://docs.cloud.google.com/sensitive-data-protection/limits#pdf-word-limits) | Intelligent document parsing |   
`Text` | asc, brf, c, c++, cc, cpp, cs, css, cxx, dart, eml, go, h, h++, hh, hpp, hs, htm, html, hxx, ini, java, js, json, jsonl, lhs, m, markdown, md, mkd, ml, mli, ocaml, php, pht, phtml, pl, pm, py, pyw, rb, rbw, rc, rs, scala, sh, shtm, shtml, sql, tex, text, txt, vcard, vcs, wml, xhtml, xml, xsd, xsl, yaml, yml |  | Plain text |  [ De-identify content](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify)  
`Microsoft Word` | docm, docx, dotm, dotx | [Word limits](https://docs.cloud.google.com/sensitive-data-protection/limits#pdf-word-limits) | Intelligent document parsing |   
`Microsoft Excel` | xlsm, xlsx, xltm, xltx | [Excel limits](https://docs.cloud.google.com/sensitive-data-protection/limits#pdf-word-limits) | Intelligent document parsing |   
`Microsoft Powerpoint` | potm, potx, pptm, pptx | [Powerpoint limits](https://docs.cloud.google.com/sensitive-data-protection/limits#pdf-word-limits) | Intelligent document parsing |   
`Image` | bmp, gif, jpe, jpeg, jpg, png |  | 

  * OCR
  * Image content detection
  * Image content classification

|  [ Redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact)  
`Binary` | [ Unrecognized file types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#unrecognized-file-types) and images that can't be scanned using optical character recognition (OCR), image content detection, or image content classification.  |  | Binary |   
  
## Supported file clusters in discovery operations

During discovery, Sensitive Data Protection organizes the detected files into _file clusters_. These clusters are groups of similar file types. The following table shows the supported file clusters and file extensions. Not all detected files are scannable.

Files might move between file clusters as Sensitive Data Protection adds support for more file clusters. As scanning support expands, the discovery service might begin to scan files that were previously not scanned. You are billed as described in [Discovery pricing](https://cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing).

File cluster | File extensions | Limits | Scanning mode  
---|---|---|---  
`Text` |  asc, eml, htm, html, ini, json, jsonL, log, markdown, md, mkd, plist, shtm, shtml, sql, tex, text, txt, vcard, vcs, xsd, xsl  |  | Plain text  
`Source Code` | bat, brf, c, c++, cc, cmd, cpp, cs, css, cxx, dart, go, h, hh, hpp, hs, hxx, java, js, lhs, m, ml, ocaml, php, phtm, phtml, pl, ps1, py, pyw, rb, rbw, rc, rs, scala, scpt, scr, script, sh, sql, vb, vbs, wml, xml, yaml, yml |  | Plain text  
`Structured Data` | avro, csv, tsv, proto |  | Structured parsing for avro, csv, and tsv files. Plain text parsing for proto files  
`Rich Documents` |  doc, docm, docx, dotm, dotx, pdf, potm, potx, ppt, pptm, pptx, xls, xlsm, xlsx, xltm, xltx  | Supported PDF, Microsoft Word, Excel, and Powerpoint files smaller than 30 MiB are scanned. | Intelligent document parsing  
`Images` |  bmp, gif, heic, ico, jpe, jpeg, jpg, pm, png, svg, tiff, webp  | Supported images (bmp, gif, jpe, jpeg, jpg, and png) smaller than 4 MiB are scanned using OCR in [regions that support image scanning](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#image-limitations).  | 

  * OCR
  * Image content detection
  * Image content classification

  
`Executables` |  ac, air, apk, app, appimage, bas, bin, bms, class, cls, com, command, ctl, ctx, dca, ddf, dep, dll, dob, dox, dsr, dsx, dws, exe, frm, frx, gadget, ipa, mpk, oca, ocx, pag, pgx, pif, pyc, res, run, scb, tlb, vbd, vbg, vbl, vbp, vbr, vbw, vbz, vlx, wct, widget, workflow, wsf, x86, x86_64, xap, xbe, xlm  |  | Not scanned at this time  
`Archives` |  7z, a, ace, afa, alz, apk, ar, arc, arj, ark, b1, b6z, ba, bh, cab, car, cdx, cfs, cpio, cpt, dar, dd, dgc, dmg, ear, esd, gca, genozip, gz, ha, hki, ice, ima, img, iso, jar, kgb, lha, lpaq#*, lzh, lzx, mou, pak, paq#*, paq6, paq7, paq8 and variants, partimg, pea, phar, pim, pit, qda, rar, rk, run, s7z, sda, sea, sen, sfx, shar, shk, sit, sitx, sqx, swm, tar, tar.bz2, tar.gz, tar.lz4, tar.lzma, tar.xz, tar.z, tgz, uc, uc0, uc2, uca, ucn, ue2, uha, ur2, war, wim, xar, xp3, yz1, zip, zipx, zoo, zpaq, zz  |  | Sensitive Data Protection scans files within archives that have these file extensions: bz2, cpio, gz, jar, lz4, lzma, tar, tar.bz2, tar.gz, tar.lz4, tar.lzma, tar.xz, tar.z, xz, z, zip The scanning mode used for each file depends on the type of the file.  
`Multimedia` |  3g2, 3gp, 8svx, aa, aac, aax, act, aiff, alac, amr, amv, ape, asf, au, avi, awb, cda, drc, dss, dvf, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, iklax, ivs, M2TS, m2v, m4a, m4b, m4p, m4p (with DRM), m4v, mkv, mmf, mng, mogg, mov, movpkg, mp2, mp3, mp4, mpc, mpe, mpeg, mpg, mpv, msv, MTS, mxf, nmf, nsv, oga, ogg, ogv, opus, qt, ra, raw, rf64, rm, rmvb, roq, sln, svi, TS, tta, viv, vob, voc, vox, wav, webm, wma, wmv, wv, yuv  |  | Not scanned at this time  
`AI Models` |  caffemodel, ckpt, coreml, dlc, ggjt, ggmf, ggml, gguf, h5, keras, llamafile, mar, mleap, nc, npy, npz, onnx, pb, pkl, prompt, pt, pt2, pte, pth, ptl, safetensors, surml, tflite, tfrecords  |  | Not scanned at this time  
`Unknown` |  Any other file not within another cluster.  | These are files that lack extensions or use common but non-standard extensions, like .dat or .1 or .2 | Not scanned at this time  
  
## Unrecognized file types in Cloud Storage

If a file is not recognized during a [storage scan](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage), the system will, by default, scan it as a binary file. It attempts to convert the content to UTF_8, and then scans it as plain text.

If a file is not recognized during a [discovery scan](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles), the system doesn't scan it.

If you have a collection of files you want to skip because Sensitive Data Protection doesn't recognize them, you can specify an exclusion list using [`CloudStorageOptions.file_set.regex_file_set.exclude_regex`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageRegexFileSet).

## Limits on bytes scanned per file

In general, you can limit the number of bytes scanned per file. In the Google Cloud console, you do so by [turning on sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#dlp-inspect-storage-console). In the Cloud Data Loss Prevention API, you set the [`bytes_limit_per_file`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageOptions.FIELDS.bytes_limit_per_file) or [`bytesLimitPerFilePercent`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageOptions.FIELDS.bytes_limit_per_file_percent) field.

Sampling isn't supported in OCR and intelligent parsing modes. That is, when the following file types are scanned in OCR or intelligent document parsing mode, Sensitive Data Protection ignores any settings that you apply to limit the bytes scanned per file.

  * Image
  * Microsoft Excel
  * Microsoft PowerPoint
  * Microsoft Word
  * PDF



If you scan these files in binary mode, the limits apply.

## Scanning modes

Each scanning mode provides additional [location details](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Location) in [inspection findings](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Finding). 

Scanning mode | Notes | Additional location details to be provided  
---|---|---  
Binary | If a file fails to be parsed as any other type, it will be converted to UTF_8 and scanned as text. Binary scanning affects detection quality.  |   
Intelligent document parsing | Documents are parsed with text extracted from formatting. Embedded images are scanned using OCR in [regions that support it ](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#image-limitations). Outside these regions, images are scanned as binary files. |  [ `DocumentLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DocumentLocation)  
Metadata extraction | All files scanned from Cloud Storage will have [`metadata`](https://docs.cloud.google.com/storage/docs/metadata) scanned in addition to the contents of the file. |  [ `MetadataLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataLocation)  
Optical character recognition (OCR) |  In [regions that support image scanning](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#image-limitations), Sensitive Data Protection uses OCR to find text-based infoTypes in images. |  [ `ImageLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ImageLocation)  
Image content detection | In regions that support image scanning, Sensitive Data Protection can analyze image pixels and features directly, rather than text extracted from images. This scanning mode focuses on locating a specific item within the image and produces a bounding box around it. For example, this scanning mode can detect a person or a barcode at a specific location in an image.  Sensitive Data Protection uses this scanning mode for any [object infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#objects-images) that are specified in the inspection or redaction configuration. |  [ `ImageLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ImageLocation)  
Image content classification | In regions that support image scanning, Sensitive Data Protection can analyze image pixels and features directly, rather than text extracted from images. This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification. Sensitive Data Protection uses this scanning mode for any [image context infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#image-context) that are specified in the inspection or redaction configuration. |  [ `ImageLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ImageLocation)  
Plain text |  | No additional details  
Structured parsing |  Structural information is used to influence findings. In this scanning mode, Sensitive Data Protection uses the header information for context. It performs a cross-row and cross-column analysis to find correlated data. For example, this scanning mode can identify a street address whose components are distributed across multiple columns in a row. The scan results contain structural information, such as the row that contains the finding and the name of the column. Findings don't cross a table's cell boundaries. |  [ `RecordLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#RecordLocation)  
  
## Scanning structured files in structured parsing mode

When you scan a structured file—such as an Avro, CSV, or TSV file—Sensitive Data Protection attempts to scan the file in [structured parsing scanning mode](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#structured-parsing). This scanning mode has a superior detection quality compared to [binary scanning](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#binary) because the structured parsing mode searches for correlations between rows and columns in the structured data. Findings are returned with additional metadata indicating the location of the finding, including the [`fieldId`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#recordlocation).

However, in the following cases, Sensitive Data Protection might revert to binary scanning mode, which doesn't include the enhancements of the structured parsing mode:

  * The file or header is corrupted.
  * The inspection job configuration has size limits—such as [`bytesLimitPerFile` and `bytesLimitPerFilePercent`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#cloudstorageoptions)—that are too small. For example, if the `bytesLimitPerFile` limit isn't large enough to include a full block header and at least one row of valid data, then Sensitive Data Protection might scan that file in binary scanning mode.



The selection of data that is scanned depends on whether [sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageOptions.FIELDS.sample_method) is set to start from the top of the file or from a random position.

For example, suppose that you have an Avro file that has 50 KB block headers and 2 MB data blocks. In general, starting the sample from the top helps you make sure that the block header is always included in the sample that Sensitive Data Protection takes. If you start sampling from a random position in the file and the sample size is smaller than a data block, there's a chance that the block header isn't included in the sample. In this example, increasing the sample size (specified by `bytesLimitPerFile` or `bytesLimitPerFilePercent`) to 2.05 MB helps prevent the inspection from reverting to binary parsing mode.

[ ![Example: When a sample size is too small, the inspection might not include the block header.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/random-sampling-avro.svg)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/random-sampling-avro.svg) Example: When a sample size is too small, the inspection might not include the block header (click to enlarge).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
