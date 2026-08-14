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

It also includes a dedicated section on **CipherHealth-specific value** — clinical best practices, in-house clinical support, integration/interoperability, and the fact that **most of your data feeds are already configured**, which materially reduces the operational and IT lift relative to standing up a new vendor from scratch.

We pulled this together from our implementation playbooks, published vendor documentation, and third-party market summaries — not from sales decks.

If it would help your internal stakeholders, we can also walk through the comparison on a 30-minute call and tailor the “resource needs” section to your unit count and current rounding model.

Thanks again, and please reach out whenever the internal work moves forward.

Best,  
[Your name]

**Attachment:** This document (or a formatted PDF export)

---

## How to read this document

### Scope

This comparison covers **inpatient digital rounding** — structured leader/nurse/patient/location rounds with real-time issue capture, routing, and reporting. For **Penn**, it also addresses how Cipher compares to **Press Ganey**, **Huron/Studer**, and **point-solution rounding tools** against priorities: HRO/harm prevention, complaint reduction, and LTR across six entities.

It does **not** fully compare:

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

## Master side-by-side (shareable)

**Vendors:** CipherRounds · NRC Health Rounding · GetWell Rounds+ · Epic-native · Paper/manual  
**Legend:** ● Core · ◐ Partial / config-dependent · ○ Not primary · — Not applicable

### At a glance

| | **CipherRounds** | **NRC Health** | **GetWell Rounds+** | **Epic-native** | **Paper / manual** |
|---|---|---|---|---|---|
| **What it is** | Purpose-built digital rounding for patient, staff, and location rounds with closed-loop recovery | Mobile-first rounding + PX/employee analytics (Nobl acquisition, 2024) | Configurable digital rounding/survey platform; part of broader GetWell suite | EHR modules + internal workflow build (Rover = clinical bedside, not PX rounding) | Clipboards, spreadsheets, memory |
| **Vendor category** | Care coordination / rounding specialist | Experience measurement + rounding | Inpatient engagement + rounding | System of record | None |
| **Typical buyer** | CNO, PX, CQO | CNO, PX, HR | CNO, COO (often existing GetWell shop) | CIO + CNO (“use Epic”) | Unit managers |
| **Incremental license cost** | Yes — enterprise SaaS | Yes — enterprise SaaS | Yes — enterprise SaaS | Often perceived as “free” (Epic already licensed) | None |
| **Hidden cost** | Low IT lift if certified integration | Analytics/HRIS integration + quarterly consulting cadence | Larger if GetWell Inpatient bundled; interface work | **High** internal Epic analyst + nursing ops time | Nurse/leader time, inconsistency, late recovery |

---

### Capabilities

| Capability | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Patient experience rounding** | ● Scripts mapped to HCAHPS domains; real-time routing | ● Leader rounding on patients + environment | ● Real-time surveys + dashboards | ◐ Custom Flowsheets/forms; no native PX rounding product | ◐ Varies by unit |
| **Leader / nurse-leader rounding** | ● | ● | ● | ◐ Build your own | ◐ |
| **Staff / employee rounding** | ● Recognition + staff listening | ● **Core strength** — employee voice, HRIS integrations | ● Employee experience use cases | ○ | ◐ |
| **Location / environmental / safety rounding** | ● CAUTI, CLABSI, falls, HAPI, environment checks | ● Listed as quality & safety use case | ● Quality, safety, regulatory checklists (100+ use cases) | ◐ Safety checks via custom build | ◐ |
| **Real-time service recovery** | ● Issue → owner in minutes; 200M+ interactions tracked start→resolution (platform) | ● Auto-alerts; vendor cites seamless resolution | ● Alerts, reminders, escalations to departments | ◐ Requires Epic workflow/In Basket build | ○ |
| **Ambient listening / AI documentation** | ● Keeps documentation off the nurse | ● Agentic AI summaries + sentiment/themes (2026 positioning) | ○ Not a primary Rounds+ feature | ○ | ○ |
| **Predictive “who to round on first”** | ◐ Program rules + analytics | ● **Core strength** — Predictable Experience heatmaps + predictive scores | ◐ Stronger if GetWell Inpatient data present | ◐ Manual prioritization or custom build | ○ |
| **Historical PX context at bedside** | ◐ Via EHR + platform data | ● **Core strength** — past HCAHPS/survey/round data in context | ◐ With Inpatient + EHR pre-population | ◐ If built into Epic workflow | ○ |
| **Surveys-by-text / batch outreach** | ◐ (CipherOutreach for outbound) | ◐ Real-time feedback focus | ● Text/email batch surveys to patients/staff | ◐ MyChart / SMS if configured | ○ |
| **HCAHPS domain mapping** | ● Built into round scripts | ● Analytics + benchmark comparison | ◐ Configurable forms | ◐ DIY | ○ |
| **Multi-language** | ● | ◐ Confirm in demo | ◐ Pediatric: parent/caregiver rounding | ◐ MyChart language support | ◐ |
| **EHR write-back (discrete fields)** | ● Near-real-time Epic Flowsheets (HL7-ORU); MDM for issues | ● EMR integrations (vendor-stated) | ● Epic, Cerner, Meditech + 6 others; ADT | ● Native chart | ○ |
| **Data latency to EHR** | Seconds (near-real-time) | Vendor-stated real-time | Real-time alerts; interface-dependent | Native — but recovery loop is separate | — |
| **Inpatient + post-discharge same vendor** | ● CipherOutreach on one platform | ○ Surveys/measurement core; not execution layer | ◐ GetWell Navigate (separate product) | ◐ Epic worklists / MyChart | ○ |
| **In-room bedside engagement (TV/tablet)** | ○ Not required | ○ | ● **GetWell Inpatient** — routes requests into Rounds+ | ○ | ○ |
| **Industry benchmarks in product** | ◐ Outcomes library + customer analytics | ● **Core strength** — NRC benchmarks, quarterly reviews | ◐ Embedded reporting | ○ | ○ |
| **Peer-reviewed / published outcomes** | ● 15+ years customer outcomes (HCAHPS, HAI, turnover) | ◐ Vendor-cited: +22 HCAHPS percentile pts, 30% call lights, 40% falls | ◐ Primarily workflow/PX improvement | ○ Limited for rounding | ○ |

