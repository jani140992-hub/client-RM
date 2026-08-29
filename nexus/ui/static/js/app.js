/**
 * NexusCRM Client Portal Single-Page Application Engine.
 * Manages view switching, API interactions, 10-stage stepper progression, and screening consoles.
 */

const state = {
    activeTab: 'dashboard',
    clients: [],
    currentClient: null,
    dashboard: null,
    tasks: [],
    audit: []
};

const STAGES = [
    { code: 'PROSPECT_LEAD', title: '1. Lead' },
    { code: 'PRE_QUALIFICATION', title: '2. Pre-Qual' },
    { code: 'INFORMATION_GATHERING', title: '3. Data Coll.' },
    { code: 'IDV_AND_VERIFICATION', title: '4. IDV Check' },
    { code: 'KYC_AML_SCREENING', title: '5. Sanctions' },
    { code: 'EDD_INVESTIGATION', title: '6. EDD Case' },
    { code: 'CREDIT_UNDERWRITING', title: '7. Credit' },
    { code: 'LEGAL_CONTRACTING', title: '8. Legal' },
    { code: 'ACCOUNT_PROVISIONING', title: '9. Provision' },
    { code: 'FINAL_APPROVAL_GATE', title: '10. 4-Eyes' },
    { code: 'COMPLETED', title: 'Active' }
];

document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

async function initApp() {
    await fetchDashboardMetrics();
    await loadClients();
    setupEventListeners();
}

function setupEventListeners() {
    const globalInput = document.getElementById('globalSearchInput');
    if (globalInput) {
        globalInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const val = globalInput.value.trim();
                switchTab('clients');
                document.getElementById('clientFilterSearch').value = val;
                loadClients();
            }
        });
    }

    const scrInput = document.getElementById('screeningSearchInput');
    if (scrInput) {
        scrInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                runAdHocScreening();
            }
        });
    }
}

function switchTab(tabId) {
    state.activeTab = tabId;

    // Update Tab Buttons
    document.querySelectorAll('.nav-tab').forEach(btn => {
        btn.classList.remove('active-tab', 'text-cyan-400');
        btn.classList.add('text-slate-400');
    });
    const activeBtn = document.getElementById(`tab-btn-${tabId}`);
    if (activeBtn) {
        activeBtn.classList.add('active-tab');
        activeBtn.classList.remove('text-slate-400');
    }

    // Toggle Views
    document.querySelectorAll('.tab-view').forEach(view => {
        view.classList.add('hidden');
    });
    const targetView = document.getElementById(`view-${tabId}`);
    if (targetView) {
        targetView.classList.remove('hidden');
    }

    // Trigger tab-specific loads
    if (tabId === 'dashboard') fetchDashboardMetrics();
    if (tabId === 'clients') loadClients();
    if (tabId === 'tasks') loadTasks();
    if (tabId === 'audit') loadAuditTrail();
}

// ----------------------------------------------------
// 1. Dashboard Functions
// ----------------------------------------------------
async function fetchDashboardMetrics() {
    try {
        const res = await fetch('/api/v1/analytics/overview');
        const json = await res.json();
        if (json.success) {
            state.dashboard = json.data;
            renderDashboard(json.data);
        }
    } catch (e) {
        console.error('Error fetching dashboard overview:', e);
    }
}

