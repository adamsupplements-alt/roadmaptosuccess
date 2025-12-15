from __future__ import annotations

from pathlib import Path
import base64
import mimetypes

import streamlit as st


# =============================
# Page config
# =============================
st.set_page_config(
    page_title="LQR Road Map to SUCCESS",
    page_icon="🏠",
    layout="centered",
)


# =============================
# Paths
# =============================
APP_ROOT = Path(__file__).parent
ASSETS_DIR = APP_ROOT / "assets"
VAULT_DIR = APP_ROOT / "vault"
LOGO_PATH = ASSETS_DIR / "lqr_logo.png"


# =============================
# Brand palette (logo-derived)
# =============================
BRAND = {
    "primary": "#006BDD",
    "primary_dark": "#0A4FA8",
    "navy": "#0B1B2B",
    "text": "#0F172A",
    "muted": "#475569",
    "bg": "#FFFFFF",
    "surface": "#F6F8FC",
    "border": "#E5E7EB",
    "success": "#16A34A",
    "warning": "#F59E0B",
    "danger": "#EF4444",
}


def _b64_image(path: Path) -> str | None:
    if not path.exists():
        return None
    return base64.b64encode(path.read_bytes()).decode("utf-8")


LOGO_B64 = _b64_image(LOGO_PATH)


