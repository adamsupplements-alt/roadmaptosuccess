import os
from pathlib import Path

import streamlit as st

# -----------------------------
# Config
# -----------------------------
st.set_page_config(
    page_title="LQR Road Map to SUCCESS",
    page_icon="🏠",
    layout="centered",
)

# -----------------------------
# Branding (tweak if needed)
# -----------------------------
BRAND = {
    "accent": "#036BDA",        # LQR blue (from logo)
    "accent_strong": "#125DAD", # deeper blue
    "bg_1": "#050814",
    "bg_2": "#0B1226",
    "text": "#F9FAFB",
    "muted": "#9CA3AF",
    "border": "rgba(31,41,55,.95)",
}

APP_ROOT = Path(__file__).parent
ASSETS_DIR = APP_ROOT / "assets"
VAULT_DIR = APP_ROOT / "vault"

LOGO_PATH = ASSETS_DIR / "lqr_logo.png"

# -----------------------------
# Global styling
# -----------------------------
st.markdown(
    f"""
<style>
    .stApp {{
        background: radial-gradient(circle at top, {BRAND["bg_2"]} 0%, {BRAND["bg_1"]} 65%);
        color: {BRAND["text"]};
    }}
    header[data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    [data-testid="stSidebar"] {{
        background: rgba(2,6,23,.92);
        border-right: 1px solid {BRAND["border"]};
    }}

    .lqr-header {{
        display:flex;
        align-items:center;
        justify-content:space-between;
        gap:16px;
        padding: 14px 14px 10px;
        border: 1px solid rgba(15,23,42,.85);
        background: linear-gradient(135deg, rgba(15,23,42,.96), rgba(15,23,42,.80));
        border-radius: 18px;
        box-shadow: 0 12px 26px rgba(15,23,42,.85);
        margin-bottom: 14px;
    }}
    .lqr-left {{
        display:flex;
        align-items:center;
        gap:12px;
        min-width: 0;
    }}
    .lqr-title {{
        margin:0;
        font-size: 1.05rem;
        letter-spacing: .03em;
        text-transform: uppercase;
        line-height: 1.2;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    .lqr-title span {{
        color: {BRAND["accent"]};
        font-weight: 800;
    }}
    .lqr-sub {{
        margin: 2px 0 0;
        color: {BRAND["muted"]};
        font-size: .85rem;
    }}
    .pill {{
        border-radius: 999px;
        padding: .30rem .70rem;
        border: 1px solid rgba(3,107,218,.35);
        background: radial-gradient(circle at top left, rgba(3,107,218,.20), rgba(15,23,42,.95));
        font-size: .72rem;
        text-transform: uppercase;
        letter-spacing: .09em;
        display:inline-flex;
        align-items:center;
        gap:.4rem;
        white-space: nowrap;
        color: #e0f2fe;
    }}
    .dot {{
        width: 7px;
        height: 7px;
        border-radius: 999px;
        background: #4ade80;
        box-shadow: 0 0 0 6px rgba(34,197,94,.24);
        display:inline-block;
    }}

    .card {{
        border: 1px solid rgba(15,23,42,.95);
        background: radial-gradient(circle at top left, rgba(15,23,42,.35), rgba(2,6,23,.96));
        border-radius: 18px;
        padding: 14px 14px 12px;
        box-shadow: 0 12px 30px rgba(15,23,42,.85);
        transition: transform .12s ease-out, border-color .12s ease-out;
    }}
    .card:hover {{
        transform: translateY(-2px);
        border-color: rgba(3,107,218,.45);
    }}
    .card-title {{
        font-size: .98rem;
        font-weight: 800;
        margin: 0 0 6px;
    }}
    .muted {{
        color: {BRAND["muted"]};
        font-size: .9rem;
        margin: 0;
    }}
    .badge {{
        display:inline-block;
        border-radius: 999px;
        padding: .18rem .55rem;
        font-size: .70rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        border: 1px solid rgba(75,85,99,.9);
        color: {BRAND["muted"]};
        white-space: nowrap;
    }}
    .badge.accent {{ border-color: rgba(3,107,218,.9); color: {BRAND["accent"]}; }}
    .badge.success {{ border-color: rgba(74,222,128,.9); color: #86efac; }}
    .badge.warning {{ border-color: rgba(245,158,11,.9); color: #fbbf24; }}
    .badge.danger  {{ border-color: rgba(249,115,115,.9); color: #fca5a5; }}

    .block {{
        border: 1px solid rgba(15,23,42,.95);
        background: linear-gradient(145deg, rgba(15,23,42,.92), rgba(15,23,42,.80));
        border-radius: 18px;
        padding: 14px 14px 10px;
        box-shadow: 0 12px 26px rgba(15,23,42,.90);
        margin-bottom: 12px;
    }}
    .callout {{
        border-radius: 12px;
        border: 1px dashed rgba(3,107,218,.65);
        background: rgba(3,107,218,.10);
        padding: 10px 12px;
        color: #dbeafe;
        font-size: .92rem;
        margin-top: 8px;
    }}
    .backlink {{
        color: {BRAND["muted"]};
        font-size: .9rem;
        text-decoration: none;
        cursor: pointer;
    }}
    .backlink:hover {{ color: {BRAND["accent"]}; }}

    /* Buttons (Streamlit) */
    div.stButton > button {{
        border-radius: 999px !important;
        border: 1px solid rgba(51,65,85,.9) !important;
        background: rgba(15,23,42,.98) !important;
        color: {BRAND["text"]} !important;
    }}
    div.stButton > button:hover {{
        border-color: rgba(3,107,218,.85) !important;
    }}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Navigation state
# -----------------------------
PAGES = {
    "home": "Buckets",
    "vault": "Vault",
    "training": "Training",
    # Buckets
    "bucket_denied": "Denied",
    "bucket_components": "Components Only",
    "bucket_shingles": "Shingle Repairs",
    "bucket_slopes": "Slope Approval",
    "bucket_full": "Full Roof Approval",
    # Component playbooks
    "comp_vents": "Components • Vents",
    "comp_flashings": "Components • Flashings",
    "comp_valleys": "Components • Valleys",
}

if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page_key: str):
    st.session_state.page = page_key
    st.rerun()

# -----------------------------
# Helpers
# -----------------------------
def header():
    col_left, col_right = st.columns([0.78, 0.22], vertical_alignment="center")

    with col_left:
        st.markdown('<div class="lqr-header"><div class="lqr-left">', unsafe_allow_html=True)
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), width=120)
        st.markdown(
            """
            <div style="min-width:0">
              <h1 class="lqr-title">LQR <span>Road Map to SUCCESS</span></h1>
              <p class="lqr-sub">Pick the bucket. Follow the steps. Win the claim.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown(
            '<div class="pill"><span class="dot"></span><span>Bucket Picker</span></div>',
            unsafe_allow_html=True,
        )

def bottom_nav(active_key: str):
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🧺 Buckets", use_container_width=True, disabled=(active_key == "home"), on_click=go, args=("home",))
    with c2:
        st.button("🔎 Vault", use_container_width=True, disabled=(active_key == "vault"), on_click=go, args=("vault",))
    with c3:
        st.button("📚 Training", use_container_width=True, disabled=(active_key == "training"), on_click=go, args=("training",))

def badge(text: str, kind: str = "accent"):
    st.markdown(f'<span class="badge {kind}">{text}</span>', unsafe_allow_html=True)

def block(title: str, body_md: str = "", callout_md: str | None = None):
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown(f"### {title}")
    if body_md:
        st.markdown(body_md)
    if callout_md:
        st.markdown(f'<div class="callout">{callout_md}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def docs_section(doc_items: list[tuple[str, str]]):
    """
    doc_items: [(label, relative_path_from_repo_root)]
    Example: ("Engineer Testing Repairability (PDF)", "vault/Claim Success/Engineer Testing Repairability.pdf")
    """
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("### Recommended Docs")
    st.caption("If a file isn’t present in the repo under /vault, you’ll see “Not found.”")
    for label, rel_path in doc_items:
        file_path = APP_ROOT / rel_path
        if file_path.exists() and file_path.is_file():
            data = file_path.read_bytes()
            st.download_button(
                label=f"⬇️ {label}",
                data=data,
                file_name=file_path.name,
                mime="application/octet-stream",
                use_container_width=True,
            )
        else:
            st.warning(f"Not found: {rel_path}")
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Page content
# -----------------------------
header()

page = st.session_state.page

# Top quick nav (optional)
with st.sidebar:
    st.markdown("## Navigation")
    st.radio(
        "Go to",
        options=list(PAGES.keys()),
        format_func=lambda k: PAGES[k],
        index=list(PAGES.keys()).index(page) if page in PAGES else 0,
        key="sidebar_nav",
        on_change=lambda: go(st.session_state.sidebar_nav),
    )
    st.markdown("---")
    st.caption("Tip: Keep your vault file/folder names EXACT (case-sensitive).")

# HOME
if page == "home":
    st.markdown("## Choose the claim bucket")
    badge("5 Buckets", "accent")
    st.write("")
    st.caption("Start here. If you need docs or visuals, use the bottom navigation (Vault / Training).")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🟥 Denied")
        st.markdown('<p class="muted">Carrier said no. Force a second look (or end it fast).</p>', unsafe_allow_html=True)
        st.button("Open ➜", use_container_width=True, on_click=go, args=("bucket_denied",))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card" style="margin-top:12px;">', unsafe_allow_html=True)
        st.markdown("### 🟨 Shingle Repairs")
        st.markdown('<p class="muted">Spot repairs approved. Prove repairability & CAR, then expand.</p>', unsafe_allow_html=True)
        st.button("Open ➜", use_container_width=True, on_click=go, args=("bucket_shingles",))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card" style="margin-top:12px;">', unsafe_allow_html=True)
        st.markdown("### 🟩 Full Roof Approval")
        st.markdown('<p class="muted">Claim won. Validate scope, prevent surprises, set expectations.</p>', unsafe_allow_html=True)
        st.button("Open ➜", use_container_width=True, on_click=go, args=("bucket_full",))
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🟧 Components Only")
        st.markdown('<p class="muted">They paid parts (vents/flashings/valley) but not shingles.</p>', unsafe_allow_html=True)
        st.button("Open ➜", use_container_width=True, on_click=go, args=("bucket_components",))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card" style="margin-top:12px;">', unsafe_allow_html=True)
        st.markdown("### 🟦 Slope Approval")
        st.markdown('<p class="muted">Some slopes paid, others denied. Win with connections & continuity.</p>', unsafe_allow_html=True)
        st.button("Open ➜", use_container_width=True, on_click=go, args=("bucket_slopes",))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="callout"><strong>Rule:</strong> Identify the bucket first. Then follow the steps in order. No free-styling.</div>', unsafe_allow_html=True)
    bottom_nav("home")

# VAULT
elif page == "vault":
    st.markdown("## Vault")
    badge("Vault", "accent")
    block(
        "What this is",
        "This page is a holder for documents and reference material.",
        "Next step: we can auto-list whatever is inside your `vault/` folder and make it searchable.",
    )
    bottom_nav("vault")

# TRAINING
elif page == "training":
    st.markdown("## Training")
    badge("Training", "accent")
    block(
        "What this is",
        "This page is a holder for training modules and playbooks.",
        "Next step: we can turn each bucket into a short “module” with checklists + examples.",
    )
    bottom_nav("training")

# BUCKET 1 — DENIED
elif page == "bucket_denied":
    st.markdown("## Denied Claim")
    badge("Denied", "danger")
    st.markdown('<a class="backlink" onclick="return false;">←</a>', unsafe_allow_html=True)
    if st.button("← Back to Buckets"):
        go("home")

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

    block(
        "Step-by-step road map",
        "**Step 1: Identify why it was denied**\n- Cause denial\n- Date of loss denial\n- Mixed denial\n\n"
        "**Step 2: Pick the correct leverage**\n- **Cause** → Damage ID + strong photo reports\n- **Date** → weather history + clean homeowner timeline\n- **Mixed** → simplify the story and remove noise\n\n"
        "**Step 3: Align the homeowner**\n- Explain denial in plain language\n- Set expectations (not guaranteed)\n- Give the homeowner the words + attachments\n\n"
        "**Step 4: Ask for the right next step**\n- Reinspection\n- Supervisor review\n- Desk review with new evidence",
        "<strong>Common mistakes:</strong> Don’t argue matching. Don’t ask full roof first. Don’t fight the carrier for the homeowner.",
    )

    docs_section([
        ("Direct Physical Damage Argument (DOCX)", "vault/Claim Success/Direct Physical Damage Argument.docx"),
        ("Engineer Testing Repairability (PDF)", "vault/Claim Success/Engineer Testing Repairability.pdf"),
        ("DMI Initial Response (DOCX)", "vault/Claim Success/DMI Initial Response.docx"),
        ("DMI Follow-Up Response (DOCX)", "vault/Claim Success/DMI Follow UP Response.docx"),
        ("IRC Outline (Reference) (PDF)", "vault/Claim Success/IRC Outline.pdf"),
    ])

    bottom_nav("home")

# BUCKET 2 — COMPONENTS ONLY
elif page == "bucket_components":
    st.markdown("## Bucket 2 — Components Only")
    badge("Components Only", "warning")
    if st.button("← Back to Buckets"):
        go("home")

    st.markdown('<div class="callout"><strong>Core Rule:</strong> If a component is approved, shingles are always impacted.</div>', unsafe_allow_html=True)

    block(
        "You’re in this bucket if…",
        "- The carrier approved one or more roof components\n"
        "- No roofing material is included in the scope\n"
        "- The approved work cannot be completed without disturbing shingles"
    )

    st.markdown("### Component Groups (Tap to open)")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🌀 Vents ➜", use_container_width=True, on_click=go, args=("comp_vents",))
    with c2:
        st.button("🧱 Flashings ➜", use_container_width=True, on_click=go, args=("comp_flashings",))
    with c3:
        st.button("💧 Valleys ➜", use_container_width=True, on_click=go, args=("comp_valleys",))

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

# BUCKET 3 — SHINGLES
elif page == "bucket_shingles":
    st.markdown("## Shingle Repairs")
    badge("Shingles", "accent")
    if st.button("← Back to Buckets"):
        go("home")

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

    block(
        "Step-by-step road map",
        "**Step 1: Validate the scope**\n- Are counts and locations accurate?\n- Was damage missed?\n\n"
        "**Step 2: Test repairability**\n- Lift shingles and evaluate seal integrity\n- Document cracking/tearing/mat damage\n- If repairs cause damage → repairs aren’t reasonable\n\n"
        "**Step 3: Evaluate matching & availability (CAR)**\n- Same product available? Same size/profile? Acceptable appearance?\n- Document visual tests with photos\n\n"
        "**Step 4: Expand using repair areas**\n- One repair affects multiple shingles\n- Repairs overlap and naturally expand to slopes",
        "<strong>Common mistakes:</strong> Don’t skip repair testing. Don’t skip visual match photos. Don’t ask full roof before slopes.",
    )

    docs_section([
        ("Engineer Testing Repairability (PDF)", "vault/Claim Success/Engineer Testing Repairability.pdf"),
        ("Definitions of Reasonable and Uniform (DOCX)", "vault/Claim Success/Definitions of Reasonable and Uniform.docx"),
        ("Uniform Appearance and Compatibility (DOCX)", "vault/Claim Success/Uniform Appearance and Compability.docx"),
        ("Repair Area Concept (PDF)", "vault/Claim Success/Repair Area Concept.pdf"),
    ])

    bottom_nav("home")

# BUCKET 4 — SLOPES
elif page == "bucket_slopes":
    st.markdown("## Slope Approval")
    badge("Slopes", "accent")
    if st.button("← Back to Buckets"):
        go("home")

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

    block(
        "Step-by-step road map",
        "**Step 1: Identify slope connections**\n- Hips, ridges, valleys, continuous runs\n\n"
        "**Step 2: Show construction reality**\n- Underlayment overlaps\n- Valley linings\n- Assembly continuity\n\n"
        "**Step 3: Define slope-level repair areas**\n- Removing one slope disturbs another\n- Proper installation requires continuity",
        "<strong>Common mistakes:</strong> Don’t treat slopes independently. Don’t skip underlayment continuity. Don’t skip construction photos.",
    )

    docs_section([
        ("Hip and Ridge Overlap (PDF)", "vault/Claim Success/Hip and Ridge Overlap.pdf"),
        ("Repair Area Concept (PDF)", "vault/Claim Success/Repair Area Concept.pdf"),
        ("Mixing Manufacturer (PDF)", "vault/Claim Success/Mixing Manufacture (6).pdf"),
        ("OC Berkshire Discontinued (PDF)", "vault/Claim Success/OC Berkshire Disco.pdf"),
        ("Owens Corning Oakridge Compatibility Letter (PDF)", "vault/Claim Success/owens_corning_oakridge_compatibility_letter.pdf"),
        ("GAF Timberline Do Not Mix (PDF)", "vault/Claim Success/GAF Timberline Do not mix.185217.pdf"),
    ])

    bottom_nav("home")

# BUCKET 5 — FULL
elif page == "bucket_full":
    st.markdown("## Full Roof Approval")
    badge("Full", "success")
    if st.button("← Back to Buckets"):
        go("home")

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

    block(
        "Step-by-step road map",
        "**Step 1: Validate the scope**\n- Accessories, waste, flashings, ventilation, underlayment, valleys\n\n"
        "**Step 2: Prevent production issues**\n- No missing line items\n- No field surprises\n- No last-minute supplements\n\n"
        "**Step 3: Set homeowner expectations**\n- Timeline\n- Mortgage process\n- Supplements vs change orders",
        "<strong>Common mistakes:</strong> Assuming scope is complete. Poor handoff to production. Not preparing the homeowner.",
    )

    docs_section([
        ("Do Not Mix AR & Non-AR (PDF)", "vault/Claim Success/Do Not Mix AR & Non-AR.pdf"),
    ])

    bottom_nav("home")

# COMPONENTS — VENTS
elif page == "comp_vents":
    st.markdown("## Components Playbook — Vents")
    badge("Vents", "warning")
    if st.button("← Back to Components"):
        go("bucket_components")

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

# COMPONENTS — FLASHINGS
elif page == "comp_flashings":
    st.markdown("## Components Playbook — Flashings")
    badge("Flashings", "warning")
    if st.button("← Back to Components"):
        go("bucket_components")

    block("Scenario", "Carrier approved flashing replacement only (step flashing and/or chimney flashing). No slope or full replacement approved.")
    block(
        "Adjuster Position (Carrier Logic)",
        "“The flashing is damaged and has been approved for replacement. The surrounding roofing material is not damaged and does not require replacement.”\n\n"
        "**Adjuster’s core assumptions**\n- Flashing is viewed stand-alone\n- Damage is isolated to metal\n- Roofing outside area is undamaged\n- Replacement can be completed without expanding scope"
    )
    block(
        "Carrier-Safe Core Argument",
        "",
        "To remove and replace the approved flashing components, the roofing material integrated with the flashing must be removed to access fasteners and install properly. Once disturbed, it cannot be reused without compromising system performance.",
    )
    bottom_nav("home")

# COMPONENTS — VALLEYS
elif page == "comp_valleys":
    st.markdown("## Components Playbook — Valleys")
    badge("Valleys", "warning")
    if st.button("← Back to Components"):
        go("bucket_components")

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