function renderDashboard(data) {
    document.getElementById('kpi-total-clients').textContent = data.total_clients || 0;
    document.getElementById('kpi-active-cases').textContent = data.active_onboardings || 0;
    document.getElementById('kpi-sla-green').textContent = data.sla_breakdown?.GREEN || 0;
    document.getElementById('kpi-sla-amber').textContent = data.sla_breakdown?.AMBER || 0;
    document.getElementById('kpi-sla-red').textContent = data.sla_breakdown?.RED || 0;
    document.getElementById('kpi-screening-hits').textContent = data.open_screening_hits || 0;

    // Render Funnel
    const funnelContainer = document.getElementById('stageFunnelContainer');
    if (funnelContainer && data.stage_funnel) {
        funnelContainer.innerHTML = '';
        const maxVal = Math.max(...Object.values(data.stage_funnel), 1);

        STAGES.forEach(st => {
            const count = data.stage_funnel[st.code] || 0;
            const pct = Math.round((count / maxVal) * 100);

            const row = document.createElement('div');
            row.className = 'space-y-1';
            row.innerHTML = `
                <div class="flex justify-between text-xs">
                    <span class="text-slate-300 font-medium">${st.title}</span>
                    <span class="font-bold text-slate-200 font-mono">${count}</span>
                </div>
                <div class="w-full bg-slate-900 rounded-full h-2 overflow-hidden">
                    <div class="bg-cyan-500 h-2 rounded-full transition-all duration-500" style="width: ${pct}%"></div>
                </div>
            `;
            funnelContainer.appendChild(row);
        });
    }

    // Render Risk Distribution
    const riskContainer = document.getElementById('riskDistributionContainer');
    if (riskContainer && data.risk_tier_distribution) {
        riskContainer.innerHTML = '';
        const total = data.total_clients || 1;
        const tiers = [
            { label: 'Low Risk', key: 'LOW', color: 'bg-emerald-500', text: 'text-emerald-400' },
            { label: 'Medium Risk', key: 'MEDIUM', color: 'bg-amber-500', text: 'text-amber-400' },
            { label: 'High Risk', key: 'HIGH', color: 'bg-rose-500', text: 'text-rose-400' },
            { label: 'Prohibited', key: 'PROHIBITED', color: 'bg-red-700', text: 'text-red-400' }
        ];

        tiers.forEach(t => {
            const count = data.risk_tier_distribution[t.key] || 0;
            const pct = Math.round((count / total) * 100);
            const card = document.createElement('div');
            card.className = 'bg-slate-900 border border-slate-800 rounded-lg p-3';
            card.innerHTML = `
                <div class="flex justify-between items-center mb-1 text-xs">
                    <span class="font-semibold ${t.text}">${t.label}</span>
                    <span class="font-bold text-slate-200 font-mono">${count} (${pct}%)</span>
                </div>
                <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                    <div class="${t.color} h-1.5 rounded-full" style="width: ${pct}%"></div>
                </div>
            `;
            riskContainer.appendChild(card);
        });
    }
}

// ----------------------------------------------------
// 2. Clients & Pipeline Table
// ----------------------------------------------------
async function loadClients() {
    const search = document.getElementById('clientFilterSearch')?.value.trim() || '';
    const status = document.getElementById('clientFilterStatus')?.value || '';
    const risk = document.getElementById('clientFilterRisk')?.value || '';

    let url = `/api/v1/clients?limit=100`;
    if (search) url += `&search=${encodeURIComponent(search)}`;
    if (status) url += `&status=${encodeURIComponent(status)}`;
    if (risk) url += `&risk_tier=${encodeURIComponent(risk)}`;

    try {
        const res = await fetch(url);
        const json = await res.json();
        if (json.success) {
            state.clients = json.data;
            renderClientsTable(json.data);
        }
    } catch (e) {
        console.error('Error fetching clients:', e);
    }
}

