# CipherRounds — Objective Vendor Comparison

**Purpose:** Support a prospect follow-up with an objective, side-by-side view of digital rounding platforms — capabilities, implementation, support, and operational resources — not marketing collateral.

**Prepared for:** Jen (prospect contact)  
**Prepared by:** CipherHealth  
**Date:** August 14, 2026  
**Classification:** CIPHERHEALTH CONFIDENTIAL — share externally only with prospect approval

---

## Draft reply email

**Subject:** Rounding platform comparison + staying in touch

Hi Jen,

Thank you for the candid update — it’s helpful to know the CNOs see value and that the gating factors are alignment, funding, and operational support rather than product fit. That tracks with what we see at similar systems, and we’re glad Caryn and you are continuing those internal conversations. No pressure from our side on timing; we’ll stay available when it’s useful.

In the meantime, attached is an objective comparison of CipherRounds against the rounding options we most often see evaluated alongside us: **NRC Health**, **GetWell Rounds+**, **Epic-native rounding**, and **paper/manual programs**. It focuses on what you asked for:

- Capabilities (what each platform actually does in daily workflow)
- Implementation requirements (IT, EHR, hardware, timeline)
- Support model (who does what after go-live)
- Resource needs (clinical, operational, and IT FTE expectations)

We pulled this together from our implementation playbooks, published vendor documentation, and third-party market summaries — not from sales decks. Where a row reflects CipherHealth-specific delivery (for example, typical IT hours or clinical partnership structure), we’ve labeled it clearly. Where we could not verify a competitor claim from public sources, we’ve marked it **Unverified** rather than guess.

If it would help your internal stakeholders, we can also walk through the comparison on a 30-minute call and tailor the “resource needs” section to your unit count and current rounding model.

Thanks again, and please reach out whenever the internal work moves forward.

Best,  
[Your name]

**Attachment:** This document (or a formatted PDF export)

---

## How to read this document

### Scope

This comparison covers **inpatient digital rounding** — structured leader/nurse/patient/location rounds with real-time issue capture, routing, and reporting. It does **not** fully compare:

- Post-discharge outreach (CipherOutreach is noted only where it affects total platform footprint)
- In-room bedside entertainment/education platforms (GetWell Inpatient, Oneview) except where they integrate with rounding
- HCAHPS survey vendors (Press Ganey, Qualtrics) unless they also offer structured rounding workflows

### Sources

| Source type | Used for |
|---|---|
| CipherHealth AE onboarding library (internal) | CipherRounds capabilities, implementation benchmarks, support model, outcomes context |
| Vendor public product pages | NRC Health, GetWell, Epic positioning |
| AVIA Marketplace product profiles | Cross-vendor capability lists where available |
| Third-party market analysis (Ouva 2026 patient engagement guide) | Category framing and neutral vendor summaries |

### Legend

- **●** = Core / native capability  
- **◐** = Partial, add-on, or depends on configuration  
- **○** = Not a primary focus or typically requires a separate product  
- **Unverified** = Could not confirm from public documentation; validate in RFP/demo

---

## Executive summary (one page)

| Dimension | CipherRounds | NRC Health Rounding | GetWell Rounds+ | Epic-native rounding | Paper / manual |
|---|---|---|---|---|---|
| **Primary purpose** | Operational rounding + service recovery + safety capture across patient, staff, and location rounds | Experience + employee listening with AI-assisted documentation | Digital data collection for rounding, audits, and checklists; strongest when paired with GetWell Inpatient | Document rounds inside Epic; leverage existing EHR investment | Low software cost; high variability |
| **Best fit when…** | You want one rounding platform tied to HCAHPS domains, safety programs, and (optionally) the same vendor for post-discharge outreach | PX/HR analytics and “Human Understanding” program are already central; ambient AI documentation is a priority | You already run or plan GetWell Inpatient; want rounding tied to in-room engagement | “Use what we own” is the mandate; incremental Epic module cost is acceptable | Budget is zero; consistency and real-time recovery are not strategic priorities |
| **Typical implementation** | Weeks (certified HL7/Epic integration); often 4–8 weeks for combined programs | Unverified — typically multi-phase with analytics/HRIS integrations | Standalone can be fast; full value often requires GetWell Inpatient + EHR interface project | Depends on Epic module + build; often IT-heavy configuration | None |
| **Typical IT lift (CipherHealth customers)** | **<25 IT hours** to deploy a new program (internal benchmark); bidirectional Epic/Cerner/Meditech | Unverified | EHR interface + device management; broader if Inpatient deployed | Internal Epic team + possible Vendor Services validation | None |
| **Clinical ownership required** | Nursing/PX program lead + unit champions; CipherClinical supports design | PX + HR for employee rounding; analytics admin | Nursing ops + GetWell admin; stronger change mgmt if Inpatient bundled | Nursing + Epic analyst | Unit managers only |
| **Real-time service recovery** | ● | ● | ● | ◐ (workflow-dependent) | ○ |
| **Safety / HAC-focused rounding** | ● (location + patient rounding) | ◐ (more PX-weighted in public materials) | ◐ (100+ use cases; safety is one) | ◐ | ○ |
| **Post-discharge on same platform** | ● (CipherOutreach) | ○ (PX/survey core business) | ◐ (GetWell Navigate — separate product) | ◐ (Epic outreach/worklists) | ○ |