---

### Implementation

| Requirement | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Integration method** | HL7 ADT in; ORU/MDM/Flowsheet out; certified Epic | EMR + HRIS + recognition + data warehouse | HL7/ADT + EMR interface; optional GetWell product feeds | Native + possible Vendor Services for third-party | — |
| **Epic Flowsheet mapping** | ● Configurable **without custom code** (internal) | ● Vendor-stated EMR integration | ● Epic supported; interface project typical | ● Native | — |
| **Hardware required** | Mobile (BYOD or hospital device) | Mobile | Mobile/tablet; **Inpatient adds bedside TVs/tablets** | Mobile (Rover) or workstation | Paper |
| **In-room infrastructure** | None | None | Optional — significant if Inpatient | None | None |
| **Typical go-live timeline** | **4–8 weeks** (integrated program); 3–8 weeks scoping/build per program type | Phased — confirm in SOW | Rounds+ standalone: weeks; **Inpatient + Rounds+: months** | **Months** common for net-new workflow | Immediate |
| **Buyer IT hours (order of magnitude)** | **<25 hours** (CipherHealth benchmark) | Medium — EMR + analytics stack | Medium–high | **Highest** — Epic analyst, interfaces, testing | Minimal |
| **Custom code required** | No for standard Flowsheet programs | Confirm in SOW | Interface configuration typical | Often yes — workflows, reports, routing | No |
| **Certifications / security** | HITRUST CSF, SOC 2 Type II, HIPAA, TX-RAMP L2 | Confirm in RFP | HIPAA BAA, TLS 1.2+, ~99.95% SLA (AVIA) | Epic org security model | N/A |
| **Key dependencies** | ADT feed, program design, unit champions | Often existing NRC survey relationship; HRIS for employee rounding | Scope **Rounds+ only vs. full GetWell stack** | Epic module priority, internal build capacity | None |

---

### Support model

| Element | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Implementation owner** | CipherHealth Implementation (certified EHR) | NRC professional services | Get Well PS + training | Internal IT + Epic team | Internal |
| **Clinical program design** | CipherClinical (RNs/MSNs) + Clinical Advisory Board | NRC clinical/consulting; quarterly benchmark reviews | Get Well training + config | Internal nursing/PX leadership | Informal |
| **Post-go-live owner** | CSM + outcomes reviews | Customer success + quarterly data reviews | Customer success | Internal — no vendor CSM | None |
| **Analytics** | Cipher dashboards + annual outcomes review | **Benchmark-centric** reports + NRC analyst meetings | Rounds+ dashboards; richer with Inpatient | Epic SlicerDicer/report builds | Manual |
| **Expansion (new units)** | CSM + Implementation | NRC CS | Config + training | Epic project queue | Local |
| **Security / AI governance** | Dedicated security reviews; AI governance per deployment | Confirm in RFP | Standard SaaS security pack | Internal | — |

---

### Resource needs (operational)

