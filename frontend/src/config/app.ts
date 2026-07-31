export const appConfig = {
  name: "Beeta Lab",
  description:
    "AI-powered Historical Intelligence Platform for creators and researchers.",

  api: {
    baseUrl:
      process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000",
  },

  app: {
    version: "0.1.0",
  },
} as const;