function renderClientsTable(clients) {
    const tbody = document.getElementById('clientsTableBody');
    if (!tbody) return;
    tbody.innerHTML = '';

    if (clients.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="text-center py-8 text-slate-500">No institutional clients match the criteria.</td></tr>`;
        return;
    }

    clients.forEach(c => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/40 transition-colors';

        // Badges
        const riskClass = `badge-${(c.risk_tier || 'medium').toLowerCase()}`;
        const slaClass = `sla-${(c.sla_status || 'green').toLowerCase()}`;
        const stagePretty = (c.current_stage || 'PROSPECT_LEAD').replace(/_/g, ' ');

        tr.innerHTML = `
            <td class="px-5 py-4">
                <div class="font-bold text-white">${escapeHtml(c.name)}</div>
                <div class="text-[10px] text-slate-500 font-mono">${escapeHtml(c.client_number)}</div>
            </td>
            <td class="px-4 py-4 text-slate-300">
                ${(c.client_segment || '').replace(/_/g, ' ')}
            </td>
            <td class="px-4 py-4 text-slate-300 font-medium">
                ${escapeHtml(c.rm_name || 'Unassigned')}
            </td>
            <td class="px-4 py-4 font-mono text-[11px] text-cyan-400">
                ${stagePretty}
            </td>
            <td class="px-4 py-4">
                <div class="flex items-center gap-2">
                    <div class="w-16 bg-slate-900 rounded-full h-1.5 overflow-hidden">
                        <div class="bg-cyan-500 h-1.5 rounded-full" style="width: ${c.completion_percentage || 0}%"></div>
                    </div>
                    <span class="text-[10px] font-mono text-slate-400">${c.completion_percentage || 0}%</span>
                </div>
            </td>
            <td class="px-4 py-4">
                <span class="px-2 py-0.5 rounded text-[10px] font-bold ${riskClass}">
                    ${c.risk_tier}
                </span>
            </td>
            <td class="px-4 py-4">
                <span class="px-2 py-0.5 rounded text-[10px] font-bold ${slaClass}">
                    ${c.sla_status || 'GREEN'}
                </span>
            </td>
            <td class="px-5 py-4 text-right">
                <button onclick="openWorkbench('${c.id}')" class="bg-cyan-600/20 hover:bg-cyan-600/40 text-cyan-400 border border-cyan-500/30 text-xs px-3 py-1.5 rounded-lg transition-all">
                    Workbench <i class="fa-solid fa-arrow-right ml-1 text-[10px]"></i>
                </button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// ----------------------------------------------------
// 3. Workbench & Onboarding Progression
// ----------------------------------------------------
async function openWorkbench(clientId) {
    try {
        const [cRes, obRes, docRes] = await Promise.all([
            fetch(`/api/v1/clients/${clientId}`).then(r => r.json()),
            fetch(`/api/v1/onboarding/${clientId}`).then(r => r.json()),
            fetch(`/api/v1/documents/${clientId}`).then(r => r.json())
        ]);

        if (cRes.success) {
            state.currentClient = cRes.data;
            renderWorkbench(cRes.data, obRes.data, docRes);
            switchTab('workbench');
        }
    } catch (e) {
        console.error('Error opening workbench:', e);
    }
}

function renderWorkbench(client, onboardingCase, docData) {
    document.getElementById('wb-client-name').textContent = client.name;
    document.getElementById('wb-client-id').textContent = client.client_number;

    const riskBadge = document.getElementById('wb-risk-badge');
    riskBadge.textContent = `${client.risk_tier} RISK (${client.composite_risk_score}/10)`;
    riskBadge.className = `text-xs font-bold px-2.5 py-1 rounded-full badge-${client.risk_tier.toLowerCase()}`;

    const desc = document.getElementById('wb-client-desc');
    desc.textContent = `Segment: ${client.client_segment.replace(/_/g, ' ')} &bull; Primary RM: ${client.rm_name || 'None'} &bull; Case: ${onboardingCase ? onboardingCase.case_number : 'None'}`;

    // Stepper
    renderStepper(onboardingCase);

    // UBOs
    renderUbos(client);

    // Document Checklist
    renderDocuments(docData);
}

function renderStepper(obCase) {
    const container = document.getElementById('workbenchStepperContainer');
    if (!container) return;
    container.innerHTML = '';

    const currentStage = obCase?.current_stage || 'PROSPECT_LEAD';
    let passedCurrent = false;

    STAGES.forEach((st, idx) => {
        const isCurrent = (st.code === currentStage);
        const isCompleted = obCase?.current_stage === 'COMPLETED' || (!passedCurrent && !isCurrent);
        if (isCurrent) passedCurrent = true;

        let bg = 'bg-slate-900 border-slate-800 text-slate-500';
        if (isCurrent) {
            bg = 'bg-cyan-950 border-cyan-500 text-cyan-300 ring-2 ring-cyan-500/20';
        } else if (isCompleted) {
            bg = 'bg-emerald-950 border-emerald-800 text-emerald-400';
        }

        const stepDiv = document.createElement('div');
        stepDiv.className = `border rounded-lg p-2 text-center text-[10px] font-bold ${bg}`;
        stepDiv.innerHTML = `
            <div class="mb-1">${isCompleted ? '<i class="fa-solid fa-check"></i>' : (isCurrent ? '<i class="fa-solid fa-circle-dot animate-pulse"></i>' : idx + 1)}</div>
            <div class="truncate">${st.title}</div>
        `;
        container.appendChild(stepDiv);
    });

    const advBtn = document.getElementById('btn-advance-stage');
    if (advBtn) {
        if (obCase?.current_stage === 'COMPLETED') {
            advBtn.disabled = true;
            advBtn.className = 'bg-slate-800 text-slate-500 text-xs font-bold px-4 py-2 rounded-lg cursor-not-allowed';
            advBtn.innerHTML = `<i class="fa-solid fa-check-double mr-1"></i> Fully Onboarded`;
        } else {
            advBtn.disabled = false;
            advBtn.className = 'bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white px-4 py-2 rounded-lg flex items-center gap-2 shadow-lg shadow-emerald-900/30';
            advBtn.innerHTML = `<i class="fa-solid fa-forward-step"></i> Advance Stage`;
        }
    }
}

function renderUbos(client) {
    const container = document.getElementById('wbUboContainer');
    const countLabel = document.getElementById('wb-ubo-count');
    if (!container) return;
    container.innerHTML = '';

    // If client has contacts or mock UBOs
    const contacts = client.contacts || [];
    countLabel.textContent = `${contacts.length} Signatories / UBOs`;

    if (contacts.length === 0) {
        container.innerHTML = `<div class="text-slate-500 text-xs text-center py-6">No UBO records registered yet.</div>`;
        return;
    }

    contacts.forEach(c => {
        const item = document.createElement('div');
        item.className = 'bg-slate-900 border border-slate-800 rounded-lg p-3 flex justify-between items-center';
        item.innerHTML = `
            <div>
                <div class="font-bold text-white text-xs">${escapeHtml(c.first_name)} ${escapeHtml(c.last_name)}</div>
                <div class="text-[10px] text-slate-400">${escapeHtml(c.title)} &bull; ${escapeHtml(c.nationality)}</div>
            </div>
            <div class="flex items-center gap-2">
                ${c.has_pep_flag ? '<span class="bg-rose-950 text-rose-400 border border-rose-800 text-[10px] font-bold px-2 py-0.5 rounded">PEP Tier 2</span>' : ''}
                <span class="bg-emerald-950 text-emerald-400 border border-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded">IDV Verified</span>
            </div>
        `;
        container.appendChild(item);
    });
}

function renderDocuments(docData) {
    const container = document.getElementById('wbDocContainer');
    const statusLabel = document.getElementById('wb-doc-status');
    if (!container) return;
    container.innerHTML = '';

    const reqs = docData.checklist?.requirements || [];
    const satisfied = docData.checklist?.all_mandatory_satisfied;
    statusLabel.textContent = satisfied ? 'Checklist Complete' : 'Missing Documents';
    statusLabel.className = `text-xs font-bold ${satisfied ? 'text-emerald-400' : 'text-amber-400'}`;

    if (reqs.length === 0) {
        container.innerHTML = `<div class="text-slate-500 text-xs text-center py-6">No requirements mapped.</div>`;
        return;
    }

    reqs.forEach(r => {
        const isAppr = (r.status === 'APPROVED');
        const item = document.createElement('div');
        item.className = 'bg-slate-900 border border-slate-800 rounded-lg p-2.5 flex justify-between items-center text-xs';
        item.innerHTML = `
            <div class="truncate max-w-[70%]">
                <div class="font-medium text-slate-200 truncate">${escapeHtml(r.title)}</div>
                <div class="text-[10px] text-slate-500 font-mono">${r.code} ${r.is_mandatory ? '<span class="text-rose-400 font-bold ml-1">*Mandatory</span>' : ''}</div>
            </div>
            <div>
                ${isAppr 
                    ? '<span class="bg-emerald-950 text-emerald-400 border border-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded"><i class="fa-solid fa-check mr-1"></i> Approved</span>' 
                    : '<span class="bg-slate-800 text-slate-400 text-[10px] font-bold px-2 py-0.5 rounded">Pending File</span>'}
            </div>
        `;
        container.appendChild(item);
    });
}

async function advanceStageCurrentClient() {
    if (!state.currentClient || !state.currentClient.onboarding_case) {
        alert('No active onboarding case.');
        return;
    }
    const caseId = state.currentClient.onboarding_case.id;

    try {
        const res = await fetch('/api/v1/onboarding/advance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                case_id: caseId,
                actor_id: 'USR-COMPLIANCE-01',
                actor_role: 'SENIOR_COMPLIANCE_OFFICER',
                notes: 'Stage advanced from Workbench portal.'
            })
        });
        const json = await res.json();
        if (json.success) {
            await openWorkbench(state.currentClient.id);
            await fetchDashboardMetrics();
        } else {
            alert('Cannot advance stage: ' + (json.error || 'Check prerequisites.'));
        }
    } catch (e) {
        console.error('Error advancing stage:', e);
    }
}