| Resource | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Executive sponsor** | CNO or PX exec | CNO + **often HR** (employee rounding) | CNO / COO | CNO + CIO | Nurse manager |
| **Program owner** | 0.25–0.5 FTE PX/nursing lead | 0.25–0.5 FTE PX + analytics admin | 0.25–0.5 FTE (+ Inpatient admin if bundled) | 0.25–0.5 FTE + **Epic analyst allocation** | ~0.1 FTE |
| **Unit champions** | 1 per pilot unit | 1 per pilot unit | 1 per pilot unit | 1 per pilot unit | Informal |
| **Frontline time per round** | ~2–5 min capture; ambient listening cuts after-round admin | Similar; AI summary reduces documentation | Similar | Often **higher** — manual charting | 5–10+ min |
| **IT — implementation** | Low | Medium | Medium–high | **High** | None |
| **IT — ongoing** | Low (SaaS) | Low–medium | Medium (devices + interfaces if Inpatient) | Medium (Epic maintenance) | None |
| **Change management** | Moderate | Moderate | **Higher** if Inpatient deployed | **High** — workflow redesign | Low |
| **Nursing FTE impact** | Designed to **reduce** admin (0.5 hr/day saved — site benchmark) | Vendor cites call-light reduction, fall reduction | Reduces documentation vs. paper | Often **adds** workflow steps unless carefully built | High variability |

---

### Documented outcomes (examples — not guarantees)

| Outcome area | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **HCAHPS / experience** | 99th percentile key domains; +389% RN responsiveness (Lenox Hill); +36% top-box (Providence) | Vendor-cited: **+22 percentile points** across domains | Workflow/PX improvement stories | Limited rounding-specific data | Unmeasured / variable |
| **Safety (HAI, falls)** | 30%+ CAUTI/CLABSI drop; 78%/85% falls reduction | Vendor-cited: **40% fall reduction** year 1 | Safety checklist use cases | Depends on internal program | Unmeasured |
| **Staff / retention** | 9.2% vs 15% turnover at >90% rounding; 42% burnout drop (Norton) | Vendor-cited: employee voice → retention | Employee rounding use cases | — | — |
| **Operational** | 0.5 hr/day saved per nurse; 57% complaint/grievance reduction (platform) | Vendor-cited: **30% call-light reduction** | Real-time recovery alerts | — | — |

---

### When each option wins (neutral)

| Primary goal | Best fit |
|---|---|
| Standardize patient + leader + location/safety rounding with closed-loop recovery; optionally combine with post-discharge on one platform | **CipherRounds** (+ CipherOutreach if transitions matter) |
| PX/employee listening, predictive prioritization, benchmark analytics; already an NRC survey customer | **NRC Health** |
| Full in-room engagement (education, requests, entertainment) with rounding as one module | **GetWell Inpatient + Rounds+** |
| Minimize new vendors; willing to spend internal Epic + nursing ops capacity | **Epic-native build** |
| No budget or alignment this cycle | **Paper/manual** |

**Bottom line:** These are not interchangeable. NRC leads on **measurement, prediction, and benchmarks**. GetWell leads when **in-room engagement** is already in scope. Epic-native minimizes **vendor spend** but shifts cost to **internal build and staffing**. CipherRounds is built for **operational rounding + recovery + safety** with a path to **post-discharge on the same coordination layer**.

---

## CipherHealth differentiated value

*This section answers: “Why CipherRounds specifically — beyond a feature checklist?” Use it with Jen’s CNOs, CIO, and operational sponsors.*

### Headline for internal conversations

> **CipherHealth is not a rounding app — it is 15+ years of clinically validated best practices, delivered with in-house nursing leadership, on an integration footprint you have largely already built.**

---

### 1. Clinical best practices (not templates)

| Dimension | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Program origin** | ● 15+ years of scripts & escalation paths built by frontline nurses | ◐ Best-practice consulting + benchmarks | ◐ Configurable forms (100+ use cases) | ◐ Internal design | ◐ Unit-by-unit habit |
| **HCAHPS domain mapping** | ● Built into standard round scripts | ● Analytics overlay | ◐ Form configuration | ◐ DIY | ○ |
| **Safety program library (HAC, falls, HAPI, lines)** | ● Standardized patient + location rounding checklists | ◐ PX-weighted; safety listed | ◐ Checklist use cases | ◐ Build required | ◐ |
| **Service recovery playbooks** | ● Route negative signal → owner in minutes; tracked start→resolution | ● Real-time alerts | ● Alert/escalation engine | ◐ Workflow build | ○ |
| **Evidence base** | ● 1B+ encounters; outcomes tied to HCAHPS, HAI, turnover | ● Benchmark library | ◐ Workflow improvement | ○ | ○ |
| **Continuous refinement** | ● Clinical Advisory Board + customer outcomes feed roadmap | ● Quarterly benchmark reviews | ◐ Product updates | ◐ Internal only | ○ |
| **“What to do next” guidance** | ● Actionable analytics — not just what happened | ◐ Predictive prioritization | ◐ Dashboards | ◐ Reports | ○ |

**What this means in practice**

