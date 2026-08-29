"""
MiFID II / MiFIR Investor Categorization, Appropriateness & Suitability Matrix.
Classifies institutional and wealth clients and enforces complex financial product risk limits.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any

@dataclass
class AssetClassComplexity:
    code: str
    name: str
    is_complex: bool
    minimum_client_category: str
    leverage_multiplier_cap: float
    target_market_summary: str

ASSET_CLASSES: Dict[str, AssetClassComplexity] = {
    "GOV_BONDS": AssetClassComplexity(
        code="GOV_BONDS",
        name="Government Sovereign Bonds",
        is_complex=False,
        minimum_client_category="RETAIL",
        leverage_multiplier_cap=1.0,
        target_market_summary="Conservative capital preservation investors"
    ),
    "CORP_BONDS_IG": AssetClassComplexity(
        code="CORP_BONDS_IG",
        name="Investment Grade Corporate Debt",
        is_complex=False,
        minimum_client_category="RETAIL",
        leverage_multiplier_cap=1.5,
        target_market_summary="Income-seeking conservative to balanced investors"
    ),
    "EQUITY_CASH": AssetClassComplexity(
        code="EQUITY_CASH",
        name="Cash Equities (Large & Mid Cap)",
        is_complex=False,
        minimum_client_category="RETAIL",
        leverage_multiplier_cap=2.0,
        target_market_summary="Capital growth investors with moderate volatility tolerance"
    ),
    "UCITS_ETF": AssetClassComplexity(
        code="UCITS_ETF",
        name="Physical Plain-Vanilla ETFs",
        is_complex=False,
        minimum_client_category="RETAIL",
        leverage_multiplier_cap=2.0,
        target_market_summary="Broad market diversification with low total expense ratio"
    ),
    "CORP_BONDS_HY": AssetClassComplexity(
        code="CORP_BONDS_HY",
        name="High Yield Sub-Investment Grade Debt",
        is_complex=True,
        minimum_client_category="ELECTIVE_PROFESSIONAL",
        leverage_multiplier_cap=3.0,
        target_market_summary="High income investors accepting credit default risk"
    ),
    "FX_SPOT": AssetClassComplexity(
        code="FX_SPOT",
        name="Foreign Currency Spot Deliverable",
        is_complex=False,
        minimum_client_category="RETAIL",
        leverage_multiplier_cap=5.0,
        target_market_summary="Hedging or liquidity management for treasury clients"
    ),
    "FX_DERIVATIVES": AssetClassComplexity(
        code="FX_DERIVATIVES",
        name="OTC FX Forwards, Swaps, & Options",
        is_complex=True,
        minimum_client_category="ELECTIVE_PROFESSIONAL",
        leverage_multiplier_cap=20.0,
        target_market_summary="Corporate treasury hedging and currency speculation"
    ),
    "INTEREST_RATE_SWAPS": AssetClassComplexity(
        code="INTEREST_RATE_SWAPS",
        name="OTC Interest Rate Swaps & Swaptions",
        is_complex=True,
        minimum_client_category="PER_SE_PROFESSIONAL",
        leverage_multiplier_cap=30.0,
        target_market_summary="Institutional balance sheet asset-liability hedging"
    ),
    "CREDIT_DEFAULT_SWAPS": AssetClassComplexity(
        code="CREDIT_DEFAULT_SWAPS",
        name="Single Name & Index CDS",
        is_complex=True,
        minimum_client_category="PER_SE_PROFESSIONAL",
        leverage_multiplier_cap=25.0,
        target_market_summary="Institutional credit protection hedging and macro directional exposure"
    ),
    "COMMODITY_FUTURES": AssetClassComplexity(
        code="COMMODITY_FUTURES",
        name="Exchange Traded Commodity Futures",
        is_complex=True,
        minimum_client_category="ELECTIVE_PROFESSIONAL",
        leverage_multiplier_cap=15.0,
        target_market_summary="Producers, refiners, and active speculative trading desks"
    ),
    "STRUCTURED_NOTES": AssetClassComplexity(
        code="STRUCTURED_NOTES",
        name="Capital Protected & Reverse Convertible Notes",
        is_complex=True,
        minimum_client_category="ELECTIVE_PROFESSIONAL",
        leverage_multiplier_cap=2.0,
        target_market_summary="Wealth clients seeking asymmetric yield structures"
    ),
    "PRIVATE_EQUITY": AssetClassComplexity(
        code="PRIVATE_EQUITY",
        name="Private Equity Direct Co-investments",
        is_complex=True,
        minimum_client_category="PER_SE_PROFESSIONAL",
        leverage_multiplier_cap=1.0,
        target_market_summary="Illiquid long-term capital allocation for qualified institutions"
    ),
}


def evaluate_mifid_client_category(
    balance_sheet_total_eur: float,
    net_turnover_eur: float,
    own_funds_eur: float,
    is_regulated_financial_institution: bool = False
) -> str:
    if is_regulated_financial_institution:
        return "PER_SE_PROFESSIONAL"

    conditions_met = 0
    if balance_sheet_total_eur >= 20_000_000:
        conditions_met += 1
    if net_turnover_eur >= 40_000_000:
        conditions_met += 1
    if own_funds_eur >= 2_000_000:
        conditions_met += 1

    if conditions_met >= 2:
        return "PER_SE_PROFESSIONAL"
    return "RETAIL"