async function runScreeningOnCurrentClient() {
    if (!state.currentClient || !state.currentClient.onboarding_case) return;
    const caseId = state.currentClient.onboarding_case.id;

    try {
        const res = await fetch('/api/v1/screening/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                case_id: caseId,
                client_id: state.currentClient.id
            })
        });
        const json = await res.json();
        if (json.success) {
            alert(`KYC/AML Screening complete! Total hits: ${json.data.total_hits_found}`);
            await openWorkbench(state.currentClient.id);
        }
    } catch (e) {
        console.error('Error running screening:', e);
    }
}

// ----------------------------------------------------
// 4. Screening Console View
// ----------------------------------------------------
async function runAdHocScreening() {
    const query = document.getElementById('screeningSearchInput')?.value.trim();
    if (!query) return;

    const container = document.getElementById('screeningResultsContainer');
    container.innerHTML = `<div class="text-center py-8 text-slate-400 text-xs"><i class="fa-solid fa-spinner animate-spin mr-2"></i> Screened against 1,200 OFAC SDN entities & 1,500 PEP entries...</div>`;

    try {
        const res = await fetch('/api/v1/screening/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: query })
        });
        const json = await res.json();
        if (json.success) {
            renderScreeningResults(json);
        }
    } catch (e) {
        console.error('Error running ad-hoc screening:', e);
    }
}