- Rounding scripts, escalation paths, and safety checklists are **clinical programs refined across hundreds of health systems** — not blank forms your nurses have to design from scratch.
- Every round maps to a **specific HCAHPS domain or safety objective**, so leaders can tie daily work to board-level metrics (VBP, HAC Reduction Program, Leapfrog).
- Competitors offer **configuration** or **measurement**; CipherHealth offers **proven workflows** that CNOs at peer systems (Henry Ford, Prisma, Norton, Intermountain, MD Anderson, and others on the Clinical Advisory Board) have helped shape.

---

### 2. Clinical support (partnership, not a services upsell)

| Support element | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **In-house clinical leadership** | ● SVP Clinical Strategy (Joy Avery, MSN, RN) + VP Clinical Services (Donna Pritchard, DNP, FNP-BC) — both former CNO/C-suite operators | ◐ Consulting & benchmark analysts | ◐ Training & implementation | ○ Internal only | ○ |
| **Clinical Advisory Board** | ● 9 senior nurse/PX/care-management executives at peer systems vet workflows & roadmap | ○ | ○ | ○ | ○ |
| **Program design support** | ● Gap analysis, custom script design, escalation mapping — led by RNs/MSNs | ● Quarterly data reviews | ◐ Config assistance | ◐ Internal nursing | ○ |
| **“Will this work for our nurses?”** | ● Bring Clinical Strategy to CNO/CMO conversations | ◐ PX consulting | ◐ Training | ◐ Internal | ○ |
| **Post-go-live clinical stewardship** | ● CSM + annual outcomes review + Analytics tie-back | ● CS + benchmark sessions | ● CS | ○ | ○ |
| **Safety / quality alignment** | ● CQO-ready: HAC, falls, HAPI programs built in | ◐ | ◐ | ◐ | ○ |

**CipherHealth clinical teams available on deals**

| Team | What they do |
|---|---|
| **Clinical Strategy & SMEs** | Designed the scripts and escalation paths; run gap analyses and custom program design |
| **Clinical Advisory Board** | Peer CNO/PX leaders who validate that workflows reflect real-world nursing operations |
| **Solution Consulting** | Workflow mapping, integration fit, tailored demos |
| **Implementation** | Certified Epic/Cerner/Meditech go-live |
| **CSM + Analytics** | Adoption, outcomes stewardship, HCAHPS/safety/staff metric reviews |

**Objection this answers:** *“This adds to nurse workload.”* → Clinical SMEs co-design the rollout; ambient listening removes post-round documentation; customer benchmarks show ~0.5 hr/day returned per nurse and 42% burnout reduction (Norton, 30,000 leader rounds/year).

---

### 3. Integration & interoperability

| Dimension | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **EHR strategy** | ● Augments EHR as **system of action**; EHR stays system of record | ● EMR + HRIS + warehouse | ● EMR + optional GetWell product feeds | ● EHR-only | — |
| **Epic certification** | ● Certified integration; 70%+ of customers / 350+ hospitals on Epic | ● Vendor-stated EMR integrations | ● Epic in supported EMR list | ● Native | — |
| **Inbound feeds** | ● HL7-ADT (demographics, encounter); SFTP flat-file fallback | ● EMR integrations | ● ADT + EMR pre-population | ● Native | — |
| **Outbound write-back** | ● HL7-ORU → discrete Epic Flowsheets (seconds); HL7-MDM for issue documentation | ● Vendor-stated | ● Interface-dependent | ● Native | — |
| **Flowsheet configurability** | ● **No custom code** for standard programs — configurable mapping | Confirm in SOW | Interface project typical | ◐ Analyst build | — |
| **EHR Activation Gateway** | ● Streamlines program activation & patient data movement with Epic | ○ | ○ | ○ | — |
| **Data latency** | ● Near-real-time (seconds, not nightly batch) | Vendor-stated real-time | Real-time alerts; varies | Native chart; recovery loop separate | — |
| **Multi-EHR support** | ● Epic, Cerner, Meditech (bidirectional) | ● EMR + HRIS + warehouse | ● 9+ EMRs listed | Single EHR | — |
| **One-to-many integration model** | ● One integration footprint serves Outreach + Rounds + Access | ◐ | ◐ | ○ | — |
| **Platform consolidation** | ● Single vendor, single security posture, single analytics hub | ◐ PX/HR focus | ◐ Broader if Inpatient added | ◐ | ○ |
| **Security / compliance** | ● HITRUST CSF, SOC 2 Type II, HIPAA, TX-RAMP Level 2 | Confirm in RFP | HIPAA BAA, TLS 1.2+ | Epic org controls | — |

**Interoperability in plain language**

- **Inbound:** ADT tells CipherHealth who is on which unit — patients appear on rounding lists automatically.
- **Outbound:** Round responses land as **discrete Flowsheet rows in Epic within seconds**, so nurses and leaders act from the chart, not a separate silo.
- **What stays in CipherHealth:** Operational analytics (reach, coverage, time-to-resolution, unit trends) — set this expectation early with CIO.
- **Why this matters vs. competitors:** Many tools store rounding data in a standalone repository. CipherHealth writes structured results **into the workflow clinicians already use**, without a custom interface build for each program.

