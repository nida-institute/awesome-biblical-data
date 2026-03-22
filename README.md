# Awesome Biblical Data

A curated catalog of high-quality datasets and tools for biblical and linguistic
scholarship. Focused on what is freely available and how to get it onto your
machine or into your database.

**Suggest a resource:** [Open an issue](https://github.com/nida-institute/awesome-biblical-data/issues/new)

The machine-readable version of this catalog is [`resources.json`](resources.json).

---

## Contents

- [Awesome Biblical Data](#awesome-biblical-data)
  - [Contents](#contents)
  - [1. Greek New Testament — Base Texts](#1-greek-new-testament--base-texts)
  - [2. Manuscript Transcriptions \& Textual Variants](#2-manuscript-transcriptions--textual-variants)
  - [3. Septuagint (LXX)](#3-septuagint-lxx)
  - [4. Hebrew Bible — Base Texts \& Morphology](#4-hebrew-bible--base-texts--morphology)
  - [5. Greek NT — Morphology \& Syntax](#5-greek-nt--morphology--syntax)
  - [6. Treebanks](#6-treebanks)
  - [7. Discourse Analysis](#7-discourse-analysis)
  - [8. Lexicons](#8-lexicons)
  - [9. Semantic Domains \& Thematic Resources](#9-semantic-domains--thematic-resources)
  - [10. Entity Annotation](#10-entity-annotation)
  - [11. Geography \& Places](#11-geography--places)
  - [12. Hellenistic \& Patristic Corpora](#12-hellenistic--patristic-corpora)
  - [13. Papyri \& Inscriptions](#13-papyri--inscriptions)
  - [14. Jewish Texts](#14-jewish-texts)
  - [15. Versification \& Alignment](#15-versification--alignment)
  - [16. Translation \& Publishing Infrastructure](#16-translation--publishing-infrastructure)
  - [Contributing](#contributing)

---

## 1. Greek New Testament — Base Texts

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **SBLGNT** | Society of Biblical Literature Greek New Testament. High-quality critical text. Note the [license](http://sblgnt.com/license/) — imposes conditions on downstream works. | Custom (see license) | XML, OSIS, text | [morphgnt/sblgnt](https://github.com/morphgnt/sblgnt) |
| **Nestle 1904** | Eberhard Nestle's 1904 GNT. Used in many treebanks. | Public Domain | CSV, XML | [biblicalhumanities/Nestle1904](https://github.com/biblicalhumanities/Nestle1904) |
| **Byzantine Majority Text (Robinson-Pierpont RP2018)** | Robinson-Pierpont Byzantine Textform. Use RP2018 — RP2005 had accent errors. TEI-XML directly collatable with Münster INTF transcriptions via CollateX. | Public Domain | TEI-XML, CSV Unicode, Beta code | `git clone https://github.com/byztxt/byzantine-majority-text` — locally at `/Users/jonathan/github/byztxt/byzantine-majority-text/` |
| **Antoniades 1904/1912 Patriarchal Edition** | Ecumenical Patriarchate edition with Robinson's morphological parsing and Strong's numbers. Narrower manuscript base than Robinson-Pierpont. | Public Domain | Beta code, Unicode | `git clone https://github.com/byztxt/greektext-antoniades` — locally at `/Users/jonathan/github/byztxt/greektext-antoniades/` |
| **CNTR Statistical Restoration (SR)** | World's first computer-generated GNT based on statistical analysis of earliest manuscripts. Alan Bunning / Center for New Testament Restoration. | CC BY 4.0 | Multiple | [Center-for-New-Testament-Restoration/SR](https://github.com/Center-for-New-Testament-Restoration/SR) |
| **Westcott-Hort** | Classic critical text, as edited by Joshua Grauman. | Public Domain | Text | [scrolltag.com](http://scrolltag.com/westcott_and_hort.html) |

---

## 2. Manuscript Transcriptions & Textual Variants

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **CNTR Electronic Transcriptions** | Alan Bunning's transcriptions of every extant Greek NT manuscript to 400 AD. The most comprehensive freely available set. Collation, apparatus, and manuscript viewer at [greekcntr.org](https://greekcntr.org). | See [terms](https://greekcntr.org/terms/index.html) | Multiple | [Center-for-New-Testament-Restoration/electronic-transcriptions](https://github.com/Center-for-New-Testament-Restoration/electronic-transcriptions) |
| **Codex Sinaiticus** | Complete digital edition of Codex Sinaiticus (4th c.) with TEI XML transcription download. | See site | TEI XML | [codexsinaiticus.org](https://www.codexsinaiticus.org/en/) — downloads at [transcription_download](https://codexsinaiticus.org/en/project/transcription_download.aspx) |
| **Amsterdam Database of NT Conjectural Emendation** | Scholarly conjectural emendations to the Greek NT, with attribution. | Open | SQL, web | [ntvmr.uni-muenster.de/nt-conjectures-attribution](http://ntvmr.uni-muenster.de/nt-conjectures-attribution) — data [as SQL](http://ntvmr.uni-muenster.de/community/vmr/api/projects/ntconjectures/admin/sql/scripts/) |

---

## 3. Septuagint (LXX)

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Macula LXX** | Word-level morphology for the Septuagint, same schema as Macula Greek NT. Anchored to Macula node IDs. | CC BY 4.0 | XML, TSV | [Clear-Bible/macula-greek](https://github.com/Clear-Bible/macula-greek) (LXX folder) |
| **Rahlfs-Hanhart LXX** | The standard critical edition. Morphological tagging available via several sources. | See source | Text | Via [Logos/Faithlife](https://www.logos.com/) or [CATSS](http://ccat.sas.upenn.edu/) |
| **CATSS LXX Morphology** | Computer-Assisted Tools for Septuagint Studies morphological text. Not freely licensed — see [user agreement](http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/0-user-declaration.txt). | Restricted | Plain text | [ccat.sas.upenn.edu](http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/) |
| **Swete's Septuagint** | Machine-corrected version. Morphological tagging in progress (contact James Tauber). | Open | XML | [OpenGreekAndLatin/septuagint-dev](https://github.com/OpenGreekAndLatin/septuagint-dev) |

---

## 4. Hebrew Bible — Base Texts & Morphology

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Macula Hebrew (WLC-based)** | Word-level morphology, lemma, gloss, POS, gender/number/person, pronominal suffixes for the entire Hebrew Bible. The go-to for pipeline work. | CC BY 4.0 | TSV, XML | `git clone https://github.com/Clear-Bible/macula-hebrew` |
| **Westminster Leningrad Codex (WLC)** | The base text used by Macula Hebrew, BHS, and most Hebrew Bible work. | Various | XML, OSIS | Via [OpenScriptures/morphhb](https://github.com/openscriptures/morphhb) or Macula |
| **OpenScriptures Hebrew Bible (morphhb)** | Parsed Hebrew Bible with Strong's numbers and morphology tags. | MIT | XML | `git clone https://github.com/openscriptures/morphhb` |
| **ETCBC / BHSA (Biblia Hebraica Stuttgartensia Amstelodamensis)** | The most complete Hebrew syntactic database: clause, phrase, and word nodes with full feature set. Three millennium of scholarship encoded. Access via `text-fabric` Python library. | CC BY-NC 4.0 | Text-Fabric nodes | `pip install text-fabric` then `tf.use('etcbc/bhsa')` — data at [etcbc/bhsa](https://github.com/etcbc/bhsa) |
| **Shebanq** | ETCBC Hebrew Bible data as a queryable SQL database with a web interface. | Open | SQL, web | [shebanq.ancient-data.org](https://shebanq.ancient-data.org/) |

---

## 5. Greek NT — Morphology & Syntax

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Macula Greek NT** | Word-level morphology for the GNT anchored to SBLGNT. Same schema as Macula Hebrew. The standard for pipeline work. | CC BY 4.0 | XML, TSV | `git clone https://github.com/Clear-Bible/macula-greek` |
| **MorphGNT (SBLGNT)** | Per-word morphology for SBLGNT. The original open high-quality GNT morphology. | CC BY-SA 3.0 | Plain text columns | `git clone https://github.com/morphgnt/sblgnt` |
| **MorphGNT (Nestle1904)** | Nestle 1904 with MorphGNT conventions. | CC BY 4.0 | CSV | [biblicalhumanities/Nestle1904](https://github.com/biblicalhumanities/Nestle1904) |
| **MorphGNT (Tischendorf)** | Tischendorf GNT with MorphGNT morphology. | Open | Plain text columns | [morphgnt/tischendorf](https://github.com/morphgnt/tischendorf) |
| **Clear-Bible Speaker Quotations** | Word-level identification of quotations in OT and NT with speaker attribution. | CC BY 4.0 | JSON | [Clear-Bible/speaker-quotations](https://github.com/Clear-Bible/speaker-quotations) |

---

## 6. Treebanks

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **GBI Treebank (Nestle1904 & SBLGNT)** | Global Bible Initiative HPSG constituent grammar treebank. High quality. | Open | XML | [biblicalhumanities/greek-new-testament](https://github.com/biblicalhumanities/greek-new-testament) (syntax-trees/) |
| **Lowfat Trees (Nestle1904 & SBLGNT)** | GBI trees transformed into a simpler, more XQuery-friendly format. Best for BaseX/XQuery work. | Open | XML | Same repo as GBI — lowfat folder |
| **PROIEL Treebank** | High-quality dependency trees for Tischendorf GNT. Part of a parallel corpus spanning Greek, Armenian, Gothic, Old Church Slavonic, Latin. | CC BY-NC-SA 4.0 | XML | [proiel/proiel-treebank](https://github.com/proiel/proiel-treebank) |

---

## 7. Discourse Analysis

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Levinsohn LGNTDF** | Stephen Levinsohn's complete discourse feature markup of the Greek NT (UBS4/NA27). 806+ word-level annotations. 2016 Biblical Humanities Dataset of the Year. Released by SIL International. | Custom — freely distributable, not for sale; see [LICENSE](https://github.com/biblicalhumanities/levinsohn/blob/master/LICENSE.md) | XML | `git clone https://github.com/biblicalhumanities/levinsohn` |

---

## 8. Lexicons

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Abbott-Smith** | _A Manual Greek Lexicon of the New Testament_. Best-quality public domain Greek NT lexicon. | Public Domain | TEI XML | [translatable-exegetical-tools/Abbott-Smith](https://github.com/translatable-exegetical-tools/Abbott-Smith) — locally in LLMFlow `inputs/Abbot-Smith/` |
| **Liddell-Scott-Jones (LSJ)** | _A Greek-English Lexicon_. The standard unabridged classical Greek lexicon. Unicode version at [gcelano/LSJ_GreekUnicode](https://github.com/gcelano/LSJ_GreekUnicode). | Perseus license | TEI XML | [PerseusDL/lexica](https://github.com/PerseusDL/lexica) or gcelano's Unicode version |
| **Dodson Greek Lexicon** | Simple glosses and short definitions for GNT vocabulary. Public domain. | Public Domain | CSV, XML | [biblicalhumanities/Dodson-Greek-Lexicon](https://github.com/biblicalhumanities/Dodson-Greek-Lexicon) |
| **Mounce Concise Dictionary** | Mounce's Concise Greek-English Dictionary of Biblical Greek. | CC BY-SA | JSON | [jcuenod/dictionary](https://github.com/jcuenod/dictionary) |
| **Strong's Dictionary** | Greek and Hebrew Strong's numbers with definitions. Widely used for cross-reference. | Public Domain | XML | [openscriptures/strongs](https://github.com/openscriptures/strongs) |
| **BDAG** | _A Greek-English Lexicon of the New Testament_ (Bauer-Danker-Arndt-Gingrich). The scholarly standard. **Not freely available** — reference only. | Commercial | — | Publisher: University of Chicago Press |

---

## 9. Semantic Domains & Thematic Resources

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **UBS Semantic Dictionary of Biblical Hebrew (SDBH)** | UBS semantic domain lexicon for the Hebrew Bible. Word-level domain annotations in Macula Hebrew. | Open | JSON, XML | [ubsicap/ubs-open-license](https://github.com/ubsicap/ubs-open-license) — see also [semanticdictionary.org](https://semanticdictionary.org/) |
| **UBS Semantic Dictionary of the Greek NT (SDGNT)** | UBS semantic domain lexicon for the GNT. Same repo. | Open | JSON, XML | [ubsicap/ubs-open-license](https://github.com/ubsicap/ubs-open-license) |
| **UBS Thematic Lexicons (Flora, Fauna, Realia)** | Three lexicons for plants, animals, and man-made objects in the Bible. Issued under open license March 2025. | Open | JSON | [ubsicap/ubs-open-license/flora-fauna-realia](https://github.com/ubsicap/ubs-open-license/tree/main/flora-fauna-realia) |
| **STEPBible TIPNR** | Translators Individualised Proper Names with all References. Tyndale House. High-quality proper noun data. | CC BY | Text | [STEPBible/STEPBible-Data](https://github.com/STEPBible/STEPBible-Data) — TIPNR file |
| **Patristic Text Archive TIPNR** | JSON/XML versions of TIPNR with persons and places separated. | Open | JSON, XML | [PatristicTextArchive/tipnr_data](https://github.com/PatristicTextArchive/tipnr_data) |

---

## 10. Entity Annotation

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **ACAI** | People, places, deities, groups, fauna, flora, realia, and keyterms anchored to Macula node IDs. People and places span both testaments. Rick Brannan / Mission Mutual. The most comprehensive open entity annotation set. | CC BY-SA 4.0 | JSON, Markdown | [BibleAquifer/ACAI](https://github.com/BibleAquifer/ACAI) |
| **OpenBible.info Bible Geocoding Data** | Geocoded coordinates for biblical place names with passage references. | CC BY | CSV | [openbibleinfo/Bible-Geocoding-Data](https://github.com/openbibleinfo/Bible-Geocoding-Data) |
| **Theographic Bible Metadata (viz.bible)** | Robert Rouse's structured metadata for biblical people, places, events, and relationships. Used by ACAI. | CC BY | JSON | [robertrouse/theographic-bible-metadata](https://github.com/robertrouse/theographic-bible-metadata) |

---

## 11. Geography & Places

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Pleiades** | Gazetteer of ancient world places (Greek, Roman, Near Eastern). The scholarly standard for ancient geography. Coordinates, name variants, periods, references. Essential for any spatial pipeline work. | CC BY 3.0 | JSON, CSV, RDF | [pleiades.stoa.org](https://pleiades.stoa.org/) — bulk downloads at [pleiades.stoa.org/downloads](https://pleiades.stoa.org/downloads) |
| **OpenBible.info Bible Geocoding** | See Entity Annotation above — geocoded biblical places. | CC BY | CSV | [openbibleinfo/Bible-Geocoding-Data](https://github.com/openbibleinfo/Bible-Geocoding-Data) |

---

## 12. Hellenistic & Patristic Corpora

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **First1KGreek / Open Greek and Latin** | TEI P5 XML for Josephus, Philo, Apostolic Fathers, and much of the first 1000 years of Greek literature. Best for Hellenistic context corpora. | CC BY-SA 3.0 | TEI XML | [OpenGreekAndLatin/First1KGreek](https://github.com/OpenGreekAndLatin/First1KGreek) |
| **Perseus Digital Library** | Massive collection of Greek and Latin classical texts in TEI XML with morphological tagging. Homer, Plato, Thucydides, Cicero, and much more. | Various CC | TEI XML | [PerseusDL](https://github.com/PerseusDL) — canonical access via [perseus.tufts.edu](http://www.perseus.tufts.edu/) |
| **Patrologia Graeca (Migne)** | Massive collection of Church Fathers, volumes 1–161. Open Greek and Latin project. | Open | XML | [OGL-PatrologiaGraecaDev](https://github.com/OGL-PatrologiaGraecaDev) |
| **Cramer's Catenae** | For each NT verse, lists comments by early Church Fathers. | Open | XML | [OpenGreekAndLatin/catenae-dev](https://github.com/OpenGreekAndLatin/catenae-dev) |
| **Coptic Scriptorium** | Coptic corpus with morphology and phrasing. Freely licensed. Essential for early Christian documentary and literary texts. | CC | XML | [data.copticscriptorium.org](http://data.copticscriptorium.org/) / [GitHub](https://github.com/CopticScriptorium) |

---

## 13. Papyri & Inscriptions

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Papyri.info / DDBDP** | Duke Databank of Documentary Papyri. Documentary papyri (letters, contracts, receipts) in EpiDoc XML. Best source for Koine Greek in real-world contexts. | CC BY 3.0 | EpiDoc XML | [papyri.info](https://papyri.info/) — bulk download at [github.com/papyri/idp.data](https://github.com/papyri/idp.data) |
| **PHI Greek Inscriptions** | Packard Humanities Institute corpus of Greek epigraphic texts. Requires access request. | Restricted | Text | [epigraphy.packhum.org](https://epigraphy.packhum.org/) |
| **EAGLE / EDH** | Europeana network of ancient Greek and Latin epigraphic resources. Epigraphik-Datenbank Heidelberg for Latin inscriptions. | Open | EpiDoc XML | [eagle-network.eu](https://www.eagle-network.eu/) / [edh.ub.uni-heidelberg.de](https://edh.ub.uni-heidelberg.de/) |
| **Trismegistos** | Portal for ancient papyri and inscriptions. Cross-references between collections. | See site | Web API | [trismegistos.org](https://www.trismegistos.org/) |

---

## 14. Jewish Texts

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Sefaria** | Jewish text library: Tanakh with commentaries (Rashi, Ibn Ezra, Nachmanides), Mishnah, Talmud, Midrash, Targums, Kabbalah, lexicon, and Hebrew grammar. Indispensable for Jewish context. | CC BY-NC | JSON | [Sefaria/Sefaria-Export](https://github.com/Sefaria/Sefaria-Export) |

---

## 15. Versification & Alignment

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Copenhagen Alliance Versification Specification** | Canonical versification schemes (ORG, ENG, and others) for cross-translation reference alignment. ACAI uses the ORG scheme. | Open | JSON + code | [Copenhagen-Alliance/versification-specification](https://github.com/Copenhagen-Alliance/versification-specification) |
| **Clear-Bible Alignments (Biblica)** | Word-level alignment of translations to Macula Hebrew/Greek. Used by ACAI for Markdown visualization. | Open | JSON | [Clear-Bible/Alignments](https://github.com/Clear-Bible/Alignments) |

---

## 16. Translation & Publishing Infrastructure

| Name | Description | License | Format | Get It |
|---|---|---|---|---|
| **Scripture Burrito** | Standard for packaging and exchanging Scripture-related data. Exchange format for Paratext. | Open | JSON schema | [docs.burrito.bible](https://docs.burrito.bible/) / [bible-burrito/format](https://github.com/bible-burrito/format) |
| **Paratext USFM/USX** | Bible translation project format. Access local Paratext projects via `usfmtc` (Martin Hosken / SIL). | Tools: MIT | USFM, USX | [`pip install usfmtc`](https://pypi.org/project/usfmtc/) |
| **USX 3.1 Schema** | XML serialization of USFM 3.1 maintained by United Bible Societies. | Open | XML schema | [ubsicap/usx](https://github.com/ubsicap/usx) |

---

## Contributing

To suggest a dataset, [open an issue](https://github.com/nida-institute/awesome-biblical-data/issues/new) with:
- Name and brief description
- License
- Where to get it (GitHub URL, download URL, or acquisition process)
- Format(s) available
- Why it meets a bar of scholarly quality

This catalog focuses on resources that are: (a) freely available or clearly acquirable, (b) of genuine scholarly quality, and (c) useful for computational work. Survey data, informal concordances, and ecclesial-only resources are generally out of scope.

---

_Maintained by the [NIDA Institute](https://github.com/nida-institute). Machine-readable version: [`resources.json`](resources.json)._
