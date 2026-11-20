import type { MarketCode } from "../types/market";

/**
 * Which market this dashboard serves. The US and India apps are separate
 * repositories; this is the India app (default IN).
 */
const raw = String(import.meta.env.VITE_APP_MARKET ?? "IN").toUpperCase();

export const APP_MARKET: MarketCode = raw === "US" ? "US" : "IN";

/** Markets shown in the market tabs. */
export const APP_MARKETS: MarketCode[] = [APP_MARKET];