# =============================
# Global styling
# =============================
st.markdown(
    f"""
<style>
  /* ====== App baseline ====== */
  .stApp {{
    background: {BRAND["bg"]};
    color: {BRAND["text"]};
  }}

  header[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
  }}

  section[data-testid="stMain"] .block-container {{
    padding-top: 1.0rem;
    padding-bottom: 2.2rem;
    max-width: 980px;
  }}

  /* ====== Sidebar hard override (prevents white-on-white / dark theme mismatch) ====== */
  [data-testid="stSidebar"] {{
    background: {BRAND["surface"]} !important;
    border-right: 1px solid {BRAND["border"]} !important;
  }}
  [data-testid="stSidebar"], [data-testid="stSidebar"] * {{
    color: {BRAND["navy"]} !important;
  }}
  [data-testid="stSidebar"] a {{
    color: {BRAND["primary"]} !important;
  }}
  [data-testid="stSidebar"] .stCaption,
  [data-testid="stSidebar"] .stMarkdown small {{
    color: {BRAND["muted"]} !important;
  }}

  /* ====== Typography polish ====== */
  h1, h2, h3, h4 {{
    color: {BRAND["navy"]};
  }}
  .muted {{
    color: {BRAND["muted"]};
  }}

  /* ====== Header ====== */
  .lqr-top {{
    border: 1px solid {BRAND["border"]};
    background: linear-gradient(180deg, #FFFFFF 0%, {BRAND["surface"]} 100%);
    border-radius: 18px;
    padding: 14px 16px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
    margin-bottom: 14px;
  }}
  .lqr-title {{
    margin: 0;
    font-size: 1.25rem;
    line-height: 1.15;
    letter-spacing: .02em;
    text-transform: uppercase;
    color: {BRAND["navy"]};
  }}
  .lqr-title span {{
    color: {BRAND["primary"]};
    font-weight: 900;
  }}
  .lqr-sub {{
    margin: 6px 0 0;
    color: {BRAND["muted"]};
    font-size: .95rem;
  }}
  .pill {{
    border-radius: 999px;
    padding: .38rem .75rem;
    border: 1px solid rgba(0,107,221,.25);
    background: rgba(0,107,221,.08);
    font-size: .72rem;
    text-transform: uppercase;
    letter-spacing: .09em;
    display:inline-flex;
    align-items:center;
    gap:.45rem;
    color: {BRAND["navy"]};
    white-space: nowrap;
  }}
  .dot {{
    width: 8px;
    height: 8px;
    border-radius: 999px;
    background: {BRAND["success"]};
    box-shadow: 0 0 0 6px rgba(22,163,74,.16);
    display:inline-block;
  }}

  /* ====== Cards / blocks ====== */
  .card {{
    border: 1px solid {BRAND["border"]};
    background: #FFFFFF;
    border-radius: 18px;
    padding: 14px 14px 12px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
    height: 100%;
  }}
  .card h3 {{
    margin: 0 0 6px;
    font-size: 1.02rem;
    color: {BRAND["navy"]};
  }}
  .card p {{
    margin: 0 0 10px;
    color: {BRAND["muted"]};
    font-size: .95rem;
  }}

  .block {{
    border: 1px solid {BRAND["border"]};
    background: #FFFFFF;
    border-radius: 18px;
    padding: 14px 14px 10px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
    margin-bottom: 12px;
  }}

  .callout {{
    border-radius: 14px;
    border: 1px dashed rgba(0,107,221,.45);
    background: rgba(0,107,221,.06);
    padding: 10px 12px;
    color: {BRAND["navy"]};
    font-size: .95rem;
    margin-top: 8px;
  }}

  /* ====== Badges ====== */
  .badge {{
    display:inline-block;
    border-radius: 999px;
    padding: .18rem .6rem;
    font-size: .70rem;
    text-transform: uppercase;
    letter-spacing: .08em;
    border: 1px solid {BRAND["border"]};
    color: {BRAND["muted"]};
    white-space: nowrap;
  }}
  .badge.accent  {{ border-color: rgba(0,107,221,.45); color: {BRAND["primary_dark"]}; background: rgba(0,107,221,.06); }}
  .badge.success {{ border-color: rgba(22,163,74,.45); color: {BRAND["success"]}; background: rgba(22,163,74,.06); }}
  .badge.warning {{ border-color: rgba(245,158,11,.45); color: {BRAND["warning"]}; background: rgba(245,158,11,.06); }}
  .badge.danger  {{ border-color: rgba(239,68,68,.45); color: {BRAND["danger"]};  background: rgba(239,68,68,.06); }}

  /* ====== Streamlit buttons (primary) ====== */
  div.stButton > button {{
    border-radius: 999px !important;
    border: 1px solid rgba(0,107,221,.22) !important;
    background: {BRAND["primary"]} !important;
    color: white !important;
    font-weight: 800 !important;
  }}
  div.stButton > button:hover {{
    border-color: rgba(0,107,221,.55) !important;
    background: {BRAND["primary_dark"]} !important;
  }}
  div.stButton > button:disabled {{
    opacity: .55 !important;
    background: #CBD5E1 !important;
    border-color: #CBD5E1 !important;
    color: #0F172A !important;
  }}

  /* ====== Expanders polish ====== */
  details summary {{
    font-weight: 800 !important;
    color: {BRAND["navy"]} !important;
  }}
</style>
""",
    unsafe_allow_html=True,
)


# =============================
# Navigation state
# =============================
PAGES = {
    "home": "Buckets",
    "vault": "Vault",
    "training": "Training",
    "bucket_denied": "Denied",
    "bucket_components": "Components Only",
    "bucket_shingles": "Shingle Repairs",
    "bucket_slopes": "Slope Approval",
    "bucket_full": "Full Roof Approval",
    "comp_vents": "Components • Vents",
    "comp_flashings": "Components • Flashings",
    "comp_valleys": "Components • Valleys",
}

if "page" not in st.session_state:
    st.session_state.page = "home"


def go(page_key: str):
    st.session_state.page = page_key
    st.rerun()


# =============================
# UI helpers
# =============================
def badge(text: str, kind: str = "accent"):
    st.markdown(f'<span class="badge {kind}">{text}</span>', unsafe_allow_html=True)


