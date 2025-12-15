import os
import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="LQR Road Map to SUCCESS",
    page_icon="🧺",
    layout="centered",
)

# -----------------------------
# Styling (Streamlit CSS)
# -----------------------------
CSS = """
<style>
:root{
  --text:#f9fafb;
  --muted:#9ca3af;
  --accent:#38bdf8;
  --danger:#f97373;
  --warning:#f59e0b;
  --success:#4ade80;
  --radius:18px;
  --border:rgba(31,41,55,.95);
}
html, body, [class*="stApp"]{
  background: radial-gradient(circle at top,#111827 0,#020617 55%) !important;
  color: var(--text) !important;
}
.block {
  background: linear-gradient(145deg, rgba(15,23,42,.92), rgba(15,23,42,.8));
  border-radius: var(--radius);
  padding: .85rem .9rem;
  border: 1px solid rgba(15,23,42,.95);
  box-shadow: 0 12px 26px rgba(15,23,42,.9);
  margin-bottom: .8rem;
}
.badge {
  border-radius: 999px;
  padding: .15rem .5rem;
  font-size: .72rem;
  text-transform: uppercase;
  letter-spacing: .08em;
  border: 1px solid rgba(75,85,99,.9);
  color: var(--muted);
  white-space: nowrap;
}
.badge.danger { border-color: rgba(249,115,115,.9); color: var(--danger); }
.badge.warning{ border-color: rgba(245,158,11,.9);  color: var(--warning); }
.badge.accent { border-color: rgba(56,189,248,.9);  color: var(--accent); }
.badge.success{ border-color: rgba(74,222,128,.9);  color: var(--success); }

.hdr {
  padding: 1rem 1.25rem .75rem;
  border-bottom: 1px solid rgba(15,23,42,.75);
  background: linear-gradient(135deg, rgba(15,23,42,.96), rgba(15,23,42,.85));
  border-radius: 16px;
}
.subtitle { margin-top: .2rem; color: var(--muted); font-size: .9rem; }
.pill{
  border-radius:999px;
  padding:.32rem .8rem;
  border:1px solid rgba(56,189,248,.3);
  background:radial-gradient(circle at top left,rgba(56,189,248,.25),rgba(15,23,42,.95));
  font-size:.72rem;
  text-transform:uppercase;
  letter-spacing:.09em;
  display:inline-flex;
  align-items:center;
  gap:.45rem;
  white-space:nowrap;
}
.dot{
  width:6px;height:6px;border-radius:999px;
  background:var(--success);
  box-shadow:0 0 0 6px rgba(34,197,94,.28);
}

.card {
  background: radial-gradient(circle at top left, rgba(15,23,42,.35), rgba(2,6,23,.96));
  border-radius: var(--radius);
  border: 1px solid rgba(15,23,42,.95);
  box-shadow: 0 12px 30px rgba(15,23,42,.85);
  padding: .9rem .9rem .75rem;
}
.card-title { font-size: 1.02rem; font-weight: 750; margin: 0; }
.card-body { color: var(--muted); font-size: .9rem; margin-top: .25rem; }
.card-footer { color: var(--muted); font-size: .8rem; margin-top: .6rem; display:flex; justify-content:space-between; }
.icon{
  width:32px;height:32px;border-radius:999px;
  display:inline-flex;align-items:center;justify-content:center;
  font-size:1.05rem;
  background:radial-gradient(circle at top,rgba(56,189,248,.18),rgba(15,23,42,.92));
  border:1px solid rgba(56,189,248,.4);
  flex-shrink:0;
}
.callout{
  border-radius:12px;
  border:1px dashed rgba(56,189,248,.6);
  background:rgba(56,189,248,.08);
  padding:.55rem .65rem;
  margin-top:.45rem;
  color:#dbeafe;
  font-size:.9rem;
}
.small-muted { color: var(--muted); font-size: .88rem; }
hr { border: none; height: 1px; background: rgba(31,41,55,.95); margin: .8rem 0; }

div[data-testid="stVerticalBlockBorderWrapper"]{
  background: transparent !important;
  border: none !important;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------
# Helpers
# -----------------------------
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.join(REPO_ROOT, "vault")

def set_view(view_id: str):
    st.session_state["view"] = view_id
    st.rerun()

def back_row(back_to: str, badge_text: str, badge_kind: str):
    c1, c2 = st.columns([3, 1])
    with c1:
        if st.button("← Back", key=f"back_{back_to}_{st.session_state.get('view','')}", use_container_width=False):
            set_view(back_to)
    with c2:
        st.markdown(f'<span class="badge {badge_kind}">{badge_text}</span>', unsafe_allow_html=True)

def header():
    left, right = st.columns([4, 1])
    with left:
        st.markdown(
            """
            <div class="hdr">
              <div style="display:flex;justify-content:space-between;gap:.75rem;align-items:flex-start;">
                <div>
                  <div style="font-size:1.15rem;letter-spacing:.03em;text-transform:uppercase;font-weight:800;">
                    LQR <span style="font-weight:600;color:var(--accent)">Road Map to SUCCESS</span>
                  </div>
                  <div class="subtitle">Pick the bucket. Follow the steps. Win the claim.</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown('<div style="display:flex;justify-content:flex-end;margin-top:.35rem;"><span class="pill"><span class="dot"></span>Bucket Picker</span></div>', unsafe_allow_html=True)