**Bottom line for internal stakeholders:** The products are not interchangeable. NRC and GetWell skew toward experience analytics and, in GetWell’s case, a broader inpatient engagement suite. Epic-native options minimize incremental vendor spend but typically shift burden to internal IT and clinical staff to configure workflows and close the loop. CipherRounds is purpose-built for rounding + recovery + safety capture, with a path to combine inpatient rounding and post-discharge outreach on one coordination layer.

---

## Detailed comparison

### 1. Capabilities

| Capability | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Patient experience rounding** | ● Structured scripts mapped to HCAHPS domains; real-time routing | ● Mobile-first; heatmaps and PX analytics | ● Real-time surveys and alerts | ◐ Rover / workflows vary by build | ◐ Inconsistent |
| **Leader / nurse-leader rounding** | ● | ● | ● | ◐ | ◐ |
| **Staff / employee rounding** | ● Recognition + staff listening | ● Strong employee voice focus | ● Supported | ○ | ◐ |
| **Location / environmental rounding** | ● Safety, CLABSI/CAUTI checks, environment audits | ◐ | ● (audit/checklist use cases) | ◐ | ◐ |
| **Service recovery routing** | ● Issue → owner in minutes; tracked start→resolution | ● Real-time recovery | ● Automated alerts to departments | ◐ Requires Epic workflow build | ○ |
| **Ambient listening / AI documentation** | ● Reduces post-round documentation | ● Agentic AI summaries (public positioning) | ○ Not primary in Rounds+ materials | ○ | ○ |
| **Predictive prioritization (who to visit first)** | ◐ Analytics + program rules | ● “Predictable Experience” heatmaps | ◐ Stronger with GetWell Inpatient data | ◐ | ○ |
| **Multi-language support** | ● | Unverified | Unverified | ◐ | ◐ |
| **EHR write-back (discrete data)** | ● Near-real-time Flowsheet write-back (Epic); HL7-ORU/MDM | ● EMR integrations listed publicly | ● Epic, Cerner, Meditech + others (AVIA) | ● Native | ○ |
| **Combined inpatient + post-discharge data** | ● Single platform (Outreach + Rounds) | ○ | ◐ Separate products | ◐ | ○ |
| **Published clinical outcomes** | ● 15+ years; HCAHPS, HAI, turnover case studies | ● Benchmark-oriented analytics | ◐ Primarily workflow/PX improvement stories | ○ Limited for rounding-specific outcomes | ○ |
| **Security certifications (verify current)** | HITRUST CSF, SOC 2 Type II, HIPAA, TX-RAMP Level 2 | Unverified — confirm in RFP | TLS 1.2+, cloud/GovCloud options (AVIA) | Epic org controls | N/A |

**Capability notes**

- **CipherRounds:** Patient, staff, and location rounding in one system; ambient listening to reduce documentation burden; analytics tie interactions to HCAHPS, safety, and staff metrics. Differentiator vs. survey-first tools: fix issues **during** the stay, not after discharge.
- **NRC Health:** Strongest when the buyer already invests in NRC for surveys/benchmarks and wants rounding + employee listening + AI documentation in the same vendor relationship.
- **GetWell Rounds+:** Flexible forms/surveys (100+ use cases per vendor materials). Full “patient engagement loop” typically assumes **GetWell Inpatient** (bedside tablets/TVs) feeding requests into Rounds+.
- **Epic-native:** Epic excels as system of record. Rounding modules/workflows can document rounds but generally require internal build for escalation, cross-department routing, and analytics comparable to a purpose-built rounding platform.
- **Paper/manual:** Zero license cost; highest variability in coverage, documentation burden, and time-to-resolution.

