\# ECG POC — Data Dictionary (Week: TBD)



\## 1) File format \& schema

\- Source system: MUSE (fallback: Epiphany)

\- Container/format: ☐ XML ☐ PDF ☐ WFDB ☐ Other: \_\_\_\_\_\_

\- Schema/version (if XML): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Compression (if any): ☐ None ☐ ZIP ☐ GZIP ☐ Other: \_\_\_\_\_\_



\## 2) Signals

\- Sampling rate (Hz): \_\_\_\_\_\_\_\_\_\_

\- Expected values: {250, 500} — confirm actual

\- Lead order (12-lead):

&nbsp; - \[ ] I

&nbsp; - \[ ] II

&nbsp; - \[ ] III

&nbsp; - \[ ] aVR

&nbsp; - \[ ] aVL

&nbsp; - \[ ] aVF

&nbsp; - \[ ] V1

&nbsp; - \[ ] V2

&nbsp; - \[ ] V3

&nbsp; - \[ ] V4

&nbsp; - \[ ] V5

&nbsp; - \[ ] V6

\- Units: ☐ mV ☐ µV ☐ Other: \_\_\_\_\_\_

\- Signal length (typical): \_\_\_\_\_\_ seconds

\- Line frequency: ☐ 60 Hz ☐ 50 Hz



\## 3) Timestamps

\- Present per sample? ☐ Yes ☐ No

\- Time zone / clock source: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Start time field/tag: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Any gaps/drops noted: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## 4) De-identification

\- Applied by: ☐ Biomed ☐ Export tool ☐ Script ☐ Not yet

\- Fields removed/hashed: 

&nbsp; - ☐ Name ☐ MRN ☐ DOB ☐ Accession ☐ Visit # ☐ Device serial ☐ Other: \_\_\_\_\_\_

\- PHI audit trail/location: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## 5) Metadata (tick what you receive)

\- Patient:

&nbsp; - ☐ Age  ☐ Sex  ☐ Height  ☐ Weight

\- Acquisition:

&nbsp; - ☐ Device model  ☐ Acquisition site/ward  ☐ Tech ID  ☐ Study ID

\- Technical:

&nbsp; - ☐ Filter settings  ☐ Gain  ☐ Paper speed (if printed)  ☐ Noise flags/quality

\- Interpretation/report:

&nbsp; - ☐ Auto-interpretation text

&nbsp; - ☐ Clinician over-read (final report) 

&nbsp; - ☐ Measurements: HR, PR, QRS, QT, QTc, axes

\- Other notes: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## 6) File locations \& access

\- Drop location (on-prem share): `\\\\server\\path\\folder`

\- Permissions: ☐ Read-only ☐ Write ☐ List

\- Expected delivery pattern: ☐ One-time batch ☐ Rolling daily ☐ Other

\- Retention plan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## 7) Validation checklist (fill as you verify)

\- \[ ] Can open files without errors

\- \[ ] Sampling rate matches config (`target\_fs`)

\- \[ ] Lead names map to expected order

\- \[ ] Units confirmed (mV)

\- \[ ] At least 50 studies parse end-to-end

\- \[ ] De-identification verified (no PHI in files or logs)



\## 8) Field/tag mapping (fill when you see the XML)

| Concept                    | MUSE/Epiphany tag/path     | Example value     | Notes/transform |

|---------------------------|----------------------------|-------------------|-----------------|

| Sampling rate             | …                           | 500               |                 |

| Lead list                 | …                           | I,II,III,…        | map to config   |

| Units                     | …                           | mV                |                 |

| Start timestamp           | …                           | 2025-11-12 10:05  | local time?     |

| Auto-interpretation text  | …                           | “Normal ECG”      |                 |

| Final report              | …                           | “NSR, QTc 430ms”  |                 |

| HR/QRS/QT/QTc             | …                           | 72/92/360/430     | ints/ms         |



\## 9) Open questions (leave blanks now; fill after huddle)

1\. Is ED data fully in MUSE for the target week? If not, Epiphany export steps/cost?

2\. Exact XML schema version and any vendor-specific quirks?

3\. Best practice for de-identification (who applies, how verified)?

4\. Where should we log access (audit trail location)?