---

### 4. Your integration footprint — feeds largely in place

**For your organization:** Through the work already completed in this evaluation (slide-deck discovery, integration scoping, and/or existing CipherHealth connectivity), **most of the core data feeds required for CipherRounds are already configured or mapped**. Rounding is not a greenfield interface project.

| Feed / capability | Typical status | Rounding impact |
|---|---|---|
| **HL7-ADT (patient eligibility / census)** | ● Already established or scoped | Patients auto-populate on unit rounding lists — no manual census |
| **Epic Flowsheet outbound (HL7-ORU)** | ● Already established or mapped | Round responses visible in chart in near-real-time |
| **Issue documentation (HL7-MDM)** | ◐ Confirm final mapping | Service-recovery notes can flow into Epic |
| **EHR Activation Gateway** | ◐ Available if on Epic | Faster program activation; less IT re-work per new unit |
| **Security / BAA / SSO** | ● Already in place or in progress | No new vendor security review cycle from scratch |

**What is still needed (order of magnitude)**

| Workstream | Owner | Lift |
|---|---|---|
| Rounding-specific Flowsheet row mapping | Cipher Implementation + Epic analyst | Low — mostly configuration, not custom code |
| Round scripts & escalation paths | CipherClinical + your PX/nursing lead | Moderate — clinical design, not IT |
| Unit champion training & pilot | Your nursing ops + Cipher CSM | Moderate — change management |
| Net-new IT interface work | Your IT team | **Minimal** — majority of feeds already done |

**Compare to alternatives**

| Scenario | Typical IT lift |
|---|---|
| **CipherRounds at your org (feeds in place)** | **<25 hours** remaining (internal benchmark) |
| New vendor — stand up ADT + EMR write-back from zero | 80–200+ hours |
| Epic-native — build workflows, reports, routing | 100–300+ hours (Epic analyst queue) |
| GetWell Inpatient + Rounds+ (if not already deployed) | Months + device + interface work |

**Message for the CIO:** *“You are not buying another integration project. You are activating a clinical program on infrastructure that is largely already built.”*

---

### 5. Additional value (beyond rounding)

| Value | CipherHealth | Competitors (typical) |
|---|---|---|
| **Full care continuum on one platform** | ● Pre-admission → inpatient rounding → post-discharge outreach (CipherOutreach) — one coordination layer | ◐ Rounding-only, survey-only, or in-room-only |
| **Longitudinal patient data** | ● 1B+ encounters; 200M+ interactions tracked start→resolution; 17M documented patient saves | ◐ Siloed to PX or single workflow |
| **Workforce extension** | ● Ambient listening + automation give nurses time back; not “another login” | ◐ Often adds documentation or survey admin |
| **AI governance** | ● Purpose-built for healthcare; no secondary training on customer data; security-reviewed deployments | Varies — validate in RFP |
| **Enterprise pricing model** | ● No per-message/per-call charges — programs optimized for reach, not metered usage | Varies |
| **Outcomes accountability** | ● Published customer results across HCAHPS, readmissions, HAI, staff retention | ◐ Benchmark or workflow stories |
| **Vendor consolidation** | ● Replace or avoid point solutions for rounding + outreach + recovery | ◐ Often requires multiple products |
| **TCM / TEAM / HAC readiness (2026)** | ● Same platform runs CMS-aligned post-discharge programs with shared integration | ◐ Not core for NRC/GetWell rounding |
| **Reference depth** | ● 350+ hospitals; 70%+ Epic; named outcomes (Lenox Hill, Providence, Norton, Intermountain, etc.) | Varies |

**Platform proof points (marketing-approved — use with reference discipline)**

| Metric | Result | Context |
|---|---|---|
| Patient reach (post-discharge) | 96% vs ~40% portal | Digital-first vs. MyChart-dependent |
| IT deployment | <25 hours for new program | CipherHealth benchmark |
| Readmission reduction | Up to 41% (Intermountain) | Outreach + coordination |
| HCAHPS | 99th percentile key domains (Lenox Hill) | After rounding program redesign |
| Staff turnover | 9.2% vs 15% at >90% rounding | Regional Medical Center |
| Nurse time returned | 0.5 hr/day | Rounding workflows |
| Complaints & grievances | 57% reduction | Platform benchmark |

---

### Side-by-side: “soft” factors that drive adoption