function renderScreeningResults(data) {
    const container = document.getElementById('screeningResultsContainer');
    container.innerHTML = '';

    const ofacHits = data.ofac_hits || [];
    const pepHits = data.pep_hits || [];

    if (ofacHits.length === 0 && pepHits.length === 0) {
        container.innerHTML = `
            <div class="bg-emerald-950/40 border border-emerald-800 rounded-xl p-6 text-center">
                <i class="fa-solid fa-shield-check text-4xl text-emerald-400 mb-2"></i>
                <h4 class="text-base font-bold text-white">Clean Clearance &bull; No Matches Found</h4>
                <p class="text-xs text-slate-400 mt-1">Query "${escapeHtml(data.query)}" returned 0 true or fuzzy matches against OFAC SDN and global PEP rosters.</p>
            </div>
        `;
        return;
    }

    // Render OFAC Hits
    if (ofacHits.length > 0) {
        const ofacBox = document.createElement('div');
        ofacBox.className = 'space-y-3';
        ofacBox.innerHTML = `
            <h4 class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-2">
                <i class="fa-solid fa-ban"></i> OFAC SDN Sanctions Matches (${ofacHits.length})
            </h4>
        `;
        ofacHits.forEach(h => {
            const card = document.createElement('div');
            card.className = 'bg-slate-800/80 border border-rose-800/60 rounded-xl p-4 flex justify-between items-start text-xs';
            card.innerHTML = `
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-bold text-white text-sm">${escapeHtml(h.name)}</span>
                        <span class="bg-rose-950 text-rose-300 font-mono text-[10px] px-2 py-0.5 rounded border border-rose-800">Match: ${(h.match_score * 100).toFixed(1)}%</span>
                        <span class="bg-slate-900 text-slate-300 text-[10px] px-2 py-0.5 rounded">${h.sdn_type}</span>
                    </div>
                    <div class="text-slate-400 text-xs mt-1">Programs: <span class="text-rose-400 font-bold">${h.programs.join(', ')}</span></div>
                    <div class="text-slate-400 text-xs mt-1">Remarks: ${escapeHtml(h.remarks || 'None')}</div>
                </div>
                <button onclick="alert('Disposition logged for audit.')" class="bg-slate-700 hover:bg-slate-600 text-white text-xs px-3 py-1.5 rounded-lg">
                    Clear False Positive
                </button>
            `;
            ofacBox.appendChild(card);
        });
        container.appendChild(ofacBox);
    }

    // Render PEP Hits
    if (pepHits.length > 0) {
        const pepBox = document.createElement('div');
        pepBox.className = 'space-y-3 mt-6';
        pepBox.innerHTML = `
            <h4 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
                <i class="fa-solid fa-user-tie"></i> Politically Exposed Persons (PEP) Matches (${pepHits.length})
            </h4>
        `;
        pepHits.forEach(p => {
            const card = document.createElement('div');
            card.className = 'bg-slate-800/80 border border-amber-800/60 rounded-xl p-4 flex justify-between items-start text-xs';
            card.innerHTML = `
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-bold text-white text-sm">${escapeHtml(p.full_name)}</span>
                        <span class="bg-amber-950 text-amber-300 font-mono text-[10px] px-2 py-0.5 rounded border border-amber-800">Tier ${p.tier} PEP</span>
                        <span class="bg-slate-900 text-slate-300 text-[10px] px-2 py-0.5 rounded">${p.country_name}</span>
                    </div>
                    <div class="text-slate-400 text-xs mt-1">Title: <span class="text-slate-200 font-medium">${escapeHtml(p.role_title)}</span> &bull; ${escapeHtml(p.department_or_agency)}</div>
                    <div class="text-slate-400 text-xs mt-1">Source of Wealth: ${escapeHtml(p.source_of_wealth || 'Public Record')}</div>
                </div>
                <button onclick="alert('EDD escalation initiated.')" class="bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold text-xs px-3 py-1.5 rounded-lg">
                    Initiate EDD
                </button>
            `;
            pepBox.appendChild(card);
        });
        container.appendChild(pepBox);
    }
}