def block(title: str, body_md: str = "", callout_html: str | None = None):
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown(f"### {title}")
    if body_md:
        st.markdown(body_md)
    if callout_html:
        st.markdown(f'<div class="callout">{callout_html}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def header():
    st.markdown('<div class="lqr-top">', unsafe_allow_html=True)

    c_logo, c_title, c_pill = st.columns([0.34, 0.46, 0.20], vertical_alignment="center")

    with c_logo:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_container_width=True)
        else:
            st.markdown("**LQR**")

    with c_title:
        st.markdown(
            f"""
<h1 class="lqr-title">LQR <span>Road Map to SUCCESS</span></h1>
<div class="lqr-sub">Pick the bucket. Follow the steps. Win the claim.</div>
""",
            unsafe_allow_html=True,
        )

    with c_pill:
        st.markdown(
            '<div class="pill"><span class="dot"></span><span>Bucket Picker</span></div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


def nav_sidebar(current_page: str):
    with st.sidebar:
        st.markdown("## Navigation")
        selection = st.radio(
            "Go to",
            options=list(PAGES.keys()),
            format_func=lambda k: PAGES[k],
            index=list(PAGES.keys()).index(current_page) if current_page in PAGES else 0,
            key="sidebar_nav",
        )
        if selection != current_page:
            go(selection)

        st.markdown("---")
        st.caption("Tip: Keep your vault file/folder names EXACT (case-sensitive).")


def bottom_nav(active_key: str):
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🧺 Buckets", use_container_width=True, disabled=(active_key == "home"), on_click=go, args=("home",), key=f"nav_home_{active_key}")
    with c2:
        st.button("🔎 Vault", use_container_width=True, disabled=(active_key == "vault"), on_click=go, args=("vault",), key=f"nav_vault_{active_key}")
    with c3:
        st.button("📚 Training", use_container_width=True, disabled=(active_key == "training"), on_click=go, args=("training",), key=f"nav_training_{active_key}")


def docs_section(doc_items: list[tuple[str, str]]):
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("### Recommended Docs")
    st.caption("If a file isn’t present in the repo under /vault, you’ll see “Not found.”")

    for i, (label, rel_path) in enumerate(doc_items):
        file_path = APP_ROOT / rel_path
        if file_path.exists() and file_path.is_file():
            data = file_path.read_bytes()
            mime, _ = mimetypes.guess_type(str(file_path))
            st.download_button(
                label=f"⬇️ {label}",
                data=data,
                file_name=file_path.name,
                mime=mime or "application/octet-stream",
                use_container_width=True,
                key=f"dl_{rel_path}_{i}",
            )
        else:
            st.warning(f"Not found: {rel_path}")

    st.markdown("</div>", unsafe_allow_html=True)


def vault_browser():
    block(
        "Vault",
        "Search, browse, and download anything under `/vault`.",
        "If you don’t see a file, confirm it exists in the GitHub repo and was deployed with the app.",
    )

    query = st.text_input("Search vault files", placeholder="Type part of a filename (ex: repairability, IRC, oakridge)…", key="vault_search")
    only_pdf = st.toggle("PDF only", value=False, key="vault_pdf_only")

    if not VAULT_DIR.exists():
        st.error("No /vault folder found in the repo.")
        return

    files = [p for p in VAULT_DIR.rglob("*") if p.is_file()]
    if only_pdf:
        files = [p for p in files if p.suffix.lower() == ".pdf"]

    if query.strip():
        q = query.strip().lower()
        files = [p for p in files if q in p.name.lower() or q in str(p.relative_to(VAULT_DIR)).lower()]

    files.sort(key=lambda p: str(p.relative_to(VAULT_DIR)).lower())

    st.caption(f"Files found: {len(files)}")

    if not files:
        st.info("No matching files found.")
        return

    # Group by folder
    by_folder: dict[str, list[Path]] = {}
    for p in files:
        folder = str(p.parent.relative_to(VAULT_DIR))
        by_folder.setdefault(folder, []).append(p)

    for folder, items in by_folder.items():
        with st.expander(folder if folder != "." else "vault/ (root)", expanded=(query.strip() != "")):
            for i, p in enumerate(items):
                rel = p.relative_to(APP_ROOT)
                mime, _ = mimetypes.guess_type(str(p))
                st.download_button(
                    label=f"⬇️ {p.name}",
                    data=p.read_bytes(),
                    file_name=p.name,
                    mime=mime or "application/octet-stream",
                    use_container_width=True,
                    key=f"vault_dl_{folder}_{p.name}_{i}",
                )
                st.caption(f"{rel}")


def bucket_steps(title: str, steps: list[tuple[str, str]], expanded_first: bool = True):
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown(f"### {title}")
    for idx, (step_title, step_body) in enumerate(steps, start=1):
        with st.expander(f"Step {idx}: {step_title}", expanded=(expanded_first and idx == 1)):
            st.markdown(step_body)
    st.markdown("</div>", unsafe_allow_html=True)


# =============================
# Render shell
# =============================
header()
page = st.session_state.page
nav_sidebar(page)


# =============================
# Pages
# =============================
if page == "home":
    st.markdown("## Choose the claim bucket")
    badge("5 Buckets", "accent")
    st.caption("Start here. Use the search if you already know what you’re looking for.")

    search = st.text_input("Search buckets", placeholder="Type: denied, components, slopes, full…", key="bucket_search").strip().lower()

    buckets = [
        ("🟥", "Denied", "Carrier said no. Force a second look (or end it fast).", "bucket_denied"),
        ("🟧", "Components Only", "They paid parts (vents/flashings/valley) but not shingles.", "bucket_components"),
        ("🟨", "Shingle Repairs", "Spot repairs approved. Prove repairability & CAR, then expand.", "bucket_shingles"),
        ("🟦", "Slope Approval", "Some slopes paid, others denied. Win with connections & continuity.", "bucket_slopes"),
        ("🟩", "Full Roof Approval", "Claim won. Validate scope, prevent surprises, set expectations.", "bucket_full"),
    ]

    if search:
        buckets = [b for b in buckets if search in (b[1] + " " + b[2]).lower()]

    c1, c2 = st.columns(2)

    # render as grid
    for i, (emoji, name, desc, key) in enumerate(buckets):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {emoji} {name}")
            st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
            st.button("Open ➜", use_container_width=True, on_click=go, args=(key,), key=f"open_{key}")
            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")

    st.markdown(
        '<div class="callout"><strong>Rule:</strong> Identify the bucket first → follow the steps in order (no free-styling).</div>',
        unsafe_allow_html=True,
    )

    bottom_nav("home")

elif page == "vault":
    vault_browser()
    bottom_nav("vault")

elif page == "training":
    block(
        "Training",
        "This is where your quick modules live.",
        "Next step: we can convert each bucket into a checklist + photo examples + “what to say” scripts.",
    )

    with st.expander("Suggested upgrades (fast wins)", expanded=True):
        st.markdown(
            "- Add a 1–2 minute checklist per bucket\n"
            "- Add ‘common mistakes’ per bucket (you already started)\n"
            "- Add a quick ‘homeowner language’ script\n"
            "- Add example photo packs in Vault and link them here"
        )

    bottom_nav("training")

elif page == "bucket_denied":
    st.markdown("## Denied Claim")
    badge("Denied", "danger")
    st.button("← Back to Buckets", on_click=go, args=("home",), key="back_denied")

    block(
        "You’re in this bucket if…",
        "- The carrier denied the roof\n- No roof scope was approved\n- Collateral may or may not have been paid",
        "<strong>Mindset:</strong> Denial ≠ dead claim. This is evidence + homeowner-driven.",
    )

    block(
        "Your goal",
        "**Get the carrier to take a second look** — or determine early the claim is not viable.\n\n"
        "**Success exit:**\n- ✔ Reinspection scheduled OR desk/supervisor review confirmed → move to the new bucket the carrier creates."
    )

    bucket_steps(
        "Step-by-step road map",
        [
            ("Identify the denial reason", "- Cause denial\n- Date of loss denial\n- Mixed denial"),
            ("Pick the correct leverage", "- **Cause** → Damage ID + strong photo reports\n- **Date** → weather history + clean homeowner timeline\n- **Mixed** → simplify the story and remove noise"),
            ("Align the homeowner", "- Explain denial in plain language\n- Set expectations (not guaranteed)\n- Give the homeowner the words + attachments"),
            ("Ask for the right next step", "- Reinspection\n- Supervisor review\n- Desk review with new evidence"),
        ],
    )

    st.markdown('<div class="callout"><strong>Common mistakes:</strong> Don’t argue matching. Don’t ask full roof first. Don’t fight the carrier for the homeowner.</div>', unsafe_allow_html=True)

    docs_section([
        ("Direct Physical Damage Argument (DOCX)", "vault/Claim Success/Direct Physical Damage Argument.docx"),
        ("Engineer Testing Repairability (PDF)", "vault/Claim Success/Engineer Testing Repairability.pdf"),
        ("DMI Initial Response (DOCX)", "vault/Claim Success/DMI Initial Response.docx"),
        ("DMI Follow-Up Response (DOCX)", "vault/Claim Success/DMI Follow UP Response.docx"),
        ("IRC Outline (Reference) (PDF)", "vault/Claim Success/IRC Outline.pdf"),
    ])

    bottom_nav("home")

elif page == "bucket_components":
    st.markdown("## Components Only")
    badge("Components Only", "warning")
    st.button("← Back to Buckets", on_click=go, args=("home",), key="back_components")

    st.markdown('<div class="callout"><strong>Core Rule:</strong> If a component is approved, shingles are always impacted.</div>', unsafe_allow_html=True)

    block(
        "You’re in this bucket if…",
        "- The carrier approved one or more roof components\n"
        "- No roofing material is included in the scope\n"
        "- The approved work cannot be completed without disturbing shingles"
    )

    st.markdown("### Component groups")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🌀 Vents", use_container_width=True, on_click=go, args=("comp_vents",), key="open_comp_vents")
    with c2:
        st.button("🧱 Flashings", use_container_width=True, on_click=go, args=("comp_flashings",), key="open_comp_flashings")
    with c3:
        st.button("💧 Valleys", use_container_width=True, on_click=go, args=("comp_valleys",), key="open_comp_valleys")

    block(
        "The question that drives every components claim",
        "",
        "“How are we expected to remove and replace this component without affecting the surrounding roofing material?”",
    )

    block(
        "Next Step Logic",
        "- If roofing material is added → move to **Shingle Repairs**\n"
        "- If repairs are not reasonable → escalate toward **Slope Approval**\n"
        "- If scope direction is unclear → request written clarification or reinspection"
    )

    bottom_nav("home")

elif page == "bucket_shingles":
    st.markdown("## Shingle Repairs")
    badge("Shingles", "accent")
    st.button("← Back to Buckets", on_click=go, args=("home",), key="back_shingles")

    block(
        "You’re in this bucket if…",
        "- Specific shingle counts were approved\n- Spot repairs only\n- No full slopes approved",
        "<strong>Mindset:</strong> Repairability + CAR drive the outcome now.",
    )

    block(
        "Your goal",
        "**Determine if repairs are reasonable** — and move to slopes if they’re not.\n\n"
        "**Success exit:**\n- ✔ Full slope(s) approved → move to **Slope Approval**."
    )

    bucket_steps(
        "Step-by-step road map",
        [
            ("Validate the scope", "- Are counts and locations accurate?\n- Was damage missed?"),
            ("Test repairability", "- Lift shingles and evaluate seal integrity\n- Document cracking/tearing/mat damage\n- If repairs cause damage → repairs aren’t reasonable"),
            ("Evaluate matching & availability (CAR)", "- Same product available? Same size/profile? Acceptable appearance?\n- Document visual tests with photos"),
            ("Expand using repair areas", "- One repair affects multiple shingles\n- Repairs overlap and naturally expand to slopes"),
        ],
    )

    st.markdown('<div class="callout"><strong>Common mistakes:</strong> Don’t skip repair testing. Don’t skip visual match photos. Don’t ask full roof before slopes.</div>', unsafe_allow_html=True)

    docs_section([
        ("Engineer Testing Repairability (PDF)", "vault/Claim Success/Engineer Testing Repairability.pdf"),
        ("Definitions of Reasonable and Uniform (DOCX)", "vault/Claim Success/Definitions of Reasonable and Uniform.docx"),
        ("Uniform Appearance and Compatibility (DOCX)", "vault/Claim Success/Uniform Appearance and Compability.docx"),
        ("Repair Area Concept (PDF)", "vault/Claim Success/Repair Area Concept.pdf"),
    ])

    bottom_nav("home")

elif page == "bucket_slopes":
    st.markdown("## Slope Approval")
    badge("Slopes", "accent")
    st.button("← Back to Buckets", on_click=go, args=("home",), key="back_slopes")

    block(
        "You’re in this bucket if…",
        "- One or more slopes are approved\n- Other slopes are denied",
        "<strong>Mindset:</strong> Slopes are connected systems — hips/valleys/ridges force continuity.",
    )

    block(
        "Your goal",
        "**Expand partial approval to all connected slopes.**\n\n"
        "**Success exit:**\n- ✔ All slopes approved → move to **Full Roof Approval**."
    )

    bucket_steps(
        "Step-by-step road map",
        [
            ("Identify slope connections", "- Hips, ridges, valleys, continuous runs"),
            ("Show construction reality", "- Underlayment overlaps\n- Valley linings\n- Assembly continuity"),
            ("Define slope-level repair areas", "- Removing one slope disturbs another\n- Proper installation requires continuity"),
        ],
    )

    st.markdown('<div class="callout"><strong>Common mistakes:</strong> Don’t treat slopes independently. Don’t skip underlayment continuity. Don’t skip construction photos.</div>', unsafe_allow_html=True)

    docs_section([
        ("Hip and Ridge Overlap (PDF)", "vault/Claim Success/Hip and Ridge Overlap.pdf"),
        ("Repair Area Concept (PDF)", "vault/Claim Success/Repair Area Concept.pdf"),
        ("Mixing Manufacturer (PDF)", "vault/Claim Success/Mixing Manufacture (6).pdf"),
        ("OC Berkshire Discontinued (PDF)", "vault/Claim Success/OC Berkshire Disco.pdf"),
        ("Owens Corning Oakridge Compatibility Letter (PDF)", "vault/Claim Success/owens_corning_oakridge_compatibility_letter.pdf"),
        ("GAF Timberline Do Not Mix (PDF)", "vault/Claim Success/GAF Timberline Do not mix.185217.pdf"),
    ])

    bottom_nav("home")

elif page == "bucket_full":
    st.markdown("## Full Roof Approval")
    badge("Full", "success")
    st.button("← Back to Buckets", on_click=go, args=("home",), key="back_full")

    block(
        "You’re in this bucket if…",
        "- Full roof replacement is approved (or effectively all slopes).",
        "<strong>Mindset:</strong> Protect margin and homeowner experience by preventing surprises.",
    )

    block(
        "Your goal",
        "**Finish clean. Protect margin. Avoid surprises.**\n\n"
        "**Final success:**\n- ✔ Roof built\n- ✔ Claim closed\n- ✔ Homeowner confident"
    )

    bucket_steps(
        "Step-by-step road map",
        [
            ("Validate the scope", "- Accessories, waste, flashings, ventilation, underlayment, valleys"),
            ("Prevent production issues", "- No missing line items\n- No field surprises\n- No last-minute supplements"),
            ("Set homeowner expectations", "- Timeline\n- Mortgage process\n- Supplements vs change orders"),
        ],
    )

    st.markdown('<div class="callout"><strong>Common mistakes:</strong> Assuming scope is complete. Poor handoff to production. Not preparing the homeowner.</div>', unsafe_allow_html=True)

    docs_section([
        ("Do Not Mix AR & Non-AR (PDF)", "vault/Claim Success/Do Not Mix AR & Non-AR.pdf"),
    ])

    bottom_nav("home")

elif page == "comp_vents":
    st.markdown("## Components Playbook — Vents")
    badge("Vents", "warning")
    st.button("← Back to Components", on_click=go, args=("bucket_components",), key="back_comp_vents")

    block("Scenario", "Carrier approved box vents and/or pipe jacks only. No slope or full replacement approved.")
    block(
        "Adjuster Position (Carrier Logic)",
        "“The vents are damaged and have been approved for replacement. The surrounding roofing material is not damaged and does not require replacement.”\n\n"
        "**Adjuster’s core assumptions**\n- Vents are viewed as individual accessories\n- Replacement is assumed localized\n- Surrounding roofing material is reusable\n- Scope is limited to the visible damaged component"
    )
    block(
        "Supplementer Position (Roofing Reality)",
        "“Roof vents are not surface-mounted accessories. They are fastened through and sealed within the roofing system and cannot be removed or replaced independently of the surrounding roofing material.”"
    )
    block(
        "Carrier-Safe Core Argument",
        "",
        "To remove and replace the approved vent components, the roofing material tied into the vents must be lifted or removed to access fasteners and integrate the new components. Once disturbed, this material cannot be reused without compromising seal integrity.",
    )
    bottom_nav("home")

elif page == "comp_flashings":
    st.markdown("## Components Playbook — Flashings")
    badge("Flashings", "warning")
    st.button("← Back to Components", on_click=go, args=("bucket_components",), key="back_comp_flashings")

    block("Scenario", "Carrier approved flashing replacement only (step flashing and/or chimney flashing). No slope or full replacement approved.")
    block(
        "Adjuster Position (Carrier Logic)",
        "“The flashing is damaged and have been approved for replacement. The surrounding roofing material is not damaged and does not require replacement.”\n\n"
        "**Adjuster’s core assumptions**\n- Flashing is viewed stand-alone\n- Damage is isolated to metal\n- Roofing outside area is undamaged\n- Replacement can be completed without expanding scope"
    )
    block(
        "Carrier-Safe Core Argument",
        "",
        "To remove and replace the approved flashing components, the roofing material integrated with the flashing must be removed to access fasteners and install properly. Once disturbed, it cannot be reused without compromising system performance.",
    )
    bottom_nav("home")

elif page == "comp_valleys":
    st.markdown("## Components Playbook — Valleys")
    badge("Valleys", "warning")
    st.button("← Back to Components", on_click=go, args=("bucket_components",), key="back_comp_valleys")

    block("Scenario", "Carrier approved valley work only. No slope or full replacement approved.")
    block(
        "Adjuster Position (How the IC Thinks)",
        "“The damage appears isolated to the valley area. We’ve approved valley repair/replacement. The surrounding roofing material is not damaged and does not require replacement.”\n\n"
        "**Adjuster’s core assumptions**\n- Valley is viewed as a defined area, not a system\n- Roofing outside the valley is undamaged\n- Repair can be made without affecting adjacent roofing\n- Cost containment: limit scope to approved component only"
    )
    block(
        "Carrier-Safe Core Argument",
        "",
        "In order to complete the approved valley work correctly, the roofing material tied into the valley must be removed continuously. Once removed, it cannot be reused without compromising system integrity. The scope must reflect how the work is actually performed.",
    )
    bottom_nav("home")

else:
    st.error("Unknown page. Returning home.")
    st.session_state.page = "home"
    st.rerun()