| Factor | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper |
|---|---|---|---|---|---|
| **Clinical credibility in the room** | ● CNO-grade clinical team + Advisory Board | ● PX/HR analytics credibility | ◐ Implementation/training | ◐ Internal champions only | ○ |
| **Time to value (your org)** | ● **Weeks** — feeds largely done | Phased | Weeks–months | Months | — |
| **Nurse adoption friction** | ● No new login; embedded workflow; ambient listening | ● Mobile-first | ● App-based | ◐ Epic workflow training | Low initially |
| **CIO risk** | ● Certified, HITRUST; minimal net-new interfaces | Medium | Medium–high | High internal queue | None |
| **CFO story** | ● Workforce + penalty avoidance + consolidation | ◐ Benchmark ROI | ◐ Varies by scope | ◐ “Free” license, hidden labor | None |
| **Expand path** | ● Add units, safety programs, Outreach on same platform | ◐ Add PX modules | ◐ Add Inpatient, Navigate | ◐ Epic roadmap | — |

---

## Where Cipher wins — and why the alternatives do not compare (Penn)

*Use this section with Penn stakeholders when the conversation is about **HRO and harm prevention**, **complaint reduction**, and **Likelihood to Recommend (LTR)** across **all six entities** — not a generic rounding bake-off.*

### Penn’s priorities vs. what each category actually delivers

If Penn’s priorities are advancing **High Reliability Organization (HRO) principles and harm prevention**, **reducing complaints and grievances**, and **improving Likelihood to Recommend**, this is **not a comparison of equivalent platforms**.

Press Ganey, Huron/Studer, and point-solution rounding tools each address **a portion** of the challenge. **None** provides Cipher’s integrated, real-time infrastructure for:

1. **Identifying** risk  
2. **Driving** intervention  
3. **Verifying** resolution  
4. **Measuring** the outcome  

…across all six entities on one platform.

| Penn priority | What Cipher delivers | Press Ganey | Huron/Studer | Point solutions (Nobl, MyRounding, etc.) |
|---|---|---|---|---|
| **HRO / harm prevention** | ● Real-time safety tracers (falls, HAPI, CAUTI/CLABSI, environment); location + patient rounding; auditability | ○ Post-hoc survey signals | ◐ Methodology & training | ◐ Document the round only |
| **Reduce complaints / grievances** | ● In-stay service recovery with named ownership, SLA routing, verified closure | ○ Identifies dissatisfaction after discharge | ◐ Teaches recovery behavior | ◐ Alert or record — closure varies |
| **Improve LTR / HCAHPS** | ● Fix experience **before** discharge; analytics tie intervention → LTR domains | ● Benchmarks **after** the stay | ◐ Rounding habits via consulting | ◐ Leader-round documentation |
| **Enterprise consistency (6 entities)** | ● One platform, one routing model, one analytics layer, Epic-integrated | ◐ System-level benchmarks | ◐ Engagement-dependent | ○ Per-site tools & reports |
| **Closed-loop accountability** | ● Concern → owned action → verified resolution → measurable outcome | ○ Awareness only | ○ Expectations, not enforcement | ◐ Task created ≠ resolved |
| **Post-discharge continuity** | ● CipherOutreach confirms resolution & captures post-discharge signal | ● Surveys | ○ | ○ Separate product required |

---

### Press Ganey: Measures what happened; it does not change what is happening

**What Press Ganey is built for:** Post-discharge surveys, benchmarking, and retrospective analytics.

**What it does not provide:** Bedside workflows, real-time routing, accountable ownership, and verified resolution needed to intervene **while the patient is still in Penn’s care**.

| Capability | Press Ganey | Cipher |
|---|---|---|
| Tell Penn where dissatisfaction occurred | ● Strong | ● Also captures in-stay signals |
| Intervene at the bedside before discharge | ○ | ● |
| Route issue to named owner with SLA | ○ | ● Enterprise routing by issue, severity, location, department |
| Verify the issue was resolved — not just referred | ○ | ● Closed-loop completion |
| Connect intervention to complaint/LTR improvement | ◐ Retrospective correlation | ● Longitudinal: round → action → resolution → outcome |
| Quality & safety tracers (HAC, falls, lines) | ○ | ● Built-in |
| Epic-integrated operational workflow | ○ | ● Near-real-time Flowsheet write-back |

**Why it matters for Penn:** A complaint identified **after discharge** is a missed opportunity for service recovery. Penn does not need more **awareness** of its scores — it needs the ability to **change the patient experience before that experience becomes a complaint or a low LTR rating**.

> **Distinction:** Press Ganey is the **system of insight** (what already broke). Cipher is the **system of execution** (what happens next).

---

### Huron/Studer: Provides the methodology, but not the enterprise execution infrastructure

**What Huron/Studer is built for:** Respected consulting, training, and rounding **methodology**.

**What it does not compare with:** Cipher’s technology depth — intelligent patient prioritization, ambient capture, AI-generated summaries, enterprise escalation routing, Epic-integrated workflows, comprehensive auditability, and closed-loop issue resolution.