---

### 2. Implementation requirements

| Requirement | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **EHR integration method** | HL7 ADT in; ORU/MDM/Flowsheet out; certified Epic integration | EMR + HRIS + warehouse integrations (public) | HL7/interface + optional GetWell product integrations | Native | None |
| **Epic-specific** | Flowsheets (configurable without custom code per internal playbooks); EHR Activation Gateway for program activation | Unverified | Epic in supported EMR list; interface project typical | Module/workflow configuration | None |
| **Hardware** | Mobile devices (BYOD or hospital-issued); no in-room TV required | Mobile devices | Mobile devices; value increases with GetWell Inpatient hardware | Mobile or workstation | Paper/clipboards |
| **Network / security** | SaaS; BAA; SSO options | SaaS | SaaS; TLS 1.2+ | Internal | None |
| **Typical timeline** | **4–8 weeks** for integrated program (internal benchmark for 2026 programs) | Unverified — often phased | Standalone: weeks; full suite: months | Highly variable (months common for net-new workflow) | Immediate |
| **IT hours (buyer side)** | **<25 hours** to deploy new program (CipherHealth benchmark) | Unverified | Interface + device + content admin | Often **highest** — Epic analyst + interface team | Minimal |
| **Custom code required?** | No for standard Flowsheet mapping (internal) | Unverified | Usually interface configuration | Often workflow builds | No |
| **Dependencies** | ADT feed, rounding program design, unit champions | Analytics/HRIS if employee rounding | Strong dependency on GetWell ecosystem for full ROI | Epic module licensing, internal prioritization | None |

**Implementation notes**

- **Phased rollout** is common for all digital platforms: pilot unit → refine scripts/routing → scale. CipherHealth typically starts with highest-HCAHPS-pressure or highest-variance units.
- **Epic “free” rounding** still consumes Epic analyst time, nursing workflow design, and often produces **passive documentation** without the closed-loop recovery a purpose-built tool provides.
- **GetWell** implementations should be scoped as **Rounds+ only** vs. **Inpatient + Rounds+** — the latter is a materially larger project.

---

### 3. Support model

| Support element | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Implementation partner** | CipherHealth Implementation (certified EHR integrations) | NRC implementation / customer success | Get Well professional services | Internal IT + Epic team | Internal only |
| **Clinical program design** | CipherClinical Strategy + SMEs (RNs/MSNs); Clinical Advisory Board | NRC consulting / best practices | Get Well training resources | Internal nursing leadership | Internal |
| **Ongoing customer success** | CSM + outcomes reviews | Customer success (typical enterprise SaaS) | Customer success + training | Internal | None |
| **Analytics / outcomes reporting** | CipherHealth dashboards + annual outcomes review; EHR for clinical view | NRC analytics + benchmarks | Rounds+ dashboards; richer if Inpatient integrated | Epic reporting / SlicerDicer builds | Manual spreadsheets |
| **Escalation / support hours** | Enterprise support (confirm SLA in contract) | Unverified | Unverified | Internal IT ticket queue | N/A |
| **Security / compliance support** | Dedicated security reviews; HITRUST/SOC 2 artifacts | Confirm in RFP | Security pack on AVIA | Epic org process | N/A |
| **Expansion / new units** | CSM + Implementation for new units/programs | Unverified | Additional config + training | Epic project queue | Local decision |

**CipherHealth support model (detail for prospect)**

| Team | Role in rounding deployment |
|---|---|
| **Clinical Strategy & SMEs** | Gap analysis, script/escalation design, CNO credibility |
| **Solution Consulting** | Workflow mapping, demo, integration fit |
| **Implementation** | HL7/interface, testing, go-live |
| **CSM** | Adoption, outcomes stewardship, expansion |
| **Analytics** | HCAHPS/safety/staff metric tie-back |
| **Security & Compliance** | BAA, AI governance, audit artifacts |

---

### 4. Resource needs (operational)

Estimates below are **order-of-magnitude planning ranges** for a mid-size hospital or multi-hospital system. Actuals depend on bed count, units in scope, and program maturity. Validate in discovery.

