import { apiClient } from "@/lib/api/client";
import type { HealthResponse } from "@/types/api";

export async function getHealth(): Promise<HealthResponse> {
  const response = await apiClient.get<HealthResponse>("/api/health");
  return response.data;
}