| Capability | Huron/Studer | Cipher |
|---|---|---|
| Establish rounding expectations & leader behaviors | ● Consulting & training | ● Clinical programs + in-house nurse SMEs |
| Reinforce expectations daily across 6 entities | ○ Depends on local discipline post-engagement | ● Embedded workflows, automation, measurement |
| Intelligent patient prioritization | ○ | ● Smart prioritization + context-aware workflows |
| Ambient capture / AI-generated summaries | ○ | ● Reduces documentation burden on nurses |
| Enterprise escalation routing with SLAs | ○ | ● Dynamic triggers, alerts, next-best-action |
| Epic-integrated, auditable workflows | ○ | ● Certified integration; feeds largely in place at Penn |
| Verified closed-loop resolution | ○ | ● Not task creation — resolution confirmed |
| Sustained outcomes after consulting ends | ◐ Variable | ● CSM, analytics, Clinical Advisory Board |

**Why it matters for Penn:** Training can establish expectations, but Penn needs a **system that reinforces those expectations every day** across six entities. Without embedded workflows, ownership, automation, and measurement, **consistency declines after the consulting engagement ends**.

> **Distinction:** Huron/Studer **teaches the methodology**. Cipher **operationalizes it in real time** — every shift, every unit, every entity.

---

### Point-solution tools: Digitize a round; they do not coordinate the full response

**Examples:** Nobl (now NRC Health), MyRounding, iRound, and similar tools.

**What they do:** Document nurse-leader or patient rounds.

**What they do not compare with:** Cipher’s broader capabilities across quality and safety tracers, real-time service recovery, intelligent workflow automation, discharge outreach, and longitudinal outcome measurement.

| Capability | Point solutions | Cipher |
|---|---|---|
| Document a leader/patient round | ● | ● |
| Quality & safety tracers (HAC program, environment, lines) | ◐ Limited or add-on | ● Native |
| Real-time service recovery with enterprise routing | ◐ Basic alerts | ● By issue, severity, location, department, SLA |
| Intelligent workflow automation | ○ | ● Triggers, dynamic questions, next-best-action |
| Ambient capture + AI summaries | ◐ NRC/Nobl adds this post-acquisition | ● |
| Post-discharge follow-up / confirmation | ○ Separate vendor | ● CipherOutreach on same platform |
| Connect bedside concern → post-discharge outcome | ○ | ● Longitudinal on one platform |
| Enterprise integration (Epic, APIs) | ◐ Interface per tool | ● Certified; Penn feeds largely configured |
| Implementation + workflow design + adoption services | ◐ Varies | ● Clinical Strategy, Implementation, CSM |
| Single accountability model across 6 entities | ○ Fragmented | ● One platform, one analytics hub |

**Why it matters for Penn:** Penn would likely need **multiple products, integrations, and reporting structures** to approximate what Cipher provides natively. That creates **fragmented accountability** and makes it harder to determine whether an issue was merely **recorded**, **referred to someone**, or **actually resolved**.

> **Distinction:** Point solutions **document an isolated workflow**. Cipher **coordinates the full response** — identify, intervene, verify, measure.

---

### Cipher: Built for the priorities Penn is trying to advance

Cipher uniquely brings together:

- **Real-time identification** of patient, safety, and service concerns  
- **Smart patient prioritization** and context-aware rounding workflows  
- **Ambient capture** and AI-generated summaries  
- **Dynamic questions, triggers, alerts**, and next-best-action guidance  
- **Epic integration** and flexible APIs — with **most data feeds already configured at Penn**  
- **Enterprise routing** by issue, severity, location, department, and SLA  
- **Quality and safety tracers** with comprehensive auditability  
- **Named ownership and escalation** across all six entities  
- **Verified, closed-loop completion** — not simply task creation or referral  
- **Post-discharge confirmation** through CipherOutreach  
- **Analytics** connecting rounding, intervention, complaints, outcomes, and LTR  
- **Implementation, integration, workflow design, adoption, and optimization** services — led by in-house clinical leaders, not generic project managers  

#### Side-by-side: the full loop Penn needs

| Stage | Press Ganey | Huron/Studer | Point solutions | **Cipher** |
|---|---|---|---|---|
| **1. Identify risk** | After discharge (survey) | During consulting engagement | At round (manual) | ● Real-time, in-stay, prioritized |
| **2. Drive intervention** | ○ | ◐ Trained behavior | ◐ Alert/record | ● Routed action with owner + SLA |
| **3. Verify resolution** | ○ | ○ | ◐ Unclear | ● Closed-loop confirmation |
| **4. Measure outcome** | ● Benchmarks | ◐ Post-project review | ◐ Tool reports | ● LTR, complaints, safety, HCAHPS tied to intervention |
| **5. Sustain across 6 entities** | ◐ Benchmark only | ◐ Fades post-engagement | ○ Fragmented | ● One enterprise platform |