| Resource | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Executive sponsor** | CNO or PX executive | CNO + often HR for employee rounding | CNO / COO | CNO + CIO | Unit manager |
| **Program owner (FTE)** | 0.25–0.5 FTE PX/nursing program lead | 0.25–0.5 FTE | 0.25–0.5 FTE (+ Inpatient admin if bundled) | 0.25–0.5 FTE + Epic analyst time | 0.1 FTE |
| **Unit champions** | 1 per pilot unit (nurse manager or charge) | Similar | Similar | Similar | Informal |
| **Frontline time per round** | ~2–5 min documented (digital); ambient listening reduces after-round documentation | Similar; AI summary may reduce admin | Similar | Often **higher** documentation burden | 5–10+ min + manual entry |
| **IT during implementation** | Low (<25 hours internal benchmark) | Medium | Medium–high | High | None |
| **IT ongoing** | Low (SaaS) | Low–medium | Medium (devices + interfaces) | Medium (Epic maintenance) | None |
| **Training burden** | Moderate — one-time + new hire | Moderate | Moderate; higher if Inpatient | High — Epic workflow training | Low |
| **Analytics staff** | Optional — Cipher dashboards + EHR | Often uses NRC analyst | Rounds+ admin | Epic report builders | Manual |

**Documented CipherHealth customer outcomes (rounding-adjacent — for context, not a guarantee)**

| Metric | Example result | Source type |
|---|---|---|
| HCAHPS / experience | 99th percentile key domains; +389% RN responsiveness | Lenox Hill (Northwell) — marketing-approved |
| Leader rounding | +36% top-box scores | Providence |
| HAI | 30%+ drop in CAUTI/CLABSI | Northern VA Trauma Center |
| Staff turnover | 9.2% vs 15% with >90% rounding | Regional Medical Center |
| Nurse time | ~0.5 hr/day saved via rounding workflows | Site-wide benchmark |
| Burnout | 42% drop; 30,000 leader rounds/year | Norton Healthcare |

---

## When each option wins (neutral framing)

Use this section in internal discussions without disparaging competitors.

| If the hospital’s primary goal is… | Likely best fit |
|---|---|
| Standardize leader/patient/location rounding with closed-loop recovery and optional post-discharge on one platform | **CipherRounds** (+ CipherOutreach if transitions matter) |
| Double down on PX + employee listening with AI documentation and benchmark analytics | **NRC Health** |
| Build a full in-room engagement strategy (education, requests, entertainment) with rounding as one module | **GetWell Inpatient + Rounds+** |
| Minimize new vendors; accept internal Epic build and staffing load | **Epic-native workflows** |
| No capital or alignment for digital rounding this cycle | **Paper/manual** (status quo) |

---

## Questions for Jen’s internal working group

These help tailor the comparison to their environment:

1. **Scope:** Patient-only rounding, or also leader, staff, and location/safety rounding?
2. **EHR:** Epic (which integration — Flowsheets, Rover, both)? Cerner/Meditech?
3. **Existing vendors:** NRC, GetWell, or Press Ganey/Qualtrics already in-house?
4. **Success metrics:** HCAHPS domains, HAC/safety, staff retention, grievances — which is the board-level priority?
5. **Operational constraint:** Is the blocker nursing FTE, IT queue, or vendor budget?
6. **Post-discharge:** Is rounding evaluation separate from TCM/TEAM/post-discharge outreach?

---

## Appendix A — CipherRounds capability checklist (for RFP alignment)

Use this as a line-item checklist against any vendor response.

- [ ] Patient, leader, staff, and location rounding in one platform  
- [ ] Real-time issue routing with ownership and resolution tracking  
- [ ] HCAHPS domain mapping in round scripts  
- [ ] Safety rounding (falls, HAPI, CAUTI/CLABSI, environment)  
- [ ] Ambient listening or equivalent documentation reduction  
- [ ] Bidirectional EHR integration with discrete Flowsheet write-back  
- [ ] Near-real-time data (not nightly batch only)  
- [ ] Multi-language rounding  
- [ ] Role-based analytics (unit, leader, domain, trend)  
- [ ] Clinical implementation support from licensed clinicians  
- [ ] Documented outcomes in peer-reviewed or enterprise case studies  
- [ ] HITRUST/SOC 2/HIPAA compliance artifacts  
- [ ] Optional post-discharge outreach on same platform  

---

## Appendix B — Document maintenance

| Item | Action |
|---|---|
| **Pricing** | Not included — requires scoped proposal based on bed count, modules, and integration |
| **Competitor rows marked Unverified** | Re-validate before formal RFP submission |
| **References** | Named customers cited only when cleared for that account |
| **Updates** | Refresh quarterly or when major competitor/Epic releases change the landscape |

---

*CipherHealth internal and confidential. Customer-facing shareable version should remove internal-only benchmarks marked explicitly as CipherHealth delivery data if your sponsor prefers.*