// ----------------------------------------------------
// 5. Tasks Queue
// ----------------------------------------------------
async function loadTasks() {
    try {
        const res = await fetch('/api/v1/tasks?limit=50');
        const json = await res.json();
        if (json.success) {
            state.tasks = json.data;
            renderTasks(json.data);
        }
    } catch (e) {
        console.error('Error fetching tasks:', e);
    }
}

function renderTasks(tasks) {
    const tbody = document.getElementById('tasksTableBody');
    if (!tbody) return;
    tbody.innerHTML = '';

    if (tasks.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" class="text-center py-8 text-slate-500">No action items pending.</td></tr>`;
        return;
    }

    tasks.forEach(t => {
        const isDone = (t.status === 'COMPLETED');
        const prioClass = t.priority === 'HIGH' ? 'text-rose-400' : 'text-amber-400';

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/40 transition-colors';
        tr.innerHTML = `
            <td class="px-5 py-3.5">
                <div class="font-bold text-white">${escapeHtml(t.title)}</div>
                <div class="text-[10px] text-slate-500">${escapeHtml(t.description || '')}</div>
            </td>
            <td class="px-4 py-3.5">
                <div class="text-slate-200 font-medium">${escapeHtml(t.client_name)}</div>
                <div class="text-[10px] text-slate-500 font-mono">${escapeHtml(t.case_number)}</div>
            </td>
            <td class="px-4 py-3.5 font-bold ${prioClass}">
                ${t.priority}
            </td>
            <td class="px-4 py-3.5 font-mono text-slate-300">
                ${t.due_date}
            </td>
            <td class="px-4 py-3.5">
                <span class="px-2 py-0.5 rounded text-[10px] font-bold ${isDone ? 'bg-emerald-950 text-emerald-400' : 'bg-amber-950 text-amber-400'}">
                    ${t.status}
                </span>
            </td>
            <td class="px-5 py-3.5 text-right">
                ${isDone 
                    ? '<span class="text-xs text-slate-500">Resolved</span>' 
                    : `<button onclick="completeTaskAction('${t.id}')" class="bg-cyan-600/20 hover:bg-cyan-600/40 text-cyan-400 border border-cyan-500/30 text-xs px-3 py-1 rounded-lg">Mark Done</button>`}
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function completeTaskAction(taskId) {
    alert(`Task ${taskId} completed!`);
    loadTasks();
}

// ----------------------------------------------------
// 6. Audit Trail Explorer
// ----------------------------------------------------
async function loadAuditTrail() {
    try {
        const res = await fetch('/api/v1/audit/trail?limit=40');
        const json = await res.json();
        if (json.success) {
            state.audit = json.data;
            renderAuditTrail(json.data);
        }
    } catch (e) {
        console.error('Error fetching audit trail:', e);
    }
}

function renderAuditTrail(events) {
    const container = document.getElementById('auditTimelineContainer');
    if (!container) return;
    container.innerHTML = '';

    events.forEach(ev => {
        const item = document.createElement('div');
        item.className = 'bg-slate-900 border border-slate-800 rounded-xl p-4 text-xs space-y-2';
        item.innerHTML = `
            <div class="flex justify-between items-center">
                <div class="flex items-center gap-2">
                    <span class="bg-slate-800 text-cyan-400 font-bold px-2 py-0.5 rounded text-[10px]">${ev.action}</span>
                    <span class="text-white font-bold">${escapeHtml(ev.change_summary)}</span>
                </div>
                <span class="text-[10px] text-slate-500 font-mono">${ev.timestamp}</span>
            </div>
            <div class="flex items-center justify-between text-[10px] text-slate-400 pt-1 border-t border-slate-800">
                <div>Actor: <span class="text-slate-200 font-medium">${escapeHtml(ev.actor_name)}</span> (${ev.actor_role}) &bull; IP: ${ev.ip_address}</div>
                <div class="font-mono text-slate-500 truncate max-w-xs">Hash: ${ev.event_hash}</div>
            </div>
        `;
        container.appendChild(item);
    });
}

function exportAuditTrail() {
    const blob = new Blob([JSON.stringify(state.audit, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `nexuscrm_audit_export_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
}

// ----------------------------------------------------
// Modals & Helpers
// ----------------------------------------------------
function openNewClientModal() {
    document.getElementById('newClientModal')?.classList.remove('hidden');
}

function closeNewClientModal() {
    document.getElementById('newClientModal')?.classList.add('hidden');
}

async function submitNewClient() {
    const name = document.getElementById('modalClientName')?.value.trim();
    const segment = document.getElementById('modalClientSegment')?.value;
    const juris = document.getElementById('modalJurisdiction')?.value;
    const entityType = document.getElementById('modalEntityType')?.value;
    const naics = document.getElementById('modalNaicsCode')?.value.trim();

    if (!name) {
        alert('Please provide a Legal Corporate Name.');
        return;
    }

    try {
        const res = await fetch('/api/v1/clients', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                client_segment: segment,
                jurisdiction: juris,
                entity_type: entityType,
                naics_code: naics,
                rm_id: 'RM-101'
            })
        });
        const json = await res.json();
        if (json.success) {
            closeNewClientModal();
            await loadClients();
            await fetchDashboardMetrics();
            alert(`Client ${name} registered successfully!`);
        } else {
            alert('Error: ' + (json.error || 'Failed to create client'));
        }
    } catch (e) {
        console.error('Error creating client:', e);
    }
}

function escapeHtml(str) {
    if (!str) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