---

### The fundamental distinction

The alternatives do not compare in the areas most critical to Penn because they were built for **different purposes**:

| Category | Built to… | Gap for Penn |
|---|---|---|
| **Press Ganey** | Measure the experience **after** it occurs | Cannot change what is happening at the bedside |
| **Huron/Studer** | Teach the **methodology** | Cannot enforce it daily across six entities without embedded technology |
| **Point solutions** | **Document** an isolated workflow | Cannot coordinate identification → intervention → verification → measurement |
| **Cipher** | **Operationalize the entire process in real time** | — |

**For Penn, that distinction matters.** Harm prevention and service recovery depend on **what happens next** — not simply what is measured, taught, or documented.

Cipher ensures that:

1. A **concern** becomes an **owned action**  
2. The action becomes a **verified resolution**  
3. The resolution connects to **measurable improvements** in complaints, safety, and LTR  

…across all six entities, on infrastructure Penn has largely already built.

---

## Detailed notes (by vendor)

### CipherRounds (CipherHealth)

- **Core job:** Execute rounding — patient, leader, staff, location — and close the loop before discharge.
- **Differentiators vs. others:** Same platform as CipherOutreach (pre-admission through post-discharge); ambient listening; safety rounding tied to HAC/VBP; near-real-time Flowsheet write-back without custom code; clinical SMEs co-design programs.
- **Implementation (internal benchmarks):** 4–8 weeks; <25 IT hours; HL7 ADT in / ORU+MDM out; 70%+ of customers on Epic (350+ hospitals).
- **Support:** Clinical Strategy, Solution Consulting, Implementation, CSM, Analytics, Security.

### NRC Health Rounding

- **Core job:** Make rounding intentional with **predictive prioritization**, **benchmark analytics**, and **employee + patient voice** in one relationship — especially if NRC already runs your HCAHPS/survey program.
- **Differentiators vs. others:** Predictable Experience (predicted in-stay experience scores); deep historical PX context at bedside; quarterly benchmark reviews with NRC analysts; Nobl acquisition (2024) for real-time rounding; HRIS integrations for employee rounding.
- **Tradeoffs:** Measurement and PX intelligence are the center of gravity; post-discharge **execution** (TCM calls, automated follow-up) is not the core product. Validate integration depth and timeline in SOW.

### GetWell Rounds+

- **Core job:** Flexible digital data collection — PX rounding, employee rounding, safety/regulatory audits, discharge data — on one configurable platform.
- **Differentiators vs. others:** 100+ use cases; surveys-by-text/email for batch reach; unlimited users/devices; **deepest value when GetWell Inpatient is deployed** (in-room requests route into Rounds+ for recovery).
- **Tradeoffs:** Scope creep risk — Rounds+ alone vs. Inpatient + Rounds+ is a very different project size. GetWell Navigate is a separate product for outpatient/post-discharge AI texting. No ambient listening as a headline capability.

### Epic-native (build inside Epic)

- **Core job:** Keep everything in the EHR; avoid incremental vendor spend.
- **Reality check:** Epic Rover is a **clinical bedside** tool (BCMA, vitals, specimen collection) — **not** a leader/PX rounding platform. PX rounding in Epic typically means custom Flowsheets, reports, and In Basket routing built by your Epic team.
- **Tradeoffs:** License may be “free,” but **labor is not** — Epic analyst time, workflow design, and ongoing maintenance. Passive documentation without purpose-built recovery/routing. Internal playbooks note Epic-native outreach reaches ~40% of patients vs. ~96% digital-first; data can lag 24 hours if batch-based.

### Paper / manual

- **Core job:** Zero software cost.
- **Tradeoffs:** Inconsistent coverage, issues surface after discharge, no closed-loop tracking, highest documentation burden, no cross-unit analytics. Status quo bias is the main “competitor” in stalled deals.

---

## Questions for Penn’s internal working group

These help tailor the comparison to Penn’s six-entity environment:

1. **Scope:** Patient-only rounding, or also leader, staff, location/safety, and quality tracers across all entities?
2. **EHR:** Epic Flowsheet integration status — what is live vs. still to map for rounding-specific rows?
3. **Existing vendors:** Press Ganey (surveys/benchmarks), Huron/Studer (methodology), Nobl/NRC, or other point tools already in use?
4. **Success metrics:** HRO/harm events, complaints/grievances, LTR — which is the board-level priority per entity?
5. **Operational constraint:** Is the blocker nursing FTE, IT queue, funding, or cross-entity alignment?
6. **Accountability model:** Today, can Penn confirm an issue was **resolved** — not just recorded or referred — across all six entities?
7. **Post-discharge:** Should bedside concerns connect to CipherOutreach follow-up on the same platform?

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