def card_button(icon: str, title: str, body: str, footer_left: str, footer_right: str, target_view: str, key: str):
    st.markdown(
        f"""
        <div class="card">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:.6rem;">
            <div style="display:flex;align-items:center;gap:.6rem;">
              <div class="icon">{icon}</div>
              <div class="card-title">{title}</div>
            </div>
          </div>
          <div class="card-body">{body}</div>
          <div class="card-footer"><span><small>{footer_left}</small></span><span>{footer_right}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Click area = a button below the card (Streamlit can't make the whole div clickable without JS)
    if st.button("Open ➜", key=key, use_container_width=True):
        set_view(target_view)

def vault_download(rel_path: str, label: str, key: str):
    """
    rel_path is relative to repo root, e.g.
      "vault/Claim Success/Engineer Testing Repairability.pdf"
    """
    abs_path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.isfile(abs_path):
        st.warning(f"Missing file in repo: {rel_path}")
        return
    with open(abs_path, "rb") as f:
        data = f.read()
    st.download_button(
        label=label,
        data=data,
        file_name=os.path.basename(abs_path),
        key=key,
        use_container_width=True
    )

# -----------------------------
# Init state
# -----------------------------
if "view" not in st.session_state:
    st.session_state["view"] = "home"

# -----------------------------
# Screens
# -----------------------------
def view_home():
    st.markdown("## Choose the claim bucket")
    st.markdown('<span class="badge accent">5 Buckets</span>', unsafe_allow_html=True)
    st.markdown(
        '<div class="small-muted">Start here. If you need docs or visuals, use the bottom navigation (Vault / Training).</div>',
        unsafe_allow_html=True
    )
    st.write("")

    card_button("🟥", "Denied",
        "Carrier said no. Force a second look (or end it fast).",
        "Bucket 1", "Open ➜", "bucket_denied", "open_denied")

    card_button("🟧", "Components Only",
        "They paid parts (vents/flashings/valley) but not shingles.",
        "Bucket 2", "Open ➜", "bucket_components", "open_components")

    card_button("🟨", "Shingle Repairs",
        "Spot repairs approved. Prove repairability & CAR, then expand.",
        "Bucket 3", "Open ➜", "bucket_shingles", "open_shingles")

    card_button("🟦", "Slope Approval",
        "Some slopes paid, others denied. Win with connections & continuity.",
        "Bucket 4", "Open ➜", "bucket_slopes", "open_slopes")

    card_button("🟩", "Full Roof Approval",
        "Claim won. Validate scope, prevent surprises, set expectations.",
        "Bucket 5", "Open ➜", "bucket_full", "open_full")

    st.markdown('<div class="callout"><strong>Rule:</strong> Identify the bucket first. Then follow the steps in order. No free-styling.</div>', unsafe_allow_html=True)

def view_bucket_denied():
    back_row("home", "Denied", "danger")
    st.markdown("## Denied Claim")
    st.markdown('<div class="small-muted">The carrier said no. Don’t guess. Don’t spiral. Follow the steps.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="block">
          <h3>You’re in this bucket if…</h3>
          <ul class="compact">
            <li>The carrier denied the roof.</li>
            <li>No roof scope was approved.</li>
            <li>Collateral may or may not have been paid.</li>
          </ul>
          <div class="callout"><strong>Mindset:</strong> Denial ≠ dead claim. This is evidence + homeowner-driven.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Your goal</h3>
          <div class="small-muted"><strong>Get the carrier to take a second look</strong> — or determine early the claim is not viable.</div>
          <h4>Success exit</h4>
          <div class="small-muted">✔ Reinspection scheduled or desk/supervisor review confirmed → move to the new bucket the carrier creates.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Step-by-step road map</h3>
          <h4>Step 1: Identify why it was denied</h4>
          <ul class="compact"><li>Cause denial</li><li>Date of loss denial</li><li>Mixed denial</li></ul>

          <h4>Step 2: Pick the correct leverage</h4>
          <ul class="compact">
            <li><strong>Cause</strong> → Damage ID + strong photo reports.</li>
            <li><strong>Date</strong> → weather history + clean homeowner timeline.</li>
            <li><strong>Mixed</strong> → simplify the story and remove noise.</li>
          </ul>

          <h4>Step 3: Align the homeowner</h4>
          <ul class="compact"><li>Explain denial in plain language.</li><li>Set expectations (not guaranteed).</li><li>Give the homeowner the words + attachments.</li></ul>

          <h4>Step 4: Ask for the right next step</h4>
          <ul class="compact"><li>Reinspection</li><li>Supervisor review</li><li>Desk review with new evidence</li></ul>

          <div class="callout"><strong>Common mistakes:</strong> Don’t argue matching. Don’t ask full roof first. Don’t fight the carrier for the homeowner.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="block"><h3>Recommended Docs</h3><div class="small-muted">Downloads pull from your repo’s <code>vault/</code> folder.</div></div>', unsafe_allow_html=True)
    vault_download("vault/Claim Success/Direct Physical Damage Argument.docx", "Direct Physical Damage Argument (DOCX)", "dl_denied_1")
    vault_download("vault/Claim Success/Engineer Testing Repairability.pdf", "Engineer Testing Repairability (PDF)", "dl_denied_2")
    vault_download("vault/Claim Success/DMI Initial Response.docx", "DMI Initial Response (DOCX)", "dl_denied_3")
    vault_download("vault/Claim Success/DMI Follow UP Response.docx", "DMI Follow-Up Response (DOCX)", "dl_denied_4")
    vault_download("vault/Claim Success/IRC Outline.pdf", "IRC Outline (Reference) (PDF)", "dl_denied_5")

    st.markdown('<div class="callout"><strong>Tip:</strong> If a file is missing, confirm the exact filename/case in GitHub (Windows vs Linux will bite you).</div>', unsafe_allow_html=True)

def view_bucket_components():
    back_row("home", "Components Only", "warning")
    st.markdown("## Bucket 2 — Components Only")
    st.markdown('<div class="callout"><strong>Core Rule:</strong> If a component is approved, shingles are always impacted.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="block">
          <h3>You’re in this bucket if…</h3>
          <ul class="compact">
            <li>The carrier approved one or more roof components</li>
            <li>No roofing material is included in the scope</li>
            <li>The approved work cannot be completed without disturbing shingles</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="block"><h3>Component Groups (Foundational Concept)</h3><div class="small-muted">Tap a group to open the playbook.</div></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🌀 Vents", use_container_width=True):
            set_view("components_vents")
    with c2:
        if st.button("🧱 Flashings", use_container_width=True):
            set_view("components_flashings")
    with c3:
        if st.button("💧 Valleys", use_container_width=True):
            set_view("components_valleys")

    st.markdown(
        """
        <div class="block">
          <h3>The Question That Drives Every Components Claim</h3>
          <div class="callout">“How are we expected to remove and replace this component without affecting the surrounding roofing material?”</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Next Step Logic</h3>
          <ul class="compact">
            <li>If roofing material is added → Move to <strong>Shingle Repairs</strong></li>
            <li>If repairs are not reasonable → Escalate toward <strong>Slope Approval</strong></li>
            <li>If scope direction is unclear → Request written clarification or reinspection</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

def view_bucket_shingles():
    back_row("home", "Shingles", "accent")
    st.markdown("## Shingle Repairs")
    st.markdown('<div class="small-muted">They admitted roof damage. Now prove whether repairs are reasonable.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="block">
          <h3>You’re in this bucket if…</h3>
          <ul class="compact"><li>Specific shingle counts were approved.</li><li>Spot repairs only.</li><li>No full slopes approved.</li></ul>
          <div class="callout"><strong>Mindset:</strong> Repairability + CAR drive the outcome now.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Your goal</h3>
          <div class="small-muted"><strong>Determine if repairs are reasonable</strong> — and move to slopes if they’re not.</div>
          <h4>Success exit</h4>
          <div class="small-muted">✔ Full slope(s) approved → move to <strong>Slope Approval</strong>.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Step-by-step road map</h3>
          <h4>Step 1: Validate the scope</h4>
          <ul class="compact"><li>Are counts and locations accurate?</li><li>Was damage missed?</li></ul>

          <h4>Step 2: Test repairability</h4>
          <ul class="compact"><li>Lift shingles and evaluate seal integrity.</li><li>Document cracking/tearing/mat damage.</li><li>If repairs cause damage → repairs aren’t reasonable.</li></ul>

          <h4>Step 3: Evaluate matching & availability (CAR)</h4>
          <ul class="compact"><li>Same product available? Same size/profile? Acceptable appearance?</li><li>Document visual tests with photos.</li></ul>

          <h4>Step 4: Expand using repair areas</h4>
          <ul class="compact"><li>One repair affects multiple shingles.</li><li>Repairs overlap and naturally expand to slopes.</li></ul>

          <div class="callout"><strong>Common mistakes:</strong> Don’t skip repair testing. Don’t skip visual match photos. Don’t ask full roof before slopes.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="block"><h3>Recommended Docs</h3></div>', unsafe_allow_html=True)
    vault_download("vault/Claim Success/Engineer Testing Repairability.pdf", "Engineer Testing Repairability (PDF)", "dl_shingles_1")
    vault_download("vault/Claim Success/Definitions of Reasonable and Uniform.docx", "Definitions of Reasonable and Uniform (DOCX)", "dl_shingles_2")
    vault_download("vault/Claim Success/Uniform Appearance and Compability.docx", "Uniform Appearance and Compatibility (DOCX)", "dl_shingles_3")
    vault_download("vault/Claim Success/Repair Area Concept.pdf", "Repair Area Concept (PDF)", "dl_shingles_4")

def view_bucket_slopes():
    back_row("home", "Slopes", "accent")
    st.markdown("## Slope Approval")
    st.markdown('<div class="small-muted">Some slopes are paid. Others are not. Now you win with construction reality.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="block">
          <h3>You’re in this bucket if…</h3>
          <ul class="compact"><li>One or more slopes are approved.</li><li>Other slopes are denied.</li></ul>
          <div class="callout"><strong>Mindset:</strong> Slopes are connected systems — hips/valleys/ridges force continuity.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Your goal</h3>
          <div class="small-muted"><strong>Expand partial approval to all connected slopes.</strong></div>
          <h4>Success exit</h4>
          <div class="small-muted">✔ All slopes approved → move to <strong>Full Roof Approval</strong>.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Step-by-step road map</h3>
          <h4>Step 1: Identify slope connections</h4>
          <ul class="compact"><li>Hips, ridges, valleys, continuous runs.</li></ul>

          <h4>Step 2: Show construction reality</h4>
          <ul class="compact"><li>Underlayment overlaps</li><li>Valley linings</li><li>Vapor retarder / assembly continuity</li></ul>

          <h4>Step 3: Define slope-level repair areas</h4>
          <ul class="compact"><li>Removing one slope disturbs another.</li><li>Proper installation requires continuity.</li></ul>

          <div class="callout"><strong>Common mistakes:</strong> Don’t treat slopes independently. Don’t skip underlayment continuity. Don’t skip construction photos.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="block"><h3>Recommended Docs</h3></div>', unsafe_allow_html=True)
    vault_download("vault/Claim Success/Hip and Ridge Overlap.pdf", "Hip and Ridge Overlap (PDF)", "dl_slopes_1")
    vault_download("vault/Claim Success/Repair Area Concept.pdf", "Repair Area Concept (PDF)", "dl_slopes_2")
    vault_download("vault/Claim Success/Mixing Manufacturer (6).pdf", "Mixing Manufacturer (PDF)", "dl_slopes_3")
    vault_download("vault/Claim Success/OC Berkshire Disco.pdf", "OC Berkshire Discontinued (PDF)", "dl_slopes_4")
    vault_download("vault/Claim Success/owens_corning_oakridge_compatibility_letter.pdf", "Owens Corning Oakridge Compatibility Letter (PDF)", "dl_slopes_5")
    vault_download("vault/Claim Success/GAF Timberline Do not mix.185217.pdf", "GAF Timberline Do Not Mix (PDF)", "dl_slopes_6")

def view_bucket_full():
    back_row("home", "Full", "success")
    st.markdown("## Full Roof Approval")
    st.markdown('<div class="small-muted">The claim is won. Now don’t lose it operationally.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="block">
          <h3>You’re in this bucket if…</h3>
          <ul class="compact"><li>Full roof replacement is approved (or effectively all slopes).</li></ul>
          <div class="callout"><strong>Mindset:</strong> Protect margin and homeowner experience by preventing surprises.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Your goal</h3>
          <div class="small-muted"><strong>Finish clean. Protect margin. Avoid surprises.</strong></div>
          <h4>Final success</h4>
          <div class="small-muted">✔ Roof built ✔ Claim closed ✔ Homeowner confident</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="block">
          <h3>Step-by-step road map</h3>
          <h4>Step 1: Validate the scope</h4>
          <ul class="compact"><li>Accessories, waste, flashings, ventilation, underlayment, valleys.</li></ul>
          <h4>Step 2: Prevent production issues</h4>
          <ul class="compact"><li>No missing line items. No field surprises. No last-minute supplements.</li></ul>
          <h4>Step 3: Set homeowner expectations</h4>
          <ul class="compact"><li>Timeline • Mortgage process • Supplements vs change orders</li></ul>
          <div class="callout"><strong>Common mistakes:</strong> Assuming scope is complete. Poor handoff to production. Not preparing the homeowner.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="block"><h3>Recommended Docs</h3></div>', unsafe_allow_html=True)
    vault_download("vault/Claim Success/Do Not Mix AR & Non-AR.pdf", "Do Not Mix AR & Non-AR (PDF)", "dl_full_1")

def view_vault():
    back_row("home", "Vault", "accent")
    st.markdown("## Vault")
    st.markdown('<div class="small-muted">This screen can become a searchable library. For now, it lists files under <code>vault/</code>.</div>', unsafe_allow_html=True)
    st.write("")

    if not os.path.isdir(VAULT_ROOT):
        st.warning("No /vault folder found in this repo yet.")
        return

    query = st.text_input("Search vault filenames", placeholder="type part of a filename…")
    matches = []
    for root, _, files in os.walk(VAULT_ROOT):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), REPO_ROOT)
            if (not query) or (query.lower() in fn.lower()):
                matches.append(rel)

    if not matches:
        st.info("No matches.")
        return

    for i, rel in enumerate(sorted(matches)[:200]):
        vault_download(rel, f"Download: {os.path.basename(rel)}", key=f"vault_list_{i}")

def view_training():
    back_row("home", "Training", "accent")
    st.markdown("## Training")
    st.markdown('<div class="small-muted">Placeholder screen. Next step is building modules and linking docs/videos.</div>', unsafe_allow_html=True)

def view_components_vents():
    back_row("bucket_components", "Vents", "warning")
    st.markdown("## Components Playbook — Vents")
    st.markdown('<div class="small-muted">Carrier approved box vents and/or pipe jacks only. No slope or full replacement approved.</div>', unsafe_allow_html=True)
    st.markdown('<div class="block"><h3>Carrier-Safe Core Argument</h3><div class="callout">To remove and replace the approved vent components, the roofing material directly tied into the vents must be lifted or removed to access fasteners and integrate the new components. Once disturbed, this material cannot be reused without compromising seal integrity. To complete the approved work properly, the roofing material impacted by the vent replacement must be addressed in the scope.</div></div>', unsafe_allow_html=True)

def view_components_flashings():
    back_row("bucket_components", "Flashings", "warning")
    st.markdown("## Components Playbook — Flashings")
    st.markdown('<div class="small-muted">Carrier approved flashing replacement only (step flashing and/or chimney flashing). No slope or full replacement approved.</div>', unsafe_allow_html=True)
    st.markdown('<div class="block"><h3>Carrier-Safe Core Argument</h3><div class="callout">To remove and replace the approved flashing components, the roofing material integrated with the flashing must be removed to access and properly install the new flashing. Once disturbed, this material cannot be reused without compromising the roof system. To complete the approved work correctly, the roofing material impacted by the flashing replacement must be addressed in the scope.</div></div>', unsafe_allow_html=True)

def view_components_valleys():
    back_row("bucket_components", "Valleys", "warning")
    st.markdown("## Components Playbook — Valleys")
    st.markdown('<div class="small-muted">Carrier approved valley work only. No slope or full replacement approved.</div>', unsafe_allow_html=True)
    st.markdown('<div class="block"><h3>Carrier-Safe Core Argument</h3><div class="callout">In order to complete the approved valley work correctly, the roofing material tied into the valley must be removed continuously. Once removed, it cannot be reused without compromising system integrity. To complete the work as approved and restore a watertight roof system, the roofing material impacted by the valley replacement must be addressed in the scope.</div></div>', unsafe_allow_html=True)

# -----------------------------
# Router
# -----------------------------
header()

ROUTES = {
    "home": view_home,
    "bucket_denied": view_bucket_denied,
    "bucket_components": view_bucket_components,
    "bucket_shingles": view_bucket_shingles,
    "bucket_slopes": view_bucket_slopes,
    "bucket_full": view_bucket_full,
    "vault": view_vault,
    "training": view_training,
    "components_vents": view_components_vents,
    "components_flashings": view_components_flashings,
    "components_valleys": view_components_valleys,
}

view_id = st.session_state.get("view", "home")
ROUTES.get(view_id, view_home)()

st.markdown("---")

# Bottom navigation (Streamlit can't truly "fixed" position without JS; this is the reliable version)
nav1, nav2, nav3 = st.columns(3)
with nav1:
    if st.button("🧺 Buckets", use_container_width=True):
        set_view("home")
with nav2:
    if st.button("🔎 Vault", use_container_width=True):
        set_view("vault")
with nav3:
    if st.button("📚 Training", use_container_width=True):
        set_view("training")
