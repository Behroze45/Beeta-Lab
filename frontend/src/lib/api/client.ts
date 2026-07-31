import axios from "axios";

import { appConfig } from "@/config/app";

export const apiClient = axios.create({
  baseURL: appConfig.api.baseUrl,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 10000,
});